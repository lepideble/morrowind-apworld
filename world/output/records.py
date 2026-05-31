from collections.abc import Mapping


item_types = ('Armor', 'MiscItem')


class Cells:
    records: list
    data: dict[str, dict]

    def __init__(self, records: list):
        self.records = records
        self.data = {}

    def __getitem__(self, key) -> dict:
        if key in self.data:
            return self.data[key]
        else:
            return next(record for record in self.records if record['type'] == 'Cell' and record['name'] == key)

    def __setitem__(self, key: str, value: dict):
        self.data[key] = value

    def get_records(self) -> list:
        return [{**value, 'id': key} for key, value in self.data.items()]


class Items:
    records: list
    data: dict[str, dict]

    def __init__(self, records: list):
        self.records = records
        self.data = {}

    def __getitem__(self, key) -> dict:
        if key in self.data:
            return self.data[key]
        else:
            return next(record for record in self.records if record['type'] in item_types and record['id'] == key)

    def __setitem__(self, key: str, value: dict):
        self.data[key] = value

    def get_records(self) -> list:
        return [{**value, 'id': key} for key, value in self.data.items()]


class Dialogue(Mapping):
    records: list
    data: dict[str, dict]

    def __init__(self, records: list = []):
        self.records = records
        self.data = {}

    def __getitem__(self, key: str) -> dict:
        if key in self.data:
            return self.data[key]
        else:
            try:
                return next(record for record in self.records if record['id'] == key)
            except StopIteration:
                raise KeyError(key) from None

    def __setitem__(self, key: str, value: dict):
        self.data[key] = value

    def __iter__(self):
        return (record['id'] for record in self.records)

    def __len__(self):
        return len(self.records)

    def __iter__(self):
        return


class Dialogues(Mapping):
    records: list
    data: dict[str, Dialogue]
    dialogue_type: str

    def __init__(self, records: list, dialogue_type: str):
        self.records = records
        self.data = {}
        self.dialogue_type = dialogue_type

    def __getitem__(self, key: str) -> Dialogue:
        if key not in self.data:
            records = []
            current_topic = None
            for record in self.records:
                if record['type'] == 'Dialogue' and record['dialogue_type'] == self.dialogue_type:
                    current_topic = record['id']
                if record['type'] == 'DialogueInfo' and record['data']['dialogue_type'] == self.dialogue_type:
                    if current_topic == key:
                        records.append(record)

            self.data[key] = Dialogue(records)

        return self.data[key]

    def __setitem__(self, key: str, value: Dialogue):
        self.data[key] = value

    def __iter__(self):
        return (record['id'] for record in self.records if record['type'] == 'Dialogue' and record['dialogue_type'] == self.dialogue_type)

    def __len__(self):
        return sum(1 for _ in self.__iter__())

    def get_records(self) -> list:
        records = []

        for dialogue_id, dialogue in self.data.items():
            if len(dialogue.data) == 0:
                continue

            records.append({
                'type': 'Dialogue',
                'flags': '',
                'id': dialogue_id,
                'dialogue_type': self.dialogue_type,
            })

            for key, value in dialogue.data.items():
                records.append({ **value, 'id': key })

        return records


class Journal(Dialogue):
    def __init__(self):
        super().__init__([])


class Records:
    cells: Cells
    items: Items
    journals: Dialogues
    greetings: Dialogues
    topics: Dialogues

    def __init__(self, records: list):
        self.cells = Cells(records)
        self.items = Items(records)
        self.journals = Dialogues(records, 'Journal')
        self.greetings = Dialogues(records, 'Greeting')
        self.topics = Dialogues(records, 'Topic')

    def get_records(self) -> list:
        return [
            *self.cells.get_records(),
            *self.items.get_records(),
            *self.journals.get_records(),
            *self.greetings.get_records(),
            *self.topics.get_records(),
        ]
