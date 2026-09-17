import io
import json
import os
import subprocess

from .records import Records


def load(*paths: str) -> Records:
    masters = []
    records = []

    for path in paths:
        file_size = os.path.getsize(path)
        json_data = subprocess.run(['tes3conv', path], capture_output=True)
        data = json.load(io.BytesIO(json_data.stdout))

        masters.append([os.path.basename(path), file_size])
        records.extend(data)

    return Records(masters, records)


def save(records: Records, path: str):
    records_data = records.get_records()

    subprocess.run(['tes3conv', '--overwrite', '-', path], input=json.dumps([
        {
            'type': 'Header',
            'flags': '',
            'version': 1.3,
            'file_type': 'Esp',
            'author': 'Archipelago',
            'description': 'Archipelago mod for Morrowind',
            'num_objects': len(records_data),
            'masters': records.masters,
        },
        *records_data,
    ]).encode())
