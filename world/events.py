from dataclasses import dataclass, field

from rule_builder.rules import Has, HasAll, Rule, True_


@dataclass
class EventData:
    rule: Rule = field(default_factory=lambda: True_())

events = {
    'Report to Caius Cosades completed': EventData(),
    'Antabolis Informant started': EventData(Has('Report to Caius Cosades completed')),
    'Antabolis Informant completed': EventData(HasAll('Antabolis Informant started', 'Hasphat\'s notes for Cosades')),
    'Gra-Muzgob Informant started': EventData(Has('Antabolis Informant completed')),
    'Gra-Muzgob Informant completed': EventData(HasAll('Gra-Muzgob Informant started', 'Nerevarine cult notes')),
    'Vivec Informants started': EventData(Has('Gra-Muzgob Informant completed')),
    'Vivec Informants completed': EventData(HasAll('Vivec Informants started', 'Notes from Huleeya')),
}
