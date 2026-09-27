import collections
import importlib
import os

from worlds.Files import APPlayerContainer

from .data.items import items


def _recursive_list_files(traversable) -> collections.abc.Iterator[str]:
    for file in traversable.iterdir():
        if file.is_dir():
            for name in _recursive_list_files(file):
                yield file.name + '/' + name
        else:
            yield file.name


files_ressource = importlib.resources.files(__name__).joinpath('files')
files_list = list(_recursive_list_files(files_ressource))


def _to_lua(value) -> str:
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        return '"' + value + '"'
    if isinstance(value, tuple):
        return '{' + ', '.join(map(_to_lua, value)) + '}'
    raise Error(f'Unexpected type: {type(value)}')


def _to_lua_file(data: dict) -> str:
    file = ''
    file += 'return {\n'
    for key, value in data.items():
        file += f'    [{_to_lua(key)}] = {_to_lua(value)},\n'
    file += '}\n'
    return file


class MorrowindMod(APPlayerContainer):
    patch_file_ending = '.zip'

    def write_contents(self, opened_zipfile) -> None:
        super().write_contents(opened_zipfile)

        for file in files_list:
            opened_zipfile.writestr(file, files_ressource.joinpath(file).read_bytes())

        opened_zipfile.writestr('scripts/archipelago/data/items.lua', _to_lua_file(self.items_data))
        opened_zipfile.writestr('scripts/archipelago/data/locations.lua', _to_lua_file(self.locations_data))


def generate_output(world, output_directory: str) -> None:
    mod = MorrowindMod(
        os.path.join(
            output_directory,
            f'{world.multiworld.get_out_file_name_base(world.player)}{MorrowindMod.patch_file_ending}',
        ),
        world.player,
        world.player_name,
    )

    mod.items_data = {
        item_data.id: (item_data.record_id, item_data.count)
        for item_data in items.values()
    }
    mod.locations_data = {
        location.address: location.item.name if location.player == location.item.player else f"{world.multiworld.get_player_name(location.item.player)}'s {location.item.name}"
        for location in world.get_locations()
        if location.address is not None
    }

    mod.write()
