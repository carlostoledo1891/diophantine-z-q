"""Curate a local deployment tree. Never commits, pushes, or copies credentials.

Static imports are traversed inside the four declared code directories, including
imports inside functions. Explicit dynamic fixture loads are recorded below.
Production inputs require a separate allowlisted overlay manifest from the owner.
"""
from pathlib import Path
import argparse
import ast
import hashlib
import json
import sys

SOURCE = Path(__file__).resolve().parents[1]
CODE_DIRS = ('controller', 'adapter', 'publisher', 'gate', 'immutable-cache')
PRODUCTION = ('controller/runtime.py', 'controller/ingress.py', 'controller/quota_probe.py')
TESTS = ('controller/test_runtime.py', 'controller/test_ingress.py', 'controller/test_git_state.py',
         'publisher/test_github_app_transport.py', 'adapter/test_live_protocol_context_forks.py',
         'immutable-cache/test_immutable_git_cache.py', 'controller/test_runtime_idle.py',
         'controller/test_controller_blob_cache.py', 'controller/test_pr_state_projection.py',
         'adapter/test_source_bound_ci.py')
DYNAMIC = {'adapter/test_manifest_gate.py': ('gate/test_offline_gate.py',)}
DOCUMENTS = (
    'CURRENT-OPERATION.md', 'DEPLOYMENT-STATUS.md',
    'controller/COMPOSITION-REVIEW.md',
    'independent-review/compact-policy-sol/PUBLISHER-REUSE-ACCEPTANCE.md',
    'independent-review/compact-policy-sol/DIAGNOSTICS-REVIEW.md',
    'independent-review/compact-policy-sol/REFRESH-REVIEW.md',
    'independent-review/compact-policy-sol/PROJECTION-REVIEW.md',
    'pr-state-audit/FILES.json', 'pr-state-audit/ANALYSIS.md',
    'pr-state-audit/REPRODUCTION.json', 'pr-state-audit/INTEGRATION-REVIEW.md',
    'adapter/GITHUB-READ-CONTEXT.md',
    'adapter/SOURCE-BOUND-CI.md',
    'pr10-state-diagnosis/V3-INTEGRATED-REVIEW.md',
    'pr10-state-diagnosis/V3-PROJECTION-CHECKS.json',
    'pr10-state-diagnosis/V3-REFRESH-CHECKS.json',
    'pr10-state-diagnosis/V3-FULL-PINS.json',
    'pr10-state-diagnosis/V3-RUNTIME-TESTS.log',
    'pr10-state-diagnosis/V3-REGRESSION-TESTS.log',
    'pr10-state-diagnosis/DIFF.json',
    'pr10-state-diagnosis/CONTEXT.json',
    'pr10-state-diagnosis/OPERATIONAL-REVIEW.md',
    'pr10-state-diagnosis/OPERATIONAL-CHECKS.json',
    'independent-review/source-bound-ci-sol/REVIEW.md',
    'protocol-v1.2/final-review/source-bound-implementation/AUTHOR-REPORT.md',
    'protocol-v1.2/final-review/source-bound-implementation/CANDIDATE.json',
    'protocol-v1.2/final-review/source-bound-implementation/ROOT-TESTS.json',
    'independent-review/compact-policy-sol/publisher-reuse-independent.json',
    'independent-review/compact-policy-sol/CONTROLLER-CACHE-ACCEPTANCE.md',
    'independent-review/compact-policy-sol/CONTROLLER-QUOTA-REVIEW.md',
    'independent-review/compact-policy-sol/REVIEW.md',
    'independent-review/compact-policy-sol/REPAIRED-ACCEPTANCE.md',
    'independent-review/compact-policy-sol/repaired-verification.json',
    'setup-packets/sol-final-review/REVIEW.md',
    'setup-packets/sol-final-review/decisions.json',
    'setup-packets/sol-final-review/INGRESS-REVIEW.md',
    'controller/MEMORY-CACHE-INTEGRATION.json',
    'independent-review/deployment-review/ingress/REVIEW.md',
    'DEPLOYMENT-DECISION.md', 'USER-CHOICE.json', 'STATE-BOOTSTRAPPED.json',
    'controller/RUNTIME.md', 'controller/INGRESS.md', 'controller/requirements.lock',
    'controller/DEPENDENCY-SOURCES.json', 'controller/RUNTIME-VERIFICATION.json',
    'controller/INGRESS-VERIFICATION.json', 'controller/BOOTSTRAP-CHECK.json',
    'controller/workflow.template.yml', 'controller/ingress.workflow.template.yml',
    'publisher/TRANSPORT.md', 'publisher/TRANSPORT-MANIFEST.json',
    'adapter/LIVE-FORK-PROFILE.md', 'adapter/LIVE-FORK-VERIFICATION.json',
    'adapter/FORK-AND-RESTORE.md', 'adapter/DURABLE-INTAKE.md',
    'independent-review/publisher/REVIEW.md', 'independent-review/publisher/acceptance.json',
    'independent-review/publisher/TRANSPORT-REVIEW.md',
    'independent-review/publisher/transport-acceptance.json',
    'independent-review/publisher/RUNTIME-CHECKS.json',
    'independent-review/adapter/FORK-RESTORE-REVIEW.md',
    'independent-review/adapter/LEDGER-REVIEW.md',
    'independent-review/adapter/DURABLE-INTAKE-REVIEW.md',
    'independent-review/adapter/STORE-BRIDGE-REVIEW.md',
    'independent-review/adapter/SCHEMA2-REVIEW.md',
    'independent-review/deployment-review/state/REVIEW.md',
    'immutable-cache/README.md', 'immutable-cache/MANIFEST.json',
    'independent-review/immutable-cache/REVIEW.md', 'independent-review/immutable-cache/acceptance.json',
)
OPTIONAL_REVIEWS = ('independent-review/publisher/RUNTIME-REVIEW.md',
                    'independent-review/publisher/runtime-acceptance.json',
                    'independent-review/adapter/INGRESS-REVIEW.md')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def safe_relative(value):
    p = Path(value)
    if not isinstance(value, str) or p.is_absolute() or any(x in ('', '.', '..') for x in value.split('/')) or '\\' in value:
        raise ValueError('invalid curated relative path')
    return p


def closure(seeds):
    modules = {}
    for directory in CODE_DIRS:
        for p in (SOURCE/directory).glob('*.py'):
            modules.setdefault(p.stem, []).append(p.relative_to(SOURCE).as_posix())
    pending = list(seeds)
    found = set()
    edges = {}
    external = set()
    while pending:
        relative = pending.pop()
        if relative in found:
            continue
        found.add(relative)
        tree = ast.parse((SOURCE/relative).read_text(encoding='utf-8-sig'))
        names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names.update(x.name.split('.')[0] for x in node.names)
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                names.add(node.module.split('.')[0])
        dependencies = set(DYNAMIC.get(relative, ()))
        for name in names:
            choices = modules.get(name, [])
            if choices:
                if len(choices) != 1:
                    raise ValueError('ambiguous local module: '+name)
                dependencies.add(choices[0])
            elif name not in sys.stdlib_module_names:
                external.add(name)
        edges[relative] = sorted(dependencies)
        pending.extend(dependencies)
    return found, edges, external


def stage(output, overlay=None):
    output = output.resolve()
    if output != SOURCE/'deployment-bundle':
        raise ValueError('staging is restricted to the designated deployment-bundle directory')
    production, prod_edges, prod_external = closure(PRODUCTION)
    tests, test_edges, test_external = closure(TESTS)
    # The schema1 source is included for its explicit fixture dependency. It is
    # not selected as the production schema2 validator.
    selected = {p: (p, 'production' if p in production else 'test-only') for p in production | tests}
    for relative in DOCUMENTS:
        selected[relative] = (relative, 'documentation-or-evidence')
    missing_reviews = []
    for relative in OPTIONAL_REVIEWS:
        if (SOURCE/relative).is_file():
            selected[relative] = (relative, 'documentation-or-evidence')
        else:
            missing_reviews.append(relative)
    selected['.github/workflows/protocol-controller.yml'] = ('controller/workflow.template.yml', 'workflow')
    selected['.github/workflows/protocol-ingress.yml'] = ('controller/ingress.workflow.template.yml', 'workflow')
    selected['.github/workflows/protocol-quota-probe.yml'] = ('controller/quota.workflow.template.yml', 'workflow')
    if overlay is not None:
        rows = json.loads(overlay.read_text())
        if type(rows) is not dict:
            raise ValueError('input overlay must map destination paths to source-relative paths')
        for destination, source in rows.items():
            safe_relative(destination); safe_relative(source)
            if not (destination == 'controller/config.json' or
                    destination.startswith('packets/') or destination.startswith('controller/ingress-batches/')):
                raise ValueError('overlay is not a protected data path')
            if not destination.endswith('.json') or destination in selected:
                raise ValueError('overlay cannot replace code or evidence')
            selected[destination] = (source, 'protected-owner-input')
    output.mkdir(exist_ok=True)
    manifest = {}
    for destination, (source, role) in sorted(selected.items()):
        safe_relative(destination); safe_relative(source)
        path = SOURCE/source
        if path.resolve() != path or not path.is_file():
            raise ValueError('curated source missing or symlink: '+source)
        raw = path.read_bytes()
        if b'-----BEGIN PRIVATE KEY-----' in raw or b'-----BEGIN RSA PRIVATE KEY-----' in raw:
            raise ValueError('private key bytes forbidden in bundle')
        target = output/destination
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.resolve() != target:
            raise ValueError('bundle destination symlink')
        target.write_bytes(raw)
        manifest[destination] = {'sha256': sha(raw), 'bytes': len(raw), 'source': source, 'role': role}
    readme = (
        '# Curated controller deployment staging\n\n'
        'No commit or push is performed by this staging tool. Runtime and ingress\n'
        'use only the files marked production and workflow in BUNDLE-MANIFEST.json.\n'
        'Test-only files contain synthetic observations and fake HTTP transports.\n'
        'They are never production observations, receipts, configuration or packets.\n\n'
        'Protected config and packet overlays must be supplied by the owner. This\n'
        'tree does not contain credentials or a copy of remote protocol-state.\n'
        'The bootstrap record documents an earlier observation, not a live read.\n\n'
        'Runtime smoke test: from controller/, run python -B -m unittest\n'
        'test_runtime test_ingress test_git_state -v. Full transport tests run\n'
        'separately from publisher/ and require the locked cryptography dependency.\n'
    ).encode()
    (output/'BUNDLE-README.md').write_bytes(readme)
    manifest['BUNDLE-README.md'] = {'sha256': sha(readme), 'bytes': len(readme), 'source': None, 'role': 'staging-note'}
    allowed = set(manifest) | {'BUNDLE-MANIFEST.json'}
    extras = [p.relative_to(output).as_posix() for p in output.rglob('*') if p.is_file() and p.relative_to(output).as_posix() not in allowed]
    if extras:
        raise ValueError('untracked files remain in staging; not silently removed: '+repr(extras))
    result = {'schema': 'protocol-deployment-bundle/v1', 'files': manifest,
        'production_roots': list(PRODUCTION), 'production_edges': prod_edges,
        'test_edges': test_edges, 'external_production_imports': sorted(prod_external),
        'external_test_imports': sorted(test_external), 'explicit_dynamic_fixture_loads': DYNAMIC,
        'missing_optional_reviews': missing_reviews,
        'protected_config_present': 'controller/config.json' in selected,
        'limitation': 'Staging and byte inventory only, not independent acceptance or live deployment.'}
    raw = (json.dumps(result, sort_keys=True, indent=2)+'\n').encode()
    (output/'BUNDLE-MANIFEST.json').write_bytes(raw)
    print(json.dumps({'manifest_sha256': sha(raw), 'file_count': len(manifest),
                      'production_python_files': len(production), 'protected_config_present': result['protected_config_present']}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--overlay', type=Path)
    args = parser.parse_args()
    stage(SOURCE/'deployment-bundle', args.overlay)
