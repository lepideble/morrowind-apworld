import io
import json
import os
import subprocess

from settings import get_settings
from worlds.Files import APAutoPatchInterface

from ..common import GAME_NAME
from .dialogue import get_dialogue_records
from .scripts import get_scripts


class MorrowindPatch(APAutoPatchInterface):
    game = GAME_NAME
    patch_file_ending = '.apmw'
    result_file_ending = ''

    dialogue_data: list
    items_data: dict[int, tuple[str, int]]

    def write_contents(self, opened_zipfile) -> None:
        super().write_contents(opened_zipfile)

        opened_zipfile.writestr('dialogue.json', json.dumps(self.dialogue_data))
        opened_zipfile.writestr('items.json', json.dumps(self.items_data))

    def read_contents(self, opened_zipfile) -> dict:
        self.dialogue_data = json.load(io.BytesIO(opened_zipfile.read('dialogue.json')))
        self.items_data = json.load(io.BytesIO(opened_zipfile.read('items.json')))

        return super().read_contents(opened_zipfile)

    def patch(self, target: str) -> None:
        self.read()

        morrowind_esm_path = get_settings().morrowind_options.morrowind_esm_path
        tes3conv_path = get_settings().morrowind_options.tes3conv_path

        # Write scripts
        for file_name, file_data in get_scripts(self.items_data).items():
            file_path = os.path.join(target, file_name)

            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, 'wb') as file:
                file.write(file_data)

        # Write omwaddon
        morrowind_esm_size = os.path.getsize(morrowind_esm_path)

        morrowind_json = subprocess.run([tes3conv_path, morrowind_esm_path], capture_output=True)
        morrowind_data = json.load(io.BytesIO(morrowind_json.stdout))

        records = []
        records+= get_dialogue_records(morrowind_data, self.dialogue_data)

        omwaddon_data = json.dumps([
            {
                'type': 'Header',
                'flags': '',
                'version': 1.3,
                'file_type': 'Esp',
                'author': 'Archipelago',
                'description': 'Archipelago mod for Morrowind',
                'num_objects': len(records),
                'masters': [
                    ['Morrowind.esm', morrowind_esm_size],
                ],
            },
            *records,
        ])

        subprocess.run([tes3conv_path, '-', os.path.join(target, 'archipelago.omwaddon')], input=omwaddon_data.encode())
