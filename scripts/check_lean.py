#!/usr/bin/env python3
"""Verify the fixed helper snapshot; optionally compile it in a fresh output tree."""
import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time
import threading

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "lean"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args, *, cwd=PROJECT, env=None):
    return subprocess.run(args, cwd=cwd, env=env, capture_output=True, check=True)


def code_only(text):
    """Remove nested Lean comments and quoted strings for the supplementary lint."""
    out = []; i = 0; depth = 0
    while i < len(text):
        if depth:
            if text.startswith('/-', i): depth += 1; i += 2
            elif text.startswith('-/', i): depth -= 1; i += 2
            else: out.append('\n' if text[i] == '\n' else ' '); i += 1
        elif text.startswith('/-', i): depth = 1; out.append(' '); i += 2
        elif text.startswith('--', i):
            end = text.find('\n', i); i = len(text) if end == -1 else end
        elif text[i] == '"':
            i += 1; out.append(' ')
            while i < len(text):
                if text[i] == '\\': i += 2
                elif text[i] == '"': i += 1; break
                else: i += 1
        else: out.append(text[i]); i += 1
    if depth: raise ValueError('Unclosed Lean comment')
    return ''.join(out)


def main():
    if not __debug__:
        raise RuntimeError('Run without Python -O: validation assertions must be enabled')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', action='store_true')
    parser.add_argument('--dependencies', type=Path, default=PROJECT / '.lake/packages',
                        help='Pinned Lake packages; shared caches are read only')
    parser.add_argument('--lean', default='lean', help='Lean executable for the pinned toolchain')
    parser.add_argument('--jobs', type=int, default=2, choices=range(1, 5),
                        help='Concurrent project compilers, between 1 and 4')
    parser.add_argument('--output', type=Path,
                        help='A NEW directory for project artifacts, logs and receipts')
    args = parser.parse_args()
    manifest = json.loads((PROJECT / 'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
    rows = manifest['files']; modules = {r['module']: r for r in rows if 'module' in r}
    assert len(modules) == 48 and manifest['main_theorem_proved'] is False
    for row in rows:
        assert sha(PROJECT / row['path']) == row['sha256'], row['path']
    imports = {}
    for mod, row in modules.items():
        code = code_only((PROJECT / row['path']).read_text(encoding='utf-8'))
        assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide|implemented_by)\b', code), mod
        assert not re.search(r'^\s*(?:private\s+|public\s+)?constant\s', code, re.M), mod
        assert 'skipKernelTC' not in code, mod
        deps = re.findall(r'^\s*(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?([\w.]+)', code, re.M)
        assert all(d in modules for d in deps if d.startswith('ZInQ.')), mod
        assert not any(d.startswith('Frozen') for d in deps), mod
        imports[mod] = {d for d in deps if d in modules}
    root_code = code_only((PROJECT / 'ZInQ.lean').read_text(encoding='utf-8'))
    root_imports = re.findall(r'^public import ([\w.]+)$', root_code, re.M)
    assert set(root_imports) == set(modules) and len(root_imports) == 48
    frozen = code_only((PROJECT / manifest['quarantined_target']).read_text(encoding='utf-8'))
    assert len(re.findall(r'\bsorry\b', frozen)) == 1
    assert set(PROJECT.glob('ZInQ/*.lean')) == {PROJECT / r['path'] for r in modules.values()}
    print(json.dumps({'source_check': 'PASS', 'byte_identical_modules': 48,
                      'main_theorem_proved': False, 'quarantined_sorries': 1}), flush=True)
    if not args.build: return

    dependencies = args.dependencies.resolve()
    lake_manifest = json.loads((PROJECT / 'lake-manifest.json').read_text(encoding='utf-8'))
    libraries = []; pins = []
    for package in lake_manifest['packages']:
        folder = dependencies / package['name']
        assert folder.is_dir(), f'Missing dependency {folder}; run lake exe cache get first'
        actual = run(['git', '-c', 'safe.directory=' + str(folder), 'rev-parse', 'HEAD'], cwd=folder).stdout.decode().strip()
        assert actual == package['rev'], package['name']
        run(['git', '-c', 'safe.directory=' + str(folder), 'diff', '--quiet', 'HEAD', '--'], cwd=folder)
        library = folder / '.lake/build/lib/lean'
        if library.is_dir(): libraries.append(library)
        pins.append({'name': package['name'], 'revision': actual})
    version = run([args.lean, '--version']).stdout.decode().strip()
    assert 'version 4.35.0,' in version, version
    output = (args.output or PROJECT / '.checks' / str(time.time_ns())).resolve()
    assert not output.exists(), 'Output directory must be new; old project artifacts are never reused'
    output.mkdir(parents=True); lib = output / 'lib'; lib.mkdir()
    env = os.environ.copy()
    env.pop('LEAN_SRC_PATH', None)
    env['LEAN_PATH'] = os.pathsep.join(str(p) for p in [lib, *libraries])
    pending = dict(imports); order = []
    while pending:
        ready = sorted(k for k, deps in pending.items() if not deps.intersection(pending))
        assert ready, 'Cyclic project imports'
        for name in ready: order.append(name); del pending[name]
    commands = []; started = time.monotonic(); log_lock = threading.Lock()
    def compile_file(label, path, target=None):
        argv = [args.lean, '-j1', '-Ddebug.skipKernelTC=false']
        if target:
            target.parent.mkdir(parents=True, exist_ok=True)
            argv += ['-o', str(target)]
        argv += [str(path)]
        before = time.monotonic()
        result = subprocess.run(argv, cwd=PROJECT, env=env, capture_output=True)
        log = result.stdout + result.stderr
        (output / (label + '.log')).write_bytes(log)
        entry = {'target': label, 'exit_code': result.returncode, 'seconds': round(time.monotonic()-before, 3)}
        with log_lock:
            commands.append(entry)
            print(json.dumps(entry), flush=True)
            (output / 'commands.json').write_text(json.dumps(commands, indent=2)+'\n')
        if result.returncode:
            raise RuntimeError(f'Compilation failed for {label}; see {output / (label + ".log")}')
        return log.decode(encoding='utf-8', errors='replace')
    waiting = set(order); completed = set(); active = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        while waiting or active:
            for mod in sorted(waiting):
                if len(active) >= args.jobs: break
                if not imports[mod].issubset(completed): continue
                future = pool.submit(compile_file, mod, PROJECT / modules[mod]['path'],
                                     lib / (mod.replace('.', '/') + '.olean'))
                active[future] = mod; waiting.remove(mod)
            assert active, 'Unsatisfied module dependency'
            done, _ = concurrent.futures.wait(active, return_when=concurrent.futures.FIRST_COMPLETED)
            for future in done:
                future.result(); completed.add(active.pop(future))
    compile_file('ZInQ', PROJECT / 'ZInQ.lean', lib / 'ZInQ.olean')
    audit = compile_file('axioms', PROJECT / 'Checks/Axioms.lean')
    match = re.search(r'AXIOM_AUDIT_PASS declarations=(\d+) modules=(\d+)', audit)
    assert match and int(match[2]) == 48 and int(match[1]) >= 463
    result = {'status': 'PASS', 'toolchain': version, 'dependency_pins': pins,
              'source_manifest_sha256': sha(PROJECT/'SOURCE_MANIFEST.json'),
              'project_modules_freshly_compiled': 48, 'root_compiled': True,
              'declarations_axiom_checked': int(match[1]), 'allowed_axioms': manifest['allowed_axioms'],
              'main_theorem_proved': False, 'quarantined_target_compiled': False,
              'dependency_libraries': 'Prebuilt cache at verified source revisions; not rebuilt',
              'project_artifact_reuse': False, 'seconds': round(time.monotonic()-started, 3)}
    (output/'RESULT.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result), flush=True)


if __name__ == '__main__': main()
