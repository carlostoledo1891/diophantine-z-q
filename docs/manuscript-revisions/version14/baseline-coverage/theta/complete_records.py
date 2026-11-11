from pathlib import Path
import json,hashlib,re
H=Path(__file__).resolve().parent;WS=H.parents[3];R=H.parents[2]/'quartic-version6-release/repository'
def sha(b):return hashlib.sha256(b).hexdigest()
def write(name,x):(H/name).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
src=R/'manuscripts/quartic_v13.tex';data=src.read_bytes();ls=data.splitlines(keepends=True)
pdf=WS/'work/ramsey-2006.pdf';txt=WS/'work/astra-arithmetic-closure-002/ramsey-primary-full.txt'
rec=dict(id='T028-RAMSEY-6.2',source_use_id='T028',decision='accepted within stated scope: exact source formula and substitution',reviewer='/root/astra_v14_baseline_theta',source=dict(path=str(pdf),sha256=sha(pdf.read_bytes()),publication='Nick Ramsey, Geometric and p-adic Modular Forms of Half-Integral Weight, Annales de l’Institut Fourier 56(3) (2006), 599–624',locator='Theorem 6.2, printed p.615; preceding definition of T_l²; PDF page 18',text_read=dict(path=str(txt),sha256=sha(txt.read_bytes())),render_read=dict(path='ramsey-p615.png',sha256=sha((H/'ramsey-p615.png').read_bytes()))),consumer=dict(path=str(src),lines=[13678,13721],sha256=sha(b''.join(ls[13677:13721]))),old_inventory_match='A031 source family has algebraic-model locators only; this is a new exact source/occurrence link, not a manuscript repair.',obligations={
'source_hypotheses':'Theorem 6.2 requires F in M_(k/2)(4N,R,chi), a prime l not dividing 4N, and 4Nl invertible in R. Take k=3, characteristic-zero coefficient field, l=p outside actual level support S1.',
'constructed_objects':'The actual sieved algebraic even form of ex:app-even-phase, with scalar character psi and good eigenvalue eta(p)a_p(E).',
'domain_and_index_coverage':'The theorem gives every Fourier index n. It includes the Legendre value zero when p divides n; a_(n/p²) is zero for a nonintegral index. No squarefree restriction.',
'transition_and_comparison_maps':'Use the source normalized Hecke operator l^-2 pi1_*(pi2^*F times Theta_(l²)^k). Its theorem explicitly identifies this with the classical Fourier operator. No use of its bad-prime U_l or Gauss normalization.',
'consumed_object_identity':'The source q-expansion belongs to T_(p²) of the same F. Good-Hecke eigenspace and commuting sieve give T_(p²)F=eta(p)a_p(E)F. Rearranging the coefficient equality gives E.12 for the same a(n).',
'coefficient_and_normalization':'At k=3 the source l^((k-1)/2-1)=1 and (-1/l)^((k-1)/2)(n/l)=(-n/l). The last coefficient is p psi(p²)=p eta(p)². No conjugation or absolute square.',
'local_conditions':'p avoids S1=S0 union B; no condition at bad or dyadic primes is inferred. The ring is a field of characteristic zero, not a residue coefficient ring.',
'exceptional_cases':'p is odd because 2 divides the level. Terms for p dividing n and p² dividing n are part of the stated formula. Zero coefficients are allowed.',
'downstream_consumption':'Integer shell polynomials at13693–13721, minimum-depth coefficients, O.9/O.10 divisions, and the nonempty-seed coefficient computation use this exact recurrence.'})
write('RAMSEY-HECKE-SUPPLIER.json',rec)
requests=[
('XS01',['T002','T029'],[1878,1956],'sec:rc','Fixed E, period convention, full rational two-torsion, admissible unit filters and full-corank-one assumption.'),
('XS02',['T020','T022','T030','T058','T061'],[1171,1225],'lem:forward-rank','At independently nonzero central value or known simple zero, rank and finite two-primary Sha conclusions for the actual twist; no reverse inference at unknown base.'),
('XS03',['T047','T054','T055','T066'],[2144,2304],'ex:sec7-typed-graph; ex:sec7-symbol; ex:sec7-coefficient-rules; ex:sec7-realization','Actual full-two-torsion typed graphs, symbol domain, reverse Legendre conventions, primary type, and finite compatible prime realization.'),
('XS04',['T057','T058','T066','T068'],[2305,2423],'ex:sec7-seed-partition; ex:sec7-address; ex:sec7-one-symbol-address','Definitions of partitionability, stationary versus activated terminals, nonempty contraction outputs, and address target interface. Proof supplied in assigned T066–T068.'),
('XS05',['T059','T070'],[2547,2585],'(3.4), (3.5); ex:sec7-genus-lower','Native height ratio 2j_rc−2j_gen=v2 L_*(hkprime)−v2 L_*(h*)+epsilon with |epsilon|≤2; arithmetic bound2j_rc≥4omega(h)+s(h)+s(hkprime)−C_R(E,A), uniformly for omega(kprime)≤A. These must use the same native lattices as O.8 and the final coordinate.'),
('XS06',['T070'],[4154,4326],'ex:arith-central-calibration','At known simple-zero constituents, exact central valuation of the same retained coordinate; regularity and determinant specialization including torsion/saturation and local terms.'),
('XS07',['T070'],[4327,4514],'ex:arith-common-coordinate','One integral support correction eta formed before characters, with actual Lambda-unit comparison to primitive coordinate. O-units alone do not preserve central valuation.'),
('XS08',['T070','T071'],[4515,4567],'ex:arith-base-zero','Unknown base derivative zero implies same coordinate zero, using full-corank one without assuming finite Sha at the base.'),
('XS09',['T071'],[5673,5832],'ex:limits-fixed-field-clearing','Fixed-field denominator bound c_det=a+4(h_K+2c_E+2t_K) for actual corrected coordinate, independent of binary dimension and later active primes.'),
('XS10',['T058','T071'],[5833,6060],'ex:limits-coefficient-transfer; sec:limits','Finite coefficient comparison with L_T(M)=16(d_K+5)M and b>(L_T+2)(2^M−1); produce x nonzero with v2 difference≥M−2c from f_x u_x=d_x, controlling negative f coefficients and d constant only.'),
('XS11',['T071'],[1090,1128],'hyp:RC','Restricted converse theorem statement matches simple-zero conclusion and its input assumptions; later pole/integer/compiler consumers require separate slices.'),
]
out=[]
for id,uses,(a,b),label,assertion in requests:
    out.append(dict(id=id,source_uses=uses,supplier_labels_or_equations=label,supplier_locator_window=[a,b],window_sha256=sha(b''.join(ls[a-1:b])),required_assertion=assertion,status='cross-slice integration requested; not a demonstrated unsupported inference',window_scope='Locator window for supplier and context, not a claim that this reviewer audited the whole supplying proof.'))
write('CROSS-SLICE-REQUESTS.json',out)
frozen=json.loads((H/'INITIAL-FREEZE.json').read_text());coverage=json.loads((H/'COVERAGE-INDEX.json').read_text());uses=json.loads((H/'INITIAL-SOURCE-USES.json').read_text())['uses']
assert [x['line'] for x in coverage['lines']]==list(range(12194,16545))
assert len({x['id'] for x in uses})==74
for x in uses:assert sha((H/x['excerpt_path']).read_bytes())==x['excerpt_sha256']
for x in coverage['lines']:assert sha(ls[x['line']-1])==x['line_sha256']
for name in ['INITIAL-SOURCE-USES.json','COVERAGE-INDEX.json','assigned-source.tex']:assert sha((H/name).read_bytes())==frozen[name]
write('FINAL-VALIDATION.json',dict(source_sha256=sha(data),complete_line_interval=True,unique_source_uses=74,all_passage_hashes_match=True,all_line_hashes_match=True,initial_freeze_unchanged=True,proof_truth_checked_by_script=False,warning='Only structural, identity and coverage-index consistency checks.'))
files={str(p.relative_to(H)).replace('\\','/'):sha(p.read_bytes()) for p in sorted(H.rglob('*')) if p.is_file() and p.name!='FINAL-MANIFEST.json'}
write('FINAL-MANIFEST.json',dict(algorithm='SHA-256',files=files))
print(json.dumps(dict(files=len(files),source_uses=74,covered_lines=4351,ramsey_source_sha256=rec['source']['sha256'],final_manifest_sha256=sha((H/'FINAL-MANIFEST.json').read_bytes())),indent=2))
