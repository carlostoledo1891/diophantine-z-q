"""Exploratory candidate only: completeness requires separate arithmetic review."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from math import gcd,lcm
import json,hashlib,copy
HERE=Path(__file__).resolve().parent
WORK=HERE.parents[2]
SOURCE=WORK/'quartic-under300-20261107/10-combination/sparse-shared314/candidate314-ir.json'
raw=SOURCE.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='aa546258e21f0274a5baf1786c4f15d47f4d6b7ffd6d38a925bad823f0de6382'
old=json.loads(raw); new=copy.deepcopy(old)
new['status']='Exploratory anchor-gamma coupling; arithmetic and structural independent reviews required.'
new['coordinates']=[c for c in new['coordinates'] if c['id']!=1100]
names={1101:'anchor.u2',1102:'anchor.u4',1103:'anchor.u8',1104:'anchor.u16',1105:'shared313.gamma16'}
for c in new['coordinates']:
    if c['id'] in names:c['name']=names[c['id']]
def terms(p):return [{'sPower':s,'monomial':list(m),'coefficient':str(c)} for (s,m),c in sorted(p.items()) if c]
for r in new['residuals']:
    if r['id']==2000:
        r['terms']=terms({(0,(55,55)):-1,(0,(1101,)):1})
    elif r['id']==2005:
        r['terms']=terms({(0,(1103,1106)):1,(0,(1105,1105)):-1})
    elif r['id'] in (919,930,941):
        for t in r['terms']:
            t['monomial']=[1105 if x==1104 else x for x in t['monomial']]
        r['terms'].sort(key=lambda t:(t['sPower'],t['monomial']))
total=defaultdict(int)
for r in new['residuals']:
    p={(t['sPower'],tuple(t['monomial'])):Fraction(t['coefficient']) for t in r['terms']}
    denominator=lcm(*(c.denominator for c in p.values()))
    content=gcd(*(int(c*denominator) for c in p.values()))
    p={k:int(c*denominator)//content for k,c in p.items()}
    for (s,m),a in p.items():
        for (t,n),b in p.items():total[s+t,tuple(sorted(m+n))]+=a*b
total={k:v for k,v in total.items() if v}
def write(name,obj):
    data=(json.dumps(obj,indent=2)+'\n').encode()
    path=HERE/name
    if path.exists():assert path.read_bytes()==data
    else:path.write_bytes(data)
    return hashlib.sha256(data).hexdigest()
ih=write('candidate313-ir.json',new)
ph=write('polynomial313.json',{'terms':terms(total)})
out={'status':'exploratory; independent arithmetic and structural reviews required','sourceSha256':hashlib.sha256(raw).hexdigest(),'candidateSha256':ih,'polynomialSha256':ph,'variables':len(new['coordinates']),'residuals':len(new['residuals']),'coefficientPowerEntries':len(total),'monomials':len({m for s,m in total}),'changedRows':[919,930,941,2000,2005],'deletedCoordinate':1100,'meaning':'gamma=1/v55; requires newly selected private anchor witnesses'}
write('CERTIFICATE.json',out)
print(json.dumps(out,indent=2))
