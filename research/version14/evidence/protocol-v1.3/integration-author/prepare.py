"""Prepare a local exact-byte integration. No Git or remote mutation."""
from pathlib import Path
import hashlib
import importlib.util
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parents[2]
SOURCE = WORKSPACE / 'work/protocol-ruleset-20261107'
V13 = ROOT.parent
REPO = SOURCE / 'deployment-repository'
BASE = '18793299c641e653e32c9648c37c7a50ecd51928'
TREE = ROOT / 'tree'

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def save(path, raw):
    if path.exists() and path.read_bytes() != raw:
        raise ValueError('refusing to overwrite changed integration artifact: ' + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

def main():
    overlay_paths = set()
    for directory in (V13 / 'gate-author', V13 / 'gate-author/runtime-r2'):
        overlay_paths.update(json.loads((directory / 'CANDIDATE.json').read_text())['files'])
    baseline = {}
    for entry in git('ls-tree', '-rz', '--full-tree', BASE).split(b'\0'):
        if not entry:
            continue
        metadata, raw_path = entry.split(b'\t', 1)
        mode, kind, oid = metadata.decode().split()
        path = raw_path.decode()
        if kind != 'blob' or mode != '100644':
            raise ValueError('unsupported baseline entry: ' + path)
        raw = git('cat-file', 'blob', oid)
        if path not in overlay_paths:
            save(TREE / path, raw)
        baseline[path] = {'git_blob': oid, 'sha256': sha(raw)}
    accepted = {}
    for directory in (V13 / 'gate-author', V13 / 'gate-author/runtime-r2'):
        manifest = json.loads((directory / 'CANDIDATE.json').read_text())
        for path, expected in manifest['files'].items():
            source = directory / path
            raw = source.read_bytes()
            if sha(raw) != expected:
                raise ValueError('accepted source digest mismatch: ' + str(source))
            destination = TREE / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(raw)
            accepted[path] = {'sha256': expected, 'source': str(source.relative_to(WORKSPACE))}
    if hashlib.sha256((SOURCE/'controller/stage_bundle.py').read_bytes()).hexdigest() != '191cd76f17740153c958fb41d87a05a1a670a6d67dbfa8a383b72bc0d3e01a9b':
        raise ValueError('baseline staging-tool digest changed')
    spec = importlib.util.spec_from_file_location('staging', SOURCE / 'controller/stage_bundle.py')
    staging = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(staging)
    staging.SOURCE = TREE
    tests = tuple(dict.fromkeys((*staging.TESTS, 'adapter/test_coverage_gate.py', 'controller/test_runtime_coverage.py')))
    production, production_edges, external = staging.closure(staging.PRODUCTION)
    test_files, test_edges, test_external = staging.closure(tests)
    # Validate every literal live-profile dependency against the integrated bytes.
    import ast
    pins = {}
    for path in ('adapter/live_protocol_context.py', 'adapter/live_protocol_context_forks.py'):
        module = ast.parse((TREE / path).read_text())
        for node in module.body:
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
                try:
                    candidate = ast.literal_eval(node.value)
                except (ValueError, TypeError):
                    continue
                if candidate and all(isinstance(k, str) and k.endswith('.py') and isinstance(v, str) and len(v) == 64 for k, v in candidate.items()):
                    for name, digest in candidate.items():
                        actual = sha((TREE / 'adapter' / name).read_bytes())
                        if actual != digest:
                            raise ValueError('live dependency pin mismatch: ' + path + ' -> ' + name)
                    pins[path] = candidate
    if len(pins) != 2:
        raise ValueError('both live dependency maps must be validated')
    result = {'schema': 'protocol-v13-local-integration/v1', 'baseline_commit': BASE,
        'baseline_files': baseline, 'accepted_overlays': accepted,
        'production_roots': staging.PRODUCTION, 'test_roots': tests,
        'production_files': sorted(production), 'test_files': sorted(test_files),
        'production_edges': production_edges, 'test_edges': test_edges,
        'external_production_imports': sorted(external), 'external_test_imports': sorted(test_external),
        'validated_live_dependency_maps': pins,
        'configuration_status': 'baseline configuration preserved; actual v1.3 contexts and profiles not supplied',
        'deployment_authorized': False}
    save(ROOT / 'INTEGRATION.json', (json.dumps(result, indent=2, sort_keys=True) + '\n').encode())
    print(json.dumps({'accepted_overlays': len(accepted), 'production_files': len(production), 'test_roots': len(tests), 'manifest_sha256': sha((ROOT / 'INTEGRATION.json').read_bytes())}))

if __name__ == '__main__':
    main()
