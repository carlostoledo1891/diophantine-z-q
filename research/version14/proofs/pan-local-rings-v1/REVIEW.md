# Independent review of Pan's local-ring application

Reviewer: `/root`, 8 November 2026. The accompanying decision binds the exact author packet. This is a bounded source and mathematical connection review, not acceptance of the entire Pan proof, the manuscript, or a release.

## Sources actually read

I read Pan's pinned author text, pages 38–47; Thorne's pinned author text, pages 17–19; Taylor's final article, Lemma 2.7 on pages 193–194 and Lemma 3.2 with its proof on pages 197–199; and Allen–Newton–Thorne's final article, Section 3.1 on pages 2406–2407. I also read Taylor's final Proposition 3.1 on page 196. The source hashes are in SOURCE-PINS.json. I rendered and inspected the two pages of the published correction and Pan page 46, in addition to extracting the source text.

The final Taylor and Allen–Newton–Thorne texts are available. The read Pan and original Thorne texts are author versions. The correction explicitly identifies the defective published Thorne assertion, but does not certify that all other passages in the author versions equal their journal counterparts. Those final-version qualifications remain.

## The published correction and the actual branches

The published correction concerns generic reducedness of the special fiber of the entire unreduced trivial-character lifting ring. Its valid replacement first takes the nilreduction of the lifting ring. These are different assertions. A square-zero thickening of a DVR already illustrates why flatness and identical prime spectra do not imply the stronger statement.

Pan's Lemma 4.2.10(1) asks for componentwise information. Its finite-type supplier is Taylor's final Lemma 3.2(1), not the literal first part of Taylor's final Proposition 3.1. The reduced components have generically reduced special fibers, and the special-fiber components are distinct. Pan's Proposition 4.2.4 proof explicitly passes the trivial-character factors to their reductions on page 47. I therefore accept the author's finding that the published correction does not by itself invalidate this inference.

The other branch is different. In Pan's Section 4.1.1, the character has 5-power order and factors through the residue-field units. Its value alpha at the chosen tame generator is a nontrivial root of unity when the character is nontrivial. Consequently alpha and its inverse are distinct and each has order dividing q-1. The applicable Thorne assertion is Proposition 3.15(2), followed by Proposition 3.16. The defective all-trivial assertion 3.15(1) is not the premise used here. The arbitrary nontrivial residual representation branches in Pan use Shotton and are outside this review.

## Fixed determinant and nilpotent quotients

I checked the proposed replacement for Pan's overbrief global polynomial-ring comparison. Multiplication of the Frobenius matrix by a scalar s defines a degree-two finite etale map from the fixed-determinant scheme times G_m to the unrestricted scheme. Algebraically the cover adjoins s with s^2=det(Phi)/d. The derivative 2s is a unit, and its inverse map divides Phi by s. This is a cover, not a global affine-line product.

At the chosen residual point, the sheet s=1 has a unique functorial lift because 2 is invertible. This gives the claimed formal power-series factor and preserves the framing and inertia matrix. An idempotent in the fixed-determinant generic fiber remains a nontrivial constant idempotent in the formal-variable extension; connectedness therefore descends in the required direction. The corresponding irreducibility and dimension comparisons are valid. Regularity uses the stated excellent-ring regular-completion facts, which remain explicit inputs.

For the finite-type component comparison I checked the reduction before passing through the cover. At a generic special-fiber point of the reduced unrestricted scheme, Taylor's distinct-component assertion leaves one component. Its local ring is a DVR with uniformizer lambda. The finite etale cover preserves this local property. Each component of the cover has relative dimension four, and the dimension formula ensures that generic points of a component's special fiber are generic points of the total special fiber. Thus this checks componentwise reducedness, not merely a statement about one selected component. Removing the Laurent variable gives relative dimension three and the unique-component incidence needed for the fixed-determinant scheme.

The nilradicals here are nilpotent because the rings are Noetherian. Their extended ideals remain nilpotent under the finite tensor constructions and the stated Noetherian completions. Hence passage to reduction preserves the prime-spectrum and component-quotient assertions used downstream. It does not preserve the stronger scheme-theoretic assertion about the original special fiber. The proposed proof keeps this distinction throughout.

## Extra flatness claim

I independently noticed the same source-to-use difference recorded by the author: Thorne's read Proposition 3.15(2) and Taylor's final Proposition 3.1(1) do not state flatness of the unreduced ring. A characteristic-zero generic point and geometric irreducibility do not rule out embedded torsion. The source-only branch comparison cannot close that additional inference.

The author's Section 4 supplies a valid direct proof for the actual two-dimensional ring. I checked each integral step. Monic division shows that the inertia characteristic polynomial divides X^q-X over O. The argument cancels the nonzero element alpha-beta in O, rather than inverting it in an arbitrary coefficient algebra. Cayley–Hamilton then turns the Frobenius relation into commutation even over nonreduced algebras.

Writing each matrix as a scalar plus a trace-zero matrix is valid at 5. Computing the commutator gives exactly the three 2-by-2 minors in Section 4, up to signs and units. The determinant of the inertia matrix gives x^2+yz=delta^2; the fixed Frobenius determinant gives the displayed monic quadratic equation for w. These equations describe the full lifting scheme, not its reduction. The unit determinant already guarantees invertibility of the Frobenius matrix.

The proposed straightening proof for the minor quotient is sufficient over O and over its residue field. An exchange decreases the sum of column indices assigned to the first row. At termination those factors occupy the earliest entries of the total column multiset. The row count and column multiplicities determine the resulting monomial uniquely. Their images under the displayed substitution are distinct polynomial monomials. This proves both spanning and independence, and in particular that the residue quotient is a domain.

The reduction of x^2+yz-delta^2 is nonzero in that domain. If lambda g=f h, reduction first forces h to be divisible by lambda; cancellation in the torsion-free minor quotient then forces g to lie in (f). This proves actual O-torsion-freeness of the quotient. The monic quadratic extension is free of rank two, and localization and Noetherian completion preserve flatness. I accept this proof of flatness of the unreduced fixed-determinant ring. It does not apply the commuting relation in the trivial-character case, where the required polynomial divisibility fails.

## Consumers, history and limits

The immediate consumers are Pan's Lemma 4.2.10 and Proposition 4.2.4, with Lemma 4.2.7 retained for the completed-tensor calculation. The manuscript's current use of Pan is at lines 839–862 and 7393–7409 of the source with hash 63db4260c5d918c91935461a814e1296378f051f12c61b12c6f3d896df8a3503. The current TeX does not yet include this new supplement. Acceptance of it does not constitute incorporation.

My bounded history search covered the earlier pan-route-author, pan-kisin-transfer-review, pan-sw99-transfer-author-r2 and pan-utility-author packets, the installed Version 14 proof sources, and current TeX for the correction and its exact identifiers. I found no prior explicit treatment in that scope. This supports classifying the correction comparison and explicit flatness proof as newly documented here. It does not show that no earlier argument anywhere could supply flatness, or that the main theorem was false.

I did not author the proposed matrix proof or determinant connection. I requested precise source locators and independently identified the missing flatness inference. The author supplied the proof. This acceptance retains Pan's other local branches, the completed-tensor and regular-completion facts, and the unresolved final-version comparisons. It is not a complete audit of all uses of Thorne, all of Pan, or the global modularity theorem.
