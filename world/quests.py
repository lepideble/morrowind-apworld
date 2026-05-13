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
