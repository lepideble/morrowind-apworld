from rule_builder.rules import Has, True_

from ...quests import ThePathOfTheIncarnate
from . import ald_ruhn, cavern_of_the_incarnate, urshilaku_camp


name = 'Ashlands region'


exits = [
    # Sub-regions
    ('Ald\'ruhn', True_()),
    ('Cavern of the Incarnate', Has(ThePathOfTheIncarnate.Started)),
    ('Urshilaku Camp', True_()),
    # Neighbouring regions
    ('Grazelands region', True_()),
    ('Molag Amur region', True_()),
    ('Red Mountain region', True_()),
    ('Sheogorad region', True_()),
    ('West Gash region', True_()),
]


regions = [
    ald_ruhn,
    cavern_of_the_incarnate,
    urshilaku_camp,
]
