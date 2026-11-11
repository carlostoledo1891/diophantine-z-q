from package_paths import reference_repo
"""Independent exact check of the 510-coordinate combination; imports no producer."""
import json,hashlib,sys
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from math import gcd,lcm
H=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def p(ts):
 a={}
 for t in ts:
  m=tuple([-1]*t.get('sPower',0)+t['monomial']);a[m]=a.get(m,F(0))+F(t['coefficient'])
 return {m:c for m,c in a.items() if c}
def add(a,b,k=1):
 c=a.copy()
 for m,v in b.items():c[m]=c.get(m,0)+k*v
 return {m:v for m,v in c.items() if v}
def mul(a,b):
 c={}
 for m,v in a.items():
  for n,w in b.items():
   k=tuple(sorted(m+n));c[k]=c.get(k,0)+v*w
 return {m:v for m,v in c.items() if v}
def mon(*v):return {tuple(sorted(v)):F(1)}
def sub(a,mp):
 out={}
 for m,v in a.items():
  t={():v}
  for x in m:t=mul(t,mp.get(x,mon(x)))
  out=add(out,t)
 return out
def norm(a):
 den=reduce(lcm,(v.denominator for v in a.values()),1)
 g=reduce(gcd,(abs(int(v*den)) for v in a.values()),0)
 return {m:v*F(den,g) for m,v in a.items()}
product='--product' in sys.argv
tag='505' if product else '510'
cert=read(H/f'certificate{tag}.json');d=read(Path(cert['depthSource']));new=read(H/f'candidate{tag}-ir.json')
assert sha(Path(cert['depthSource']))==cert['depthSha256']
assert sha(H/f'candidate{tag}-ir.json')==cert['statistics']['candidateSha256']
assert sha(H/f'polynomial{tag}.json')==cert['statistics']['polynomialSha256']
cn={c['name']:c['id'] for c in d['coordinates']};old={r['name']:p(r['terms']) for r in d['residuals']};actual={r['name']:p(r['terms']) for r in new['residuals']}
expected=old.copy();maps={};factors={};removed=[];dropped=set()
for k in range(3):
 pre=f'detector{k}.';b=cn[pre+'B'];u=cn[pre+'U2.quadratic'];removed.append(u)
 for n in ['scaled_e','p','s']:maps[cn[pre+n]]=mon(b,cn[pre+n])
 for n in ['q','p2.quadratic','s2.quadratic','Bh.quadratic']:maps[cn[pre+n]]=mon(b,b,cn[pre+n])
 maps[cn[pre+'q2.quadratic']]=mon(b,b,b,b,cn[pre+'q2.quadratic']);maps[u]=mon(b,b)
 drop=pre+'U2.definition';dropped.add(drop)
 for n in ['p2.definition','s2.definition','firstConic','Bh.definition']:factors[pre+n]=mon(b,b)
 for n in ['q2.definition','secondConic']:factors[pre+n]=mon(b,b,b,b)
 w0=p(d['values'][pre+'W.0']['terms']);w1=p(d['values'][pre+'W.1']['terms']);n=mon(cn[pre+'normOver2w0'])
 assert old[pre+'w0Inverse.definition']==add(mon(),mul(w0,mon(cn[pre+'w0Inverse'])),-1)
 assert old[pre+'normOver2w0.definition']==add(add(mul(w0,w0),mul(w1,w1),-2),mul(w0,n),-2)
 assert sub(old[pre+'B.definition'],{b:{}})==mul(n,n)
for k in range(5):
 pre=f'V{k}.';a=cn[pre+'dxInverse.0'];b=cn[pre+'dxInverse.1'];r0=pre+'dxInverse.definition.0';r1=pre+'dxInverse.definition.1'
 assert {n for n,q in old.items() if any(a in m or b in m for m in q)}=={r0,r1}
 expected[r0]={m:v for m,v in old[r0].items() if b not in m};dropped.add(r1);removed.append(b)
 # Strip the actual row scalar and extract the two affine components.
 scalar=-old[r0][()];standard={m:v/scalar for m,v in old[r0].items()}
 A={tuple(x for x in m if x!=a):v for m,v in standard.items() if a in m}
 B={tuple(x for x in m if x!=b):v/2 for m,v in standard.items() if b in m}
 standard2=add(mul(B,mon(a)),mul(A,mon(b)))
 assert norm(standard2)==norm(old[r1]) or norm(standard2)=={m:-v for m,v in norm(old[r1]).items()}
 N=add(mul(A,A),mul(B,B),-2)
 assert add(mul(A,A),mul(B,B),-2)==N
 assert add(mul(B,A),mul(A,B),-1)=={}
anchor=cn['anchor.physicalA.quadratic'];f0=cn['Sscalar.f.0'];f1=cn['Sscalar.f.1']
assert {n for n,q in old.items() if any(anchor in m for m in q)}=={'anchor.physicalA.definition','anchor.translatedEquation'}
assert {n for n,q in old.items() if any(set(m)&{55,56,57} for m in q)}=={'anchor.translatedEquation'}
assert p(d['values']['Sscalar.f.1']['terms'])==mon(f1)
assert old['anchor.physicalA.definition']==add(add(add(mon(f0,f0),mon(f0,f1)),mon(f1,f1),-1),mon(anchor),-1)
dropped.add('anchor.physicalA.definition');removed.append(anchor)
expected['anchor.translatedEquation']=add(add(add(add(mon(55,55),mon(56,56),6),mon(57,57),-2),mon(f1,f1),-3),mon(-1,57),-4)
added=set()
if product:
 base=read(Path(cert['baseline']))
 assert sha(Path(cert['baseline']))==cert['baselineSha256']
 dropped.update(r['name'] for r in base['residuals'] if r['id'] in range(481,494))
 removed.extend(cn[c['name']] for c in base['coordinates'] if c['id'] in range(515,528))
 nc={c['name']:c['id'] for c in new['coordinates']}
 def v(n):return p(d['values'][n]['terms'])
 q,A,U,V,V2,B,B2,W=[mon(nc['reduced_scalar.'+s]) for s in ['norm_fH','constant_node','ratio_leaf0','ratio_leaf1','ratio_leaf1_squared','ratio_node','ratio_node_squared','root']]
 added={x for x in nc.values() if x not in cn.values()}
 r=v('scalar.r');z0=v('scalar.zRatio.0');z1=v('scalar.zRatio.1');f0p=v('U0.f.0');f1p=v('U0.f.1');i32=mon(cn['scalar.rInverse32.square.quadratic'])
 expected.update({
  'reduced_scalar.norm_fH':add(q,add(mul(f0p,f0p),mul(f1p,f1p),-2),-1),
  'reduced_scalar.constant_node':add(mul(r,add(A,mon(),-1)),mul(q,q),-1),
  'reduced_scalar.ratio_leaf0':add(U,mul(z0,i32),-1),
  'reduced_scalar.ratio_leaf1':add(V,mul(z1,i32),-1),
  'reduced_scalar.ratio_leaf1_squared':add(V2,mul(V,V),-1),
  'reduced_scalar.ratio_node':add(B,add(mul(U,U),mul(r,V2)),-1),
  'reduced_scalar.ratio_node_squared':add(B2,mul(B,B),-1),
  'reduced_scalar.root':add(W,add(mul(A,A),mul(r,B2)),-1)})
 attach=next(r['name'] for r in base['residuals'] if r['id']==495)
 expected[attach]=add(v('scalar.W2'),mul(W,W),-1)
 # The new coordinate IDs may reuse a just-deleted original ID.
 added={nc['reduced_scalar.'+s] for s in ['norm_fH','constant_node','ratio_leaf0','ratio_leaf1','ratio_leaf1_squared','ratio_node','ratio_node_squared','root']}
 x,D=mon(10000),mon(10001);xx=mul(x,x)
 assert add(add(mul(add(xx,D),add(xx,D)),mul(add({m:3*c for m,c in xx.items()},D,-1),add({m:3*c for m,c in xx.items()},D,-1)),-1),mul(xx,add(xx,D,-1)),8)=={}
assert set(actual)==set(expected)-dropped
for name,q in expected.items():
 if name in dropped:
  if name.endswith('U2.definition'):assert sub(q,maps)=={}
  continue
 assert sub(q,maps)==mul(factors.get(name,mon()),actual[name]),name
assert {c['id'] for c in new['coordinates']}==({c['id'] for c in d['coordinates']}-set(removed))|added
assert new['fixedParameter']['value']=='3^(2^25)'
total={}
for q in actual.values():
 assert max(sum(x!=-1 for x in m) for m in q)<=2
 items=list(norm(q).items())
 for i,(m,a) in enumerate(items):
  for j in range(i,len(items)):
   n,b=items[j];key=tuple(sorted(m+n));total[key]=total.get(key,0)+a*b*(1 if i==j else 2)
total={m:c for m,c in total.items() if c}
assert p(read(H/f'polynomial{tag}.json')['terms'])==total
assert len(new['coordinates'])==int(tag) and len(actual)==(474 if product else 479)
assert len(total)==(24748 if product else 24881) and max(sum(x!=-1 for x in m) for m in total)==4
assert {x for m in total for x in m if x!=-1}=={c['id'] for c in new['coordinates']}
assert any(c==1 and -1 not in m for m,c in total.items())
assert [(m,c) for m,c in total.items() if m.count(-1)==2]==[((-1,-1,57,57),16)]
assert (57,57) not in total and (-1,57,57) not in total
assert max(abs(c.numerator).bit_length() for m,c in total.items() if -1 not in m)==1520
assert max(abs(c) for m,c in total.items() if m.count(-1)==1)<=48
# Independent local starting direction on the literal curve, using tangent doubling.
def km(a,b):return (a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def ka(a,b):return (a[0]+b[0],a[1]+b[1])
def ks(a,n):return (a[0]*n,a[1]*n)
def ki(a):return ks((a[0],-a[1]),1/(a[0]**2-2*a[1]**2))
x=(F(57,8),F(-7,2));y=(F(-165,8),F(417,32));D=(F(11),F(-6))
assert km(y,y)==ka(km(km(x,x),x),ks(km(D,x),-1))
s=km(ka(ks(km(x,x),3),ks(D,-1)),ki(ks(y,2)))
x2=ka(km(s,s),ks(x,-2));y2=ka(km(s,ka(x,ks(x2,-1))),ks(y,-1));z2=ks(km(x2,ki(y2)),-1)
assert z2==(F(3396356159088,3287811625151),F(-4135204317756,3287811625151))
res=tuple(((a/3).numerator*pow((a/3).denominator,-1,3))%3 for a in z2)
assert res==(2,1) and tuple(c%3 for c in km(res,res))==(0,1)
result={'verified':True,'variables':int(tag),'witnesses':int(tag)-1,'residuals':len(actual),'degree':4,'monomials':len(total),'content':1,
        'maximumCoefficient':'16*3^(2^26)','baselineLocalDirection':list(res),
        'scope':'Full residual comparison, rational pole maps and guards, chart incidence, anchor binding, all SOS coefficients; arithmetic reasoning reviewed separately.'}
(H/f'VERIFICATION{tag}.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if product and (H/'candidate521-ir.json').exists():
 ordinary=read(H/'candidate521-ir.json');oc={c['name']:c['id'] for c in ordinary['coordinates']}
 ors={r['name']:p(r['terms']) for r in ordinary['residuals']}
 assert set(ors)==set(actual)|{f'constant.definition{j}' for j in range(16)}
 for name,q in actual.items():assert ors[name]==sub(q,{-1:mon(oc['constant.c15'])})
 for j in range(16):
  rhs={():F(3**1024)} if not j else mon(oc[f'constant.c{j-1}'],oc[f'constant.c{j-1}'])
  assert ors[f'constant.definition{j}']==add(mon(oc[f'constant.c{j}']),rhs,-1)
 ototal={}
 for q in ors.values():ototal=add(ototal,mul(norm(q),norm(q)))
 assert ototal==p(read(H/'polynomial521.json')['terms'])
 assert len(ototal)==24795 and max(map(len,ototal))==4
 assert max(abs(c) for c in ototal.values())==3**2048+1005072314881896
 assert set(c['id'] for c in ordinary['coordinates'])==set(x for m in ototal for x in m)
 print('Ordinary 521-coordinate lift and all 24795 coefficients independently checked.')
