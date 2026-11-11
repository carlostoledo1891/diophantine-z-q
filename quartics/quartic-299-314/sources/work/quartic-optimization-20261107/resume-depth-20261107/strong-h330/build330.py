"""Delete the H4 fourth-power pair using the even valuation of f(H)."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import reduce
from math import gcd,lcm
import copy,hashlib,json
H=Path(__file__).resolve().parent;source=H.parent/'four-groups/candidate332-ir.json'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='27dfc0e11bcdaceb2c71b6562bb3e9a0f3dfd5147338a4a4ffd14d1f53ba4c63'
old=json.loads(source.read_bytes());new=copy.deepcopy(old)
gone={r['id'] for r in old['residuals'] if r['name'].startswith('four.high4.fourth.')}
assert len(gone)==2
new['residuals']=[r for r in new['residuals'] if r['id'] not in gone]
new['coordinates']=[c for c in new['coordinates'] if c['id'] not in (824,825)]
changed=[]
for det,q,q2 in ((0,360,374),(1,408,422),(2,456,470)):
 for group in (0,2):
  for comp in (0,1):
   row=next(r for r in new['residuals'] if r['name']==f'four.det{det}.group{group}.{comp}')
   p=defaultdict(F,{tuple(t['monomial']):F(t['coefficient']) for t in row['terms']})
   def term(c,*ids):p[tuple(sorted(ids))]+=F(c)
   if group==0:
    if comp==0:
     term(1,311,q);term(-1,q);term(2,253,q);term(-1,319,q)
    else:
     term(2,312,q);term(-4,320,q);term(4,254,q)
   else:
    term(1,824+comp,q2);term(-1 if comp==0 else -2,311+comp,q2)
   row['terms']=[{'sPower':0,'monomial':list(m),'coefficient':str(c)} for m,c in sorted(p.items()) if c];changed.append(row['id'])
new['status']='Research330: four-group detector with stronger H completeness depth; independent review pending.'
assert len(new['coordinates'])==330 and len(new['residuals'])==300
total=defaultdict(F)
for r in new['residuals']:
 p={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']}
 den=reduce(lcm,(c.denominator for c in p.values()),1);div=reduce(gcd,(abs(int(c*den)) for c in p.values()))
 p={m:c*den/div for m,c in p.items()}
 for m,c in p.items():
  for n,d in p.items():total[tuple(sorted(m+n))]+=c*d
poly={'terms':[{'sPower':m.count(-1),'monomial':[i for i in m if i>=0],'coefficient':str(c)} for m,c in sorted(total.items()) if c]}
def write(name,value):
 p=H/name;p.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8');return hashlib.sha256(p.read_bytes()).hexdigest()
ch=write('candidate330-ir.json',new);ph=write('polynomial330.json',poly)
cert={'sourceSha256':hashlib.sha256(source.read_bytes()).hexdigest(),'candidateSha256':ch,'polynomialSha256':ph,'removedCoordinates':[824,825],'removedRows':sorted(gone),'changedRows':sorted(changed),'variables':330,'witnesses':329,'residuals':300,'monomials':len(poly['terms']),'arithmeticAcceptance':False}
write('CERTIFICATE.json',cert);print(json.dumps(cert,indent=2))
