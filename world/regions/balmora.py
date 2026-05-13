from rule_builder.rules import Has, HasAll

from ..locations import LocationData, DialogueLocationData
from ..quests import AntabolisInformant, CorprusCure, MeetSulMatuul, GraMuzgobInformant, SixthHouseBase, VivecInformants, ZainsubaniInformant

name = 'Balmora'

locations = {
    # Caius Cosades
    'Report to Caius Cosades reward': DialogueLocationData(
        items=['200 Gold'],
        topic_id='Orders',
        response_id='2090431221919117613',
    ),
    'Antabolis Informant start': LocationData(
        events=[AntabolisInformant.Started],
    ),
    'Antabolis Informant reward': LocationData(
        rule=HasAll(AntabolisInformant.Started, 'Hasphat\'s notes for Cosades'),
        events=[AntabolisInformant.Completed],
    ),
    'Gra-Muzgob Informant start': LocationData(
        rule=Has(AntabolisInformant.Completed),
        events=[GraMuzgobInformant.Started],
    ),
    'Gra-Muzgob Informant reward': LocationData(
        rule=HasAll(GraMuzgobInformant.Started, 'Nerevarine cult notes'),
        events=[GraMuzgobInformant.Completed],
    ),
    'Vivec Informants start': DialogueLocationData(
        rule=Has(GraMuzgobInformant.Completed),
        events=[VivecInformants.Started],
        items=['200 Gold', 'Mission to Vivec -- from Caius'],
        topic_id='Orders',
        response_id='140525241648531121',
    ),
    'Vivec Informants reward': LocationData(
        rule=HasAll(VivecInformants.Started, 'Notes from Huleeya'),
        events=[VivecInformants.Completed],
    ),
    'Zainsubani Informant start': DialogueLocationData(
        rule=Has(VivecInformants.Completed),
        events=[ZainsubaniInformant.Started],
        items=['100 Gold'],
        topic_id='Orders',
        response_id='443826593117014513',
    ),
    'Meet Sul-Matuul start': DialogueLocationData(
        rule=Has(ZainsubaniInformant.Completed),
        events=[MeetSulMatuul.Started],
        items=['200 Gold', 'Decoded package'],
        topic_id='Orders',
        response_id='25246150001870514559',
    ),
    'Sixth House Base start': DialogueLocationData(
        rule=Has(MeetSulMatuul.Completed),
        events=[SixthHouseBase.Started],
        items=['400 Gold'],
        topic_id='Orders',
        response_id='1457411711895630236',
    ),
    'Corprus Cure start': DialogueLocationData(
        rule=Has(SixthHouseBase.Completed),
        events=[CorprusCure.Started],
        items=['Dwemer Coherer', '1000 Gold', '3 Quality Rising Force Potion'],
        topic_id='Orders',
        response_id='1774027995387524122',
    ),
    # Sharn gra-Muzgob
    'Gra-Muzgob notes': DialogueLocationData(
        rule=Has(GraMuzgobInformant.Started),
        items=['Nerevarine cult notes'],
        topic_id='Nerevarine cult',
        response_id='2436419953283993854',
    ),
    # Hasphat Antabolis
    'Antabolis notes': DialogueLocationData(
        rule=Has(AntabolisInformant.Started),
        items=['Hasphat\'s notes for Cosades'],
        topic_id='Sixth House',
        response_id='24786265931023614933',
    ),
}
