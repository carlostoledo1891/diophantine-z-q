"""Shared exact-byte checks for the isolated Version 14 preparation tools."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
V13_TEX = 'manuscripts/quartic_v13.tex'
V13_TEX_SHA = '9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd'
V14_TEX = 'manuscripts/quartic_v14.tex'
V14_PDF = 'manuscripts/quartic_v14.pdf'
REGISTER = 'docs/audit-history/current.json'
REVISION = 'docs/manuscript-revisions/version14'
PACKAGE = 'quartics/quartic-299-314'
V13_ARCHIVE = 'research/version13/z-in-q-version13-supplement.zip'
V13_ARCHIVE_SHA = '10787487f46ebfefe931e2e7db163a2e8bd0605b3c0325534a47cd93dd43b01b'
V14_ARCHIVE = 'research/version14/z-in-q-version14-supplement.zip'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def json_bytes(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode('utf-8')


def safe(name):
    if not isinstance(name, str) or not name or any(ord(c) < 32 for c in name) or ':' in name or '\\' in name:
        raise ValueError('Unsafe relative path: ' + repr(name))
    reserved = {'con', 'prn', 'aux', 'nul', *(f'com{i}' for i in range(1, 10)), *(f'lpt{i}' for i in range(1, 10))}
    for part in name.split('/'):
        if not part or part in ('.', '..') or part.endswith((' ', '.')) or part.split('.')[0].lower() in reserved:
            raise ValueError('Unsafe relative path: ' + repr(name))
    return PurePosixPath(name)


def read(root, name):
    path = root / safe(name)
    if path.resolve() != path or not path.is_file():
        raise ValueError('Missing or nonregular source: ' + name)
    return path.read_bytes()


def pinned(raw, expected, label):
    if sha(raw) != expected:
        raise ValueError('Digest mismatch: ' + label)
    return raw


def put(root, name, raw):
    path = root / safe(name)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as target:
        target.write(raw)


def git(repo, *args):
    return subprocess.check_output(['git', '--no-replace-objects', '-C', str(repo), *args])


def commit(repo, oid):
    if not re.fullmatch('[0-9a-f]{40}', oid) or git(repo, 'cat-file', '-t', oid).strip() != b'commit':
        raise ValueError('Expected exact Git commit ID')
    return oid


def blob(repo, oid, name):
    safe(name)
    return git(repo, 'show', oid + ':' + name)


def output_dir(path):
    target = path.resolve()
    if not target.is_relative_to(HERE) or target == HERE or target.exists():
        raise ValueError('Output must be a new directory beneath ' + str(HERE))
    return target
