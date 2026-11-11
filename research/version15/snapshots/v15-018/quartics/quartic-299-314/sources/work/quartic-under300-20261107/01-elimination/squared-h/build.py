"""Candidate squared H Kummer presentation; arithmetic review is required."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import reduce
from math import gcd,lcm
import json,hashlib,copy
HOME=Path(__file__).resolve().parent;SOURCE=HOME.parents[1]/'03-depth/candidate392t-ir.json'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='846660e49d0cef6d0f7d562625adcf9ffb72c00542bc5c666fca93dbb363d1ba'
def clean(p):return {m:c for m,c in p.items() if c}
def add(*ps):
 d=defaultdict(F)
 for p in ps:
  for m,c in p.items():d[m]+=c
 return clean(d)
def scale(p,c):return clean({m:v*c for m,v in p.items()})
def mul(p,q):
 d=defaultdict(F)
 for m,c in p.items():
  for n,e in q.items():d[tuple(sorted(m+n))]+=c*e
 return clean(d)
def v(i):return {(i,):F(1)}
def kc(a,b=0):return clean({():F(a)}),clean({():F(b)})
def ka(a,b):return add(a[0],b[0]),add(a[1],b[1])
def ks(a,b):return add(a[0],scale(b[0],-1)),add(a[1],scale(b[1],-1))
def km(a,b):return add(mul(a[0],b[0]),scale(mul(a[1],b[1]),2)),add(mul(a[0],b[1]),mul(a[1],b[0]))
def poly(row):return {tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in row['terms']}
def encode(p):return [{'sPower':m.count(-1),'monomial':[i for i in m if i>=0],'coefficient':str(c)} for m,c in sorted(p.items())]
def primitive(p):
 den=reduce(lcm,[c.denominator for c in p.values()],1);g=reduce(gcd,[abs(int(c*den)) for c in p.values()]);return scale(p,F(den,g))
old=json.loads(SOURCE.read_text());new=copy.deepcopy(old)
removedrows={34,35,112,113,130,131,263,264,661,662}
assert {r['id'] for r in old['residuals'] if any(set(t['monomial'])&{140,141,160,161} for t in r['terms'])}==removedrows
new['residuals']=[r for r in new['residuals'] if r['id'] not in removedrows]
new['coordinates']=[c for c in new['coordinates'] if c['id'] not in {160,161}]
for co in new['coordinates']:
 if co['id'] in {140,141}:co['name']='H.kummer.vSquare.'+str(co['id']-140)
t=(v(142),v(143));vv=(v(700),v(701));W=(v(140),v(141))
U=(v(311),scale(v(312),2));V=(v(178),scale(v(179),2))
D=kc(11,-6);b=kc(F(39,8),F(-9,2));ci=kc(F(456,1681),F(224,1681))
Q=km(ci,ks(ks(kc(1),km(D,W)),km(kc(2),km(b,vv))))
constraints=[('vSquare',ks(W,km(vv,vv))),('squaredProduct',ks(km(U,V),km(W,W))),('squaredSum',ks(km(Q,Q),ka(ka(U,V),km(kc(2),W)))),('ratio',ks(km(t,ka(U,W)),km(Q,vv)))]
for ids,(name,pp) in zip([(34,35),(112,113),(130,131),(661,662)],constraints):
 for i,p in zip(ids,pp):new['residuals'].append({'id':i,'name':f'H.squaredKummer.{name}.{ids.index(i)}','kind':'structural','block':'squared_H_Kummer','terms':encode(p)})
new['residuals'].sort(key=lambda r:r['id'])
new['status']='Research candidate: squared H Kummer with two globally excluded fixed branches. Independent review pending.'
total={}
for row in new['residuals']:
 p=primitive(poly(row));assert max(sum(i>=0 for i in m) for m in p)<=2
 total=add(total,mul(p,p))
def write(n,obj):
 p=HOME/n;p.write_text(json.dumps(obj,indent=2)+'\n');return hashlib.sha256(p.read_bytes()).hexdigest()
irhash=write('candidate390-ir.json',new);phash=write('polynomial390.json',{'terms':encode(total)})
certificate={'sourceSha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'candidateSha256':irhash,'polynomialSha256':phash,'variables':len(new['coordinates']),'witnesses':len(new['coordinates'])-1,'residuals':len(new['residuals']),'monomials':len(total),'maximumCoefficient':'16*3^(2^26)','degree':4,'requiresIndependentArithmeticReview':True,'removedCoordinates':[160,161],'repurposedCoordinates':[140,141]}
write('CERTIFICATE.json',certificate);print(json.dumps(certificate,indent=2))
