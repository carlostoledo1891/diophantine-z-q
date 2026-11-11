"""Verify the portable bundle's relative file bindings with standard Python."""
from pathlib import Path
from hashlib import sha256
import json
import sys

root=Path(__file__).resolve().parent
name='MANIFEST.json' if (root/'MANIFEST.json').exists() else 'PROOF-ONLY-MANIFEST.json'
manifest=json.loads((root/name).read_text(encoding='utf-8'))
failures=[]
for row in manifest['files']:
    path=(root/row['path']).resolve()
    if not path.is_relative_to(root.resolve()):
        failures.append((row['path'],'path outside bundle'));continue
    if not path.is_file():
        failures.append((row['path'],'missing'));continue
    data=path.read_bytes()
    if len(data)!=row['bytes'] or sha256(data).hexdigest()!=row['sha256']:
        failures.append((row['path'],'different bytes'))
print(json.dumps({'manifest':name,'files_checked':len(manifest['files']),'failures':failures},indent=2))
sys.exit(bool(failures))
