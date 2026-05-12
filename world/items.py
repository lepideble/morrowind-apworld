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
    'Mission to Vivec -- from Caius': ItemData(ItemClassification.filler, 'bk_a1_v_vivecinformants'),
    'Nerevarine cult notes': ItemData(ItemClassification.progression, 'bk_a1_4_sharnsnotes'),
    'Notes from Huleeya': ItemData(ItemClassification.progression, 'bk_A1_7_HuleeyaInformant'),
}
