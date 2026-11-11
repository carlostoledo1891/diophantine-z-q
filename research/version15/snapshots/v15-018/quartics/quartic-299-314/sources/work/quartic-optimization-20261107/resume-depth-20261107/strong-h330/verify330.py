"""Producer-free finite binding and full SOS checks. No arithmetic acceptance."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent
source=H.parents[2]/'quartic-under300-20261107/01-elimination/s-odd366/candidate366-ir.json'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56'
old=json.loads(source.read_bytes());new=json.loads((H/'candidate330-ir.json').read_bytes())
def A(*pp):
 d=defaultdict(Q)
 for p in pp:
  for m,c in p.items():d[m]+=c
 return {m:c for m,c in d.items() if c}
def S(p,a):return {m:c*Q(a) for m,c in p.items() if c*Q(a)}
def M(p,q):
 d=defaultdict(Q)
 for m,c in p.items():
  for n,e in q.items():d[tuple(sorted(m+n))]+=c*e
 return {m:c for m,c in d.items() if c}
def X(i):return {(i,):Q(1)}
def C(a):return {():Q(a)} if a else {}
def K(a,b):return (A(M(a[0],b[0]),S(M(a[1],b[1]),2)),A(M(a[0],b[1]),M(a[1],b[0])))
def KS(a,b):return (M(a[0],b),M(a[1],b))
def KA(*pp):return (A(*(p[0] for p in pp)),A(*(p[1] for p in pp)))
def P(i,s=1):return (X(i),S(X(i+1),s))
def power(p,n):
 out=(C(1),{})
 for _ in range(n):out=K(out,p)
 return out
def R(r):return {tuple(t['monomial']):Q(t['coefficient']) for t in r['terms']}
oldrows={r['id']:r for r in old['residuals']};newrows={r['id']:r for r in new['residuals']}
removed={375,423,471}|{i for start in (608,614,620) for i in range(start,start+4)}|set(range(624,634))|{i for start in (646,666,686) for i in range(start,start+8)}
gone={r['id'] for r in old['residuals'] if r['name'].startswith('hybrid.') or r['id'] in (327,377,427)}
assert set(oldrows)-set(newrows)==gone
assert all(newrows[i]==r for i,r in oldrows.items() if i not in gone)
assert all(r['id'] in gone for r in old['residuals'] if any(removed.intersection(t['monomial']) for t in r['terms']))
oldcoords={c['id']:c for c in old['coordinates']};newcoords={c['id']:c for c in new['coordinates']}
assert set(oldcoords)-set(newcoords)==removed
assert all(newcoords[i]==c for i,c in oldcoords.items() if i not in removed)
assert set(newcoords)-set(oldcoords)==set(range(820,835))-{824,825}

# Actual square consumers, including affine normalized scalar/Lucas outputs.
beta=A(C(2555),S(X(0),204),S(X(248),204))
mid=[P(305,2),(A(X(307),S(X(232),-6),S(beta,6),C(-9)),A(S(X(308),2),S(X(233),-6)))]
midvalues=[(A(X(232),S(X(234),-1)),A(X(233),X(235))),(A(X(232),S(beta,-1)),X(233))]
for k,rowid in enumerate((257,259)):
 sq=K(midvalues[k],midvalues[k])
 assert A(sq[0],S(mid[k][0],-1))==R(oldrows[rowid])
 assert A(sq[1],S(mid[k][1],-1))==S(R(oldrows[rowid+1]),2)
hi=[P(i,2) for i in (311,313,315,317)]+[(A(C(1),S(X(253),-2),X(319)),A(S(X(320),4),S(X(254),-4)))]
for i,lr,rowid in ((1,236,265),(2,240,267),(3,244,269)):
 v=(A(X(lr),S(X(lr+2),-1)),A(X(lr+1),X(lr+3)));sq=K(v,v)
 assert A(sq[0],S(hi[i][0],-1))==R(oldrows[rowid])
 assert A(sq[1],S(hi[i][1],-1))==S(R(oldrows[rowid+1]),2)
sq=power((A(X(253),C(-1)),S(X(254),2)),2)
assert A(sq[0],S(hi[4][0],-1))==R(oldrows[271])
assert A(sq[1],S(hi[4][1],-1))==S(R(oldrows[272]),4)

# Independent exact symbolic derivation of every cached alternate eighth power.
D=(C(11),C(-6));d4=power(D,4);da=d4[0][()];db=d4[1][()];norm=da*da-2*db*db
inv=(C(da/norm),C(-db/norm))
alts=[]
for x,w2,w4 in ((178,180,182),(196,198,200),(208,210,212),(220,222,224)):
 a,b=X(x),X(x+1)
 q0=A(M(a,a),S(M(a,b),Q(-1056,193)),S(M(b,b),8))
 q1=A(M(a,a),S(M(a,b),Q(-193,33)),S(M(b,b),8))
 w2expected=(S(q0,193),S(q1,-132))
 assert w2expected==power(K(D,(a,S(b,2))),2)
 stored_w4=(A(S(M(q0,q0),37249),S(M(q1,q1),34848)),S(M(q0,q1),-50952))
 assert stored_w4==power(K(D,(a,S(b,2))),4)
 actual=K(inv,P(w4));alts.append((actual[0],S(actual[1],-1)))
 for comp in (0,1):
  row=next(r for r in old['residuals'] if r['name']==f'logV{(0,2,3,4)[len(alts)-1]}.wPower4.{comp}.definition')
  expected=A(X(w4+comp),S((A(S(M(X(w2),X(w2)),37249),S(M(X(w2+1),X(w2+1)),34848)),S(M(X(w2),X(w2+1)),-50952))[comp],-1))
  assert R(row)==expected
v1four=(A(S(X(192),Q(37249,2401)),S(X(193),Q(-34848,2401))),S(A(X(193),S(X(192),-1)),Q(25476,2401)))

expected=[]
def pair_rows(out,value):
 expected.extend(A(X(out+j),S(value[j],-1)) for j in (0,1))
for j in range(2):pair_rows(820+2*j,power(hi[j+2],2))
for j in range(3):pair_rows(826+2*j,power(P(255+2*j,2),2))
for n,b,q,qq,mm,e2,ee,ww in ((0,634,360,374,359,361,356,380),(1,654,408,422,407,409,404,428),(2,674,456,470,455,457,452,476)):
 expected.append(A(X(832+n),S(M(X(e2),X(e2)),-1)))
 for j in range(3):pair_rows(b+2*j,KA((C(1),{}),KS(hi[4] if j==0 else hi[1] if j==1 else mid[0],X(q if j<2 else mm)),KS(P(820+2*j) if j<2 else hi[0],X(qq)),KS(P(826+2*j),X(832+n)),KS(alts[j],X(ee))))
 pair_rows(b+6,KA((C(1),{}),KS(mid[1],X(mm)),KS(P(261,2),X(e2)),KS(v1four,X(832+n)),KS(alts[3],X(ee))))
 pair_rows(b+8,K(P(b),P(b+2)));pair_rows(b+10,K(P(b+4),P(b+6)));pair_rows(ww,K(P(b+8),P(b+10)))
newids=sorted(set(newrows)-set(oldrows));assert len(expected)==len(newids)==55
assert all(R(newrows[i])==p for i,p in zip(newids,expected))
assert len(newcoords)==330 and len(newrows)==300
assert {i for r in newrows.values() for t in r['terms'] for i in t['monomial']}==set(newcoords)
assert all(len(t['monomial'])<=2 for r in newrows.values() for t in r['terms'])

# Check both residue partitions for each odd alpha, representing every odd integer.
for a in range(1,16,2):
 for types in (((2,79),(4,158),(8,4),(16,8)),((2,19),(4,158),(8,4),(16,8)),((2,19),(4,2),(8,4),(16,8))):
  sets=[{0}]+[{(k-j*a)%16 for k in range(0,16,d)} for d,j in types]
  assert sum(map(len,sets))==len(set.union(*sets))

# Full primitive SOS, upper-triangular accumulation independent of producer.
total=defaultdict(int)
for row in newrows.values():
 p={tuple([-1]*t['sPower']+t['monomial']):Q(t['coefficient']) for t in row['terms']}
 den=1
 for c in p.values():den=lcm(den,c.denominator)
 div=0
 for c in p.values():div=gcd(div,abs(int(c*den)))
 terms=sorted((m,int(c*den)//div) for m,c in p.items())
 for i,(m,c) in enumerate(terms):
  for j in range(i,len(terms)):
   n,d=terms[j];total[tuple(sorted(m+n))]+=c*d*(1 if i==j else 2)
actual={tuple([-1]*t['sPower']+t['monomial']):int(t['coefficient']) for t in json.loads((H/'polynomial330.json').read_bytes())['terms']}
assert {m:c for m,c in total.items() if c}==actual
content=0
for c in actual.values():content=gcd(content,abs(c))
assert content==1 and max(len([i for i in m if i>=0]) for m in actual)==4
result={'sourceSha256':hashlib.sha256(source.read_bytes()).hexdigest(),'candidateSha256':hashlib.sha256((H/'candidate330-ir.json').read_bytes()).hexdigest(),'polynomialSha256':hashlib.sha256((H/'polynomial330.json').read_bytes()).hexdigest(),'variables':330,'witnesses':329,'rows':300,'monomials':len(actual),'content':content,'maxConstantCoefficientBits':max(abs(c).bit_length() for m,c in actual.items() if -1 not in m),'allFiniteChecksPassed':True,'arithmeticAcceptance':False}
(H/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
