from rule_builder.rules import True_

from . import dagoth_ur, odrosal, vemynal


name = 'Red Mountain region'


exits = [
    # Sub-regions
    ('Dagoth Ur', True_()),
    ('Odrosal', True_()),
    ('Vemynal', True_()),
    # Neighbouring regions
    ('Ashlands region', True_()),
]


regions = [
    dagoth_ur,
    odrosal,
    vemynal,
]
