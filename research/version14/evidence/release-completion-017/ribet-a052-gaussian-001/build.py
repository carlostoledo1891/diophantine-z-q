from pathlib import Path
import json,hashlib,difflib,datetime,re

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
BASE=ROOT/'work/source-risk-review-20261107/cj-incorporation-gaussian-002/local-only/base-fa53.tex'
PDF=ROOT/'work/source-risk-review-20261107/jk-final-access-gaussian-001/local-only/ribet1990-final.pdf'
CJ=ROOT/'work/source-risk-review-20261107/cj-conductor-one-author/PROOF.md'
def pin(p):
 b=p.read_bytes();return dict(path=p.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
def loc(p,a,b):
 return dict(**pin(p),start_line=a,end_line=b,excerpt_sha256=hashlib.sha256(b''.join(p.read_bytes().splitlines(keepends=True)[a-1:b])).hexdigest())
def put(n,x):
 p=OUT/n;assert not p.exists(),p;p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert pin(BASE)['sha256']=='fa53dcc19ad2d9efb43aa8e44fcbd514479ea216838dcbb64a4ab39fe12a67fd'
assert pin(PDF)['sha256']=='08f8ebfda40855d0f6d9e90e1dc352eb6576ecc44cc7c6e6ca3d448d724503b4'
raw=BASE.read_bytes(); lines=raw.splitlines(keepends=True)
old=b''.join(lines[14157:14168])
new=r'''Let $R$ be an Eichler order of level $N$.  Choose an enhanced
supersingular reference curve $\mathcal E_0$ with endomorphism order $R$, as in
\cite[Proposition 3.6, pp.~441--443]{ribet-geometry-1990}.
For an enhanced supersingular curve $\mathcal E$, use the right $R$-module
$\operatorname{Hom}(\mathcal E_0,\mathcal E)$ convention of
\cite[Proposition 3.3 and Remark 3.5(a), pp.~440--441]{ribet-geometry-1990}.
Writing its completed lattice as $z\widehat R$ gives
$X=B^\times\backslash\widehat B^\times/\widehat R^\times$,
with endomorphism order $R_z=B\cap z\widehat Rz^{-1}$ and automorphism
group $R_z^\times$.  Here the enhancement is the cyclic subgroup of
order $N$; arbitrary prime-power exponents, including at two, are allowed.
In the source's Section 3 setup one may choose its auxiliary prime
outside $N\ell_0$.
By \cite[Remark 3.5(b), p.~441]{ribet-geometry-1990}, Frobenius acts
on this set by right multiplication by a division uniformizer at
$\ell_0$ and by $1$ elsewhere, and this action is an involution.
Consequently every corresponding geometric coarse point is fixed by
Frobenius squared.  Its closed-point residue degree therefore divides
two, so it is a point of $X_0(N)(\mathbb F_{\ell_0^2})$.
This asserts coarse-point rationality; no chosen scalar-Frobenius
elliptic model is needed.
'''.encode()
anchor=b'\\bibitem{jetchevkane}'
bib=r'''\bibitem{ribet-geometry-1990} K. A. Ribet,
\emph{On modular representations of $\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)$
arising from modular forms}, Inventiones Mathematicae 100 (1990),
431--476, Section 3, Proposition 3.3, Remarks 3.5(a)--(b), and Proposition 3.6.
\url{https://math.berkeley.edu/~ribet/Articles/invent_100.pdf}.
\bibitem{jetchevkane}'''.encode()
edits=[('A052-geometric-consumer',old,new),('published-bibliography',anchor,bib)]
candidate=raw;records=[]
for id,o,n in edits:
 assert raw.count(o)==1
 at=raw.index(o);a=raw[:at].count(b'\n')+1
 records.append(dict(id=id,base=loc(BASE,a,a+o.count(b'\n')-(1 if o.endswith(b'\n') else 0)),old_utf8=o.decode(),new_utf8=n.decode(),old_sha256=hashlib.sha256(o).hexdigest(),new_sha256=hashlib.sha256(n).hexdigest()))
 candidate=candidate.replace(o,n,1)
target=OUT/'candidate-quartic_v14.tex';target.write_bytes(candidate)
for r,(_,o,n) in zip(records,edits):
 at=candidate.index(n);a=candidate[:at].count(b'\n')+1;r['candidate']=loc(target,a,a+n.count(b'\n')-(1 if n.endswith(b'\n') else 0))
put('EDIT-MAP.json',dict(base=pin(BASE),candidate=pin(target),edits=records,no_live_mutation=True,encoding='Unchanged raw bytes outside exact replacements; inserted fragments use LF',combination='Disjoint from CJ002 summary/table/reduction-body and its insertion before the Cornut-Jetchev bibliography entry; not automatically adopted together'))
(OUT/'candidate.diff').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(keepends=True),candidate.decode().splitlines(keepends=True),fromfile='fa53/quartic_v14.tex',tofile='A052-candidate/quartic_v14.tex')),encoding='utf-8')
def a(statement,objects,hypotheses,quantifiers,normalizations,exceptions,order):
 return dict(statement=statement,objects=objects,hypotheses=hypotheses,quantifiers=quantifiers,parameter_range='q=ell_0 odd prime; all positive N coprime to q, with arbitrary prime-power exponents including2; choose auxiliary p outside Nq.',uniformity='Exact geometric classification and actions; no asymptotic bound or discriminant size condition.',constants='No class-number or automorphism quotient factor is inserted; Frobenius has order dividing2 on the coarse set.',normalizations=normalizations,exceptional_cases=exceptions,limit_order=order)
specs=[
 ('A052-RIBET-GEOMETRY',[438,439,440,441,442,443],'Section3 setup; p439 endomorphism description; Prop3.3p440; Remark3.5(a)p441; Prop3.6pp441-443',
 a('Geometric supersingular cyclic-level pairs form B*\\Bhat*/Rhat*, with endomorphism ring R_z=B intersect zRhat z^-1 and automorphism group R_z*.','Enhanced curves E=(A,C), fixed E0, Eichler order R, right module I=Hom(E0,E), coordinate z.','Ribet Section3 hypotheses and geometric category over algebraic closure F_q; Prop3.6 realizes an initially chosen Eichler order as the reference endomorphism ring.','Every geometric enhanced pair and every reference Eichler order of the stated level.','Ihat=zRhat; rational quasi-isogeny changes z on left; integral basis changes it on right. Endomorphisms act on I on the left.','Do not divide labelled embeddings by the field normalizer; no squarefree level or scalar elliptic model is assumed.','Choose auxiliary p, then reference E0 and rational identifications, then the class-set coordinate.'),[(14158,14168)],[(18,18),(33,46)]),
 ('A052-RIBET-TATE',[440,441,442],'Prop3.3 construction p440; right-module convention Remark3.5(a)p441; order formula p442',
 a('Prime-to-q ideal quotients correspond to the same adelic lattice multiplication, with one uniform inverse ideal convention.','Enhanced prime-to-q Tate lattices, covariant q-Dieudonne convention, right Hom module, CM ideal a prime to Nq.','The quotient and its endomorphisms exist by retained good-reduction facts; source geometric/Tate classification and O action are fixed.','Every prime-to-Nq ideal representative and every prime component of the fixed reference realization.','At l!=q use usual Tate modules; at q use Ribet transpose of contravariant Dieudonne module. Quotient replaces Lambda_l by a_l^-1 Lambda_l, hence z by a^-1 z.','Do not use an etale rank-two q-adic Tate module; do not conflate a transporter with its inverse. No source claim supplies quotient-specialization existence.','Construct the ideal quotient using retained inputs, then compare its lattices in the same rational identification.'),[(14959,14989)],[(50,60)]),
 ('A052-RIBET-FROBENIUS',[441,443],'Remark3.5(b)p441; closing Prop3.6 paragraph p443',
 a('q-Frobenius on supersingular enhanced isomorphism classes is right multiplication by an idele equal to1 away fromq and a division uniformizer atq, and is an involution.','The right double class set, right ideals, local division order and geometric Frobenius twist.','Same right-module and reference-order convention as the geometric classification.','Every geometric enhanced pair, including exceptional supersingular automorphism groups.','The right ideal operation is the subideal of indexq^2; no switch to a left-module convention is made.','No identification of the two labelled inert residue embeddings is inferred from equality of coarse points.','Fix class-set convention before interpreting the right uniformizer operation and then compare the parametrization values.'),[(14183,14186),(15037,15056)],[(68,70),(83,83)]),
 ('A052-COARSE-DESCENT',[441],'Ribet Remark3.5(b) plus local proof in REPORT section Coarse rationality',
 a('Every supersingular geometric coarse modular point is F_(q^2)-rational; a parametrization overF_q sends it into E(F_(q^2)), so one lambda_M evaluates all terms.','The finite-type coarse scheme X0(N)/F_q, closed-point residue field, Frobenius orbit, rational modular parametrization.','Ribet Frobenius is involutive on its geometric supersingular point set; the parametrization extends overF_q by retained good-reduction input.','Every supersingular geometric coarse point and every corresponding parametrization value used in the finite character sum.','Closed-point degree equals Frobenius orbit length; fixed by square implies degree divides2. This is descent of a coarse scheme point.','No descent of all labelled moduli objects, isogenies or embeddings; no scalar-Frobenius elliptic model is concluded or needed.','Use geometric classification and involution, deduce residue degree, then apply the F_q morphism and lambda_M.'),[(14163,14186),(14982,14989),(15045,15056)],[(70,70),(79,79)])]
apps=[]
for id,pages,locator,assertion,consumers,cjconsumers in specs:
 apps.append(dict(id=id,author='/root/astra_v14_baseline_gaussian',status='author proposed published replacement; independent application review pending',assertion=assertion,
   supplier=dict(**pin(PDF),printed_pages=pages,physical_pdf_pages_1_based=[p-429 for p in pages],locator=locator,version='final published scan'),
   supplier_passage_role='proof' if id=='A052-COARSE-DESCENT' else 'statement',project_connection=pin(OUT/'REPORT.md'),
   current_consumers=[loc(BASE,*x) for x in consumers],cj_consumers=[loc(CJ,*x) for x in cjconsumers],
   candidate_consumer=records[0]['candidate'],independent_acceptance=None))
put('APPLICATIONS.json',dict(schema='published-source-application-author/v1.4',applications=apps,
 nine_obligations=dict(source_hypotheses='Set M=N,q=ell_0; choose unused auxiliary p. No squarefreeness or extra representation hypothesis enters geometric propositions.',constructed_objects='Right Hom module of geometric enhanced curves, reference order, adele coordinate and its left order.',domain_and_indices='Geometric characteristicq moduli with cyclic N prime toq, including every exponent at2; distinguish coarse scheme points from models.',transition_and_comparison_maps='Same quasi-isogeny identification; Ihat=zRhat; ideal quotient multiplies lattice by a^-1; right uniformizer is source Frobenius.',lattices_and_quotients='Use right R modules and B-left/Rhat-right double cosets; q component is Dieudonne, not etale Tate.',uniformity_and_constants='Exact bijection/action; no new mass factors, character phases or asymptotic constants.',vertical_character_and_limits='Not a nilcharacter application. Relevant character compatibility is unchanged inert residue conjugation and project norm/Schwartz signs; all remain separate.',consumer_strength_and_non_circularity='Coarse rationality supplies lambda_M domain without choosing a scalar model; CJ reduction count is not used to obtain geometric classification.',related_uses_and_consistency='Whole fa53 manuscript search and explicit CJ consumers recorded in RELATED-USES; existing scalar character values are unrelated.'),
 limitations=['No selfacceptance','No final JK comparison','No acceptance of unfinished good-reduction draft','No whole coefficient identity or global release approval']))
patterns=[r'scalar.{0,80}Frobenius',r'Frobenius.{0,80}scalar',r'supersingular',r'division.uniformizer',r'coarse moduli',r'coarse point']
text=raw.decode();hits=[]
for pattern in patterns:
 for m in re.finditer(pattern,text,re.I|re.S):
  line=text[:m.start()].count('\n')+1
  hits.append(dict(pattern=pattern,line=line,matched=m.group()))
put('RELATED-USES.json',dict(schema='bounded-related-use-author/v1',base=pin(BASE),search_patterns=patterns,hits=hits,
 affected=[dict(location=loc(BASE,a,b),disposition=d) for a,b,d in [
 (14158,14186,'Replace geometric-source paragraph and scalar-model route by right-module source and explicit coarse-point proof.'),
 (14246,14249,'Local quaternion residue-field Frobenius/conjugation; unchanged and does not use scalar elliptic model.'),
 (14982,14989,'Only coarse rationality and parametrization values are needed for the finite sum; new proof supplies them.'),
 (15037,15056,'Right uniformizer=Frobenius supplied by published Remark3.5b; arithmetic/geometric inverses agree on Fq2 values.'),
 (3238,3252,'Separate CM raising-isogeny congruence; no dependency on the scalar model sentence.'),
 (3392,3399,'Fell2 residue field comes from principal ideal class-field splitting, not chosen scalar model.'),
 (3463,3469,'Same ring-class residue field; no scalar model dependency.'),
 (4480,4487,'Frobenius scalar of moving character; unrelated to supersingular elliptic models.'),
 (4625,4633,'Unramified Galois-character scalar; unrelated.'),
 (5795,5798,'Character scalar entries in singular differentials; unrelated.')]],
 cj_proof=pin(CJ),cj_scalar_model_occurrences=0,claim='No inspected current consumer requires a chosen scalar-Frobenius elliptic model; it is replaced only by the actually needed coarse rationality.',
 historical_review='Earlier conditional CJ review described the old scalar-model route. It remains unchanged; this source proposal is a new connecting proof requiring independent review.'))
put('SOURCE-PINS.json',dict(primary=pin(PDF),url='https://math.berkeley.edu/~ribet/Articles/invent_100.pdf',doi='10.1007/BF01231195',version='Final printed Invent.Math.100(1990),431-476',
 viewed_renders=[pin(OUT/'local-only'/f'ribet-{i:02}.png') for i in [2,9,10,11,12,13,14]],
 published_locators=['Section3 setup p438','Enhanced curves, endomorphisms and automorphisms p439','Prop3.3 and Tate/Dieudonne construction p440','Remark3.5(a) right/left module conventions p441','Remark3.5(b) right uniformizer Frobenius involution p441','Prop3.6 and proof pp441-443'],
 correction_search=dict(queries=['site.math.berkeley.edu/~ribet "On modular representations" erratum','"10.1007/BF01231195" correction erratum'],author_archive='https://math.berkeley.edu/~ribet/Articles/',result='No separate correction to these passages found in bounded search; universal absence not asserted'),
 retained_unaccepted_draft=dict(path='work/source-risk-review-20261107/cj-good-reduction-root/PROOF-DRAFT.md',sha256='a13f646503e35dc24670c72637905e3c4cff4067c144340e634f3df94ef4c2c6',role='Excluded from acceptance; unfinished source closure'),
 transitive_inputs='Published geometric statements retained as imports; no reproof of their Deuring/Dieudonne foundation claimed'))
put('CHECKS.json',dict(base=pin(BASE),candidate=pin(target),exact_edits=2,JK_old_occurrences=raw.count(b'jetchevkane'),JK_candidate_occurrences=candidate.count(b'jetchevkane'),
 CJ_unchanged=raw.count(b'cornutjetchev')==candidate.count(b'cornutjetchev'),no_source_pdf_in_public_candidate=True,
 no_live_mutation=True,full_TeX_build='Not run; source/application and exact candidate offered for independent review'))
put('MANIFEST.json',dict(schema='bounded-published-replacement-author/v1',author='/root/astra_v14_baseline_gaussian',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 status='Published source/connection and candidate proposal awaiting independent review',files=[dict(**pin(p),local_only='local-only' in p.parts) for p in sorted(OUT.rglob('*')) if p.is_file()],
 external_source=pin(PDF),base=pin(BASE),no_live_mutation=True))
print(json.dumps(dict(manifest=pin(OUT/'MANIFEST.json'),report=pin(OUT/'REPORT.md'),applications=pin(OUT/'APPLICATIONS.json'),candidate=pin(target))))
