"""Delete three trace inverse guards. New arithmetic proof requires review."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict, Counter
from math import gcd,lcm
from functools import reduce
import json,hashlib,copy
HERE=Path(__file__).resolve().parent
SOURCE=HERE/'unweighted372/candidate372-ir.json'
PIN='ff487de4c99d74214eef654dafb1bb2a0a5faca0df3fde5cb636de92297222ce'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==PIN
old=json.loads(SOURCE.read_text(encoding='utf-8')); new=copy.deepcopy(old)
drop={382,430,478}; rows={334,384,434}
assert {r['id'] for r in old['residuals'] if any(drop.intersection(t['monomial']) for t in r['terms'])}==rows
new['coordinates']=[c for c in new['coordinates'] if c['id'] not in drop]
new['residuals']=[r for r in new['residuals'] if r['id'] not in rows]
new['status']='Research candidate369. Conditional trace interpretation; independent arithmetic review pending.'
total=defaultdict(F)
for r in new['residuals']:
 p={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']}
 den=reduce(lcm,(c.denominator for c in p.values()),1)
 g=reduce(gcd,(abs(int(c*den)) for c in p.values()))
 p={m:c*den/g for m,c in p.items()}
 for m,c in p.items():
  for n,d in p.items():total[tuple(sorted(m+n))]+=c*d
terms=[{'sPower':m.count(-1),'monomial':[i for i in m if i>=0],'coefficient':str(c)} for m,c in sorted(total.items()) if c]
def write(name,obj):
 path=HERE/name; path.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
 return hashlib.sha256(path.read_bytes()).hexdigest()
ih=write('candidate369-ir.json',new); ph=write('polynomial369.json',{'terms':terms})
cert={'sourceSha256':PIN,'candidateSha256':ih,'polynomialSha256':ph,'removedCoordinates':sorted(drop),'removedRows':sorted(rows),'variables':len(new['coordinates']),'residuals':len(new['residuals']),'monomials':len(terms),'degree':4,'maximumCoefficient':'16*3^(2^26)','arithmeticStatus':'pending independent review; not full old-witness equivalence'}
write('CERTIFICATE369.json',cert)
print(json.dumps(cert,indent=2))
