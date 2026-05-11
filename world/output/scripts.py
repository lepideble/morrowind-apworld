import collections
import importlib


def _recursive_list_files(traversable) -> collections.abc.Iterator[str]:
    for file in traversable.iterdir():
        if file.is_dir():
            for name in _recursive_list_files(file):
                yield file.name + '/' + name
        else:
            yield file.name


def _generate_lua_items_data(items_data: dict[int, tuple[str, int]]) -> str:
    yield 'return {\n'
    for item_id, (item_record_id, item_count) in items_data.items():
        yield '    [' + str(item_id) + '] = {"' + item_record_id + '", ' + str(item_count) + '},\n'
    yield '}\n'


def get_scripts(items_data: dict[int, tuple[str, int]]) -> dict[str, bytes]:
    files_ressource = importlib.resources.files(__name__).joinpath('files')
    files_list = list(_recursive_list_files(files_ressource))

    scripts = {}

    for file in _recursive_list_files(files_ressource):
        scripts[file] = files_ressource.joinpath(file).read_bytes()

    scripts['scripts/archipelago/items.lua'] = ''.join(_generate_lua_items_data(items_data)).encode()

    return scripts
