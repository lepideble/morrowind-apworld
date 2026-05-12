import re
from collections import defaultdict
from dataclasses import dataclass, field

from ..items import items
from ..locations import DialogueLocationData
from ..regions import location_name_to_data


def get_dialogue_data(world) -> dict:
    dialogue_data = defaultdict(lambda: defaultdict(list))

    for location in world.get_locations():
        if location.address is None:
            continue

        region_data, location_data, original_item = location_name_to_data[location.name]

        if not isinstance(location_data, DialogueLocationData):
            continue

        item = location.item

        if location.player == item.player:
            item_name = item.name
        else:
            item_name = f"{world.multiworld.get_player_name(item.player)}'s {item.name}"

        dialogue_data[location_data.topic_id][location_data.response_id].append({
            'item_id': f'ap_{location.address}',
            'item_name': item_name,
            'original_item_id': items[original_item].recordId,
        })

    return dialogue_data


def get_dialogue_records(morrowind_data: list, dialogue_data: dict) -> list:
    records = []

    for topic_id, responses_data in dialogue_data.items():
        for response_id, items_data in responses_data.items():
            for item_data in items_data:
                records.append({
                    'type': 'MiscItem',
                    'flags': '',
                    'id': item_data['item_id'],
                    'name': item_data['item_name'],
                    'script': '',
                    'mesh': 'm\\Gold_001.NIF',
                    'icon': 'm\\Tx_Gold_001.tga',
                    'data': {
                        'weight': 0.0,
                        'value': 0,
                        'flags': '',
                    },
                })

    for topic_id, responses_data in dialogue_data.items():
        records.append({
            'type': 'Dialogue',
            'flags': '',
            'id': topic_id,
            'dialogue_type': 'Topic',
        })

        for response_id, items_data in responses_data.items():
            original_record = next(record for record in morrowind_data if record['type'] == 'DialogueInfo' and record['id'] == response_id)

            script_text = original_record['script_text']
            for item_data in items_data:
                script_text = re.sub(
                    f'Player->AddItem[, "]+{item_data['original_item_id']}[, "]+[0-9]+',
                    f'Player->AddItem {item_data['item_id']} 1',
                    script_text,
                    flags=re.IGNORECASE,
                )

            records.append({
                **original_record,
                'script_text': script_text,
            })

    return records
