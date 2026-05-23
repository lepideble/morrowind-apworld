from rule_builder.rules import Has, HasAll

from ...locations import LocationData, DialogueLocationData
from ...quests import AntabolisInformant, CorprusCure, MeetSulMatuul, MehraMiloAndTheLostProphecies, GraMuzgobInformant, SixthHouseBase, VivecInformants, ZainsubaniInformant


name = 'Balmora'


locations = {
    # Caius Cosades
    'Report to Caius Cosades reward': DialogueLocationData(
        items=['200 Gold'],
        topic='Orders',
        response_id='2090431221919117613',
    ),
    'Antabolis Informant start': LocationData(
        events=[AntabolisInformant.Started],
    ),
    'Antabolis Informant reward': LocationData(
        rule=HasAll(AntabolisInformant.GetNotes, 'Hasphat\'s notes for Cosades'),
        events=[AntabolisInformant.Completed],
    ),
    'Gra-Muzgob Informant start': LocationData(
        rule=Has(AntabolisInformant.Completed),
        events=[GraMuzgobInformant.Started],
    ),
    'Gra-Muzgob Informant completed': LocationData(
        rule=HasAll(GraMuzgobInformant.GetNotes, 'Nerevarine cult notes'),
        events=[GraMuzgobInformant.Completed],
    ),
    'Gra-Muzgob Informant promotion': DialogueLocationData(
        rule=Has(GraMuzgobInformant.Completed),
        items=['Scroll of Divine Intervention', 'Scroll of Almsivi Intervention'],
        topic='Blades Apprentice',
        response_id='1010328727326818700',
    ),
    'Vivec Informants start': DialogueLocationData(
        rule=Has(GraMuzgobInformant.Completed),
        events=[VivecInformants.Started],
        items=['200 Gold', 'Mission to Vivec -- from Caius'],
        topic='Orders',
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
        topic='Orders',
        response_id='443826593117014513',
    ),
    'Meet Sul-Matuul start': DialogueLocationData(
        rule=Has(ZainsubaniInformant.Completed),
        events=[MeetSulMatuul.Started],
        items=['200 Gold', 'Decoded package'],
        topic='Orders',
        response_id='25246150001870514559',
    ),
    'Sixth House Base start': DialogueLocationData(
        rule=Has(MeetSulMatuul.Completed),
        events=[SixthHouseBase.Started],
        items=['400 Gold'],
        topic='Orders',
        response_id='1457411711895630236',
    ),
    'Corprus Cure start': DialogueLocationData(
        rule=Has(SixthHouseBase.Completed),
        events=[CorprusCure.Started],
        items=['Dwemer Coherer', '1000 Gold', '3 Quality Rising Force Potion'],
        topic='Orders',
        response_id='1774027995387524122',
    ),
    'Mehra Milo and the Lost Prophecies start': DialogueLocationData(
        rule=Has(CorprusCure.Completed),
        events=[MehraMiloAndTheLostProphecies.Started],
        topic='Orders',
        response_id='256041812384511341',
    ),
    # Sharn gra-Muzgob
    'Gra-Muzgob supplies': DialogueLocationData(
        rule=Has(GraMuzgobInformant.Started),
        items=['Fireblade', '2 Scroll of Taldam\'s Scorcher', '2 Scroll of Vitality'],
        topic='Andrano Ancestral Tomb',
        response_id='1091431135261045346',
    ),
    'Gra-Muzgob notes': DialogueLocationData(
        rule=HasAll(GraMuzgobInformant.Started, 'Skull of Llevule Andrano'),
        events=[GraMuzgobInformant.GetNotes],
        items=['Nerevarine cult notes'],
        topic='Nerevarine cult',
        response_id='2436419953283993854',
    ),
    # Hasphat Antabolis
    'Antabolis notes': DialogueLocationData(
        rule=HasAll(AntabolisInformant.Started, 'Dwemer puzzle box'),
        events=[AntabolisInformant.GetNotes],
        items=['Hasphat\'s notes for Cosades'],
        topic='Sixth House',
        response_id='24786265931023614933',
    ),
    'Antabolis Informant: Arkngthand key': DialogueLocationData(
        rule=Has(AntabolisInformant.Completed),
        items=['Key to Lower Arkngthand'],
        topic='Dwemer puzzle box',
        response_id='2012632121258661882',
    ),
}
