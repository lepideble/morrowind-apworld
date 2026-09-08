from subprocess import run

from Patch import create_rom_file
from settings import get_settings
from worlds.LauncherComponents import Component, components, SuffixIdentifier, Type, launch

from .common import GAME_NAME, PATCH_FILE_ENDING


def launch_client(patch_file):
    meta_data, result_file = create_rom_file(patch_file)

    run([
        get_settings().morrowind_options.openmw_archipelago_path,
        '--data', result_file,
        '--content', 'archipelago.omwscripts',
        '--content', 'archipelago.omwaddon',
    ])


components.append(Component(
    display_name=f"{GAME_NAME} Client",
    component_type=Type.CLIENT,
    file_identifier=SuffixIdentifier(PATCH_FILE_ENDING),
    func=lambda *args: launch(launch_client, name=f"{GAME_NAME} Client", args=args),
    game_name=GAME_NAME,
))
