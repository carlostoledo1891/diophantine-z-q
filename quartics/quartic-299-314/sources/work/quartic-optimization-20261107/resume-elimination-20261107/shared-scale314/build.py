"""Emit the new guarded common-scale presentation. Arithmetic review is separate."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import copy, hashlib, json
H=Path(__file__).resolve().parent
WORK=H.parents[2]
SOURCE=WORK/'quartic-under300-20261107/10-combination/combined315/candidate315-ir.json'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='d450a34735fe84bab0900abb3931740d4f7cedb1004ede7a81e1a09c4249f8b8'
old=json.loads(SOURCE.read_bytes()); new=copy.deepcopy(old)
rows={r['id']:r for r in old['residuals']}
def clean(p):return {m:c for m,c in p.items() if c}
def plus(*ps):
    out=defaultdict(F)
    for p in ps:
        for m,c in p.items():out[m]+=c
    return clean(out)
def times(p,q):
    out=defaultdict(F)
    for m,c in p.items():
        for n,d in q.items():out[tuple(sorted(m+n))]+=c*d
    return clean(out)
def scale(p,c):return clean({m:v*c for m,v in p.items()})
def var(i):return {(i,):F(1)}
ONE={():F(1)}
def terms(p):return [{'sPower':0,'monomial':list(m),'coefficient':str(c)} for m,c in sorted(p.items())]
def poly(r):
    assert all(t['sPower']==0 for t in r['terms'])
    return {tuple(t['monomial']):F(t['coefficient']) for t in r['terms']}
def leaf(row,weight):
    out={}
    for m,c in poly(rows[row]).items():
        if weight in m:
            n=list(m);n.remove(weight);out[tuple(n)]=-c
    return out
leaf_specs={'H1':(919,374),'H2':(921,374),'H3':(923,374),'H4':(919,843),
 'M0':(919,369),'M1':(923,369),'U':(921,360),'P1':(921,350),
 'P2':(923,843),'P3':(923,832),'P4':(923,350),'Z1':(921,832),
 'T0':(919,356),'T2':(921,356),'T3':(923,356),'T4':(919,832)}
leaves={name:(leaf(row,w),leaf(row+1,w)) for name,(row,w) in leaf_specs.items()}
layout=[(0,350,355,359,832,356,360,369,374,843),
        (1,398,403,407,833,404,408,417,422,844),
        (2,446,451,455,834,452,456,465,470,845)]
powerids={i for _,E,R2,R3,E4,E8,A,B,C,D in layout for i in (R2,R3,E4,E8,A,B,C,D)}
isgroup=lambda r:r['name'].startswith('three.det') and '.group' in r['name']
removed={r['id'] for r in old['residuals'] if not isgroup(r) and any(powerids.intersection(t['monomial']) for t in r['terms'])}
assert len(removed)==24
dropped={i for _,E,R2,R3,E4,E8,A,B,C,D in layout for i in (A,B,C,D)}
new['coordinates']=[c for c in new['coordinates'] if c['id'] not in dropped]
new['residuals']=[r for r in new['residuals'] if r['id'] not in removed]
names=['gamma','gamma2','gamma4','gamma8','gamma16','inverseGamma16','gamma40','gamma80','gamma160','P1squared.real','P1squared.imag']
for i,name in enumerate(names,1100):new['coordinates'].append({'id':i,'name':'shared314.'+name,'kind':'gate','block':'shared314','protected':False})
for c in new['coordinates']:
    for j,E,R2,R3,E4,E8,A,B,C,D in layout:
        if c['id'] in (R2,R3):c['name']=f'shared314.det{j}.'+('R2' if c['id']==R2 else 'R3')
rid=2000
def add(name,p):
    global rid
    new['residuals'].append({'id':rid,'name':'shared314.'+name,'kind':'structural','block':'shared314','terms':terms(p)});rid+=1
for out,left in [(1101,1100),(1102,1101),(1103,1102),(1104,1103)]:add(f'power{out}',plus(var(out),scale(times(var(left),var(left)),-1)))
add('inverse',plus(times(var(1104),var(1105)),scale(ONE,-1)))
add('power1106',plus(times(var(1106),var(1105)),scale(times(var(1104),var(1103)),-1)))
for out,left in [(1107,1106),(1108,1107)]:add(f'power{out}',plus(var(out),scale(times(var(left),var(left)),-1)))
a,b=leaves['P1']
add('P1square.real',plus(var(1109),scale(times(a,a),-1),scale(times(b,b),-2)))
add('P1square.imag',plus(var(1110),scale(times(a,b),-2)))
leaves['P1square']=(var(1109),var(1110))
scaled={i:1108 for i in (826,827,820,821,822,823,835,836,828,829)}
scaled.update({i:1106 for i in (837,838,839,840)})
scaled.update({i:1107 for i in (830,831,841,842)})
for r in new['residuals']:
    if r['name'].startswith('three.shared.'):
        for t in r['terms']:
            if len(t['monomial'])==1 and t['monomial'][0] in scaled:
                i=t['monomial'][0];assert F(t['coefficient'])==1
                t['monomial']=sorted([i,scaled[i]])
        r['name']='shared314.'+r['name']
for c in new['coordinates']:
    if c['id'] in scaled:c['name']='shared314.scaled.'+c['name']
groups=[ [('R','H1'),('R2','H2'),('E','U'),('E4','Z1')],
 [('R','H3'),('R2','H4'),('R3','P2'),('E4','P4'),('E','P1square'),('E8','T0')],
 [('R','M0'),('R2','M1'),('R3','P3'),('E8','T2'),('E4','T3'),('E','T4')] ]
physicalR={}
for j,E,R2,R3,E4,E8,A,B,C,D in layout:
    er=next(r for r in old['residuals'] if r['name']==f'detector{j}.eWeight.definition')
    R={}
    for m,c in poly(er).items():
        if E in m:
            n=list(m);n.remove(E);R[tuple(n)]=c
        else:assert m==() and c==-1
    physicalR[str(j)]=terms(R)
    add(f'det{j}.R2',plus(var(R2),scale(times(R,R),-1)))
    add(f'det{j}.R3',plus(var(R3),scale(times(R,var(R2)),-1)))
    add(f'det{j}.E4',plus(times(var(E4),var(R3)),scale(var(E),-1)))
    add(f'det{j}.E8',plus(var(E8),scale(times(var(E4),var(E4)),-1)))
    weights={'R':R,'R2':var(R2),'R3':var(R3),'E':var(E),'E4':var(E4),'E8':var(E8)}
    for g,spec in enumerate(groups):
        for component in (0,1):
            row=next(r for r in new['residuals'] if r['name']==f'three.det{j}.group{g}.{component}')
            output=[(m,c) for m,c in poly(row).items() if len(m)==1]
            assert len(output)==1
            p=dict(output)
            if component==0:p=plus(p,scale(ONE,-1))
            for weight,name in spec:p=plus(p,scale(times(weights[weight],leaves[name][component]),-1))
            if g==0 and component==0:p=plus(p,scale(times(var(1104),var(E8)),-1))
            row['terms']=terms(p)
new['coordinates'].sort(key=lambda c:c['id']);new['residuals'].sort(key=lambda r:r['id'])
new['status']='Research candidate314. New arithmetic and complete composition require independent review.'
total=defaultdict(int)
for r in new['residuals']:
    q={(t['sPower'],tuple(t['monomial'])):F(t['coefficient']) for t in r['terms']}
    assert len(q)==len(r['terms']) and all(len(m)<=2 for e,m in q)
    den=lcm(*(c.denominator for c in q.values()));gc=gcd(*(int(c*den) for c in q.values()))
    q={m:int(c*den)//gc for m,c in q.items()}
    for (e,m),c in q.items():
        for (f,n),d in q.items():total[e+f,tuple(sorted(m+n))]+=c*d
def write(name,obj):
    p=H/name;p.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8',newline='\n');return hashlib.sha256(p.read_bytes()).hexdigest()
ih=write('candidate314-ir.json',new)
ph=write('polynomial314.json',{'terms':[{'sPower':e,'monomial':list(m),'coefficient':str(c)} for (e,m),c in sorted(total.items()) if c]})
cert={'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'candidate_sha256':ih,'polynomial_sha256':ph,
 'variables':len(new['coordinates']),'residuals':len(new['residuals']),'coefficient_terms':sum(bool(c) for c in total.values()),'monomials':len({m for (e,m),c in total.items() if c}),
 'deleted_coordinates':sorted(dropped),'removed_rows':sorted(removed),'new_coordinates':list(range(1100,1111)),
 'scaled_coordinates':scaled,'groups':groups,'physicalR':physicalR,'status':'Research only; not independently accepted.'}
write('CERTIFICATE.json',cert);print(json.dumps({k:v for k,v in cert.items() if k not in ('physicalR','groups','scaled_coordinates')},indent=2))
