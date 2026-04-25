from dataclasses import dataclass, field
from itertools import count

from BaseClasses import ItemClassification


ids = count(start=1)


@dataclass
class ItemData:
    id: int = field(default_factory=lambda: next(ids), init=False)
    classification: ItemClassification
    recordId: str
    count: int = 1


items = {
    '200 Gold': ItemData(ItemClassification.filler, 'gold_001', 200),
    'Hasphat\'s notes for Cosades': ItemData(ItemClassification.progression, 'bk_a1_2_antabolistocosades'),
    'Nerevarine cult notes': ItemData(ItemClassification.progression, 'bk_a1_4_sharnsnotes')
}
