import collections
import importlib

from Utils import cache_argsless

from ..items import items


def _recursive_list_files(traversable) -> collections.abc.Iterator[str]:
    for file in traversable.iterdir():
        if file.is_dir():
            for name in _recursive_list_files(file):
                yield file.name + '/' + name
        else:
            yield file.name


def _generate_lua_items_data() -> str:
    yield 'return {\n'
    for item_name, item_data in items.items():
        yield '    [' + str(item_data.id) + '] = {"' + item_data.recordId + '", ' + str(item_data.count) + '},\n'
    yield '}\n'


@cache_argsless
def get_scripts() -> dict[str, bytes]:
    files_ressource = importlib.resources.files(__name__).joinpath('files')
    files_list = list(_recursive_list_files(files_ressource))

    scripts = {}

    for file in _recursive_list_files(files_ressource):
        scripts[file] = files_ressource.joinpath(file).read_bytes()

    scripts['scripts/archipelago/items.lua'] = ''.join(_generate_lua_items_data()).encode()

    return scripts