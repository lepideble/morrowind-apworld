from rule_builder.rules import Has, HasAll

from ...locations import LocationData, DialogueLocationData
from ...quests import CorprusCure, SixthHouseBase


name = 'Tel Fyr'


locations = {
    # Divayth Fyr
    'Divayth Fyr ask to fetch boots': LocationData(
        rule=Has(SixthHouseBase.Completed),
        events=[CorprusCure.DivaythFyrFetchBoots],
    ),
    'Bring boots to Divayth Fyr': LocationData(
        rule=HasAll(CorprusCure.DivaythFyrFetchBoots, 'Dwemer Boots of Flying'),
        events=[CorprusCure.Completed],
    ),
    # Yagrum Bagarn
    'Yagrum Bagarn boots': DialogueLocationData(
        rule=Has(CorprusCure.DivaythFyrFetchBoots),
        events=[CorprusCure.YagrumBagarnGaveBoots],
        items=['Dwemer Boots of Flying'],
        topic='Dwemer boots',
        response_id='11310263561489620560',
    ),
}
