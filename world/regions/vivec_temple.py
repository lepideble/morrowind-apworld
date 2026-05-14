from rule_builder.rules import Has

from ..locations import DialogueLocationData
from ..quests import HortatorAndNerevarine


name = 'Vivec, Temple'

locations = {
    # Vivec
    'Meet Vivec': DialogueLocationData(
        rule=Has(HortatorAndNerevarine.Started),
        events=[HortatorAndNerevarine.Completed],
        items=['Wraithguard'],
        topic_id='business',
        response_id=['1389871372227023138', '22053304572540420424'],
    ),
}
