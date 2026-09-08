from rule_builder.rules import Has, HasAll

from ...locations import DialogueLocationData
from ...quests import ThePathOfTheIncarnate, ZainabNerevarine


name = 'Zainab Camp'


locations = {
    # Kaushad
    'Zainab Nerevarine: reward': DialogueLocationData(
        rule=Has(ThePathOfTheIncarnate.Completed),
        events=[ZainabNerevarine.Completed],
        items=['Thong of Zainab'],
        topic='Telvanni bride',
        response_id='1772430844181427661',
    ),
    'Zainab Nerevarine: wedding gift': DialogueLocationData(
        rule=Has(ZainabNerevarine.Completed),
        items=['Ashkhan\'s Wedding Gift'],
        topic='Telvanni bride',
        response_id='23585283422667725',
    ),
}