from pathlib import Path
import hashlib,json
B=Path(__file__).resolve().parents[3];D=Path(__file__).resolve().parent
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
for r in json.loads((D/'PINS.json').read_text())['files']:
 checks.append((r['path'],h(B/r['path'])==r['sha256']))
for r in json.loads((D/'MANIFEST.json').read_text())['files']:
 checks.append((r['path'],h(B/r['path'])==r['sha256']))
f=json.loads((D/'FINAL-CHECKS.json').read_text())
checks.append(('final checked result',f['checks']==439 and f['passed']==439 and not f['failed']))
print(json.dumps({'checks':len(checks),'passed':sum(v for k,v in checks),'failed':[k for k,v in checks if not v]}))
assert all(v for k,v in checks)
