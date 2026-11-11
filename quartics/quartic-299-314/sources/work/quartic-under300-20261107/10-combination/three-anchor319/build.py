"""Provisional composition of the independently accepted 326 and 359 components."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as F
from math import gcd,lcm
import copy,hashlib,json
H=Path(__file__).resolve().parent;WORK=H.parents[2]
sources={
 'base':('quartic-under300-20261107/01-elimination/s-odd366/candidate366-ir.json','0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56'),
 'detector':('quartic-optimization-20261107/resume-depth-20261107/three326/candidate326-ir.json','48cf6abbc2bd5393b14413314e1297c8bf235bd990202c7bb97ac203b7387c84'),
 'anchor':('quartic-optimization-20261107/resume-elimination-20261107/abscissa359/candidate359-ir.json','282fbc534713ddf056f1c8ed3d8b6dd933b95cad234fa9367896559e982c78d1')}
data={}
for key,(path,digest) in sources.items():
 raw=(WORK/path).read_bytes();assert hashlib.sha256(raw).hexdigest()==digest
 data[key]=json.loads(raw)
# Row identifiers are labels only; coordinates903/904 are unchanged.
for row in data['anchor']['residuals']:
 if row['id'] in (903,904):row['id']+=1000
out=copy.deepcopy(data['base']);deltas={}
for section in ['coordinates','residuals']:
 base={x['id']:x for x in data['base'][section]};parts=[]
 for name in ['detector','anchor']:
  p={x['id']:x for x in data[name][section]}
  touched={i for i in set(base)|set(p) if base.get(i)!=p.get(i)}
  parts.append((p,touched));deltas[name+'.'+section]=sorted(touched)
 assert not parts[0][1]&parts[1][1],(section,'overlapping changes')
 merged=copy.deepcopy(base)
 for p,touched in parts:
  for i in touched:
   if i in p:merged[i]=copy.deepcopy(p[i])
   else:merged.pop(i)
 out[section]=[merged[i] for i in sorted(merged)]
for name in ['detector','anchor']:
 for k,v in data['base'].items():
  if k not in ['coordinates','residuals','status']:assert data[name][k]==v
out['status']='Provisional319: three-group detector326 plus parity-anchor359. Inputs independently accepted; full composition acceptance required.'
total=defaultdict(int)
for row in out['residuals']:
 p={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in row['terms']}
 den=lcm(*(v.denominator for v in p.values()));g=gcd(*(int(v*den) for v in p.values()))
 q={m:int(v*den)//g for m,v in p.items()}
 for m,c in q.items():
  for n,d in q.items():total[tuple(sorted(m+n))]+=c*d
def write(name,obj):
 raw=(json.dumps(obj,indent=2)+'\n').encode();p=H/name
 if p.exists():assert p.read_bytes()==raw,'Refusing to overwrite frozen '+name
 else:p.write_bytes(raw)
 return hashlib.sha256(raw).hexdigest()
ih=write('candidate319-ir.json',out)
ph=write('polynomial319.json',{'terms':[{'sPower':m.count(-1),'monomial':[i for i in m if i>=0],'coefficient':str(c)} for m,c in sorted(total.items()) if c]})
cert={'sources':sources,'candidateSha256':ih,'polynomialSha256':ph,'changedObjectIds':deltas,'anchorResidualIdMap':{'903':1903,'904':1904},
 'variables':len(out['coordinates']),'residuals':len(out['residuals']),'monomials':sum(bool(c) for c in total.values()),'status':'provisional; no independent acceptance asserted'}
write('CERTIFICATE.json',cert);print(json.dumps({k:v for k,v in cert.items() if k not in ['sources','changedObjectIds']},indent=2))
