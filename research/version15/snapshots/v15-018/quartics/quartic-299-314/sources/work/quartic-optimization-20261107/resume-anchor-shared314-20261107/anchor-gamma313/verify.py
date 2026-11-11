"""Check literal delta, Laurent reconstruction, and full SOS; no producer import."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent; W=H.parents[2]
def read(p,pin):
    b=p.read_bytes();assert hashlib.sha256(b).hexdigest()==pin
    return json.loads(b)
old=read(W/'quartic-under300-20261107/10-combination/sparse-shared314/candidate314-ir.json','aa546258e21f0274a5baf1786c4f15d47f4d6b7ffd6d38a925bad823f0de6382')
new=read(H/'candidate313-ir.json','6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a')
table=read(H/'polynomial313.json','d3eaca34d9b5bb3f24593ca601f30f22c430f4b71e47e9f607a050501fc8d63d')
def dec(r):
    p={(t['sPower'],tuple(t['monomial'])):Fraction(t['coefficient']) for t in r['terms']}
    assert len(p)==len(r['terms']) and all(p.values())
    return p
o={r['id']:r for r in old['residuals']};n={r['id']:r for r in new['residuals']}
oc={c['id']:c for c in old['coordinates']};nc={c['id']:c for c in new['coordinates']}
assert len(n)==len(new['residuals']) and len(nc)==len(new['coordinates'])
assert set(o)==set(n) and set(nc)==set(oc)-{1100}
assert {i for i in o if o[i]!=n[i]}=={919,930,941,2000,2005}
assert set(old)==set(new)
for k in old:
    if k not in {'coordinates','residuals','status'}:assert old[k]==new[k]
for i,c in nc.items():
    if i in range(1101,1106):assert {k:v for k,v in c.items() if k!='name'}=={k:v for k,v in oc[i].items() if k!='name'}
    else:assert c==oc[i]
assert dec(n[2000])=={(0,(55,55)):-1,(0,(1101,)):1}
for i in range(2001,2004):
    output=1101+i-2000
    assert dec(n[i])=={(0,(output-1,output-1)):-1,(0,(output,)):1}
assert dec(n[2004])=={(0,()):-1,(0,(1104,1105)):1}
assert dec(n[2005])=={(0,(1103,1106)):1,(0,(1105,1105)):-1}
for r,output in [(2006,1107),(2007,1108)]:assert dec(n[r])=={(0,(output-1,output-1)):-1,(0,(output,)):1}
assert {i for i,r in o.items() if any(1100 in m for s,m in dec(r))}=={2000}
assert {i for i,r in o.items() if i<2000 and any(set(range(1100,1106))&set(m) for s,m in dec(r))}=={919,930,941}
assert {i for i,r in o.items() if any(55 in m for s,m in dec(r))}=={504}
# Interpret all chain values as powers of the nonzero new anchor u=v55.
# u!=0 follows from the four square equations and u16*J=1.
opowers={1100:-1,1101:-2,1102:-4,1103:-8,1104:-16,1105:16,1106:-40,1107:-80,1108:-160}
npowers={1101:2,1102:4,1103:8,1104:16,1105:-16,1106:-40,1107:-80,1108:-160}
def laurent(p,powers):
    out=defaultdict(Fraction)
    for (s,m),c in p.items():
        exponent=m.count(55)+sum(powers.get(i,0) for i in m)
        remaining=tuple(i for i in m if i not in powers and i!=55)
        out[s,exponent,remaining]+=c
    return {k:v for k,v in out.items() if v}
for i in o:
    assert laurent(dec(o[i]),opowers)==laurent(dec(n[i]),npowers),i
for i in range(2000,2008):assert not laurent(dec(n[i]),npowers)
# Full primitive integer SOS, with fixed C kept formal.
full=defaultdict(int);used=set()
for r in n.values():
    p=dec(r);assert all(len(m)<=2 for s,m in p)
    for s,m in p:used.update(m)
    denominator=lcm(*(c.denominator for c in p.values()))
    content=gcd(*(int(c*denominator) for c in p.values()))
    terms=[(s,m,int(c*denominator)//content) for (s,m),c in p.items()]
    for i,(s,m,c) in enumerate(terms):
        for j in range(i,len(terms)):
            t,l,d=terms[j];full[s+t,tuple(sorted(m+l))]+=c*d*(1 if i==j else 2)
full={k:v for k,v in full.items() if v}
assert full==dec(table) and used==set(nc)
assert (len(nc),len(n),len(full))==(313,283,6076)
assert max(len(m) for s,m in full)==4 and gcd(*full.values())==1
group=defaultdict(dict)
for (s,m),c in full.items():group[m][s]=c
assert len(group)==6073 and group[(89,)*4]=={0:64,2:186624}
assert all(max(p)<=2 and abs(p.get(1,0))<=1728 and abs(p.get(0,0))<2**2048 for p in group.values())
assert all(abs(p.get(2,0))<186624 for m,p in group.items() if m!=(89,)*4)
assert any(p=={0:1} for p in group.values())
out={'status':'PASS: algebraic checks only; completeness needs independent arithmetic review','variables':313,'residuals':283,'monomials':6073,'coefficientPowerEntries':6076,'changedRows':[919,930,941,2000,2005],'allUnchangedObjects':True,'nonzeroAnchorForced':True,'allRowsLaurentReconstruction':True,'fullSOS':True,'degree':4,'content':1,'maximumCoefficient':'186624*C^2+64'}
(H/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
