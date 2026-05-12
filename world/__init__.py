from BaseClasses import Item, Location, Region
from worlds.AutoWorld import World

from .common import GAME_NAME
from .events import events
from .items import items
from .locations import locations
from .options import MorrowindOptions
from .output import generate_output
from .settings import MorrowindSettings


class MorrowindItem(Item):
    game = GAME_NAME


class MorrowindLocation(Location):
    game = GAME_NAME


class MorrowindWorld(World):
    game = GAME_NAME

    item_name_to_id = {name: item.id for name, item in items.items()}
    location_name_to_id = {name: location.id for name, location in locations.items()}

    settings: MorrowindSettings

    options_dataclass = MorrowindOptions
    options: MorrowindOptions

    origin_region_name = 'Vvardenfell'

    def create_regions(self) -> None:
        vvardenfell = Region('Vvardenfell', self.player, self.multiworld)

        for location_name, location_data in locations.items():
            location = MorrowindLocation(self.player, location_name, location_data.id, vvardenfell)
            vvardenfell.locations.append(location)
            self.set_rule(location, location_data.rule)

        for event_name, event_data in events.items():
            vvardenfell.add_event(event_name, rule=event_data.rule)

        self.multiworld.regions.append(vvardenfell)

    def create_items(self) -> None:
        for location_name, location_data in locations.items():
            self.multiworld.itempool.append(self.create_item(location_data.original_item))

    def create_item(self, name: str) -> None:
        return MorrowindItem(name, items[name].classification, items[name].id, self.player)

    def generate_output(self, output_directory: str) -> None:
        generate_output(self, output_directory)
