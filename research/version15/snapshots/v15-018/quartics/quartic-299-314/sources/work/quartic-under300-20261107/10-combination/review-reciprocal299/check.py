"""Independent S-interface binding and complete polynomial reconstruction."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import json,hashlib
from algebra import add,scale,mul,v,constant,ka,ks,km,pair,kc,dec
H=Path(__file__).resolve().parent;W=H.parents[2];O=W/'quartic-optimization-20261107'
def load(p,h):
    b=p.read_bytes();assert hashlib.sha256(b).hexdigest()==h,p
    return json.loads(b)
sourcePin='ecc9bb4e2e4b5a5a2109524a40c4140317f036d9811b580b04711e4a89cb25e6'
pins=json.loads((H/'TARGET.json').read_bytes())
old=load(O/'resume-elimination-20261107/reciprocal301/candidate301-ir.json',sourcePin)
new=load(O/'resume-elimination-20261107/reciprocal299-r2/candidate299-ir.json',pins['candidate'])
table=load(O/'resume-elimination-20261107/reciprocal299-r2/polynomial299.json',pins['polynomial'])
rr={r['id']:r for r in old['residuals']};nn={r['id']:r for r in new['residuals']}
cc={c['id']:c for c in old['coordinates']};nc={c['id']:c for c in new['coordinates']}
assert len(rr)==len(old['residuals']) and len(nn)==len(new['residuals'])
assert len(cc)==len(old['coordinates']) and len(nc)==len(new['coordinates'])
def eq(rows,i,p):assert dec(rows[i])==p[0] and dec(rows[i+1])==p[1],i
D=(constant(11),constant(-6));one=kc(1)
a,b,c=pair(5),pair(7),pair(84,im=2)
V,I,Q,J,K=map(pair,[25,27,118,120,122])
Y,B,L,z=pair(257,im=2),pair(196,im=2),pair(236),pair(168)
N=(add(constant(F(-87,41)),scale(v(142),-1),scale(v(143),F(7,2)),scale(v(700),F(-80,41)),scale(v(701),F(212,41))),
   add(constant(F(129,164)),scale(v(142),F(7,4)),scale(v(143),-1),scale(v(700),F(106,41)),scale(v(701),F(-80,41))))
# Bind every old changed S equation, rather than relying on its name.
eq(rr,708,ka(km(a,I),ks(km(b,V),-1),ks(km(D,km(V,J)),-1),ks(km(c,Q),-1)))
eq(rr,710,ka(km(a,K),km(b,Q),km(c,V),km(D,km(Q,J))))
eq(rr,712,ka(km(V,Q),ks(km(c,J),-1)))
eq(rr,714,ka(km(V,V),km(Q,Q),ks(km(b,J),2),km(D,km(J,J)),kc(-1)))
eq(rr,209,ka(km(I,I),ks(c,-1),km(D,km(c,Y))))
eq(rr,148,ka(km(K,K),ks(c,-1),km(D,km(c,B))))
eq(rr,188,ka(km(I,L),ks(km(V,N),-1)))
eq(rr,120,ka(km(K,z),Q))
# Same physical cache slots and ratios, new reciprocal meanings for private pairs.
f,h,A,s=V,I,Q,J;d=ka(f,ks(A,-1));k=ka(km(s,d),ks(h,-1))
expected={
    708:ka(km(h,h),ks(f,-1),km(D,km(f,Y))),
    710:ka(ks(km(s,h),2),ks(km(c,d),-1),kc(-1),km(D,ka(ks(Y,2),km(f,A)))),
    712:ka(km(s,s),ks(c,-1),km(D,ka(f,A))),
    714:ka(km(a,b),ks(km(D,h),-1),km(s,ka(km(D,f),c))),
    209:ka(km(f,f),ks(Y,-1)),148:ka(km(A,A),ks(B,-1)),
    188:ka(km(h,L),km(f,N)),120:ka(km(ka(one,ks(km(D,B),-1)),z),ks(k,-1)),
    2220:ka(km(ka(one,ks(km(D,Y),-1)),L),km(h,N))}
covered=set()
for i,p in expected.items():eq(nn,i,p);covered.update([i,i+1])
added={2220,2221};deleted={122,123};repurposed={25,26,27,28,118,119,120,121}
assert set(nn)==set(rr)|added and set(nc)==set(cc)-deleted
assert {i for i in rr if nn[i]!=rr[i]}==covered-added
for i,c0 in nc.items():
    if i in repurposed:assert {k:v for k,v in c0.items() if k!='name'}=={k:v for k,v in cc[i].items() if k!='name'}
    else:assert c0==cc[i]
oldUses={i:sorted(rid for rid,r in rr.items() if any(i in m for m in dec(r))) for i in repurposed|deleted}
newUses={i:sorted(rid for rid,r in nn.items() if any(i in m for m in dec(r))) for i in repurposed}
assert all(set(u)<=covered for u in oldUses.values()) and all(set(u)<=covered for u in newUses.values())
assert all(not set(m)&deleted for r in nn.values() for m in dec(r))
for key,value in old.items():
    if key not in {'coordinates','residuals','status'}:assert new[key]==value
# Both S root curves and every scalar/anchor row retain literal source objects.
for rid,p in [(8,ka(km(a,a),ks(c,-1))),(10,ka(km(b,b),ks(km(c,c),-1),D))]:
    for j,want in enumerate(p):
        got=dec(nn[rid+j]);assert nn[rid+j]==rr[rid+j] and set(got)==set(want)
        assert len({got[m]/want[m] for m in want})==1
scalarRows=[i for i in rr if any(t in str(rr[i].get('block','')).lower() for t in ['scalar','anchor'])]
assert all(nn[i]==rr[i] for i in scalarRows)
assert nn[504]==rr[504] and nn[1903]==rr[1903]
# The old S-root sign restoration remains an exact action on the new system.
signCoordinates={5,6,7,8,543,544,549};negativeRows=[]
for rid,row in nn.items():
    p=dec(row);transformed={m:q*(-1)**sum(i in signCoordinates for i in m) for m,q in p.items()}
    if transformed==scale(p,-1):negativeRows.append(rid)
    else:assert transformed==p,rid
assert sorted(negativeRows)==[474,475,513,514]
# Full exact primitive-integer SOS.
total=defaultdict(F);active=set()
for row in nn.values():
    p=dec(row);active.update(i for m in p for i in m if i!=-1)
    assert all(sum(i!=-1 for i in m)<=2 for m in p)
    den=lcm(*(q.denominator for q in p.values()));g=gcd(*(int(q*den) for q in p.values()))
    p=scale(p,F(den,g))
    for m,q in mul(p,p).items():total[m]+=q
total={m:q for m,q in total.items() if q}
assert total==dec(table) and active==set(nc)
# Reproduce the rejected slot error as an independent negative fixture.
wrongActive=set()
for rid,row in nn.items():
    for m in dec(row):
        wrongActive.update(({196:202,197:203}.get(i,i) if rid in covered else i) for i in m if i!=-1)
assert wrongActive-set(nc)=={202,203}
assert (len(nc),len(nn),len(total))==(299,279,pins['terms'])
assert max(sum(i!=-1 for i in m) for m in total)==4 and gcd(*(int(q) for q in total.values()))==1
group=defaultdict(dict)
for m,q in total.items():group[tuple(i for i in m if i!=-1)][m.count(-1)]=q
def sign(p):
    p={a:q for a,q in p.items() if q}
    if not p:return 0
    degree=max(p);tail=sum(abs(q) for a,q in p.items() if a<degree)
    assert tail<2**2048 and abs(p[degree])>=1
    return 1 if p[degree]>0 else -1
for p in group.values():
    for eps in [-1,1]:assert sign({a:F(186624 if a==2 else 0)+eps*p.get(a,0) for a in set(p)|{2}})>=0
assert group[(89,89,89,89)]=={2:F(186624)}
out={'status':'PASS','candidate':pins['candidate'],'polynomial':pins['polynomial'],'variables':299,'witnesses':298,
     'residuals':279,'terms':len(total),'monomials':len(group),'degree':4,'content':1,'maximum':'186624*C^2',
     'changedRows':sorted(covered-added),'addedRows':sorted(added),'deletedCoordinates':sorted(deleted),
     'oldPrivateIncidence':oldUses,'newPrivateIncidence':newUses,'scalarRowsUnchanged':scalarRows,
     'alternateCache':[196,197],'primaryCache':[257,258],'allOutsideObjectsUnchanged':True,
     'signAction':{'coordinates':sorted(signCoordinates),'negativeRows':negativeRows,'allOtherRowsFixed':True},
     'rejectedSlotNegativeFixture':{'undeclaredCoordinates':[202,203],'rejected':True}}
(H/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
