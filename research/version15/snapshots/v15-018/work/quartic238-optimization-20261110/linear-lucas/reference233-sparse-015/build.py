import json,hashlib,math
from fractions import Fraction as F
from pathlib import Path
O=Path(__file__).resolve().parent;B=O.parents[3]
P=B/'work/quartic238-optimization-20261110/linear-lucas/reference233-014/candidate233-ir.json'
M=B/'work/quartic238-optimization-20261110/linear-lucas/reference235-sparse-012/MAPS.json'
assert hashlib.sha256(P.read_bytes()).hexdigest()=='26d9a2aef8b92fb7fa7d42a24c185ac71d889c0952a0e0bf4b44d09ea9e67691'
assert hashlib.sha256(M.read_bytes()).hexdigest()=='2b67b66717bdb01f24e80be8a34fdbffd9b20ff06f8da7d2586b71d1f3b9fa6d'
def read(ts):return {(t['parameterPower'],tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def add(p,k,v):
 p[k]=p.get(k,F(0))+v
 if not p[k]:del p[k]
def plus(p,q,c=1):
 r=p.copy()
 for k,v in q.items():add(r,k,c*v)
 return r
def mul(p,q):
 r={}
 for (a,m),c in p.items():
  for (b,n),d in q.items():add(r,(a+b,tuple(sorted(m+n))),c*d)
 return r
def sub(p,ss):
 r={}
 for (a,m),c in p.items():
  q={(a,()):c}
  for i in m:q=mul(q,ss.get(i,{(0,(i,)):F(1)}))
  r=plus(r,q)
 return r
def ser(p):return [dict(parameterPower=a,monomial=list(m),coefficient=str(c)) for (a,m),c in sorted(p.items())]
def ci(i):
 assert i not in [21,22]
 return i-2*(i>22)
oldnames=[r['name'] for r in json.loads((B/'work/quartic238-optimization-20261110/linear-lucas/reference235-011/candidate235-ir.json').read_bytes())['residuals']]
def ri(i):
 return names[oldnames[i]]
s=json.loads(P.read_bytes());names={r['name']:i for i,r in enumerate(s['residuals'])};rows=[read(r['terms']) for r in s['residuals']];stages=[]
for old in json.loads(M.read_bytes())['stages']:
 t=json.loads(json.dumps(old))
 if t['kind']=='coordinates':
  ss={ci(int(i)):{(a,tuple(ci(j) for j in m)):v for (a,m),v in read(ts).items()} for i,ts in t['old_in_new'].items()}
  assert 132 not in ss and all(132 not in m for p in ss.values() for a,m in p)
  rows=[sub(p,ss) for p in rows];t['old_in_new']={str(i):ser(p) for i,p in ss.items()}
 elif t['kind']=='row_add':
  i,j=ri(t['target']),ri(t['source']);rows[i]=plus(rows[i],rows[j],F(t['factor']));t.update(target=i,source=j)
 else:
  i,j=ri(t['first']),ri(t['second']);p,q=rows[i],rows[j];rows[i]=plus(p,q);rows[j]=plus(p,q,-1);t.update(first=i,second=j)
 stages.append(t)
def primitive(p):
 l=math.lcm(*(v.denominator for v in p.values()));g=math.gcd(*(int(v*l) for v in p.values()));return {k:v*l/g for k,v in p.items()}
norms=[primitive(p) for p in rows];total={}
for p in norms:total=plus(total,mul(p,p))
newids=[i for i,r in enumerate(s['residuals']) if r['name'].startswith('V0.reference.square_eliminated')]
sourceids=newids+[i for i,r in enumerate(s['residuals']) if r['name'].startswith('testSquare.40.0.')]
for iteration in range(4):
 score=len({m for a,m in total});best=None
 for i in newids:
  for j in sourceids:
   if i==j:continue
   factors_try={-rows[i][k]/rows[j][k] for k in set(rows[i])&set(rows[j])}
   for f in factors_try:
    raw=plus(rows[i],rows[j],f);nn=primitive(raw)
    tt=plus(plus(total,mul(norms[i],norms[i]),-1),mul(nn,nn))
    sc=len({m for a,m in tt})
    if sc<score:
     score=sc;best=(i,j,f,raw,nn,tt)
 if best is None:break
 i,j,f,raw,nn,total=best;rows[i]=raw;norms[i]=nn
 stages.append({'kind':'row_add','target':i,'source':j,'factor':str(f),'label':'new reference-square sparsification'})
 print('row improvement',score,i,j,str(f))
factors=[]
for i,p in enumerate(rows):
 l=math.lcm(*(v.denominator for v in p.values()));g=math.gcd(*(int(v*l) for v in p.values()));f=F(l,g)
 rows[i]={k:v*f for k,v in p.items()};factors.append(str(f))
poly={}
for p in rows:poly=plus(poly,mul(p,p))
assert len(rows)==207 and max(len(m) for p in rows for a,m in p)==2
assert set(i for a,m in poly for i in m)==set(range(1,234))
assert all(v.denominator==1 for v in poly.values())
s['source']={'parent_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'construction':'Invertible sparse presentation of accepted parity core'}
for r,p in zip(s['residuals'],rows):r['terms']=ser(p)
stats={'variables':233,'residuals':len(rows),'coordinate_monomials':len({m for a,m in poly}),'parameter_terms':len(poly),'degree':max(len(m) for a,m in poly),'content':math.gcd(*(int(v) for v in poly.values()))}
for name,obj in [('candidate233-ir.json',s),('candidate233-polynomial.json',{'variables':233,'degree':4,'terms':ser(poly)}),('MAPS.json',{'stages':stages,'normalization_factors':factors,'convention':'Ordered old-in-new substitutions; zero-based row operations; parity coordinate132 untouched.'}),('STATISTICS.json',stats)]:
 (O/name).write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(stats))



