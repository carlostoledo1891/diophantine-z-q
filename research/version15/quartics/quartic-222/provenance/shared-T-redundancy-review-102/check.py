import runpy,contextlib,io,json,pathlib
from fractions import Fraction as F
from collections import defaultdict
from functools import reduce
from math import gcd
with contextlib.redirect_stdout(io.StringIO()):ns=runpy.run_path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic238-optimization-20261110/resume-20261110/shared-T-domain-check-101/reverse-check.py')
pa,pm,ps,pc,k,px=[ns[x] for x in ['pa','pm','ps','pc','k','px']]
a,b,d=ns['a'],ns['b'],ns['d']; f,S=ns['f'],ns['S']; A=pa(pc(a),ps(f,ns['c']))
left=pa(pm(pa(ps(S,b),pc(ns['neg'](d))),ns['targetF']),ps(pm(A,ns['targetE']),k(-1)))
H=pa(pm(f,pm(S,S)),ps(pm(f,f),k(11,-6)),pc(k(-1)))
assert left==ps(H,ns['mul'](k(8),a))
P=pathlib.Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/quartic238-optimization-20261110/global/resume-20261110/shared-T-redundancy224-006'); par=P.parent/'shared-T-elimination224-004'
cert=json.loads((par/'CONVERSE-RESULT.json').read_text())
for c in cert['checks'][:2]:assert {x['relation'] for x in c['certificate']}<=set([0,1,3])
q=ns['qs'][2];M={tuple(x for x in m if x!=4):coef for m,coef in q.items() if 4 in m}
assert set(M)=={(),(0,),(1,),(3,)}
for coef in M.values():assert all(x.denominator%149 for x in coef)
cs=M[(1,)]; norm=cs[0]**2-2*cs[1]**2;assert norm.numerator%149 and norm.denominator%149
# Independent integer sparse full-SOS computation.
def terms(row):
 z=defaultdict(int)
 for t in row['terms']:z[t['parameterPower'],tuple(t['monomial'])]+=int(t['coefficient'])
 return {k:v for k,v in z.items() if v}
air=json.loads((par/'candidate224-ir.json').read_text());bir=json.loads((P/'candidate224-ir.json').read_text())
assert len(bir['residuals'])==198
assert [terms(x) for x in bir['residuals']]==[terms(x) for x in air['residuals'][:198]]
assert air['coordinates']==bir['coordinates'] and air['inputCoordinate']==bir['inputCoordinate']==1 and air['fixedParameter']==bir['fixedParameter']
acc=defaultdict(int)
for r in bir['residuals']:
 ts=terms(r)
 for (a,m),c in ts.items():
  for (b,n),d in ts.items():acc[a+b,tuple(sorted(m+n))]+=c*d
acc={k:v for k,v in acc.items() if v}
assert acc==terms(json.loads((P/'candidate224-polynomial.json').read_text()))
assert max(len(m) for a,m in acc)==4 and reduce(gcd,(abs(v) for v in acc.values()))==1
assert set(i for a,m in acc for i in m)==set(range(1,225))
assert max(abs(v) for (a,m),v in acc.items() if a==0)<149**214
assert max(abs(v) for (a,m),v in acc.items() if a==1)==44402
assert {(a,m):v for (a,m),v in acc.items() if a==2}=={(2,(114,114)):1} and acc[0,(114,114)]==1
print(json.dumps({'status':'pass','F_E_use_only_Q0_Q1_Q3':True,'H_curve_identity_checked':True,'M_coefficients_149_integral':True,'M_S_coefficient_norm':str(norm),'variables':224,'rows':198,'coordinate_monomials':len({m for a,m in acc}),'parameter_terms':len(acc),'degree':4,'content':1},indent=2))
