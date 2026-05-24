from rule_builder.rules import True_

from . import vivec_foreign_quarter, vivec_hlaalu, vivec_temple


name = 'Ascadian Isles region'


exits = [
    # Sub-regions
    ('Vivec, Foreign Quarter', True_()),
    ('Vivec, Hlaalu', True_()),
    ('Vivec, Temple', True_()),
    # Neighbouring regions
    ('Bitter Coast region', True_()),
    ('West Gash region', True_()),
    ('Molag Amur region', True_()),
    ('Azura\'s Coast region', True_()),
]


regions = [
    vivec_foreign_quarter,
    vivec_hlaalu,
    vivec_temple,
]
