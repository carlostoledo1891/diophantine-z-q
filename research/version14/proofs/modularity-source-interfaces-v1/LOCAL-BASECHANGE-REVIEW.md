# Independent review of the modular local base-change bridge

Reviewer: `/root/astra_v14_baseline_compiler`. Author: `/root/astra_v14_source_review`.

Accepted: the new pair-specific local parameter restriction argument in `h-modular-local-basechange-author-001`, manifest `db0093ffcec9d1c409fce0c1cce038c83507f0efe65727316f54ee6840e50e96`, proof `1e951eacf3afc004b1a8dd7327a4e9ea5485e05cdbff10c04268052a87091d47`. Acceptance is under the explicitly retained global base-change, attachment and local comparison inputs. The argument removes the need to treat IAS Chapter 2(e) as a general local theorem for these actual modular pairs. It does not authenticate the original Langlands edition or prove a theorem for arbitrary local representations without globalization.

## Independence and source reading

I did not author this new bridge or supply a repair to it. I previously supplied feedback on H003's post-cleaning removal of finite inertia and authored other bounded local proposals. Their accepted ordering, field and local conclusions remain incoming premises here; this review does not independently reapprove my own earlier contributions. The new global-to-local inference is the present author's work.

I read the whole new proof before its application record. I then read H-D4's proof and root review, H-D5 arithmetic002 and Gaussian's review, and root's separate H-D5 object clarification. The latter is bound as additional review evidence even though the new bridge's source list preserves the earlier review's historical pending wording.

I independently read final Skinner pp.241–243 and visually inspected p.242. Equation (1) supplies the away-from-coefficient-prime comparison, and Theorem 1 supplies potential semistability and the same full Frobenius-semisimple comparison at coefficient-prime places. The hypotheses permit the weight-two type k_i=2,w=0, every totally real intermediate field and coefficient prime 2. There is no finite-discrete-series-place requirement. Skinner p.243 explicitly distinguishes the cases previously covered by Saito from the remaining cases.

I also read final Fontaine Expose III pp.145–147 and 156–159, including the semilinear module action, scalar extension, tensor and dual rules, period-module definitions and normalization of N. Pages 158–159 were checked visually. Final Kisin pp.630–633 and H003 Section 6 identify the actual applications rather than leaving them as a general type list.

## Global identity before local comparison

Both pi and Pi are already cuspidal modular representations. The accepted H-D4 ascent applies to this actual pair and supplies compatible Galois attachments over both fields. At the almost-all places needed for Chebotarev, both the forms and the field extension are unramified. Raising unitary Satake roots to the residue-degree power commutes with passage to arithmetic roots because q_w=q_v^f. The resulting global characteristic polynomials are those of restriction.

The residual nonsolvability premise supplies absolute irreducibility of the restricted representation in the admissible tower. Thus equality of semisimplifications identifies the actual two-dimensional representations. This is an actual characteristic-zero isomorphism r_Pi=r_pi restricted to G_L. Neither residual equality with the target nor ramified local compatibility is used to obtain it. This avoids both a circular target-modularity argument and a hidden use of the local base-change conclusion.

## WD restriction and the two duals

At the coefficient prime, the finite extensions used to define D_pst after extending the base field form a cofinal family in those used before extension. With a common algebraic closure, B_st and compatible embeddings, the same union of period vectors is obtained. The semilinear Galois action restricts; the absolute Frobenius and N are unchanged. The resulting Weil action therefore restricts with the appropriate residue degree. This is compatible with Fontaine's scalar-extension and discrete-action definitions.

Away from the coefficient prime, restricting the same tame additive character and its exponential-monodromy expression gives the corresponding statement. A separately normalized tame generator or valuation can multiply N by a nonzero scalar. Fontaine 5.2.1–3 explicitly records the analogous period normalization and its isomorphism invariance. In particular this cannot change N=0 or its rank. Even a ramification degree divisible by 2 remains a nonzero scalar in the characteristic-zero coefficient field; it cannot annihilate N.

For Frobenius semisimplification, take a Frobenius power centralizing finite inertia. Its unipotent Jordan factor commutes with inertia and N. Discarding this factor commutes with restriction and the change to a residue-degree power. Thus no inertia or monodromy is lost in the comparison used here. The proof does not claim equality of the original, possibly nonsemisimple Frobenius operators.

Skinner's R_pi is in the geometric convention, while the H attachment is its dual r_pi. The first dual changes the parameter P_K to P_K^vee, and likewise over L; N becomes minus its transpose. The global restriction isomorphism then gives P_L^vee=(P_K^vee)|W_L. Taking the second dual gives P_L=P_K|W_L. This recovers the original inertia characters, rather than their inverses. Duality commutes with the restriction and introduces no extra Tate twist. These are the two distinct uses of the contragredient in the proof, not a single unrecorded convention change.

## Normalized twist

Skinner explicitly takes uniformizers to geometric Frobenius in local reciprocity. For eta_v=Rec_v(|.|_v), the geometric-Frobenius value is q_v^(-1). Its restriction at w has value q_v^(-f)=q_w^(-1). Equivalently |Norm(x)|_v=|x|_w. The exponent is the residue degree f, not the total degree ef.

Choosing the positive real half-power and the same coefficient embedding makes these half-powers compatible as well. Using the stated unramified-twist property of local Langlands, the factors eta^(-1/2) in Skinner's normalized parameters cancel on the two sides. This gives the asserted Rec_w(Pi_w)=Rec_v(pi_v)|W_L as Frobenius-semisimple WD pairs with compatible normalizations. No independent square-root choice, quadratic character or cyclotomic twist remains. The local Langlands unramified-twist property is an explicit retained premise; the proof does not use general local base change to justify it.

## Actual H consumers

The supplied H-D4, H-D5 and H003 consumer spans were read and independently hashed. Their roles match the new assertion.

* At H003 step 3, the preparation acts on an already modular comparison form. Places kept split retain the same local factor. The Kisin ordinary and cuspidal type-change lemmas remain separate inputs; after a type change this bridge applies to the newly constructed form and its own attachment.
* At step 4, killing finite inertia for an N=0 modular parameter produces trivial inertia and N=0 after base change. At a place above 2, H-D5 supplies crystallinity and the retained integral H-D2 theorem supplies the stated BT conclusion. The target's BT property still comes from its own hypotheses and prescribed extension, not from congruence to the modular form.
* At step 5, the principal-series inertia introduced by cleaning must actually be killed. With N=0 this gives unramifiedness at the non-2 places. At a Steinberg place N remains nonzero under restriction. Determinant normalization and the chosen unramified quadratic-character comparison remain separate; parameter restriction alone does not equate those characters.

For a nonnormal intermediate field, the accepted H-D4 construction uses the solvable normal closure and its own cyclic towers. Every local use here remains a restriction of an actual global Galois isomorphism. Descent twists are tracked on both sides. The target is eligible for modular descent only after Proposition 3.2.9 has supplied its modularity.

## Decision limits

No mathematical repair was needed in this frozen bridge. The accepted new inference is from the modular global pair and the full local comparison to its local restriction statement, together with the exact normalization and H consumption checks above. Global Langlands existence/descent and its original-edition qualification, the full Galois-attachment input, Skinner's published theorem and its proof ancestry, local Langlands twist normalization, the type-change and field constructions, integral BT and patching remain separately recorded inputs. No whole-H, whole-Serre, manuscript or release approval follows.

The accompanying checks verify raw file pins and the three supplied consumer excerpts. They supplement the source and mathematical reading, rather than stand in for it.
