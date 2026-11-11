# Bounded audit of the crystalline Hecke map

This author-side source audit concerns the map eta imported by CEGGPS Proposition6.17 from CEG+16 Theorem4.1. It accompanies the proposed restricted route, not a whole-proof approval. The pinned source is the 49-page author PDF of *Patching and the p-adic local Langlands correspondence*. Its final journal version is Cambridge Journal of Mathematics4(2), 197–287, DOI10.4310/CJM.2016.v4.n2.a2. The final edition has not been compared in this packet.

## Exact statement and normalization

Theorem4.1, author p31, interpolates the action of the type Hecke algebra on the one-dimensional type space in the classical locally algebraic representation attached to each potentially crystalline point. Its target is the generic fiber of the framed local deformation ring of that fixed type. The theorem does not assert an identification of the locally algebraic vectors in a p-adic Banach representation.

The source conventions in Section1.5, author pp5–6, use geometric Frobenius, Hodge–Tate weight -1 for epsilon, and

    r_p(pi) = rec_p(pi tensor |det|^((1-n)/2)).

Its algebraic representation is the dual of the highest-weight representation associated to the ordered Hodge–Tate weights. For n=2 and increasing weights u<v, the highest weight before taking the dual is (v-1,u). The dual has highest weight (-u,1-v), hence is

    Sym^(v-u-1) E^2 tensor det^(1-v).

This is exactly the CEGGPS body convention for the pure algebraic type used in the restricted route. It is not the conflicting introductory formula already excluded in the predecessor. The distinction between this negative-epsilon convention and the Paškūnas Galois label V_P is still handled by V_P=r_C tensor epsilon in source-closure003.

The algebraic Hecke identification in the proof of Proposition4.2, author pp34–35, sends an endomorphism-valued Hecke function to its product with the algebraic representation. Its Bernstein-center twist is |det|^((1-n)/2). Thus its stated interpolation uses the same r_p normalization, rather than rec_p without this twist. The natural action on Hom_K is retained; no transpose or inverse character is silently substituted.

## Proof dependencies actually used

The local proof occupies author pp30–38, before the return to the global patched-module setting. Its stages are as follows.

1. A Weil–Deligne representation varies analytically over the fixed-type deformation space. Proposition4.2 uses the family result labelled Chenevier Corollaire3.19 and its pseudotrace description of the Bernstein center, then proves the needed generation statement in Lemma4.5. These concern classical Weil and smooth-representation parameters. They do not identify Banach locally algebraic vectors.
2. Proposition4.2 combines that family map with the algebraic Hecke identification and the explicit r_p twist. Classical type theory identifies the character on the type space. The proof uses its own Section3, including the classical local Langlands correspondence. A mention of a smooth supercuspidal Bernstein component in this argument is not an invocation of the disputed p-adic supercuspidal identity.
3. Lemma4.8 bounds the relevant Hecke eigenvalues. Its inputs are Hu2009 Theorem1.2(ii) versus (iv), Proposition3.2(2), and the locally analytic Jacquet formula of Emerton2006a Proposition4.3.6. The source bibliography identifies the latter as *Jacquet modules of locally analytic representations of p-adic reductive groups. I*, Ann. Sci. ENS39(2006), 775–839. This is not the Emerton2011 local-global compatibility manuscript. The use is the Jacquet formula for an algebraic tensor a smooth representation and its weak-admissibility inequalities.
4. Propositions4.10–4.12 extend the bound to the type Hecke algebra. Kisin2008 Theorem3.3.8 supplies generic-fiber regularity. The bounded-functions result of de Jong1995 Proposition7.3.6 then places the rigid-analytic values in the algebraic generic-fiber ring, proving Theorem4.1.

I read the stated proof and its direct citations at these locators. This is an incoming-edge audit, not a new independent proof of all of the cited classical type theory, family comparison, or rigid geometry. The Chenevier item was labelled a preprint in this old author PDF. A chapter with that title is now published in *Shimura Varieties*, LMS Lecture Note Series457, pp266–296, DOI10.1017/9781108649711.011. That bibliographic fact is not a completed statement-by-statement final-edition comparison.

No call to Emerton2011's disputed supercuspidal locally algebraic identity occurs in the bounded proof read here. This conclusion is based on the proof stages and their actual references, not on an assertion that any occurrence of the name Emerton is harmless. It does not cover other sections of the paper or all of its transitive ancestors.

## Connection at CEGGPS Proposition6.17

CEGGPS author pp33–34 define alpha using the rank-one type module. Its proof checks alpha=eta on a dense set of crystalline points. For the auxiliary absolutely irreducible residual block, all characteristic-zero Galois lifts are irreducible. The reducible-Galois branch citing Breuil–Emerton is therefore not used.

At the selected distinct-root nonexceptional crystalline points, the earlier source-closure proposal supplies the actual Colmez Banach fiber, not merely equality of its Galois image. Berger–Breuil supplies the locally algebraic principal-series embedding with the indicated parameter. The type space has dimension one, so the Hecke character on the Banach type space is the character on this embedded classical type space. Theorem4.1 identifies that character with eta evaluated at the same point. Reducedness and density then give equality with alpha. The prior independent SC06–SC09 decision is conditional on these specified inputs; this note does not expand that decision.

The unramified character variable does not change the two-Frobenius-root ratio. The nonexceptional dense set in the fixed-determinant one-dimensional space therefore remains dense after adjoining that variable. The reduced generic-fiber ring and its faithful rank-one module are the objects used to pass from pointwise equality to equality of ring maps.

For later integration, the dimension-two Jacquet statement in the all-point spherical argument means the normalized smooth J0 in Colmez's notation. It does not mean the entire Jacquet module after tensoring by an algebraic representation. This clarification records the independent review's scope; it changes no frozen predecessor bytes.

## Remaining qualifications

The map's normalization and its role in the restricted crystalline proof are now explicitly traced. Final-edition comparisons for CEG+16, CEGGPS and BM remain separate. The currently proposed direct principal-series Ext proof and BP fixed-center application bridge also require their own independent decisions. This note does not certify the whole patched-module construction, the full Breuil–Mézard theorem for arbitrary types, the Hu–Tan theorem, the manuscript, or a release.
