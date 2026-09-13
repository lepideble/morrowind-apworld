from rule_builder.rules import Has, HasAll

from ...locations import LocationData
from ...quests import TheCitadelsOfTheSixthHouse


name = 'Dagoth Ur'


locations = {
    'Destroy Heart of Lorkhan enchantment': LocationData(
        rule=HasAll('Keening', 'Wraithguard'),
        events=[TheCitadelsOfTheSixthHouse.DestroyHeartEnchantment],
    ),
    'The Citadels of the Sixth House Reward': LocationData(
        rule=Has(TheCitadelsOfTheSixthHouse.DestroyHeartEnchantment),
        events=[TheCitadelsOfTheSixthHouse.Completed],
    ),
}
