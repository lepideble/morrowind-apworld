from rule_builder.rules import HasAll

from ...locations import LocationData, DialogueLocationData
from ...quests import AhemmusaNerevarine, ErabenimsunNerevarine, HortatorAndNerevarine, UrshilakuNerevarine, ZainabNerevarine


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
    # Vivec
    'Meet Vivec': DialogueLocationData(
        rule=HasAll(HortatorAndNerevarine.MeetArchcanonSaryoni, 'Secret Palace Entrance Key'),
        events=[HortatorAndNerevarine.Completed],
        items=['Wraithguard'],
        topic='business',
        response_id=['1389871372227023138', '22053304572540420424'],
    ),
}
