from fractions import Fraction as F
import json,pathlib
P=pathlib.Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic238-optimization-20261110/global/resume-20261110/shared-T-elimination224-004/FIELD-RELATIONS.json')
rels=next(x for x in json.loads(P.read_text()) if x['dropped']=='g')['relations']
def k(a=0,b=0):return F(a),F(b)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def mul(x,y):return x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def inv(x):
 n=x[0]**2-2*x[1]**2
 assert n
 return x[0]/n,-x[1]/n

# Independent polynomial arithmetic, keys are sorted variable-index tuples.
def pa(*ps):
 out={}
 for p in ps:
  for m,c in p.items():out[m]=add(out.get(m,k()),c)
 return {m:c for m,c in out.items() if c!=k()}
def pm(p,q):
 out={}
 for m,c in p.items():
  for n,d in q.items():
   z=tuple(sorted(m+n));out[z]=add(out.get(z,k()),mul(c,d))
 return {m:c for m,c in out.items() if c!=k()}
def ps(p,c):return {m:mul(v,c) for m,v in p.items() if mul(v,c)!=k()}
def pc(c):return {():c}
def px(i):return {(i,):k(1)}
qs=[{tuple(t['monomial']):k(*t['coefficient']) for t in r} for r in rels]
f,S,g,B,w,W,T=[px(i) for i in range(7)]
a,b,c,d=k(57,-28),k(8,-14),k(88,-48),k(39,-36)
alpha,beta,gamma,delta=k(156,F(69,2)),k(118,60),k(-288,-128),k(252,-672)
ge=ps(pa(pm(pa(ps(S,beta),pc(alpha)),T),ps(S,neg(alpha)),pc(neg(gamma))),inv(delta))
targetF=pa(pm(pa(pc(a),ps(f,c)),ge),ps(pm(f,S),b),ps(f,d))
targetE=pa(ps(pm(S,ge),b),ps(ge,neg(d)),ps(f,neg(a)),pc(k(8)))
Anorm=pa(pc(mul(a,a)),ps(f,mul(k(2),mul(a,c))),ps(B,mul(c,c)))
N=pa(pc(k(8)),ps(f,neg(a)),ps(ge,mul(k(-2),d)))
targetW=pa(pm(Anorm,w),ps(pm(N,N),k(-1)))
checks=json.loads(P.with_name('CONVERSE-RESULT.json').read_text())['checks']
for row,target in zip(checks,[targetF,targetE,targetW]):
 assembled={}
 for term in row['certificate']:
  assembled=pa(assembled,pm(qs[term['relation']],{tuple(term['multiplier']):k(*term['coefficient'])}))
 assert assembled==target,row['name']
 assert not row['remainder']
print(json.dumps({'status':'pass','exact_reverse_identities':[r['name'] for r in checks],'variable_divisions':0,'constant_division':'delta=252-672*sqrt2 only; norm nonzero'},indent=2))
