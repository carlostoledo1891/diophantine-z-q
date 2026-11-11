"""Producer-free full transport, polynomial map identities and quartic expansion."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent;WORK=H.parents[2]
def read(p,pin):
    assert hashlib.sha256(p.read_bytes()).hexdigest()==pin,p
    return json.loads(p.read_bytes())
old=read(WORK/'quartic-under300-20261107/10-combination/combined320/candidate320-ir.json','d1171bc47ed8ec15aac10ca6708208e9de9c2dfa7a973732ede76269a1bee02f')
new=read(H/'candidate319-ir.json','847d21a2d0a45571f043b82289df0da55f4e814167844bdc39fc134e4f4c2676')
table=read(H/'polynomial319.json','8320b69d290a37017060e34742fb025cbc1c13e40a5b7d750893e9912d3796ef')
def clean(p):return {m:c for m,c in p.items() if c}
def add(*ps):
    out=defaultdict(F)
    for p in ps:
        for m,c in p.items():out[m]+=c
    return clean(out)
def sc(p,k):return clean({m:c*k for m,c in p.items()})
def mul(*ps):
    out={():F(1)}
    for p in ps:
        q=defaultdict(F)
        for m,c in out.items():
            for n,d in p.items():q[tuple(sorted(m+n))]+=c*d
        out=clean(q)
    return out
def v(i):return {(i,):F(1)}
def sq(p):return mul(p,p)
def dec(r):
    out={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']}
    assert len(out)==len(r['terms'])
    return out
o={r['id']:r for r in old['residuals']};n={r['id']:r for r in new['residuals']}
assert set(n)==set(o)-{904}
assert {i for i in n if n[i]!=o[i]}=={903,504}
oc={c['id']:c for c in old['coordinates']};nc={c['id']:c for c in new['coordinates']}
assert set(nc)==set(oc)-{904}
for i in nc:
    if i in {55,56,57,903}:assert {k:x for k,x in nc[i].items() if k!='name'}=={k:x for k,x in oc[i].items() if k!='name'}
    else:assert nc[i]==oc[i]
for k in old:
    if k not in {'coordinates','residuals','status'}:assert old[k]==new[k]
for doc,private,rows in [(old,{55,56,57,903,904},{504,903,904}),(new,{55,56,57,903},{504,903})]:
    assert {r['id'] for r in doc['residuals'] if any(private.intersection(t['monomial']) for t in r['terms'])}==rows
C,g0,g1,tau,U,V,W,Q,B=map(v,[-1,543,544,549,55,56,57,903,904])
root=add(sc(sq(v(83)),48),sc(sq(v(87)),48),sc(sq(v(89)),432))
guard=add(mul(g0,tau),{():F(-1)})
assert dec(o[732])==guard
assert dec(o[903])==add(Q,sc(root,-1))
assert dec(o[904])==add(B,sc(g1,-2),sc(mul(C,Q,tau),-1))
assert dec(n[903])==add(Q,sc(mul(g0,g1),-2),sc(mul(C,root),-1))
assert dec(n[504])==add(sq(U),sc(sq(V),6),sc(sq(W),-2),sc(mul(C,W),-4),sc(sq(Q),-3))
def pullback(p):
    mapping={55:mul(g0,U),56:mul(g0,V),57:mul(g0,W),903:mul(g0,B)}
    return add(*(sc(mul(*(mapping.get(i,v(i)) for i in m)),c) for m,c in p.items()))
# Unconditional polynomial identities; only the existing guard is needed.
assert pullback(dec(n[903]))==add(mul(g0,dec(o[904])),mul(C,dec(o[903])),mul(C,Q,guard))
assert pullback(dec(n[504]))==add(mul(sq(g0),dec(o[504])),sc(mul(C,g0,W,guard),4))
def reverse_pullback(p):
    mapping={55:mul(tau,U),56:mul(tau,V),57:mul(tau,W),903:root,904:mul(tau,Q)}
    return add(*(sc(mul(*(mapping.get(i,v(i)) for i in m)),c) for m,c in p.items()))
assert reverse_pullback(dec(o[903]))=={}
assert reverse_pullback(dec(o[904]))==add(mul(tau,dec(n[903])),sc(mul(g1,guard),2))
assert reverse_pullback(dec(o[504]))==mul(sq(tau),dec(n[504]))
total={};used=set()
for row in n.values():
    p=dec(row);assert max(sum(i>=0 for i in m) for m in p)<=2
    used.update(i for m in p for i in m if i>=0)
    den=lcm(*(c.denominator for c in p.values()));g=gcd(*(int(c*den) for c in p.values()))
    total=add(total,sq({m:F(int(c*den)//g) for m,c in p.items()}))
assert total==dec(table) and used==set(nc)
group=defaultdict(dict)
for m,c in total.items():group[tuple(i for i in m if i>=0)][m.count(-1)]=c
assert (len(nc),len(n),len(total),len(group))==(319,289,5662,5659)
assert max(map(len,group))==4
assert group[(89,89,89,89)]=={2:F(186624),0:F(64)}
assert max(abs(p.get(2,0)) for p in group.values())==186624
assert max(abs(p.get(1,0)) for p in group.values())<=1728
assert all(abs(p.get(0,F(0)).numerator).bit_length()<2048 for p in group.values())
assert all(abs(p.get(2,0))<186624 for m,p in group.items() if m!=(89,89,89,89))
assert any(p=={0:F(1)} for p in group.values())
assert all(max(p)<=2 for p in group.values())
result={'variables':319,'witnesses':318,'residuals':289,'monomials':5659,'coefficient_power_entries':5662,'degree':4,'content':1,'maximum_coefficient':'186624*3^(2^26)+64','unconditional_polynomial_map_identities':True,'all_private_consumers_checked':True,'full_SOS':True,'independent_review':'required'}
(H/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
