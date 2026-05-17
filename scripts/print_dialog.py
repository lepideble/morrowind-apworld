from argparse import ArgumentParser
from importlib import resources
from json import load as json_load
from os import path
from textwrap import indent, TextWrapper


indentation = '  '
text_wrapper = TextWrapper(width=120, initial_indent=indentation, subsequent_indent=indentation, replace_whitespace=False)


def render_text(text: str) -> str:
    return '\n'.join((warped for line in text.splitlines() for warped in (text_wrapper.wrap(line) if line else [''])))


def render_script(script_text: str) -> str:
    return indent('\n'.join(script_text.splitlines()), indentation)


def remove_comments(script_text: str) -> str:
    return '\n'.join((line for line in script_text.splitlines() if not line.startswith(';')))


def render_comparison(filter: dict) -> str:
    match filter['comparison']:
        case 'Equal':
            sign = '='
        case 'Greater':
            sign = '>'
        case 'GreaterEqual':
            sign = '≥'
        case 'Less':
            sign = '<'
        case 'LessEqual':
            sign = '≤'
        case _:
            raise Exception(f'Unknown comparison: {comparison}')

    return f'{sign} {filter['value']['data']}'


def print_dialog(speaker: str|None, journal: str|None, set_journal: str|None, topic: str|None):
    with open(path.join(path.dirname(path.dirname(__file__)), 'data', 'Morrowind.json')) as file:
        morrowind_records = json_load(file)

    current_topic = None

    for record in morrowind_records:
        if record['type'] == 'Dialogue' and record['dialogue_type'] == 'Topic':
            current_topic = record['id']

        if record['type'] != 'DialogueInfo':
            continue

        if speaker is not None and speaker != record['speaker_id']:
            continue

        if journal is not None:
            found = False
            for filter in record['filters']:
                if filter['filter_type'] == 'Journal' and filter['function'] == 'JournalType' and filter['id'] == journal:
                    found = True
            if journal in remove_comments(record['script_text']):
                found = True
            if not found:
                continue

        if set_journal is not None and set_journal not in remove_comments(record['script_text']):
            continue

        if topic is not None and topic != current_topic:
            continue

        conditions = []
        for filter in record['filters']:
            match (filter['filter_type'], filter['function']):
                case ('Dead', 'DeadType'):
                    conditions.append(f'character {filter['id']} is dead')
                case ('Function', 'Choice'):
                    conditions.append(f'choice {filter['value']['data']}')
                case ('Function', 'PcCorprus'):
                    match (filter['comparison'], filter['value']['data']):
                        case ('Equal', 1) | ('GreaterEqual', 1):
                            conditions.append(f'player have corpus')
                        case ('Equal', 0):
                            conditions.append(f'player doesn\'t have corpus')
                        case _:
                            raise Exception('Unexpected corpus condition')
                case ('Function', 'PcExpelled'):
                    conditions.append('player expelled')
                case ('Function', 'PcMercantile'):
                    conditions.append(f'player mercantile {render_comparison(filter)}')
                case ('Function', 'PcLevel'):
                    if filter['comparison'] == 'GreaterEqual' and filter['value']['data'] == 1:
                        # Useless condition
                        pass
                    else:
                        conditions.append(f'player level {render_comparison(filter)}')
                case ('Function', 'PcReputation'):
                    conditions.append(f'player reputation {render_comparison(filter)}')
                case ('Function', 'PcSex'):
                    conditions.append(f'player sex {render_comparison(filter)}')
                case ('Function', 'PcSpeechcraft'):
                    conditions.append(f'player sperchcraft {render_comparison(filter)}')
                case ('Function', 'TalkedToPc'):
                    conditions.append(f'player talked to speaker {render_comparison(filter)}')
                case ('Global', 'VariableCompare'):
                    conditions.append(f'global variable {filter['id']} {render_comparison(filter)}')
                case ('Item', 'ItemType'):
                    conditions.append(f'player has item {filter['id']} count {render_comparison(filter)}')
                case ('Journal', 'JournalType'):
                    conditions.append(f'journal {filter['id']} {render_comparison(filter)}')
                case ('Local', 'VariableCompare'):
                    conditions.append(f'local variable {filter['id']} {render_comparison(filter)}')
                case ('NotCell', 'NotCell'):
                    conditions.append(f'not cell {filter['id']} not {render_comparison(filter)}')
                case ('NotId', 'NotIdType'):
                    conditions.append(f'speaker not {filter['id']}')
                case ('NotLocal', 'VariableCompare'):
                    conditions.append(f'local variable {filter['id']} not {render_comparison(filter)}')
                case ('NotFaction', 'NotFaction'):
                    conditions.append(f'not faction {filter['id']} not {render_comparison(filter)}')
                case _:
                     raise Exception(f'Unknown filter type: {(filter['filter_type'], filter['function'])}')

        print()
        print(f'id: {record['id']}')
        if record['speaker_id']:
            print(f'speaker: {record['speaker_id']}')
        if record['data']['dialogue_type'] == 'Greeting':
            print('greeting')
        else:
            print(f'topic: {current_topic}')
        if len(conditions) > 0:
            print('conditions:')
            for condition in conditions:
                print(f'{indentation}{condition}')
        print('text:')
        print(render_text(record['text']))
        if record['script_text']:
            print('script:')
            print(render_script(record['script_text']))


parser = ArgumentParser()
parser.add_argument('--journal', help='Filter entries that have either a condition or set the corresponding journal')
parser.add_argument('--set-journal', help='Filter entries that set the corresponding journal')
parser.add_argument('--topic')
parser.add_argument('--speaker')


if __name__ == '__main__':
    print_dialog(**vars(parser.parse_args()))
