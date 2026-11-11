from fractions import Fraction as Q
from math import gcd,lcm
from collections import defaultdict
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent
source=P.parent/'shared-alternate-226-001/candidate226-ir.json'
raw=source.read_bytes();assert hashlib.sha256(raw).hexdigest()=='d9853b6618d91e42625029dee0015164bbf45445fb15d58d237cadd5d90def48'
ir=json.loads(raw);rows={r['id']:r for r in ir['residuals']}
def clean(p):return {m:c for m,c in p.items() if c}
def add(*ps):
 d=defaultdict(Q)
 for p in ps:
  for m,c in p.items():d[m]+=c
 return clean(d)
def sc(p,c):return clean({m:c*v for m,v in p.items()})
def mul(p,q):
 d=defaultdict(Q)
 for (a,m),c in p.items():
  for (b,n),e in q.items():d[a+b,tuple(sorted(m+n))]+=c*e
 return clean(d)
def v(i):return {(0,(i,)):Q(1)}
def const(c):return {(0,()):Q(c)} if c else {}
def fadd(*ps):return tuple(add(*(p[i] for p in ps)) for i in range(2))
def fsc(p,c):return tuple(sc(x,c) for x in p)
def fm(p,q):return add(mul(p[0],q[0]),sc(mul(p[1],q[1]),2)),add(mul(p[0],q[1]),mul(p[1],q[0]))
def fc(a,b=0):return const(a),const(b)
def pair(i):return v(i),v(i+1)
def poly(r):return {(t['parameterPower'],tuple(t['monomial'])):Q(t['coefficient']) for t in r['terms']}
def primitive(p):
 d=lcm(*(c.denominator for c in p.values())); pp={m:int(c*d) for m,c in p.items()};g=gcd(*pp.values());return {m:c//g for m,c in pp.items()}
def terms(p):return [{'parameterPower':a,'monomial':list(m),'coefficient':str(c)} for (a,m),c in sorted(p.items())]

rels=json.loads((P/'FIELD-RELATIONS.json').read_text())[0]['relations']
F=pair(17);S=pair(19);G=pair(126);B=(v(74),sc(v(75),2));w=(v(21),sc(v(22),2));W=(add(sc(v(23),Q(37249,2401)),sc(v(24),Q(-34848,2401))),sc(add(v(23),sc(v(24),-1)),Q(25476,2401)));T=pair(225)
fields=[F,S,G,B,w,W,T]
def expand(rel):
 out=fc(0)
 for t in rel:
  p=fc(*map(Q,t['coefficient']))
  for i in t['monomial']:p=fm(p,fields[i])
  out=fadd(out,p)
 return out
# Check stored B/W outputs exactly span the expected field square definitions.
bdef=expand(rels[0]);wdef=expand(rels[4])
assert bdef[0]==poly(rows[26]) and bdef[1]==sc(poly(rows[27]),2)
assert wdef[0]==add(sc(poly(rows[7]),Q(193,2401)),sc(poly(rows[8]),Q(-1056,2401)))
assert wdef[1]==add(sc(poly(rows[7]),Q(132,2401)),sc(poly(rows[8]),Q(-772,2401)))

a=fc(57,-28);b=fc(8,-14);c=fc(88,-48);d0=fc(39,-36)
oldF=fadd(fm(fadd(a,fm(c,F)),G),fm(b,fm(F,S)),fm(d0,F))
oldE=fadd(fm(b,fm(S,G)),fsc(fm(d0,G),-1),fsc(fm(a,F),-1),fc(8))
N=fadd(fc(8),fsc(fm(a,F),-1),fsc(fm(d0,G),-2))
A2=fadd(fm(a,a),fsc(fm(fm(a,c),F),2),fm(fm(c,c),B))
oldW=fadd(fm(A2,w),fsc(fm(N,N),-1))
assert oldF==tuple(poly(rows[i])for i in [3,4])
assert oldE==tuple(poly(rows[i])for i in [5,6])
assert oldW==(poly(rows[1]),sc(poly(rows[2]),2))

deleted={126,127};removed={1,2,3,4,5,6,199,200}
assert {r['id']for r in ir['residuals']if any(deleted.intersection(t['monomial'])for t in r['terms'])}==removed
coords=[c for c in ir['coordinates']if c['id']not in deleted];mapping={c['id']:i+1 for i,c in enumerate(coords)}
newrows=[]
def put(name,p,parent=None):
 assert max((len(m)for a,m in p),default=0)<=2
 pp={(a,tuple(sorted(mapping[i]for i in m))):c for (a,m),c in p.items()}
 rr={'id':len(newrows)+1,'name':name,'terms':terms(pp)}
 if parent:rr['parentRowId']=parent
 newrows.append(rr)
for r in ir['residuals']:
 if r['id']not in removed:put(r['name'],poly(r),r['id'])
for i in [1,2,3,5]:
 for part,p in enumerate(expand(rels[i])):put('sharedT.reference.relation'+str(i)+'.'+str(part),primitive(p))
assert len(coords)==224 and len(newrows)==200
newir=dict(ir,variables=224,coordinates=[dict(c,id=mapping[c['id']])for c in coords],residuals=newrows,source={'parent_sha256':hashlib.sha256(raw).hexdigest(),'construction':'Polynomial elimination of g_H using exact shared-T reference identities'})
acc=defaultdict(int)
for r in newrows:
 items=list(poly(r).items())
 for i,((a,m),c)in enumerate(items):
  for j in range(i,len(items)):
   (b,n),d=items[j];acc[a+b,tuple(sorted(m+n))]+=int(c*d)*(1 if i==j else 2)
acc=clean(acc);assert gcd(*acc.values())==1 and max(len(m)for a,m in acc)==4
assert {i for a,m in acc for i in m}==set(range(1,225))
assert max(abs(c)for (a,m),c in acc.items()if a==0)<149**214
assert [(m,c)for(a,m),c in acc.items()if a==2]==[((114,114),1)] and acc[(0,(114,114))]==1
assert max(abs(c)for(a,m),c in acc.items()if a==1)==44402
stats={'coefficient_height':'A_N^2+1 for N>=53; ineffective defining threshold unchanged','variables':224,'residuals':200,'unchanged_parent_rows':192,'coordinate_monomials':len({m for a,m in acc}),'parameter_terms':len(acc),'degree':4,'content':1}
for name,obj in [('candidate224-ir.json',newir),('candidate224-polynomial.json',{'variables':224,'degree':4,'inputCoordinate':ir['inputCoordinate'],'fixedParameter':ir['fixedParameter'],'terms':terms(acc)}),('STATISTICS.json',stats),('MAPS.json',{'old_to_new':mapping,'deleted':sorted(deleted),'removed_rows':sorted(removed),'new_relations':[1,2,3,5],'field_convention':'FIELD-RELATIONS variables f,S,g,B,w,W,T; B andw use2sqrt2 imaginary basis; W is decoded from original nonsingular two-output basis.'})]:
 (P/name).write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(stats))
