import collections

from ..data.classes import PickableItemLocationData
from ..data.items import items
from ..data.regions import location_name_to_data, location_name_to_id
from ..lib.records import Records


def get_cells_data() -> dict:
    cells_data = collections.defaultdict(list)

    for (location_name, (region_data, location_data, original_item)) in location_name_to_data.items():
        if not isinstance(location_data, PickableItemLocationData):
            continue

        location_id = location_name_to_id[location_name]

        cells_data[location_data.cell].append({
            'item_id': f'ap_{location_id}',
            'original_item_id': items[original_item].recordId,
        })

    return cells_data


def patch_cells_records(records: Records):
    for cell, items in get_cells_data().items():
        for item_data in items:
            original_record = records.items[item_data['original_item_id']]

            records.items[item_data['item_id']] = {
                'type': 'MiscItem',
                'flags': '',
                'name': 'Archipelago Item',
                'script': original_record['script'],
                'mesh': original_record['mesh'],
                'icon': 'm\\Tx_Gold_001.tga',
                'data': {
                    'weight': 0.0,
                    'value': 0,
                    'flags': '',
                },
            }

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
