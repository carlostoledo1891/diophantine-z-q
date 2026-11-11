"""Materialize an exact reviewed Version 14 packet as a local install layer."""
import argparse
import json
from pathlib import Path

from release_common import PACKAGE, json_bytes, output_dir, pinned, put, read, sha

MANIFEST = 'PACKAGE-MANIFEST.json'
DOWNLOADS = {
    'quartic-299-symbolic-coefficients.json': 'quartics/quartic-299-symbolic-coefficients.json',
    'quartic-299-symbolic-coefficients.txt': 'quartics/quartic-299-symbolic-coefficients.txt',
    'quartic-314-ordinary-coefficients.txt': 'quartics/quartic-314-fully-expanded.txt',
}


def collect(source, digest):
    manifest_raw = pinned(read(source, MANIFEST), digest, MANIFEST)
    rows = json.loads(manifest_raw)
    if MANIFEST in rows or not {'ARTIFACTS.json', 'SOURCE-MANIFEST.json', 'verify_lineage.py', *DOWNLOADS}.issubset(rows):
        raise ValueError('Incomplete reviewed Version 14 package manifest')
    contents = {}
    for name, record in sorted(rows.items()):
        raw = pinned(read(source, name), record['sha256'], name)
        if len(raw) != record['bytes']:
            raise ValueError('Wrong package byte count: ' + name)
        contents[name] = raw
    files = {PACKAGE + '/' + name: raw for name, raw in contents.items()}
    files.update({destination: contents[name] for name, destination in DOWNLOADS.items()})
    files[PACKAGE + '/' + MANIFEST] = manifest_raw
    return files


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--package', required=True, type=Path)
    p.add_argument('--package-sha256', required=True)
    p.add_argument('--output', required=True, type=Path)
    args = p.parse_args()
    files = collect(args.package.resolve(), args.package_sha256)
    output = output_dir(args.output)
    for name, raw in sorted(files.items()):
        put(output, name, raw)
    put(output, 'INSTALL.json', json_bytes({'package_manifest_sha256': args.package_sha256,
        'files': {name: {'sha256': sha(raw), 'bytes': len(raw)} for name, raw in sorted(files.items())}}))


if __name__ == '__main__':
    main()
