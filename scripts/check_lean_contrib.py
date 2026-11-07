#!/usr/bin/env python3
"""Check the contributed Lean libraries beside the accepted snapshot; optionally compile them fresh.

The contributed libraries live in lean/ next to the 48-module ZInQ snapshot and leave it
untouched: lakefile.toml, ZInQ.lean, SOURCE_MANIFEST.json, Checks/Axioms.lean and the frozen
target are not edited, and scripts/check_lean.py runs first and must pass. lakefile.toml is
pinned by SOURCE_MANIFEST.json, so the libraries have no lean_lib entry; with --build this
script compiles them, and the snapshot modules they import, the way scripts/check_lean.py
compiles the snapshot: one `lean -j1 -Ddebug.skipKernelTC=false` per module, into a NEW output
directory, against the pinned dependency libraries only.

A passing check says that the contributed declarations compile, that their axioms are
propext, Quot.sound and Classical.choice, and that the printed facts equal
lean/CONTRIB_EXPECTED.json. It is not a proof of the main theorem.
"""
import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import threading
import time

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_lean  # noqa: E402  (sha, code_only and the paths of the snapshot check)

ROOT, PROJECT = check_lean.ROOT, check_lean.PROJECT
CONTRIB = ['EllipticModel', 'CondZQ']       # library roots: R.lean and R/**/*.lean
CHECKS = ['Checks/ContribAxioms.lean',      # compiled last, against the fresh libraries
          'Checks/ConditionalStatement.lean']
EXTRA = {'Frozen.BoundedIntegerPolynomial': 'Frozen/BoundedIntegerPolynomial.lean'}  # only for the checks
SPANS = [('CondZQ/Main.lean', 'Frozen/BoundedIntegerPolynomial.lean')]  # equal conclusions
PIN_SOURCES = True                          # contributed sources must have the expected SHA-256
EXPECTED = PROJECT / 'CONTRIB_EXPECTED.json'
FROZEN = 'Frozen/BoundedIntegerPolynomial.lean'
FROZEN_SHA256 = '0889579ae56e75eca811af520eb4e18c9f697e163db408771b93fdbc651a95b9'
FORBIDDEN = r'\b(sorry|admit|axiom|unsafe|native_decide|implemented_by|opaque)\b'
IMPORT = r'^\s*(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?([\w.]+)'
SORRY = r"declaration uses [`']sorry[`']"
SPAN_START = '  \u2203 P : MvPolynomial'.encode()


def contributed():
    mods = {}
    for root in CONTRIB:
        files = [PROJECT / (root + '.lean'), *sorted((PROJECT / root).rglob('*.lean'))]
        for path in files:
            rel = path.relative_to(PROJECT).with_suffix('')
            mods['.'.join(rel.parts)] = path
    return mods


def conclusion(path):
    """The bytes from the theorem's `  ∃ P : MvPolynomial` to the byte before its `:= by`."""
    data = path.read_bytes(); i = data.find(SPAN_START); j = data.find(b':= by', i)
    assert data.count(SPAN_START) == 1 and 0 <= i < j, path
    return data[i:j]


def source_check():
    snap = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/check_lean.py')],
                          cwd=ROOT, capture_output=True, text=True)
    assert snap.returncode == 0 and '"source_check": "PASS"' in snap.stdout, snap.stdout + snap.stderr
    assert check_lean.sha(PROJECT / FROZEN) == FROZEN_SHA256, 'frozen target changed'
    manifest = json.loads((PROJECT / 'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
    snapshot = {r['module']: PROJECT / r['path'] for r in manifest['files'] if 'module' in r}
    mods = contributed(); imports = {}
    for mod, path in mods.items():
        raw = path.read_text(encoding='utf-8')
        code = check_lean.code_only(raw)
        assert re.match(r'\s*module\b', code), f'{mod}: missing module header'
        assert not re.search(FORBIDDEN, code), mod
        assert not re.search(r'^\s*(?:private\s+|public\s+)?constant\s', code, re.M), mod
        assert 'skipKernelTC' not in code, mod
        deps = re.findall(IMPORT, code, re.M)
        for d in deps:
            assert d in mods or d in snapshot or d.split('.')[0] in ('Mathlib', 'Lean'), (mod, d)
        imports[mod] = [d for d in deps if d in mods or d in snapshot]
    for root in CONTRIB:  # each root imports every module under it, so the audit sees them all
        under = {m for m in mods if m.startswith(root + '.')}
        assert under <= set(re.findall(IMPORT, check_lean.code_only(mods[root].read_text(encoding='utf-8')), re.M)), root
    for check in CHECKS:
        code = check_lean.code_only((PROJECT / check).read_text(encoding='utf-8'))
        assert not re.search(r'\b(sorry|admit|axiom)\b', code), check
    spans = {}
    for ours, theirs in SPANS:  # a conclusion copied byte for byte from the frozen target
        assert conclusion(PROJECT / ours) == conclusion(PROJECT / theirs), (ours, theirs)
        spans[ours] = {'equals': theirs, 'bytes': len(conclusion(PROJECT / ours)),
                       'sha256': hashlib.sha256(conclusion(PROJECT / ours)).hexdigest()}
    sources = {p.relative_to(PROJECT).as_posix(): check_lean.sha(p)
               for p in sorted([*mods.values(), *(PROJECT / c for c in CHECKS)])}
    pinned = json.loads(EXPECTED.read_text(encoding='utf-8')).get('source_sha256', {})
    if PIN_SOURCES:  # the reviewed statements and proofs, pinned like SOURCE_MANIFEST.json pins the snapshot
        changed = sorted(k for k in set(sources) | set(pinned) if sources.get(k) != pinned.get(k))
        assert not changed, f'sources differ from CONTRIB_EXPECTED.json: {changed}'
    print(json.dumps({'contrib_source_check': 'PASS', 'snapshot_source_check': 'PASS',
                      'contributed_modules': len(mods), 'pinned_sources': len(sources),
                      'frozen_target_sha256': FROZEN_SHA256}), flush=True)
    return mods, snapshot, imports, spans, sources


def main():
    if not __debug__:
        raise RuntimeError('Run without Python -O: validation assertions must be enabled')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', action='store_true')
    parser.add_argument('--dependencies', type=Path, default=PROJECT / '.lake/packages',
                        help='Pinned Lake packages; shared caches are read only')
    parser.add_argument('--lean', default='lean', help='Lean executable for the pinned toolchain')
    parser.add_argument('--jobs', type=int, default=2, choices=range(1, 5),
                        help='Concurrent compilers, between 1 and 4')
    parser.add_argument('--output', type=Path, help='A NEW directory for artifacts, logs and receipts')
    args = parser.parse_args()
    mods, snapshot, imports, spans, sources = source_check()
    if not args.build: return

    dependencies = args.dependencies.resolve()
    lake_manifest = json.loads((PROJECT / 'lake-manifest.json').read_text(encoding='utf-8'))
    libraries = []; pins = []
    for package in lake_manifest['packages']:
        folder = dependencies / package['name']
        assert folder.is_dir(), f'Missing dependency {folder}; run lake exe cache get first'
        actual = check_lean.run(['git', '-c', 'safe.directory=' + str(folder), 'rev-parse', 'HEAD'], cwd=folder).stdout.decode().strip()
        assert actual == package['rev'], package['name']
        check_lean.run(['git', '-c', 'safe.directory=' + str(folder), 'diff', '--quiet', 'HEAD', '--'], cwd=folder)
        library = folder / '.lake/build/lib/lean'
        if library.is_dir(): libraries.append(library)
        pins.append({'name': package['name'], 'revision': actual})
    version = check_lean.run([args.lean, '--version']).stdout.decode().strip()
    assert 'version 4.35.0,' in version, version
    output = (args.output or PROJECT / '.checks' / ('contrib-' + str(time.time_ns()))).resolve()
    assert not output.exists(), 'Output directory must be new; old project artifacts are never reused'
    output.mkdir(parents=True); lib = output / 'lib'; lib.mkdir()
    env = os.environ.copy()
    env.pop('LEAN_SRC_PATH', None)
    env['LEAN_PATH'] = os.pathsep.join(str(p) for p in [lib, *libraries])

    # the contributed modules, the snapshot modules they reach, and the extra check-only modules
    for mod, path in snapshot.items():
        imports.setdefault(mod, [d for d in re.findall(IMPORT, check_lean.code_only(path.read_text(encoding='utf-8')), re.M) if d in snapshot])
    paths = {**snapshot, **mods, **{m: PROJECT / p for m, p in EXTRA.items()}}
    for m, p in EXTRA.items():
        imports[m] = []
    needed = set(); stack = [*mods, *EXTRA]
    while stack:
        m = stack.pop()
        if m not in needed: needed.add(m); stack.extend(imports[m])
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
        entry = {'target': label, 'exit_code': result.returncode, 'seconds': round(time.monotonic() - before, 3)}
        with log_lock:
            commands.append(entry)
            print(json.dumps(entry), flush=True)
            (output / 'commands.json').write_text(json.dumps(commands, indent=2) + '\n')
        if result.returncode:
            raise RuntimeError(f'Compilation failed for {label}; see {output / (label + ".log")}')
        return log.decode(encoding='utf-8', errors='replace')

    logs = {}; waiting = set(needed); completed = set(); active = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        while waiting or active:
            for mod in sorted(waiting):
                if len(active) >= args.jobs: break
                if not set(imports[mod]).issubset(completed): continue
                future = pool.submit(compile_file, mod, paths[mod], lib / (mod.replace('.', '/') + '.olean'))
                active[future] = mod; waiting.remove(mod)
            assert active, 'Unsatisfied module dependency'
            done, _ = concurrent.futures.wait(active, return_when=concurrent.futures.FIRST_COMPLETED)
            for future in done:
                mod = active.pop(future); logs[mod] = future.result(); completed.add(mod)
    for mod in mods:  # no warning of a proof hole in any contributed module
        assert not re.search(SORRY, logs[mod]), mod
    check_logs = {c: compile_file('check-' + Path(c).stem, PROJECT / c) for c in CHECKS}
    text = '\n'.join(check_logs.values())
    match = re.search(r'CONTRIB_AXIOM_AUDIT_PASS declarations=(\d+) modules=(\d+)', text)
    assert match, 'axiom audit did not pass'
    named = {m[1]: [a.strip() for a in m[2].split(',') if a.strip()]
             for m in re.finditer(r"'([\w.]+)' depends on axioms: \[([^\]]*)\]", text)}
    statements = sorted(set(re.findall(r'^.*STATEMENT_CHECK_PASS .*$', text, re.M)))
    statements = [s[s.index('STATEMENT_CHECK_PASS'):] for s in statements]
    facts = {'contributed_modules': sorted(mods),
             'snapshot_modules_compiled': sorted(m for m in needed if m in snapshot),
             'check_only_modules_compiled': sorted(EXTRA),
             'check_only_sorry_warnings': {m: len(re.findall(SORRY, logs[m])) for m in sorted(EXTRA)},
             'conclusion_spans': spans,
             'source_sha256': sources,
             'contributed_declarations_axiom_checked': int(match[1]),
             'contributed_modules_audited': int(match[2]),
             'named_theorem_axioms': named,
             'statement_checks': statements,
             'allowed_axioms': ['propext', 'Quot.sound', 'Classical.choice'],
             'frozen_target': FROZEN, 'frozen_target_sha256': check_lean.sha(PROJECT / FROZEN),
             'main_theorem_proved': False}
    expected = json.loads(EXPECTED.read_text(encoding='utf-8'))
    (output / 'FACTS.json').write_text(json.dumps(facts, indent=2) + '\n')
    for key in sorted(set(expected) | set(facts)):
        assert expected.get(key) == facts.get(key), f'{key}: expected {expected.get(key)!r}, found {facts.get(key)!r}'
    for name, axioms in named.items():
        assert set(axioms) <= set(facts['allowed_axioms']), name
    result = {'status': 'PASS', 'toolchain': version, 'dependency_pins': pins, **facts,
              'dependency_libraries': 'Prebuilt cache at verified source revisions; not rebuilt',
              'project_artifact_reuse': False, 'seconds': round(time.monotonic() - started, 3)}
    (output / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result), flush=True)


if __name__ == '__main__': main()
