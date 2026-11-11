"""Producer-free exact guard composition and physical new-R interfaces."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from functools import reduce
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent;S=H/'unweighted372/candidate372-ir.json'
assert hashlib.sha256(S.read_bytes()).hexdigest()=='ff487de4c99d74214eef654dafb1bb2a0a5faca0df3fde5cb636de92297222ce'
old=json.loads(S.read_text(encoding='utf-8'));new=json.loads((H/'candidate369-ir.json').read_text(encoding='utf-8'))
sr={r['id']:r for r in old['residuals']};nr={r['id']:r for r in new['residuals']}
def add(*ps):
 out=defaultdict(Q)
 for p in ps:
  for m,c in p.items():out[m]+=c
 return {m:c for m,c in out.items() if c}
def mul(p,q):
 out=defaultdict(Q)
 for m,c in p.items():
  for n,d in q.items():out[tuple(sorted(m+n))]+=c*d
 return {m:c for m,c in out.items() if c}
def sc(p,a):return {m:c*a for m,c in p.items() if c*a}
def v(i):return {(i,):Q(1)}
def dec(r):return {tuple([-1]*t['sPower']+t['monomial']):Q(t['coefficient']) for t in r['terms']}
drop={382,430,478};gone={334,384,434}
assert new['coordinates']==[c for c in old['coordinates'] if c['id'] not in drop]
assert set(nr)==set(sr)-gone and all(nr[i]==sr[i] for i in nr)
assert {r['id'] for r in old['residuals'] if any(drop.intersection(t['monomial']) for t in r['terms'])}==gone
for k in old:
 if k not in {'coordinates','residuals','status'}:assert old[k]==new[k]
interfaces=[]
for det,E,er,w,z,nr_id,B,br,guard,inv in [(0,350,302,380,383,335,385,337,334,382),(1,398,352,428,431,385,433,387,384,430),(2,446,402,476,479,435,481,437,434,478)]:
 assert dec(sr[guard])==add({():Q(1)},sc(mul(v(w),v(inv)),-1))
 assert dec(nr[nr_id])==add(mul(v(w),v(w)),sc(mul(v(w+1),v(w+1)),-2),sc(mul(v(w),v(z)),-2))
 p=dec(nr[er]);assert p[()]==-1
 R={tuple(i for i in m if i!=E):c for m,c in p.items() if E in m}
 assert p==add(mul(v(E),R),{():Q(-1)})
 assert all(len(m)<=1 for m in R)
 assert dec(nr[br])==add(mul(v(B),add(R,v(E),{():Q(2)})),sc(mul(v(z),v(z)),-1))
 interfaces.append({'detector':det,'Erow':er,'normRow':nr_id,'Brow':br,'deletedInverseRow':guard,'identities':['E*R=1','Norm(W)=2*w0*z','B*(R+E+2)=z^2']})
total={};used=set()
for row in nr.values():
 p=dec(row);assert max(sum(i>=0 for i in m) for m in p)<=2
 used|={i for m in p for i in m if i>=0}
 den=reduce(lcm,(c.denominator for c in p.values()),1);g=reduce(gcd,(abs(int(c*den)) for c in p.values()))
 p=sc(p,Q(den,g));total=add(total,mul(p,p))
assert total==dec(json.loads((H/'polynomial369.json').read_text(encoding='utf-8')))
assert used=={c['id'] for c in new['coordinates']}
assert (len(used),len(nr),len(total))==(369,339,6568)
assert [(m,c) for m,c in total.items() if m.count(-1)==2]==[((-1,-1,57,57,549,549),Q(16))]
assert len({tuple(i for i in m if i>=0) for m in total})==len(total)
assert max(abs(c) for m,c in total.items() if m.count(-1)==1)<=96
assert max(abs(c.numerator).bit_length() for m,c in total.items() if -1 not in m)<2048
assert reduce(gcd,(abs(c.numerator) for c in total.values()))==1
out={'sourceSha256':hashlib.sha256(S.read_bytes()).hexdigest(),'candidateSha256':hashlib.sha256((H/'candidate369-ir.json').read_bytes()).hexdigest(),'variables':369,'residuals':339,'monomials':6568,'degree':4,'maximumCoefficient':'16*3^(2^26)','completePrivateIncidence':True,'allOutsideObjectsIdentical':True,'interfaces':interfaces,'fullSOS':True,'arithmeticStatus':'pending independent composition review'}
(H/'VERIFICATION369.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
