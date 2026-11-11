"""Build an isolated cumulative Version 14 supplement from reviewed Git bytes."""
import argparse
from datetime import date
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import zipfile

from install_packet import DOWNLOADS, MANIFEST
from release_common import (
    HERE, PACKAGE, REGISTER, REVISION, V13_ARCHIVE, V13_ARCHIVE_SHA,
    V14_ARCHIVE, V14_PDF, V14_TEX, blob, commit, json_bytes, output_dir,
    pinned, put, safe, sha,
)
from restore import checked_zip

AUDIT = 'scripts/check_audit_history.py'
INVENTORY = REVISION + '/validate-applications.py'
REPLAY = PACKAGE + '/verify_lineage.py'
PROTOCOL_DOCUMENTS = {'.github/pull_request_template.md', 'CONTRIBUTING.md', 'README.md',
    'docs/research-review/PROTOCOL.md', 'docs/research-review/README.md',
    'docs/research-review/protocol-v1.2.md'}
PROTOCOL_HASHES = {
    'docs/research-review/PROTOCOL.md': 'd3eb878bb3fb12d3b27d157e33f417f6f81bf2a873370f2758e8ccb1e5314d0a',
    'docs/research-review/protocol-v1.2.md': 'b5365b3d9cd9a782bf7fd0b6020403d5d400eac13dc7e60875484a8769d3d925'}
REQUIRED = PROTOCOL_DOCUMENTS | {V14_TEX, V14_PDF, REGISTER, 'README.md', 'CITATION.bib', 'AGENTS.md',
    'manuscripts/README.md', 'quartics/README.md', 'docs/release-policy.md',
    'docs/building.md', 'docs/archiving.md', 'docs/research-guide.md',
    'research/version14/README.md', REVISION + '/GUIDE.md',
    REVISION + '/APPLICATIONS.json', REVISION + '/inventory-install-manifest.json',
    REVISION + '/addition.tex', REVISION + '/edits.json', REVISION + '/new-edits.json',
    REVISION + '/v13-review-record.json', REVISION + '/build-report.json',
    REVISION + '/pdf-qa.json', AUDIT, INVENTORY, REPLAY, PACKAGE + '/' + MANIFEST,
    *DOWNLOADS.values()}


def admissible(name):
    path = safe(name)
    denied = {'.git', '.env', '.ssh', '.aws', '__pycache__', 'secrets', 'credentials',
              'conversations', 'transcripts', 'chat_history', 'node_modules'}
    if any(part.lower() in denied for part in path.parts):
        raise ValueError('Excluded private/runtime path: ' + name)
    if path.suffix.lower() in ('.pem', '.key', '.p12', '.pfx', '.zip'):
        raise ValueError('Excluded credential or nested archive path: ' + name)
    if path.suffix.lower() == '.pdf' and name != V14_PDF:
        raise ValueError('Only the current manuscript PDF is included in the new layer')


def coverage_paths(coverage, selection):
    if type(coverage) is not dict or set(coverage) != {'coverage', 'profiles', 'evidence'}:
        raise ValueError('Explicit coverage, profiles and evidence path lists are required')
    paths = set()
    for role, names in coverage.items():
        if type(names) is not list or not names or any(type(name) is not str for name in names) or len(set(names)) != len(names):
            raise ValueError('Nonempty unique actual path list required: ' + role)
        for name in names:
            safe(name)
            if name not in selection:
                raise ValueError('Coverage/profile/evidence file absent from reviewed selection: ' + name)
            paths.add(name)
    return paths


def collect(repo, oid, selection, coverage=None):
    if not REQUIRED <= set(selection):
        raise ValueError('Missing required release files: ' + repr(sorted(REQUIRED - set(selection))))
    coverage_paths(coverage, selection)
    current = {}
    for name, digest in sorted(selection.items()):
        admissible(name)
        raw = pinned(blob(repo, oid, name), digest, name)
        if b'-----BEGIN PRIVATE KEY-----' in raw or b'-----BEGIN RSA PRIVATE KEY-----' in raw:
            raise ValueError('Credential marker in selected bytes: ' + name)
        current[name] = raw
    for name, expected in PROTOCOL_HASHES.items():
        pinned(current[name], expected, 'governing/historical protocol')
    register = json.loads(current[REGISTER])
    if register['manuscript'] != {'path': V14_TEX, 'sha256': sha(current[V14_TEX])}:
        raise ValueError('Current register does not bind the selected Version 14 manuscript')
    if not register.get('contracts') or any(not row.get('approval') for row in register['contracts']):
        raise ValueError('Final current register must include actual approval pins')
    for name, item in json.loads(current[PACKAGE + '/' + MANIFEST]).items():
        path = PACKAGE + '/' + name
        if path not in current or sha(current[path]) != item['sha256'] or len(current[path]) != item['bytes']:
            raise ValueError('Missing or changed exact package member: ' + path)
    for name, public_name in DOWNLOADS.items():
        if current[PACKAGE + '/' + name] != current[public_name]:
            raise ValueError('Public download differs from reviewed package: ' + public_name)
    for name in json.loads(current[REVISION + '/inventory-install-manifest.json'])['files']:
        if name not in current:
            raise ValueError('Inventory install member absent from new layer: ' + name)
    return current


def write_archive(path, files, day):
    with zipfile.ZipFile(path, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for name, raw in sorted(files.items()):
            safe(name)
            info = zipfile.ZipInfo(name, (day.year, day.month, day.day, 0, 0, 0))
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, raw, compress_type=zipfile.ZIP_DEFLATED, compresslevel=6)


def replay(archive, root):
    extracted = root / 'extracted'
    restored = root / 'restored'
    with checked_zip(archive.read_bytes())[0] as checked:
        for name in checked.namelist():
            put(extracted, name, checked.read(name))
    commands = [([str(extracted / 'restore.py'), str(restored)], root),
        ([AUDIT, '--self-test'], restored), ([INVENTORY, '--repo', '.', '--self-test'], restored),
        (['verify_lineage.py'], restored / PACKAGE)]
    logs = []
    environment = {key: value for key, value in os.environ.items() if not key.startswith('PROTOCOL_') and key not in ('GITHUB_TOKEN', 'GH_TOKEN', 'PYTHONPATH', 'PYTHONHOME', 'PYTHONSTARTUP')}
    for command, cwd in commands:
        result = subprocess.run([sys.executable, '-E', '-B', *command], cwd=cwd,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False, env=environment)
        if result.returncode:
            raise RuntimeError('Fresh archive replay failed: ' + ' '.join(command) + '\n' + result.stdout.decode('utf-8', errors='replace'))
        logs.append(result.stdout)
    return logs


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', required=True, type=Path)
    p.add_argument('--commit', required=True)
    p.add_argument('--selection', required=True, type=Path)
    p.add_argument('--selection-sha256', required=True)
    p.add_argument('--coverage-selection', required=True, type=Path)
    p.add_argument('--coverage-selection-sha256', required=True)
    p.add_argument('--date', required=True, type=date.fromisoformat)
    p.add_argument('--output', required=True, type=Path)
    p.add_argument('--final-state', required=True, action='store_true')
    args = p.parse_args()
    oid = commit(args.repo, args.commit)
    selection = json.loads(pinned(args.selection.read_bytes(), args.selection_sha256, 'reviewed handoff selection'))
    coverage = json.loads(pinned(args.coverage_selection.read_bytes(), args.coverage_selection_sha256, 'reviewed coverage evidence selection'))
    current = collect(args.repo, oid, selection, coverage)
    historical = pinned(blob(args.repo, oid, V13_ARCHIVE), V13_ARCHIVE_SHA, V13_ARCHIVE)
    files = {'version13-base.zip': historical, 'restore.py': (HERE / 'restore.py').read_bytes(),
        'README.txt': b'Version 14 cumulative research supplement. Verify the published SHA-256, extract, and run python -B restore.py NEW_DIRECTORY. Earlier archive layers are preserved byte for byte.\n'}
    files.update({'current/' + name: raw for name, raw in current.items()})
    files['MANIFEST.json'] = json_bytes({'schema': 'quartic-version14-supplement/v1', 'source_commit': oid,
        'selection_sha256': args.selection_sha256, 'coverage_selection_sha256': args.coverage_selection_sha256,
        'coverage_paths': coverage, 'files': {name: sha(raw) for name, raw in sorted(files.items())}})
    output = output_dir(args.output)
    with tempfile.TemporaryDirectory(prefix='v14-handoff-', dir=HERE) as tmp:
        directory = Path(tmp)
        archive = directory / 'candidate.zip'
        write_archive(archive, files, args.date)
        logs = replay(archive, directory)
        raw = archive.read_bytes()
    put(output, V14_ARCHIVE, raw)
    for i, log in enumerate(logs, 1):
        put(output, f'restore-check-{i}.log', log)
    put(output, 'PACKAGE-RECEIPT.json', json_bytes({'schema': 'quartic-v14-supplement-build/v1',
        'source_commit': oid, 'selection_sha256': args.selection_sha256,
        'coverage_selection_sha256': args.coverage_selection_sha256, 'historical_base_sha256': V13_ARCHIVE_SHA,
        'archive': {'path': V14_ARCHIVE, 'sha256': sha(raw), 'bytes': len(raw)},
        'replay_log_sha256': [sha(log) for log in logs], 'python': sys.version,
        'status': 'built and fresh restore verified locally; publication pending'}))


if __name__ == '__main__':
    main()
