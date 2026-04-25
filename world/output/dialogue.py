import re

from dataclasses import dataclass, field

from ..locations import locations, DialogueLocationData


def get_dialogue_data(world) -> list:
    dialogue_data = []

    for location in world.get_locations():
        if location.address is None:
            continue

        location_data = locations[location.name]

        if not isinstance(location_data, DialogueLocationData):
            continue

        item = location.item

        if location.player == item.player:
            item_name = item.name
        else:
            item_name = f"{world.multiworld.get_player_name(item.player)}'s {item.name}"

        dialogue_data.append({
            'item_id': f'ap_{location.address}',
            'item_name': item_name,
            'topic_id': location_data.topic_id,
            'response_id': location_data.response_id,
            'original_item_id': location_data.original_item_id,
        })

    return dialogue_data


def get_dialogue_records(morrowind_data: list, dialogue_data: list) -> list:
    records = []

    for dialogue_datum in dialogue_data:
        original_record = next(
            record for record in morrowind_data
            if record['type'] == 'DialogueInfo' and record['id'] == dialogue_datum['response_id']
        )

        records.append({
            'type': 'MiscItem',
            'flags': '',
            'id': dialogue_datum['item_id'],
            'name': dialogue_datum['item_name'],
            'script': '',
            'mesh': 'm\\Gold_001.NIF',
            'icon': 'm\\Tx_Gold_001.tga',
            'data': {
                'weight': 0.0,
                'value': 0,
                'flags': '',
            },
        })
        records.append({
            'type': 'Dialogue',
            'flags': '',
            'id': dialogue_datum['topic_id'],
            'dialogue_type': 'Topic',
        })
        records.append({
            **original_record,
            'script_text': re.sub(
                f'Player->AddItem[, "]+{dialogue_datum['original_item_id']}[, "]+[0-9]+',
                f'Player->AddItem {dialogue_datum['item_id']} 1',
                original_record['script_text'],
                flags=re.IGNORECASE,
            )
        })

    return records
