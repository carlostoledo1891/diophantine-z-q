"""Use the original integrity checker with a cross-platform path bootstrap.

The original wrapper and all frozen packet bytes remain unchanged. Only its
single expected child-process command is adapted; no verification is skipped.
"""
from pathlib import Path
from types import SimpleNamespace
import importlib.util
import hashlib
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / 'quartics/quartic-394-411'
ORIGINAL_SHA256 = 'faa43aab6431a9cb7ae14f92a47f649c494825ea5f3d56e798d73ad41e59ebd0'


def portable_run(command, **kwargs):
    expected = [sys.executable, '-X', 'utf8', '-B', str(PACKET / 'verify_lineage.py')]
    if command != expected:
        raise ValueError('Unexpected original verifier command')
    if set(kwargs) != {'cwd', 'check'} or kwargs['check'] is not True or kwargs['cwd'] != PACKET:
        raise ValueError('Unexpected original verifier process options')
    return subprocess.run([sys.executable, '-X', 'utf8', '-B',
                           str(ROOT / 'scripts/quartic394_path_bootstrap.py')], **kwargs)


def main():
    path = ROOT / 'scripts/check_quartic394.py'
    if hashlib.sha256(path.read_bytes()).hexdigest() != ORIGINAL_SHA256:
        raise ValueError('Original integrity checker differs from the reviewed version')
    spec = importlib.util.spec_from_file_location('original_quartic394_checker', path)
    original = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(original)
    old_process_module = original.subprocess
    original.subprocess = SimpleNamespace(run=portable_run)
    try:
        original.main()
    finally:
        original.subprocess = old_process_module


if __name__ == '__main__':
    main()
