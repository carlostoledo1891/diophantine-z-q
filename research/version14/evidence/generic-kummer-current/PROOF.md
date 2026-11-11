# Generic finite Kummer input for the actual Heegner fields

Author: /root/v14_arithmetic_author. New bounded connecting proof; source-set adoption and independent review remain separate.

## Published input and domain

Silverman, The Arithmetic of Elliptic Curves, second edition (Springer,2009), printed66, SectionIII.4, states that every nonzero isogeny is surjective and finite. Example4.1, printed67, constructs [m] over the field of definition; Proposition4.2(a), printed68, says it is nonconstant for m nonzero. The exact retained PDF SHA256 is72ee67bfa1e3fdf582ac7e4b032d7ca0b35a168ed6443ac39c121fbb788cab25. These three original pages were rendered and visually read. This uses their stated multiplication and isogeny results, not an uninspected erratum or an assertion about arbitrary rational maps.

Let F be a characteristic-zero field, E/F an elliptic curve and n=2^a with a>=1. Its separable closure is algebraically closed. The published input therefore makes [n]:E(Fsep)->E(Fsep) surjective, with finite kernel E[n]. Equip these groups with their discrete continuous G_F actions. Each algebraic point has an open stabilizer.

## Cocycle construction and exactness

For P in E(F), choose Q in E(Fsep) with nQ=P and put delta(P)(g)=gQ-Q. This is a continuous E[n]-valued cocycle. Replacing Q by Q+T with T in E[n] changes it by a coboundary. Choosing sums of division points proves additivity. It vanishes in H1(F,E[n]) precisely when Q can be changed by n-torsion to an F-rational point, equivalently P belongs to nE(F).

If an E[n]-valued cocycle becomes a coboundary gQ-Q as an E(Fsep)-valued cocycle, then nQ is F-rational, so its class is delta(nQ). Conversely every delta class is such a coboundary after inclusion in E(Fsep). Thus the kernel of H1(F,E[n])->H1(F,E) is exactly E(F)/nE(F).

The image is precisely H1(F,E)[n]. Indeed it is annihilated by n. Conversely, for an E(Fsep)-valued continuous cocycle c whose class is killed by n, write n c(g)=gP-P. Choose Q with nQ=P. Then c(g)-(gQ-Q) takes values in E[n] and represents the original class. These constructions prove the short exact sequence

0 -> E(F)/nE(F) -> H1(F,E[n]) -> H1(F,E)[n] -> 0.

## Naturality and the current uses

Restriction to a field extension, transport by a field isomorphism, and a homomorphism of elliptic curves commute with the construction by applying the map to the chosen division point Q. In particular delta is additive, takes n-multiples to zero, and commutes with the action of an automorphism of a finite normal field extension. No division by a field degree or by n in a coefficient group occurs.

For the current number field M_I and n=2^a, the point identity in main3882-3886 is an actual n-multiple, hence its Kummer class vanishes. Together with the separately supplied ring-class generators and norm identity, this gives the asserted invariance of the derivative class. The norm identity and description of the relative group are not proved here.

For a finite extension F of Q_p and finite unramified Fprime/F, a class v in H1(F,E[n]) that becomes Kummer over Fprime has image in H1(F,E) restricting to zero. The separately supplied local cohomology bound kills that image by c_E. Exactness then makes c_E v Kummer over F. This proves only the Kummer-sequence step used at main3942-3946. The local cohomology bound, unramifiedness, component group, connected-model and smooth-lifting claims remain separate.

The domain includes the permitted number fields and all their nonarchimedean completions, including residue characteristic2. The argument never uses good reduction, finite Sha, rank assumptions or rationality of E[n] over F. It does not strengthen the earlier Q-only forward Selmer record.
