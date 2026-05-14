from rule_builder.rules import Has

from ..locations import LocationData
from ..quests import TheCitadelsOfTheSixthHouse


name = 'Dagoth Ur'

locations = {
    'Destroy Heart of Lorkhan enchantment': LocationData(
        rule=Has('Wraithguard'),
        events=[TheCitadelsOfTheSixthHouse.DestroyHearthEnchantment],
    ),
    'The Citadels of the Sixth House Reward': LocationData(
        rule=Has(TheCitadelsOfTheSixthHouse.DestroyHearthEnchantment),
        events=[TheCitadelsOfTheSixthHouse.Completed],
    ),
}
