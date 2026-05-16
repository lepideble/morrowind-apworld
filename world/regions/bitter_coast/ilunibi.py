from rule_builder.rules import Has

from ...locations import LocationData
from ...quests import SixthHouseBase


name = 'Ilunibi'


locations = {
    'Kill Dagoth Gares': LocationData(
        rule=Has(SixthHouseBase.Started),
        events=[SixthHouseBase.Completed]
    ),
}
