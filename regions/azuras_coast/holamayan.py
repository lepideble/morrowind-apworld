from rule_builder.rules import Has, HasAll

from ...locations import LocationData, DialogueLocationData
from ...quests import MehraMiloAndTheLostProphecies


name = 'Holamayan'


locations = {
    'Mehra Milo and the Lost Prophecies completed': DialogueLocationData(
        rule=Has(MehraMiloAndTheLostProphecies.Started),
        events=[MehraMiloAndTheLostProphecies.Completed],
        items=['The Lost Prophecy', 'The Seven Curses', 'Kagrenac\'s Tools'],
        topic='lost prophecies',
        response_id='1989213207236428662',
    ),
}
