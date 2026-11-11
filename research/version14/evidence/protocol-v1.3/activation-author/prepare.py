"""Prepare accepted v1.3 runtime with an idle config and all rollout history.

Read-only Git access; writes only under this isolated preparation directory.
"""
from pathlib import Path
import copy
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
V13 = HERE.parent
PROTOCOL = V13.parent / 'protocol-ruleset-20261107'
REPO = PROTOCOL / 'deployment-repository'
BASE = 'bc56dd5efa51eaefc3007044c59ba1d063ec8aa8'
BUNDLE = V13 / 'integration-author/tree/deployment-bundle'
IDLE = PROTOCOL / 'protocol-v1.2/postmerge-idle-785efabe'
TREE = HERE / 'tree'

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def json_bytes(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()

def read_json(path):
    return json.loads(path.read_bytes())

def write(path, raw):
    if path.exists() and path.read_bytes() != raw:
        raise ValueError('preserve different frozen preparation bytes: ' + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)

def main():
    assert sha((V13 / 'integration-author/MANIFEST.json').read_bytes()) == '50c322d6a88ab0ae800bf4b9a39fd371cfac72c153514a8bcd4249b49d2ea796'
    assert sha((BUNDLE / 'BUNDLE-MANIFEST.json').read_bytes()) == 'a7a880139ca8b146d7d64f6dea64da73f940638fb92fdd3afff9c3fcc954de4a'
    assert sha((IDLE / 'overlay.json').read_bytes()) == '127c954755c2bc0a08d540c4c4dcb2b9b326c444af4687bd8aaa05879ccedcd8'
    git = ['git', '-C', str(REPO)]
    rows = subprocess.check_output(git + ['ls-tree', '-rz', '--full-tree', BASE]).split(b'\0')
    objects = []
    for row in rows:
        if not row:
            continue
        meta, path = row.split(b'\t')
        mode, kind, oid = meta.decode().split()
        assert mode == '100644' and kind == 'blob'
        objects.append((path.decode(), oid))
    data = subprocess.check_output(git + ['cat-file', '--batch'], input=('\n'.join(o for _, o in objects) + '\n').encode())
    offset = 0
    baseline = {}
    for path, oid in objects:
        end = data.index(b'\n', offset)
        got, kind, size = data[offset:end].decode().split()
        assert got == oid and kind == 'blob'
        offset = end + 1
        raw = data[offset:offset + int(size)]
        offset += int(size) + 1
        assert hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == oid
        baseline[path] = raw
    files = dict(baseline)
    staged = read_json(BUNDLE / 'BUNDLE-MANIFEST.json')
    for path, row in staged['files'].items():
        raw = (BUNDLE / path).read_bytes()
        assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
        files[path] = raw
    overlay = read_json(IDLE / 'overlay.json')
    assert len(overlay) == 20
    for path, source in overlay.items():
        raw = (PROTOCOL / source).read_bytes()
        if path != 'controller/config.json':
            assert baseline[path] == raw
        else:
            assert sha(raw) == '00c3118bc4bd74dd0871e297c9ab2d733f2185aeb24d44f0abe6ef397d5b2c97'
        files[path] = raw
    review = (V13 / 'independent-review/INTEGRATION-REVIEW.md').read_bytes()
    assert sha(review) == '418a824b52ef57f3f3ea6361e1d7e599726876324f21942376ea043e709048ba'
    files['integration-evidence/INTEGRATION-REVIEW.md'] = review
    # Preserve owner README/.gitattributes and every baseline history file.
    assert set(baseline) <= set(files)
    new_manifest = copy.deepcopy(staged)
    new_manifest['files'] = {}
    for path, raw in sorted(files.items()):
        if path == 'BUNDLE-MANIFEST.json':
            continue
        row = copy.deepcopy(staged['files'].get(path, {}))
        row.update(sha256=sha(raw), bytes=len(raw))
        if path in overlay:
            row.update(source=overlay[path], role='protected-owner-input')
        elif path not in staged['files']:
            row.update(source=None, role='preserved-owner-file' if path in baseline else 'independent-review')
        new_manifest['files'][path] = row
    new_manifest['protected_config_present'] = True
    files['BUNDLE-MANIFEST.json'] = json_bytes(new_manifest)
    changes = []
    for path, raw in sorted(files.items()):
        write(TREE / path, raw)
        if baseline.get(path) != raw:
            changes.append({'path': path, 'base_sha256': sha(baseline[path]) if path in baseline else None,
                            'candidate_sha256': sha(raw), 'bytes': len(raw)})
    # Every production byte comes from the already accepted combined bundle.
    for path, row in staged['files'].items():
        assert sha(files[path]) == row['sha256']
    assert read_json(TREE / 'controller/config.json')['jobs'] == []
    result = {'schema': 'v13-idle-activation-preparation/v1',
        'author': '/root/protocol_v12_acceptance', 'baseline_commit': BASE,
        'postmerge_idle_commit': None, 'future_activation_commit': None,
        'deployment_precondition': 'Both exact v1.2 normal merges and their complete immutable readbacks succeeded.',
        'accepted_bundle_manifest_sha256': sha((BUNDLE / 'BUNDLE-MANIFEST.json').read_bytes()),
        'accepted_integration_review_sha256': sha(review), 'source_code_changed_from_accepted_bundle': False,
        'history_mappings_preserved': 20, 'nonconfig_history_files_byte_identical': 19,
        'base_file_count': len(baseline), 'candidate_file_count': len(files), 'removed_paths': [],
        'changes_from_bc56dd5': changes,
        'files': {p: {'sha256': sha(raw), 'bytes': len(raw)} for p, raw in sorted(files.items())},
        'actual_v13_pr_packets_or_profiles_created': False, 'remote_mutations': False}
    write(HERE / 'ACTIVATION.json', json_bytes(result))
    print(json.dumps({'candidate_files': len(files), 'changed_or_added_files': len(changes),
                      'history_mappings': 20, 'jobs': [], 'deployment': 'not performed'}))

if __name__ == '__main__':
    main()
