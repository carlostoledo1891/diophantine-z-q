from pathlib import Path
import json,hashlib,math
from fractions import Fraction as F
O=Path(__file__).resolve().parent
exec((O.parent/'parity-sparse-001/build.py').read_text().split('s=json.loads(P.read_bytes())')[0])
P=O.parent/'reference235-011/candidate235-ir.json'
assert hashlib.sha256(P.read_bytes()).hexdigest()=='53b3296814c84d5a7f695829957cfbcd8829018b5799f58339f8518f2e35e395'
s=json.loads(P.read_bytes())
def con(v):return {(0,()):F(v)} if v else {}
def var(i):return {(0,(i,)):F(1)}
def fp(x,y):return plus(mul(x[0],y[0]),mul(x[1],y[1]),2),plus(mul(x[0],y[1]),mul(x[1],y[0]))
def fa(*xs):
 out=({}, {})
 for x in xs:out=plus(out[0],x[0]),plus(out[1],x[1])
 return out
def fc(a,b=0):return con(a),con(b)
f=var(17),var(18);g=var(137),var(138);B=var(84),{(0,(85,)):F(2)};w=var(31),{(0,(32,)):F(2)}
a,c,d=fc(57,-28),fc(88,-48),fc(39,-36)
A2=fa(fp(a,a),fp(fc(2),fp(fp(a,c),f)),fp(fp(c,c),B))
N=fa(fc(8),fp(fc(-1),fp(a,f)),fp(fc(-2),fp(d,g)))
eq=fa(fp(A2,w),fp(fc(-1),fp(N,N)))
cm={i:i-2*(i>22) for i in range(1,236) if i not in [21,22]};rows=[];factors=[]
for component,p in enumerate(eq):
 l=math.lcm(*(v.denominator for v in p.values()));gcd=math.gcd(*(int(v*l) for v in p.values()));factor=F(l,gcd);factors.append(str(factor))
 rows.append({'id':component+1,'name':f'V0.reference.square_eliminated.{component}','terms':ser({(a,tuple(cm[i] for i in m)):v*factor for (a,m),v in p.items()})})
rm={}
for r in s['residuals']:
 if r['id'] in [5,6,7,8]:continue
 assert all(not(set(t['monomial'])&{21,22}) for t in r['terms'])
 nr=dict(r,id=len(rows)+1,terms=[dict(t,monomial=[cm[i] for i in t['monomial']]) for t in r['terms']]);rows.append(nr);rm[r['id']]=nr['id']
coords=[dict(x,id=cm[x['id']]) for x in s['coordinates'] if x['id'] not in [21,22]]
out=dict(s,variables=233,coordinates=coords,residuals=rows,source={'parent_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'construction':'Reference reciprocal eliminated using stored square; author finite construction'})
poly={}
for r in rows:poly=plus(poly,mul(read(r['terms']),read(r['terms'])))
assert len(rows)==207 and set(i for a,m in poly for i in m)==set(range(1,234))
assert max(len(m) for a,m in poly)==4 and all(v.denominator==1 for v in poly.values())
stats={'variables':233,'rows':207,'coordinate_monomials':len({m for a,m in poly}),'parameter_terms':len(poly),'degree':4,'content':math.gcd(*(int(v) for v in poly.values()))}
for name,obj in [('candidate233-ir.json',out),('candidate233-polynomial.json',{'variables':233,'degree':4,'terms':ser(poly)}),('MAP.json',{'coordinate_map':cm,'unchanged_row_map':rm,'deleted_parent_rows':[5,6,7,8],'deleted_parent_coordinates':[21,22],'new_row_normalizations':factors,'forward':'Forget parentV0.f21/22; carry allothercoordinates.','inverse':'Compute fieldA=a+c*f,N=8-a*f-2d*g in parentnames. Restorev=N/A in21/22. DividebyNorm(A),notbyitsindividualcomponents. A!=0 by retainedforced149argument.'}),('STATISTICS.json',stats)]:
 (O/name).write_text(json.dumps(obj,indent=2)+'\n')
print(stats)
