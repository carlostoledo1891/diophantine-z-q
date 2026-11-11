"""Replace the scalar weight chain in frozen330; no arithmetic change."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import reduce
from math import gcd,lcm
import copy,hashlib,json
H=Path(__file__).resolve().parent;source=H.parent/'strong-h330/candidate330-ir.json'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='41602bf9d25d52ae6e461f958eb21e1d752190ef71a72c1cc7c444f4e0a9fff6'
old=json.loads(source.read_bytes());new=copy.deepcopy(old)
removed={362,410,458};gone=set();changed=[];bindings=[]
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
 replace(f'detector{n}.toric.c.definition',p(((e11,E),1),((e8,e4),-1)))
 replace(f'detector{n}.toric.d.definition',p(((e8,),1),((e4,e4),-1)))
 replace(f'detector{n}.toric.q10.definition',p(((e19,),1),((e11,e8),-1)))
 q=productR(e39);q[(e19,e19)]=F(-1);replace(f'detector{n}.E10.power2.definition',q)
 q=productR(e79);q[(e39,e39)]=F(-1);replace(f'detector{n}.toric.q40.definition',q)
 gone.add(find(f'detector{n}.E1.power3.definition')['id'])
 for c in new['coordinates']:
  if c['id']==e11:c['name']=f'detector{n}.chain.E11'
  if c['id']==e39:c['name']=f'detector{n}.chain.E39'
 bindings.append({'detector':n,'E':E,'E2':e2,'E4':e4,'E8':e8,'E11':e11,'E19':e19,'E39':e39,'E79':e79,'R':terms(R)})
assert all(r['id'] in gone|set(changed) for r in old['residuals'] if any(removed.intersection(t['monomial']) for t in r['terms']))
new['coordinates']=[c for c in new['coordinates'] if c['id'] not in removed]
new['residuals']=[r for r in new['residuals'] if r['id'] not in gone]
new['status']='Research327: equivalent scalar chain on pending330 detector; independent review pending.'
assert len(new['coordinates'])==327 and len(new['residuals'])==297
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
ch=write('candidate327-ir.json',new);ph=write('polynomial327.json',poly)
cert={'sourceSha256':hashlib.sha256(source.read_bytes()).hexdigest(),'candidateSha256':ch,'polynomialSha256':ph,'removedCoordinates':sorted(removed),'removedRows':sorted(gone),'changedRows':sorted(changed),'bindings':bindings,'variables':327,'witnesses':326,'rows':297,'monomials':len(poly['terms']),'arithmeticAcceptance':False}
write('CERTIFICATE.json',cert);print(json.dumps({k:v for k,v in cert.items() if k!='bindings'},indent=2))
