from rule_builder.rules import Has

from ...locations import DialogueLocationData
from ...quests import AhemmusaNerevarine, ThePathOfTheIncarnate


name = 'Ald Daedroth'


locations = {
    'Ahemmusa Nerevarine: reward': DialogueLocationData(
        rule=Has(ThePathOfTheIncarnate.Completed),
        events=[AhemmusaNerevarine.Completed],
        items=['Madstone of the Ahemmusa'],
        topic='name you Nerevarine',
        response_id='212441521742418353',
    ),
}
