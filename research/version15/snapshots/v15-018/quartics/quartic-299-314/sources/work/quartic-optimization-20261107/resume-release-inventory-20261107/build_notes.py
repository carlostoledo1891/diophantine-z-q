"""Read-only source comparison; writes preparatory notes only beside this file.

Does not execute candidate code, grant acceptance, or edit release inventories.
"""
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
WORK=ROOT/'work'
REPO=WORK/'quartic-version6-release/repository'
U='work/quartic-under300-20261107/'
O='work/quartic-optimization-20261107/'
R='work/quartic-version6-release/repository/'
pins={}
frozen=HERE/'SOURCE-PINS.json'
if frozen.exists():
    for path,meta in json.loads(frozen.read_bytes()).items():
        # STATUS is a navigation index, not an acceptance authority.
        if path.endswith('/STATUS.json'):continue
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==meta['sha256'],('Frozen input changed',path)
def pin(path):
    p=ROOT/path;raw=p.read_bytes();sha=hashlib.sha256(raw).hexdigest()
    pins[path]={'sha256':sha,'bytes':len(raw)}
    return {'path':path,'sha256':sha}
def obj(path):
    pin(path);return json.loads((ROOT/path).read_bytes())
def span(path,heading):
    info=pin(path); lines=(ROOT/path).read_text(encoding='utf-8-sig').splitlines()
    at=[i for i,s in enumerate(lines) if s==heading]
    assert len(at)==1,(path,heading)
    start=at[0];end=next((i for i in range(start+1,len(lines)) if lines[i].startswith('## ')),len(lines))
    return {**info,'heading':heading,'startLine':start+1,'endLine':end}
def write(name,value):
    (HERE/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

specs=[
('published394',R+'quartics/quartic-394-411/candidate394-ir.json',R+'docs/manuscript-revisions/version13/GUIDE.md',R+'quartics/quartic-394-411/reviews/mathematical-review.md','published','/root/astra_quartic_opt10_combination','/root/astra_quartic_opt03_depth',None),
('kummer392t',U+'03-depth/candidate392t-ir.json',U+'03-depth/REPORT392t.md',U+'01-elimination/review392t/REVIEW.md','accepted_component','/root/astra_quartic_opt03_depth','/root/astra_quartic_opt01_elimination','published394'),
('squaredH390',U+'01-elimination/squared-h/candidate390-ir.json',U+'01-elimination/squared-h/REPORT.md',U+'03-depth/review390/REVIEW.md','accepted_component','/root/astra_quartic_opt01_elimination','/root/astra_quartic_opt03_depth','kummer392t'),
('contact372',U+'10-combination/unweighted372/candidate372-ir.json',U+'10-combination/unweighted372/REPORT.md',U+'01-elimination/review372/REVIEW.md','accepted_component','/root/astra_quartic_opt10_combination','/root/astra_quartic_opt01_elimination','squaredH390'),
('guards369',U+'10-combination/candidate369-ir.json',U+'10-combination/REPORT369.md',U+'01-elimination/review369/REVIEW.md','accepted_component','/root/astra_quartic_opt10_combination','/root/astra_quartic_opt01_elimination','contact372'),
('Sparity366',U+'01-elimination/s-odd366/candidate366-ir.json',U+'01-elimination/s-odd366/REPORT.md',U+'03-depth/review366/REVIEW.md','accepted_component','/root/astra_quartic_opt01_elimination','/root/astra_quartic_opt03_depth','guards369'),
('four332',O+'resume-depth-20261107/four-groups/candidate332-ir.json',O+'resume-depth-20261107/four-groups/REPORT.md',O+'resume-review332-20261107/REVIEW.md','accepted_component','/root/astra_quartic_opt03_depth','/root/astra_quartic_opt05_anchor','Sparity366'),
('strong330',O+'resume-depth-20261107/strong-h330/candidate330-ir.json',O+'resume-depth-20261107/strong-h330/REPORT.md',O+'resume-sol-review330-20261107/REVIEW.md','accepted_component','/root/astra_quartic_opt03_depth','/root/sol_protocol_final_review','four332'),
('chain327',O+'resume-depth-20261107/chain327/candidate327-ir.json',O+'resume-depth-20261107/chain327/REPORT.md',O+'resume-sol-review327-20261107/REVIEW.md','accepted_component','/root/astra_quartic_opt03_depth','/root/sol_protocol_final_review','strong330'),
('three326',O+'resume-depth-20261107/three326/candidate326-ir.json',O+'resume-depth-20261107/three326/REPORT.md',O+'resume-sol-review326-20261107/REVIEW.md','accepted_component','/root/astra_quartic_opt03_depth','/root/sol_protocol_final_review','chain327'),
('abscissa359',O+'resume-elimination-20261107/abscissa359/candidate359-ir.json',O+'resume-elimination-20261107/abscissa359/REPORT.md',O+'resume-review359-20261107/REVIEW.md','accepted_component','/root/astra_quartic_opt01_elimination','/root/astra_bl_horizontal_repair','Sparity366'),
('combined320',U+'10-combination/combined320/candidate320-ir.json',U+'10-combination/combined320/REPORT.md',O+'resume-sol-review320-20261107/REVIEW.md','accepted_composition','/root/astra_quartic_opt10_combination','/root/sol_protocol_final_review','chain327'),
('threeAnchor319',U+'10-combination/three-anchor319/candidate319-ir.json',U+'10-combination/three-anchor319/REPORT.md',O+'root-review-three319/REVIEW.md','accepted_composition','/root/astra_quartic_opt10_combination','/root','three326'),
('exact319',O+'resume-elimination-20261107/exact319/candidate319-ir.json',O+'resume-elimination-20261107/exact319/REPORT.md',O+'resume-sol-review319-20261107/REVIEW.md','accepted_exact_component','/root/astra_quartic_opt01_elimination','/root/sol_protocol_final_review','combined320'),
('combined318',U+'10-combination/combined318/candidate318-ir.json',U+'10-combination/combined318/REPORT.md',None,'pending_composition_review','/root/astra_quartic_opt10_combination',None,'threeAnchor319'),
('alternative358',U+'10-combination/squared-anchor358/candidate358-ir.json',U+'10-combination/squared-anchor358/REPORT.md',O+'resume-review358-20261107/REVIEW.md','accepted_unselected_alternative','/root/astra_quartic_opt10_combination','/root/astra_bl_horizontal_repair','abscissa359'),
]
components={};irs={}
for key,ir,report,review,status,author,reviewer,source in specs:
    data=obj(ir);irs[key]=data
    components[key]={'id':key,'candidate':pin(ir),'report':pin(report),'recordedStatus':status,'componentAuthor':author,'recordedReviewer':reviewer,'review':pin(review) if review else None,'comparedWith':source,'variables':len(data['coordinates']),'residuals':len(data['residuals']),'newApprovalCreatedHere':False}
    assert len({r['id'] for r in data['residuals']})==len(data['residuals'])
    if source:
        delta={}
        for field in ('coordinates','residuals'):
            a={x['id']:x for x in irs[source][field]};b={x['id']:x for x in data[field]}
            delta[field]={'deleted':sorted(set(a)-set(b)),'added':sorted(set(b)-set(a)),'changed':sorted(i for i in set(a)&set(b) if a[i]!=b[i])}
        components[key]['objectDelta']=delta
assert components['combined318']['candidate']['sha256']=='e8f213d1470a296ea09dabaf417b6d0003215de496069518ddc64b9737746cf1'
components['combined318']['residualTransport']={'anchorDefinition':{'sourceComponent903':'target1903'},'deletedAnchorB':{'sourceComponent904':'target1904'},'unchangedDetectorRows':[903,904],'coordinateIDsUnchangedByLabelMap':True}
components['threeAnchor319']['residualTransport']={'anchorRows':{'903':1903,'904':1904},'unchangedDetectorRows':[903,904],'coordinateIDsUnchangedByLabelMap':True}

inventory_path=R+'docs/manuscript-revisions/version13/APPLICATIONS.json'
inventory=obj(inventory_path)
assert len(inventory['applications'])==39
baseline_refs={k:inventory[k] for k in ('text','baselineManuscript','existingSourceCatalog','externalSources','inheritedInventory','compatibilityInventory','explicitInheritedReferences')}
for item in (inventory['text'],inventory['baselineManuscript'],inventory['existingSourceCatalog'],inventory['inheritedInventory']):
    assert pin(R+item['path'])['sha256']==item['sha256']
baseline_refs['v13Manuscript']=pin(R+'manuscripts/quartic_v13.tex')
baseline_refs['v13Inventory']=pin(inventory_path)
baseline_refs['retentionRule']='Carry source records, exact version/errata qualifications and restricted-converse scope unchanged; no new external source or stronger theorem has been introduced by these packets.'
baseline_refs['conventions']={
 'field':'K=Q(rho), rho^2=2; E:y^2=x^3-Dx, D=11-6rho=(3-rho)^2; P=2R0, R0=(1+rho,2rho).',
 'coefficients':'F_s denotes the rational rho coefficient of f([s]P), while X_n is the rho coefficient of x([n]P). They are different functions. Physical X_A=2*v83, X_T=2*v87, X_Z=2*v89; F_s=2*g0*g1.',
 'valuations':'At consumed p>76176 use integral unramified normalization. At3 the quadratic field is inert and the curve has good reduction. At2 use v(2)=1, v(rho)=1/2 and the integral formal subgroup, not good reduction.',
 'localDomain':'The new contact argument uses required positive odd alpha=v_p(F5(A*lambda)), with1+R a unit. A radical-free detector has no asserted global trace inverse.',
 'fixedConstant':'C=3^(2^25) is a fixed integer coefficient, not a rational variable in symbolic candidates.',
 'height':'Same three positive rational square scales1,C0^2,(1+C1^2)^2, exponent19 height constant Hcal and root-height transfer Bmax^2-6<7Hcal*|N|^(19/k).',
 'logarithms':'Same rational N/Q high evaluator at order40 and same G2 shallow evaluator with actual precision12. Tests require middle order10; completeness for326 consumes the stronger actual precision12.',
 'provenance':'All author/reviewer identities here are identities recorded in the cited internal reports. No provider attestation or new independent approval is asserted.'}
write('RETAINED-SOURCES.json',baseline_refs)

lemmas=[]
def lemma(id,component,kind,headings,old,new,obligations,baseline,selected=True):
    comp=components[component]
    lemmas.append({'id':id,'component':component,'kind':kind,'selected318Dependency':selected,'oldObject':old,'newObject':new,'requiredInternalLemmaOrMap':obligations,'baselineApplications':['V13-'+x for x in baseline.split()],
      'authorProof':[span(comp['report']['path'],s) for s in headings],'recordedReview':comp['review'],'author':comp['componentAuthor'],'reviewer':comp['recordedReviewer'],'recordedStatus':comp['recordedStatus'],'newApprovalCreatedHere':False})

lemma('N01-KUMMER-AFFINE','kummer392t','exact_guarded_rational_substitution',['## Equations and meanings','## Exact reverse reconstruction','## Forward map and completeness'],
 'H x,f,S and V0 reciprocal F with scalar/primary/log consumers of S',
 'c(f+F)+Dv²+2bv=1, v=ft, F=vt; S=(b+ct+Dv)/a',
 'Nonzero f follows algebraically; restore x=1/f. Forward uses old proved c+Df nonzero; reverse identity divides only by c and f. Every outside S value is identical.',
 'H-EXACT-RESCALING SHARED-RECIPROCAL H-SUBTRACTION RECIPROCAL-IDENTITY SCALAR-NORM24')
lemma('N02-SQUARED-H-RECONSTRUCTION','squaredH390','exact_map_on_explicit_open_domain',['## Equations and exact interface','## Reconstruction on Q,U nonzero'],
 'Stored f,F with U=f²,V=F²', 'Stored W=v², UV=W², Q²=U+V+2W, t(U+W)=Qv, Q=(1-DW-2bv)/c',
 'On UQ!=0 recover f=(U+W)/Q, F=(V+W)/Q and all old values. New U=0 or Q=0 branches are not covered by the rational map and require N03.',
 'H-EXACT-RESCALING H-SUBTRACTION H-NO-ROOT')
lemma('N03-SQUARED-H-EXCEPTIONS','squaredH390','new_local_and_height_application',['## The two possible new branches are fixed','## Signed one-place argument, only on the fixed branches','## Closing the branch exclusion before H is defined'],
 'H and V0 already interpreted; detector leaves actual squares', 'Before H interpretation: U=0 gives V=1/c²; Q=0 gives U=V=-v² with v=(3+2rho)/4 or(-36+16rho)/49',
 'Prove fixed values units at every p>76176, permit only the classified negative squares, obtain no contact prime, use all three radicals1 and pre-H scalar anchor/root-height contradiction. Do not apply logarithm ratios first.',
 'V0-EXCLUSION H-TORSION-EXCLUSION H-HALF-INDEX HEIGHT HEIGHT-CONTRADICTIONS BIQUADRATIC')
lemma('N04-CONTACT-POLE-LOCAL','contact372','new_one_place_application',['## New detector and its quadratic realization','## Soundness at the required primes'],
 'Rold=F5(t)/(A^5(t-1)^6), old weighted detector/pole parameter', 'R=F5(A lambda), E=1/R; B=R/(T²(1+R)²)',
 'Use only required positive odd-contact valuations alpha>0 with1+R unit. Establish v(B)<=alpha+2Lambda and use unchanged negative-odd pole obstruction. Exact same unweighted tests/orders, no claim at arbitrary odd valuations outside required radicals.',
 'HEIGHT GROUPED-POLYNOMIALS TORIC-POWERS FACTORED-POLES PREPARATION-CONIC HEIGHT-CONTRADICTIONS')
lemma('N05-CONTACT-POLE-COMPLETE','contact372','new_ordered_completeness_application',['## Completeness and its ordering'],
 'Old delta-normalized R and original real/small-prime estimates', 'R is square multiplier of Rold; B~1/(4(A lambda)^5); E tends0 at prepared2,3,17',
 'Fix roots/scales and compact/finite neighborhoods before primes. Selected v(R)=1, other valuations even, trace a unit, B square reduced denominator; at2,3,17 preserve squareclasses and raise v(B); obtain0<B<17 with same final H.',
 'REAL-INITIAL FINITE-SUPPORT REAL-FINAL-CRT PREPARATION-ZERO FACTORED-POLES FINAL-COMPLETENESS')
lemma('N06-CONDITIONAL-GUARDS','guards369','new_domain_sensitive_soundness',['## The new interface, rather than the old normalization','## The order of the whole proof'],
 'Global inverses for Re(W)', 'Inverses deleted; establish W,Re(W),z,T nonzero only at a required contact prime',
 'At radical-free R=-1 branch no inverse restoration is asserted or needed. At required primes first prove local unique-minimum nonzero, then decode trace/B and pole. Re-run exceptional H/root-height logic on this conditional domain.',
 'V0-EXCLUSION HEIGHT-CONTRADICTIONS FACTORED-POLES PREPARATION-CONIC')
lemma('N07-S-PARITY','Sparity366','new_anchor_parity_application',[],
 'S has three private odd-norm witnesses', 'S merely a nonzero integral multiple before anchor; local3 anchor contradiction rules out even S index',
 'Use reduction of odd scalar s=index(S)-1 to f(P)=2rho and anisotropy/residue of u²-2(w+C)²+6v²=3F²-2C². No H or height hypothesis.',
 'MODEL ODD-NORM ANCHOR-COEFFICIENT ANCHOR-RESCALING')
# N07 proof heading belongs to its independent review, not its author report.
lemmas[-1]['authorProof']=[span(components['Sparity366']['report']['path'],'## 3. An even a contradicts the anchor at 3')]
lemmas[-1]['reviewProof']=[span(components['Sparity366']['review']['path'],'## The new parity argument')]
lemma('N08-S-HALF-RESTORATION','Sparity366','new_use_of_existing_half_point_and_exact_sign_map',[],
 'Private half-point coordinates supplied in S odd chart', 'Choose[index(S)]R0 after parity, align(h,j) through the whole-system S involution, then restore old half point',
 'Sign map flips5,6,7,8,25,26,27,28,55,56,57,120,121,543,544,549. It must hold on the actual target or be used only after restoring source366. The map is not arbitrary pointwise sign selection.',
 'ODD-NORM MODEL ANCHOR-RESCALING FINAL-COMPLETENESS')
lemmas[-1]['authorProof']=[span(components['Sparity366']['report']['path'],'## 4. Why a sign normalization is necessary'),span(components['Sparity366']['report']['path'],'## 5. Reverse and forward maps')]
lemmas[-1]['reviewProof']=[span(components['Sparity366']['review']['path'],'## Global sign map and half-point restoration')]
lemma('N09-PREH-VALUATION-AND-CACHE','four332','new_pre_domain_valuation_application_plus_exact_cache',
 ['## Literal realization and witness count','## Valuation facts without circular H assumptions'],
 'Square meanings used after H reconstruction; original cached w²/w⁴ evaluator values',
 'Before H meaning, U valuation in4Z and T0 in16Z generically; exceptional T0 unit; other leaves from unconditional biquadratic identities',
 'Derive curve equation from Kummer without dividing c+Df, even valuation of x from y²=x(x²-D), F via fF=v²; verify conjugated f(V)^8 cache with fixed5764801 denominator, shifted M1 square constant15321 and factor-two field conventions.',
 'BIQUADRATIC H-SUBTRACTION V0-EXCLUSION LOG-APPROX GROUPED-POLYNOMIALS')
lemmas[-1]['priorCorrectionAttribution']={
 'review':pin(U+'12-independent-next/REVIEW354.md'),
 'correctedAuthorReport':pin(U+'06-detector-next/REPORT.md'),
 'laterNonAuthorApplicationReview':pin(U+'10-combination/review-packed348/REVIEW.md'),
 'note':'The354 reviewer /root/astra_bl_synthesis identified the premature generic V0 interpretation and supplied the valuation-only correction. N09 records its current application and cache binding, not a claim that332 newly discovered that correction.'}
lemma('N10-FOUR-GROUPS','four332','new_local_packing_and_completeness',
 ['## Four exact sums','## Same-place soundness','## Ordered completeness, including every pole condition'],
 'Product of individual square tests', 'Four sums with disjoint mod16 classes, product W=G0G1G2G3',
 'Unique minimum including zero leaves, one common place from trace/pole, orders40/10 and low f>=2. OriginalPi19 supplies margins1,2,4,8. Not a bijection of old detector fibers.',
 'GROUPED-POLYNOMIALS HEIGHT LOG-TRANSFER HEIGHT-CONTRADICTIONS REAL-FINAL-CRT FINAL-COMPLETENESS')
lemma('N11-STRONG-H330','strong330','new_weight_application_and_stronger_CRT',
 ['## Changed groups and exact accounting','## Why the new local class is valid before any height conclusion','## Stronger completeness choice and its compatibility'],
 'E79 H0² and E158 H4^4', 'Move H0² into E158 multiplicity4 slot and H4² into E79 slot',
 'Force f(H)>=80. OriginalPi19 is insufficient for this particular witness construction; Pi39 gives primary depth40. Coprimalities and real-density hypotheses remain unchanged. Selected only in320 and exact319, not the final three-group route.',
 'GROUPED-POLYNOMIALS LOG-TRANSFER REAL-FINAL-CRT FINAL-COMPLETENESS',False)
lemma('N12-CHAIN327','chain327','exact_Laurent_helper_substitution',
 ['## Both maps and all nonzero domains','## Literal coordinate incidence'],
 'E3,c=R³,E38 helper slots', 'Repurposed E11,E39; keep actual E,E2,E4,E8,E19,E79,E158',
 'ER=1 globally supplies both denominators; unique exact exponent values. No new arithmetic theorem or progression requirement; transports whichever selected detector values are required.',
 'TORIC-POWERS CONSTANT-PIVOT SOS-FINITE')
lemma('N13-THREE326-LOCAL','three326','new_three_group_one_place_application',
 ['## The new sums','## Local residue argument, before H and the integer labels'],
 'Four groups of330/327', 'Three mixed groups with E157, E158, E79, E39, E8, E4, E and shared fourth/eighth powers',
 'Disjoint residue classes per group modulo16, zero leaves omitted, common-place trace bound. H1..H4>=40,H0>=40,M0,M1>=10,f(U2)>=40, other low f>=2. Before H use N09 and fixed-unit exceptions. Decode B only at required radical primes.',
 'GROUPED-POLYNOMIALS BIQUADRATIC HEIGHT LOG-TRANSFER V0-EXCLUSION HEIGHT-CONTRADICTIONS')
lemma('N14-THREE326-COMPLETE','three326','new_application_of_original_CRT_and_actual_mixed_precisions',
 ['## Completeness with the original progression'],
 'Strong330/327 particularPi39 witnesses', 'Return to originalPi19 construction; primary depth20, f>=40, primary-ratio precision80, V1 G2 precision12, other rational log precision40',
 'Rebuild witnesses from source, not merely weaken a fixedPi39 witness. Actual M0>=12 and M1>=80 supply margins G0[2,3,9,8,12],G1[2,1,8,4,79],G2[2,281,8,3,156,159]. E weights now include1; enlarge small-prime divisibility before primes; same compact real neighborhood and0<B<17.',
 'LOG-APPROX LOG-TRANSFER REAL-INITIAL FINITE-SUPPORT REAL-FINAL-CRT PREPARATION-ZERO FINAL-COMPLETENESS')
lemma('N15-ABSCISSA-COEFFICIENTS','abscissa359','new_local_coefficient_lemmas',
 ['## Uniform abscissa valuation before parity'],
 'Coefficient lemma for F_n=f1([n]P), mainly used for scalar anchor', 'X_n=rho coefficient of x([n]P): v3=0 for odd n; -2-2v3(n) for even nonzero n; v2=-1 for odd n',
 'All nonzero positive/negative n. Use actual z([2m]P) leading residue, Laurent x=z^-2+O(z²); at2 use integral formal subgroup with normalized v(2)=1,v(rho)=1/2, not good reduction at2.',
 'MODEL ODD-NORM ANCHOR-COEFFICIENT')
lemma('N16-SHIFTED-ANCHOR359','abscissa359','changed_universal_quaternion_application',
 ['## Exact delta','## Reverse map','## Forward map'],
 'Quaternion parameter F_s/C and separate A,T,Z odd-norm witnesses', 't=F_s/C+Qroots, Qroots=12(XA²+XT²)+108XZ²; physicalq=48v83²+48v87²+432v89²',
 't rational including0; same criterion integral at2 and3. Classes2Z,1+4Z,3+4Z forbid cancellation and recover scalar integrality plus root oddness before H/height. Separate2-adic lemma supplies forward Qroots integrality. Restore old private anchor by same criterion, not by fixed-witness equality.',
 'ODD-NORM ANCHOR-RESCALING ANCHOR-COEFFICIENT HEIGHT HEIGHT-CONTRADICTIONS FINAL-COMPLETENESS')
lemma('N17-ROOT-SIGN-RESTORATION','abscissa359','new_application_of_existing_half_points_and_full_sign_maps',
 ['## Reverse map'],
 'A,T,Z supplied with private half-chart coordinates', 'Delete nine witnesses; reconstruct half points afterN16, using whole-system A/T/Z sign maps',
 'A flips1,2,3,4,21,22,23,24,112,113; T flips9,10,11,12,29,30,31,32,128,129; Z flips13,14,15,16,33,34,35,36,136,137. Check every final row or restore reviewed source first. Physical roots, abscissae, Qroots, B remain fixed.',
 'MODEL ODD-NORM BIQUADRATIC FINAL-COMPLETENESS')
lemma('N18-EXACT-UNSCALING','exact319','exact_guarded_private_polynomial_bijection',
 ['## Literal source block','## Forward and reverse maps'],
 'Q=q,B=2g1+C Q tau, scaled private U,V,W', 'T=2g0g1+Cq; u=g0U,v=g0V,w=g0W; deleteB',
 'Retaing0tau=1. InverseQ=q,B=tauT,U=tauu,V=tauv,W=tauw. Five unconditional row identities; zero private values allowed. Same quaternion parameterT/C=F_s/C+q. No new quaternion application or valuation lemma.',
 'ANCHOR-RESCALING CONSTANT-PIVOT SOS-FINITE FINITE-COUNTS ORDINARY-GATE')
lemma('N19-ALTERNATE-SQUARED358','alternative358','changed_quaternion_parameter_unselected',
 ['## Scalar facts before the anchor inference','## Recovering the old parameter and root parities','## Forward construction'],
 'F_s/C+Qroots with F_s=2g0g1', 'g1²/C+Qroots instead',
 'Requires new orbit-specific equalityv3(g1²)=v3(F_s), including odd/even s, and2-integrality ofg1 via formal subgroup. Restore old parameter by existential quaternion witnesses. This is NOT the exact unscaling map and is NOT used in318.',
 'ANCHOR-COEFFICIENT ANCHOR-RESCALING ODD-NORM FINAL-COMPLETENESS',False)

coverage={
'MODEL':('changed_application',['N07-S-PARITY','N15-ABSCISSA-COEFFICIENTS','N17-ROOT-SIGN-RESTORATION'],'Same global group decomposition; applies first without odd-chart witnesses, then restores parity before height.'),
'HEIGHT':('same_theorem_new_inputs',['N03-SQUARED-H-EXCEPTIONS','N04-CONTACT-POLE-LOCAL','N13-THREE326-LOCAL','N16-SHIFTED-ANCHOR359'],'Same three scales and exponent19 constant; renewed root oddness and local divisibilities are prerequisites.'),
'LOG-APPROX':('same_formula_new_consumer_binding',['N09-PREH-VALUATION-AND-CACHE','N14-THREE326-COMPLETE'],'RationalN/Q and G2 unchanged; retain zeros, denominator proofs and precision40/12.326 explicitly consumes actual12 onM0.'),
'LOG-TRANSFER':('same_theorem_new_local_inputs',['N13-THREE326-LOCAL','N14-THREE326-COMPLETE'],'Same relative-to-absolute integrality transfer after restored point domains; no order40 assertion forG2.'),
'ODD-NORM':('replacement_application',['N07-S-PARITY','N08-S-HALF-RESTORATION','N15-ABSCISSA-COEFFICIENTS','N16-SHIFTED-ANCHOR359','N17-ROOT-SIGN-RESTORATION'],'All four private root odd charts disappear through two separate parity proofs; old norm lemma remains the restoration target.'),
'SHARED-RECIPROCAL':('exact_representation_transport',['N01-KUMMER-AFFINE'],'Retained scalar/primary quotient meanings restored under affineS substitution.'),
'IDENTITY-CHARTS':('retained_domain_after_new_entry_proof',['N02-SQUARED-H-RECONSTRUCTION','N03-SQUARED-H-EXCEPTIONS'],'Ui,Vi identity tolerance unchanged; added squared-H branches must be excluded before old interpretation.'),
'V0-EXCLUSION':('changed_application',['N03-SQUARED-H-EXCEPTIONS','N06-CONDITIONAL-GUARDS','N09-PREH-VALUATION-AND-CACHE','N13-THREE326-LOCAL'],'Same fixed-unit contradiction now uses new conditional three-group detector.'),
'BIQUADRATIC':('unchanged_identities_earlier_use',['N09-PREH-VALUATION-AND-CACHE','N17-ROOT-SIGN-RESTORATION'],'Unconditional fourth-power identities are used before H/log interpretation; preserve zero branches and all root signs.'),
'H-HALF-INDEX':('retained_after_reconstruction',['N02-SQUARED-H-RECONSTRUCTION','N03-SQUARED-H-EXCEPTIONS'],'Old half-index theorem is unchanged, applied only after genericH reconstruction.'),
'H-TORSION-EXCLUSION':('retained_after_new_domain_proof',['N03-SQUARED-H-EXCEPTIONS','N13-THREE326-LOCAL'],'Retain old exclusions; newU=0/Q=0 branch argument precedes them.'),
'H-SUBTRACTION':('exact_representation_and_preH_use',['N01-KUMMER-AFFINE','N02-SQUARED-H-RECONSTRUCTION','N09-PREH-VALUATION-AND-CACHE'],'Old reciprocal identity restored. Pre-H curve identity must not dividec+Df.'),
'H-NO-ROOT':('retained_after_reconstruction',['N01-KUMMER-AFFINE','N02-SQUARED-H-RECONSTRUCTION','N03-SQUARED-H-EXCEPTIONS'],'Existing modular no-root certificates unchanged; do not use their late hypotheses to assume new generic branch.'),
'H-LOG-IDENTITIES':('retained_after_reconstruction',['N03-SQUARED-H-EXCEPTIONS','N13-THREE326-LOCAL'],'Same zero-tolerant log/unit identities; restored H and renewedlocalorders supply domains.'),
'INPUT-PARITY':('retained_after_new_inputs',['N13-THREE326-LOCAL'],'Same beta=51(2X+1)^2+2504 and final parity bridge.'),
'INPUT-LOCAL-ONE-CHOICE':('unchanged_historical_bridge',[],'Historical intermediate correction choice remains historical; selected final scalar correction is unchanged.'),
'DETERMINISTIC-CORRECTION':('unchanged',[],'Same scalar correction constants and finite support.'),
'SCALAR-NORM24':('same_arithmetic_exact_H_transport',['N01-KUMMER-AFFINE','N02-SQUARED-H-RECONSTRUCTION'],'Actual scalar exponent24 and norm formulas unchanged; U=fH² and S restored exactly.'),
'SCALAR-TORSION-LOG':('unchanged_after_scalar_point_restoration',['N07-S-PARITY'],'Same two scalar branches and depth24 proof; no exact-valuation357 premise.'),
'SCALAR-HEIGHT':('same_theorem_new_anchor_entry',['N16-SHIFTED-ANCHOR359'],'Same scalar upper bound; old lower-bound anchor restored independently beforehand.'),
'ANCHOR-COEFFICIENT':('same_scalar_lemma_plus_new_abscissa_applications',['N07-S-PARITY','N15-ABSCISSA-COEFFICIENTS','N16-SHIFTED-ANCHOR359'],'Original even-indexF coefficient theorem retained.359 addsX coefficients and odd-s case;358extra g1 facts excluded fromselected318.'),
'HEIGHT-CONTRADICTIONS':('same_bounds_new_verified_premises',['N03-SQUARED-H-EXCEPTIONS','N13-THREE326-LOCAL','N16-SHIFTED-ANCHOR359'],'All-radicals1 contradiction precedesH; laterLucas/input height arguments keeporders40/10 and Hcal.'),
'GROUPED-POLYNOMIALS':('replaced_detector_application',['N09-PREH-VALUATION-AND-CACHE','N10-FOUR-GROUPS','N13-THREE326-LOCAL'],'Finalselected route hasthree mixed-residue sums, not oldgrouped product polynomial.'),
'TORIC-POWERS':('exact_changed_parameter_and_helpers',['N04-CONTACT-POLE-LOCAL','N12-CHAIN327','N13-THREE326-LOCAL'],'ER=1, E11/E39 helpers andE157=R E158. Historicalslot namesE38/c cannot be reused semantically.'),
'CONSTANT-PIVOT':('same_algebra_new_finite_binding',['N12-CHAIN327','N18-EXACT-UNSCALING'],'Generic exact-elimination principle unchanged; new rowlabel collisions need explicit transport.'),
'FACTORED-POLES':('same_certificate_new_B_domain',['N04-CONTACT-POLE-LOCAL','N05-CONTACT-POLE-COMPLETE','N06-CONDITIONAL-GUARDS'],'Same normalized/factored map includingzero privatefactors; detectorB changed, scalarB notchanged.'),
'PREPARATION-CONIC':('same_obstruction_new_parameter',['N04-CONTACT-POLE-LOCAL','N06-CONDITIONAL-GUARDS'],'Use same negative-odd obstruction afterB!=0 is established atrequiredcontact.'),
'REAL-INITIAL':('same_theorem_new_uniform_bounds',['N05-CONTACT-POLE-COMPLETE','N14-THREE326-COMPLETE'],'Same initialH/scalar choices; new finite powers bounded on fixedneighborhood.'),
'FINITE-SUPPORT':('same_theorem_new_depth_budget',['N05-CONTACT-POLE-COMPLETE','N14-THREE326-COMPLETE'],'Increase free denominator divisibility ifneededbeforecontactprimes, not anindependentlatechoice.'),
'REAL-FINAL-CRT':('changed_application_branch_specific',['N05-CONTACT-POLE-COMPLETE','N11-STRONG-H330','N14-THREE326-COMPLETE'],'320/exact319 usePi39; threeAnchor319/pending318 useoriginalPi19 withactualG2precision12.'),
'PREPARATION-ZERO':('same_theorem_new_detector_inputs',['N05-CONTACT-POLE-COMPLETE','N14-THREE326-COMPLETE'],'NewdetectorB has0<B<17,squarereduceddenominator,2/3/17squareclassesanddepths; scalarpreparedB unchanged.'),
'NORMALIZED-SCALAR-POLE':('unchanged',[],'Scalar normalized pole equations and their zero cases unchanged.'),
'ANCHOR-RESCALING':('changed_parameter_then_exact_private_map',['N16-SHIFTED-ANCHOR359','N18-EXACT-UNSCALING'],'359 changes quaternionparameter; exact319/318retainthatparameter while undoingprivateg0scaling.'),
'ORDINARY-GATE':('new_artifact_required_not_accepted',['N18-EXACT-UNSCALING'],'Old394-to411 companion nottransportedautomatically. NewunscaledT usesC*q; a storedq gate neededwhenCbecomesvariable. No finalordinarytable.'),
'FINAL-COMPLETENESS':('new_composition_binding',['N05-CONTACT-POLE-COMPLETE','N14-THREE326-COMPLETE','N16-SHIFTED-ANCHOR359','N18-EXACT-UNSCALING'],'Choosepoint/detectorwitnessesfirst, privatequaternionwitnesseslast, exactunscalinglast.318stillpending.'),
'SOS-FINITE':('same_principle_new_artifacts',['N18-EXACT-UNSCALING'],'NeednewfullSOS,uniqueIDtransport,compactmapsandcoefficient-specializationchecks.'),
'FINITE-COUNTS':('new_finite_binding',['N18-EXACT-UNSCALING'],'318has5676actualmonomialsbut5679coefficient-powerentries; max186624*C²+64. Not old16C².'),
'RECIPROCAL-IDENTITY':('same_identity_new_coordinate_binding',['N01-KUMMER-AFFINE'],'Inheritedscalarandpointidentityretained; HsemanticSreadthroughaffineformula.'),
'H-EXACT-RESCALING':('additional_exact_maps_and_branch_exclusion',['N01-KUMMER-AFFINE','N02-SQUARED-H-RECONSTRUCTION','N03-SQUARED-H-EXCEPTIONS'],'The earlier exactHrescaling is followed byKummerandsquared-Hchanges; preserveitsunderlyingmeaningsafterreconstruction.'),
}
rows=[]
for app in inventory['applications']:
    short=app['id'][4:];status,ids,note=coverage.pop(short)
    rows.append({'id':app['id'],'baselineRecordSha256Canonical':hashlib.sha256(json.dumps(app,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest(),
      'baselineSource':app['source'],'baselineConsumers':app['consumers'],'deltaClassification':status,'newEntryIds':ids,'releaseNote':note,'newApprovalCreatedHere':False})
assert not coverage
assert all(x in {l['id'] for l in lemmas} for r in rows for x in r['newEntryIds'])
write('APPLICATION-DELTA.json',{'schema':'preparatory-release-delta/1','status':'Notes only; not a production inventory or new acceptance','baselineInventory':pin(inventory_path),'baselineApplicationCount':len(rows),'applications':rows,'newInternalEntries':lemmas})
write('CANDIDATES.json',{'status':'Recorded source statuses, not new approvals','components':components,'selectedPendingLineage':['published394','kummer392t','squaredH390','contact372','guards369','Sparity366','three326','abscissa359','threeAnchor319','combined318'],
 'soundnessOrderForPending318':['Invert the exact private unscaling using retained g0*tau=1 to recover threeAnchor319.','Use359 on the still merely integral root indices: separate the three valuation classes, recover root oddness and the original scalar anchor, and apply the A/T/Z sign maps to restore326.','Only on restored326 invoke its inherited366 S-parity/S-sign restoration and its pre-H detector argument. Do not apply the S sign map directly to the shifted B equation.','Exclude squared-H branches before interpreting logarithms; then apply the unchanged local comparisons and height/input arguments.'],
 'completenessOrderForPending318':['Construct326 witnesses using originalPi19 and actualG2 precision12.','Apply359 forward map, choosing only private quaternion witnesses after the root/scalar data are fixed.','Apply the exact private unscaling last; all nonprivate values stay fixed.'],
 'twoDistinct319s':{'threeAnchor319':'three-group326 plus359, originalPi19','exact319':'private unscaling ofcombined320, strongfour-groupPi39'},
 'noAutomaticAdditivity':['positive365 vsparity359','alternative358 vsexactunscaling','four/threegroupcounts','ordinary379 vsanycurrentanchor']})

adverse=[
 (U+'06-detector-next/REPORT-initial-da55ccd2.md','Superseded initial pre-H valuation argument. Preserve with later corrected proof; do not present correction as unchanged original evidence.'),
 (U+'12-independent-next/REVIEW354.md','Accepted corrected354; explicitly credits its reviewer with the pre-H valuation repair. Preserve that contribution and the later independent application review, not just the final PASS.'),
 (O+'resume-elimination-20261107/after359/CONDITIONAL357.md','Unresolved exact-valuation completeness modulus; not used.'),
 (O+'resume-elimination-20261107/REPORT.md','Earlier362 inverse-coefficient anchor;359 replaces it, savings are not additive.'),
 (U+'11-anchor-next/REPORT.md','Accepted positive365 alternative; not current quaternion-parameter route.'),
 (O+'resume-anchor-20261107/REPORT.md','Separate bounded-decimal379 component; its positive-anchor hypotheses cannot be silently imported.'),
 (O+'resume-logarithms-20261107/REPORT.md','No saving; fixed-interface algebraic obstruction, not newlogarithmapproximant.'),
 (O+'resume-fixed-v0-20261107/REPORT.md','No saving; finite-field probe and lost-normalization counterexample are not adopted mathematics.'),
 (U+'10-combination/SEARCH-NOTES.md','Failed cubic/contactsign, primarytestdeletion, oddrootdeletion andtwointegerLucasroutes.'),
 (U+'10-combination/order39/REPORT.md','Unselected order39 alternative requires a larger anchor and a fresh complete artifact/application review; current selected route keeps order40.'),
]
write('PRESERVED-ALTERNATIVES.json',[{'source':pin(p),'disposition':why} for p,why in adverse])
pin(U+'10-combination/STATUS.json')
source_status=(ROOT/(U+'10-combination/STATUS.json')).read_bytes()
(HERE/'STATUS-SNAPSHOT.json').write_bytes(source_status)
write('SOURCE-PINS.json',pins)
summary=['# Coverage of the published39 applications','',
 'This is an index into APPLICATION-DELTA.json, not an approval record. Original source and consumer spans are retained verbatim there.','',
 '| Published application | Classification | New entry references |','|---|---|---|']
for row in rows:summary.append('| '+row['id']+' | '+row['deltaClassification']+' | '+', '.join(row['newEntryIds'])+' |')
(HERE/'BASELINE-COVERAGE.md').write_text('\n'.join(summary)+'\n',encoding='utf-8')
print(json.dumps({'components':len(components),'baselineApplications':len(rows),'newInternalEntries':len(lemmas),'sourceFiles':len(pins),'pending318RemainsPending':components['combined318']['recordedStatus']=='pending_composition_review'},indent=2))
