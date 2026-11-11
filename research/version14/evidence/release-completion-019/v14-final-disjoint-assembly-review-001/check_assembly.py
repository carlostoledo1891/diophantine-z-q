import collections
import hashlib
import json
from pathlib import Path

BASE = Path('C:/Users/glaze/Documents/Codex/2026-11-02/lo')
REPO = BASE / 'work/quartic-v14-release/preview-repository'
RISK = BASE / 'work/source-risk-review-20261107'
PREP = RISK / 'v14-integration-source-line-index-work-001/final-protocol-preparation'
TARGET = PREP / 'installable-012'
OUT = Path(__file__).parent

def read(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

errors = []
manifest = read(TARGET / 'MANIFEST.json')
for item in manifest['files']:
    p = BASE / item['path']
    if not p.is_file() or sha(p) != item['sha256']:
        errors.append(['manifest', item['path']])

rel = Path('overlay/docs/manuscript-revisions/version14/final-coverage')
dossier = read(TARGET / rel / 'DOSSIER.json')
old = read(PREP / 'installable-010' / rel / 'DOSSIER.json')
connections = read(TARGET / rel / 'CONNECTIONS.json')
prior_connections = read(PREP / 'installable-010' / rel / 'CONNECTIONS.json')
packet = read(TARGET / 'PACKET-CANDIDATE.json')
unchanged = {k: dossier[k] == old[k] for k in ['sources', 'coverage_index', 'reconciled_uses']}
unchanged['connections'] = connections['connections'] == prior_connections['connections']
for k, ok in unchanged.items():
    if not ok:
        errors.append(['changed', k])

for pin in dossier['sources']:
    p = REPO / pin['path']
    if sha(p) != pin['sha256']:
        errors.append(['source_sha', pin['path']])
    n = len(p.read_bytes().splitlines())
    covered = set()
    for row in dossier['coverage_index']:
        loc = row['location']
        if loc['pin']['path'] == pin['path']:
            covered.update(range(loc['start_line'], loc['end_line'] + 1))
    missing = sorted(set(range(1, n + 1)) - covered)
    if missing:
        errors.append(['uncovered_lines', pin['path'], missing[:20]])

uses = {u['id']: u for u in dossier['reconciled_uses']}
for c in connections['connections']:
    if c['needed_assertion'] != uses[c['use_id']]['assertion']:
        errors.append(['needed_assertion', c['use_id']])
    if c['connecting_derivation']['output_assertion'] != c['needed_assertion']:
        errors.append(['derivation_output', c['use_id']])
if set(uses) != {c['use_id'] for c in connections['connections']}:
    errors.append(['connection_coverage'])
if {f['id'] for f in packet['findings']} != {f['finding_id'] for f in connections['findings']}:
    errors.append(['finding_coverage'])
if any(f['status'] not in ['repaired', 'rebutted', 'out_of_scope', 'duplicate'] for f in packet['findings']):
    errors.append(['open_finding'])

pins = {}
def collect(obj):
    if isinstance(obj, dict):
        if obj.get('side') == 'head' and 'path' in obj and 'sha256' in obj:
            pins[(obj['path'], obj['sha256'])] = True
        for v in obj.values():
            collect(v)
    elif isinstance(obj, list):
        for v in obj:
            collect(v)
collect(packet)
stale = []
for path, expected in pins:
    p = REPO / path
    if p.is_file() and sha(p) != expected:
        stale.append(path)

artifacts = ['manuscripts/quartic_v14.tex', 'manuscripts/quartic_v14.pdf',
             'docs/manuscript-revisions/version14/APPLICATIONS.json', 'docs/audit-history/current.json',
             'README.md', 'docs/manuscript-revisions/version14/GUIDE.md',
             'docs/manuscript-revisions/version14/RELEASE-PROFILE.json',
             'research/version14/CUMULATIVE-HANDOFF.md',
             'quartics/quartic-299-symbolic-coefficients.json', 'quartics/quartic-314-fully-expanded.txt']
result = {
    'reviewer': '/root/v14_final_disjoint_assembly_review',
    'target_manifest_sha256': sha(TARGET / 'MANIFEST.json'),
    'manifest_members_checked': len(manifest['files']),
    'unchanged_from_010': unchanged,
    'counts': {'sources': len(dossier['sources']), 'uses': len(uses), 'rows': len(dossier['coverage_index']),
               'applications': len(packet['applications']), 'findings': len(packet['findings'])},
    'finding_statuses': dict(collections.Counter(f['status'] for f in packet['findings'])),
    'coverage_statuses': dict(collections.Counter(r['status'] for r in dossier['coverage_index'])),
    'source_side_errors': errors,
    'packet_unique_head_pins': len(pins),
    'packet_stale_paths': sorted(set(stale)),
    'artifacts': [{'path': p, 'sha256': sha(REPO / p)} for p in artifacts if (REPO / p).is_file()],
    'scope': 'Independent byte, physical coverage and interface-object checks. These checks do not establish arithmetic validity, source-first reconstruction independence, controller eligibility, or final Git/release acceptance.'
}
(OUT / 'CHECKS.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
