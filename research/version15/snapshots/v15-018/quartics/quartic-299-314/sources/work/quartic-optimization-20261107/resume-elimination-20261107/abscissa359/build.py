"""Three-root parity packing into the retained quaternion anchor. Research only."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import reduce
from math import gcd,lcm
import copy,hashlib,json
H=Path(__file__).resolve().parent
ROOT=H.parents[3]
SOURCE=ROOT/'work/quartic-under300-20261107/01-elimination/s-odd366/candidate366-ir.json'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56'
old=json.loads(SOURCE.read_text());new=copy.deepcopy(old)
drop={66,67,68,74,75,76,78,79,80}
gone={687,688,689,693,694,695,696,697,698}
assert {r['id'] for r in old['residuals'] if any(drop.intersection(t['monomial']) for t in r['terms'])}==gone
assert not set(range(900,905)).intersection(c['id'] for c in old['coordinates'])
assert not set(range(900,905)).intersection(r['id'] for r in old['residuals'])
new['coordinates']=[c for c in old['coordinates'] if c['id'] not in drop]
for i,name in enumerate(('Q','B'),903):
    new['coordinates'].append({'id':i,'name':'packedParity.'+name,'kind':'gate','block':'packed_parity_anchor','protected':False})
new['residuals']=[r for r in new['residuals'] if r['id'] not in gone]
anchor=next(r for r in new['residuals'] if r['id']==504)
anchor['name']='anchor.packedRootParity'
anchor['terms']=[t for t in anchor['terms'] if t['monomial']!=[544,544]]
anchor['terms'].append({'sPower':0,'monomial':[904,904],'coefficient':'-3'})
def row(i,name,terms):
    new['residuals'].append({'id':i,'name':name,'kind':'structural','block':'packed_parity_anchor',
        'terms':[{'sPower':s,'monomial':sorted(m),'coefficient':str(c)} for s,m,c in terms]})
row(903,'packedParity.sum',[(0,[903],1),(0,[83,83],-48),(0,[87,87],-48),(0,[89,89],-432)])
row(904,'packedParity.scaledAnchor',[(0,[904],1),(0,[544],-2),(1,[903,549],-1)])
new['status']='Research359: three root parities packed into quaternion anchor; source projection proof pending independent review.'
total=defaultdict(F)
for r in new['residuals']:
    p={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']}
    den=reduce(lcm,(c.denominator for c in p.values()),1)
    content=reduce(gcd,(abs(int(c*den)) for c in p.values()))
    p={m:c*den/content for m,c in p.items()}
    for m,c in p.items():
        for n,d in p.items():total[tuple(sorted(m+n))]+=c*d
terms=[{'sPower':m.count(-1),'monomial':[i for i in m if i>=0],'coefficient':str(c)} for m,c in sorted(total.items()) if c]
def write(name,value):
    p=H/name;p.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8',newline='\n')
    return hashlib.sha256(p.read_bytes()).hexdigest()
candidate=write('candidate359-ir.json',new)
polynomial=write('polynomial359.json',{'terms':terms})
certificate={'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'candidate_sha256':candidate,
    'polynomial_sha256':polynomial,'removed_coordinates':sorted(drop),'removed_rows':sorted(gone),
    'added_coordinates':[903,904],'added_rows':[903,904],'changed_rows':[504],
    'variables':len(new['coordinates']),'witnesses':len(new['coordinates'])-1,'residuals':len(new['residuals']),
    'coefficient_terms':len(terms),'monomials':len({tuple(t['monomial']) for t in terms}),
    'degree':max(len(t['monomial']) for t in terms),'status':'Independent review required; no release claim.'}
write('CERTIFICATE.json',certificate)
print(json.dumps(certificate,indent=2))
