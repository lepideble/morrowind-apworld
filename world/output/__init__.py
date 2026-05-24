from os import path

from ..items import items
from .cells import get_cells_data
from .dialogue import get_dialogue_data
from .patch import MorrowindPatch


def generate_output(world, output_directory: str) -> None:
    patch = MorrowindPatch(
        path.join(
            output_directory,
            f'{world.multiworld.get_out_file_name_base(world.player)}{MorrowindPatch.patch_file_ending}',
        ),
        world.player,
        world.player_name,
    )

    patch.cells_data = get_cells_data(world)
    patch.dialogue_data = get_dialogue_data(world)
    patch.items_data = {item_data.id: (item_data.recordId, item_data.count) for item_data in items.values()}
    patch.write()
