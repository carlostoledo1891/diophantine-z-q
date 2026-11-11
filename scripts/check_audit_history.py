"""Validate Issue 2 history/incorporation evidence; does not verify mathematics."""
import argparse
import copy
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = 'docs/audit-history/issue2/register.json'
STATUSES = {'prior_justification_found', 'prior_inputs_found_route_expanded',
            'attribution_or_history', 'new_argument_required', 'unresolved'}

def need(condition, message):
    if not condition:
        raise ValueError(message)

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def validate(record, read):
    need(record['schema'] == 1, 'Unknown history schema')
    need(bool(record['scope']), 'Missing scope')
    def pinned(pin):
        path = pin['path']
        need(not Path(path).is_absolute() and '..' not in Path(path).parts,
             'Non-repository path')
        raw = read(path)
        need(digest(raw) == pin['sha256'], 'Changed bound file: ' + path)
        return raw
    tex = pinned(record['manuscript']).decode('utf-8')
    # This immutable register records Version 10 history. Current-edition
    # selection and fresh application acceptance are checked separately below.
    responses = json.loads(pinned(record['responses']))
    need(record['issue'] == responses['issue'], 'Issue identity changed')
    lines = tex.splitlines(keepends=True)
    for evidence in record['evidence'].values():
        pinned(evidence)
        need(len(evidence['origin_sha256']) == 64 and evidence['origin_line_ranges'],
             'Missing origin locator')
    expected = [r['number'] for r in responses['items']]
    need([r['number'] for r in record['items']] == expected == list(range(1, 10)),
         'Missing, duplicate or reordered disposition')
    for row, response in zip(record['items'], responses['items']):
        n = str(row['number'])
        need(row['historical_status'] in STATUSES, 'Unknown historical status: ' + n)
        need(row['historical_status'] != 'unresolved', 'Unresolved history: ' + n)
        need(row['manuscript_status'] == 'incorporated', 'Incomplete incorporation: ' + n)
        need(row['assessment'].strip() and row['assessment_scope'].strip(), 'Missing assessment: ' + n)
        refs = row['historical_evidence']
        need(all(r in record['evidence'] for r in refs), 'Unknown evidence: ' + n)
        if row['historical_status'].startswith('prior_'):
            need(bool(refs), 'Prior-justification claim without evidence: ' + n)
        need(row['current_labels'] == response['labels'], 'Response label mismatch: ' + n)
        for label in row['current_labels']:
            need(tex.count('\\label{' + label + '}') == 1, 'Missing or duplicate label: ' + label)
        need(bool(row['application_spans']), 'Missing consuming passage: ' + n)
        for span in row['application_spans']:
            a, b = span['start_line'], span['end_line']
            need(isinstance(a, int) and isinstance(b, int) and 1 <= a <= b <= len(lines), 'Invalid passage: ' + n)
            need(digest(''.join(lines[a-1:b]).encode('utf-8')) == span['sha256'], 'Changed consuming passage: ' + n)

def self_test(record, read):
    cases = []
    x = copy.deepcopy(record); x['items'].pop(); cases.append(('missing item', x, read))
    x = copy.deepcopy(record); x['items'][1]['historical_evidence'] = []; cases.append(('unsupported prior proof', x, read))
    x = copy.deepcopy(record); x['items'][1]['historical_status'] = 'unresolved'; cases.append(('unresolved history', x, read))
    x = copy.deepcopy(record); x['items'][5]['application_spans'][0]['start_line'] += 1; cases.append(('shifted passage', x, read))
    x = copy.deepcopy(record); x['items'][5]['manuscript_status'] = 'pending'; cases.append(('unincorporated repair', x, read))
    evidence_path = next(iter(record['evidence'].values()))['path']
    for path in [record['manuscript']['path'], evidence_path]:
        def altered(p, target=path):
            return read(p) + b'\nchanged' if p == target else read(p)
        cases.append(('changed bytes ' + path, record, altered))
    for label, data, reader in cases:
        try:
            validate(data, reader)
        except ValueError:
            continue
        raise ValueError('Negative control unexpectedly accepted: ' + label)
    print(f'PASS: {len(cases)} negative controls rejected.')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    read = lambda p: (ROOT / p).read_bytes()
    record = json.loads(read(REGISTER))
    validate(record, read)
    print('PASS: 9 historical dispositions, evidence pins and manuscript passages. Not a mathematical proof check.')
    if args.self_test:
        self_test(record, read)
    from check_application_reviews import check_current
    check_current(read, args.self_test)

if __name__ == '__main__':
    main()
