"""Complete chord/tangent equations remove five half-trace guards.

Produces a candidate only. The projection argument is in REPORT.md.
"""
from pathlib import Path
from fractions import Fraction as Q
from functools import reduce
from math import gcd,lcm
import json,hashlib,copy
HERE=Path(__file__).resolve().parent
REPO=HERE.parent.parent/'quartic-version6-release/repository'
SRC=REPO/'quartics/quartic-498-514/candidate498-ir.json'
SEM=REPO/'quartics/quartic-498-514/work/03-depth/beta12/final/candidate-ir.json'
assert hashlib.sha256(SRC.read_bytes()).hexdigest()=='7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a'
src=json.loads(SRC.read_text());sem=json.loads(SEM.read_text())
def add(*ps):
    out={}
    for p in ps:
        for key,c in p.items():out[key]=out.get(key,Q(0))+c
    return {k:v for k,v in out.items() if v}
def scale(p,c):return {k:v*c for k,v in p.items() if v*c}
def sub(p,q):return add(p,scale(q,-1))
def mul(p,q):
    out={}
    for (s,m),c in p.items():
        for (t,n),d in q.items():
            key=(s+t,tuple(sorted(m+n)));out[key]=out.get(key,Q(0))+c*d
    return {k:v for k,v in out.items() if v}
def C(c):return {(0,()):Q(c)} if c else {}
def read(ts,mp=None):
    out={}
    for t in ts:
        m=tuple(sorted(mp[i] if mp else i for i in t['monomial']))
        key=(t.get('sPower',0),m);out[key]=out.get(key,Q(0))+Q(t['coefficient'])
    return {k:v for k,v in out.items() if v}
def terms(p):return [{'sPower':s,'monomial':list(m),'coefficient':str(c)} for (s,m),c in sorted(p.items())]
def normal(p):
    den=reduce(lcm,(c.denominator for c in p.values()),1)
    g=reduce(gcd,(abs(int(c*den)) for c in p.values()),0)
    return scale(p,Q(den,g))
def canonical(p):return scale(p,1/p[min(p)])
def fc(a,b=0):return (C(a),C(b))
def fa(a,b):return tuple(add(a[i],b[i]) for i in range(2))
def fs(a,b):return tuple(sub(a[i],b[i]) for i in range(2))
def fm(a,b):return (add(mul(a[0],b[0]),scale(mul(a[1],b[1]),2)),add(mul(a[0],b[1]),mul(a[1],b[0])))
def fscale(a,c):return tuple(scale(p,c) for p in a)
target_names={c['name']:c['id'] for c in src['coordinates']}
mp={c['id']:target_names[c['name']] for c in sem['coordinates'] if c['name'] in target_names}
def val(name):return tuple(read(sem['values'][name+'.'+str(i)]['terms'],mp) for i in range(2))
rows={r['name']:read(r['terms']) for r in src['residuals']}
new=copy.deepcopy(src);removed_ids=[];removed_rows=[];added=[];contracts=[]
next_row=max(r['id'] for r in src['residuals'])+1
for i,(incoming,root) in enumerate(zip(['H','UA','US','UT','UZ'],['P','A','S','T','Z'])):
    pre=f'V{i}';x1=val(incoming+'.x');y1=fm(val(incoming+'.h'),val(incoming+'.j'))
    x2=fc(Q(57,8),Q(-7,2)) if root=='P' else val(root+'.x')
    y2=fc(Q(-165,8),Q(417,32)) if root=='P' else fm(val(root+'.h'),val(root+'.j'))
    m=val(pre+'.slope');q=val(pre+'.slopeSquare');xr=val(pre+'.x');yr=val(pre+'.y')
    assert xr==fs(fs(q,x1),x2)
    checks={'slope':fs(fm(m,fs(x1,x2)),fa(y1,y2)),
            'slopeSquare':fs(fm(m,m),q),
            'yProduct':fs(fs(fm(m,fs(x1,xr)),y1),yr)}
    # Semantic formulas must be the actual retained equations, including all
    # compiler component normalizations. Match by exact proportionality.
    for label,pair in checks.items():
        for component,p in enumerate(pair):
            candidates=[(name,r) for name,r in rows.items() if name.startswith(pre+'.'+label)]
            matches=[name for name,r in candidates if canonical(p)==canonical(r)]
            assert len(matches)==1,(pre,label,component,matches)
    delta=fs(fscale(fa(x1,x2),3),fscale(q,2))
    tangent=fa(fs(fs(fm(q,delta),fscale(fm(m,yr),2)),fa(fa(fm(x1,x1),fm(x1,x2)),fm(x2,x2))),fc(11,-6))
    guard=target_names[pre+'.dxRationalCoefficientInverse'];removed_ids.append(guard)
    uses=[r for r in src['residuals'] if any(guard in t['monomial'] for t in r['terms'])]
    assert len(uses)==1
    removed_rows.append(uses[0]['id'])
    for component,p in enumerate(tangent):
        assert max(len(mon) for s,mon in p)<=2
        added.append({'id':next_row,'name':pre+'.completeTangent.'+str(component),'terms':terms(normal(p))})
        next_row+=1
    contracts.append({'block':pre,'guardId':guard,'guardRow':uses[0]['id'],
                      'slope':list(map(terms,m)),'slopeSquare':list(map(terms,q)),
                      'x1':list(map(terms,x1)),'x2':list(map(terms,x2)),
                      'resultY':list(map(terms,yr)),'newResiduals':list(map(terms,tangent))})
new['coordinates']=[c for c in new['coordinates'] if c['id'] not in removed_ids]
new['residuals']=[r for r in new['residuals'] if r['id'] not in removed_rows]+added
new['format']='complete-comparison-tangent-quadratic-system-v1'
new['status']='Candidate pending independent review; complete comparison differences with no half-trace guards.'
poly={}
for row in new['residuals']:
    p=normal(read(row['terms']));row['terms']=terms(p)
    poly=add(poly,mul(p,p))
assert len(new['coordinates'])==493 and len(new['residuals'])==472
assert {v for s,m in poly for v in m}=={c['id'] for c in new['coordinates']}
assert max(len(m) for s,m in poly)==4
assert any(c==1 and not s and not any(t and n==m for t,n in poly) for (s,m),c in poly.items())
def write(name,obj):(HERE/name).write_text(json.dumps(obj,indent=2)+'\n')
# Generic identity after q=m^2 and yR=m(x1-xR)-y1 are substituted.
# This proves the added equation on the old nonzero-abscissa-difference chart.
xx,xx2,yy,yy2,mm,dd=({(0,(i,)):Q(1)} for i in range(1,7))
dx=sub(xx,xx2);ss=sub(add(mul(xx,xx),mul(xx,xx2),mul(xx2,xx2)),dd)
aa=sub(mul(mm,dx),add(yy,yy2))
tt=sub(sub(scale(mul(mm,yy),2),mul(mul(mm,mm),dx)),ss)
ee=sub(add(mul(yy,yy),mul(dd,xx)),mul(mul(xx,xx),xx))
ee2=sub(add(mul(yy2,yy2),mul(dd,xx2)),mul(mul(xx2,xx2),xx2))
assert add(sub(mul(dx,tt),sub(ee,ee2)),mul(aa,add(scale(yy2,2),aa)))=={}
write('candidate493-ir.json',new)
write('polynomial493.json',{'fixedParameter':new['fixedParameter'],'terms':terms(poly)})
write('tangent-contracts.json',contracts)
report={'sourceSha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
        'semanticSourceSha256':hashlib.sha256(SEM.read_bytes()).hexdigest(),
        'variables':493,'witnesses':492,'residuals':472,'degree':4,
        'monomials':len({m for s,m in poly}),'removedGuardIds':removed_ids,
        'removedGuardRows':removed_rows,'addedRows':10,
        'genericChordIdentity':True,
        'candidateSha256':hashlib.sha256((HERE/'candidate493-ir.json').read_bytes()).hexdigest()}
write('CHECKS.json',report);print(json.dumps(report,indent=2))
