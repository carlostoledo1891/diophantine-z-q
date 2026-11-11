# Baba–Granath: final source compared for the current use

Author evidence prepared by `/root/astra_v14_assertions_arithmetic`, run `local:v14:arithmetic-assertion-author:20261107`. Independent source-review disposition remains required. No manuscript or preview files were changed.

The final journal PDF was obtained freely from [Cambridge's publisher endpoint](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E6B7F5233E98E9C8E013658575FF713F/S0008414X00022008a.pdf/genus-2-curves-with-quaternionic-multiplication.pdf): Srinath Baba and Håkan Granath, *Genus 2 Curves with Quaternionic Multiplication*, Canadian Journal of Mathematics 60(4) (2008), 734–757, DOI [10.4153/CJM-2008-033-7](https://doi.org/10.4153/CJM-2008-033-7). It has 24 pages, publisher page furniture and DOI, and SHA256 `c711b2bed2aa0dd70d1bc1dd06c6d4a921c4b8735452bc143431f080a8cac12c`. This is final publisher text, not an author copy inferred equivalent from metadata.

The pinned 26-page 2005 preprint has SHA256 `b049ce64f9b662af0e078f4faa9e5325cc7a99bf2d6ccda0a31a84719d031c32`. Both files' relevant pages were extracted and visually inspected. The intake was the reviewer's exact `babagranath` row in `SOURCE-VERSION-DISPOSITIONS-001.json`. Current application A001 consumes the quotient/branch description at manuscript lines 495–498 and the polarized-equivalence and Igusa-coordinate description at 608–617. The manuscript SHA256 remains `b8421edc569a832c9c4271e3592b10df58e75d25f4dc5619c2b4a6766157044d`.

## Matched statements and conventions

| Current dependency | Pinned preprint | Final source | Comparison |
|---|---|---|---|
| Polarized coarse moduli equivalence, preserving the principal polarization and the action of the stable subring R | §2.1, pp.3–5; Theorem 1 p.4 | §2.1 pp.736–738; Theorem 2.1 p.737 | Same needed equivalence relation and quotient conclusion. The final text explicitly calls the moduli space coarse. For R=Z the conclusion is V_Z=V/W. This is an isomorphism-class statement, not a universal-family or rational descent theorem. |
| Discriminant-six quaternion/order/polarization parameter and the two twisting rings | §3 p.6 | §3 p.739 | Same B=(2,−3), O=Z[i,(j+1)/2], μ=2j+ij with μ²=−6; twisting rings Z[i] and Z[j+ij]. The two involutions generate the full four-element Atkin–Lehner group in this case. |
| Rational quotient | Lemma 2 p.7 | Lemma 3.1 pp.739–740 | Same V/W≅P¹ over Q and rationality of the three marked images. |
| Branch stabilizers | §3.1 table p.7 | §3.1 table p.740 | Same full-normalizer row: one elliptic orbit each of orders 2, 4, 6, no order-3 orbit. The final row is explicitly labelled Γ_W. Together with the labelled fixed points, orders at z₂,z₃,z₆ are 4,6,2. |
| Arithmetic coordinate and finite nonzero locus | Proposition 7 p.9 | Proposition 3.6 p.742 | Same isomorphism of the genus-two locus with P¹ minus {0,∞}; same displayed weighted Igusa coordinates [12(j+1),6(j²+j+1),4(j³−2j²+1),j³]. The two omitted points are the product-polarization cases. The manuscript explicitly restricts to finite nonzero j. |
| Match arithmetic j to analytic j_m² | Proposition 10 pp.11–12 | Proposition 3.9 p.744 | Same equality and same normalization assigning j(z₂)=0, j(z₃)=∞, j(z₆)=−16/27. This j is not the classical elliptic j. Consequently the required branch labels and orders are unchanged. |

These are specific statement-level matches, not a claim that the entire files or all proofs are equivalent. The final text supports the imported quotient and branch assertions in the current use, subject to retaining the following explicit normalization correction.

## Actual differences and necessary separate proof

The preprint p.4 defines a twisting element in the positive normalizer but immediately says its norm is negative. The final p.737 uses the full normalizer and conditions tr(χ)=tr(χμ)=0, explains the negative norm, and adds the primitive-element description. Thus the final definition resolves that positive-normalizer inconsistency. For the trace-zero elements here, tr(χμ)=0 is equivalent to χμ+μχ=0. The final theorem's quotient conclusion is preserved under the corrected definition; this change must not be described as byte or literal equivalence.

Both versions display E(x,y)=Trd(conjugate(x) μ y) on the O lattice and call it principal. The final p.736 still has this formula. The current manuscript instead uses E₀(x,y)=Trd(μ⁻¹x conjugate(y)), with the Lin–Yang convention and its own matrix computation at lines 486–496. Since μ²=−6 and the trace form is alternating, E=6E₀. An exact rational computation in `check_normalization.py` reproduces the manuscript's matrix, gives det(E₀)=1 and det(E)=6⁴=1296. `NORMALIZATION-CHECK.json` records the successful check. Thus the final Baba–Granath displayed formula does not itself establish a principal polarization in the stated lattice convention. The manuscript's inverse-μ form, positive-sign choice, determinant-one calculation, and its separately sourced Rosati/polarization identification must remain explicit. Multiplying by a positive scalar preserves the Rosati involution but does not preserve principality.

A smaller proof typo also persists: the last paragraph of Lemma 3.1 refers to the rationality of z₃ when ruling out conjugacy of z₂ and z₆. The preceding paragraph has already established rationality of z₂. Using z₂ instead gives the intended argument: conjugate images with one Q-rational must coincide, contrary to the distinct marked orbits. This is a local correction to the printed proof, not a changed statement.

The all-determinant-components adelic quotient, level-three degree bound ≤324, integral model, and descent of a universal abelian scheme are additional manuscript arguments. The published coarse-moduli theorem does not by itself supply these. This comparison does not reapprove those arguments or remove their existing dependencies.

## Proposed disposition

The final-source retrieval and comparison for the specifically listed A001 statements are complete. Proposed review disposition: accept the final statement mapping while retaining the explicit normalization correction and independent manuscript proof obligations. The reviewer must decide acceptance; this report generates no approval. A bibliography successor could cite the 2008 publication and final theorem numbers. No such edit has been made.

Only this report, its exact-hash evidence, and the authored normalization checker/result are candidates for release. The final PDF, author text extracts, and rendered source pages remain local under `local-only/` and must not be redistributed with the preview.
