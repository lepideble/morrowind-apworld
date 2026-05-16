from rule_builder.rules import Has

from ...locations import DialogueLocationData
from ...quests import ErabenimsunNerevarine, ThePathOfTheIncarnate


name = 'Erabenimsun Camp'


locations = {
    # Han-Ammu
    'Erabenimsun Nerevarine: named nerevarine': DialogueLocationData(
        rule=Has(ThePathOfTheIncarnate.Completed),
        events=[ErabenimsunNerevarine.Completed],
        topic='name you Nerevarine',
        response_id='2540886782558121314',
    ),
    # Manirai
    'Erabenimsun Nerevarine: reward': DialogueLocationData(
        rule=Has(ErabenimsunNerevarine.Completed),
        items=['The Seizing of the Erabenimsun'],
        topic='Seizing of the Erabenimsun',
        response_id='2090914198831011425',
    ),
}
