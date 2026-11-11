from fractions import Fraction as Q
from math import gcd,lcm
from collections import defaultdict
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent
source=Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic238-optimization-20261110/resume-20261110/scalar-contact-quartic-001/candidate232-ir.json')
raw=source.read_bytes();assert hashlib.sha256(raw).hexdigest()=='87601e9690f94240e22d949b774522467572d562035d1c3143d04d4c36dc4f35'
ir=json.loads(raw); rows={r['id']:r for r in ir['residuals']}
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
S=pair(19);gH=pair(134);T=pair(233);A=fc(156,Q(69,2));B=fc(118,60);C=fc(-288,-128);G=fc(252,-672);d=fc(3,-1)
N=fadd(fm(A,S),C,fm(G,gH));D=fadd(fm(B,S),A);tdef=fadd(fm(D,T),fsc(N,-1))
remove_rows=set();replace={};cert=[];deleted=set(range(21,29))
for i in range(4):
 z=pair(21+2*i);LP=pair(49+4*i);k=pair(187+14*i);E=fadd(pair(177+14*i),fsc(pair(179+14*i),-1));K=fsc(fm(d,k),2)
 alt=fadd(fm(N,z),fm(D,LP));root=fadd(E,fm(K,z));altids=[9+4*i,10+4*i];rootids=[144+18*i,145+18*i]
 assert poly(rows[altids[0]])==alt[0]
 assert poly(rows[altids[1]])==sc(alt[1],2)
 for j in range(2):assert poly(rows[rootids[j]])==root[j]
 direct=fadd(fm(E,T),fsc(fm(K,LP),-1))
 # D*direct = D*T*root - K*alt - K*z*tdef.
 identity=fadd(fm(D,direct),fsc(fm(fm(D,T),root),-1),fm(K,alt),fm(fm(K,z),tdef))
 assert all(not p for p in identity)
 for j,rid in enumerate(rootids):replace[rid]=('alternate.direct.'+str(i+1)+'.'+str(j),primitive(direct[j]))
 remove_rows.update(altids)
 actual={r['id'] for r in ir['residuals'] if any(set(t['monomial'])&{21+2*i,22+2*i} for t in r['terms'])}
 assert actual==set(altids+rootids),actual
 cert.append({'pair':i+1,'deleted_coordinates':[21+2*i,22+2*i],'old_alternate_rows':altids,'replaced_root_rows':rootids,'all_consumers':sorted(actual),'field_identity':True})
oldcoords=ir['coordinates']+[{'id':233,'sourceId':'shared-T-0','name':'shared.alternate.negativeReciprocalZ0.0','kind':'gate'},{'id':234,'sourceId':'shared-T-1','name':'shared.alternate.negativeReciprocalZ0.1','kind':'gate'}]
coords=[c for c in oldcoords if c['id'] not in deleted];mapping={c['id']:i+1 for i,c in enumerate(coords)};coords=[dict(c,id=mapping[c['id']]) for c in coords]
newrows=[];unchanged=[]
def append(name,p,oldid=None):
 pp={(a,tuple(sorted(mapping[i] for i in m))):c for (a,m),c in p.items()}
 assert all(len(m)<=2 for a,m in pp)
 rr={'id':len(newrows)+1,'name':name,'terms':terms(pp)}
 if oldid is not None:rr['parentRowId']=oldid
 newrows.append(rr)
for r in ir['residuals']:
 if r['id'] in remove_rows:continue
 if r['id'] in replace:name,p=replace[r['id']]
 else:name,p=r['name'],poly(r);unchanged.append(r['id'])
 assert not any(deleted.intersection(m) for a,m in p)
 append(name,p,r['id'])
for j in range(2):append('shared.alternate.T.definition.'+str(j),primitive(tdef[j]))
assert len(coords)==226 and len(newrows)==200 and len(unchanged)==190
out=dict(ir,variables=226,coordinates=coords,residuals=newrows,source={'parent_sha256':hashlib.sha256(raw).hexdigest(),'parent_path':str(source),'adaptation':'shared alternate denominator; Jose Brox public34454098637ba9100b19071da55a38199589f5e0 direct-ratio idea'})
(P/'candidate226-ir.json').write_text(json.dumps(out,indent=2)+'\n')
# Independent unordered pair expansion, all residuals unweighted.
acc=defaultdict(int)
for r in newrows:
 items=list(poly(r).items());assert all(c.denominator==1 for _,c in items)
 for i,((a,m),c) in enumerate(items):
  for j in range(i,len(items)):
   (b,n),e=items[j];acc[a+b,tuple(sorted(m+n))]+=int(c*e)*(1 if i==j else 2)
acc=clean(acc);assert max(len(m) for a,m in acc)==4;assert gcd(*acc.values())==1
profiles=defaultdict(dict)
for (a,m),c in acc.items():profiles[m][a]=c
stats={'variables':226,'residuals':200,'degree':4,'content':1,'parameter_terms':len(acc),'coordinate_monomials':len(profiles),'unchanged_parent_rows':190,'replaced_parent_rows':8,'removed_parent_rows':8,'added_rows':2,'all_variables_used':len({i for a,m in acc for i in m})==226,'parameter_power_profiles':sorted({tuple(p) for p in profiles.values()})}
(P/'candidate226-polynomial.json').write_text(json.dumps({'variables':226,'degree':4,'inputCoordinate':ir['inputCoordinate'],'fixedParameter':ir['fixedParameter'],'terms':terms(acc)},indent=2)+'\n')
constant_max=max(abs(c) for (a,m),c in acc.items() if a==0)
assert constant_max<149**214
assert [(m,c) for (a,m),c in acc.items() if a==2]==[((114,114),1)]
assert acc[(0,(114,114))]==1
assert max(abs(c) for (a,m),c in acc.items() if a==1)==44402
stats.update({'maximum_parameter_free_coefficient':str(constant_max),'maximum_linear_parameter_coefficient':44402,'coefficient_height':'A_N^2+1 for N>=53','coefficient_threshold_not_defining_threshold':True})
(P/'STATISTICS.json').write_text(json.dumps(stats,indent=2)+'\n')
(P/'MAPS.json').write_text(json.dumps({'old_to_new':mapping,'deleted':sorted(deleted),'T_old_ids':[233,234],'T_new_ids':[mapping[233],mapping[234]],'unchanged_rows':unchanged,'certificates':cert,'forward':'T=N/D; delete each z_i','reverse':'z_i=-LP_i/T; forget T','required_domain':'D!=0 andT!=0, separately established from retained reference/scalar rows'},indent=2)+'\n')
print(json.dumps(stats))
