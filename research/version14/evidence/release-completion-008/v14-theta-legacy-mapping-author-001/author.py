import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent;R=ROOT/'work/source-risk-review-20261107'
def sha(b):return hashlib.sha256(b).hexdigest()
def digest(o):return sha(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
legacy_path=R/'v14-active-closure-map-004/ROWS.json';theta_path=R/'v14-theta-active-author-003/COMPONENTS.json'
legacy={r['id']:r for r in json.loads(legacy_path.read_bytes())};theta={c['use']['id']:c for c in json.loads(theta_path.read_bytes())}
# This is a clause map, not a declaration that every historical requirement
# is discharged by the selected theta clauses.
specs=[
(53,[2,14,19,20,22],'Common retained scalar, uniform clearing, and conditional central calibration, in the order preceding odd normalization.','The earlier global even upper-bound construction is not inferred merely from the scalar construction.'),
(54,[3,4,5,6,7,8,9,12],'Original lattice and smoothers; integral j-star/Mackey and primitive descent; exact good Euler factor, local constancy and discriminant basis.','Source inputs remain those explicitly retained by the accepted current clauses.'),
(55,[15,16,17,18,19,20,21,22],'Real cyclotomic residual dimensions and signatures, rank-two cancellation, nonsaturated real lattice, wedge factor, coefficientwise clearing and exact local terms.','No imaginary-field shortcut replaces the real cyclotomic construction.'),
(56,[29,56,57],'Sequential signed nonvanishing and one-prime plus four-prime construction, including finite avoidance and actual twist.','Root-number formulas and the prime realization input remain separate named prerequisites.'),
(57,[66,67,68],'Separate projections and preserved odd minimum, followed by the actual graph/network construction and simultaneous address degree bounds.','The earlier universal type alphabet, one-free-bit specification and neutral-primary construction require their own graph-source bindings; these are not established solely by these theta paragraphs.'),
(58,[27,28,46,60,61,69],'Phase control, coefficient visibility, bounded-below attained odd depth, finite-budget divisions and selection of one actual stage.','The even lower bound and earlier abstract depth/omission interface are separate inputs.'),
(59,[28,47,48,49,50,51,52,53,54],'Integral recurrence and level operations, integer divisions before reduction, fresh copies, determinant contraction and local trace identity.','Retain the actual block construction and simultaneous Chebotarev inputs; finite-budget and nonempty-output conditions are not removed.'),
(60,[50,66,67,69],'Fresh-copy invariance and actual-stage graph realization keep old data and separate projection constraints.','The general prime realization theorem for every compatible type and external incidence pattern is a separate supplier, not proved by this mapping.'),
(61,[60,67,68],'Attained odd minimum and network/degree construction on retained nonempty graphs.','The earlier abstract minimum-seed, forest-derivative and empty-unit combinatorial lemmas require their own current graph-source binding.'),
(62,[61,67,68,69],'Finite budget, network minors and simultaneous degree choices, then actual stage before prime realization.','The earlier grounded/variable-terminal abstract network interface and polynomial-ring argument remain separate where not repeated in the cited current clauses.'),
(63,[14,19,20,22,56,57,58],'Retained even scalar/calibration and application of the stationary upper bound in the companion construction.','The earlier full stationary-cube upper-bound proof is an incoming supplier; its conclusion is not reproved by the theta application.'),
(64,[56,57,58],'Finite preparation, dummy vertices, actual auxiliary twist and bounded-support companion with stationary upper valuation.','General prime realization and the stationary bound retain their separately named proofs; no prime-size bound follows.'),
(65,[59],'Two unaveraged height descriptions, actual native free-line indices and comparison for already known simple-zero twists.','CST formulas, norm/index inputs and the companion estimate remain explicit prerequisites; no simple-zero conclusion is assumed for an unknown parameter.'),
(66,[29,30,31,32],'Fixed witness, unaveraged genus point and torsion annihilation, Kummer translation and compatible finite-field detector.','The general open-image and finite Chebotarev imported statements need their own source joins; this mapping does not replace them.'),
(67,[33,34,35,36,37,38,39,40,41,42,43,44,45,46,59,60,61],'Current weighted theta construction, fixed-type conductor-one image, opposite orientation, mass, same-place finite sum, visibility and finite-budget odd depth.','Historical unrestricted orientation-image wording is superseded by current T033/T044/T045. Only the corrected fixed-type statement is selected; all external inputs remain explicit.'),
(68,[23,24,25,26,27,28,47,48,49,50,51,52,53,54],'Full eigenspace and scalar local projection, flat field descent, rational phase, shell recurrence, fresh trace and conductor-one local identity.','Waldspurger, Ramsey, Weil, Carayol and Casselman inputs have distinct accepted source wrappers; simultaneous Chebotarev and block construction remain separate.'),
(69,[46,60,62,66,69,70],'Empty-unit visibility alternative, retained minima under independent projections, fixed quadratic field and actual final-stage use.','The earlier rationalized sum/difference Selmer comparison and fresh-field independence construction remain separate suppliers if not included in their current RC bindings.'),
(70,[63,64],'All-index convolution extends the assumed congruence off the filter; the family-specific split-cubic halving argument forces 2-primary order four and contradicts divisibility eight.','The compatible prime realization and standard halving criterion are retained inputs; this is not a universal elliptic-curve assertion.')]
rows=[]
for number,targets,matched,limits in specs:
 ident='HIST-arithmetic-AR-U'+str(number).zfill(3);old=legacy[ident];links=[]
 for t in targets:
  c=theta['ACTIVE-THETA-T'+str(t).zfill(3)]
  assert c['connection']['use_sha256']==digest(c['use'])
  links.append({'use_id':c['use']['id'],'use_sha256':digest(c['use']),'statement':c['use']['assertion']['statement'],'consumer_locations':c['connection']['consumer_locations']})
 rows.append({'id':ident,'historical_statement':old['statement'],'matched_clauses':matched,'links':links,'remaining_conditions_or_unmapped_suppliers':limits,'disposition':'partial explicit clause mapping; no whole-ancestry closure'})
result={'author':'/root/v14_sign_conductor','status':'author proposal pending independent clause review','inputs':[{'path':str(p.relative_to(ROOT)).replace('\\','/'),'sha256':sha(p.read_bytes())} for p in [legacy_path,theta_path]],'rows':rows,'invariants':['No accepted component bytes change.','Every linked use has the same current main consumer and an exact canonical use hash.','Historical observations are not new dependencies.','Unmapped earlier graph/prime/RC suppliers remain explicit and must be joined separately.']}
(OUT/'COMPARISON.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
(OUT/'MANIFEST.json').write_text(json.dumps({'files':{p.name:{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}},indent=2)+'\n',encoding='utf8')
print(sha((OUT/'MANIFEST.json').read_bytes()))
