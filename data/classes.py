from dataclasses import dataclass, field
from enum import StrEnum
from itertools import count

from BaseClasses import ItemClassification
from rule_builder.rules import Rule, True_


item_ids = count(start=1)


@dataclass
class ItemData:
    id: int = field(default_factory=lambda: next(item_ids), init=False)
    classification: ItemClassification
    recordId: str
    count: int = 1


@dataclass
class LocationData:
    rule: Rule = field(default_factory=lambda: True_())
    events: list = field(default_factory=list)
    items: list = field(default_factory=list)


@dataclass
class DialogueLocationData(LocationData):
    topic: str = field(kw_only=True)
    response_id: str | list[str] = field(kw_only=True)


@dataclass
class PickableItemLocationData(LocationData):
    cell: str = field(kw_only=True)


class Quest(StrEnum):
    pass
