from rule_builder.rules import Has, HasAll

from ..locations import LocationData, DialogueLocationData
from ..quests import CorprusCure, SixthHouseBase

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
    # TODO: This check can be missed if you give the boots to Divayth Fyr before checking it, either
    #   - Force to do this check before bringing the boots to Divayth Fyr
    #   - Change the detection logic here (not sure what condition we can use)
    'Yagrum Bagarn boots': DialogueLocationData(
        rule=Has(CorprusCure.DivaythFyrFetchBoots),
        events=[CorprusCure.YagrumBagarnGaveBoots],
        items=['Dwemer Boots of Flying'],
        topic_id='Dwemer boots',
        response_id='11310263561489620560',
    ),
}
