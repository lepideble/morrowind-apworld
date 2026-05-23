from .records import Journal, Records


def copy_journal_entry(records: Records, old_journal_id: str, new_journal_id, old_id: int, new_id: int):
    records.journals[new_journal_id] = Journal()
    records.journals[new_journal_id][new_id] = {
        **records.journals[old_journal_id][old_id],
        'prev_id': '',
        'next_id': '',
    }


def patch_topic_response_script(records: Records, topic: str, response_id: str, old: str, new: str):
    records.topics[topic][response_id] = {
        **records.topics[topic][response_id],
        'script_text': records.topics[topic][response_id]['script_text'].replace(old, new)
    }


def patch_topic_response_filter(records: Records, topic: str, response_id: str, index: int, new_filter: dict):
    records.topics[topic][response_id] = {
        **records.topics[topic][response_id],
        'filters': [
            { **new_filter, 'index': index } if old_filter['index'] == index else old_filter
            for old_filter in records.topics[topic][response_id]['filters']
        ]
    }


def patch_journal_records(records: Records):
    copy_journal_entry(
        records,
        old_journal_id='A1_4_MuzgobInformant',
        new_journal_id='AP_A1_4_MuzgobInformant_12',
        old_id='20234212771163929428',
        new_id='40786711255784614059082211258',
    )
    patch_topic_response_script(
        records,
        topic='Andrano Ancestral Tomb',
        response_id='1091431135261045346',
        old='Journal A1_4_MuzgobInformant 12',
        new='Journal AP_A1_4_MuzgobInformant_12 12'
    )
    patch_topic_response_filter(
        records,
        topic='Andrano Ancestral Tomb',
        response_id='31045242555523926',
        index=0,
        new_filter={
            'filter_type': 'Journal',
            'function': 'JournalType',
            'comparison': 'GreaterEqual',
            'id': 'AP_A1_4_MuzgobInformant_12',
            'value': {
                'type': 'Integer',
                'data': 12,
            },
        }
    )
