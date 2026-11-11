# Independent RED bridge review

Reviewer: `/root/astra_quartic_opt05_anchor`. Date: 2026-11-08.

I accept the mathematical connection in `RED-BRIDGE.md`, SHA256 `752f9bcc94d8fe334441b5cea21e2c63ca3bac082b66047f610234aaa8bca37d`, within the conditions below. Its author is `/root/astra_v14_baseline_compiler`; I did not author or repair this bridge. The supplied packet manifest is `21b92d293f924780b65f29f28a4e570dd161ae669782bdde1a32ecfc57826b09`. This decision concerns the new bridge, not the author's own review of the larger HT application.

## The topological implication

Let Pi be a topologically irreducible admissible unitary E-Banach representation with Pi_lalg nonzero, and let 0 -> Pi -> X -> Pi -> 0 be an exact Banach extension whose locally algebraic sequence is exact. The exact Banach sequence uses the closed embedding and quotient topology. Put C equal to the closure of X_lalg. Local algebraicity is preserved by the inclusion, so the first Pi_lalg lies in X_lalg. Since Pi_lalg is a nonzero invariant subspace of Pi, its closure is Pi. The embedded Pi is therefore contained in C.

The quotient map X -> X/Pi identifies C/Pi with a closed subspace: its inverse image is exactly the closed space C, and this is the quotient topology. Surjectivity on locally algebraic vectors implies that C/Pi contains the second Pi_lalg. That subspace is dense in the quotient Pi by the same irreducibility argument. Thus C/Pi = X/Pi and C = X. No assertion that the image of an arbitrary closed subspace under an arbitrary continuous map is closed is needed.

This applies to every generator of the subspace in BM Definition 4.17. Taking linear spans gives inclusion in Dospinescu's Ext_alg subspace. It does not require that every element of a span itself have a chosen representative with an additional property. The split extension represents zero and causes no exception. Absolute irreducibility is stronger than needed for this topological implication, but is retained for the source theorem application. Irreducibility of X is neither assumed nor used.

## Actual source comparison

I read the pinned BM author-v3 definition and its uses in 4.18--4.21, including the distinction between the RED subspace and unrestricted Ext. I independently obtained the public Dospinescu author PDF from `https://perso.ens-lyon.fr/gabriel.dospinescu/extalg1.pdf`; its exact raw SHA256 is `a7e5be90904309fa74ef0b074e60376a217c13d05e854c39636cfbc0f06524c2`. I read printed pages 2--6 and 40--42. The exact PDF and extracted text are local-only evidence, not a public redistribution payload.

Dospinescu's page 2 category Rep_E(delta) consists of unitary admissible fixed-central-character Banach representations of topologically finite length. The page 3 convention is p >= 5. His supersingular condition is a condition on the p-adic Banach representation, not the mod-p residual representation. A length-two self-extension of a representation in this category remains in that category. For the actual application, these category hypotheses, the Banach correspondence and nonzero locally algebraic vectors remain required inputs.

Page 5 Theorem 1.3 identifies the span of dense-locally-algebraic self-extensions with fixed-determinant de Rham self-extensions. The determinant is epsilon times the central character, under the source's reciprocity convention. Proposition 1.4 makes the latter space one-dimensional except for the stated special case. Section 7.4, Definition 7.16 and Proposition 7.17 repeat the fixed-determinant condition and compute it via trace-zero endomorphisms. The special case has a Weil--Deligne representation that is a direct sum of two characters with ratio norm or inverse norm. An irreducible supercuspidal Weil parameter is outside that case. Hence the RED subspace has dimension at most one.

This uses exactly the fixed-central-character category on the Banach side and the fixed determinant over E[epsilon]/epsilon^2 on the Galois side. It does not use the determinant of the underlying four-dimensional E-representation, and it does not replace the determinant-constrained Ext group with the unrestricted group. The theorem is applied over the finite coefficient field on which the actual target and type are being considered.

The author's Remark 1.6 records a problem with the converse implication, density implying exactness on locally algebraic vectors in the reducible-locally-algebraic special case. This bridge uses only exactness implying density, which is also explicitly stated on page 5. The argument therefore does not rely on that rejected converse, even before excluding the special case. The local-algebraic irreducibility needed by BM Lemma 4.18 is a separate input, not a consequence of this review.

## Decision and boundaries

The new topological implication is accepted. Its application to the specified supercuspidal RED bound is accepted relative to the exact Dospinescu theorem and the retained correspondence/type hypotheses. No proof edit or stronger premise is required. This is an independent review of a new connecting argument, not a renewal of every ancestor theorem.

The downloaded Dospinescu document remains an author version. This review does not establish equality with the final Compositio edition or independently reconstruct all of Theorem 1.3. The pinned BM document likewise remains author v3 with final Duke comparison open. The proposition's proof on pages 41--42 and its source imports were read for the determinant and exceptional-case interpretation, not certified transitively. The actual target still requires an absolutely irreducible supersingular Banach representation, the established Colmez object, and the nonzero locally algebraic/type identification. No general full-HT result, complementary local branch, module flatness assertion or global manuscript acceptance follows from this bounded decision.

## Reproducibility

`check.py` checks this review's source pins, every member of the target manifest, and the BM source excerpt against its exact raw line interval. These are identity checks, not automated mathematical proof. No frozen author file, manuscript or live service was modified.
