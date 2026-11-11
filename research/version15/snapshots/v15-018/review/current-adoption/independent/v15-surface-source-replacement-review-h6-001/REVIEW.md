# Published-source replacement for the surface height lemma

Decision: accepted as a proposed new source application, including the surface-height replacement text in consolidated-tex-proposal-030. This is not retroactive acceptance of the old direct Rémond2022 application in frozen8867, and does not install a manuscript change.

## Exact published supplier and field

I read Gaudron–Rémond, Nouveaux théorèmes d'isogénie, Mémoires de la SMF176 (2023), from the final publisher PDF, SHA b1e2e32bec626cf6d27fb7d6d8702b5c707e0c3dc002d979088e62d8cda514a4. The relevant locations are §1.2 p2, §1.5 pp7–8, Chapter16 pp97–98, and bibliography p122. The proof page98 was also rendered and inspected visually.

The convention on p2 explicitly keeps every unqualified abelian variety, morphism, isogeny, abelian subvariety and simplicity notion over the fixed base field K. It distinguishes base extension rather than silently passing to the algebraic closure. Chapter16 starts with an arbitrary abelian variety C over the number field K. In the proof of Lemma16.2(1), the authors choose a K-isogenous MM variety D whose height is no larger than that of C and then express D as an actual product of K-simple varieties. Repeated simple isogeny classes are explicitly allowed. No enlargement of K is introduced in this step.

Set K=L' and C=J. The chosen complex embedding used for other Chapter16 quantities adds no field extension or degree factor to this construction. The finiteness assumption used earlier in the monograph is available for number fields as stated there. This supplier applies to arbitrary J of dimension g, with no principal-polarization or absolute-simplicity condition.

The step cites Rémond2022 Corollary1.3 for D and Rémond2017 Theorem1.6 for its product decomposition. These dependencies remain part of the argument. They are references[28] and[25] on p122: Propriétés de la hauteur de Faltings, Ann. Scuola Norm. Sup. Pisa23 (2022),1589–1596; and Variétés abéliennes et ordres maximaux, Rev. Mat. Iberoam.33 (2017),1173–1195. This review does not claim direct final-edition comparison of either separate article.

## Subproduct and multiplicities

An L'-isogeny factor A of J is an L'-isogeny factor of D. In the semisimple isogeny category over L', its multiplicity in each simple isogeny class is at most the multiplicity in D. Selecting that many of the actual factors D_i produces an actual subproduct B over L' which is L'-isogenous to A. Repeated elliptic factors cause no exception; two isogenous elliptic factors may both be selected when A has that multiplicity. The complement E is the product of the remaining factors. Thus D is isomorphic to B times E, dim(B)=2 and dim(E)=g-2. B need not be a subvariety of J, and the proposal does not assert that it is.

The separate independent idempotent/block-matrix argument in v15-surface-factor-review-arithmetic-001 establishes exactly this multiplicity step. Its receipt ab872825e746eb399557136b3409f4cb6da3f58ffe57f62bb85ddce7a2ed3beb is retained as supporting evidence. No assumption that geometric endomorphisms descend to L' is needed.

## Height convention and constants

The2023 supplier states on p7 that hF is the stable height with Faltings' original normalization. The final2014 Gaudron–Rémond paper, §2.3 p352, explicitly compares its internal height h with hF by hF=h-(dim/2)log(pi), records additivity on products and the absolute half-log isogeny bound, and says that the latter is independent of this normalization. I visually inspected p352. Corollary8.4 p400 gives the lower bound for all abelian varieties, not only principally polarized ones. Together these yield hF(E)>=-dim(E)log(pi*sqrt(2))>=-3dim(E)/2. For dim(E)=0 the height is zero, as the proposal separately states.

Product additivity and hF(D)<=hF(J) therefore give

 hF(B)=hF(D)-hF(E)<=hF(J)+3(g-2)/2<=H_J.

Apply2023 Theorem1.9(1) with its source variety equal to B, target equal to A, and both base field and extension field equal to L'. Both isogeny directions are provided, so the needed B-to-A direction is available. For dimension2, Xi(B)^2 is (14^32*d'*max(1,log(d'),hF(B)))^16. The half-log height cost contributes exactly8 times the logarithm of the bracket. Replacing hF(B) by H_J proves the unchanged displayed surface bound. No factor involving the unrelated fiber-splitting field appears. Its later contact consumer is unchanged because the lemma's hypotheses, conclusion and constants are unchanged.

## Proposal and policy boundary

The surface replacement in030, after-text SHA60547e0593235899cc538103266aea3bb6789f21ef23a72948d22434c28e90b7, states the needed construction, multiplicity selection, height inequality and unchanged isogeny step correctly. Its zero-dimensional complement case is explicit. The half-log citation to2014 §2.3 is appropriate. A bibliographic/source-use record should retain the exact2017 title and Theorem1.6 and the2022 Corollary1.3 through the2023 proof, as named above.

Using this exact published proof passage as an immediate supplier is consistent with the source-first policy determination communicated for this proposal. It is a new current-use derivation, not a claim that the unavailable final2022 Corollary1.2 has now been read, that Rémond dependence vanished, or that old8867 was already source-complete. A changed manuscript and source contract must name this new supplier and be compared after installation. Broader source-first closure and assembled-proof approval remain separate.

Authorship: I did not author the root replacement proposal or GI's030 text. I authored the earlier conditional surface review, whose unavailable-final2022 limitation remains historical. This decision checks the new published source and application independently; no own raw/sparse233 work is reviewed.
