from rule_builder.rules import Has, HasAll

from ..locations import LocationData
from ..quests import AhemmusaNerevarine, ErabenimsunNerevarine, HlaaluHortator, HortatorAndNerevarine, RedoranHortator, TelvanniHortator, ThePathOfTheIncarnate, UrshilakuNerevarine, ZainabNerevarine

# Placeholder locations for quest where implementation is not finished

name = '__placeholders__'

locations = {
    'ErabenimsunNerevarine': LocationData(
        rule=Has(ThePathOfTheIncarnate.Completed),
        events=[ErabenimsunNerevarine.Completed]
    ),
    'ZainabNerevarine': LocationData(
        rule=Has(ThePathOfTheIncarnate.Completed),
        events=[ZainabNerevarine.Completed]
    ),
    'AllNerevarine': LocationData(
        rule=HasAll(AhemmusaNerevarine.Completed, ErabenimsunNerevarine.Completed, UrshilakuNerevarine.Completed, ZainabNerevarine.Completed),
        events=[HortatorAndNerevarine.NamedNerevarine]
    ),
    'HlaaluHortator': LocationData(
        rule=Has(ThePathOfTheIncarnate.Completed),
        events=[HlaaluHortator.Completed]
    ),
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
