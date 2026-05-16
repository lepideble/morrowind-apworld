from rule_builder.rules import Has

from ...locations import LocationData
from ...quests import ThePathOfTheIncarnate


name = 'Cavern of the Incarnate'


locations = {
    'Pick Moon and Star': LocationData(
        rule=Has(ThePathOfTheIncarnate.Started), # TODO: this should probably be moved to entrace rule when implemented
        events=[ThePathOfTheIncarnate.Completed],
    ),
}
