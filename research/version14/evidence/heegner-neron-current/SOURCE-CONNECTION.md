# Neron model input for the fixed local Heegner argument

Author: /root/v14_arithmetic_author. This is a new source application, pending independent review and explicit source-scope adoption.

## Published input

J. S. Milne, Arithmetic Duality Theorems, second edition, BookSurge 2006, Appendix C Theorem C.6 and the following paragraph, printed319–320: over a Noetherian normal one-dimensional integral base with perfect residue fields, an abelian variety has a smooth separated finite-type Neron model. Formation commutes with etale base change; its identity open subgroup has connected fibres and its component sheaf is finite at each closed point.

The proof of I Proposition3.8, printed46–47, uses smooth reduction over a Henselian valuation ring and the identity subgroup. Smooth residue points lift by Hensel’s lemma. This geometry is used here without importing the proposition’s cohomological conclusion.

## Actual specialization

Let F be the nonarchimedean characteristic-zero local field and B/F the actual elliptic curve in the fixed-local-condition argument; let Fprime/F be finite unramified. Their integer rings are complete discrete valuation rings with finite, hence perfect, residue fields. Thus the published base hypotheses apply. The extension of integer rings is finite etale, so the Neron model over Fprime is the base change of the model over F.

Write B0(Fprime) for points of the identity open subgroup. It has smooth geometrically connected special fibre. Henselian smooth lifting gives a surjection from these integral points onto the identity special-fibre points over kprime. A rational point of B extends to the Neron model by its mapping property. Taking its special-fibre component gives an injection B(Fprime)/B0(Fprime) into the finite group Phi_B(kbar).

Etale base change leaves this geometric component group unchanged. Consequently its order c_B annihilates that quotient for every finite unramified extension, including extensions of even degree. Finitely many fixed local curves therefore permit one common multiple of their geometric component orders. This is not an assertion that the rational component counts stay unchanged.

## Boundaries

The Lang theorem, additive normal-basis argument, formal-group filtration and limiting correction, and the resulting H1 annihilation are separate inputs or local deductions in the existing proof. No good-reduction assumption, semistability assumption, division by the extension degree, or bound uniform over arbitrary varying elliptic curves is asserted. CM point reduction, extension of a modular parametrization, and Atkin–Lehner actions are not supplied.
