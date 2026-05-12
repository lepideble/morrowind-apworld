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
