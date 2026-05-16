from itertools import count

from ..util import enumerate_names
from . import ascadian_isles, ashlands, azuras_coast, balmora, bitter_coast, cavern_of_the_incarnate, dagoth_ur, grazelands, holamayan, molag_amur


# Gather all regions an sub regions into an unique list
regions = []

def _add_regions_recursives(regions_to_add: list):
    for region in regions_to_add:
        regions.append(region)
        if hasattr(region, 'regions'):
            _add_regions_recursives(region.regions)

_add_regions_recursives([
    ascadian_isles,
    ashlands,
    azuras_coast,
    balmora,
    bitter_coast,
    cavern_of_the_incarnate,
    dagoth_ur,
    grazelands,
    holamayan,
    molag_amur,
])


# Gather all locations
location_name_to_data = {}
location_name_to_id = {}

ids = count(start=1)

for region in regions:
    for location_name, location_data in getattr(region, 'locations', {}).items():
        for name, item in enumerate_names(location_name, location_data.items):
            location_name_to_data[name] = (region, location_data, item)
            location_name_to_id[name] = next(ids)

del ids
