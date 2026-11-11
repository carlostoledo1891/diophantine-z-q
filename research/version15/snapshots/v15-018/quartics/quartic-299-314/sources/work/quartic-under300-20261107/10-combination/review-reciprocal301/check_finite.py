"""Reviewer-owned full301 reconstruction, with no author imports."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent;W=H.parents[2];O=W/'quartic-optimization-20261107'
def load(p,h):
    b=p.read_bytes();assert hashlib.sha256(b).hexdigest()==h,p
    return json.loads(b)
old=load(O/'reciprocal307-20261107/candidate307-ir.json','0b94aaf7669b3fe89cdf48f4718750991cfea4dd289695543f29b0cd533f29a1')
new=load(O/'resume-elimination-20261107/reciprocal301/candidate301-ir.json','ecc9bb4e2e4b5a5a2109524a40c4140317f036d9811b580b04711e4a89cb25e6')
table=load(O/'resume-elimination-20261107/reciprocal301/polynomial301.json','738893f68014f1b92852585fcda5e32946cdcdb702fe37f6f7c584d4f97be76f')
def add(*ps):
    q=defaultdict(F)
    for p in ps:
        for m,c in p.items():q[m]+=c
    return {m:c for m,c in q.items() if c}
def scale(p,k):return {m:c*k for m,c in p.items() if c*k}
def mul(a,b):
    q=defaultdict(F)
    for m,c in a.items():
        for n,d in b.items():q[tuple(sorted(m+n))]+=c*d
    return {m:c for m,c in q.items() if c}
def v(i):return {(i,):F(1)}
def constant(x):return {():F(x)} if x else {}
def ka(*xs):return add(*(x[0] for x in xs)),add(*(x[1] for x in xs))
def ks(x,k):return scale(x[0],k),scale(x[1],k)
def km(a,b):return add(mul(a[0],b[0]),scale(mul(a[1],b[1]),2)),add(mul(a[0],b[1]),mul(a[1],b[0]))
def pair(i,re=1,im=1):return scale(v(i),re),scale(v(i+1),im)
def kc(x):return constant(x),{}
def dec(r):
    p={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in r['terms']}
    assert len(p)==len(r['terms']) and all(p.values());return p
rr={r['id']:r for r in old['residuals']};nn={r['id']:r for r in new['residuals']}
cc={c['id']:c for c in old['coordinates']};nc={c['id']:c for c in new['coordinates']}
assert len(rr)==len(old['residuals']) and len(nn)==len(new['residuals'])
assert len(cc)==len(old['coordinates']) and len(nc)==len(new['coordinates'])
def eq(rows,i,p):assert dec(rows[i])==p[0] and dec(rows[i+1])==p[1],i
D=(constant(11),constant(-6));removed=set();changed={};deleted=set();incidence={}
for ci,cr,fi,Fi,si,ki,Yi,Bi,zi,chart,raw,reg,pc,ys,bs in [
    (82,1,21,110,112,114,255,190,164,700,116,2202,2,207,142),
    (86,2,29,126,128,130,259,208,172,716,124,2206,18,211,160),
    (88,1,33,134,136,138,261,220,176,724,128,2210,26,213,172)]:
    f,h,A,s,k,Y,B,z=pair(fi),pair(fi+2),pair(Fi),pair(si),pair(ki),pair(Yi,im=2),pair(Bi,im=2),pair(zi)
    c=pair(ci,re=cr,im=2);delta=ka(f,ks(A,-1))
    eq(rr,ys,ka(km(f,f),ks(Y,-1)));eq(rr,bs,ka(km(A,A),ks(B,-1)))
    eq(rr,pc,ka(km(h,h),ks(f,-1),km(D,km(f,Y))))
    eq(rr,chart,ka(km(k,k),ks(A,-1),km(D,km(A,B))))
    eq(rr,chart+2,ka(km(s,delta),ks(h,-1),ks(k,-1)))
    eq(rr,chart+4,ka(km(s,ka(h,ks(k,-1))),kc(-1),km(D,ka(Y,km(f,A),B))))
    eq(rr,chart+6,ka(km(s,s),ks(c,-1),km(D,ka(f,A))))
    eq(rr,raw,ka(km(k,z),ks(A,-1)))
    eq(rr,reg,ka(km(ka(kc(1),ks(km(D,B),-1)),z),ks(k,-1)))
    q=ka(ks(km(s,h),2),ks(km(c,delta),-1),kc(-1),km(D,ka(ks(Y,2),km(f,A))))
    rg=ka(km(ka(kc(1),ks(km(D,B),-1)),z),ks(km(s,delta),-1),h)
    for rid,p in [(chart+4,q),(reg,rg)]:
        eq(nn,rid,p);changed[rid]=p[0];changed[rid+1]=p[1]
    removed.update([chart,chart+1,chart+2,chart+3,raw,raw+1]);deleted.update([ki,ki+1])
    for id in [ki,ki+1]:
        incidence[id]=sorted(r['id'] for r in rr.values() if any(id in t['monomial'] for t in r['terms']))
assert set(nn)==set(rr)-removed and set(nc)==set(cc)-deleted
assert all(nc[i]==c for i,c in cc.items() if i not in deleted)
assert {i for i in nn if nn[i]!=rr[i]}==set(changed)
assert all(nn[i]==r for i,r in rr.items() if i not in removed|set(changed))
assert all(set(rows)<=removed|set(changed) for rows in incidence.values())
assert all(not set(m)&deleted for r in nn.values() for m in dec(r))
for key,value in old.items():
    if key not in {'coordinates','residuals','status'}:assert new[key]==value
total=defaultdict(F);active=set()
for r in nn.values():
    p=dec(r);active.update(i for m in p for i in m if i!=-1)
    assert all(sum(i!=-1 for i in m)<=2 for m in p)
    den=lcm(*(c.denominator for c in p.values()));g=gcd(*(int(c*den) for c in p.values()))
    p=scale(p,F(den,g))
    for m,c in mul(p,p).items():total[m]+=c
total={m:c for m,c in total.items() if c}
assert total==dec(table) and active==set(nc)
assert (len(nc),len(nn),len(total))==(301,277,6423)
assert max(sum(i!=-1 for i in m) for m in total)==4 and gcd(*(int(c) for c in total.values()))==1
# Compare every coefficient polynomial to M=186624*C^2 using C>2^2048.
group=defaultdict(dict)
for m,c in total.items():group[tuple(i for i in m if i!=-1)][m.count(-1)]=c
def sign(p):
    p={a:c for a,c in p.items() if c}
    if not p:return 0
    d=max(p);tail=sum(abs(c) for a,c in p.items() if a<d)
    assert tail<2**2048 and abs(p[d])>=1
    return 1 if p[d]>0 else -1
for p in group.values():
    for e in [-1,1]:assert sign({a:F(186624 if a==2 else 0)+e*p.get(a,0) for a in set(p)|{2}})>=0
assert group[(89,89,89,89)]=={2:F(186624)}
out={'status':'PASS','variables':301,'witnesses':300,'residuals':277,'monomials':6423,'degree':4,'content':1,
     'maximum':'186624*C^2, C=3^(2^25)','deletedCoordinates':sorted(deleted),'removedRows':sorted(removed),
     'changedRows':sorted(changed),'oldPrivateIncidence':incidence,'allOtherObjectsUnchanged':True,
     'sourceSha256':'0b94aaf7669b3fe89cdf48f4718750991cfea4dd289695543f29b0cd533f29a1',
     'candidateSha256':'ecc9bb4e2e4b5a5a2109524a40c4140317f036d9811b580b04711e4a89cb25e6'}
(H/'FINITE-CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
