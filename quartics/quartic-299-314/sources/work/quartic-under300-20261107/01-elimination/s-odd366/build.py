"""Delete the scalar-root private odd chart; new parity proof requires review."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import reduce
from math import gcd,lcm
import json,hashlib,copy
H=Path(__file__).resolve().parent
S=H.parents[1]/'10-combination/candidate369-ir.json'
assert hashlib.sha256(S.read_bytes()).hexdigest()=='b359a64365d05c86ad009b2b93664bd491bc1830e0077383030a0b48556e7095'
old=json.loads(S.read_text());new=copy.deepcopy(old)
drop={70,71,72};gone={690,691,692}
assert {r['id'] for r in old['residuals'] if any(drop.intersection(x['monomial']) for x in r['terms'])}==gone
new['coordinates']=[c for c in old['coordinates'] if c['id'] not in drop]
new['residuals']=[r for r in old['residuals'] if r['id'] not in gone]
new['status']='Research366: scalar anchor forces S odd; chart restoration permits an exact global sign symmetry. Independent review pending.'
total=defaultdict(F)
for row in new['residuals']:
 p={tuple([-1]*x['sPower']+x['monomial']):F(x['coefficient']) for x in row['terms']}
 den=reduce(lcm,(x.denominator for x in p.values()),1);g=reduce(gcd,(abs(int(x*den)) for x in p.values()))
 p={m:x*den/g for m,x in p.items()}
 for m,c in p.items():
  for n,d in p.items():total[tuple(sorted(m+n))]+=c*d
terms=[{'sPower':m.count(-1),'monomial':[i for i in m if i>=0],'coefficient':str(c)} for m,c in sorted(total.items()) if c]
def write(n,obj):
 p=H/n;p.write_text(json.dumps(obj,indent=2)+'\n');return hashlib.sha256(p.read_bytes()).hexdigest()
ih=write('candidate366-ir.json',new);ph=write('polynomial366.json',{'terms':terms})
cert={'sourceSha256':hashlib.sha256(S.read_bytes()).hexdigest(),'candidateSha256':ih,'polynomialSha256':ph,
 'removedCoordinates':sorted(drop),'removedRows':sorted(gone),'variables':len(new['coordinates']),
 'witnesses':len(new['coordinates'])-1,'residuals':len(new['residuals']),'monomials':len(terms),'degree':4,
 'maximumCoefficient':'16*3^(2^26)','status':'new parity/sign-restoration proof pending independent acceptance'}
write('CERTIFICATE.json',cert);print(json.dumps(cert,indent=2))
