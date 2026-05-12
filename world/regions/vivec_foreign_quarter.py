from rule_builder.rules import Has, HasAll

from ..locations import LocationData, DialogueLocationData
from ..quests import AntabolisInformant, GraMuzgobInformant, VivecInformants, ZainsubaniInformant

name = 'Vivec, Foreign Quarter'

locations = {
    # Huleeya
    'Huleeya notes': DialogueLocationData(
        rule=Has(VivecInformants.Started),
        items=['Notes from Huleeya'],
        topic_id='Nerevarine cult',
        response_id='678171652181916488',
    ),
}
