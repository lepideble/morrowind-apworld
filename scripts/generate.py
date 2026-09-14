import os

from .config import morrowind_esm_path
from .lib.esp import load, save
from .lib.stub import *
from .patch import patch_records

def generate():
    records = load(morrowind_esm_path)

    patch_records(records)

    save(records, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output', 'files', 'archipelago.omwaddon'))

if __name__ == '__main__':
    generate()
