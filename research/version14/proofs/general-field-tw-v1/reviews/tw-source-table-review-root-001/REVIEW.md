# Review of the remaining general-field auxiliary-prime inputs

Reviewer: `/root`, an internal model reviewer. Source-table author: `/root/astra_quartic_opt05_anchor`. Argument author: `/root/astra_v14_baseline_theta`, with the correction contributions and independent exclusions recorded in the separate review assembly.

Decision: accepted bounded source applications U01, U03, U04 and U05, with U02 supplied by its separately accepted final-DDT decision. The independently checked ray-class supplement closes the missing U03 source/connection. This is not whole-modularity, current-manuscript or release acceptance.

## Target and independence

The target is the frozen copy of `TW-SOURCE-DISCHARGE.json`, bound to theta003 `PROOF.md`, SHA256 `69d535145031e224f2eec621a243de6d492facc17bf85a5c27dbe8c3a89907fd`. Root copied the author's two unchanged files into `frozen-input/` after the author handed off the table. This does not transfer authorship to root. `prepare_review.py` verifies all 15 supplied file identities and all 11 raw-LF consumer spans. Its output does not decide mathematics.

Root had already read the argument and the earlier review assembly, and independently reviewed the scalar correction. This is not a blind review and is not a new review of all of theta003. Here root independently compared the remaining table entries with the actual published sources and reconstructed the stated source applications. U02 retains the separate compiler decision for final DDT; root does not claim independent authorship of that decision.

## U01: finite group input

The final Khare--Wintenberger Part II, pp.537--538, Lemma 4.3(2)(ii), (4), and (5), supplies the asserted characteristic-two finite group facts. Nonsolvable image gives the projective image conjugate to `SL_2(k0)` for a finite subfield with more than two elements. The full endomorphism module has scalar invariants, its quotient by scalars has no invariants, its first cohomology for the projective group vanishes, and its only submodules are `0`, the scalars, the trace-zero module, and the full module.

The proof on p.538 invokes Dickson and Dickinson for finite-group assertions. It does not use a number field being unramified at 2. The application uses the full module `End_k(k^2)`, not a direct-sum decomposition of it into scalars and trace-zero matrices. Such a decomposition cannot be imported in characteristic 2. The earlier accepted correction also keeps the actual additive cocycle image separate from its k-linear span. These are the objects used in sections 2--4 of theta003.

The injection in scalar cohomology follows from the long exact sequence and the vanishing of invariants in the quotient. Extension of the coefficient field does not change the finite-group hypotheses as stated in the source. The source's proof ancestors remain named imported results; this review does not reprove their full texts.

## U02: already accepted DDT application

The separately frozen compiler decision accepts the published 1995 Theorem 2.19, printed p.57, with its definitions and real-place conventions on pp.54--56. It covers precisely the full adjoint module, the constant residue-field module and the constant `Z/2^j` module in the unchanged sections 5 and 6 of theta003. Its ordinary-H0 final formula and the proof's real Tate correction must not be conflated. The old author-version availability statement remains historical text at the original author freeze; current integration must point to this final-source successor.

## U03: Chebotarev and reciprocity

Root read Serre's actual section 2.1, Theorem 1, and rendered its page. The exact locator is PDF page 10 of the pinned Numdam scan, with footer 331. Numdam's front matter identifies the published article as *Publications mathematiques de l'IHES* 54 (1981), pp.123--201. Both observations are recorded rather than silently changing the printed footer. The theorem gives density `|C|/|G|` for a conjugacy-stable subset of the Galois group of a finite extension. Its displayed Frobenius sends residue classes to their norm power, so it is arithmetic Frobenius.

The finite quotient here records the residual representation, the relevant continuous finite-valued cocycle, and `T_j`. A cocycle gives a homomorphism to the finite semidirect product with its coefficient module. Consequently these simultaneous data factor through a finite Galois extension. The earlier argument supplies a group element with the required splitting, distinct residual eigenvalues and nonzero local evaluation. Splitting in the normal extension and the nonzero local restriction condition are invariant under conjugacy; changing a cocycle representative changes its value by an element of `(g-1)A`. Thus the permitted set is a nonempty union of conjugacy classes. Serre supplies infinitely many permitted places, and deleting a finite list preserves infinitude. No effective Chebotarev estimate is used.

Root read Milne, *Arithmetic Duality Theorems*, second edition 2006, I.1.3 and I.1.6 on pp.18--19, the local reciprocity discussion on p.26, and Lemma I.4.5 on p.51. These identify the required continuous characters with local or idele-class characters. For an odd residue characteristic, the principal unit group is pro-odd and hence has no nontrivial continuous 2-primary quotient. The valuation factor contributes one `Z/2^j`, and the cyclic residue-unit group contributes another when the residue cardinality is 1 modulo `2^j`. This gives precisely the `2^(2j)` local order used by theta003.

The original table named ray-class finiteness without an exact published theorem. The separately authored compiler supplement supplies Kopp and Lagarias, *Ray class groups and ray class fields for orders of number fields*, Essential Number Theory 4 (2025), 1--65, DOI 10.2140/ent.2025.4.1. Root read the final publisher PDF's title/copyright, Definitions 5.2--5.4 on p.33 and Theorem 6.9 with its proof on pp.44--45, and inspected the three mathematical pages visually. Specializing the order to O_F gives exactly the ordinary ray class quotient for a nonzero integral ideal and any subset of real places. We need only its finiteness, not its cardinality formula or unit-rank assertion.

Root independently reconstructed the supplement's connection. Each finite subextension L/F has abelian 2-power Galois group. Principal units at each odd prime in Q form a pro-odd group, so map trivially by local reciprocity; conductor exponent is at most one. Outside Q there is no inertia, and at the real and dyadic places splitting gives no additional conductor. Thus every L uses the same finite modulus m=product(Q) and empty real subset. The ideal Artin map is onto by Chebotarev. Global reciprocity and the preceding local kernel conditions kill all principal ideals generated by alpha congruent to one modulo m. Its target is therefore a quotient of the finite ray class group. All finite subextension degrees have the same finite bound. A subextension of maximal degree contains every other one, since their compositum satisfies the same conditions and bound. The entire pro-2 extension is consequently finite. This proof also covers Q empty with m=O_F, and introduces no uniformity claim as Q varies.

The compiler's supplement manifest is d9e6854d811874699175efb39db7e29c272b5988427111b309fe9efa9cd27a2d. Root accepts its two source/connection entries for this exact theta003 application. A title-plus-errata search and the author's publication page checked on November 8, 2026 did not locate a correction affecting this use; that search is not proof that no correction exists. The final publisher PDF, rather than an author preprint, is the mathematical source inspected.

## U04: local duality and Euler ratio

The applicable source is Milne's Corollary I.2.3, p.28, Theorem I.2.6, p.30, and Lemma I.2.9, pp.31--32. The last lemma directly proves Euler ratio one for a module whose order is prime to the residue characteristic; the harder dyadic part of Theorem I.2.8 is unnecessary here.

At a selected place v, v has odd residue characteristic, the coefficient module is 2-primary, and the residual representation is unramified with distinct eigenvalues. Its full endomorphism invariants have k-dimension two. The pairing `Tr(XY)` on all two-by-two matrices is perfect even in characteristic 2, as can be checked on the matrix units. Composing with the field trace supplies the finite abelian-group duality pairing when needed. The mod-2 cyclotomic character is trivial, so the twisted dual is again this full module. Local duality gives equal H2 and H0 dimensions, and Lemma I.2.9 gives `h1-h0=h2=2`. At almost all places the unramified conditions annihilate one another by I.2.6. This matches the chosen zero/full local conditions and their duals. No Euler formula at a place above 2 was silently substituted.

The introductory sentence on printed p.31 says that the cohomology groups vanish for `r >= 2`. Root checked the rendered page, not only its extracted text. This assertion cannot be used as written: the very next Euler formula retains H2, and Corollary I.2.3 supplies its possibly nonzero dual. The application here uses the stated duality and Lemma I.2.9 and never assumes H2 vanishes. The typo is therefore recorded without importing it into the source table.

## U05: the actual deformation rings

The final Kisin text, section 3.2.1, pp.625--626, defines the complete local framed deformation algebras for an absolutely irreducible residual representation with the stated determinant lift. It explicitly retains factors for infinite places in the completed tensor product. The globally variable-determinant ring fixes determinant only on the decomposition groups at S. These are exactly theta003's hypotheses and ring, so its tangent calculation properly uses full Ad. A globally fixed-determinant tangent problem would be different and is not used.

The table does not infer representability from the later prime-selection proposition. Representability is the retained standard input already used in Kisin's definition of these rings. The relative tangent sequence and complete-local generation argument are separately reviewed steps of theta003. The source field need not be unramified at 2 merely to define these rings. This review does not approve any later local-component or patched-module theorem by association.

## Applicable corrections

Root read the pinned ten-page Milne 2006 addendum, revised October 26, 2025. The correction to I.1.2 replaces M by its U-invariants where a G/U-action is needed. The degree limitation in the preliminary spectral-sequence formula is respected in the positive cohomological degrees used here. The restricted-product topology correction at p.49 is respected by using continuous idele-class characters. The addendum's note on Haberland expressly preserves the cited finite-module duality under its stated unit hypothesis. No correction to the specific statements I.2.3, I.2.6, I.2.9 or I.4.5 is asserted in the addendum. This is not a claim that Milne has no errata, or that every proof in the book has been reverified.

## Limits and integration

This review concerns the named remaining published inputs and their uses in theta003. It does not replace the independent reviews of theta003's new argument, approve all ancestors of the cited theorems, or certify the whole modularity theorem. Final current-manuscript integration, source-table incorporation and whole-proof coverage remain separate. Paid or third-party complete PDFs, extracted pages and rendered images remain local inspection evidence and are not proposed for public redistribution.
