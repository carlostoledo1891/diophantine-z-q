"""Contact-polynomial weights and bounded pole input. Pending arithmetic review."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
from functools import reduce
import json,hashlib,copy
H=Path(__file__).resolve().parent;S=H.parents[1]/'01-elimination/squared-h/candidate390-ir.json'
assert hashlib.sha256(S.read_bytes()).hexdigest()=='c986ee02f33aef0cf729bfbd73e590ac9672941be6c8f92dc3f389247daeaced'
old=json.loads(S.read_text(encoding='utf-8'));new=copy.deepcopy(old)
def add(*ps):
 d=defaultdict(F)
 for p in ps:
  for m,c in p.items():d[m]+=c
 return {m:c for m,c in d.items() if c}
def scale(p,a):return {m:c*a for m,c in p.items() if c*a}
def mul(p,q):
 d=defaultdict(F)
 for m,c in p.items():
  for n,a in q.items():d[tuple(sorted(m+n))]+=c*a
 return {m:c for m,c in d.items() if c}
def v(i):return {(i,):F(1)}
def dec(r):return {tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']}
def enc(p):return [{'sPower':m.count(-1),'monomial':[i for i in m if i>=0],'coefficient':str(c)} for m,c in sorted(p.items()) if c]
def sub(p,mapping):
 out={}
 for mon,c in p.items():
  term={():c}
  for i in mon:term=mul(term,mapping.get(i,v(i)))
  out=add(out,term)
 return out
sr={r['id']:r for r in old['residuals']}
drop={395,396,397,443,444,445};gone={349,350,351,399,400,401}
mapping={}; replacements={}; interfaces=[]
for det,E,q,a,b,ed,erow,qrow,arow,brow,edrow,Br,B,z,K in [
 (0,350,352,353,354,384,302,304,520,521,336,337,385,383,F(1952786)),
 (1,398,400,401,402,432,352,354,527,528,386,387,433,431,F(1952786,16)),
 (2,446,448,449,450,480,402,404,534,535,436,437,481,479,F(1952786))]:
 # Assert names before relying on historical IDs.
 assert sr[arow]['name']==f'detector{det}.toric.a.definition'
 assert sr[brow]['name']==f'detector{det}.toric.b.definition'
 R={tuple(i for i in m if i!=E):c/K for m,c in dec(sr[erow]).items() if E in m}
 assert all(len(m)<=1 for m in R)
 mapping[q]=v(E);mapping[a]={():F(1)};mapping[b]=R
 drop|={q,a,b,ed};gone|={qrow,arow,brow,edrow}
 replacements[erow]=add(mul(v(E),R),{():F(-1)})
 replacements[Br]=add(mul(v(B),add(R,v(E),{():F(2)})),scale(mul(v(z),v(z)),-1))
 interfaces.append({'detector':det,'E':E,'R':enc(R),'qDeleted':q,'aDeleted':a,'bDeleted':b,'eDeltaDeleted':ed,'Erow':erow,'Brow':Br})
new['coordinates']=[c for c in new['coordinates'] if c['id'] not in drop]
new['residuals']=[r for r in new['residuals'] if r['id'] not in gone]
changed=[]
for r in new['residuals']:
 p=replacements.get(r['id'],sub(dec(r),mapping))
 if p!=dec(r):changed.append(r['id']);r['terms']=enc(p)
 assert all(sum(i>=0 for i in m)<=2 for m in p)
new['status']='Research372: contact-polynomial weights and bounded pole input. Independent arithmetic review pending.'
total={}
for row in new['residuals']:
 p=dec(row);den=reduce(lcm,(c.denominator for c in p.values()),1);g=reduce(gcd,(abs(int(c*den)) for c in p.values()))
 p=scale(p,F(den,g));total=add(total,mul(p,p))
def write(n,o):
 p=H/n;p.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8');return hashlib.sha256(p.read_bytes()).hexdigest()
ih=write('candidate372-ir.json',new);ph=write('polynomial372.json',{'terms':enc(total)})
cert={'sourceSha256':hashlib.sha256(S.read_bytes()).hexdigest(),'candidateSha256':ih,'polynomialSha256':ph,'removedCoordinates':sorted(drop),'removedRows':sorted(gone),'changedRows':sorted(changed),'interfaces':interfaces,'variables':len(new['coordinates']),'residuals':len(new['residuals']),'monomials':len(total),'arithmeticStatus':'pending'}
write('CERTIFICATE.json',cert);print(json.dumps({k:v for k,v in cert.items() if k!='interfaces'},indent=2))
