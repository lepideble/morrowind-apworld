from dataclasses import dataclass, field

from rule_builder.rules import HasAll, Rule, True_


@dataclass
class EventData:
    rule: Rule = field(default_factory=lambda: True_())

events = {
    'Report to Caius Cosades completed': EventData(),
    'Antabolis Informant completed': EventData(HasAll('Report to Caius Cosades completed', 'Hasphat\'s notes for Cosades')),
    'Gra-Muzgob Informant completed': EventData(HasAll('Antabolis Informant completed', 'Nerevarine cult notes')),
}