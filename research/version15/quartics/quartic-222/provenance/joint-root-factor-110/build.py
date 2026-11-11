from fractions import Fraction as F
from collections import defaultdict
from functools import reduce
from math import gcd
import json, pathlib
ROOT=pathlib.Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic238-optimization-20261110/')
C=ROOT/'global/resume-20261110/shared-alternate-226-001'
P=ROOT/'resume-20261110/scalar-contact-quartic-001/candidate232-ir.json'
old=json.loads(P.read_text()); new=json.loads((C/'candidate226-ir.json').read_text()); pub=json.loads((C/'candidate226-polynomial.json').read_text())
def clean(p): return {k:v for k,v in p.items() if v}
def add(*ps):
 d=defaultdict(F)
 for p in ps:
  for k,v in p.items(): d[k]+=v
 return clean(d)
def scale(p,c): return clean({k:v*c for k,v in p.items()})
def mul(p,q):
 d=defaultdict(F)
 for (a,m),v in p.items():
  for (b,n),w in q.items(): d[a+b,tuple(sorted(m+n))]+=v*w
 return clean(d)
def atom(i):return {(0,(i,)):F(1)}
def const(c):return {(0,()):F(c)} if c else {}
def terms(ts):
 d=defaultdict(F)
 for t in ts:d[t['parameterPower'],tuple(t['monomial'])]+=F(t['coefficient'])
 return clean(d)
def fa(x,y):return (add(x[0],y[0]),add(x[1],y[1]))
def fm(x,y):return (add(mul(x[0],y[0]),scale(mul(x[1],y[1]),2)),add(mul(x[0],y[1]),mul(x[1],y[0])))
def fc(a,b=0):return (const(a),const(b))
def fp(a,b):return (atom(a),atom(b))
def neg(x):return tuple(scale(z,-1) for z in x)
def remap(p):return {(a,tuple(sorted(i if i<21 else i-8 for i in m))):v for (a,m),v in p.items()}

from math import lcm
OUT=ROOT/'resume-20261110/joint-root-factor-110'
P=ROOT/'global/resume-20261110/shared-T-redundancy224-006/candidate224-ir.json'
par=json.loads(P.read_text()); rows=par['residuals']; q,Q0,Q1,h0,h1,j0,j1=102,89,104,88,103,90,105
H,J,K,G,Z=225,226,227,228,229
fmap={62:(179,180,0),63:(179,180,1),66:(207,208,0),67:(207,208,1),68:(221,222,0),69:(221,222,1)}
deleted=set(fmap)
scaled=set(range(167,179))|set(range(195,207))|set(range(209,221))|{179,180,207,208,221,222}
first=set(range(167,179))|set(range(195,203))|set(range(209,217))
ratio=set(range(47,55))|set(range(56,60))
def paddL(*ps):
 d=defaultdict(F)
 for p in ps:
  for key,v in p.items():d[key]+=v
 return {k:v for k,v in d.items() if v}
def pmulL(p,t):
 d=defaultdict(F)
 for (a,b,c,m),v in p.items():
  for (x,y,z,n),w in t.items():d[a+x,b+y,c+z,tuple(sorted(m+n))]+=v*w
 return {k:v for k,v in d.items() if v}
def liftvar(i):
 if i in fmap:
  u,v,im=fmap[i]
  return {(0,-2,0,(u,v)):F(1)} if im else {(0,-2,0,(u,u)):F(1),(0,-2,0,(v,v)):F(2)}
 if i==q:return {(0,1,0,()):F(1)}
 if i==Q1:return {(0,2,0,()):F(1)}
 if i==125:return {(0,0,2,()):F(1)}
 if i==126:return {(0,0,1,()):F(1)}
 return {(0,-1 if i in scaled else 0,1 if i in first or i in ratio else 0,(i,)):F(1)}
def laurent(p):
 out={}
 for (a,m),c in p.items():
  z={(a,0,0,()):c}
  for i in m:z=pmulL(z,liftvar(i))
  out=paddL(out,z)
 return out
def clearL(p):
 if not p:return {},(0,0)
 b=min(k[1] for k in p);c=min(k[2] for k in p);out={}
 for (a,x,y,m),v in p.items():
  x-=b;y-=c;assert 0<=x<=2 and 0<=y<=2,(x,y)
  n=m+(() if x==0 else (q,) if x==1 else (Q1,))+(() if y==0 else (126,) if y==1 else (125,))
  out=add(out,{(a,tuple(sorted(n))):v})
 return out,(b,c)
def primitive(p):
 de=lcm(*(x.denominator for x in p.values()));gg=reduce(gcd,(abs(int(x*de)) for x in p.values()));return scale(p,F(de,gg)),str(F(de,gg))
def serialize(p):return [{'parameterPower':a,'monomial':list(m),'coefficient':str(c)} for (a,m),c in sorted(p.items())]
byname={r['name']:r for r in rows};mods={};cert=[];removed=[]
for r in rows:
 if any(r['name'].startswith('rootProduct.'+str(i)+'.') for i in [1,3,4]) or r['name'].startswith('shared.alternate.direct.'):
  # Direct rows are selected by actual scaled-variable occurrence, not names.
  pass
for r in rows:
 p=terms(r['terms']); touched=any(set(m)&(scaled|ratio) for a,m in p)
 if touched and 'aggregate' not in r['name']:
  # all changed consumers are transported literally
  z,ex=clearL(laurent(p))
  if not z:removed.append(r['id'])
  else:mods[r['id']]=z
  cert.append({'row':r['id'],'name':r['name'],'laurent_common_factor':list(ex),'zero':not z})
# Three paired factor rows containing the removed primary outputs.
for fi in [1,2,4]:
 for part in [0,1]:
  r0=byname['residue.det0.factor'+str(fi)+'.'+str(part)+'.definition'];r1=byname['residue.det1.factor'+str(fi)+'.'+str(part)+'.definition']
  p0,p1=terms(r0['terms']),terms(r1['terms'])
  out0=135+2*fi+part;out1=151+2*fi+part
  p0=scale(p0,1/p0[0,(out0,)]);p1=scale(p1,1/p1[0,(out1,)])
  trans={q:87,Q1:Q0,h1:h0,j1:j0,out1:out0}
  pp={(a,tuple(sorted(trans.get(i,i) for i in m))):c for (a,m),c in p1.items()}
  assert pp==p0,(fi,part)
  pair=add(mul(atom(Q1),atom(out0)),scale(mul(atom(Q0),atom(out1)),-1))
  for (a,m),c in p0.items():
   if m==(out0,):continue
   if not m:pair=add(pair,scale(add(atom(Q1),scale(atom(Q0),-1)),c));continue
   powers=[i for i in m if i in [87,Q0,h0,j0]];assert len(powers)==1,(fi,m)
   power=powers[0];rest=list(m);rest.remove(power)
   if power==Q0:continue
   repl={87:K,h0:H,j0:J}[power]
   pair=add(pair,{(a,tuple(sorted(rest+[repl]))):c})
  mods[r0['id']]=pair
  # Only FU substitutions; other producer coordinates remain untouched.
  z=laurent(p1);new1,ex=clearL(z);assert ex==(0,0),(fi,part,ex)
  mods[r1['id']]=new1
  cert.append({'paired_factor':fi,'part':part,'rows':[r0['id'],r1['id']]})
# Trace: unscaled block2, scaled first with R/q, scaled blocks3/4 with1/q.
tr=next(r for r in rows if 'aggregate.rootTrace' in r['name']);tp=terms(tr['terms']);pn={};a1={};a34={}
for key,c in tp.items():
 a,m=key
 if set(m)&first:a1[key]=-c
 elif set(m)&(set(range(195,207))|set(range(209,221))):a34[key]=c
 else:pn[key]=c
assert len(a1)==18 and len(a34)==0
mods[tr['id']]=add(mul(atom(Q1),atom(G)),scale(mul(atom(125),atom(Z)),-1),a34)
helpers=[('paired.high',add(atom(H),scale(mul(atom(Q1),atom(h0)),-1),mul(atom(Q0),atom(h1)))),('paired.fourth',add(atom(J),scale(mul(atom(Q1),atom(j0)),-1),mul(atom(Q0),atom(j1)))),('paired.special',add(atom(K),scale(mul(atom(Q1),atom(87)),-1),mul(atom(Q0),atom(q)))),('trace.remainder',add(atom(G),scale(pn,-1))),('trace.first',add(atom(Z),scale(a1,-1)))]
assert len(removed)==6,removed
# Any occurrence of deleted outputs must be in a replaced or removed row.
assert all(r['id'] in mods or r['id'] in removed for r in rows if any(deleted&set(t['monomial']) for t in r['terms']))
# Required trace-independent q and R equations are literally untouched.
required=[9,43,44,45,46,56,57,68,71,73]
assert not set(required)&(set(mods)|set(removed))
coords=[c for c in par['coordinates'] if c['id'] not in deleted]+[{'id':i,'name':n,'kind':'gate'} for i,n in [(H,'paired.high'),(J,'paired.fourth'),(K,'paired.special'),(G,'trace.remainder'),(Z,'trace.first')]]
cm={c['id']:i+1 for i,c in enumerate(coords)};newrows=[];norm=[]
for r in rows:
 if r['id'] in removed:continue
 p=mods.get(r['id'],terms(r['terms']));p,fac=primitive(p)
 assert all(len(m)<=2 for a,m in p),(r['id'],r['name'])
 p={(a,tuple(sorted(cm[i] for i in m))):c for (a,m),c in p.items()};norm.append({'parent':r['id'],'scale':fac});newrows.append({'id':len(newrows)+1,'parentRowId':r['id'],'name':r['name'],'terms':serialize(p)})
for n,p in helpers:
 p,fac=primitive(p);p={(a,tuple(sorted(cm[i] for i in m))):c for (a,m),c in p.items()};norm.append({'helper':n,'scale':fac});newrows.append({'id':len(newrows)+1,'name':n,'terms':serialize(p)})
poly=add(*(mul(terms(r['terms']),terms(r['terms'])) for r in newrows));assert len(coords)==223 and len(newrows)==197
assert set(i for a,m in poly for i in m)==set(range(1,224))
new=dict(par,variables=223,coordinates=[dict(c,id=cm[c['id']]) for c in coords],residuals=newrows,source={'parent':str(P),'construction':'joint roots1,3,4 / paired factor / trace'})
stats={'variables':223,'residuals':len(newrows),'coordinate_monomials':len({m for a,m in poly}),'parameter_terms':len(poly),'degree':max(len(m) for a,m in poly),'content':reduce(gcd,(abs(c.numerator) for c in poly.values()))}
for fn,obj in [('candidate223-ir.json',new),('candidate223-polynomial.json',dict(variables=223,degree=4,inputCoordinate=1,fixedParameter=par['fixedParameter'],terms=serialize(poly))),('MAPS.json',dict(old_to_new=cm,deleted=sorted(deleted),removed_rows=removed,scaled=sorted(scaled),first_R_scaled=sorted(first),ratio_R_scaled=sorted(ratio),FU_recovery=fmap,certificates=cert,normalizations=norm,required_unchanged=required)),('STATISTICS.json',stats)]:
 (OUT/fn).write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(stats))
