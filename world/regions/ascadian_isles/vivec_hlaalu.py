from rule_builder.rules import Has

from ...locations import DialogueLocationData
from ...quests import HlaaluHortator, ThePathOfTheIncarnate


name = 'Vivec, Hlaalu'


locations = {
    # Crassius Curio
    'Hlaalu Hortator: reward': DialogueLocationData(
        rule=Has(ThePathOfTheIncarnate.Completed),
        events=[HlaaluHortator.Completed],
        items=['Belt of the Hortator'],
        topic='Hlaalu Hortator',
        response_id=['347813577123929409', '974621737323148380', '22831490429782793', '1684625245479617476'],
    ),
}
