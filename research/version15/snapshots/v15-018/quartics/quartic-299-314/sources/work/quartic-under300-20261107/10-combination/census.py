"""Reproducible structural census of accepted390, with exact physical consumers."""
from pathlib import Path
from collections import Counter,defaultdict
import hashlib,json
H=Path(__file__).resolve().parent; S=H.parent/'01-elimination/squared-h/candidate390-ir.json'
assert hashlib.sha256(S.read_bytes()).hexdigest()=='c986ee02f33aef0cf729bfbd73e590ac9672941be6c8f92dc3f389247daeaced'
p=json.loads(S.read_text(encoding='utf-8')); consumers=defaultdict(set)
for r in p['residuals']:
 for t in r['terms']:
  for i in t['monomial']:consumers[i].add(r['id'])
def family(c):
 n=c['name']
 if n.startswith(('A.','S.','T.','Z.')):return 'four odd root charts'
 if '.biquadratic.' in n:return 'four primary biquadratic charts'
 if n.startswith('hybrid.det'):return 'three detector field evaluations'
 if n.startswith('hybrid.'):return 'shared detector coefficients'
 if n.startswith(('detector0.','detector1.','detector2.')):return 'three detector weights, poles and trace interfaces'
 if n.startswith('log'):return 'rational logarithms and their squared inputs'
 if n.startswith(('L1.','L2.','L3.','L4.','LP1.','LP2.','LP3.','LP4.')):return 'eight ratio field values'
 if n.startswith('V') and '.z.' in n:return 'four comparison z outputs'
 if n.startswith(('H.','V0.')):return 'squared H chart'
 if n.startswith(('scalar.','normalized_scalar.','reduced_scalar.')):return 'scalar predicate'
 if n.startswith('heightProduct.'):return 'shared root height scales'
 if n.startswith(('testSquare.','Lucas.')):return 'shared tests and Lucas expression'
 if n.startswith('anchor.'):return 'anchor witnesses'
 return 'input and lambda'
coords=[dict(c,family=family(c),consumerRows=sorted(consumers[c['id']])) for c in p['coordinates']]
counts=Counter(c['family'] for c in coords)
out={'source':str(S.relative_to(H.parent)),'sourceSha256':hashlib.sha256(S.read_bytes()).hexdigest(),'totalVariables':len(coords),'residuals':len(p['residuals']),'familyCounts':dict(sorted(counts.items())),'coordinates':coords,'warning':'Families are assigned by coordinate names; consumerRows are computed from actual monomials. Historical names do not define semantics.'}
(H/'CENSUS390.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out['familyCounts'],indent=2))
