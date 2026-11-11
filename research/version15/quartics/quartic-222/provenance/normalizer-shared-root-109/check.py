import json,hashlib
from fractions import Fraction as F
from pathlib import Path
O=Path(__file__).resolve().parent;P=Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic238-optimization-20261110/global/resume-20261110/shared-T-elimination224-004/candidate224-ir.json');J=json.loads(P.read_bytes());rows={x['id']:x for x in J['residuals']}
def mon(d):return tuple(sorted((k,v) for k,v in d.items() if v))
def one(c=1,**kw):return {mon({int(k):v for k,v in kw.items()}):F(c)}
def add(a,b):
 z=dict(a)
 for m,c in b.items():z[m]=z.get(m,F(0))+c
 return {m:c for m,c in z.items() if c}
def mul(a,b):
 z={}
 for m,c in a.items():
  for n,d in b.items():
   e=dict(m)
   for k,v in n:e[k]=e.get(k,0)+v
   key=mon(e);z[key]=z.get(key,F(0))+c*d
 return {m:c for m,c in z.items() if c}
def var(k,e=1,c=1):return {((k,e),):F(c)}
def subst(k):
 if k==125:return var(126,2)
 if k==104:return var(102,2)
 if 167<=k<=178:return mul(var(k),mul(var(126),var(102,-1)))
 if k in [179,180]:return mul(var(k),var(102,-1))
 if k==62:return mul(add(var(179,2),var(180,2,2)),var(102,-2))
 if k==63:return mul(mul(var(179),var(180)),var(102,-2))
 return var(k)
def trans(row):
 p={}
 for t in row['terms']:
  assert t['parameterPower']==0
  z=one(int(t['coefficient']))
  for k in t['monomial']:z=mul(z,subst(k))
  p=add(p,z)
 return p
def compact(p):
 out={}
 for m,c in p.items():
  d=dict(m)
  for k,stored in [(102,104),(126,125)]:
   n=d.get(k,0)
   assert n>=0
   if n>=2:d[k]=n%2;d[stored]=d.get(stored,0)+n//2
  key=mon(d);assert all(v>=0 for k,v in key);out[key]=out.get(key,F(0))+c
 return {m:c for m,c in out.items() if c}
def serial(p):return [{'coefficient':str(c),'monomial':[k for k,e in m for _ in range(e)]} for m,c in sorted(p.items())]

LIFT=set(range(47,55))|set(range(56,60))
def subst(k):
 if k==125:return var(126,2)
 if k==104:return var(102,2)
 if k in LIFT:return mul(var(k),var(126))
 if 167<=k<=178 or 195<=k<=202 or 209<=k<=216:return mul(var(k),mul(var(126),var(102,-1)))
 if k in [179,180,207,208,221,222] or 203<=k<=206 or 217<=k<=220:return mul(var(k),var(102,-1))
 for f,u in [(62,179),(66,207),(68,221)]:
  if k==f:return mul(add(var(u,2),var(u+1,2,2)),var(102,-2))
  if k==f+1:return mul(mul(var(u),var(u+1)),var(102,-2))
 return var(k)
selected=list(range(10,16))+list(range(24,28))+list(range(116,134))+list(range(152,188))
actual=[]
for n in selected:
 if 10<=n<=13:fac=var(126,-1)
 elif n in [14,15,24,25,26,27]:fac=var(126,-2)
 elif 116<=n<=129:fac=mul(var(102,2),var(126,-2))
 elif 130<=n<=133:fac=mul(var(102),var(126,-1))
 else:
  m=(n-152)%18
  fac=mul(var(102,2),var(126,-2)) if m<=7 else var(102,2) if m<=13 else mul(var(102),var(126,-1))
 p=compact(mul(trans(rows[n]),fac))
 removed=n in [124,125,160,161,178,179]
 assert (not p)==removed,(n,p)
 if p:assert max(sum(e for k,e in m) for m in p)<=2,(n,p)
 actual.append({'old_row':n,'multiplier':[(dict(m),str(c)) for m,c in fac.items()],'removed_definition':removed,'terms':serial(p)})
# Confirm the complete occurrence census for all newly repurposed L/C/AT slots.
census=[r['id'] for r in J['residuals'] if any(k in LIFT for t in r['terms'] for k in t['monomial'])]
assert set(census)<=set(selected)
# Independent monomial comparison of trace after q^2 scaling.
def normdiff(a,b):return add(add(var(a,2),var(b,2)),mul(var(a,1,-2),var(b)))
def tracepart(a,b):return add(normdiff(a,b),{m:2*c for m,c in normdiff(a+1,b+1).items()})
trace=mul(trans(rows[192]),var(102,2))
G=add(mul(var(4,1,8),var(98)),{m:-c for m,c in tracepart(185,187).items()})
Z={}
for a,b in [(171,173),(199,201),(213,215)]:Z=add(Z,tracepart(a,b))
expected=add(mul(var(102,2),G),{m:-c for m,c in mul(var(126,2),Z).items()})
assert trace==expected
needed=[9,43,44,45,46,56,57,68,71,73]
for n in needed:
 # No source coordinate in the domain rows is rescaled, replaced or deleted.
 ids={k for t in rows[n]['terms'] for k in t['monomial']}
 assert not ids.intersection(LIFT|set(range(167,181))|set(range(195,223))|{62,63,66,67,68,69})
result={'source_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'selected_rows':actual,'rows_checked':len(actual),'removed_definitions':[124,125,160,161,178,179],'complete_new_L_C_AT_consumer_census':census,'trace_G':serial(G),'trace_Z':serial(Z),'trace_identity_exact':True,'trace_replacement':'x104*G-x125*Z','domain_rows_unaffected':needed,'extra_M_helper_required':False,'scope':'Exact replacement normalization for root blocks1,3,4 plus every L/C/AT consumer; existing paired-factor rewrite must still be composed/independently checked.'}
(O/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['selected_rows','trace_G','trace_Z']}))
