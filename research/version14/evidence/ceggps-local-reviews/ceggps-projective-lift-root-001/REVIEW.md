# Independent review of integral projective lifting

Reviewer: `/root`, 2026-11-08. The target is ELEM-LIFT in `ceggps-elementary-suppliers-003`, manifest `12ebdc095d3b3cdab501ecd5ba754bf5eb63f01889e909999ba494f505f65d87`, proof `c0dcdab9913355a0f76a3ddf0ee87a15dd8a43d1017af51719c914d0a067dc13`, Section 2. This report accepts the lifting lemma and verifies its application to the last inference of the pinned BM Theorem 5.2. It does not accept the proof of all of Theorem 5.2, the smooth Ext argument, or the final manuscript.

## Reading and independence

I read the complete proposed Section 2, all nine ELEM-LIFT comparisons, and the actual BM author text at pp.17 and29. I inspected those PDF pages to check the character and duality notation, the quotient exact sequence and the concluding projective-cover assertion. The pinned BM text is arXiv:1209.5205v3, not an authenticated final Duke edition. I compared the two explicit changes from elementary002 to003; Section 1 and its ELEM-EXT card are unchanged and outside this review.

The source-review agent authored the main idempotent-lifting and compact-Nakayama proof. During review I requested a distinct compact character and supplied the short finite-generation bridge from an essential cover. That feedback is recorded in PRELIMINARY.md and in the author's DELTA. My report is not an independent origin review of those two contributions; a separate anchor review is required for them and is bound separately in the decision. I did not author the underlying lifting proof.

## The exact algebraic inference

Here O is the ring of integers of the finite coefficient extension of Q5, not an arbitrary noncompact valuation ring. The central-character quotient of O[[K]] is a compact Hausdorff ring. Multiplication by the coefficient uniformizer pi is central. Its powers give a separated complete filtration: each finite continuous quotient is killed by a power of pi, and compatible cosets lift by compactness. Passing to the closed central-character quotient preserves these properties. This justifies the pi-adic idempotent limit in the actual ring; no commutativity of K is assumed.

If u is an approximate idempotent and e=u^2-u, the prescribed update is u' = u+(1-2u)e. Direct polynomial expansion gives u'^2-u'=e^2(4e-3). All terms commute with u because they are polynomials in the same element. Thus the error gains a factor of two in its pi-adic order at each step in the finite matrix endomorphism ring. The limit is an idempotent lifting the given one. Its image P is a finite free direct summand in the compact category, with the required reduction. For left modules one can use row vectors and right multiplication by that matrix; the idempotent argument does not change.

Finite free modules are projective for continuous surjections of compact modules: choose lifts of their finitely many basis images. Their finite direct summands are projective as well. This lifts the reduction isomorphism P/pi P to M/pi M to a continuous map P to M.

The image is compact and hence closed. Its compact cokernel C has C/pi C=0. Every finite continuous O-quotient of C is pi-primary, so C=pi C implies each such quotient is zero; separation then implies C=0. Thus the map is surjective. With L its closed kernel, O-torsion-freeness of M gives Tor_1^O(M,O/pi)=M[pi]=0. Reducing the exact sequence therefore identifies L/pi L with the kernel of the reduction isomorphism, which is zero. The same compact-Nakayama argument gives L=0. The resulting continuous bijection is a homeomorphism because its source is compact and its target Hausdorff.

For the cover statement, a closed submodule mapping onto the finite semisimple target has full image modulo pi by essentiality of the reduced cover. Its compact quotient has zero reduction and vanishes. Images of maps from arbitrary compact modules are closed, so this is the essential-epimorphism property in the actual category, not merely for algebraic finite submodules. The integral epimorphism is consequently a projective cover.

## Matching the BM consumer

The BM proof constructs x earlier, identifies the reduction of Coker(x) with the dual of its K-injective envelope and derives O-torsion-freeness by the displayed snake-lemma sequence. Those prior assertions are retained inputs. They are not consequences of the new lemma.

The actual compact character is eta=zeta_BM^(-1), because the smooth representation is dualized. The successor now uses eta in the quotient ring and keeps it distinct from the smooth character in Section 1. This is a correction to the application notation; the lifting argument is uniform in eta.

The finite K-socle gives a finite semisimple target S. For its projective cover Pbar, lift finitely many generators of S to Pbar. The image of the induced map from a finite free R/pi R-module is compact and closed and maps onto S. Essentiality forces it to be all of Pbar; projectivity splits the map. Pbar is therefore finite projective, precisely the hypothesis of the lifting lemma. This bridge is now written in the proposal and separately reviewed because I contributed it during review.

Every map remains over the same central-character quotient. No scalar-5 condition on the G representation is introduced by the coefficient-uniformizer calculation. There is no step inverting pi, changing compact modules into Banach spaces, discarding torsion without a hypothesis, or replacing the actual cover by an unrelated object of the same dimension.

## Scope and retained obligations

Subject to the separately recorded review of the two contributed clarifications, ELEM-LIFT can replace the concluding appeal to Paškūnas 2010 Proposition 4.6 in the pinned BM5.2 proof. This removes that particular supplier use, not all uses of that article: its admissibility statement or other references must be handled on their own evidence.

The construction of the K-injective enlargement, the exact sequence giving x, finite-length and socle inputs, BP symmetry and tree arguments, the final BM edition comparison, all subsequent crystalline and patching arguments, and final C10/Hu–Tan/Pan closure remain separate. No final-edition equivalence, whole-source validation or release approval is asserted.

CHECKS.json verifies six target-manifest members, eight local source/context files, the three proof-span hashes, unchanged ELEM-EXT bytes and the exact BM passages. Only the two BM passages are used as source evidence for this report; verification of the other context-file hashes is not a claim of reading or approving their mathematics. Page images and source PDFs are local-only and excluded from the public payload.
