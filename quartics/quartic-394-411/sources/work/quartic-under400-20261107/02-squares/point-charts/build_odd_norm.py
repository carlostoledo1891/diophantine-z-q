"""Replace four field-square odd charts by half-abscissa norm charts."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,copy,sys,math,functools
H=Path(__file__).resolve().parent;W=H.parents[1];R=H.parents[2]/'quartic-version6-release/repository'
S=W/'10-combination/rational453-ir.json';SEM=R/'quartics/quartic-498-514/work/03-depth/beta12/final/candidate-ir.json'
sys.path.insert(0,str(H.parents[3]/'work/quartic-optimization-20261107/02-squares'))
from search import read,encode,add,mul,degree,vs
old=json.loads(S.read_text());sem=json.loads(SEM.read_text());cn={c['name']:c['id'] for c in old['coordinates']};rn={r['name']:r['id'] for r in old['residuals']};mp={c['id']:cn[c['name']] for c in sem['coordinates'] if c['name'] in cn}
def remap(p):return {(s,tuple(sorted(mp[i] for i in m))):v for (s,m),v in p.items()}
def val(n):return tuple(remap(read(sem['values'][n+'.'+str(i)]['terms'])) for i in range(2))
def sc(p,k):return {m:v*k for m,v in p.items() if v*k}
def sub(a,b):return add(a,b,-1)
def c(k):return {(0,()):Q(k)} if k else {}
def v(i):return {(0,(i,)):Q(1)}
def fa(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def fs(a,b):return tuple(sub(x,y) for x,y in zip(a,b))
def fm(a,b):return add(mul(a[0],b[0]),mul(a[1],b[1]),2),add(mul(a[0],b[1]),mul(a[1],b[0]))
def fsc(a,k):return tuple(sc(x,k) for x in a)
def canon(p):return sc(p,1/p[min(p)])
rows={r['id']:copy.deepcopy(r) for r in old['residuals']};ops=[];deleted=set();renames={}
for root in ['A','S','T','Z']:
 pre=root+'.odd.';h,j,x=[val(root+'.'+n) for n in ['h','j','x']];summ=fa(x,j)
 t0,t1,r0,r1=[cn[pre+n] for n in ['t0','t1','r0','r1']];ts=(v(t0),v(t1));rs=(v(r0),v(r1))
 oldC=fs(fm(ts,ts),fsc(summ,2));oldK=fs(fa(fm(ts,h),summ),fm((c(1),c(1)),fm(rs,rs)))
 for k in range(2):
  assert canon(read(rows[rn[pre+'halfParameter.'+str(k)]]['terms']))==canon(oldC[k])
  assert canon(read(rows[rn[pre+'halfAbscissaClass.'+str(k)]]['terms']))==canon(oldK[k])
 a=(v(t0),v(t1));half=fs(fs(fm(a,a),fsc(fm(summ,a),2)),(c(11),c(-6)))
 norm=add(add(mul(a[0],a[0]),mul(a[1],a[1]),-2),mul(v(r0),v(r0)))
 for k in range(2):
  rid=rn[pre+'halfParameter.'+str(k)];rows[rid]['name']=pre+'halfAbscissaEquation.'+str(k);rows[rid]['terms']=encode(half[k])
 rid=rn[pre+'halfAbscissaClass.0'];rows[rid]['name']=pre+'halfAbscissaNorm';rows[rid]['terms']=encode(norm)
 drop=rn[pre+'halfAbscissaClass.1'];del rows[drop];deleted.add(r1)
 renames.update({t0:pre+'a0',t1:pre+'a1',r0:pre+'normRoot'})
 ops.append({'root':root,'oldCoordinates':[t0,t1,r0,r1],'newCoordinates':[t0,t1,r0],'deletedRow':drop,'oldRows':[rn[pre+'halfParameter.'+str(k)] for k in range(2)]+[rn[pre+'halfAbscissaClass.'+str(k)] for k in range(2)]})
coords=[dict(x,name=renames.get(x['id'],x['name'])) for x in old['coordinates'] if x['id'] not in deleted]
out=dict(old,coordinates=coords,residuals=list(rows.values()),status='Candidate pending independent review: odd halfpoint norm charts.')
(H/'candidate449-ir.json').write_text(json.dumps(out,indent=2)+'\n');total={}
for r in out['residuals']:
 p=read(r['terms']);den=functools.reduce(math.lcm,(v.denominator for v in p.values()),1);g=functools.reduce(math.gcd,(abs(v.numerator*(den//v.denominator)) for v in p.values()),0);p=sc(p,Q(den,g));total=add(total,mul(p,p))
assert {x for s,m in total for x in m}=={x['id'] for x in coords}
(H/'polynomial449.json').write_text(json.dumps({'fixedParameter':old['fixedParameter'],'terms':encode(total)},indent=2)+'\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
cert={'source':str(S),'sourceSha256':sha(S),'semanticSource':str(SEM),'semanticSourceSha256':sha(SEM),'manuscript':str(R/'manuscripts/quartic_v12.tex'),'manuscriptSha256':sha(R/'manuscripts/quartic_v12.tex'),'candidateSha256':sha(H/'candidate449-ir.json'),'polynomialSha256':sha(H/'polynomial449.json'),'operations':ops,'counts':{'variables':len(coords),'witnesses':len(coords)-1,'residuals':len(rows),'degree':degree(total),'monomials':len({m for s,m in total})}}
(H/'certificate449.json').write_text(json.dumps(cert,indent=2)+'\n');print(json.dumps(cert['counts'],indent=2))
