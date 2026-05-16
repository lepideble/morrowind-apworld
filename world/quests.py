from enum import StrEnum


class Quest(StrEnum):
    pass


class AntabolisInformant(Quest):
    Started = 'Antabolis Informant started'
    Completed = 'Antabolis Informant completed'


class GraMuzgobInformant(Quest):
    Started = 'Gra-Muzgob Informant started'
    Completed = 'Gra-Muzgob Informant completed'


class VivecInformants(Quest):
    Started = 'Vivec Informants started'
    Completed = 'Vivec Informants completed'


class ZainsubaniInformant(Quest):
    Started = 'Zainsubani Informant started'
    Completed = 'Zainsubani Informant completed'


class MeetSulMatuul(Quest):
    Started = 'Meet Sul-Matuul started'
    Completed = 'Meet Sul-Matuul completed'


class SixthHouseBase(Quest): # A2_2_6thHouse
    Started = 'Sixth House Base started' # 5
    Completed = 'Sixth House Base completed' # 50


class CorprusCure(Quest): # A2_3_CorprusCure
    Started = 'Corprus Cure started' # 1
    DivaythFyrFetchBoots = 'Corprus Cure Divayth Fyr fetch boots' # 25
    YagrumBagarnGaveBoots = 'Corprus Cure Yagrum Bagarn gave boots' # 40
    Completed = 'Corprus Cure completed' # 50


class MehraMiloAndTheLostProphecies(Quest): # A2_4_MiloGone
    Started = 'Mehra Milo and the Lost Prophecies started' # 1
    Completed = 'Mehra Milo and the Lost Prophecies completed' # 50


class ThePathOfTheIncarnate(Quest): # A2_6_Incarnate
    Started = 'The Path of the Incarnate started' # 1
    Completed = 'The Path of the Incarnate completed' # 50


class HlaaluHortator(Quest): # B6_HlaaluHort
    Completed = 'Hlaalu Hortator: completed' # 50


class RedoranHortator(Quest): # B5_RedoranHort
    Completed = 'Redoran Hortator: completed' # 50


class TelvanniHortator(Quest): # B7_TelvanniHort
    Completed = 'Telvanni Hortator: completed' # 50


class AhemmusaNerevarine(Quest): # B2_AhemmusaSafe
    Completed = 'Ahemmusa Nerevarine completed' # 50


class ErabenimsunNerevarine(Quest): # B4_KillWarLovers
    Completed = 'Erabenimsun Nerevarine completed' # 50


class UrshilakuNerevarine(Quest): # B1_UnifyUrshilaku
    Completed = 'Urshilaku Nerevarine completed' # 50


class ZainabNerevarine(Quest): # B3_ZainabBride
    Completed = 'Zainab Nerevarine completed' # 50


class HortatorAndNerevarine(Quest): # B8_MeetVivec
    NamedHortator = 'Hortator and Nerevarine: named hortator' # B8_All_Hortator 50
    NamedNerevarine = 'Hortator and Nerevarine: named nerevarine' # B8_All_Nerevarine 50
    MeetArchcanonSaryoni = 'Hortator and Nerevarine: meet Archcanon Saryoni' # 30
    Completed = 'Hortator and Nerevarine: completed' # 50


class TheCitadelsOfTheSixthHouse(Quest): # C3_DestroyDagoth
    DestroyHearthEnchantment = 'Destroy Heart of Lorkhan enchantment' # 20
    Completed = 'The Citadels of the Sixth House completed' # 50
