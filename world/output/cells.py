from collections import defaultdict

from ..items import items
from ..locations import PickableItemLocationData
from ..regions import location_name_to_data
from .records import Records


def get_cells_data(world) -> dict:
    cells_data = defaultdict(list)

    for location in world.get_locations():
        if location.address is None:
            continue

        region_data, location_data, original_item = location_name_to_data[location.name]

        if not isinstance(location_data, PickableItemLocationData):
            continue

        item = location.item

        if location.player == item.player:
            item_name = item.name
        else:
            item_name = f"{world.multiworld.get_player_name(item.player)}'s {item.name}"

        cells_data[location_data.cell].append({
            'item_id': f'ap_{location.address}',
            'item_name': item_name,
            'original_item_id': items[original_item].recordId,
        })

    return cells_data


def patch_cells_records(records: Records, cells_data: dict) -> list:
    for cell, items in cells_data.items():
        for item_data in items:
            original_record = records.items[item_data['original_item_id']]

            records.items[item_data['item_id']] = {
                'type': 'MiscItem',
                'flags': '',
                'name': item_data['item_name'],
                'script': original_record['script'],
                'mesh': original_record['mesh'],
                'icon': 'm\\Tx_Gold_001.tga',
                'data': {
                    'weight': 0.0,
                    'value': 0,
                    'flags': '',
                },
            }

    for cell, items in cells_data.items():
        original_record = records.cells[cell]

        record = {
            'type': 'Cell',
            'flags': original_record['flags'],
            'name': original_record['name'],
            'data': original_record['data'],
            'references': [],
        }

        for item_data in items:
            original_reference = next(reference for reference in original_record['references'] if reference['id'] == item_data['original_item_id'])

            record['references'].append({
                'mast_index': original_reference['mast_index'] + 1,
                'refr_index': original_reference['refr_index'],
                'id': item_data['item_id'],
                'temporary': original_reference['temporary'],
                'translation': original_reference['translation'],
                'rotation': original_reference['rotation'],
            })

        records.cells[cell] = record

    return records
