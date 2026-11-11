from pathlib import Path
import hashlib,json
R=Path.cwd();B=R/'work/source-risk-review-20261107'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def j(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def put(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
db=B/'h5-full-b-map-review-001';dt=B/'five-to-three-independent-review-001'
assert not (db/'MANIFEST.json').exists() and not (dt/'MANIFEST.json').exists()
checks=j(dt/'CHECKS.json');assert checks['passed'] and checks['count']==93
fullb="""# Independent full-B normalizer-map review

Accepted for H5-FULL-B-NORMALIZER-MAP, H5-PRIME11-B-MAP, and H5-B-SCALAR-DISCREPANCIES, relative to the named existing PEL, endomorphism and same-L Hom inputs. This is a bounded mathematical/source-to-application decision, not strict ordinary adoption, TeX incorporation, or whole-H5 approval.

The author target is h5-scalar-normalizer-author-arithmetic-001, manifest 6e65bc53231605b1019796cbfc38c9dc30a22dbd5076c406eafcef24b38c919a, proof 4de428677392e79ce0af17a190b5038aefdfd8153ce5d7f480c94050d92e212d. I read the complete proof and all three application cards. Actual current occurrences and the seven incoming locations are pinned in the author's SOURCES.json, against PROPOSED.tex 99d35bfe017ffdea59f134520a05a5ae15ccfa41c9d0004da02bee4f67431cee.

Independence. I did not author this new proof. Root supplied advance guidance about the scalar chart map; I asked that the upper-half-plane domain and actual order-normalizer premise be explicit. I authored the earlier geometric-isogeny connection, which is therefore not independently reapproved here: its input is consumed through Arithmetic's separate acceptance b6586ca0afe689f8b6b4d580fbfffbc6f57dbc2b1e6af7b43ff0bb860c0c61c5. The full-cover input retains the earlier independent review 9875bfa37bff87dfcccdced9d019f872879865c547d4bc948d851969c2456984. No new proof of either ancestor is claimed.

Source reading. I read the official Springer Chapter43 capture, especially 43.1.2-43.1.3: Lambda_tau=i_infty(O)(tau,1)^t and i_tau=i_infty, together with the rational normalizer action. The displayed chart is an upper-half-plane chart; this source alone is not an all-component theorem. Capture hash 1febf4824c6641e51b9fdbec542ca148819bb38e51be257e68a05f939c306ce7 binds an official HTML extract, not a final-PDF comparison. I separately reread the accepted full-cover Sections6-7 and current normalizer definition7846-7882. In particular, N normalizes the maximal order's finite completion, not merely the principal-level subgroup.

All-component map. The actual right normalizer action changes the finite lattice while retaining the rational left-B module and Hodge structure. The two lattices are commensurable. A rational scalar clearing their inclusion is a Hodge map commuting with the entire left-B action and induces an isogeny in the asserted source-to-target direction. This intrinsic argument applies on every component via the accepted PEL comparison. In the separately labeled chart, lambda=cz+d satisfies lambda*v_(bz)=b*v_z. Scalar lambda times the identity therefore sends the source lattice to O*b*v_z inside O*v_z after the stated clearing, giving A_(bz) to A_z and commuting with i_infty(B). Matrix b is not substituted for this scalar map. The determinant of right multiplication on the rank-four quaternion algebra is Nrd(b)^2, giving the displayed index. The actual geometric maps are over L by the retained all-Hom result.

Prime-to11 choice. The current normalizer premise implies n_11 belongs to Q_11^times GL_2(Z_11). The proof's elementary matrix-unit argument verifies this local order-normalizer description. Thus the two 11-adic lattices are homothetic. Multiplication by a rational power of11 equalizes them; an integer prime to11 then clears all remaining lattice denominators. The resulting B-linear map is an isomorphism on the 11-adic lattices, so its degree is prime to11. Central rescaling preserves class and direction. No later arbitrary Skolem-Noether correction is inserted into this degree choice.

Finite scalar family. Choose the maps on the finite Galois quotient with the identity at its identity, then inflate. Their discrepancies lie in End^0(A)=B and commute with B, hence lie in Q^times. Associativity yields the scalar cocycle. Tate functoriality preserves the same identities at every prime. This last assertion is not itself Frobenius compatibility, which has its own review.

Limits. The degree support is only controlled at11; sign-cochain splitting, semisimplicity, modularity and the whole H5 proof remain outside this decision. The Theta integration candidate is not approved here. Ninety-three combined identity checks verify both selected author packages, exact source/consumer spans, and the separate compatibility delta. These checks support exact binding rather than replace mathematical reading. No author or manuscript bytes were changed.
"""
trace="""# Independent prime-five to prime-three compatibility review

Accepted for COV-FIVE-TO-THREE, relative to the named incoming representation and classical-modular inputs. The exact target is five-to-three-author-sol-002, manifest a3f48e27c8df1e1999bc07abc06b1cfa3a2d32636cb37346b356535fd69f83b9, proof d710da5f50fc650c723f2dab3c83a17010de4785fcc9ccee878b734adac9bec8. This is not strict ordinary adoption, a new conductor bound, or whole-manuscript approval.

The current target PROPOSED.tex is 99d35bfe017ffdea59f134520a05a5ae15ccfa41c9d0004da02bee4f67431cee. The exact construction8100-8120, comparison8121-8131, consumer8218-8222, and separate C6 occurrence8140-8142 have verified raw-byte bindings. C6's p5-only realization is not used as a substitute for the new prime-three identity.

Independence. Source-first requirements were frozen before the new proof at d08cf5ceb9035e24d7d9ecea751c4fffb67ddb6d5a4adec6ce62894dd82e73e1. I read the entire new proof and all source/consumer records. My earlier QM/Hodge/source work is disclosed in that record and not reapproved here. The only requested successor change was wording: iota_3 extends the original prime-three coefficient embedding, independently of iota_5; it does not extend a map with codomain Qbar_5. The raw check verifies this is the sole proof change. I supplied no substantive new derivation. The author already excluded form-level primes for cofinite comparison before my reminder.

Published input. I directly viewed Milne, Abelian Varieties, Arithmetic Geometry (1986), printed123 and125, from PDF 86259344a576e4ef75a9d81e9bf43143f872a72b14cf8fcc2703f3aea6349136. The degree function is extended to End^0 by clearing denominators. The printed125 definition gives the rational degree polynomial of an arbitrary rational endomorphism, and Proposition12.9 identifies it with the characteristic polynomial on the covariant rational Tate module for every prime different from the ground-field characteristic, in particular identifying trace. This is an arbitrary-endomorphism assertion, not just finite-field Frobenius. No recursive audit of its published proof is claimed. The viewed printed123/125 image hashes are recorded by the checker.

Actual reduced operator. A finite comparison extension and a common integer clear the finitely many quasi-isogeny denominators and permit spreading the finite equations and maps over good models. They do not replace controlled L-prime or the original support T. At a good rational prime p, arithmetic Frobenius acts on the residue field as x mapped to x^p, even when its degree exceeds one. The twisted source is therefore the p-twist. The reduction of m*mu_sigma composed with relative p-Frobenius is an endomorphism of the same special-fiber abelian surface; it is not replaced by q-Frobenius of the whole residue field.

Specialization and trace. For ell unequal to p, torsion in the good abelian scheme is finite etale: the proof gives properness, finite geometric fibers and invertible differential. Specialization over the strict henselization is functorial for the map and twisted source. The reduced operator therefore gives the original Tate operator, after dividing by m. Milne's rational-endomorphism statement produces a rational trace q_p independent of ell. The full representation has trace iota_ell(t_sigma)*q_p for the same algebraic t_sigma=a_sigma/b(sigma). Since it is two copies of r_ell, the latter trace is one half of this number. The positive degree normalizer a_sigma is not mistaken for a root of unity; the controlled character b is not replaced by an unrelated modular twist.

The same form at three. A common number field contains the original scalar/splitting field and the chosen form's coefficients. Independently extend the fixed embeddings to iota_5 and iota_3. Equality at five gives equality of the algebraic numbers at cofinally many good primes, and applying iota_3 gives the same-form traces at three. The retained semisimplicity and fixed-representation Chebotarev/Brauer-Nesbitt inputs then identify r_3 with the classical semisimple weight-two realization.

Incoming boundaries. The finite B-compatible maps and scalar discrepancies are supplied by the separate full-B review sealed alongside this one. Faltings semisimplicity, the already known r_5 realization, the classical semisimple realization at3, and Chebotarev/Brauer-Nesbitt remain named inputs. The future ordinary records must bind their actual scopes; this review does not manufacture a missing published source contract. The cofinite comparison excludes form-level primes without assuming the desired support bound. Once global identification holds, the existing conductor argument uses r_3 at p=5 and r_5 at other primes. No p=ell comparison or new optimal-level claim is made.

Validation. All selected author members, listed sources and raw spans, two viewed images, unchanged INPUTS/CONSUMPTION/FRONTIER and the single literal002 delta passed93 checks. The predecessor remains unchanged. The separate full-B receipt is bound in INPUTS.json. Mathematical reading supplies the decision; identity checks alone would not do so. No author/manuscript bytes changed, and ordinary-record and TeX incorporation remain separate.
"""
def seal(d,report,scope,inputs):
 d.mkdir(exist_ok=True)
 (d/'REVIEW.md').write_text(report,encoding='utf-8',newline='\n')
 put(d/'DECISION.json',{'status':'accepted_in_bounded_scope','independent_acceptance':True,'scope':scope,'ordinary_adoption':False,'tex_incorporation':False,'whole_proof_approval':False,'report_sha256':sha(d/'REVIEW.md')})
 put(d/'INPUTS.json',inputs)
 if d!=dt:put(d/'CHECKS.json',checks)
 members=[]
 for f in ['REVIEW.md','DECISION.json','INPUTS.json','CHECKS.json']:
  p=d/f;members.append({'path':f,'sha256':sha(p),'bytes':p.stat().st_size})
 put(d/'MANIFEST.json',{'status':'accepted_in_bounded_scope','files':members,'local_source_assets_excluded':True})
 for x in members:
  assert sha(d/x['path'])==x['sha256'] and (d/x['path']).stat().st_size==x['bytes']
 ans={'path':str(d.relative_to(R)),'manifest':sha(d/'MANIFEST.json'),'review':sha(d/'REVIEW.md'),'decision':sha(d/'DECISION.json')}
 print(json.dumps(ans));return ans
a=B/'h5-scalar-normalizer-author-arithmetic-001';s=B/'five-to-three-author-sol-002'
b=seal(db,fullb,['H5-FULL-B-NORMALIZER-MAP','H5-PRIME11-B-MAP','H5-B-SCALAR-DISCREPANCIES'],{'author_manifest':str((a/'MANIFEST.json').relative_to(R)),'sha256':sha(a/'MANIFEST.json'),'source_records':j(a/'SOURCES.json'),'prior_authored_input_independent_review':'b6586ca0afe689f8b6b4d580fbfffbc6f57dbc2b1e6af7b43ff0bb860c0c61c5'})
seal(dt,trace,['COV-FIVE-TO-THREE'],{'author_manifest':str((s/'MANIFEST.json').relative_to(R)),'sha256':sha(s/'MANIFEST.json'),'sources':j(s/'INPUTS.json'),'consumption':j(s/'CONSUMPTION.json'),'full_B_review':b,'retained_frontier':j(s/'FRONTIER.json'),'checker':{'path':str((dt/'check_inputs.py').relative_to(R)),'sha256':sha(dt/'check_inputs.py')}})

