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


def _generate_lua_items_data(items_data: dict[int, tuple[str, int]]) -> collections.abc.Iterator[str]:
    yield 'return {\n'
    for item_id, (item_record_id, item_count) in items_data.items():
        yield '    [' + str(item_id) + '] = {"' + item_record_id + '", ' + str(item_count) + '},\n'
    yield '}\n'


def _generate_lua_locations_data(locations_data: dict[int, tuple[str, int]]) -> collections.abc.Iterator[str]:
    yield 'local content = require("openmw.content")'
    yield ''
    yield 'function onContentFilesLoaded()'
    for location_id, location_item in locations_data.items():
        yield f'    content.miscs.records.ap_{location_id}.name = "{location_item}"'
    yield 'end'
    yield ''
    yield 'return {'
    yield '    engineHandlers = {'
    yield '        onContentFilesLoaded = onContentFilesLoaded'
    yield '    }'
    yield '}'


class MorrowindMod(APPlayerContainer):
    patch_file_ending = '.zip'

    def write_contents(self, opened_zipfile) -> None:
        super().write_contents(opened_zipfile)

        for file in files_list:
            opened_zipfile.writestr(file, files_ressource.joinpath(file).read_bytes())

        opened_zipfile.writestr('scripts/archipelago/items.lua', ''.join(_generate_lua_items_data(self.items_data)))
        opened_zipfile.writestr('scripts/archipelago/locations.lua', '\n'.join(_generate_lua_locations_data(self.locations_data)) + '\n')


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
        item_data.id: (item_data.recordId, item_data.count)
        for item_data in items.values()
    }
    mod.locations_data = {
        location.address: location.item.name if location.player == location.item.player else f"{world.multiworld.get_player_name(location.item.player)}'s {location.item.name}"
        for location in world.get_locations()
        if location.address is not None
    }

    mod.write()
