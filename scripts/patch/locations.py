from ..data.classes import CreatureInventory
from ..data.items import items
from ..data.regions import location_name_to_data, location_name_to_id
from ..lib.records import Records

def create_archipelago_item():
    return {
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

def patch_locations_records(records: Records):
    for (location_name, (region_data, location_data, original_item)) in location_name_to_data.items():
        location_id = location_name_to_id[location_name]
        original_item_id = items[original_item].record_id
        archipelago_item_id = f'ap_{location_id}'

        if isinstance(location_data, CreatureInventory):
            records.items[archipelago_item_id] = create_archipelago_item()

            record = records.creatures[location_data.creature_id]

            item_index = next(
                index
                for index, (count, item_id) in enumerate(record.inventory)
                if item_id == original_item_id
            )

            record.inventory[item_index] = [1, archipelago_item_id]
