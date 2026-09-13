from rule_builder.rules import True_

from . import arkngthand, erabenimsun_camp


name = 'Molag Amur region'


exits = [
    # Sub-regions
    ('Arkngthand', True_()),
    ('Erabenimsun Camp', True_()),
    # Neighbouring regions
    ('Ashlands region', True_()),
    ('Grazelands region', True_()),
    ('Azura\'s Coast region', True_()),
    ('Ascadian Isles region', True_()),
    ('West Gash region', True_()),
]


regions = [
    arkngthand,
    erabenimsun_camp,
]
