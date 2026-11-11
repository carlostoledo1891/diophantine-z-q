from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
m=json.loads((p/'MANIFEST.json').read_text(encoding='utf-8'))
for x in m['files']:
 b=(p/x['path']).read_bytes()
 assert len(b)==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256'],x['path']
print('PASS: portable file bytes; no mathematical acceptance inferred')
