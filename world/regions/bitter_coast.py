from rule_builder.rules import Has

from ..locations import LocationData
from ..quests import SixthHouseBase

name = 'Bitter Coast Region'

locations = {
    'Kill Dagoth Gares': LocationData(
        rule=Has(SixthHouseBase.Started),
        events=[SixthHouseBase.Completed]
    ),
}
