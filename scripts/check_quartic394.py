"""Replay the frozen 394/411 construction and all published coefficients.

This verifies finite algebra and file integrity, not the inherited arithmetic.
"""
from pathlib import Path, PurePosixPath
import hashlib, json, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / 'quartics/quartic-394-411'

def check_manifest():
    manifest = json.loads((PACKET / 'PACKAGE-MANIFEST.json').read_bytes())
    for name, entry in manifest.items():
        rel = PurePosixPath(name)
        if rel.is_absolute() or '..' in rel.parts or ':' in name or '\\' in name:
            raise ValueError('Unsafe packet path')
        path = (PACKET / name).resolve()
        if not path.is_relative_to(PACKET.resolve()):
            raise ValueError('Packet path escapes its root')
        raw = path.read_bytes()
        if len(raw) != entry['bytes'] or hashlib.sha256(raw).hexdigest() != entry['sha256']:
            raise ValueError('Changed packet file: ' + name)
    return len(manifest)

def main():
    manifest_before = (PACKET / 'PACKAGE-MANIFEST.json').read_bytes()
    count = check_manifest()
    # Historical source scripts have locale-sensitive reads. A UTF-8 interpreter
    # makes their pinned source replay explicit on both Windows and Linux.
    subprocess.run([sys.executable, '-X', 'utf8', '-B', str(PACKET / 'verify_lineage.py')],
                   cwd=PACKET, check=True)
    if (PACKET / 'PACKAGE-MANIFEST.json').read_bytes() != manifest_before:
        raise ValueError('The replay changed its manifest')
    if check_manifest() != count:
        raise ValueError('The replay changed its file set')
    for source, target in {
        'quartic-394-symbolic-coefficients.json': 'quartic-394-symbolic-coefficients.json',
        'quartic-394-symbolic-coefficients.txt': 'quartic-394-symbolic-coefficients.txt',
        'quartic-411-ordinary-coefficients.txt': 'quartic-411-fully-expanded.txt',
    }.items():
        if (PACKET / source).read_bytes() != (ROOT / 'quartics' / target).read_bytes():
            raise ValueError('Download does not match reviewed packet: ' + target)
    output = ROOT / 'build/quartic-394'
    output.mkdir(parents=True, exist_ok=True)
    result = {'status': 'PASS', 'packet_files': count,
              'statistics': json.loads((PACKET / 'ARTIFACTS.json').read_bytes())['statistics'],
              'scope': 'Finite source replay, exact coefficients and download identity; not a proof of the inherited arithmetic.'}
    (output / 'verification.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result))

if __name__ == '__main__':
    main()
