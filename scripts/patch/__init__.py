from ..lib.records import Records
from .cells import patch_cells_records
from .dialogue import patch_dialogue_records
from .journal import patch_journal_records


def patch_records(records: Records):
    patch_cells_records(records)
    patch_dialogue_records(records)
    patch_journal_records(records)
