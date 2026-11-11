"""Replace the scalar weight chain in frozen326; no arithmetic change."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import reduce
from math import gcd,lcm
import copy,hashlib,json
H=Path(__file__).resolve().parent;source=H.parent/'three326/candidate326-ir.json'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='48cf6abbc2bd5393b14413314e1297c8bf235bd990202c7bb97ac203b7387c84'
old=json.loads(source.read_bytes());new=copy.deepcopy(old)
removed={361,409,457};gone=set();changed=[];bindings=[]
def terms(p):return [{'sPower':0,'monomial':list(m),'coefficient':str(c)} for m,c in sorted(p.items()) if c]
def find(name):return next(r for r in new['residuals'] if r['name']==name)
def replace(name,p):
 r=find(name);r['terms']=terms(p);changed.append(r['id'])
for n,E,e2,e4,e8,e11,e19,e39,e79 in ((0,350,361,832,356,355,359,369,360),(1,398,409,833,404,403,407,417,408),(2,446,457,834,452,451,455,465,456)):
 root=find(f'detector{n}.eWeight.definition')
 R={}
 for t in root['terms']:
  if E in t['monomial']:
   mon=list(t['monomial']);mon.remove(E);R[tuple(mon)]=F(t['coefficient'])
  else:assert t['monomial']==[] and F(t['coefficient'])==-1
 assert all(len(m)<=1 for m in R)
 def productR(i):return {tuple(sorted(m+(i,))):c for m,c in R.items()}
 def p(*pairs):return dict((tuple(sorted(m)),F(c)) for m,c in pairs)
 R2=defaultdict(F)
 for m,c in R.items():
  for k,d in R.items():R2[tuple(sorted(m+k))]+=c*d
 q={m:-c for m,c in R2.items()};q[tuple(sorted((e11,E)))]=F(1)
 replace(f'detector{n}.toric.c.definition',q)
 replace(f'four.det{n}.E4',p(((e4,e11),1),((E,),-1)))
 replace(f'detector{n}.toric.q10.definition',p(((e19,e11),1),((e8,e8),-1)))
 gone.add(find(f'detector{n}.E1.power2.definition')['id'])
 for c in new['coordinates']:
  if c['id']==e11:c['name']=f'detector{n}.chain.R3'
 bindings.append({'detector':n,'E':E,'E4':e4,'E8':e8,'R3':e11,'E19':e19,'E39':e39,'E79':e79,'R':terms(R)})
assert all(r['id'] in gone|set(changed) for r in old['residuals'] if any(removed.intersection(t['monomial']) for t in r['terms']))
new['coordinates']=[c for c in new['coordinates'] if c['id'] not in removed]
new['residuals']=[r for r in new['residuals'] if r['id'] not in gone]
new['status']='Research323: equivalent scalar chain on accepted326 detector; independent review pending.'
assert len(new['coordinates'])==323 and len(new['residuals'])==293
total=defaultdict(F)
for r in new['residuals']:
 p={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']}
 den=reduce(lcm,(c.denominator for c in p.values()),1);div=reduce(gcd,(abs(int(c*den)) for c in p.values()))
 p={m:c*den/div for m,c in p.items()}
 for m,c in p.items():
  for k,d in p.items():total[tuple(sorted(m+k))]+=c*d
poly={'terms':[{'sPower':m.count(-1),'monomial':[i for i in m if i>=0],'coefficient':str(c)} for m,c in sorted(total.items()) if c]}
def write(name,obj):
 p=H/name;p.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8');return hashlib.sha256(p.read_bytes()).hexdigest()
ch=write('candidate323-ir.json',new);ph=write('polynomial323.json',poly)
cert={'sourceSha256':hashlib.sha256(source.read_bytes()).hexdigest(),'candidateSha256':ch,'polynomialSha256':ph,'removedCoordinates':sorted(removed),'removedRows':sorted(gone),'changedRows':sorted(changed),'bindings':bindings,'variables':323,'witnesses':322,'rows':293,'monomials':len(poly['terms']),'arithmeticAcceptance':False}
write('CERTIFICATE.json',cert);print(json.dumps({k:v for k,v in cert.items() if k!='bindings'},indent=2))
