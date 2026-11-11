"""Run the frozen verifier with manifest-constrained historical path mapping."""
from pathlib import Path
import builtins
import io
import json
import os
import runpy
import sys

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / 'quartics/quartic-394-411'


def make_mapper(packet, original_root, manifest):
    source_root = packet / 'sources'
    if source_root.is_symlink():
        raise ValueError('Historical source root is a symbolic link')
    sources = source_root.resolve()
    prefix = original_root.replace('\\', '/').rstrip('/')

    def remap(file):
        if not isinstance(file, (str, bytes, os.PathLike)):
            return file
        # A restored packet can itself sit below the historical workspace on
        # Windows. Its real current paths must not be interpreted as old ones.
        # On POSIX, C:\\... is relative, so do not resolve it against the cwd.
        native = Path(os.fsdecode(file))
        if native.is_absolute() and native.resolve().is_relative_to(packet.resolve()):
            return file
        text = os.fsdecode(file).replace('\\', '/')
        if text != prefix and not text.startswith(prefix + '/'):
            return file
        relative = text[len(prefix) + 1:]
        parts = relative.split('/')
        if (not relative or any(p in ('', '.', '..') for p in parts)
                or ':' in relative or '\x00' in relative or relative not in manifest):
            raise ValueError('Unlisted or unsafe historical path: ' + relative)
        target = sources
        for part in parts:
            target = target / part
            if target.is_symlink():
                raise ValueError('Historical path crosses a symbolic link')
        resolved = target.resolve()
        if not resolved.is_relative_to(sources) or not resolved.is_file():
            raise ValueError('Missing or escaping historical input: ' + relative)
        return resolved

    return remap


def main():
    plan = json.loads((PACKET / 'VERIFICATION-PLAN.json').read_bytes())
    manifest = json.loads((PACKET / 'SOURCE-MANIFEST.json').read_bytes())
    remap = make_mapper(PACKET, plan['originalRoot'], manifest)
    old_open, old_io_open, old_argv = builtins.open, io.open, sys.argv

    def mapped_open(file, *args, **kwargs):
        return old_open(remap(file), *args, **kwargs)

    def mapped_io_open(file, *args, **kwargs):
        return old_io_open(remap(file), *args, **kwargs)

    builtins.open, io.open = mapped_open, mapped_io_open
    verifier = PACKET / 'verify_lineage.py'
    sys.argv = [str(verifier)]
    try:
        runpy.run_path(str(verifier), run_name='__main__')
    finally:
        builtins.open, io.open, sys.argv = old_open, old_io_open, old_argv


if __name__ == '__main__':
    main()
