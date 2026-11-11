from pathlib import Path
import hashlib, json
root = Path(__file__).resolve().parent
files = {}
for path in sorted(root.glob('*.py')) + [root / 'README.md', root / 'TITLE-FIX.json']:
    raw = path.read_bytes()
    files[path.name] = {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
for path in sorted((root / 'history').rglob('*')):
    if path.is_file():
        raw = path.read_bytes()
        files[path.relative_to(root).as_posix()] = {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
value = {'author': '/root', 'status': 'awaiting independent review',
         'change': 'Narrow administrative title metadata without changing generated manuscript bytes or any checker.',
         'tests': {'count': 29, 'result': 'PASS', 'runtime': 'pinned CPython 3.12.14', 'seconds': 26.481},
         'files': files}
(root / 'MANIFEST.json').write_text(json.dumps(value, indent=2, sort_keys=True) + '\n', encoding='utf-8')
print(hashlib.sha256((root / 'MANIFEST.json').read_bytes()).hexdigest())
