import json,hashlib,copy
from pathlib import Path
O=Path(__file__).resolve().parent;A=O.parent/'v14-local-twist-application-001'
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(n,x):(O/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
rows=json.loads((A/'COMPONENTS.json').read_text())
needed=[
 ('The fixed original E over Q2, its displayed quadratic twists E^h and E^h0, and their minimal invariant differentials or duals.','h and h0 are odd 2-adic units with h=h0*u^2 and u in Z2^times; compare displayed differentials with minimal invariant differentials.','Every such unit-square change, with h0 in the fixed four representatives.','Residue characteristic two; no nonunit u is allowed.','The valuation equals that for h0, so takes finitely many values.'),
 ('The actual twist E^h at an active good odd prime q.','E is good at q; q divides squarefree h; the twist is already proved bad by NOS and has j(E^h)=j(E) integral.','Every active good odd prime in this family.','Includes q=3; the minimal reduction criterion has no restriction excluding3.','The actual bad integral-j twist is additive.'),
 ('The original good E and its quadratic twist at an odd good prime q, with V2 Tate coefficients.','The original E is good at q. At active q the quadratic character is ramified because q divides squarefree h; at unused q it is unramified.','Every active or unused good odd prime in the specified support.','Tate prime2 differs from the odd residue prime.','Ramified inertia gives bad reduction of the twist; unramified inertia gives good reduction.'),
 ('The fixed local quadratic twists at primes dividing2N and the actual active/unused good primes.','Fix the original E and finite set2N; the local squareclasses range over a finite set. Active twists have already been proved additive, unused twists good; the original Kato norm polynomial is supplied separately.','Every twist in these fixed local classes, and its active/unused good primes.','All fixed bad primes including2 and active good odd primes including3.','Only finitely many fixed bad-prime factors occur and are nonzero; active factors are1 and unused factors equal #E^h(Fq)/q.')]
available=[
 ('Weierstrass coordinate changes and minimal invariant differentials over a local field.','Use the standard admissible change of variables and minimal integral Weierstrass equations.','Every such change and minimal equation.','The published transformation and minimal differential assertions, including residue characteristic2.','Exact differential scaling and uniqueness up to a local unit.','Standard invariant differential; no fixed twist family is part of this source statement.'),
 ('Minimal integral Weierstrass equations over a local field.','The equation is minimal.','Every such equation.','All residue characteristics of VII.5.1, including3.','The local reduction type is determined by the published minimal-model criteria.','Minimal c4 and discriminant; multiplicative reduction has c4 a unit and positive discriminant valuation.'),
 ('An elliptic curve over a local field and its prime-to-residue-characteristic Tate module.','The Tate prime differs from the residue characteristic.','Every such curve and Tate prime.','The good-reduction equivalence of VII.7.1.','Good reduction is equivalent to an unramified Tate representation.','Usual inertia action; no ramified quadratic family is assumed by the theorem.'),
 ('An elliptic curve and its local Euler polynomial.','The local reduction type is given.','Each prime and each of the four reduction cases.','Good, split multiplicative, nonsplit multiplicative and additive reduction.','Exact local formulas; no uniform finite-list assertion is in the source alone.','Appendix C.16 local reciprocal factor evaluated at s=1.')]
for i in range(4):
 t=rows[i];u=t['use'];c=t['connection'];n=copy.deepcopy(c['needed_assertion']);a=copy.deepcopy(c['available_assertion'])
 for k,v in zip(['objects','hypotheses','quantifiers','parameter_range','uniformity'],needed[i]):n[k]=v
 n['normalizations']='The actual fixed minimal invariant differential or its dual and the Appendix C.16 local Euler convention; the fixed original rational comparison and Kato norm relation are separate.'
 for k,v in zip(['objects','hypotheses','quantifiers','parameter_range','uniformity','normalizations'],available[i]):a[k]=v
 a['constants']='No family-uniform constant asserted by this primitive input.';a['exceptional_cases']='Only the stated published local conditions apply.';a['limit_order']='No inverse-limit interchange.'
 u['assertion']=n;c['needed_assertion']=n;c['available_assertion']=a;c['connecting_derivation']['output_assertion']=n
 c['use_sha256']=sha(json.dumps(u,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
dump('COMPONENTS.json',rows)
for n in ['RECONCILIATION.json','CALLER-CLARIFICATION.json']:(O/n).write_bytes((A/n).read_bytes())
dump('DELTA.json',{'predecessor':str(A),'change':'Only the four primitive available/needed profile fields and consequent use digests are specialized. Assertions statements, proof, raw locations, observation reconciliation and actual caller convention proposal are unchanged.'})
dump('MANIFEST.json',{'author':'/root/v14_sign_conductor','files':{p.name:{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in O.iterdir() if p.is_file() and p.name!='MANIFEST.json'},'status':'Immutable profile correction awaiting independent review'})
print(sha((O/'MANIFEST.json').read_bytes()))
