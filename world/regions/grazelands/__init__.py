from rule_builder.rules import True_

from . import tel_vos, zainab_camp


name = 'Grazelands region'


exits = [
    # Sub-regions
    ('Tel Vos', True_()),
    ('Zainab Camp', True_()),
    # Neighbouring regions
    ('Ashlands region', True_()),
    ('Azura\'s Coast region', True_()),
    ('Molag Amur region', True_()),
    ('Sheogorad region', True_()),
]


regions = [
    tel_vos,
    zainab_camp,
]
