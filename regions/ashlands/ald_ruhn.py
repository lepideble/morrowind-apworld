from rule_builder.rules import Has

from ...locations import DialogueLocationData
from ...quests import RedoranHortator, ThePathOfTheIncarnate, ZainsubaniInformant


name = 'Ald\'ruhn'


locations = {
    # Athyn Sarethi
    'Redoran Hortator: reward': DialogueLocationData(
        rule=Has(ThePathOfTheIncarnate.Completed),
        events=[RedoranHortator.Completed],
        items=['Public notice', 'note from the Archcanon', 'Ring of the Hortator'],
        topic='Redoran Hortator',
        response_id='644392992292611115',
    ),
    # Hassour Zainsubani
    'Zainsubani Informant reward': DialogueLocationData(
        rule=Has(ZainsubaniInformant.Started),
        events=[ZainsubaniInformant.Completed],
        items=['Zainsubani\'s Notes'],
        topic='Ashlanders',
        response_id='169562763275484215',
    ),
}
