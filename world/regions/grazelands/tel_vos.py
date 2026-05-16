from rule_builder.rules import Has

from ...locations import DialogueLocationData
from ...quests import TelvanniHortator, ThePathOfTheIncarnate


name = 'Tel Vos'


locations = {
    # Aryon
    # They are other character that can make you Thelvanni hortator, but Aryon is the only one that can give you the robe so let's put this here for now
    'Telvanni Hortator: reward': DialogueLocationData(
        rule=Has(ThePathOfTheIncarnate.Completed),
        events=[TelvanniHortator.Completed],
        items=['Robe of the Hortator'],
        topic='Telvanni Hortator',
        response_id=['1322299981438926449', '97061008048819821', '3143321756286653938', '2247352503238118193'],
    ),
}
