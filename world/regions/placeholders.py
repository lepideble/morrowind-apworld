from rule_builder.rules import Has, HasAll

from ..locations import LocationData
from ..quests import HlaaluHortator, HortatorAndNerevarine, RedoranHortator, TelvanniHortator, ThePathOfTheIncarnate

# Placeholder locations for quest where implementation is not finished

name = '__placeholders__'

locations = {
    'RedoranHortator': LocationData(
        rule=Has(ThePathOfTheIncarnate.Completed),
        events=[RedoranHortator.Completed]
    ),
    'TelvanniHortator': LocationData(
        rule=Has(ThePathOfTheIncarnate.Completed),
        events=[TelvanniHortator.Completed]
    ),
    'AllHortator': LocationData(
        rule=HasAll(HlaaluHortator.Completed, RedoranHortator.Completed, TelvanniHortator.Completed),
        events=[HortatorAndNerevarine.NamedHortator]
    ),
}
