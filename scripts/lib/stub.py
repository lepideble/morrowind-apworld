"""Small stub to allow importing data without archipelago"""

import enum
import types
import sys

class BaseClasses(types.ModuleType):
    class ItemClassification(enum.IntFlag):
        filler = 0b00000
        progression = 0b00001
        useful = 0b00010

class RuleBuilderRules(types.ModuleType):
    class Has:
        def __init__(*args):
            pass

    class HasAll:
        def __init__(*args):
            pass

    class Rule:
        pass

    class True_:
        pass

sys.modules['BaseClasses'] = BaseClasses
sys.modules['rule_builder.rules'] = RuleBuilderRules
