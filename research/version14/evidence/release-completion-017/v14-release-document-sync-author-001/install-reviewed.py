import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

base = Path(__file__).resolve().parents[3]
risk = base / 'work/source-risk-review-20261107'
packet = Path(__file__).resolve().parent
repo = base / 'work/quartic-v14-release/preview-repository'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest_path = packet / 'MANIFEST.json'
review_path = risk / 'v14-release-document-sync-review-h6-001/REVIEW.json'
assert sha(manifest_path) == '742f8fd84045a98288c2a9b004b8cef6e165123e463c7e4e605560d789fd5a80'
assert sha(review_path) == '8ea50cdca74df994aa731e725d81f661e8f418f22e315555dddb10b2f6f41adb'
manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
pins = {row['path']: row for row in manifest['files']}
for name, row in pins.items():
    path = packet / name
    assert sha(path) == row['sha256'], name
    assert path.stat().st_size == row['bytes'], name

changes = []
for name, row in pins.items():
    if not name.startswith('overlay/'):
        continue
    relative = name.removeprefix('overlay/')
    destination = (repo / relative).resolve()
    assert destination.is_relative_to(repo.resolve())
    before = pins['inputs/' + relative]['sha256']
    assert sha(destination) == before, relative
    changes.append((relative, destination, packet / name, before, row['sha256']))
assert len(changes) == 9

for relative, destination, source, before, after in changes:
    destination.write_bytes(source.read_bytes())
    assert sha(destination) == after, relative

receipt = {
    'installed_at': datetime.now(timezone.utc).isoformat(),
    'manifest_sha256': sha(manifest_path),
    'review_sha256': sha(review_path),
    'scope': 'Install independently reviewed nine-file release-document overlay; no public acceptance or publication claim.',
    'files': [{'path': p, 'before_sha256': b, 'after_sha256': a} for p, _, _, b, a in changes],
}
(packet / 'INSTALLATION.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'installed_files': len(changes), 'receipt_sha256': sha(packet / 'INSTALLATION.json')}))

checklist = risk / 'v14-item28-checklist-root-001'
prior = json.loads((checklist / 'PROGRESS-003.json').read_text(encoding='utf-8'))
evidence_names = [
    'v14-integration-source-line-index-work-001/FINAL-STATE.json',
    'v14-integration-source-line-index-work-001/final-coverage-review/REVIEW-GI.json',
    'v14-seven-root-assembly-review-arithmetic-002/REVIEW.json',
    'v14-sign-pending-resolution-002/REVIEW-GI.json',
    'v14-final-main-edit-batch-root-002/CANONICAL-INSTALLATION.json',
    'v14-integration-source-line-index-work-001/final-contracts/ACTUAL-SELF-TEST.json',
]
summary = {
    'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'basis': 'Successor status against installed 5882a770 manuscript. Existing independent reports are cited, not recreated or converted into authenticated public acceptances.',
    'main_sha256': sha(repo / 'manuscripts/quartic_v14.tex'),
    'rows': [{'id': row['id'], 'status': 'Internal content review complete; public gate acceptance separate'} for row in prior['rows']],
    'remaining_release_obligations': [
        'Authenticated eligible Astra run/review evidence and controller coverage continuity',
        'Final source commit and passing required public checks',
        'Cumulative handoff package, fresh restore, public and private publication readbacks',
    ],
    'evidence': [{'path': name, 'sha256': sha(risk / name)} for name in evidence_names],
    'limits': 'This is checklist reconciliation based on scoped accepted reviews and final coverage. It is not a new mathematical review, provider model attestation, or public release approval.',
}
(checklist / 'PROGRESS-004.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'checklist': str(checklist / 'PROGRESS-004.json'), 'sha256': sha(checklist / 'PROGRESS-004.json')}))
