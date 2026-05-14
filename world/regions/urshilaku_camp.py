from rule_builder.rules import Has

from ..locations import LocationData, DialogueLocationData
from ..quests import MeetSulMatuul, MehraMiloAndTheLostProphecies, ThePathOfTheIncarnate

name = 'Urshilaku Camp'

locations = {
    'Meet Sul-Matuul reward': DialogueLocationData(
        rule=Has(MeetSulMatuul.Started),
        events=[MeetSulMatuul.Completed],
        items=['The Seven Visions', 'The Stranger'],
        topic_id='pass the test',
        response_id='309174525291904929',
    ),
    'The Path of the Incarnate start': DialogueLocationData(
        rule=Has(MehraMiloAndTheLostProphecies.Completed),
        events=[ThePathOfTheIncarnate.Started],
        topic_id='lost prophecies',
        response_id='1756732638309928813',
    ),
}
