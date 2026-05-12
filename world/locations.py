from dataclasses import dataclass, field
from itertools import count

from rule_builder.rules import Has, Rule, True_


ids = count(start=1)


@dataclass
class LocationData:
    id: int = field(default_factory=lambda: next(ids), init=False)
    original_item: str
    rule: Rule = field(default_factory=lambda: True_())


@dataclass
class DialogueLocationData(LocationData):
    topic_id: str = field(kw_only=True)
    response_id: str = field(kw_only=True)


locations = {
    'Report to Caius Cosades reward': DialogueLocationData(
        original_item='200 Gold',
        topic_id='Orders',
        response_id='2090431221919117613',
    ),
    'Antabolis notes': DialogueLocationData(
        original_item='Hasphat\'s notes for Cosades',
        rule=Has('Report to Caius Cosades completed'),
        topic_id='Sixth House',
        response_id='24786265931023614933',
    ),
    'Gra-Muzgob notes': DialogueLocationData(
        original_item='Nerevarine cult notes',
        rule=Has('Antabolis Informant completed'),
        topic_id='Nerevarine cult',
        response_id='2436419953283993854',
    ),
    'Mission to Vivec 1': DialogueLocationData(
        original_item='200 Gold',
        rule=Has('Vivec Informants started'),
        topic_id='Orders',
        response_id='140525241648531121',
    ),
    'Mission to Vivec 2': DialogueLocationData(
        original_item='Mission to Vivec -- from Caius',
        rule=Has('Vivec Informants started'),
        topic_id='Orders',
        response_id='140525241648531121',
    ),
    'Huleeya notes': DialogueLocationData(
        original_item='Notes from Huleeya',
        rule=Has('Vivec Informants started'),
        topic_id='Nerevarine cult',
        response_id='678171652181916488',
    ),
}
