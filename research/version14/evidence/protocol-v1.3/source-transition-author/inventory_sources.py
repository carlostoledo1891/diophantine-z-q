"""Prepare unsigned closure evidence from frozen local inputs; no remote operations.

This is a review proposal, not an installable exact-context transition. The final
head/PR/merge do not exist yet. All future committed blobs must be rechecked.
"""
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREVIEW = ROOT / 'work/quartic-v14-release/preview-repository'
INSTALL = ROOT / 'work/quartic-v14-prep/inventory/final-records-002/install-root'
REVISION = 'docs/manuscript-revisions/version14/'
PACKAGE = 'quartics/quartic-299-314/'
FOUR = ('.github/workflows/manuscript-integration.yml', '.github/workflows/research-checks.yml',
        'scripts/build_paper.py', 'scripts/render_quartic_review.py')
BASES = {1446122118: '9c0b3aba60d90fdcac82115f0582a6f52f1054f7',
         1447509909: '225a60c6eb38d3b8aafc792ea8fccd4ecf7a84bd'}


def sha(raw): return hashlib.sha256(raw).hexdigest()
def load(path): return json.loads(path.read_bytes())
def dump(path, value): path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n', encoding='utf-8', newline='\n')
def git(repo, *args): return subprocess.check_output(['git', '-C', str(repo), *args], stderr=subprocess.PIPE)


def main():
    inventory_path = INSTALL / (REVISION + 'inventory-install-manifest.json')
    inventory = load(inventory_path)
    old_path = ROOT / 'work/protocol-ruleset-20261107/protocol-v1.2/deployment-v1/config.json'
    jobs = load(old_path)['jobs']
    additions = {}; origins = {}
    def add(path, raw, origin):
        digest = sha(raw)
        assert path not in additions or additions[path] == digest, ('conflicting frozen source', path)
        additions[path] = digest; origins.setdefault(path, []).append(origin)
    for name in FOUR:
        raw = (PREVIEW / name).read_bytes()
        assert raw == (ROOT / 'work/quartic-v14-release-r4/ci-preview-001' / name).read_bytes(), name
        add(name, raw, 'independently-reviewed-r4')
    for prefix in (PACKAGE, REVISION):
        for path in sorted((PREVIEW / prefix).rglob('*')):
            if path.is_file(): add(path.relative_to(PREVIEW).as_posix(), path.read_bytes(), 'current-preview')
    add('manuscripts/quartic_v14.tex', (PREVIEW / 'manuscripts/quartic_v14.tex').read_bytes(), 'current-preview')
    for name, pin in inventory['files'].items():
        raw = (INSTALL / name).read_bytes(); assert sha(raw) == pin['sha256'] and len(raw) == pin['bytes'], name
        add(name, raw, 'frozen-author-inventory-pending-review')
    add(REVISION + 'inventory-install-manifest.json', inventory_path.read_bytes(), 'frozen-author-inventory-pending-review')
    dependencies = inventory['readOnlyDependencies']
    for name, pin in dependencies.items():
        raw = (PREVIEW / name).read_bytes()
        assert sha(raw) == pin['sha256'] and len(raw) == pin['bytes'], name
        add(name, raw, 'frozen-inventory-read-only-dependency')
    proposals = []
    for job in jobs:
        policy = job['policy']; rid = policy['repository_id']; base = BASES[rid]
        repo = PREVIEW if rid == 1446122118 else ROOT / 'work/quartic-version6-release/private-repository'
        old = {policy['policy_path']: policy['policy_sha256']}
        for workflow in policy['workflows']:
            for name, digest in workflow['source_sha256'].items():
                assert name not in old or old[name] == digest
                old[name] = digest
        tree_paths = set(git(repo, 'ls-tree', '-r', '--name-only', base).decode().splitlines())
        for name, digest in old.items():
            assert sha(git(repo, 'show', base + ':' + name)) == digest, ('predecessor/base mismatch', rid, name)
        combined = dict(old); combined.update(additions)
        old_side = {name: sha(git(repo, 'show', base + ':' + name)) if name in tree_paths else None for name in combined}
        proposals.append({'repository': policy['repository'], 'repository_id': rid, 'base': base,
            'head': None, 'pull_request': None, 'merge': None,
            'status': 'unsigned-closure-proposal-not-installable',
            'predecessor_source_count': len(old), 'proposed_source_count': len(combined),
            'sources': {'base': old_side, 'head': combined, 'merge': dict(combined)},
            'changed_existing_paths': sorted(name for name in old if combined[name] != old[name]),
            'added_closure_paths': sorted(set(combined) - set(old))})
    result = {'schema': 'v14-source-closure-proposal/v1', 'proposals': proposals,
        'input_pins': {'predecessor_config': sha(old_path.read_bytes()), 'inventory_manifest': sha(inventory_path.read_bytes())},
        'added_path_origins': origins,
        'pending': ['Independent acceptance of final author inventory and exact final source map.',
                    'Final register/report/archive inputs may add or change paths; re-audit every actual CI read.',
                    'Actual head, PR and test-merge identities and complete committed Git blob verification.',
                    'Separate approval of the final protected transition configuration; no approval inferred here.']}
    dump(HERE / 'evidence/V14-SOURCE-CLOSURE-PROPOSAL.json', result)
    print(json.dumps({'repositories': [{k: p[k] for k in ('repository', 'base', 'predecessor_source_count', 'proposed_source_count', 'changed_existing_paths')} for p in proposals], 'inventory_manifest_sha256': sha(inventory_path.read_bytes())}, indent=2))


if __name__ == '__main__': main()
