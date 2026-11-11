"""Build preparatory schema only; never manufacture final application records."""
from pathlib import Path
import json
from inventory_core import digest, canonical, PREFIX

H=Path(__file__).resolve().parent
ROOT=H.parents[2]
REPO=ROOT/'work/quartic-version6-release/repository'
R6=ROOT/'work/quartic-optimization-20261107/resume-release-inventory-20261107-r6'
PKG=ROOT/'work/quartic-v14-prep/quartic-299-314'
OUTPKG='quartics/quartic-299-314/'
def pin(p, target): return {'path':target, 'sha256':digest(p.read_bytes())}
def archive(name):
    return pin(R6/name, OUTPKG+'sources/'+str((R6/name).relative_to(ROOT)).replace('\\','/'))
def write(name, value):
    (H/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

baseline=REPO/'docs/manuscript-revisions/version13/APPLICATIONS.json'
assert digest(baseline.read_bytes())=='b7c4027a0f735906b4fdde129f08294871332e49f68b25d5e2fc32e9c42d9674'
assert digest((R6/'FROZEN-MANIFEST.json').read_bytes())=='207e7ca6cca93a79fabc19db02ee5c8d2a3d9370d0ec7f19d2847d3bb6e02ae7'
old=json.loads(baseline.read_bytes())
schema={
 'schema':'v14-inventory-validation-v1',
 'status':'Preparatory author schema; final application and source review required',
 'applicationIds':[a['id'] for a in old['applications']],
 'selected':{'symbolic':'reciprocal299r2','ordinary':'ordinaryReciprocal299_314'},
 'baselineInventory':pin(baseline,str(baseline.relative_to(REPO)).replace('\\','/')),
 'baselineManuscript':pin(REPO/'manuscripts/quartic_v13.tex','manuscripts/quartic_v13.tex'),
 'routeSelection':pin(H/'ROUTE-SELECTION.json',PREFIX+'evidence/route-selection.json'),
 'r6Relation':archive('CANONICAL-RELATION.json'),
 'r6Manifest':archive('FROZEN-MANIFEST.json'),
 'repairHistory':archive('REPAIR-HISTORY.json'),
 'requiredLabels':['sec:v14','thm:v14-quartic']+['subsec:v14-'+x for x in
  ['inputs','H','parity','contact','groups','reciprocal','logarithms','completeness','anchor','finite','ordinary']],
 'finalArtifacts':{}}
for n,rows,terms in [(299,279,6630),(314,294,6672)]:
    names=[f'candidate{n}-ir.json',f'polynomial{n}.json',f'coordinate-map{n}.json',
           f'compact{n}-ir.json',f'quartic-{n}-'+('symbolic' if n==299 else 'ordinary')+'-coefficients.json',
           f'quartic-{n}-'+('symbolic' if n==299 else 'ordinary')+'-coefficients.txt']
    if n==314:names+=['quartic-314-source-id-coefficients.txt']
    schema['finalArtifacts'][str(n)]={
      'variables':n,'witnesses':n-1,'residuals':rows,'monomials':terms,'degree':4,'content':1,
      'maximumCoefficient':'186624*3^(2^26)' if n==299 else '3^4098+K0',
      'coefficientQualification':'C=3^(2^25)' if n==299 else 'K0 has 1514 bits; 2^6495 <= max < 2^6496',
      'files':[pin(PKG/name,OUTPKG+name) for name in names]}
write('validation-schema.json',schema)

# These are author comparison notes, not the final 351 obligation statements.
# The actual statements, spans and independent source-first reviews remain
# mandatory inputs to install_inventory.py.
notes={
'MODEL':('The field, curve, generator, full Mordell-Weil decomposition and root squareclass calculation are unchanged.','Root labels remain odd integers after anchor restoration. Auxiliary U and V now range over all E(K); their free indices can be half-integral and their torsion must be retained until killed.'),
'HEIGHT':('The three root-abscissa scales and the inherited height inequalities remain the same.','The anchor restores nonzero odd root labels before product-height use. The all-E auxiliary extension is not an extension of the root domain.'),
'LOG-APPROX':('The same z=-x/y, f=1/x, N8/Q2 identity and coefficient denominators are retained.','Global nonvanishing of N and Q is used on all-E alternate points; a real-interval argument restricted to old square charts is insufficient.'),
'LOG-TRANSFER':('Formal logarithm additivity/isometry at odd good places and the same orders are retained.','Both auxiliary and H torsion are killed in the doubled group identities. Zero points use analytic unit A(O)=1, never division by z(O).'),
'ODD-NORM':('The old squareclass/norm criterion is retained as a source lemma.','Private root odd charts are absent. The anchor valuation proof restores root oddness before invoking old root consumers.'),
'SHARED-RECIPROCAL':('The common semantic normalizer remains -1/z(H).','Its Kummer/squared-H presentation changes. Final primary ratios include hL+fS=0 and the regular relation (1-Df²)L+hS=0; identity branches need the latter.'),
'IDENTITY-CHARTS':('The identity point is permitted for auxiliary points, and actual oriented subtraction is still required.','The chart is now h²=f-Df³. Its identity and finite two-torsion branches differ from the previous doubled-point chart and require the new all-E analysis.'),
'V0-EXCLUSION':('The root-height contradiction and explicit small exceptional points are retained.','The contradiction excluding all empty contact radicals precedes logs and omitted-ratio recovery. At the successful place the retained detector then supplies the unit denominator.'),
'BIQUADRATIC':('The old exact substitutions remain historical derivations.','The final U,V chart is no longer the biquadratic square chart. Record it as a replaced construction, not a preserved all-E parametrization.'),
'H-HALF-INDEX':('E(K)=Z R0+E[2] and 2R0=P are unchanged.','The Kummer H chart is reconstructed first. Its half-integral free index is handled together with the new half-integral auxiliary indices.'),
'H-TORSION-EXCLUSION':('The finite exceptional-set and height-anchor exclusions remain the source mechanism.','Bind them to the actual Kummer/squared-H variables and common-scale tests before using S=-1/z(H).'),
'H-SUBTRACTION':('The fixed P and V0=H-P are unchanged.','The squared-H/Kummer substitutions must reconstruct the same oriented V0, with all exceptional denominators handled before formal-log consumers.'),
'H-NO-ROOT':('The mod71 numerator and mod7 denominator nonroot certificates with split primes are unchanged.','Their consumption expands to all four alternate V_i in E(K), including the S block. Keep this new domain use explicit.'),
'H-LOG-IDENTITIES':('The H/scalar group laws and torsion exponent two are retained.','Use [2m]U_i=[2k_i]H and [2(m-2)]V_i=[2(k_i-2n_i)]V0 with k_i integral in the R0 basis. Do not copy the old torsion-free auxiliary identities.'),
'INPUT-PARITY':('The actual input polynomial beta=51(2X+1)^2+2504 and odd integral root label are unchanged.','After height equality n=beta, the same denominator/parity proof returns X integral. No half-index input polynomial is selected.'),
'INPUT-LOCAL-ONE-CHOICE':('The Q2,Q3,Q17 unit-square criteria and integer-X local values of r are unchanged.','Apply them to the retained input polynomial and same deterministic correction, not the archived 51X²+2504 alternative.'),
'DETERMINISTIC-CORRECTION':('The selected deterministic correction is c=r+4896 with the same normalization.','The newer reciprocal and anchor changes do not alter the scalar correction row or its support. The exploratory 9792 correction is not selected.'),
'SCALAR-NORM24':('The norm identity, coefficient8 and scalar order24 are retained.','The H point is reconstructed from its final chart before q=Norm(fH) and the pole ratio are interpreted. Bind actual unchanged scalar rows.'),
'SCALAR-TORSION-LOG':('The duplication argument covering scalar R near O or (0,0) is retained.','The new S-root oriented row fixes the same scalar point, and the same depth24 conclusion is used after H reconstruction.'),
'SCALAR-HEIGHT':('The exponent19/24 and the inherited scalar-height theorem remain unchanged.','The final anchor first forces sufficient scalar coefficient divisibility. Do not use the old separate scalar anchor without the new root terms.'),
'ANCHOR-COEFFICIENT':('The coefficient lemma for nonzero even scalar index remains a retained input.','The selected numerator is exactly2g0g1, not the alternate g1² route. Root-parity restoration precedes the old even-index coefficient consumer.'),
'HEIGHT-CONTRADICTIONS':('The Lucas/root height inequalities and all three scales remain unchanged.','Bind the current common-scale detector conclusions, root-parity restoration and half-index log transfer before each order40/order10 divisibility use.'),
'GROUPED-POLYNOMIALS':('The underlying test values and same-place valuation principle remain the source inputs.','The final three groups use gamma from the anchor witness, promoted first inputs and the current residue classes. Old four-group or V13 formulas are not current.'),
'TORIC-POWERS':('Exact quadratic witness substitution is the retained algebraic principle.','Current powers are the shared314 chain with the anchor-gamma313 identification. Earlier toric chain coordinates are historical ancestors only.'),
'CONSTANT-PIVOT':('Elimination by a nonzero rational constant pivot remains valid.','Only the selected finite assembly transformations and their exact current consumers are claimed; bind their actual source/target residuals.'),
'FACTORED-POLES':('The pole conic equivalence and positive semantic input are retained.','The contact-root normalization changed earlier in the selected lineage. Bind the final positive W/B interface, including zero branches and retained scalar pole.'),
'PREPARATION-CONIC':('The preparation-zero lemma and the old conic are retained as source facts.','The final scalar preparation is already specialized and normalized. No deleted private conic coordinate is asserted to survive.'),
'REAL-INITIAL':('The source real-progression open-set theorem and finite-index formal subgroups are unchanged.','Initial H0 and scalar R choices must precede fixed root data, contact primes, lambda and the final anchor witness. The later choice cannot change the anchor quadric.'),
'FINITE-SUPPORT':('The finite scalar support supp(cr) union {2,3,17} and scalar depth requirements remain.','The common gamma has additional fixed local approximation requirements at those small primes and at selected contacts. Its new support must be accounted for by the unchanged valuation argument.'),
'REAL-FINAL-CRT':('The arbitrary sufficiently divisible modulus and real open-set progression result are unchanged.','After fixed scalar/roots/anchor quadric, choose contacts and lambda, then anchor witnesses, then final H. The constructive quadric approximation is a new internal lemma, not an unproved generic weak-approximation premise.'),
'PREPARATION-ZERO':('The positive input below17, square denominator and Q2,Q3,Q17 square/depth hypotheses remain required.','The final real neighborhood and finite modulus still supply them simultaneously for the same final H. Auxiliary chart extension does not license independent local and real choices.'),
'NORMALIZED-SCALAR-POLE':('The existing normalization map and independently established positive semantic input remain unchanged.','Bind the exact final unchanged pole rows after scalar/H reconstruction; no self-contained positivity claim is made from the private pole alone.'),
'ANCHOR-RESCALING':('The earlier Laurent rescaling remains a historical exact step.','The final quadric is u²+6v²-2w²-4Cw-3T²=0, with T=2g0g1+C Q. The common scale is identified with the selected nonzero anchor witness. New local/real construction replaces the earlier private-witness choice.'),
'ORDINARY-GATE':('Repeated squaring and unique rational extension remain the algebraic mechanism.','Use14 weighted constant gates with exponents[2049]+[2048]*11+[0,0] plus one Q gate. The selected314 bound is below2^6496; the old411 chain and below2^3247 claim are not copied.'),
'FINAL-COMPLETENESS':('The same integer input construction, root labels and source simultaneous-prime/real-progression theorems remain.','The final ordering includes the fixed anchor quadric, contact/lambda choice, constructive anchor approximation and one final H. Reciprocal/oriented witnesses are then supplied for those same points, with no extra arithmetic choices.'),
'SOS-FINITE':('An unweighted sum of squares over Q vanishes exactly when all integer-normalized rows vanish.','Use the selected corrected299 and ordinary314 residuals and the explicit consecutive-coordinate bijections. A private-witness bijection is not claimed for the all-E enlargement.'),
'FINITE-COUNTS':('Exact finite expansion and coordinate bijection verification remain the method.','Selected299 has279rows/6630terms; ordinary314 has294rows/6672terms. Distinguish source-ID text222890bytes from consecutive ordinary text264430bytes and use the exact6496-bit maximum.'),
'RECIPROCAL-IDENTITY':('The old reciprocal identity is retained for the unchanged fixed-root/scalar interfaces.','The four U/V blocks now use three oriented-slope relations; alternate k is reconstructed as s(f-F)-h. Global raw-ratio recovery follows successful-place unit evidence, not bare polynomial cancellation.'),
'H-EXACT-RESCALING':('The interpretation of the common H normalizer and fixed V0 remains unchanged.','The final Kummer/squared-H presentation replaces private H square witnesses. Include the H bootstrap and nonzero/exception exclusions before the reconstruction is consumed.')}
assert len(notes)==39
plan=[]
for app in old['applications']:
    retained,changed=notes[app['id'][4:]]
    plan.append({'applicationId':app['id'],'priorRecordSha256':digest(canonical(app)),
                 'retainedDependencyJustification':retained,
                 'currentConstructionAndConsumerChanges':changed,
                 'obligationKeysRequiringFinalDecision':list(app['obligations']),
                 'status':'Author comparison notes; final 9 statements and exact spans required'})
write('BASELINE-ADAPTATION.json',{'schema':'v14-baseline-adaptation-v1','applications':plan,
 'scope':'No automatic carry-forward approval. Every obligation requires an explicit current disposition; final text and independent review are not yet bound.'})
print('Prepared schema and39 baseline comparison notes; no final records or approvals created.')
