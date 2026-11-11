"""Author-side finite checks, independently implemented from build.py.

This file imports no producer. Independent mathematical acceptance is separate.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from math import gcd,lcm
import hashlib,json
BASE=Path(__file__).resolve().parent;ROOT=BASE.parents[2]
SRC=ROOT/'work/quartic-optimization-20261107/resume-anchor-shared314-20261107/anchor-gamma313/candidate313-ir.json'
PIN='6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a'
assert hashlib.sha256(SRC.read_bytes()).hexdigest()==PIN
old=json.loads(SRC.read_bytes());new=json.loads((BASE/'candidate307-ir.json').read_bytes())
table=json.loads((BASE/'polynomial307.json').read_bytes())
o={r['id']:r for r in old['residuals']};n={r['id']:r for r in new['residuals']}
oc={c['id']:c for c in old['coordinates']};nc={c['id']:c for c in new['coordinates']}
assert len(o)==len(old['residuals']) and len(n)==len(new['residuals'])
assert len(oc)==len(old['coordinates']) and len(nc)==len(new['coordinates'])
class P:
 def __init__(self,terms):self.t={k:Q(v) for k,v in terms.items() if v}
 @staticmethod
 def val(x):return x if isinstance(x,P) else P({(0,()):Q(x)})
 def __add__(self,x):
  x=P.val(x);d=dict(self.t)
  for k,v in x.t.items():d[k]=d.get(k,0)+v
  return P(d)
 __radd__=__add__
 def __neg__(self):return P({k:-v for k,v in self.t.items()})
 def __sub__(self,x):return self+-P.val(x)
 def __rsub__(self,x):return P.val(x)+-self
 def __mul__(self,x):
  x=P.val(x);d={}
  for (s,m),v in self.t.items():
   for (t,k),w in x.t.items():
    j=(s+t,tuple(sorted(m+k)));d[j]=d.get(j,0)+v*w
  return P(d)
 __rmul__=__mul__
 def __pow__(self,k):
  p=P.val(1)
  for _ in range(k):p=p*self
  return p
 def __eq__(self,x):return self.t==P.val(x).t
class K:
 def __init__(self,a,b=0):self.a=P.val(a);self.b=P.val(b)
 @staticmethod
 def val(x):return x if isinstance(x,K) else K(x)
 def __add__(self,x):x=K.val(x);return K(self.a+x.a,self.b+x.b)
 __radd__=__add__
 def __neg__(self):return K(-self.a,-self.b)
 def __sub__(self,x):return self+-K.val(x)
 def __rsub__(self,x):return K.val(x)+-self
 def __mul__(self,x):x=K.val(x);return K(self.a*x.a+2*self.b*x.b,self.a*x.b+self.b*x.a)
 __rmul__=__mul__
 def __pow__(self,k):
  p=K.val(1)
  for _ in range(k):p=p*self
  return p
def v(i):return P({(0,(i,)):1})
def p(i,k=1):return K(v(i),k*v(i+1))
def dec(row):
 t={(x['sPower'],tuple(x['monomial'])):Q(x['coefficient']) for x in row['terms']}
 assert len(t)==len(row['terms']);return P(t)
bound={}
def bind(rid,want):
 for k,poly in enumerate([want.a,want.b]):
  assert dec(n[rid+k])==poly,(rid+k,n[rid+k]['name'])
  bound[rid+k]=True
D=K(11,-6)
H=K(Q(-87,41)-v(142)+Q(7,2)*v(143)-Q(80,41)*v(700)+Q(212,41)*v(701),
 Q(129,164)+Q(7,4)*v(142)-v(143)+Q(106,41)*v(700)-Q(80,41)*v(701))
specs=[(1,82,21,110,112,114,255,190,232,164,2,700,116,142,207,184),
 (9,86,29,126,128,130,259,208,240,172,18,716,124,160,211,192),
 (13,88,33,134,136,138,261,220,244,176,26,724,128,172,213,196)]
deleted={3,4,11,12,15,16};repurposed=set();physical=[]
for j,(ai,ci,fi,Fi,si,ki,Yi,Bi,Li,zi,rr,cr,zr,Br,Yr,Lr) in enumerate(specs):
 a,f,h,F,s,k,Y,B,L,z=map(p,[ai,fi,fi+2,Fi,si,ki,Yi,Bi,Li,zi])
 Y=p(Yi,2);B=p(Bi,2);c=K((2 if ci==86 else 1)*v(ci),2*v(ci+1))
 bind(rr,h*h-f+D*f*Y);bind(cr,k*k-F+D*F*B)
 bind(cr+2,s*(f-F)-h-k)
 bind(cr+4,s*(h-k)-1+D*(Y+f*F+B))
 bind(cr+6,s*s-c+D*(f+F))
 bind(Yr,f*f-Y);bind(Br,F*F-B)
 bind(Lr,h*L+f*H);bind(zr,k*z-F)
 bind(2200+4*j,(1-D*Y)*L+h*H);bind(2202+4*j,(1-D*B)*z-k)
 # Retained square root uses exactly the physical c, including T's real factor2.
 rootrow={1:0,9:16,13:24}[ai]
 root=a*a-c
 for kcomp,q in enumerate([root.a,root.b]):
  got=dec(n[rootrow+kcomp]);assert set(got.t)==set(q.t)
  assert len({got.t[m]/q.t[m] for m in q.t})==1
 repurposed.update([fi,fi+1,fi+2,fi+3,Fi,Fi+1,si,si+1,ki,ki+1])
 physical.append({'root_a':ai,'primary_f':fi,'primary_h':fi+2,'alternate_F':Fi,'alternate_k':ki,'slope':si})
assert set(n)-set(o)==set(range(2200,2212))
assert not(set(o)-set(n))
changed={i for i in o if o[i]!=n[i]}
assert changed==set(bound)-set(range(2200,2212)) and len(changed)==54
assert set(oc)-set(nc)==deleted and not(set(nc)-set(oc))
for i in nc:
 if i in repurposed:
  assert {k:v for k,v in nc[i].items() if k!='name'}=={k:v for k,v in oc[i].items() if k!='name'}
 else:assert nc[i]==oc[i]
assert all(new[k]==old[k] for k in old if k not in ['coordinates','residuals','status'])
old_consumers={i for i,r in o.items() if any((repurposed|deleted).intersection(t['monomial']) for t in r['terms'])}
assert old_consumers<=changed
new_consumers={i for i,r in n.items() if any(repurposed.intersection(t['monomial']) for t in r['terms'])}
assert new_consumers<=set(bound)
assert all(not deleted.intersection(t['monomial']) for r in n.values() for t in r['terms'])

# Complete exact polynomial identity, using indeterminates, not samples.
d,f,F,h,k,s,c=[v(i) for i in range(10000,10007)]
r1=s*(f-F)-h-k;r2=s*(h-k)-1+d*(f*f+f*F+F*F)
r3=s*s-c+d*(f+F);r4=h*h-f+d*f*f*f
y=d*h-s*(d*f+c)
assert y*y-c*c*c+d*c==d*d*r4-d*(d*f+c)*(r2-s*r1)+r3*(c+d*f)*(c+d*F)
assert y+(d*k+s*(d*F+c))==-d*r1

# Literal root product and inverse chain proves all c !=0.
ca=p(82,2);cs=p(84,2);ct=K(2*v(86),2*v(87));cz=p(88,2)
height=[(289,ca*cs-p(337,2)),(291,p(337,2)*ct-2*p(339,2)),(293,p(339,2)*cz-p(341,2))]
for rid,eq in height:
 for j,expr in enumerate([eq.a,eq.b]):
  got=dec(n[rid+j]);assert set(got.t)==set(expr.t)
  assert len({got.t[m]/expr.t[m] for m in expr.t})==1
for rid,want in [(295,v(341)**2-v(343)),(345,v(37)*v(343)-v(391)),(346,v(391)**2-v(392)),
 (347,v(391)*v(392)-v(393))]:assert dec(n[rid])==want
assert dec(n[348])==301353*v(391)*v(392)+3081901*v(392)**2+7811144*v(392)*v(393)-301353*v(394)
assert dec(n[352])==-1-Q(64,976393)*v(391)*v(398)+Q(610120,976393)*v(392)*v(398)+Q(38573184,976393)*v(394)*v(398)

# Root half-sign freedoms survive as simple a -> -a actions in the new chart.
for ids in [{1,2},{9,10},{13,14}]:
 for r in n.values():
  q=dec(r);flipped=P({(e,m):a*(-1)**sum(i in ids for i in m) for (e,m),a in q.t.items()})
  assert flipped==q

# Independently expand every primitive residual square.
sos=P.val(0);active=set();primitive_content=[]
for r in n.values():
 q=dec(r);assert max(len(m) for e,m in q.t)<=2
 active.update(i for e,m in q.t for i in m)
 denominator=1
 for a in q.t.values():denominator=lcm(denominator,a.denominator)
 integers={m:int(a*denominator) for m,a in q.t.items()}
 content=0
 for a in integers.values():content=gcd(content,abs(a))
 q=P({m:Q(a,content) for m,a in integers.items()});sos=sos+q*q
assert active==set(nc) and len(nc)==307 and len(n)==295
assert sos==dec(table) and max(len(m) for e,m in sos.t)==4
assert len(sos.t)==len({m for e,m in sos.t})==6438
assert all(a.denominator==1 for a in sos.t.values())
assert any(e==0 and abs(a)==1 for (e,m),a in sos.t.items())
assert max(e for e,m in sos.t)==2
largest=max(abs(a) for (e,m),a in sos.t.items() if e==2)
assert largest==186624 and sos.t[(2,(89,89,89,89))]==186624
assert sum(m==(89,89,89,89) for e,m in sos.t)==1
assert max(abs(a) for (e,m),a in sos.t.items() if e==1)<=1728
assert max(abs(a.numerator).bit_length() for (e,m),a in sos.t.items() if e==0)<2048
assert hashlib.sha256(SRC.read_bytes()).hexdigest()==PIN
pins={str(SRC.relative_to(ROOT)):PIN}
for filename in ['candidate307-ir.json','polynomial307.json','build.py']:
 pins[filename]=hashlib.sha256((BASE/filename).read_bytes()).hexdigest()
result={'status':'PASS_AUTHOR_FINITE_CHECKS','independent_acceptance':False,'pins':pins,'variables':307,'witnesses':306,
 'residuals':295,'monomials':6438,'degree':4,'content':1,'max_coefficient':'186624*3^(2^26)',
 'changed_old_rows':sorted(changed),'added_rows':list(range(2200,2212)),'deleted_coordinates':sorted(deleted),
 'all_consumers_checked':True,'source_unchanged':True,'root_nonzero_chain_checked':True,
 'root_sign_actions_checked':True,'universal_root_curve_identity':True,'orientation_identity':True,
 'physical_coordinate_maps':physical,'source_polynomial_old_collisions_removed':3}
(BASE/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['changed_old_rows','physical_coordinate_maps']},indent=2))
