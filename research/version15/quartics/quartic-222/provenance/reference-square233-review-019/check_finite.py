import sys,json,hashlib,math
from pathlib import Path
from collections import defaultdict,Counter
base=Path(sys.argv[1]); parent=Path(sys.argv[2]); out=Path(__file__).parent
p=json.loads(parent.read_text()); s=json.loads((base/'candidate233-ir.json').read_text()); mp=json.loads((base/'MAP.json').read_text())
ren={i:i if i<21 else i-2 for i in range(1,236) if i not in (21,22)}
assert {int(k):v for k,v in mp['coordinate_map'].items()}==ren
assert s['variables']==233 and len(s['coordinates'])==233 and len(s['residuals'])==207
assert s['inputCoordinate']==p['inputCoordinate']==1
assert s['fixedParameter']==p['fixedParameter']
assert sorted(c['id'] for c in s['coordinates'])==list(range(1,234))
for c in p['coordinates']:
 if c['id'] in ren:
  expected=dict(c,id=ren[c['id']]);actual=next(x for x in s['coordinates'] if x['id']==expected['id']);assert actual==expected,(c,actual)
def readterms(r,remap=None):
 z=defaultdict(int)
 for t in r['terms']:
  m=t['monomial'];m=[remap[x] for x in m] if remap else m
  z[(t['parameterPower'],tuple(sorted(m)))]+=int(t['coefficient'])
 return {k:v for k,v in z.items() if v}
def add(*ps):
 z=defaultdict(int)
 for q in ps:
  for k,v in q.items():z[k]+=v
 return {k:v for k,v in z.items() if v}
def scale(p,c):return {k:c*v for k,v in p.items() if c*v}
def mul(p,q):
 z=defaultdict(int)
 for (e,m),a in p.items():
  for (f,n),b in q.items():z[(e+f,tuple(sorted(m+n)))]+=a*b
 return {k:v for k,v in z.items() if v}
def con(n):return {(0,()):n} if n else {}
def x(i):return {(0,(ren[i],)):1}
def ka(p,q):return (add(p[0],q[0]),add(p[1],q[1]))
def km(p,q):return (add(mul(p[0],q[0]),scale(mul(p[1],q[1]),2)),add(mul(p[0],q[1]),mul(p[1],q[0])))
def kn(p):return (scale(p[0],-1),scale(p[1],-1))
def kc(a,b=0):return (con(a),con(b))
f=(x(17),x(18));g=(x(137),x(138));B=(x(84),scale(x(85),2));w=(x(31),scale(x(32),2))
a=kc(57,-28);b=kc(8,-14);c=kc(88,-48);d=kc(39,-36)
AA=ka(ka(km(a,a),km(kc(2),km(km(a,c),f))),km(km(c,c),B));NN=ka(ka(kc(8),kn(km(a,f))),kn(km(kc(2),km(d,g))));RR=ka(km(AA,w),kn(km(NN,NN)))
rows={r['id']:r for r in s['residuals']}
removed={5,6,7,8};consumers={r['id'] for r in p['residuals'] if any(set(t['monomial'])&{21,22} for t in r['terms'])};assert consumers==removed
assert set(map(int,mp['unchanged_row_map']))==set(range(1,210))-removed
matched=set()
for old,new in mp['unchanged_row_map'].items():
 old=int(old);assert readterms(p['residuals'][old-1],ren)==readterms(rows[new]),(old,new)
 assert rows[new]['name']==p['residuals'][old-1]['name'];matched.add(new)
newrows=[readterms(r) for r in s['residuals'] if r['id'] not in matched]
def primitive_key(poly):
 vals=list(poly.values());gd=math.gcd(*vals);sign=1 if poly[sorted(poly)[0]]>0 else -1
 return tuple((k,v//gd*sign) for k,v in sorted(poly.items()))
assert Counter(map(primitive_key,newrows))==Counter(map(primitive_key,[RR[0],RR[1]]))
assert all(math.gcd(*r.values())==1 for r in newrows)
assert mp['new_row_normalizations']==['1','1/2']
assert newrows[0]==RR[0] and {k:2*v for k,v in newrows[1].items()}==RR[1]
poly=defaultdict(int)
for row in s['residuals']:
 terms=list(readterms(row).items())
 assert all(len(m)<=2 for (e,m),v in terms)
 for i,((e,m),v) in enumerate(terms):
  for j in range(i,len(terms)):
   (f,n),w=terms[j];poly[(e+f,tuple(sorted(m+n)))]+=v*w*(1 if i==j else 2)
poly={k:v for k,v in poly.items() if v}
declared=readterms(json.loads((base/'candidate233-polynomial.json').read_text()))
assert poly==declared
stats=json.loads((base/'STATISTICS.json').read_text())
monos={m for e,m in poly};degree=max(map(len,monos));content=math.gcd(*poly.values())
assert stats['coordinate_monomials']==len(monos) and stats['parameter_terms']==len(poly) and stats['degree']==degree and stats['content']==content
constant_max=max(abs(v) for (e,m),v in poly.items() if e==0)
linear_max=max(abs(v) for (e,m),v in poly.items() if e==1)
# This target's compact statistics omit coefficient maxima; derive the full envelope independently below.
if 'constant_max' in stats: assert int(stats['constant_max'])==constant_max
if 'linear_parameter_max' in stats: assert int(stats['linear_parameter_max'])==linear_max
# Exact specialized coefficient height at the first sufficient integer N, not a claim about ineffective N0.
by_m=defaultdict(dict)
for (e,m),v in poly.items():by_m[m][e]=v
param_terms=[{'power':e,'monomial':m,'coefficient':str(v)} for (e,m),v in sorted(poly.items()) if e]
assert sorted((tuple(sorted(pp.items())) for pp in by_m.values() if any(e for e in pp)))==sorted([((1,-44402),),((1,-2),),((0,1),(2,1))])
N=0
while True:
 A_N=149**(2*N+1);height=max(abs(sum(v*A_N**e for e,v in pp.items())) for pp in by_m.values())
 if height==A_N*A_N+1 and A_N>=linear_max and A_N*A_N>=constant_max:break
 N+=1
 assert N<1000
used={i for m in monos for i in m};assert used==set(range(1,234))
result={'status':'pass','parent_sha256':hashlib.sha256(parent.read_bytes()).hexdigest(),'candidate_sha256':hashlib.sha256((base/'candidate233-ir.json').read_bytes()).hexdigest(),'variables':233,'quadratic_residuals':207,'unchanged_parent_rows':len(matched),'new_field_components_checked':2,'deleted_v_consumers_exact':sorted(consumers),'complete_SOS_comparison':True,'coordinate_monomials':len(monos),'parameter_terms':len(poly),'degree':degree,'content':content,'constant_max':str(constant_max),'linear_parameter_max':str(linear_max),'parameter_terms_exact':param_terms,'height_for_all_N_at_least':N,'height_formula':'A_N^2+1','height_exact_for_positive_A':'max(constant_max,44402*A,A^2+1)','threshold_scope':'coefficient height only; not ineffective defining N0','all_coordinates_occur':True,'checks_do_not_replace_arithmetic_proof':True}
(out/'FINITE-CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['constant_max','parameter_terms_exact']}))
