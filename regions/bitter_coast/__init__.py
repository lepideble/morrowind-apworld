from rule_builder.rules import True_

from . import andrano_ancestral_tomb, ilunibi, seyda_neen


name = 'Bitter Coast region'


exits = [
    # Sub-regions
    ('Andrano Ancestral Tomb', True_()),
    ('Ilunibi', True_()),
    ('Seyda Neen', True_()),
    # Neighbouring regions
    ('Ascadian Isles region', True_()),
    ('West Gash region', True_()),
]


regions = [
    andrano_ancestral_tomb,
    ilunibi,
    seyda_neen,
]
