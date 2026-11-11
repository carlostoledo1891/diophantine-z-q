"""Producer-free literal S-extension and complete299 SOS checker."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from math import gcd,lcm
import hashlib,json,copy
HERE=Path(__file__).resolve().parent
SRC=HERE.with_name('reciprocal301')/'candidate301-ir.json'
PIN='ecc9bb4e2e4b5a5a2109524a40c4140317f036d9811b580b04711e4a89cb25e6'
assert hashlib.sha256(SRC.read_bytes()).hexdigest()==PIN
old=json.loads(SRC.read_bytes());new=json.loads((HERE/'candidate299-ir.json').read_bytes())
def validate_active(ir):
 declared={c['id'] for c in ir['coordinates']}
 active={i for r in ir['residuals'] for t in r['terms'] for i in t['monomial']}
 assert len(declared)==len(ir['coordinates']) and active==declared,(active-declared,declared-active)
validate_active(new)
bad=copy.deepcopy(new)
for row in bad['residuals']:
 if row['id'] in {120,121,148,149}:
  for term in row['terms']:term['monomial']=[{196:202,197:203}.get(i,i) for i in term['monomial']]
try:validate_active(bad)
except AssertionError:pass
else:raise AssertionError('undeclared-cache negative fixture was not rejected')
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
D=K(11,-6)
N=K(Q(-87,41)-v(142)+Q(7,2)*v(143)-Q(80,41)*v(700)+Q(212,41)*v(701),Q(129,164)+Q(7,4)*v(142)-v(143)+Q(106,41)*v(700)-Q(80,41)*v(701))
a,b,c,f,h,F,s,Y,B,L,z=map(pair,(5,7,84,25,27,118,120,257,196,236,168))
c=pair(84,2);Y=pair(257,2);B=pair(196,2);k=s*(f-F)-h
expected={708:h*h-f+D*f*Y,710:2*s*h-c*(f-F)-1+D*(2*Y+f*F),712:s*s-c+D*(f+F),
 714:a*b-D*h+s*(D*f+c),209:f*f-Y,148:F*F-B,188:h*L+f*N,120:(1-D*B)*z-k,2220:(1-D*Y)*L+h*N}
covered=set()
for rid,eq in expected.items():
 assert dec(n[rid])==eq.a and dec(n[rid+1])==eq.b,rid
 covered.update((rid,rid+1))
assert set(n)-set(o)=={2220,2221} and not set(o)-set(n)
assert {i for i in o if o[i]!=n[i]}==covered-{2220,2221}
deleted={122,123};repurposed={25,26,27,28,118,119,120,121}
oc={c['id']:c for c in old['coordinates']};nc={c['id']:c for c in new['coordinates']}
assert set(oc)-set(nc)==deleted and not set(nc)-set(oc)
for i in nc:
 if i in repurposed:assert {k:v for k,v in nc[i].items() if k!='name'}=={k:v for k,v in oc[i].items() if k!='name'}
 else:assert oc[i]==nc[i]
for rid,row in o.items():
 if any((deleted|repurposed).intersection(t['monomial']) for t in row['terms']):assert rid in covered
for rid,row in n.items():
 assert not any(deleted.intersection(t['monomial']) for t in row['terms'])
 if any(repurposed.intersection(t['monomial']) for t in row['terms']):assert rid in covered
for key in old:
 if key not in ['coordinates','residuals','status']:assert old[key]==new[key]
# Both root square conditions, including b, remain literal source rows.
for rid,eq in [(8,a*a-c),(10,b*b-c*c+D)]:
 for j,want in enumerate((eq.a,eq.b)):
  got=dec(n[rid+j]);assert n[rid+j]==o[rid+j] and got.t.keys()==want.t.keys()
  assert len({got.t[m]/want.t[m] for m in want.t})==1
# Source physical primary ratio and alternate ratio have the expected old scaling.
for rid,eq in [(188,pair(27)*L-pair(25)*N),(120,pair(122)*z+pair(118))]:
 assert dec(o[rid])==eq.a and dec(o[rid+1])==eq.b
# Bind the actual old cache meanings, not merely their selected indices.
for rid,eq in [(209,pair(27)**2-c+D*c*Y),(148,pair(122)**2-c+D*c*B)]:
 assert dec(o[rid])==eq.a and dec(o[rid+1])==eq.b
# The complete inherited S half-sign action also flips its scalar witnesses.
flips={5,6,7,8,543,544,549};negated=[]
for rid,row in n.items():
 q=dec(row);flipped=P({(a,m):v*(-1)**sum(i in flips for i in m) for (a,m),v in q.t.items()})
 assert flipped==q or flipped==-q,rid
 if flipped==-q:negated.append(rid)
assert set(negated)=={474,475,513,514}
# Polynomial reconstruction and raw-ratio saturation identities, no division.
d,f,F,h,s,c,Y,B,z=map(v,range(9000,9009));k=s*(f-F)-h
eY=f*f-Y;eB=F*F-B;eS=s*s-c+d*(f+F)
q=2*s*h-c*(f-F)-1+d*(2*Y+f*F);r2=s*(h-k)-1+d*(Y+f*F+B)
assert r2==q-eS*(f-F)+d*(eY-eB)
ch=h*h-f+d*f*Y;ck=k*k-F+d*F*B
assert ck==ch-(f-F)*r2+d*F*eY-d*f*eB
reg=(1-d*B)*z-k
assert (1-d*B)*(k*z-F)==k*reg+ck
# Complete primitive sum of squares and exact specialized coefficient maximum.
total=P.val(0);active=set()
for row in n.values():
 p=dec(row);assert max(len(m) for t,m in p.t)<=2
 active.update(i for t,m in p.t for i in m)
 den=lcm(*(c.denominator for c in p.t.values()));ints={m:int(c*den) for m,c in p.t.items()};g=gcd(*ints.values())
 pp=P({m:Q(c,g) for m,c in ints.items()});total=total+pp*pp
assert total==dec(json.loads((HERE/'polynomial299.json').read_bytes()))
assert len(nc)==len(active)==299 and active==set(nc) and len(n)==279
assert len(total.t)==6630 and max(len(m) for t,m in total.t)==4
by_m=defaultdict(dict)
for (t,m),c in total.t.items():by_m[m][t]=c
assert len(by_m)==6630 and any(d=={0:1} or d=={0:-1} for d in by_m.values())
def sign(d):
 d={a:c for a,c in d.items() if c}
 if not d:return 0
 high=max(d);bound=sum(abs(c) for a,c in d.items() if a<high)
 assert bound.denominator==1 and bound.numerator.bit_length()<2048
 return 1 if d[high]>0 else -1
for p in by_m.values():
 assert sign(p)
 for eps in (-1,1):assert sign({t:({2:186624}.get(t,0)+eps*p.get(t,0)) for t in set(p)|{2}})>=0
assert by_m[(89,89,89,89)]=={2:186624}
result={'status':'PASS_AUTHOR_CHECKS_NOT_INDEPENDENT_ACCEPTANCE','variables':299,'witnesses':298,'residuals':279,'degree':4,'monomials':6630,'content':1,'maximum':'186624*C^2; C=3^(2^25)','deleted_coordinates':sorted(deleted),'changed_rows':sorted(covered-{2220,2221}),'added_rows':[2220,2221],'S_root_orientation':'a*b=D*h-s*(D*f+c)','S_root_square_conditions_unchanged':True,'all_outside_consumers_unchanged':True,'active_cache_negative_fixture_rejected':True,'source_sha256':PIN,'candidate_sha256':hashlib.sha256((HERE/'candidate299-ir.json').read_bytes()).hexdigest(),'polynomial_sha256':hashlib.sha256((HERE/'polynomial299.json').read_bytes()).hexdigest()}
(HERE/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
