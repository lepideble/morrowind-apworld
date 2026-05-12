from rule_builder.rules import Has

from ..locations import LocationData, DialogueLocationData
from ..quests import MeetSulMatuul

name = 'Urshilaku Camp'

locations = {
    'Meet Sul-Matuul reward': DialogueLocationData(
        rule=Has(MeetSulMatuul.Started),
        events=[MeetSulMatuul.Completed],
        items=['The Seven Visions', 'The Stranger'],
        topic_id='pass the test',
        response_id='309174525291904929',
    ),
}
