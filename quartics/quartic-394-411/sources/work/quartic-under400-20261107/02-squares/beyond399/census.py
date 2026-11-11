from pathlib import Path
import hashlib,json
H=Path(__file__).resolve().parent;S=H.parents[1]/'10-combination/combined399-ir.json'
assert hashlib.sha256(S.read_bytes()).hexdigest()=='eae983889586748f5a51aa7562d23769ae46f7fba08fc8efcedbb53bc54a5a3b'
d=json.loads(S.read_text());cs={c['id']:c for c in d['coordinates']};print('counts',len(cs),len(d['residuals']))
for i,c in cs.items():
 if any(t in c['name'].lower() for t in ['inverse','reciprocal','biquadratic','chart','odd']):
  uses=[r['name'] for r in d['residuals'] if any(i in t['monomial'] for t in r['terms'])]
  print(i,c['name'],len(uses),uses)
