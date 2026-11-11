"""Transport three approved ordinary constant chains to reciprocal299."""
from pathlib import Path
from collections import defaultdict,Counter
from fractions import Fraction as F
from math import gcd,lcm
import copy,hashlib,json
H=Path(__file__).resolve().parent;WORK=H.parents[2]
component=WORK/'quartic-optimization-20261107/resume-elimination-20261107'
def load(p,h):
 b=p.read_bytes();assert hashlib.sha256(b).hexdigest()==h,p
 return json.loads(b)
source=load(H.parents[2]/'quartic-optimization-20261107/resume-elimination-20261107/reciprocal299-r2/candidate299-ir.json','8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815')
source_table=load(H.parents[2]/'quartic-optimization-20261107/resume-elimination-20261107/reciprocal299-r2/polynomial299.json','e208b503cad67bb53eb42fd78e64b3ebe9e99223692af91dd6c6b5b5b405ca3c')
old=load(component/'exact319/candidate319-ir.json','847d21a2d0a45571f043b82289df0da55f4e814167844bdc39fc134e4f4c2676')
pins={336:'72ef14cca86d1b4a817f93c5c2abf15b3a88a479ad7477f19b96c619daee6c39',335:'0985485cfda55f03b3dbde5949141fbad0846cd33fc0109aec7af024527fd217',334:'8cfc3dbbd900d5393a23572d2d4571b49fa1927a02a1297dcab281017c252951'}
def write(path,obj):
 raw=(json.dumps(obj,indent=2)+'\n').encode()
 if path.exists():assert path.read_bytes()==raw,'Frozen bytes differ: '+str(path)
 else:path.write_bytes(raw)
 return hashlib.sha256(raw).hexdigest()
inherited=next(int(t['coefficient']) for t in source_table['terms'] if not t['sPower'] and not t['monomial'])
write(H/'INHERITED-CONSTANT.json',{'sourcePolynomialSha256':'e208b503cad67bb53eb42fd78e64b3ebe9e99223692af91dd6c6b5b5b405ca3c','K':str(inherited),'bits':inherited.bit_length()})
results=[]
for oldsize,pin in pins.items():
 approved=load(component/f'ordinary-chains/{oldsize}/candidate-ir.json',pin)
 result=copy.deepcopy(source);count=oldsize-320;size=300+count
 directory=H/str(size);directory.mkdir(exist_ok=True)
 oldrows={r['id']:r for r in old['residuals']};srcrows={r['id']:r for r in source['residuals']}
 aprows={r['id']:r for r in approved['residuals']}
 assert srcrows[1903]==dict(oldrows[903],id=1903) and srcrows[504]==oldrows[504]
 assert {r['id'] for r in source['residuals'] if any(t['sPower'] for t in r['terms'])}=={504,1903}
 addedcoords=[c for c in approved['coordinates'] if c['id'] not in {x['id'] for x in old['coordinates']}]
 addedrows=[r for r in approved['residuals'] if r['id'] not in oldrows]
 assert {c['id'] for c in addedcoords}==set(range(1000,1001+count))
 assert {r['id'] for r in addedrows}==set(range(1000,1001+count))
 assert not {c['id'] for c in addedcoords}&{c['id'] for c in source['coordinates']}
 assert not {r['id'] for r in addedrows}&set(srcrows)
 result['coordinates']+=copy.deepcopy(addedcoords)
 result['residuals']=[copy.deepcopy(aprows[504]) if r['id']==504 else dict(copy.deepcopy(aprows[903]),id=1903) if r['id']==1903 else r for r in result['residuals']]+copy.deepcopy(addedrows)
 result['fixedParameter']=copy.deepcopy(approved['fixedParameter'])
 result['status']='Provisional ordinary companion of reciprocal299; complete decimal coefficients; new composition review required.'
 total=defaultdict(int)
 for row in result['residuals']:
  assert all(t['sPower']==0 for t in row['terms'])
  q={tuple(t['monomial']):F(t['coefficient']) for t in row['terms']}
  den=lcm(*(c.denominator for c in q.values()));g=gcd(*(int(c*den) for c in q.values()))
  terms={m:int(c*den)//g for m,c in q.items()}
  for m,c in terms.items():
   for n,e in terms.items():total[tuple(sorted(m+n))]+=c*e
 total={m:c for m,c in total.items() if c}
 ih=write(directory/'candidate-ir.json',result)
 ph=write(directory/'polynomial.json',{'terms':[{'sPower':0,'monomial':list(m),'coefficient':str(c)} for m,c in sorted(total.items())]})
 lines=[]
 for m,c in sorted(total.items()):
  powers=Counter(m);monomial='*'.join('x'+str(i)+(('^'+str(e)) if e!=1 else '') for i,e in sorted(powers.items())) or '1'
  lines.append(str(c)+'\t'+monomial+'\n')
 text=''.join(lines).encode('ascii');tp=directory/'polynomial.txt'
 if tp.exists():assert tp.read_bytes()==text
 else:tp.write_bytes(text)
 maximum=max(abs(c) for c in total.values())
 cert={'sourceSymbolicSha256':'8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815','approvedComponentSha256':pin,'candidateSha256':ih,'polynomialSha256':ph,'textSha256':hashlib.sha256(text).hexdigest(),'variables':len(result['coordinates']),'witnesses':len(result['coordinates'])-1,'residuals':len(result['residuals']),'monomials':len(total),'degree':max(map(len,total)),'content':gcd(*total.values()),'constantGates':count,'rootSumGates':1,'maxCoefficient':str(maximum),'maxCoefficientBits':maximum.bit_length(),'maxCoefficientDigits':len(str(maximum)),'textBytes':len(text),'status':'provisional composition'}
 assert cert['variables']==size
 write(directory/'CERTIFICATE.json',cert);results.append(cert)
write(H/'SUMMARY.json',results)
print(json.dumps([{k:r[k] for k in ['variables','residuals','monomials','constantGates','maxCoefficientBits','maxCoefficientDigits','textBytes']} for r in results],indent=2))
