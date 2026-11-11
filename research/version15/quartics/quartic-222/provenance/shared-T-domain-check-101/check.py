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
p=[{tuple(t['monomial']):k(*t['coefficient']) for t in r} for r in rels]
# f=B=0 in relation3 (zero-based index3): constant+cT*T=0.
z={m:c for m,c in p[3].items() if 0 not in m and 3 not in m}
assert set(z)=={(),(6,)}
T=mul(neg(z[()]),inv(z[(6,)]))
# Substitute this exact T and f=B=0 in relation1; remaining S coefficient and constant.
q={}
for m,c in p[1].items():
 if 0 in m or 3 in m:continue
 n=[]
 for i in m:
  if i==6:c=mul(c,T)
  else:n.append(i)
 q[tuple(n)]=add(q.get(tuple(n),k()),c)
assert q.get((1,),k())==k()
assert q[()]!=k()
print(json.dumps({'status':'f=0 excluded by polynomial equations alone','T':[str(x) for x in T],'remaining_constant':[str(x) for x in q[()]],'remaining_constant_norm':str(q[()][0]**2-2*q[()][1]**2),'uses_scalar_or_149':False},indent=2))
