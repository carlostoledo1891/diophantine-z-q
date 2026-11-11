import json,hashlib,math
from fractions import Fraction as F
from pathlib import Path
O=Path(__file__).resolve().parent;ROOT=O.parents[3]
P=O.parent/'scalar-contact-quartic-001/candidate232-ir.json'
RAW=ROOT/'work/quartic238-optimization-20261110/linear-lucas/reference233-014/candidate233-ir.json'
M=ROOT/'work/quartic238-optimization-20261110/linear-lucas/reference233-sparse-015/MAPS.json'
assert hashlib.sha256(P.read_bytes()).hexdigest()=='87601e9690f94240e22d949b774522467572d562035d1c3143d04d4c36dc4f35'
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

s=json.loads(P.read_bytes());old=json.loads(RAW.read_bytes());names={r['name']:i for i,r in enumerate(s['residuals'])}
def ci(i):
 assert i!=122
 return i-(i>122)
def ri(i):
 name=old['residuals'][i]['name']
 if name=='scalar.contact_product.definition':name='scalar.four_contact_product.definition'
 return names[name]
rows=[read(r['terms']) for r in s['residuals']];stages=[];dropped=[]
for oldstage in json.loads(M.read_bytes())['stages']:
 t=json.loads(json.dumps(oldstage))
 if t['kind']=='row_add' and t['target']==70:
  assert t['source']==69
  dropped.append(t);continue
 if t['kind']=='coordinates':
  if set(t['old_in_new'])=={'122'}:
   dropped.append(t);continue
  ss={ci(int(i)):{(a,tuple(ci(j) for j in m)):v for (a,m),v in read(ts).items()} for i,ts in t['old_in_new'].items()}
  rows=[sub(p,ss) for p in rows];t['old_in_new']={str(i):ser(p) for i,p in ss.items()}
 elif t['kind']=='row_add':
  i,j=ri(t['target']),ri(t['source']);rows[i]=plus(rows[i],rows[j],F(t['factor']));t.update(target=i,source=j)
 else:
  i,j=ri(t['first']),ri(t['second']);p,q=rows[i],rows[j];rows[i]=plus(p,q);rows[j]=plus(p,q,-1);t.update(first=i,second=j)
 stages.append(t)
assert len(dropped)==2
factors=[]
for i,p in enumerate(rows):
 l=math.lcm(*(v.denominator for v in p.values()));g=math.gcd(*(int(v*l) for v in p.values()));f=F(l,g);rows[i]={k:v*f for k,v in p.items()};factors.append(str(f))
poly={}
for p in rows:poly=plus(poly,mul(p,p))
assert len(rows)==206 and max(len(m) for p in rows for a,m in p)==2
assert set(i for a,m in poly for i in m)==set(range(1,233)) and all(v.denominator==1 for v in poly.values())
s['source']={'parent_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'stage_source_sha256':hashlib.sha256(M.read_bytes()).hexdigest(),'construction':'Accepted sparse233 transformations with deleted-rFour shear omitted and coordinate/row indices explicitly transported; normalization recomputed.'}
for r,p in zip(s['residuals'],rows):r['terms']=ser(p)
stats={'variables':232,'residuals':206,'coordinate_monomials':len({m for a,m in poly}),'parameter_terms':len(poly),'degree':max(len(m) for a,m in poly),'content':math.gcd(*(int(v) for v in poly.values()))}
for name,obj in [('candidate232-ir.json',s),('candidate232-polynomial.json',{'variables':232,'degree':4,'terms':ser(poly)}),('MAPS.json',{'stages':stages,'normalization_factors':factors,'omitted_stages':dropped,'convention':'Ordered old-in-new substitutions; zero-based row operations; normalization recomputed.'}),('STATISTICS.json',stats)]:
 (O/name).write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(stats))
