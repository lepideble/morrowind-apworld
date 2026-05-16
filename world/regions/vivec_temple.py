from rule_builder.rules import HasAll

from ..locations import DialogueLocationData
from ..quests import HortatorAndNerevarine


name = 'Vivec, Temple'


locations = {
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
