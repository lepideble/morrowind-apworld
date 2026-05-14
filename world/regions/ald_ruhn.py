from rule_builder.rules import Has

from ..locations import DialogueLocationData
from ..quests import HortatorAndNerevarine, ThePathOfTheIncarnate, ZainsubaniInformant

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
    # Athyn Sarethi
    'Hortator and Nerevarine start': DialogueLocationData(
        rule=Has(ThePathOfTheIncarnate.Completed), # TODO: put the right condition here
        events=[HortatorAndNerevarine.Started],
        items=['Public notice', 'note from the Archcanon', 'Ring of the Hortator'],
        topic_id='Redoran Hortator',
        response_id='644392992292611115',
    ),
}
