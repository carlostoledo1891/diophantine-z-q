"""Compare the two exact specifications without ignoring any mathematical field."""
from pathlib import Path
import argparse, copy, hashlib, json

p = argparse.ArgumentParser()
p.add_argument('historical', type=Path)
p.add_argument('portable', type=Path)
p.add_argument('report', type=Path)
a = p.parse_args()
sha = lambda raw: hashlib.sha256(raw).hexdigest()
old_raw, new_raw = a.historical.read_bytes(), a.portable.read_bytes()
assert len(old_raw) == 23180023 and sha(old_raw) == 'a86790bbf1095d6b1cea9c66067ad8432dd35adc320254eecde21f9f98574714'
assert len(new_raw) == 23179783 and sha(new_raw) == '4d639d4c44e69ea360d36d4591b8fdc82269d68b9363af0157d1e5c1174c7af6'
def unique_pairs(items):
    result = {}
    for k, v in items:
        assert k not in result, 'Duplicate JSON key'
        result[k] = v
    return result
old = json.loads(old_raw, object_pairs_hook=unique_pairs)
new = json.loads(new_raw, object_pairs_hook=unique_pairs)
normalized = copy.deepcopy(old)
changed = []
for name in ['precision', 'power_value']:
    left, right = old['recipes'][name]['sourceFile'], new['recipes'][name]['sourceFile']
    assert isinstance(left, str) and isinstance(right, str) and left != right
    normalized['recipes'][name]['sourceFile'] = right
    changed.append('recipes.' + name + '.sourceFile')
left, right = old['sourceHashes'], new['sourceHashes']
assert len(left) == len(right) == 1
assert list(left.keys()) != list(right.keys()) and list(left.values()) == list(right.values())
normalized['sourceHashes'] = right
changed.append('sourceHashes (one key; unchanged value)')
assert normalized == new, 'Unexpected change outside the three provenance locations'
report = {'status': 'PASS', 'method': 'Exact recursive JSON equality after precisely three asserted provenance changes; duplicate keys rejected.',
          'historical': {'bytes': len(old_raw), 'sha256': sha(old_raw)},
          'portable': {'bytes': len(new_raw), 'sha256': sha(new_raw)},
          'changed_provenance_fields': changed, 'all_other_fields_equal': True,
          'checker_sha256': sha(Path(__file__).read_bytes()),
          'limitation': 'This checks representation equality outside the specified provenance fields. It does not prove the arithmetic definition or establish from code alone that provenance labels contribute no equations.'}
a.report.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report))
