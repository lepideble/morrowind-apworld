from rule_builder.rules import True_

from . import ald_daedroth, holamayan, tel_fyr


name = 'Azura\'s Coast region'


exits = [
    # Sub-regions
    ('Ald Daedroth', True_()),
    ('Holamayan', True_()),
    ('Tel Fyr', True_()),
    # Neighbouring regions
    ('Ascadian Isles region', True_()),
    ('Molag Amur region', True_()),
    ('Grazelands region', True_()),
    ('Sheogorad region', True_()),
]


regions = [
    ald_daedroth,
    holamayan,
    tel_fyr,
]
