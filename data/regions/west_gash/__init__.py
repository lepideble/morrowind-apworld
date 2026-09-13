from rule_builder.rules import True_

from . import balmora


name = 'West Gash region'


exits = [
    # Sub-regions
    ('Balmora', True_()),
    # Neighbouring regions
    ('Ascadian Isles region', True_()),
    ('Ashlands region', True_()),
    ('Bitter Coast region', True_()),
    ('Molag Amur region', True_()),
    ('Sheogorad region', True_()),
]


regions = [
    balmora,
]
