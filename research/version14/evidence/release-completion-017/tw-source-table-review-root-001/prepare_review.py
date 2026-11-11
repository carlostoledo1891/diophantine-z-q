"""Freeze the author's source table and reproduce its exact-byte checks.

This script checks identities, not mathematical correctness.
"""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
AUTHOR = ROOT / 'work/source-risk-review-20261107/item210-source-disposition-001'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def record(path):
    data = path.read_bytes()
    return {'path': path.relative_to(ROOT).as_posix(), 'sha256': digest(data), 'bytes': len(data)}

frozen = OUT / 'frozen-input'
frozen.mkdir(exist_ok=True)
snapshots = []
for name in ('TW-SOURCE-DISCHARGE.json', 'SOURCE-PINS.json'):
    source, dest = AUTHOR / name, frozen / name
    if dest.exists():
        assert dest.read_bytes() == source.read_bytes(), f'Changed source: {source}'
    else:
        shutil.copyfile(source, dest)
    snapshots.append({'author_file': record(source), 'frozen_copy': record(dest)})

pins = json.loads((frozen / 'SOURCE-PINS.json').read_text(encoding='utf-8'))
table = json.loads((frozen / 'TW-SOURCE-DISCHARGE.json').read_text(encoding='utf-8'))
checks = []
for key, expected in pins.items():
    actual = record(ROOT / expected['path'])
    assert actual == expected, (key, actual, expected)
    checks.append({'source': key, 'match': True})
span_checks = []
for row in table['rows']:
    for span in row['consumer_spans']:
        p = ROOT / span['file']['path']
        assert record(p) == span['file']
        lines = p.read_bytes().split(b'\n')
        # Author uses LF-separated components, rejoined including the final LF.
        chunk = b'\n'.join(lines[span['start_line']-1:span['end_line']]) + b'\n'
        assert digest(chunk) == span['raw_sha256'], (row['id'], span['start_line'])
        span_checks.append({'id': row['id'], 'start_line': span['start_line'],
                            'end_line': span['end_line'], 'match': True})
result = {'scope': 'Exact identities and raw LF consumer spans only; no mathematical verdict.',
          'author': '/root/astra_quartic_opt05_anchor', 'freezer_reviewer': '/root',
          'snapshots': snapshots, 'source_checks': checks, 'span_checks': span_checks}
(OUT / 'CHECKS.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'source_pins': len(checks), 'spans': len(span_checks), 'pass': True}))
