"""Producer-free exact check of the301 delta and reconstruction identities."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from math import gcd,lcm
import hashlib,json
HERE=Path(__file__).resolve().parent;OPT=HERE.parent.parent
SRC=OPT/'reciprocal307-20261107/candidate307-ir.json'
PIN='0b94aaf7669b3fe89cdf48f4718750991cfea4dd289695543f29b0cd533f29a1'
assert hashlib.sha256(SRC.read_bytes()).hexdigest()==PIN
old=json.loads(SRC.read_bytes());new=json.loads((HERE/'candidate301-ir.json').read_bytes())
class P:
 def __init__(self,t):self.t={k:Q(v) for k,v in t.items() if v}
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
  x=P.val(x);d=defaultdict(Q)
  for (a,m),v in self.t.items():
   for (b,n),w in x.t.items():d[a+b,tuple(sorted(m+n))]+=v*w
  return P(d)
 __rmul__=__mul__
 def __pow__(self,n):
  r=P.val(1)
  for _ in range(n):r=r*self
  return r
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
 def __pow__(self,n):
  r=K.val(1)
  for _ in range(n):r=r*self
  return r
def v(i):return P({(0,(i,)):1})
def pair(i,im=1,re=1):return K(re*v(i),im*v(i+1))
def dec(row):
 d={(t['sPower'],tuple(t['monomial'])):Q(t['coefficient']) for t in row['terms']}
 assert len(d)==len(row['terms']) and all(d.values());return P(d)
o={r['id']:r for r in old['residuals']};n={r['id']:r for r in new['residuals']}
assert len(o)==len(old['residuals']) and len(n)==len(new['residuals'])
D=K(11,-6);changed=set();removed=set();deleted=set()
for ci,cr,fi,Fi,si,ki,Yi,Bi,zi,chart,zraw,zreg in [(82,1,21,110,112,114,255,190,164,700,116,2202),(86,2,29,126,128,130,259,208,172,716,124,2206),(88,1,33,134,136,138,261,220,176,724,128,2210)]:
 f,h,F,s,Y,B,z=map(pair,(fi,fi+2,Fi,si,Yi,Bi,zi));Y=pair(Yi,2);B=pair(Bi,2);c=pair(ci,2,cr)
 q=2*s*h-c*(f-F)-1+D*(2*Y+f*F)
 reg=(1-D*B)*z-s*(f-F)+h
 for rid,eq in ((chart+4,q),(zreg,reg)):
  assert dec(n[rid])==eq.a and dec(n[rid+1])==eq.b,rid
  changed.update((rid,rid+1))
 removed.update((chart,chart+1,chart+2,chart+3,zraw,zraw+1));deleted.update((ki,ki+1))
assert set(o)-set(n)==removed and not set(n)-set(o)
assert {i for i in n if n[i]!=o[i]}==changed
assert all({i for t in r['terms'] for i in t['monomial']} & deleted == set() for r in n.values())
assert all(rid in removed|changed for rid,r in o.items() if any(deleted.intersection(t['monomial']) for t in r['terms']))
assert new['coordinates']==[c for c in old['coordinates'] if c['id'] not in deleted]
for key in old:
 if key not in ['coordinates','residuals','status']:assert old[key]==new[key]
# Universal identities with an independent indeterminate D.
d,f,F,h,s,c,Y,B,z=map(v,range(9000,9009));k=s*(f-F)-h
eY=f*f-Y;eB=F*F-B;eS=s*s-c+d*(f+F)
q=2*s*h-c*(f-F)-1+d*(2*Y+f*F)
r2=s*(h-k)-1+d*(Y+f*F+B)
assert r2==q-eS*(f-F)+d*(eY-eB)
ch=h*h-f+d*f*Y;ck=k*k-F+d*F*B
assert ck==ch-(f-F)*r2+d*F*eY-d*f*eB
reg=(1-d*B)*z-k
assert (1-d*B)*(k*z-F)==k*reg+ck
# Recompute the complete primitive sum of squares.
total=P.val(0);active=set()
for r in n.values():
 p=dec(r);assert max(len(m) for a,m in p.t)<=2
 active.update(i for a,m in p.t for i in m)
 den=lcm(*(c.denominator for c in p.t.values()));ints={m:int(c*den) for m,c in p.t.items()};g=gcd(*ints.values())
 pp=P({m:Q(c,g) for m,c in ints.items()});total=total+pp*pp
table=json.loads((HERE/'polynomial301.json').read_bytes())
assert total==dec(table)
assert len(new['coordinates'])==len(active)==301 and active=={c['id'] for c in new['coordinates']}
assert len(n)==277 and len(total.t)==6423 and max(len(m) for a,m in total.t)==4
by_m=defaultdict(dict)
for (a,m),c in total.t.items():by_m[m][a]=c
assert len(by_m)==6423 and any(x=={0:1} or x=={0:-1} for x in by_m.values())
def sign(d):
 d={a:c for a,c in d.items() if c}
 if not d:return 0
 high=max(d);bound=sum(abs(c) for a,c in d.items() if a<high)
 assert bound.denominator==1 and bound.numerator.bit_length()<2048
 return 1 if d[high]>0 else -1
for p in by_m.values():
 assert sign(p)
 for eps in (-1,1):assert sign({a:({2:186624}.get(a,0)+eps*p.get(a,0)) for a in set(p)|{2}})>=0
assert by_m[(89,89,89,89)]=={2:186624}
result={'status':'PASS_AUTHOR_CHECKS_NOT_INDEPENDENT_ACCEPTANCE','variables':301,'witnesses':300,'residuals':277,'degree':4,'monomials':6423,'content':1,'maximum':'186624*C^2; C=3^(2^25)','removed_rows':sorted(removed),'changed_rows':sorted(changed),'deleted_coordinates':sorted(deleted),'universal_reconstruction_identities':True,'source_sha256':PIN,'candidate_sha256':hashlib.sha256((HERE/'candidate301-ir.json').read_bytes()).hexdigest(),'polynomial_sha256':hashlib.sha256((HERE/'polynomial301.json').read_bytes()).hexdigest()}
(HERE/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
