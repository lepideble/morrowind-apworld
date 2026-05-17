from rule_builder.rules import Has

from ...locations import PickableItemLocationData
from ...quests import AntabolisInformant


name = 'Arkngthand'


locations = {
    'Dwemer puzzle box': PickableItemLocationData(
        rule=Has(AntabolisInformant.Started),
        items=['Dwemer puzzle box'],
        cell='Arkngthand, Cells of Hollow Hand'
    ),
}
