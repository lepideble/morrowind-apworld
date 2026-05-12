from rule_builder.rules import Has, HasAll

from ..locations import DialogueLocationData
from ..quests import ZainsubaniInformant

name = 'Ald\'ruhn'

locations = {
    # Hassour Zainsubani
    'Zainsubani Informant reward': DialogueLocationData(
        rule=Has(ZainsubaniInformant.Started),
        events=[ZainsubaniInformant.Completed],
        items=['Zainsubani\'s Notes'],
        topic_id='Ashlanders',
        response_id='169562763275484215',
    ),
}
