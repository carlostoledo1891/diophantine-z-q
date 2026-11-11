import json,hashlib,math
from fractions import Fraction as F
from pathlib import Path
O=Path(__file__).resolve().parent
P=O.parent/'shared-T-redundancy224-006/candidate224-ir.json'
M=Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic238-optimization-20261110/global/resume-20261110/shared-alternate-sparse226-002/MAPS.json')
assert hashlib.sha256(P.read_bytes()).hexdigest()=='6b961988414509ff6619fb674b696c745b098d00ad2af326df43e4db5aa5d39f'
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

s=json.loads(P.read_bytes()); rawrows=[read(r['terms']) for r in s['residuals']];rows=[p.copy() for p in rawrows]
cm={int(k):v for k,v in json.loads((P.parent.parent/'shared-T-elimination224-004/MAPS.json').read_text())['old_to_new'].items()}
rm={r['parentRowId']-1:i for i,r in enumerate(s['residuals']) if 'parentRowId' in r}
stages=[];dropped=[]; inverses=[]
def invert(ss):
 ids=sorted(ss);n=len(ids);mat=[]
 for i in ids:
  p=ss[i];assert all(a==0 and len(m)<=1 for a,m in p)
  assert all(not m or m[0] in ids for a,m in p)
  mat.append([p.get((0,(j,)),F(0)) for j in ids]+[F(i==j) for j in ids]+[p.get((0,()),F(0))])
 for k in range(n):
  j=next(j for j in range(k,n) if mat[j][k]);mat[k],mat[j]=mat[j],mat[k];v=mat[k][k];mat[k]=[x/v for x in mat[k]]
  for j in range(n):
   if j!=k:
    v=mat[j][k];mat[j]=[x-v*y for x,y in zip(mat[j],mat[k])]
 inv={}
 for i,j in enumerate(ids):
  p={(0,(k,)):mat[i][n+t] for t,k in enumerate(ids) if mat[i][n+t]}
  if mat[i][-1]:p[(0,())]=-mat[i][-1]
  inv[j]=p
 for j in ids:
  assert sub(ss[j],inv)=={(0,(j,)):F(1)}
  assert sub(inv[j],ss)=={(0,(j,)):F(1)}
 return inv
for old in json.loads(M.read_bytes())['stages']:
 t=json.loads(json.dumps(old))
 if t['kind']=='coordinates':
  ss={cm[int(i)]:{(a,tuple(cm[j] for j in m)):v for (a,m),v in read(ts).items()} for i,ts in t['old_in_new'].items() if int(i) in cm}
  # Include unchanged referenced coordinates in affine inversion.
  ids={j for p in ss.values() for a,m in p for j in m}
  for j in ids:
   if j not in ss:ss[j]={(0,(j,)):F(1)}
  inv=invert(ss);rows=[sub(p,ss) for p in rows];t['old_in_new']={str(i):ser(p) for i,p in ss.items()};t['new_in_old']={str(i):ser(p) for i,p in inv.items()}
 elif t['kind']=='row_add':
  if t['target'] not in rm or t['source'] not in rm:
   assert t['target'] not in rm and t['source'] not in rm;dropped.append(t);continue
  i,j=rm[t['target']],rm[t['source']];rows[i]=plus(rows[i],rows[j],F(t['factor']));t.update(target=i,source=j)
 else:
  i,j=rm[t['first']],rm[t['second']];p,q=rows[i],rows[j];rows[i]=plus(p,q);rows[j]=plus(p,q,-1);t.update(first=i,second=j)
 stages.append(t)
assert len(dropped)==0
factors=[]
for i,p in enumerate(rows):
 l=math.lcm(*(v.denominator for v in p.values()));g=math.gcd(*(int(v*l) for v in p.values()));f=F(l,g);rows[i]={k:v*f for k,v in p.items()};factors.append(str(f))
rev=[{k:v/F(factors[i]) for k,v in p.items()} for i,p in enumerate(rows)]
for t in reversed(stages):
 if t['kind']=='coordinates':rev=[sub(p,{int(i):read(ts) for i,ts in t['new_in_old'].items()}) for p in rev]
 elif t['kind']=='row_add':
  i,j=t['target'],t['source'];rev[i]=plus(rev[i],rev[j],-F(t['factor']))
 else:
  i,j=t['first'],t['second'];p,q=rev[i],rev[j];rev[i]={k:v/2 for k,v in plus(p,q).items()};rev[j]={k:v/2 for k,v in plus(p,q,-1).items()}
assert rev==rawrows
poly={}
for p in rows:poly=plus(poly,mul(p,p))
assert len(rows)==198 and max(len(m) for p in rows for a,m in p)==2
assert set(i for a,m in poly for i in m)==set(range(1,225)) and all(v.denominator==1 for v in poly.values())
for r,p in zip(s['residuals'],rows):r['terms']=ser(p)
s['source']={'parent_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'stage_source_sha256':hashlib.sha256(M.read_bytes()).hexdigest(),'construction':'Exact accepted226 sparse stages with deleted g-shift removed; all198 rows reversed to raw224/198.'}
stats={'variables':224,'residuals':198,'coordinate_monomials':len({m for a,m in poly}),'parameter_terms':len(poly),'degree':max(len(m) for a,m in poly),'content':math.gcd(*(int(v) for v in poly.values())),'affine_stages':sum(t['kind']=='coordinates' for t in stages),'reverse_rows':198}
assert max(abs(v) for (a,m),v in poly.items() if a==0)<149**214
assert [(m,v) for (a,m),v in poly.items() if a==2]==[((114,114),F(1))] and poly[(0,(114,114))]==1
assert max(abs(v) for (a,m),v in poly.items() if a==1)==44402
stats['coefficient_height']='A_N^2+1 for N>=53; defining threshold remains ineffective'
for name,obj in [('candidate224-ir.json',s),('candidate224-polynomial.json',{'variables':224,'degree':4,'inputCoordinate':s['inputCoordinate'],'fixedParameter':s['fixedParameter'],'terms':ser(poly)}),('MAPS.json',{'stages':stages,'normalization_factors':factors,'omitted_stages':dropped}),('STATISTICS.json',stats)]:
 (O/name).write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(stats))
