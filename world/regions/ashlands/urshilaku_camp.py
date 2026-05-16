from rule_builder.rules import Has, HasAll

from ...locations import LocationData, DialogueLocationData
from ...quests import AhemmusaNerevarine, ErabenimsunNerevarine, HlaaluHortator, HortatorAndNerevarine, MeetSulMatuul, MehraMiloAndTheLostProphecies, RedoranHortator, TelvanniHortator, ThePathOfTheIncarnate, UrshilakuNerevarine, ZainabNerevarine


name = 'Urshilaku Camp'


locations = {
    # Nibani Maesa
    'Meet Sul-Matuul reward': DialogueLocationData(
        rule=Has(MeetSulMatuul.Started),
        events=[MeetSulMatuul.Completed],
        items=['The Seven Visions', 'The Stranger'],
        topic='pass the test',
        response_id='309174525291904929',
    ),
    'The Path of the Incarnate start': DialogueLocationData(
        rule=Has(MehraMiloAndTheLostProphecies.Completed),
        events=[ThePathOfTheIncarnate.Started],
        topic='lost prophecies',
        response_id='1756732638309928813',
    ),
    'Named Hortator by Nibani Maesa': LocationData(
        rule=HasAll(HlaaluHortator.Completed, RedoranHortator.Completed, TelvanniHortator.Completed),
        events=[HortatorAndNerevarine.NamedHortator],
    ),
    'Named Nerevarine by Nibani Maesa': LocationData(
        rule=HasAll(AhemmusaNerevarine.Completed, ErabenimsunNerevarine.Completed, UrshilakuNerevarine.Completed, ZainabNerevarine.Completed),
        events=[HortatorAndNerevarine.NamedNerevarine],
    ),
    # Sul-Matul
    'Named Urshilaku Nerevarine': DialogueLocationData(
        rule=Has(ThePathOfTheIncarnate.Completed),
        events=[UrshilakuNerevarine.Completed],
        items=['Teeth of the Urshilaku'],
        topic='Urshilaku Nerevarine',
        response_id='31000125462503519757',
    ),
}
