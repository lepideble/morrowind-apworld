from rule_builder.rules import Has

from ....locations import DialogueLocationData
from ....quests import HortatorAndNerevarine


name = 'Vivec, Palace of Vivec'


locations = {
    # Vivec
    'Meet Vivec': DialogueLocationData(
        rule=Has(HortatorAndNerevarine.MeetArchcanonSaryoni),
        events=[HortatorAndNerevarine.Completed],
        items=['Wraithguard'],
        topic='business',
        response_id=['1389871372227023138', '22053304572540420424'],
    ),
}
