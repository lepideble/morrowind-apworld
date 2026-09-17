import re
import collections

from ..data.classes import DialogueLocationData
from ..data.items import items
from ..data.regions import location_name_to_data, location_name_to_id
from ..lib.records import Records


def get_dialogue_data() -> dict:
    dialogue_data = collections.defaultdict(lambda: collections.defaultdict(list))

    for (location_name, (region_data, location_data, original_item)) in location_name_to_data.items():
        if not isinstance(location_data, DialogueLocationData):
            continue

        location_id = location_name_to_id[location_name]

        if isinstance(location_data.response_id, list):
            response_ids = location_data.response_id
        else:
            response_ids = [location_data.response_id]

        for response_id in response_ids:
            dialogue_data[location_data.topic][response_id].append({
                'item_id': f'ap_{location_id}',
                'original_item_id': items[original_item].recordId,
            })

    return dialogue_data


def patch_dialogue_records(records: Records):
    for topic, responses_data in get_dialogue_data().items():
        for response_id, items_data in responses_data.items():
            for item_data in items_data:
                records.items[item_data['item_id']] = {
                    'type': 'MiscItem',
                    'flags': '',
                    'name': 'Archipelago Item',
                    'script': '',
                    'mesh': 'm\\Gold_001.NIF',
                    'icon': 'm\\Tx_Gold_001.tga',
                    'data': {
                        'weight': 0.0,
                        'value': 0,
                        'flags': '',
                    },
                }

            original_record = records.topics[topic][response_id]

            script_text = original_record['script_text']
            for item_data in items_data:
                script_text = re.sub(
                    f'Player->AddItem[, "]+{item_data['original_item_id']}[, "]+[0-9]+',
                    f'Player->AddItem {item_data['item_id']} 1',
                    script_text,
                    flags=re.IGNORECASE,
                )

            records.topics[topic][response_id] = {
                **original_record,
                'script_text': script_text,
            }
