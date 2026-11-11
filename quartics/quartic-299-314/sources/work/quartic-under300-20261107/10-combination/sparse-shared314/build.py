"""An affine Lucas recentering; reduces table size, not variable count."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import copy,hashlib,json
H=Path(__file__).resolve().parent
src=H.parents[2]/'quartic-optimization-20261107/resume-elimination-20261107/shared-scale314/candidate314-ir.json'
assert hashlib.sha256(src.read_bytes()).hexdigest()=='7805ee1ebd5fec7ac20b2b5590afe9b5891c85aff8eee5f58b104a888bb9e6f5'
old=json.loads(src.read_bytes());new=copy.deepcopy(old)
def mul(p,q):
 out=defaultdict(F)
 for m,c in p.items():
  for n,d in q.items():out[tuple(sorted(m+n))]+=c*d
 return {m:c for m,c in out.items() if c}
def enc(p):return [{'sPower':m.count(-1),'monomial':[i for i in m if i>=0],'coefficient':str(c)} for m,c in sorted(p.items()) if c]
changed=[]
for row in new['residuals']:
 if not any({249,250}.intersection(t['monomial']) for t in row['terms']):continue
 p=defaultdict(F)
 for t in row['terms']:
  term={tuple([-1]*t['sPower']):F(t['coefficient'])}
  for i in t['monomial']:term=mul(term,{(i,):F(1),(i-5,):F(2)} if i in [249,250] else {(i,):F(1)})
  for m,c in term.items():p[m]+=c
 row['terms']=enc(p);changed.append(row['id'])
for c in new['coordinates']:
 if c['id'] in [249,250]:c['name']='Lucas.shiftedProduct.'+str(c['id']-249)
new['status']='Sparse Lucas affine presentation of accepted shared314; same variable count; independent finite review pending.'
total=defaultdict(int)
for row in new['residuals']:
 p={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in row['terms']}
 den=lcm(*(v.denominator for v in p.values()));g=gcd(*(int(v*den) for v in p.values()))
 q={m:int(v*den)//g for m,v in p.items()}
 for m,c in q.items():
  for n,d in q.items():total[tuple(sorted(m+n))]+=c*d
def write(name,obj):
 raw=(json.dumps(obj,indent=2)+'\n').encode();p=H/name
 if p.exists():assert p.read_bytes()==raw
 else:p.write_bytes(raw)
 return hashlib.sha256(raw).hexdigest()
ih=write('candidate314-ir.json',new);ph=write('polynomial314.json',{'terms':enc(total)})
cert={'sourceSha256':hashlib.sha256(src.read_bytes()).hexdigest(),'candidateSha256':ih,'polynomialSha256':ph,'changedRows':changed,'variables':len(new['coordinates']),'residuals':len(new['residuals']),'monomials':len({tuple(i for i in m if i>=0) for m,c in total.items() if c}),'coefficientPowerEntries':sum(bool(v) for v in total.values()),'forwardMap':'new249=old249-2*old244; new250=old250-2*old245','reverseMap':'old249=new249+2*new244; old250=new250+2*new245','status':'exact affine proposal; no variable saving'}
write('CERTIFICATE.json',cert);print(json.dumps(cert,indent=2))
