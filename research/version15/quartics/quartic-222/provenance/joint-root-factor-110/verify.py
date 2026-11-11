import build as b
import json
from fractions import Fraction as F
from collections import defaultdict
# Expand every new helper in old-labelled new coordinates.
helpers={b.H:b.add(b.mul(b.atom(b.Q1),b.atom(b.h0)),b.scale(b.mul(b.atom(b.Q0),b.atom(b.h1)),-1)),b.J:b.add(b.mul(b.atom(b.Q1),b.atom(b.j0)),b.scale(b.mul(b.atom(b.Q0),b.atom(b.j1)),-1)),b.K:b.add(b.mul(b.atom(b.Q1),b.atom(87)),b.scale(b.mul(b.atom(b.Q0),b.atom(b.q)),-1)),b.G:b.pn,b.Z:b.a1}
def expanded(p):
 out={}
 for (a,m),c in p.items():
  z={(a,()):c}
  for i in m:z=b.mul(z,helpers.get(i,b.atom(i)))
  out=b.add(out,z)
 return out
def onlypowers(p):
 out={}
 for (a,m),c in p.items():
  q=r=0;n=[]
  for i in m:
   if i==102:q+=1
   elif i==104:q+=2
   elif i==125:r+=2
   elif i==126:r+=1
   else:n.append(i)
  out=b.paddL(out,{(a,q,r,tuple(n)):c})
 return out
# Each generic transformed row equals its original after exact Laurent scaling.
pairids={}
for fi in [1,2,4]:
 for part in [0,1]:
  r0=b.byname['residue.det0.factor%d.%d.definition'%(fi,part)]
  r1=b.byname['residue.det1.factor%d.%d.definition'%(fi,part)]
  pairids[r0['id']]=(r0,r1,fi,part)
for r in b.rows:
 if r['id'] in b.removed: assert not b.laurent(b.terms(r['terms']));continue
 if r['id']==b.tr['id']:
  target={(a,x+2,y,m):c for (a,x,y,m),c in b.laurent(b.terms(r['terms'])).items()}
  assert onlypowers(expanded(b.mods[r['id']]))==target
 elif r['id'] in pairids:
  r0,r1,fi,part=pairids[r['id']];p0=b.terms(r0['terms']);p1=b.terms(r1['terms'])
  p0=b.scale(p0,1/p0[0,(135+2*fi+part,)]);p1=b.scale(p1,1/p1[0,(151+2*fi+part,)])
  target=b.laurent(b.add(b.mul(b.atom(b.Q1),p0),b.scale(b.mul(b.atom(b.Q0),p1),-1)))
  assert onlypowers(expanded(b.mods[r['id']]))==target
 elif r['id'] in b.mods:
  target,ex=b.clearL(b.laurent(b.terms(r['terms'])))
  actual=b.mods[r['id']]
  # Factor definitions were normalized by their nonzero output coefficient.
  if target!=actual:
   ratio=next(iter(actual.values()))/target[next(iter(actual))]
   assert b.scale(target,ratio)==actual
print('PASS: all parent rows, deleted identities, paired definitions and trace checked exactly')
# Parameter profile and attained height.
p=b.poly
quad=[(m,c) for (a,m),c in p.items() if a==2];lin=[abs(c) for (a,m),c in p.items() if a==1]
assert len(quad)==1 and quad[0][1]==1
m=quad[0][0]; offset=p.get((0,m),0)
const=max(abs(c) for (a,m),c in p.items() if a==0)
assert const<149**214+1 and max(lin)<149**107
print(json.dumps({'parameter_square_monomial':m,'offset':str(offset),'max_linear':str(max(lin)),'max_constant':str(const),'height':'A^2+'+str(offset),'N_at_least':53}))
