from rule_builder.rules import Has, HasAll

from ....locations import LocationData, DialogueLocationData
from ....quests import AhemmusaNerevarine, HlaaluHortator, ErabenimsunNerevarine, HortatorAndNerevarine, RedoranHortator, TelvanniHortator, UrshilakuNerevarine, ZainabNerevarine
from . import vivec_palace_of_vivec

name = 'Vivec, Temple'


locations = {
    # Danso Indules
    'Named Hortator and Nerevarine by Danso Indules': LocationData(
        rule=HasAll(HlaaluHortator.Completed, RedoranHortator.Completed, TelvanniHortator.Completed, AhemmusaNerevarine.Completed, ErabenimsunNerevarine.Completed, UrshilakuNerevarine.Completed, ZainabNerevarine.Completed),
        events=[HortatorAndNerevarine.NamedHortator, HortatorAndNerevarine.NamedNerevarine],
    ),
    # Tholer Saryoni
    'Meet Archcanon Saryoni': DialogueLocationData(
        rule=HasAll(HortatorAndNerevarine.NamedHortator, HortatorAndNerevarine.NamedNerevarine), # TODO: Add logic for the reputation path once we track it
        events=[HortatorAndNerevarine.MeetArchcanonSaryoni],
        items=['Archcanon\'s Private Key', 'Secret Palace Entrance Key'],
        topic='Temple\'s doctrine',
        response_id=['14850115581371211982', '8324178951345231004'],
    ),
}


exits = [
    ('Vivec, Palace of Vivec', Has('Secret Palace Entrance Key')),
]


regions = [
    vivec_palace_of_vivec,
]
