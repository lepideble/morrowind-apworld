from dataclasses import dataclass, field
from itertools import count

from rule_builder.rules import Has, Rule, True_


ids = count(start=1)


@dataclass
class LocationData:
    id: int = field(default_factory=lambda: next(ids), init=False)
    rule: Rule = field(default_factory=lambda: True_())


@dataclass
class DialogueLocationData(LocationData):
    topic_id: str = field(kw_only=True)
    response_id: str = field(kw_only=True)
    original_item_id: str = field(kw_only=True)


locations = {
    'Report to Caius Cosades reward': DialogueLocationData(
        topic_id='Orders',
        response_id='2090431221919117613',
        original_item_id='gold_001',
    ),
    'Antabolis Informant notes': DialogueLocationData(
        rule=Has('Report to Caius Cosades completed'),
        topic_id='Sixth House',
        response_id='24786265931023614933',
        original_item_id='bk_a1_2_antabolistocosades',
    ),
    'Gra-Muzgob Informant notes': DialogueLocationData(
        rule=Has('Antabolis Informant completed'),
        topic_id='Nerevarine cult',
        response_id='2436419953283993854',
        original_item_id='bk_a1_4_sharnsnotes',
    ),
}
