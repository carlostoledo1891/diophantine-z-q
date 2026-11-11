# Independent Milne source review

Reviewer: `/root/astra_quartic_opt05_anchor`. Date: 2026-11-07.
Author reviewed: `/root/sol_protocol_final_review`.

I accept the bounded mathematical comparisons, the exact proposed Brauer replacement, and the corrected author R3 source record identified below. I found no failed dyadic hypothesis, reversed isogeny ratio, or inappropriate BSD assumption in those applications. This is not acceptance of the complete V14 proof or of its separate Nekovar, Edixhoven, and forward-finiteness inputs.

The original frozen source-coverage record contained an error. `SOURCE-BINDINGS.json:18` calls the official addendum a complete one-page document. It has ten pages. That false coverage description must not be carried forward as evidence. I downloaded and read the complete primary addendum, including its substantive corrections beyond the first page. R2 corrects the page count; R3 also corrects a higher-local-field domain description and records the transitive I.3.8 repair. The original and both successors remain preserved. My decision uses the independent primary-source reading, not the author's verdict.

## Exact targets and primary sources

The author manifest is `milne-author/MANIFEST.json`, SHA-256 `814f3b20201fef78db3627e1def49b41bd538363fd536fe33b78e0c6fdf1cda9`. All four listed file hashes and byte counts agree. The mathematical report has hash `f0ce5d9878fa2ef6b68783168e9ce642011f9ed6ac41044602e2a62627122d6a`.

The reviewed manuscript is `work/quartic-v14-release/preview-repository/manuscripts/quartic_v14.tex`, SHA-256 `81d421af9dedd0d975024c9d0ff1b1d11249b7b36f2c9215bd2c80278f4934fc`. Every frozen author excerpt agrees with its actual bytes. No manuscript or successor004 file was changed.

I independently fetched the following official primary sources:

- [Second-edition publication record](https://www.jmilne.org/math/Books/adt.html). It identifies the July 2006 electronic file with the paperback production file apart from the copyright page.
- [Arithmetic Duality Theorems, second edition](https://www.jmilne.org/math/Books/ADTnot.pdf), 347 PDF pages, SHA-256 `2c6195ec76a974f3f336c77cb71cc3845b018aad2d43136716b3477a3bc5fb31`. The downloaded bytes equal the author's local copy.
- [Official second-edition addendum](https://www.jmilne.org/math/Books/add/ADT2006.pdf), ten PDF pages, revision October 26, 2025, SHA-256 `2eff84551aa72ce16ae20554e46baf03494fa1130612875041905f9df34ea50c`.

All book page numbers below are printed pages. I inspected the equation and diagram images on pp.28, 42, 67, 98, 99, 100 and 164, in addition to reading the relevant surrounding text and all ten addendum pages. The local source copies, full extractions and page images are confined to `local-only/` and are excluded from the handoff manifest.

## Brauer comparison and exact replacement

At manuscript 746-783 the coefficients in the character-square-root sequence are constant discrete groups. They are not roots of unity with cyclotomic action. Its kernel is nevertheless the actual trivial group of second roots of unity, so Hilbert 90 and the Kummer sequence identify the obstruction group with the two-torsion Brauer group.

Milne I.1.6(b), I.1.7 and the local reciprocity description on p.26 provide the invariant and character interpretations. Over Q_p, finite-order character square roots exist on the valuation factor. For odd p, squaring is invertible on the pro-p character group, and on the finite cyclic unit factor its image consists exactly of characters trivial at -1. At p=2 the finite sign factor supplies that obstruction; a character on the remaining procyclic Z_2 factor has a finite-order square root after increasing its two-power order. This last step does not claim that squaring is surjective on the sign factor.

The local two-torsion Brauer group has two elements, so detecting whether the obstruction vanishes determines the whole local class. Outside the chosen support, an unramified two-torsion class is zero by the cohomological dimension of the unramified quotient. The displayed global Brauer exact sequence in the proof of II.2.1, p.164, determines the real invariant from the finite invariants and injects the global class into its localizations. Changing reciprocity orientation does not change the unique nonzero two-torsion invariant.

The exact 425-byte `PROPOSED-BRAUER.tex`, SHA-256 `e54eade4962e6b81eb2113ecd2d458267fcdb096a1e8257bfd34489542230484`, correctly replaces current lines 770-774. It names the actual location of the global sequence and states the order-two comparison. The replacement retains the preceding sentence and the subsequent continuous cochain construction. A pointwise square root of the finite-image character can be chosen continuously, and a continuous sign cochain adjusts its coboundary without enlarging the values beyond mu_(2m).

The uncited repeated construction at 7209-7245 has the same coefficient convention and local obstruction. Its different preceding bound for the character order is not replaced or inferred from the first occurrence. Both occurrences pass the same obstruction check.

## Finite Kummer maps, including the dyadic places

Milne I.2.3 requires the torsion order to be prime to the characteristic of the local field. Every finite completion here has characteristic zero, including completions over 2. The residue characteristic restriction in the special case I.2.9 is not the hypothesis of I.2.3 or I.2.8.

The diagram in the proof of I.3.2 on p.42, together with I.3.3 and Corollary I.3.4, identifies the finite Kummer inclusion with the adjoint of the quotient to H^1(F,B)[2^a]. The kernel of that quotient is exactly the Kummer image. The elliptic principal polarization and Weil pairing identify the dual coefficient module. This proves exact orthogonality, rather than a purported perfect pairing on the Kummer image itself. The possible comparison sign in I.3.5 does not change the kernel; the proof here uses the actual Ext/Kummer diagram.

For M=B(F)^wedge_2 the finite torsion remains present. Derived reduction of M[-1] has M[2^a] in degree zero and M/2^a in degree one. These are the actual finite point and quotient groups. The integral restricted pairing has class in Hom(M tensor M,Z_2). The degree-one truncation of M[-1] tensor^L M[-1] contributes no map to Z_2[-2]; the relevant negative Ext groups vanish. Finite isotropy at every exponent therefore makes the bilinear form zero by separatedness. The degree-minus-one ambiguity group also vanishes. A bounded projective resolution realizes the zero class by a homotopy. Modulo two, finite local duality identifies both the degree-one quotient and the degree-two dual of degree zero. Derived Nakayama lifts this comparison for the bounded finite-type local models already used in the manuscript.

This checks the source-to-local-comparison argument at 3592-3633 and its exact repeated use at 3960-3998. The latter retains the finite torsion resolution and fixes the old local twist before scalar extension. It does not introduce a rational inverse with a hidden two-power denominator. The repeated finite-place input at 5480-5504 and 13258-13265 is the same. The global Selmer-cone theorem, coefficient-ring transport and later support switches remain distinct inputs; their validity does not follow merely from this Milne audit.

The real convention at 13238-13256 is not an application of the nonarchimedean I.3.2. Milne I.2.13 and I.3.7 use real Tate cohomology. The manuscript separately retains ordinary degree-zero local invariants through its bounded real complex. That distinction is necessary, and this review does not replace the real complex or its subsequent Nekovar limit argument with a finite-place theorem.

## Isogeny signs and normalization

I checked I.7.2 and the proof of I.7.3 on pp.96-100, including the diagram on p.99 and all factors on p.100. The surrounding BSD-invariance theorem begins with a BSD hypothesis. Its arithmetic identity (7.3.1) is proved by the finite duality diagram chase and Euler characteristic, with finite Sha as the finiteness input. No leading-term equality is used in that chase.

Use z(f)=#ker(f)/#coker(f), phi:A->B and its dual psi:B->A. Finite Sha duality gives

`#Sha(A)/#Sha(B) = #ker Sha(phi)/#ker Sha(psi)`.

Rearranging (7.3.1) therefore gives

`#Sha(A)/#Sha(B) = [z(phi_Q)/z(psi_Q)] / product_v z(phi_v)`.

For the manuscript's rank-one free groups, I and J are oriented exactly as at 4310-4318. The composites are [2], so IJ=2. Height adjointness gives I^2 Reg_B=2 Reg_A. The rational-point z ratio is thus the square of the rational-torsion ratio times Reg_B/Reg_A. This yields the signs of all terms in 4336-4340.

The local identity on p.98 uses the pulled-back differential on A. Replacing it by an integral top-form generator introduces |a|_v; the global product is one. Both pullbacks extend integrally to the Neron models, and their compositions on the two-dimensional cotangent space have determinant 4. Thus ab=4 with integral a,b, as in the manuscript. The real map is surjective on identity components; the kernel has order at most four and the target has at most four real components. The claimed period valuation is bounded with these measures.

The finite connected-fiber factors cancel on the actual prime cases used here. At split primes the restriction and product models are locally the same. At nonsplit unramified good primes the good fibers have the same Frobenius polynomial by isogeny. At a companion ramified prime the already stated model descriptions give connected fibers with the same point count: the restriction is an extension of the good elliptic fiber by an additive group, and the product has that elliptic fiber and the additive identity component of the ramified twist. The residual component-number calculation is the separate Edixhoven input at 4345-4364. This review retains it and does not infer it from Milne.

The source's set S includes infinity, all bad places, the primes dividing the isogeny degree and the nonunit differential primes. In particular 2 is included. The real Tate-degree-zero correction on p.100 is present and cancels with I.5.1 as displayed there. Finite Sha is required only at the known analytic rank-one and rank-zero constituents specified in the manuscript. The forward theorem supplying that fact remains an inherited input.

## Dimensions and repeated divisible-quotient uses

For I.4.10 and I.5.1 the coefficient order must be a unit in the S-integers. Current S_0 contains the primes over 2; its omission of archimedean symbols is the usual convention, and the field is imaginary quadratic. Thus the finite order-four module is an S-unit module. There are no real places, so I.4.10(c) gives vanishing above degree two. At the one complex place I.5.1 uses ordinary H^0 of order four and normalized absolute value 4^2. Its multiplicative characteristic is 1/4, giving h^0-h^1+h^2=-2 and h^2=h^1-4. The bound is not inferred from a generator estimate alone.

Locally the Cartier dual of trivial W=(Z/2)^2 is mu_2^2, also trivial. Hence h^2=2. I.2.8 gives characteristic [O_F:4O_F]^-1, which is 2^(-2d) at a dyadic field of degree d and one at odd places. Therefore h^1=4+2d. I.3.3 supplies the free rank d of the two-completed point group; full rational two-torsion gives two finite torsion generators. Derived reduction has dimensions 2 and 2+d. None of these assertions treats 2 as a unit in a dyadic local ring.

The addendum's distinction between infinitely divisible elements and a maximal divisible subgroup is relevant. At current 1184-1194 and 7921-7926 the cofinite two-primary group is explicitly a sum of copies of Q_2/Z_2 and a finite group. The displayed divisible summand is maximal because every divisible subgroup maps trivially into the finite quotient. In 4235-4246 and 5534-5542 the exact sequence has a divisible image and finite cokernel, which gives the same maximality directly. The proof in `pole.md:94-110` pairs cyclic factors of the entire finite alternating quotient, without asserting that its restriction to F[2] is nondegenerate. These are different valid connections, not an arbitrary-group identification. Poonen-Stoll's actual alternating-pairing application is a separate source review.

## Complete addendum disposition and scope of the finding

`ERRATA-APPLICABILITY.json` records the complete addendum by correction and page group. Two corrections need explicit attention beyond the author's first-page discussion.

The I.3.8 proof on p.46 used an invalid completion of the infinite unramified union. This is relevant background to I.6.3 and global Sha duality. The addendum repairs it by working over each finite unramified complete extension, proving vanishing through its finite-level formal filtration, and only then taking the union. Current 3214-3242 independently uses this same finite-extension order. I checked the corrected source argument; I did not classify the error as unrelated merely because I.3.8 has no literal current citation.

The I.6.24 restriction is to the components whose orders are S-units. The consumed I.6.13 finite-Sha duality and I.7.3 chase do not require the unrestricted I.6.24 assertion. Their two-primary finite coefficient modules meet the S-unit condition anyway. The flat-cohomology and characteristic-p repairs in Chapters II and III are not substitutes for these characteristic-zero Galois-cohomology arguments. The current restriction of scalars is along a separable quadratic number-field extension, not the arbitrary fppf Weil-restriction assertion questioned in III.6.3.

Finding M-01 is a source-review provenance/coverage error. Its affected current fields are `official_addendum.read_scope` and the generator's corresponding literal. It is not evidence that a V14 theorem is false. A corrected author record should preserve the original freeze, cite the exact ten-page source, and retain the relevant I.3.8 and S-unit dispositions. This independent review supplies the bounded mathematical decision despite the original incomplete coverage description. It does not approve the false original field.

`OCCURRENCES.json` pins all seven literal current Milne-ADT citations, the bibliography and the additional source-related repetitions and boundary consumers inspected here. Citations to Milne's separate abelian-variety or modular-form texts are not silently included. The switch and global Selmer rows are explicitly boundary rows, not new approvals.

## Successor checks and findings history

I checked the exact R2 manifest `037a180fccf370a828c6ffb614dfae1335018db8c947acc2fcc250eaf48777ed` and R3 manifest `9b975f6059c97ac83e5455a2b9707736fca4d886ca94789de3525e88a7fa4c12`, their parent links, all eight listed files, all current excerpt hashes and the unchanged proposed replacement. The mathematical report sections from scalar descent onward are byte-identical to R1. R3's report has SHA-256 `8eab3630d1b3f62c39d2b74ddaf7183fa2be32dee20e43b0baa14a9d4811df2e`; its source-bindings file has SHA-256 `f6cf57c1c63ae4c9fd36d737bef45df8b3ac6a12f448bdd64ef41875740a1555`.

M-01, the incorrect complete one-page reading claim, is resolved in the R2/R3 successors by the exact ten-page source pin and the complete applicability record. The false R1 field remains preserved and is not retrospectively accepted.

M-02 arose in R2's description of Exercise I.2.21 as equal positive characteristic. Printed p.39 instead specifies a two-dimensional local field of characteristic zero with positive-characteristic first residue field. The correct non-use argument is that the current fields are ordinary one-dimensional finite extensions of Q_p. R3 states that distinction explicitly. This was a source-domain description error, not a discovered failure of the current local theorem.

M-03 records the missing transitive applicability connection for I.3.8. It is true that direct finite Kummer duality does not use I.3.8, but I.6.3 explicitly does, and that support argument enters the global Sha setting used by I.7.3. R3 now records the finite-complete-extension-first repair and pins the current related manuscript argument. I checked the primary correction and its use independently. The reviewer identified the omitted source connection and pointed to the existing official repair; no new replacement theorem was invented or proved by the author and reviewer jointly.

These findings are resolved only for the exact R3 record and the occurrences listed here. They do not certify every use of Milne elsewhere or every current source-review record. `FINDINGS.json` preserves each defect, affected scope and corrected target.

## Outcome and remaining actions

Accepted within the stated source scope: Brauer obstruction comparison and its exact citation replacement; finite-place Kummer orthogonality and the written derived comparison; isogeny arithmetic signs and measure conventions conditional on the separately named component and forward-finiteness inputs; global and local residual dimensions; compatibility of the inspected repetitions with these source hypotheses and the complete addendum.

The source-record corrections are resolved in R3. No mathematical source gap was found in the bounded applications after the complete primary-source check. Any integration must use that corrected target and preserve R1/R2 findings history. No claim is made that the whole book, its unrelated later results, or the entire current manuscript has been proved by this review. There is no manuscript installation, approval-registry update, live gate receipt or release authorization here.

Run `review_checks.py` for the independent byte, occurrence, replacement and arithmetic-orientation checks. It does not execute any author script or use finite tests as a proof of duality.
