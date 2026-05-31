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
    # Misc
    'Dwemer Coherer': ItemData(ItemClassification.filler, 'misc_dwrv_artifact50'),
    'Dwemer puzzle box': ItemData(ItemClassification.progression, 'misc_dwrv_ark_cube00'),
    '100 Gold': ItemData(ItemClassification.filler, 'Gold_001', 100),
    '200 Gold': ItemData(ItemClassification.filler, 'Gold_001', 200),
    '400 Gold': ItemData(ItemClassification.filler, 'Gold_001', 400),
    '1000 Gold': ItemData(ItemClassification.filler, 'Gold_001', 1000),
    'House Dagoth cup': ItemData(ItemClassification.progression, 'misc_goblet_dagoth'),
    'Shadow Shield': ItemData(ItemClassification.progression, 'shadow_shield'),
    'Skull of Llevule Andrano': ItemData(ItemClassification.progression, 'misc_Skull_Llevule'),
    # Books
    'Decoded package': ItemData(ItemClassification.filler, 'bk_a1_1_packagedecoded'),
    'Hasphat\'s notes for Cosades': ItemData(ItemClassification.progression, 'bk_a1_2_antabolistocosades'),
    'Kagrenac\'s Tools': ItemData(ItemClassification.filler, 'bk_kagrenac\'stools'),
    'Mission to Vivec -- from Caius': ItemData(ItemClassification.filler, 'bk_a1_v_vivecinformants'),
    'Nerevarine cult notes': ItemData(ItemClassification.progression, 'bk_a1_4_sharnsnotes'),
    'Notes from Huleeya': ItemData(ItemClassification.progression, 'bk_A1_7_HuleeyaInformant'),
    'note from the Archcanon': ItemData(ItemClassification.filler, 'bk_saryoni_note'),
    'Public notice': ItemData(ItemClassification.filler, 'bk_NerevarineNotice'),
    'The Lost Prophecy': ItemData(ItemClassification.filler, 'bk_thelostprophecy'),
    'The Seven Curses': ItemData(ItemClassification.filler, 'bk_thesevencurses'),
    'The Seven Visions': ItemData(ItemClassification.filler, 'bk_a2_1_sevenvisions'),
    'The Stranger': ItemData(ItemClassification.filler, 'bk_a2_1_thestranger'),
    'Zainsubani\'s Notes': ItemData(ItemClassification.filler, 'bk_a1_11_zainsubaninotes'),
    # Equipment
    'Ashkhan\'s Wedding Gift': ItemData(ItemClassification.filler, 'exquisite_shirt_01_wedding'),
    'Belt of the Hortator': ItemData(ItemClassification.useful, 'hortatorbelt'),
    'Dwemer Boots of Flying': ItemData(ItemClassification.progression, 'dwemer_boots of flying'),
    'Fireblade': ItemData(ItemClassification.useful, 'fireblade'),
    'Madstone of the Ahemmusa': ItemData(ItemClassification.useful, 'madstone'),
    'Malipu-Ataman\'s Belt': ItemData(ItemClassification.useful, 'malipu_ataman\'s_belt'),
    'Ring of the Hortator': ItemData(ItemClassification.useful, 'hortatorring'),
    'Robe of the Hortator': ItemData(ItemClassification.useful, 'hortatorrobe'),
    'Teeth of the Urshilaku': ItemData(ItemClassification.useful, 'teeth'),
    'The Seizing of the Erabenimsun': ItemData(ItemClassification.useful, 'seizing'),
    'Thong of Zainab': ItemData(ItemClassification.useful, 'thong'),
    'Wraithguard': ItemData(ItemClassification.progression, 'wraithguard'),
    # Potions
    '3 Quality Rising Force Potion': ItemData(ItemClassification.useful, 'P_Levitation_Q', 3),
    # Scrolls
    'Scroll of Almsivi Intervention': ItemData(ItemClassification.useful, 'sc_almsiviintervention'),
    'Scroll of Divine Intervention': ItemData(ItemClassification.useful, 'sc_divineintervention'),
    '2 Scroll of Taldam\'s Scorcher': ItemData(ItemClassification.useful, 'sc_taldamsscorcher', 2),
    '2 Scroll of Vitality': ItemData(ItemClassification.useful, 'sc_vitality', 2),
    # Keys
    'Archcanon\'s Private Key': ItemData(ItemClassification.filler, 'key_archcanon_private'),
    'Key to Lower Arkngthand': ItemData(ItemClassification.filler, 'misc_dwrv_ark_key00'),
    'Secret Palace Entrance Key': ItemData(ItemClassification.progression, 'key_vivec_secret'),
}
