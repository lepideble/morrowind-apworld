from itertools import count

from ..util import enumerate_names
from . import ald_ruhn, balmora, bitter_coast, tel_fyr, urshilaku_camp, vivec_foreign_quarter


regions = [
    ald_ruhn,
    balmora,
    bitter_coast,
    tel_fyr,
    urshilaku_camp,
    vivec_foreign_quarter,
]

location_name_to_data = {}
location_name_to_id = {}

ids = count(start=1)

for region in regions:
    for location_name, location_data in region.locations.items():
        for name, item in enumerate_names(location_name, location_data.items):
            location_name_to_data[name] = (region, location_data, item)
            location_name_to_id[name] = next(ids)

del ids
