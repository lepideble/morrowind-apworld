from BaseClasses import Item, Location, Region
from worlds.AutoWorld import World

from .common import GAME_NAME
from .items import items
from .options import MorrowindOptions
from .output import generate_output
from .regions import regions, location_name_to_id
from .settings import MorrowindSettings
from .util import enumerate_names


class MorrowindItem(Item):
    game = GAME_NAME


class MorrowindLocation(Location):
    game = GAME_NAME


class MorrowindWorld(World):
    game = GAME_NAME

    item_name_to_id = {name: item.id for name, item in items.items()}
    location_name_to_id = location_name_to_id

    settings: MorrowindSettings

    options_dataclass = MorrowindOptions
    options: MorrowindOptions

    origin_region_name = 'Vvardenfell'

    def create_regions(self) -> None:
        vvardenfell = Region('Vvardenfell', self.player, self.multiworld)

        self.multiworld.regions.append(vvardenfell)

        for region_data in regions:
            region = Region(region_data.name, self.player, self.multiworld)

            vvardenfell.connect(region)
            self.multiworld.regions.append(vvardenfell)

            for location_name, location_data in region_data.locations.items():
                for name, event in enumerate_names(f'{location_name} event', location_data.events):
                    region.add_event(location_name=name, item_name=event, rule=location_data.rule)

                for name, item in enumerate_names(location_name, location_data.items):
                    location = MorrowindLocation(self.player, name, location_name_to_id[name], region)

                    region.locations.append(location)
                    self.set_rule(location, location_data.rule)

                    self.multiworld.itempool.append(self.create_item(item))

    def create_item(self, name: str) -> None:
        return MorrowindItem(name, items[name].classification, items[name].id, self.player)

    def generate_output(self, output_directory: str) -> None:
        generate_output(self, output_directory)
