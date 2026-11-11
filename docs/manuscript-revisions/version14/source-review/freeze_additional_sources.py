from pathlib import Path
import json, hashlib
from datetime import datetime, timezone
H=Path(__file__).resolve().parent
R=H.parents[2]
def digest(b):return hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,ensure_ascii=False,indent=2)+'\n').encode()
def save(name,b):
    p=H/name
    if p.exists():assert p.read_bytes()==b
    else:p.write_bytes(b)
old=json.loads((H/'whole-initial.json').read_bytes())
assert digest((H/'whole-initial.json').read_bytes())=='c95012ef4e74137fef2fc517858797368612bb749aab3d5338dd7a42623eb886'
specs=[
 ('pole',R/'work/quartic-version6-release/repository/docs/theorem-application-audit/evidence/pole.md','docs/theorem-application-audit/evidence/pole.md','b3bc7a18a7f1b68a55a4e9f84779b922456b8f5cb8fc2dccd057629ee401cf09'),
 ('interpreter',R/'work/astra-final-interpreter-precision-independent-review-001/REPORT.md','docs/research-review/proof-sources/interpreter-precision.md','05b3e36127707fc5f3bf415bf9f9a13b190af616d1af7482d3d7958a10686cd8')]
rows={
 'pole':[
 (1,14,'P01','Review scope and provenance, including explicit conditional RC input and excluded broad converse.','No verdict is used as a proof; actual proof starts below.','background'),
 (15,29,'P02','The literal eleven-witness expression has second ordinate z*r2 and root Q^2. Signed divisors of2730 supply one common positive m with the required real,2-adic,3-adic squareclasses.','B>0, B<1/2, square denominator and v_p(B)>=4 for p in{2,3,5,7,13}; H=A^2(1-B/m). The square changes degree75 to150 but not rational zeros.','dependency'),
 (30,37,'P03','The positive squarefree parts beta,theta are17 and1 mod24 and mutual local squares with disjoint support.','Negative valuations of B are even; for q|theta, positive/negative valuations force even v(H), hence v(B)=0 and B/m=1 modq. theta=1 permitted.','dependency'),
 (38,61,'P04','Split-cubic Kummer map and local image calculation give the three displayed necessary matrix conditions and an upper bound of eight global Selmer classes.','l positive squarefree, l=11mod12; torsion images(l,1),(3,-l). At odd q, open formal subgroup makes E/2 have four elements. Dyadic calculation is only necessary, never treated as full local image. At3 the second coordinate is square.','dependency'),
 (63,74,'P05','One simultaneous assignment produces kerK=<1,1_B> and lambda outside imK on Q0 and Q1. Ksharp=K+lambda*a^t factors K=Ksharp*T.','Preserve both cross-row sums with possibly nonzero individual symbols. I has d-1 slots and q0 has type(1,1); a=e_bstar+e_q0. Deleted block nonsingular even at d=1.','dependency'),
 (75,83,'P06','The enlarged determinant is a nonzero Boolean polynomial with full-product coefficient1; select its bits before realizing all auxiliary primes by CRT and Dirichlet.','Only q0-J diagonal bits vary after deletion; original block remains fixed. J empty requires no additional bits. Reverse Legendre symbols obey reciprocity. Fixed finite old support excluded.','dependency'),
 (84,91,'P07','Both n and n*theta lie in the exact restricted-converse domain, and(beta,1) supplies a third independent global Selmer class.','Actual all-place local membership includes2,3,infinity, support and remaining unramified primes. q0 outside beta excludes equality with first torsion class; negative second coordinates exclude the other two.','dependency'),
 (92,111,'P08','Finite Kummer and alternating Cassels-Tate pairing on the finite quotient of Sha give full2-infinity corank1; then RC and forward rank1 give rank1 and Sha[2]=0.','Allow divisible Sha; paired cyclic factors imply even dimF[2], not just square cardinality or a perfect pairing onF[2]. RC applies to n and n*theta, not rational e or nH.','dependency'),
 (112,124,'P09','The resulting actual points rescale to the same fixed B,m,A,H and exact saved eleven witnesses.','e=n/q1^2,z=c*q2/q1,r2=c^3*y2/(q1^3*z). Both points avoid cubic roots and O by independence. theta=1 can reuse the same point.','dependency'),
 (125,143,'P10','Silverman split-cubic map, Poonen-Stoll alternation, finite Kummer structure, BCDT and Kolyvagin are the substantive external suppliers. Immediate pole input inequalities preserve the trace and one shared B.','The report records inspected primary versions but this later reading does not claim a new primary-page audit. Multiplication local/height premises remain supplied by the manuscript.','dependency'),
 (144,158,'P11','Finite regressions and historical review boundary. The all-size proofs above, not small matrix checks or a single theta=1 witness, supply the argument.','Computational claims are historical evidence requiring their exact files if adopted. No global RC proof or new whole-manuscript acceptance is asserted by this source.','background')],
 'interpreter':[
 (1,23,'I01','Scope, exact code locators, and explicit imported packed-history and alpha/power contracts.','Historical favorable verdict is not a premise. The current manuscript supplies generic packed histories and alpha/power; source-specific machine correspondence is the added proof.','dependency'),
 (24,50,'I02','Natural signed input decoding, identical nonsingular curve/base point, exact total predicate and nonvanishing of its guarded point ratios.','Code0=0,code1=-1; field basis(1,sqrt2); z=-x/y. Good reductions20/24 and explicit full2-torsion imply the nonzero ordinate point is nontorsion. a,ell>=1,n outside sixcontacts,kappa!=0,j=n*a.','dependency'),
 (51,60,'I03','Assembler helpers implement clearing, copying, comparisons, division and lowered arithmetic on all naturals, including all actual aliases.','Fresh temporaries; output assignment delayed where aliases occur. divmod requires positive divisor. Loop variants are consumed counters or smaller list tails. Finite sample checks are not the induction.','dependency'),
 (61,70,'I04','Literal virtual-program and tape encodings yield exact finite-prefix simulation; virtual halt iff finite cleanup/unique all-zero halt.','e+1=2^w(2D+1),four base2^w digits per instruction; missing/opcode0or>=3 halts. nil=0,cons=2^h(2t+1). w=0 immediatehalt, list extension useszeros.','dependency'),
 (71,80,'I05','Normalized signed pairs and quadratic-field operations preserve actual values and exact zero tests. Jacobian doubling implements the tangent law.','pn=0 invariant; Norm zero iff both coefficients zero. Finite point hasZ!=0 andY^2=X^3+AXZ^4. O orY=0 doubles toO; otherwiseZprime=2YZ!=0.','dependency'),
 (81,96,'I06','Jacobian chord law and signed binary multiplication agree with affine group arithmetic for every reached point.','H!=0 uses chord formulas; H=R=0 doubles; H=0,R!=0 is opposite; eitherO copiesother. Accumulated+[remaining]base invariant with halving count includeszero andnegativeindices.','dependency'),
 (97,110,'I07','Fractions, reciprocal ordinates and the strict distance comparison implement precisely the total predicate with positive denominators.','O maps0/1; finiteY=0 and divisorzero reject. Sign transferred to numerator. Formula|-C| preserved using normalized signed arithmetic; all actual divisions are guarded.','dependency'),
 (111,124,'I08','Strict precision uses floor((D-1)/(4U)) and is independent of unreduced fraction scaling; repeated division by4 matches bit-length.','U,D>0; equality must reject; threshold0 rejects because required exponent is positive on guarded domain. Fixed positive scaling does not change greatest allowed exponent.','dependency'),
 (125,138,'I09','Saturated arithmetic computes the exact capped fixed height expression, including capped exponentiation and every constant.','cap>=1; zero factors retained; exponentzero gives1 including0^0; bases0/1 separated; all laterfactorialfactorspositive. H expression fixed before inputcomparison, not an unspecified large bound.','dependency'),
 (139,150,'I10','Every ideal IR input terminates at accept/reject, while primitive lowering recognizes acceptance via a unique all-zero halt.','Reject is an absorbing loop on reservedzero at122828; cleanup122829..146411 covers23582registers. No budget exhaustion is treated asfalse. Arithmetic/control induction uses actual aliases.','dependency'),
 (151,160,'I11','Cantor unpairing and wrapper relocation preserve five natural input codes and exact accepting semantics.','Triangularinterval invariant, head/tailaliases protected; wrapper368instructions, scratch[23582,23633)cleared; jumpsrelocated, no newhalt. No reversal or signeddecodinginsidewrapper.','dependency'),
 (161,174,'I12','Exact specialization of universal H plus four Cantor residuals yields the1305811-variable natural precision polynomial iff total predicate accepts.','Code e fixed; input n maps to5; oldwitnessi mapsi+7 andprivatepowerblocksshift7. Newinput0..4,tuple5..8. Value semantics forprivatepowercalls and genericpackedhistory theorem are explicitimports.','dependency'),
 (175,185,'I13','Historical exact checks bind whole objects, not fingerprints or positive samples; report preserves remaining arithmetic/bridge imports.','All1024examplesreject. General accepting direction comes from preceding invariant/termination/specialization proof. Finite replay may be retained only under its exact sourcepins.','background')]
}
newuses=[];passages=[];pins=[]
for key,origin,path,want in specs:
    raw=origin.read_bytes();assert digest(raw)==want
    pin={'side':'head','path':path,'sha256':want};pins.append(pin)
    save(key+'.additional-source-frozen.md',raw)
    lines=raw.splitlines(keepends=True)
    covered=[]
    for lo,hi,uid,statement,conditions,classification in rows[key]:
        covered+=list(range(lo,hi+1))
        pid='added-'+uid
        loc={'pin':pin,'start_line':lo,'end_line':hi,'excerpt_sha256':digest(b''.join(lines[lo-1:hi]))}
        passages.append({'id':pid,'location':loc,'reason':statement})
        assertion={'statement':statement,'objects':conditions,'hypotheses':conditions,
          'quantifiers':'For every input and parameter satisfying the explicit conditions in this recorded source use; historical provenance rows assert no mathematical universal claim.',
          'parameter_range':conditions,'uniformity':'The source argument is general on the displayed domain. Finite regressions are distinguished from that claim.',
          'constants':conditions,'normalizations':conditions,'exceptional_cases':conditions,
          'limit_order':'No new limit interchange is asserted. The explicit order of construction, guards and inference in this source passage must be preserved.'}
        newuses.append({'id':uid,'consumer':'source-local:'+uid,'passages':[pid],'assertion':assertion,'classification':classification,
          'reason':'Later source-inventory discovery after the main initial freeze. Derived by reading the actual additional proof before its ordinary-application reconciliation; source itself contains historical review claims which are not used as authority.',
          'shared_contract_justification':None,'supplier':None,'application_id':None,'inline_argument':None})
    # Blank separators not attached to a substantive row are retained explicitly.
    missing=sorted(set(range(1,len(lines)+1))-set(covered))
    assert all(not lines[n-1].strip() for n in missing),(key,missing)
    for n in missing:
        passages.append({'id':'added-'+key+'-blank-'+str(n),'location':{'pin':pin,'start_line':n,'end_line':n,'excerpt_sha256':digest(lines[n-1])},'reason':'Blank separator; no mathematical import.'})
out={'schema':'protocol-source-first/v1','sources':old['sources']+pins,'uses':old['uses']+newuses}
save('whole-initial-with-additional-sources.json',enc(out))
save('additional-initial-passages.json',enc(passages))
stamp={'run_id':'/root/astra_v14_source_review','operator_label':'local:v14:source-first-review:20261107',
 'frozen_at':datetime.now(timezone.utc).isoformat(),'predecessor_initial_sha256':digest((H/'whole-initial.json').read_bytes()),
 'successor_initial_sha256':digest((H/'whole-initial-with-additional-sources.json').read_bytes()),'added_sources':pins,'added_uses':len(newuses),
 'chronology':'Main source was frozen at the recorded c950 predecessor before whole inventory comparison. Comparison then exposed substantive additional project proofs. Their complete text was personally read; this phase freezes its source-derived uses before matching those added uses to ordinary application contracts. The source texts contain historical favorable findings and source locators. These are disclosed prior exposure, not proof premises. Original main-source notes and rows are unchanged. This is a phased reconstruction, never a claim that the combined inventory was globally blind.',
 'path_status':'Pole path already exists in repository. Interpreter path is an installation proposal; final release must install these exact bytes and recheck the head pin. No committed-source claim is made now.',
 'scope':'Adds complete local/matrix pole descent and all-input interpreter/precision correspondence. Generic packed histories, alpha/power, RC and ordinary-value bridge remain explicit manuscript suppliers. Literal code, machine and polynomial objects require separate exact computation evidence.'}
save('ADDITIONAL-SOURCE-FREEZE.json',enc(stamp))
print(json.dumps(stamp,indent=2))
