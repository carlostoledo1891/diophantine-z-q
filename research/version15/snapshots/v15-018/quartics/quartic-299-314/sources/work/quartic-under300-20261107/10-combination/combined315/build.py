"""Transport the shorter exact power chain after the private-anchor composition."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as F
from math import gcd,lcm
import copy,hashlib,json
H=Path(__file__).resolve().parent;WORK=H.parents[2]
pins={
 'base':('quartic-under300-20261107/10-combination/combined318/candidate318-ir.json','e8f213d1470a296ea09dabaf417b6d0003215de496069518ddc64b9737746cf1'),
 'old':('quartic-optimization-20261107/resume-depth-20261107/three326/candidate326-ir.json','48cf6abbc2bd5393b14413314e1297c8bf235bd990202c7bb97ac203b7387c84'),
 'component':('quartic-optimization-20261107/resume-depth-20261107/chain323/candidate323-ir.json','dc804a0f236f81c29753c5f3496254641df0fa527dd522923f4dfa331e8d2ecd')}
d={}
for key,(path,pin) in pins.items():
 raw=(WORK/path).read_bytes();assert hashlib.sha256(raw).hexdigest()==pin
 d[key]=json.loads(raw)
out=copy.deepcopy(d['base']);changes={}
for section in ['coordinates','residuals']:
 old,new=[{r['id']:r for r in d[k][section]} for k in ['old','component']]
 dst={r['id']:r for r in out[section]}
 changes[section]=[]
 for i in sorted(old.keys()|new.keys()):
  if old.get(i)==new.get(i):continue
  j=i
  expected=copy.deepcopy(old.get(i))
  if expected is not None:expected['id']=j
  assert dst.get(j)==expected,(section,i,j,'source mismatch')
  if i in new:
   dst[j]=copy.deepcopy(new[i]);dst[j]['id']=j
  else:del dst[j]
  changes[section].append({'componentId':i,'destinationId':j})
 out[section]=[dst[i] for i in sorted(dst)]
out['status']='Provisional315: three-group323 exact chain plus exact private-anchor unscaling. Independent final composition review required.'
total=defaultdict(int)
for row in out['residuals']:
 p={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in row['terms']}
 den=lcm(*(v.denominator for v in p.values()));g=gcd(*(int(v*den) for v in p.values()))
 q={m:int(v*den)//g for m,v in p.items()}
 for m,c in q.items():
  for n,e in q.items():total[tuple(sorted(m+n))]+=c*e
def write(name,obj):
 raw=(json.dumps(obj,indent=2)+'\n').encode();path=H/name
 if path.exists():assert path.read_bytes()==raw,'Frozen file differs: '+name
 else:path.write_bytes(raw)
 return hashlib.sha256(raw).hexdigest()
ih=write('candidate315-ir.json',out)
ph=write('polynomial315.json',{'terms':[{'sPower':m.count(-1),'monomial':[i for i in m if i>=0],'coefficient':str(c)} for m,c in sorted(total.items()) if c]})
cert={'sources':pins,'candidateSha256':ih,'polynomialSha256':ph,'transportedChanges':changes,'variables':len(out['coordinates']),'residuals':len(out['residuals']),'coefficientPowerEntries':sum(bool(c) for c in total.values()),'monomials':len({tuple(i for i in m if i>=0) for m,c in total.items() if c}),'status':'provisional'}
write('CERTIFICATE.json',cert);print(json.dumps(cert,indent=2))
