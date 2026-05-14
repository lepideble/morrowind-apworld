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
    '100 Gold': ItemData(ItemClassification.filler, 'Gold_001', 100),
    '200 Gold': ItemData(ItemClassification.filler, 'Gold_001', 200),
    '400 Gold': ItemData(ItemClassification.filler, 'Gold_001', 400),
    '1000 Gold': ItemData(ItemClassification.filler, 'Gold_001', 1000),
    'Decoded package': ItemData(ItemClassification.filler, 'bk_a1_1_packagedecoded'),
    'Dwemer Boots of Flying': ItemData(ItemClassification.progression, 'dwemer_boots of flying'),
    'Dwemer Coherer': ItemData(ItemClassification.filler, 'misc_dwrv_artifact50'),
    'Hasphat\'s notes for Cosades': ItemData(ItemClassification.progression, 'bk_a1_2_antabolistocosades'),
    'Kagrenac\'s Tools': ItemData(ItemClassification.filler, 'bk_kagrenac\'stools'),
    'Mission to Vivec -- from Caius': ItemData(ItemClassification.filler, 'bk_a1_v_vivecinformants'),
    'Nerevarine cult notes': ItemData(ItemClassification.progression, 'bk_a1_4_sharnsnotes'),
    'Notes from Huleeya': ItemData(ItemClassification.progression, 'bk_A1_7_HuleeyaInformant'),
    'note from the Archcanon': ItemData(ItemClassification.filler, 'bk_saryoni_note'),
    'Public notice': ItemData(ItemClassification.filler, 'bk_NerevarineNotice'),
    '3 Quality Rising Force Potion': ItemData(ItemClassification.useful, 'P_Levitation_Q', 3),
    'Ring of the Hortator': ItemData(ItemClassification.useful, 'hortatorring'),
    'The Lost Prophecy': ItemData(ItemClassification.filler, 'bk_thelostprophecy'),
    'The Seven Curses': ItemData(ItemClassification.filler, 'bk_thesevencurses'),
    'The Seven Visions': ItemData(ItemClassification.filler, 'bk_a2_1_sevenvisions'),
    'The Stranger': ItemData(ItemClassification.filler, 'bk_a2_1_thestranger'),
    'Wraithguard': ItemData(ItemClassification.progression, 'wraithguard'),
    'Zainsubani\'s Notes': ItemData(ItemClassification.filler, 'bk_a1_11_zainsubaninotes'),
}
