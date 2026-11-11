"""Current clause connections; source ancestry remains explicitly separate."""
import copy,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; OUT=Path(__file__).resolve().parent
RISK=ROOT/'work/source-risk-review-20261107'
def sha(b):return hashlib.sha256(b).hexdigest()
def digest(o):return sha(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def write(n,o):(OUT/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
source=RISK/'v14-source-reconciliation-main-001/THETA-RECONCILIATION.json'
rows=json.loads(source.read_bytes())['rows']
raw=(ROOT/'work/quartic-v14-release/preview-repository/manuscripts/quartic_v14.tex').read_bytes()
assert sha(raw)=='1f7bf748843d67c6a67d9863931ff0a15ca2548ae171ec1c1ce34b9002eb70a8'
lines=raw.splitlines(keepends=True)
def loc(a,b):return {'pin':{'side':'head','path':'manuscripts/quartic_v14.tex','sha256':sha(raw)},'start_line':a,'end_line':b,'excerpt_sha256':sha(b''.join(lines[a-1:b]))}
template=json.loads((RISK/'v14-main-active-connections-author-001/RATIONAL-MODULARITY-COMPONENT-003.json').read_bytes())
cj=json.loads((RISK/'v14-main-active-connections-author-001/CJ-COMPONENT.json').read_bytes())
replacements={
'T033':'For the actual detector stage, the quaternion algebra ramified at ell_0 and infinity and its Eichler order give the enhanced supersingular class set. Ribet\'s right-Hom lattice convention gives the same endomorphism order, and the division uniformizer acts by Frobenius. Coarse points are over F_(ell_0^2); specialization of the actual parametrization and killed cusp translations gives P_M its Hecke, Atkin–Lehner and Frobenius eigenvalues.',
'T044':'The fixed CM type reduces equivariantly and with multiplicity one onto its labelled conductor-one orientation component. With the same place and reference point, the unaveraged character sum of P_M equals lambda_M(overline(L P_D)). The opposite inert-prime orientation is supplied separately by Frobenius.',
'T045':'The stabilizer is exactly plus or minus one, so each orbit contributes the integral coefficient c0/2. All 2^(omega(N)+1) orientations have equal contribution by the paired Atkin–Lehner and Frobenius signs. Hence the coefficient is c0*2^omega(N) times one fixed-character phase times lambda_M(overline(L P_D)), at the original precision; the witness valuation is c_theta+c_w.'}
# Particular connecting arguments read in the current manuscript, not verdicts
# inferred from a historical application identifier.
arguments={
'T002':'Combine the one lattice and symbol, integral transfer, primitive norm identity, actual-class Euler-system bound and fixed old local corrections; retain K1,K2,K3 for that one class.',
'T003':'Choose one integral symbol outside the two rational Betti kernels and clear the original lattice denominator once before varying the conductor.',
'T004':'The displayed c=d_s is a unit at6NF and congruent to one at the required conductors; c(c-1)d_s(d_s-1) has valuation2e. Excluded smoothing primes are indices, not added cohomological support.',
'T005':'The Leray edge injection identifies zero inertia restrictions. Every Mackey summand restricts to upper inertia, so it vanishes; uniqueness makes these transfers compatible at all finite precisions.',
'T006':'Tensor where the quadratic character is trivial, then corestrict. Equivariance inserts chi(q) in the actual new-prime Euler factor; repeated support has factor one.',
'T007':'Use the integral group-basis map and character separation before evaluation. Repeated-two norms and vanishing lim1 of finite H0 give one compatible class; transitivity gives E.1 without group-order division.',
'T008':'Apply dual exponential and field trace to the primitive class before choosing a Gauss basis. Divide the weighted trace by sqrt(h); the signed period identity and Delta_h/h account for discriminant4h.',
'T009':'Use the finite list of local squareclasses at2N; inactive good determinants are #E^h(F_q)/q while active good local factors are one.',
'T010':'Reciprocity and finitely many power-series zeros prove nonzero generic sign components. Open image supplies rational irreducibility and a unipotent; purity is weight minus one for inverse Frobenius. Local rank-one coordinates identify J.',
'T011':'The enlarged N_K-divisible index set satisfies the two norm cases. Corestriction through the common upper field identifies Kato0.7 exactly with the supplied dyadic class. Compare subscript-zero cohomology kernels before applying the published p=2 theorem.',
'T012':'The odd local cone has injective differential with nonzero determinant; H1 is preserved and H2 contributes its determinant length. Active ramified quadratic inertia gives zero rational cone.',
'T013':'Local control and duality exclude t from old correction factors. Add the displayed lengths once: F2 pays local quotient, Fbad old bad terms, and E.1 inactive good determinants.',
'T014':'Use the same retained class in the compatible positive complex; its residual calculation, integral wedge and coefficientwise intersection establish the scalar with fixed denominator.',
'T015':'Lift minimal finite free comparisons and homotopies through Artin quotients; termwise-surjective acyclic cones have acyclic inverse limit by the product sequence.',
'T016':'Induct on the ordinary two-class field using the sole dyadic inertia generator. The explicit norm-minus-one unit has translates spanning all signatures; Kummer and Brauer invariant sequences then give the displayed dimensions.',
'T017':'Bound primes above fixed support and use Smith decomposition of finite cyclotomic specializations. Two trivial residual torsion summands force two generators in degree one. The common real action gives a fixed invariant line.',
'T018':'Different positive lifts differ by the real connecting line, so their wedge is unchanged. Cancellation of the clearing exponent leaves exactly2a wedge ztilde for the same z=F_E Z_F.',
'T019':'At each height-one DVR compute the inverse determinant by Smith entries; K2 makes the valuation nonnegative. Separately the integral wedge over O[G] and coefficientwise intersection give the fixed denominator.',
'T020':'Keep the saturation and torsion indices in the cone sequences; their explicit cancellation gives E.7. This does not specialize punctured-family primitivity.',
'T021':'The bounded real Kummer complex retains H0 and its self-annihilating H1. Finite Poitou–Tate and the compatible limits yield the exact length sequence, then universal coefficients identify the Selmer H2 length.',
'T022':'Substitute primitive K3 in the exact cone lengths. Unused good torsion cancels; every active good prime contributes minus two. Forward rank-zero supplies finiteness only when L is nonzero.',
'T023':'The nonzero reference central value selects a packet vector with nonzero Whittaker functional and positive real frequency selects the holomorphic unary-orthogonal member.',
'T024':'The additive projection and unit-character average preserve the reference by the exact two-neighborhood calculation, including the dyadic case. Smooth lower invariance gives a scalar local type.',
'T025':'The local support idempotents preserve the reference. Apply the printed same-squareclass Waldspurger identity on the entire eigenspace, then factor the polynomial square identity to get proportional functionals.',
'T026':'Compute sections by a finite affine cover and use flat field extension. A finite basis of the linear constraints defines the full eigenspace; differing good eigenvalues supply unary orthogonality.',
'T027':'Place conjugation and character twist in one full eigenspace. Compare their reference-normalized functionals; local square roots give a two-power phase whose removal is Galois fixed.',
'T028':'Only after comparison apply later exclusion sieves. Induct the integral good-prime shell recurrence at every retained index; the reference and arithmetic lower bound make the integer minimum attained.',
'T029':'Full-corank parity and the two signed nonvanishing clauses choose h_star then D_w with all fixed splitting conditions before detection.',
'T030':'The genus character leaves only D and h_star components. Forward rank kills the latter modulo torsion; the unaveraged height makes the witness non-torsion. Two good reductions and the integral character operator give one fixed multiplier.',
'T031':'A zero Kummer translation image would be a rational coboundary by the central scalar. Irreducibility makes its span full; finite index preserves an open lattice. The one element h*tau has the stated fixed valuation.',
'T032':'Realize the same sigma in each finite extension by Chebotarev. The finite-field division cocycle is additive and identifies the quotient, so its fixed row gives the witness valuation and Frobenius sign.',
'T034':'Check each actual Schwartz support under order-unit conjugation and scaling: integral projectors at2, nilpotent determinant sign at m, and division residue sign at ell_0. Their product has alpha(-1)=1.',
'T035':'Reduction modulo3 injects finite order-unit groups, so c0 clears every mass denominator. Conjugation and norm characters give representative independence and retain precision under changes of lifts.',
'T036':'With the stated self-dual measure, Fourier support lies in the dual translation lattice; sufficiently deep lower unipotents act trivially. The dyadic reference Fourier factor is retained.',
'T037':'Use the quaternion norm Weil-index identity and orthogonal sums to compute the relative diagonal Hilbert symbol. The determinants of Q_B and Q_B/m have squareclasses1 and m.',
'T038':'The explicit U,M,W relations have scalar factors independent of Q. Bruhat normal forms give one common double cover; relative eigenvalues therefore use identical lifts, including the order-four dyadic lift.',
'T039':'Factor each local congruence matrix and cancel lift ambiguities relative to theta cubed. The classical action uses gamma inverse; Hilbert reciprocity retains the dyadic factor and gives the stated character ratio.',
'T040':'At good odd primes the self-dual trace-zero lattice is spherical. Rational theta invariance and the positive-definite lattice-coset cusp expansions give holomorphy, with no additional level primes.',
'T041':'Change Q_B to Q_B/m and its real Gaussian while keeping finite weights. The exponent becomes Q_B(x)/m, so the coefficient is literally H_M(mn); measures affect Fourier operators but not this discrete sum.',
'T042':'Count preserved lines, nilpotent and imprimitive cases separately, then dualize actual isogenies for mass self-adjointness. The resulting recurrence includes all integer indices and surviving sieves.',
'T043':'Maximality identifies norm vectors with optimal embeddings. Local idempotents give two orientations per level prime and two residue orientations at ell_0; the pointwise centralizer quotient is the actual class-group torsor.',
'T046':'An integral finite-field evaluation cannot lower the native lattice index. Height zero kills the nonsimple odd-sign point by the same L, giving the all-parameter truncated bound.',
'T047':'Check actual rational matrix transforms for V_p and U_p^2; both terms have new exponent at most one. Keep unary blocks according to whether p is in J rather than introducing spurious new constituents.',
'T048':'Use the originating squarefree parameter (U minus J)r. Integral shell differences supply each factor2 before division; the unary subtraction is an integer-two division with its explicit remaining precision.',
'T049':'Finite Fourier coordinates bound the integral trace module, making it finite and closed. Good Hecke and diamond limits define trace/determinant operators on actual cuspidal and Eisenstein constituents without integral projectors.',
'T050':'At a fresh prime the V terms and unary coefficients vanish. The normalized coefficient has phase reducing to1 and actual integer-two error control, so its residue is precisely the unit symbol.',
'T051':'Use the full diamond correction and kill it by a fresh trace. The matrix trace identity plus two-fresh divisibility implies square invariance and the finite elementary quotient on reduced expansions.',
'T052':'Apply Carayol with both stated duals and Casselman to the conductor-one block. The primitive ramified determinant rules out special and supercuspidal alternatives, leaving one unramified and one ramified character.',
'T053':'Evaluate the normalized newvector Hecke sum and Whittaker coefficients to identify Fourier U_p with arithmetic Frobenius. The two matrix differences prove O.12; both vanish on unramified old blocks without semisimplicity.',
'T054':'Read O.12 at coefficient one using the same source and stage after whole-prime omission. Complementary residues produce the contraction and every stationary label multiplies with all external incidences.',
'T055':'Use fresh bridge realizations and replace one vertex at a time in the same elementary quotient. First make overlapping realizations disjoint, without testing a vertex against its own replacement.',
'T056':'Choose one signed prime in the prescribed filter, then apply the four-prime nonvanishing theorem to its actual twist with all exclusions in the splitting set; the resulting product uses at most five primes.',
'T057':'Keep dummy label count fixed before h, choose its prime realization afterward, and apply nonvanishing to the actual varying twist. The fixed even-source minimum gives F.1 and a nonempty seed contraction certificate.',
'T058':'Use the stationary one-symbol cube and its common fixed-denominator scalar to transfer the nonzero-address bound to its corank-zero base. Take the maximum over the finitely many prepared sources.',
'T059':'Combine the native two height comparisons, arithmetic lower bound and rough companion before selecting any odd minimum; the varying Sha term cancels.',
'T060':'The fixed witness and coarse bound give an attained integer minimum on one ultrafilter. Choose the threshold after a finite operator budget; bounded and large weights together give one valid stage for every Fourier index.',
'T061':'Define the odd symbol only on the bounded tested range. Visibility gives F.7. Fix the complementary twist before dimension; the sum-and-difference Selmer decomposition and separate alphabet projections retain their stated scope.',
'T062':'Compare the old coefficient at |k|D with |k| and the new one at D with1. Their central-value ratios agree; the old unit condition gives the valuation inequality without identifying their phases.',
'T063':'Under the no-seed assumption b1 gains an actual factor2. Expand all theta convolution terms and keep the distinct determinant scalars; their quadratic ratio makes the exact correction even.',
'T064':'Read a matching fresh prime and the unary-subtracted p^3 coefficient to force the mod8 congruence. Compatible K-split primes with no rational halves have exactly four two-primary points, giving the contradiction.',
'T065':'Choose bounded abstract label data and compatible finite truth tables on the same ultrafilter. Finite intersections preserve common restrictions and the witness; no stage for all cutoffs is asserted.',
'T066':'Use even repeated packets of every common label to obtain total zero. Each separate projection supplies its own seed anchors, so nonzero terminal polynomials require no product surjectivity.',
'T067':'Expand primary networks as commuting forest differences. Cauchy–Binet gives determinant and adjugate coefficients; the explicit singular and varying matrices isolate the designated first-degree action.',
'T068':'Work in the ordinary polynomial ring before Boolean reduction. The top-product monomial and exact minimum-degree accounting force one network choice for every address and both symbols; retain the stationary one-symbol specialization.',
'T069':'Fix the dimension and full graph/output budget, then intersect the finitely many table and precision sets. Choose that actual theta stage before CRT/Dirichlet realizations; visibility and the fixed even source give both upper bounds.',
'T070':'Use the same Heegner coordinate and integral support triangle before character evaluation. Native height bounds yield F.8; nonnegative finite Sha terms are used only at nonzero addresses, not the unknown base.',
'T071':'Fix denominator bound and comparison precision before dimension and theta stage. Residual coefficient transfer gives a nonzero address closer than the strict upper bound permits; Rankin factorization then gives the simple zero.'}
components=[]; pending=[]; checks=[]
for row in rows:
    key=row['use_id'].split('-')[-1]
    places=[p['location'] for p in row['passages']]
    for p in places:
        assert p==loc(p['start_line'],p['end_line']), (key,p)
    if key in ('T001','T074'):
        c=copy.deepcopy(template);u=c['use'];u.update(id='ACTIVE-THETA-'+key,passages=[p['id'] for p in row['passages']],assertion=copy.deepcopy(row['frozen_assertion']),classification='background',reason='This is a boundary summary or scope note, not a supplier of the referenced mathematical arguments.',shared_contract_justification=None,supplier=None,application_id=None,inline_argument=None)
        c.pop('connection');c['initial_mapping']=[{'id':row['use_id'],'part':'Scope summary only; mathematical applications retain their separate records.'}]
    else:
        c=copy.deepcopy(template);u=c['use'];x=copy.deepcopy(row['frozen_assertion']);m=row['semantic_match']
        x['objects']=m.get('objects_maps_conventions_uniformity',x['objects'])
        x['hypotheses']='The hypotheses in the exact current passage are retained, including these named incoming source/application conditions: '+'; '.join(h['hypotheses_and_discharge'] for h in row['historical_contracts'])
        x['normalizations']=m.get('objects_maps_conventions_uniformity',x['normalizations'])
        if key in replacements:
            x['statement']=replacements[key]
            x['hypotheses']='The actual detector stage, maximal imaginary quadratic order with units plus or minus one, split prime-power level prime to the inert odd detector prime, and the fixed CM type/place; retain the separately supplied parametrization and CM specialization inputs.'
            x['objects']='The actual enhanced supersingular pairs, their labelled embeddings, fixed-type reduction, the same P_M, lambda_M, L and unaveraged P_D.'
            x['normalizations']='Right-Hom lattice and arithmetic Frobenius conventions; fixed-type reduction has one inert-prime orientation. Opposite orientation is supplied by Frobenius. Integral c0/2 orbit mass is counted before reduction modulo2^M.'
            x['exceptional_cases']='No bijection from one fixed CM type onto both inert-prime orientations; no unlabelled injectivity, class-number averaging or division of a congruence by two. Split level includes powers of2 and inert odd detector prime may be3.'
        argument=arguments.get(key,replacements.get(key,''));assert argument,key
        # Proposition-only rows are connected through their actual following proofs.
        primary=loc(13358,13944) if key=='T002' else loc(13969,14194) if key=='T014' else places[0]
        u.update(id='ACTIVE-THETA-'+key,passages=[p['id'] for p in row['passages']],assertion=x,reason=argument,shared_contract_justification='One scoped current clause, with named incoming premises retained; no ordinary application ID is invented.',inline_argument=primary)
        u['supplier'].update(kind='inline',application_id=None,location=primary,statement=x['statement'],publication=None)
        co=c['connection'];co.update(use_id=u['id'],use_sha256=digest(u),supplier_passage_role='proof',available_assertion=copy.deepcopy(x),needed_assertion=copy.deepcopy(x),required_capabilities=[u['id']+'-output'],available_capabilities=[u['id']+'-output'],derived_capabilities=[],consumer_locations=places)
        co['connecting_derivation'].update(kind='identification',location=primary,application_id=None,output_assertion=copy.deepcopy(x))
        co['adverse_cases'].update(reason=x['exceptional_cases']+' '+argument,evidence=[primary['pin']])
        c['initial_mapping']=[{'id':row['use_id'],'part':'All unchanged clauses at their stated incoming premises.' if key not in replacements else 'Current replacement only; the removed full-orientation-image claim is not adopted.'}]
    c.pop('prior_review',None)
    c['state']='author proposal; independent clause/source comparison pending'
    c['retained_separate_inputs']=[h for h in row['historical_contracts'] if not(key in replacements and h['id']=='A028')]
    if key in replacements:c['superseded_historical_inputs']=[h for h in row['historical_contracts'] if h['id']=='A028']
    c['source_ancestry_status']='Historical contracts retain exact named prerequisites and their bounded reviews; these are not invented current ordinary IDs or automatic source closure.'
    if key=='T011':c['current_supplier_binding']={'application_id':'KATO-1999-INDEX-AND-CLASS','scope':'Actual index-set and class identity, conditional on the retained rational Euler-system hypotheses.'}
    if key=='T033':c['current_supplier_binding']={'application_id':'CURRENT-VOIGHT-RAMIFICATION','scope':'Existence of the actual quaternion algebra; enhanced supersingular/Ribet and parametrization inputs remain separate.'}
    if key=='T043':c['current_supplier_binding']={'application_id':'CURRENT-VOIGHT-EMBEDDING','scope':'Rational embedding criterion only; local orientation count is the displayed argument.'}
    if key in ('T044','T045'):c['current_supplier_binding']={'use_id':cj['use']['id'],'scope':'Fixed-type conductor-one reduction only; opposite Frobenius orientation and mass factor are separate current arguments.'}
    components.append(c)
    pending.extend({'theta_use':u['id'],'historical_id':h['id'],'title':h['title'],'source_locator':h['source_locator'],'needed_source_binding':'Reuse accepted source-version/application record; do not infer acceptance from this identifier.'} for h in c['retained_separate_inputs'])
    checks.append({'id':row['use_id'],'current_locations':len(places),'raw_locations_match':True,'classification':u['classification']})
write('COMPONENTS.json',components)
write('SOURCE-ANCESTRY.json',pending)
write('CHECKS.json',{'scope':'Exact current passage identities and canonical use digests; not semantic acceptance','rows':checks,'components':len(components),'connections':sum('connection'in c for c in components),'all_use_digests_match':all(digest(c['use'])==c['connection']['use_sha256'] for c in components if 'connection'in c)})
write('PROVENANCE.json',{'author':'/root/v14_sign_conductor','current_source_sha256':sha(raw),'read_scope':'Current main13242–17487, full mathematical clauses and immediate proof contexts; exact earlier source-family reconciliation reused without changing its historical statuses.','reconciliation':{'path':str(source.relative_to(ROOT)).replace('\\','/'),'sha256':sha(source.read_bytes())},'bounds':'69 unchanged incoming clauses and3explicit current replacements; no old full-orientation bijection resurrected. Two scope summaries are background. Source ancestry is explicit and not automatically certified by an inline connection.','current_cj_component_sha256':sha((RISK/'v14-main-active-connections-author-001/CJ-COMPONENT.json').read_bytes()),'status':'Author proposal; no final coverage or source-first approval.'})
write('MANIFEST.json',{'files':{p.name:{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}})
print(sha((OUT/'MANIFEST.json').read_bytes()))
