from dataclasses import dataclass, field
from itertools import count

from rule_builder.rules import Rule, True_


@dataclass
class LocationData:
    rule: Rule = field(default_factory=lambda: True_())
    events: list = field(default_factory=list)
    items: list = field(default_factory=list)


@dataclass
class DialogueLocationData(LocationData):
    topic_id: str = field(kw_only=True)
    response_id: str | list[str] = field(kw_only=True)
