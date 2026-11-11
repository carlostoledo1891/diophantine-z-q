"""Prepare compact physical tables and the sixteen-coordinate ordinary lift.

This does not approve or publish the selected mathematical candidate.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,hashlib,sys,copy
H=Path(__file__).resolve().parent
n=int(sys.argv[1]);O=H/f'release{n}';O.mkdir(exist_ok=True)
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,d):(O/name).write_text(json.dumps(d,indent=2)+'\n')
def pol(ts):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in ts}
def terms(p):return [{'sPower':s,'monomial':list(m),'coefficient':str(v)} for (s,m),v in sorted(p.items()) if v]
def norm(p):
    den=reduce(lcm,(v.denominator for v in p.values()),1)
    g=reduce(gcd,(abs(int(v*den)) for v in p.values()),0)
    return {m:v*F(den,g) for m,v in p.items()}
def sos(ir):
    out={}
    for row in ir['residuals']:
        p=norm(pol(row['terms']));items=list(p.items())
        for i,((s,m),v) in enumerate(items):
            for j in range(i,len(items)):
                (t,k),w=items[j];key=s+t,tuple(sorted(m+k))
                out[key]=out.get(key,0)+v*w*(1 if i==j else 2)
    return {m:v for m,v in out.items() if v}
source=H/f'combined{n}-ir.json';pp=H/f'combined{n}-polynomial.json'
ir=load(source);poly=load(pp);assert len(ir['coordinates'])==n
assert sos(ir)==pol(poly['terms'])
(O/f'candidate{n}-ir.json').write_bytes(source.read_bytes())
(O/f'polynomial{n}.json').write_bytes(pp.read_bytes())
ordinary=copy.deepcopy(ir);cstart=max(c['id'] for c in ir['coordinates'])+1
cids=list(range(cstart,cstart+16));rowstart=max(r['id'] for r in ir['residuals'])+1
ordinary['fixedParameter']={'name':'C','value':'3^(2^25)','coordinate':True,'sourceCoordinate':cids[-1]}
for row in ordinary['residuals']:
    row['terms']=terms({(0,tuple(sorted(m+(cids[-1],)*s))):v for (s,m),v in pol(row['terms']).items()})
for j,i in enumerate(cids):
    ordinary['coordinates'].append({'id':i,'name':f'constant.c{j}'})
    q={(0,(i,)):F(1),(0,() if j==0 else (cids[j-1],cids[j-1])):F(-3**1024 if j==0 else -1)}
    ordinary['residuals'].append({'id':rowstart+j,'name':f'constant.definition{j}','kind':'constant','block':'constant_lift','terms':terms(q)})
ordinary['status']='Ordinary integer coefficient lift of a frozen research candidate; mathematical review is a separate record.'
op=sos(ordinary);assert all(s==0 for s,m in op)
write(f'candidate{n+16}-ir.json',ordinary);write(f'polynomial{n+16}.json',{'fixedParameter':ordinary['fixedParameter'],'terms':terms(op)})
stats={}
for count,d,q,symbolic in [(n,ir,pol(poly['terms']),True),(n+16,ordinary,op,False)]:
    cs=sorted(d['coordinates'],key=lambda c:c['id']);mp={c['id']:j+1 for j,c in enumerate(cs)}
    coordinate_rows=[{'id':mp[c['id']],'sourceId':c['id'],'name':c['name']} for c in cs]
    compact={'format':'compact-quadratic-residuals-v1','variables':count,'inputCoordinate':1,'coordinates':coordinate_rows,
      'residuals':[dict(r,terms=terms({(s,tuple(mp[i] for i in m)):v for (s,m),v in pol(r['terms']).items()})) for r in d['residuals']]}
    if symbolic:compact['fixedParameter']=ir['fixedParameter']
    write(f'compact{count}-ir.json',compact)
    table={'format':'integer-quartic-consecutive-coordinates-v2','variables':count,'witnesses':count-1,'degree':4,'inputCoordinate':1,
      'coordinates':coordinate_rows,'terms':terms({(s,tuple(mp[i] for i in m)):v for (s,m),v in q.items()})}
    if symbolic:table['fixedParameter']=ir['fixedParameter']
    stem=f'quartic-{count}-'+('symbolic-coefficients' if symbolic else 'ordinary-coefficients')
    write(stem+'.json',table)
    lines=[f'# Integer quartic in {count} rational variables; x1 is the input.',
      '# Compact physical coordinates run from1 through the total variable count.',
      '# Rows: coefficient | C exponent | variable indices.',
      '# C=3^(2^25) is a fixed integer.' if symbolic else '# Every C exponent is zero; every coefficient is an explicit decimal integer.']
    lines += [f'# x{c["id"]} = source coordinate {c["sourceId"]}: {c["name"]}' for c in coordinate_rows]
    lines += [t['coefficient']+' | '+str(t['sPower'])+' | '+','.join(map(str,t['monomial'])) for t in table['terms']]
    (O/(stem+'.txt')).write_text('\n'.join(lines)+'\n')
    assert sos(compact)==pol(table['terms'])
    assert {i for s,m in pol(table['terms']) for i in m}==set(range(1,count+1))
    stats[str(count)]={'variables':count,'witnesses':count-1,'residuals':len(d['residuals']),'monomials':len(q),'degree':4,'content':1}
    if symbolic:stats[str(count)]['maximumCoefficient']='16*3^(2^26)'
    else:
        maximum=max(abs(v) for v in q.values());delta=maximum-3**2048
        assert maximum.denominator==1 and delta>=0
        stats[str(count)].update(maximumCoefficient=f'3^2048+{delta}',maximumCoefficientBits=maximum.numerator.bit_length())
write('ARTIFACTS.json',{'mathematicalStatus':'Pending separate final composition review','sourceSha256':sha(source),'sourcePolynomialSha256':sha(pp),'inputCoordinate':1,'coordinateRange':'1..totalVariables','constantLift':{'length':16,'firstExponent':1024,'lastExponent':1024*2**15},'statistics':stats,'files':{p.name:sha(p) for p in sorted(O.iterdir()) if p.is_file() and p.name!='ARTIFACTS.json'}})
print(json.dumps(stats,indent=2))
