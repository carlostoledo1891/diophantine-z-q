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
S=fp(19,20); g=fp(134,135); T=fp(233,234)
alpha=fc(156,F(69,2)); beta=fc(118,60)
N=fa(fa(fm(alpha,S),fc(-288,-128)),fm(fc(252,-672),g)); D=fa(fm(beta,S),alpha)
oldrows={r['id']:terms(r['terms']) for r in old['residuals']}
removed=set(); expected={}; checked=[]
for j in range(4):
 z=fp(21+2*j,22+2*j); L=fp(49+4*j,50+4*j)
 alt=fa(fm(N,z),fm(D,L)); ar=9+4*j
 assert oldrows[ar]==alt[0] and oldrows[ar+1]==scale(alt[1],2)
 E=fa(fp(177+14*j,178+14*j),neg(fp(179+14*j,180+14*j))); k=fp(187+14*j,188+14*j)
 kr=fm(fc(6,-2),k); rr=144+18*j
 root=fa(E,fm(kr,z)); assert oldrows[rr]==root[0] and oldrows[rr+1]==root[1]
 out=fa(fm(E,T),neg(fm(kr,L)))
 expected[rr]=remap(out[0]); expected[rr+1]=remap(out[1]); removed|={ar,ar+1}; checked += [ar,ar+1,rr,rr+1]
for r in old['residuals']:
 if r['id'] not in removed and r['id'] not in expected:expected[r['id']]=remap(terms(r['terms']))
assert len(expected)==198
for r in new['residuals'][:198]:assert terms(r['terms'])==expected[r['parentRowId']],r['id']
defn=fa(fm(D,T),neg(N)); assert terms(new['residuals'][198]['terms'])==remap(defn[0]); assert terms(new['residuals'][199]['terms'])==remap(scale(defn[1],2))
affected={r['id'] for r in old['residuals'] if any(any(21<=i<=28 for i in t['monomial']) for t in r['terms'])}; assert affected==set(checked)
poly=add(*(scale(mul(terms(r['terms']),terms(r['terms'])),r.get('positive_square_weight',1)) for r in new['residuals']))
assert poly==terms(pub['terms'])
assert new['inputCoordinate']==old['inputCoordinate']==1 and new['fixedParameter']==old['fixedParameter']
assert set(i for r in new['residuals'] for t in r['terms'] for i in t['monomial'])==set(range(1,227))
assert max(len(k[1]) for k in poly)==4
content=reduce(gcd,(abs(v.numerator) for v in poly.values())); assert content==1
norma=F(156)**2-2*F(69,2)**2; normb=118**2-2*60**2;assert norma.numerator%149 and normb%149
# Group all parameter coefficients by coordinate monomial, with exact integers.
profiles=defaultdict(dict)
for (p,m),v in poly.items():profiles[m][p]=int(v)
assert max(abs(d.get(0,0)) for d in profiles.values()) < 149**214+1
assert max(abs(d.get(1,0)) for d in profiles.values()) == 44402
assert all(set(d)<=set([0]) or (m==(114,114) and d=={0:1,2:1}) or set(d)=={1} for m,d in profiles.items())
print(json.dumps({'status':'pass','new_rows_checked':200,'unchanged_rows':190,'changed_parent_rows':8,'removed_parent_rows':8,'new_definition_rows':2,'deleted_coordinate_consumer_rows':sorted(affected),'parameter_terms':len(poly),'coordinate_monomials':len(profiles),'degree':4,'content':content,'all_226_variables_used':True,'input_and_parameter_unchanged':True,'alpha_norm':str(norma),'beta_norm':str(normb),'constant_max':max(abs(d.get(0,0)) for d in profiles.values()),'linear_parameter_max':max(abs(d.get(1,0)) for d in profiles.values()),'quadratic_parameter_terms':[{ 'monomial':list(m),'profile':d} for m,d in profiles.items() if 2 in d]},indent=2))
