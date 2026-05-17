import os

from Patch import create_rom_file
from worlds.LauncherComponents import Component, components, SuffixIdentifier, Type, launch

from ..common import GAME_NAME
from ..items import items
from .cells import get_cells_data
from .dialogue import get_dialogue_data
from .patch import MorrowindPatch


def generate_output(world, output_directory: str) -> None:
    patch = MorrowindPatch(
        os.path.join(
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


def generate_mod(patch_file):
    create_rom_file(patch_file)


components.append(Component(
    # cli=True,
    display_name=f"{GAME_NAME} Mod Generator",
    component_type=Type.CLIENT,
    file_identifier=SuffixIdentifier(MorrowindPatch.patch_file_ending),
    func=lambda *args: launch(generate_mod, name=f"{GAME_NAME} Mod Generator", args=args),
    game_name=GAME_NAME,
))
