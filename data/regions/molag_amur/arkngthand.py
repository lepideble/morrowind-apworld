from rule_builder.rules import Has

from ...classes import PickableItemLocationData
from ...quests import AntabolisInformant


name = 'Arkngthand'


locations = {
    'Pick Dwemer puzzle box': PickableItemLocationData(
        rule=Has(AntabolisInformant.Started),
        items=['Dwemer puzzle box'],
        cell='Arkngthand, Cells of Hollow Hand',
    ),
}
