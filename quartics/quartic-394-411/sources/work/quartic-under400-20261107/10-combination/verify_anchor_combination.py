"""Independent transport and coefficient replay of a recorded combination."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib,sys,copy
H=Path(__file__).resolve().parent
def read(n):return json.loads((H/n).read_text())
def sha(n):return hashlib.sha256((H/n).read_bytes()).hexdigest()
def p(ts):
 d={}
 for t in ts:
  key=tuple([-1]*t.get('sPower',0)+t['monomial']);assert key==tuple(sorted(key));d[key]=d.get(key,0)+F(t['coefficient'])
 return {m:v for m,v in d.items() if v}
def norm(p):
 d=reduce(lcm,(v.denominator for v in p.values()),1);g=reduce(gcd,(abs(int(v*d)) for v in p.values()),0)
 a=F(d,g)*(1 if p[min(p)]>0 else -1)
 return {m:v*a for m,v in p.items()}
def vars(p):return {i for m in p for i in m if i!=-1}
count=int(sys.argv[1]) if len(sys.argv)>1 else 488
cert=read(f'combined{count}-certificate.json');src=read(cert['source']);out=read(f'combined{count}-ir.json')
assert sha(cert['source'])==cert['sourceSha256']
assert sha(f'combined{count}-ir.json')==cert['statistics']['candidateSha256']
rows={r['name']:copy.deepcopy(r) for r in src['residuals']};cs={c['id']:copy.deepcopy(c) for c in src['coordinates']}
for op in cert['steps']:
 assert sha(op['source'])==op['sourceSha256'] and sha(op['target'])==op['targetSha256']
 if op['review']:assert sha(op['review'])==op['reviewSha256']
 before=read(op['source']);after=read(op['target']);br={r['name']:r for r in before['residuals']};ar={r['name']:r for r in after['residuals']}
 bc={c['id']:c for c in before['coordinates']};ac={c['id']:c for c in after['coordinates']}
 deleted=set(br)-set(ar);added=set(ar)-set(br);changed={k for k in br.keys()&ar.keys() if norm(p(br[k]['terms']))!=norm(p(ar[k]['terms']))}
 removed=set(bc)-set(ac);renamed={i for i in set(ac)&set(bc) if ac[i]['name']!=bc[i]['name']}
 coordmap={int(i):j for i,j in op.get('addedCoordinates',{}).items()}
 assert set(ac)-set(bc)==set(coordmap)
 assert deleted==set(op['deletedRows']) and added==set(op['addedRows']) and changed==set(op['changedRows'])
 assert removed==set(op['removedCoordinates']) and renamed==set(op['renamedCoordinates'])
 touched=set().union(*(vars(p(br[k]['terms'])) for k in deleted|changed))|removed|renamed
 assert all(cs[i]['name']==bc[i]['name'] for i in touched)
 assert all(norm(p(rows[k]['terms']))==norm(p(br[k]['terms'])) for k in deleted|changed)
 for k in deleted:del rows[k]
 def remap(ts):
  return [{'sPower':t.get('sPower',0),'monomial':sorted(coordmap.get(i,i) for i in t['monomial']),'coefficient':t['coefficient']} for t in ts]
 for k in changed:rows[k]['terms']=remap(ar[k]['terms'])
 used={r['id'] for r in rows.values()}
 for k,newid in op['addedRows'].items():
  assert newid not in used and k not in rows;used.add(newid);rows[k]=dict(ar[k],id=newid,terms=remap(ar[k]['terms']))
 for i,newid in coordmap.items():
  assert newid not in cs;cs[newid]=dict(ac[i],id=newid)
 for i in removed:del cs[i]
 for i in renamed:cs[i]['name']=ac[i]['name']
 assert len(cs)==op['variablesAfter'] and len(rows)==op['residualsAfter']
 assert set(cs)==set().union(*(vars(p(r['terms'])) for r in rows.values()))
assert {k:(dict(v,terms=[]),p(v['terms'])) for k,v in rows.items()}=={r['name']:(dict(r,terms=[]),p(r['terms'])) for r in out['residuals']}
assert cs=={c['id']:c for c in out['coordinates']}
assert src['fixedParameter']==out['fixedParameter'] and cs[0]==src['coordinates'][0]
total={}
for r in rows.values():
 pp=norm(p(r['terms']));assert max(sum(i!=-1 for i in m) for m in pp)<=2
 ts=list(pp.items())
 for i,(m,v) in enumerate(ts):
  for j in range(i,len(ts)):
   n,w=ts[j];key=tuple(sorted(m+n));total[key]=total.get(key,0)+v*w*(1 if i==j else 2)
total={m:v for m,v in total.items() if v}
assert total==p(read(f'combined{count}-polynomial.json')['terms'])
assert len(total)==cert['statistics']['monomials'] and len(cs)==count
assert max(sum(i!=-1 for i in m) for m in total)==4
assert any(-1 not in m and abs(v)==1 for m,v in total.items())
assert [(m,v) for m,v in total.items() if m.count(-1)==2]==[((-1,-1,57,57,549,549),16)]
assert (57,57,549,549) not in total and (-1,57,57,549,549) not in total
assert max(abs(v.numerator).bit_length() for m,v in total.items() if -1 not in m)<2048
assert max(abs(v) for m,v in total.items() if m.count(-1)==1)<=96
result={'finiteTransportVerified':True,**cert['statistics'],'fullSOSVerified':True,'rows':len(rows),
 'unboundNonAuthorReviewSteps':[s['step'] for s in cert['steps'] if not s['review']],
 'scope':'Exact declared-patch transport and all coefficients. Mathematical acceptance is established by separately authored source reviews.'}
(H/f'combined{count}-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
