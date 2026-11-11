"""Exact semantic audit using independently implemented upstream arithmetic."""
import json,hashlib,importlib.util,re,time
from math import gcd,lcm
from functools import reduce
from pathlib import Path
from fractions import Fraction as Q
H=Path(__file__).resolve().parent
REPO=H.parents[2]/'quartic-version6-release/repository'
VP=REPO/'quartics/quartic-523-540/final523_540/verify_elimination.py'
spec=importlib.util.spec_from_file_location('polynomial_verifier',VP);V=importlib.util.module_from_spec(spec);spec.loader.exec_module(V)
def read(p):return json.loads(p.read_text())
base=read(H/'baseline486.json');new=read(H/'candidate479-ir.json')
dep=read(REPO/'quartics/quartic-498-514/work/03-depth/beta12/final/candidate-ir.json')
assert hashlib.sha256((H/'baseline486.json').read_bytes()).hexdigest()=='55043867418ca00c68add72560b11055c71d082747d6bea61522168885875787'
assert hashlib.sha256((REPO/'quartics/quartic-498-514/work/03-depth/beta12/final/candidate-ir.json').read_bytes()).hexdigest()=='4466bd973383ba404b1cc50deaf2aa4f77361850c090dc8af80b7ba77249d57c'
rows={r['name']:V.readpoly(r['terms']) for r in base['residuals']};coords={c['id']:c['name'] for c in base['coordinates']};cn={v:k for k,v in coords.items()}
ONE={(0,()):Q(1)}
def var(i):return {(0,(i,)):Q(1)}
def sc(p,a):return {k:v*a for k,v in p.items() if v*a}
def add(a,b):return V.add(a,b)
def sub(a,b):return add(a,sc(b,-1))
def fv(name):
 name=name.replace('testSquare.10.','testSquare.12.').replace('.E10','.E12')
 return tuple(V.readpoly(dep['values'][name+'.'+str(j)]['terms']) for j in range(2))
def fm(a,b):return add(V.mul(a[0],b[0]),sc(V.mul(a[1],b[1]),2)),add(V.mul(a[0],b[1]),V.mul(a[1],b[0]))
def ev(p,env):
 d={}
 for (s,m),a in p.items():
  t={(s,()):a}
  for x in m:t=V.mul(t,env.get(x,var(x)))
  d=add(d,t)
 return d
traces=[]
def solve(selected,unknown,env):
 trace={'rows':list(selected),'preassigned':{str(x):V.terms(p) for x,p in env.items()},'pivots':[]}
 traces.append(trace)
 todo=selected.copy();unknown=unknown-set(env);progress=True
 while todo and progress:
  progress=False
  for name,p in list(todo.items()):
   ids=V.variables(p)&unknown
   if not ids:
    assert ev(p,env)=={},name
    del todo[name];progress=True;continue
   if len(ids)!=1:continue
   x=next(iter(ids));a=p.get((0,(x,)))
   if not a or any(x in m and (s,m)!=(0,(x,)) for s,m in p):continue
   q=sc(sub(p,{(0,(x,)):a}),-1/a)
   trace['pivots'].append({'row':name,'coordinate':x,'coefficient':str(a),'replacementBeforeEarlierSubstitutions':V.terms(q)})
   env[x]=ev(q,env);unknown.remove(x);del todo[name];progress=True
 if todo:raise RuntimeError(('nontriangular',len(todo),[(name,[coords.get(x,x) for x in V.variables(p)&unknown]) for name,p in todo.items()][:8]))
 assert not unknown,unknown
 return env

start=time.time();result=[];canonical={};oldchecked=set()
for order,n in [(1,9),(10,2),(40,5)]:
 prefixes=[f'symmetric.{12 if order==10 else order}.']+[f'detector{k}.E{order}.' for k in range(3)]
 selected={name:p for name,p in rows.items() if any(name.startswith(pre) for pre in prefixes)}
 unknown={i for i,name in coords.items() if any(name.startswith(pre) for pre in prefixes)}
 env={}
 for detector in range(3):
  q=cn[f'detector{detector}.q'+('1' if order==1 else str(order))]
  for i,name in coords.items():
   match=re.fullmatch(f'detector{detector}\\.E{order}\\.power([0-9]+)\\.quadratic',name)
   if match:env[i]={(0,(q,)*int(match[1])):Q(1)}
 env=solve(selected,unknown,env)
 oldchecked|=set(selected)
 for detector in range(3):
  q=var(cn[f'detector{detector}.q'+('1' if order==1 else str(order))]);expected=(ONE,{})
  for i in range(n):
   t=fv(f'testSquare.{order}.{i}');expected=fm(expected,(add(ONE,V.mul(q,t[0])),V.mul(q,t[1])))
  actual=tuple(ev(p,env) for p in fv(f'detector{detector}.E{order}'))
  assert actual==expected,(order,detector)
  canonical[detector,order]=expected
  result.append({'order':order,'detector':detector,'componentTerms':list(map(len,actual))})
 print('Verified old order',order,'rows',len(selected),'elapsed',round(time.time()-start,1),flush=True)
newrows={r['name']:V.readpoly(r['terms']) for r in new['residuals']}
newcoords={c['id']:c['name'] for c in new['coordinates']};newcn={v:k for k,v in newcoords.items()}
assert len(newrows)==len(new['residuals'])==len({r['id'] for r in new['residuals']})
assert len(newcoords)==len(newcn)==len(new['coordinates'])
newchecked=set()
for order,n in [(1,9),(10,2),(40,5)]:
 prefixes=[f'hybrid.{order}.']+[pre for k in range(3) for pre in [f'hybrid.det{k}.eval{order}.',f'hybrid.det{k}.order{order}.']]
 selected={name:p for name,p in newrows.items() if any(name.startswith(pre) for pre in prefixes)}
 unknown={i for i,name in newcoords.items() if any(name.startswith(pre) for pre in prefixes)}
 env={}
 for detector in range(3):
  q=cn[f'detector{detector}.q'+('1' if order==1 else str(order))]
  for i,name in newcoords.items():
   match=re.fullmatch(f'detector{detector}\\.E{order}\\.power([0-9]+)\\.quadratic',name)
   if match:env[i]={(0,(q,)*int(match[1])):Q(1)}
 env=solve(selected,unknown,env);newchecked|=set(selected)
 for detector in range(3):
  groups=len(new['hybridPartitions'][str(order)])
  pre=f'hybrid.det{detector}.'+(f'eval{order}.0' if groups==1 else f'order{order}.product{groups-1}')
  actual=tuple(env[newcn[pre+'.'+str(j)]] for j in range(2))
  assert actual==canonical[detector,order],('new',detector,order)
 print('Verified new order',order,'rows',len(selected),'elapsed',round(time.time()-start,1),flush=True)

# Verify old and new final multiplication networks without expanding their
# sixteen-factor products: use the nine already proved field-output pairs
# as independent formal inputs to these small multiplication networks.
for detector in range(3):
 env={};nenv={};expect=(ONE,{})
 for slot,order in enumerate([1,10,40]):
  atoms=(var(10000+slot*2),var(10001+slot*2));expect=fm(expect,atoms)
  for j,semantic in enumerate(fv(f'detector{detector}.E{order}')):
   x=cn[f'detector{detector}.E{order}.sum.{j}.quadratic'];a=semantic[(0,(x,))]
   env[x]=sc(sub(atoms[j],sub(semantic,{(0,(x,)):a})),1/a)
  groups=len(new['hybridPartitions'][str(order)])
  pre=f'hybrid.det{detector}.'+(f'eval{order}.0' if groups==1 else f'order{order}.product{groups-1}')
  for j in range(2):nenv[newcn[pre+'.'+str(j)]]=atoms[j]
 prefixes=[f'detector{detector}.Wfirst.',f'detector{detector}.W.']
 selected={name:p for name,p in rows.items() if any(name.startswith(pre) for pre in prefixes)}
 unknown={i for i,name in coords.items() if any(name.startswith(pre) for pre in prefixes)}
 env=solve(selected,unknown,env);oldchecked|=set(selected)
 assert tuple(ev(p,env) for p in fv(f'detector{detector}.W'))==expect
 prefixes=[f'hybrid.det{detector}.product',f'hybrid.det{detector}.W.']
 selected={name:p for name,p in newrows.items() if any(name.startswith(pre) for pre in prefixes)}
 unknown={i for i,name in newcoords.items() if any(name.startswith(pre) for pre in prefixes)}
 unknown|={newcn[f'detector{detector}.actualW.{j}'] for j in range(2)}
 nenv=solve(selected,unknown,nenv);newchecked|=set(selected)
 assert tuple(nenv[newcn[f'detector{detector}.actualW.{j}']] for j in range(2))==expect

# Every untouched equation survives under the exact affine output recentering.
construction=read(H/'candidate479-construction.json')
dropped=set(construction['removedRows']);removed=set(construction['removedCoordinates'])
assert set(rows)-dropped==set(newrows)-newchecked
assert dropped<=oldchecked
assert set(coords)-set(newcoords)==removed
w_maps=[]
for detector in range(3):
 for j,semantic in enumerate(fv(f'detector{detector}.W')):
  x=cn[f'detector{detector}.W.{j}.quadratic'];a=semantic[(0,(x,))]
  replacement=sc(sub(var(x),sub(semantic,{(0,(x,)):a})),1/a)
  w_maps.append({'coordinate':x,'newName':f'detector{detector}.actualW.{j}',
                 'sourceSemantic':V.terms(semantic),'oldCoordinateReplacement':V.terms(replacement)})
for x in set(coords)&set(newcoords):
 assert newcoords[x]==next((m['newName'] for m in w_maps if m['coordinate']==x),coords[x])
for name in set(rows)-dropped:
 p=rows[name]
 for m in w_maps:p=V.subst(p,m['coordinate'],V.readpoly(m['oldCoordinateReplacement']))
 assert p==newrows[name],name
 assert not V.variables(p)&removed
assert {v for p in newrows.values() for v in V.variables(p)}==set(newcoords)
assert new['fixedParameter']==base['fixedParameter']=={'name':'C','value':'3^(2^25)','coordinate':False}
assert next(c for c in new['coordinates'] if c['id']==0)==next(c for c in base['coordinates'] if c['id']==0)

total={}
for p in newrows.values():
 assert V.degree(p)<=2
 den=reduce(lcm,(v.denominator for v in p.values()),1);g=reduce(gcd,(abs(int(v*den)) for v in p.values()),0)
 p=sc(p,Q(den,g));total=add(total,V.mul(p,p))
assert V.degree(total)==4 and all(v.denominator==1 for v in total.values())
assert any(s==0 and v==1 for (s,m),v in total.items())
assert [(m,v) for (s,m),v in total.items() if s==2]==[((57,57),16)]
assert not any(s!=2 and m==(57,57) for s,m in total)
assert max(abs(v.numerator).bit_length() for (s,m),v in total.items() if s==0)<2048
assert max(abs(v) for (s,m),v in total.items() if s==1)<=48
(H/'polynomial479.json').write_text(json.dumps({'fixedParameter':new['fixedParameter'],'terms':V.terms(total)},indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
report={'verified':True,'sourceSha256':sha(H/'baseline486.json'),'candidateSha256':sha(H/'candidate479-ir.json'),
 'polynomialSha256':sha(H/'polynomial479.json'),'depthSemanticSourceSha256':sha(REPO/'quartics/quartic-498-514/work/03-depth/beta12/final/candidate-ir.json'),
 'oldOutputProductIdentities':result,'oldVerifiedRows':len(oldchecked),'newVerifiedRows':len(newchecked),
 'coordinates':len(newcoords),'witnesses':len(newcoords)-1,'quadraticResiduals':len(newrows),'degree':4,
 'monomials':len({m for s,m in total}),'formalTerms':len(total),'content':1,'maximumCoefficient':'16*3^(2^26)',
 'elapsed':time.time()-start,'proof':'Both private circuits have unique polynomial lifts after the retained power identities; each of nine field outputs is checked equal as a full polynomial. Final multiplication networks and every outside affine recentering are checked separately.'}
(H/'HYBRID-VERIFICATION.json').write_text(json.dumps(report,indent=2)+'\n')
(H/'hybrid-certificate.json').write_text(json.dumps({'sourceSha256':report['sourceSha256'],'candidateSha256':report['candidateSha256'],
 'depthSemanticSourceSha256':report['depthSemanticSourceSha256'],'partitions':new['hybridPartitions'],
 'privateCircuitSolves':traces,'outsideRecentring':w_maps,
 'proof':'Each old/new order output equals the same complete polynomial product. Unique private polynomial reconstructions and the checked final multiplication networks identify the full rational solution sets.'},indent=2)+'\n')
print(json.dumps(report,indent=2))


