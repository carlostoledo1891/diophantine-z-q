# Degree-preserving raising-isogeny specialization

Author: /root/v14_arithmetic_author. New bounded connecting proof; independent review and source-scope adoption pending.

## Inputs

BLR, Neron Models, Definition1.2/1 and Proposition1.2/8, printed12,15, extend morphisms between good elliptic models uniquely. Silverman, The Arithmetic of Elliptic Curves, second edition2009, III.6.1–6.2, printed81–83, gives dual isogenies and their multiplication composites; III.6.4, printed86, gives degree[n]=n^2 over a field.

The retained digital Stacks statements 02LS and039E say respectively that a proper morphism with finite fibres is finite, and that a morphism X->Y over S is flat when X/S is flat locally finitely presented, Y/S locally finite type, and every fibre map is flat. Exact 2026-11-08 HTML pins and retained source review are in PROVENANCE.json; this is digital-source reuse, not a new printed-edition claim.

Silverman V.3.1(a) and the definition after it, printed144–145, identify supersingularity with absence of nonzero geometric p-torsion. III.4.10(a), printed72, gives the separable degree of an isogeny as its number of geometric kernel points. II.2.12, printed26, factors a curve map through the Frobenius of degree its inseparable degree, followed by a separable map; a degree-one map of smooth projective curves is an isomorphism.

## Actual finite diagram

Fix one permitted new prime ell and a finite collection of the actual degree-ell raising isogenies. Work after a finite local extension on which their source and target elliptic curves have good models and all the selected maps and level subgroups are defined. Such common good-model realization is retained from the CM reduction/finite-diagram inputs; no uniform extension for all conductors is claimed. Let f:A->B denote one extended map. Its dual extends too. Their composites equal [ell], because they do so generically and the models are smooth with dense generic fibre and separated targets.

On every geometric fibre [ell] has degree ell^2 and is not constant. Hence neither f nor its dual can be constant on that fibre. A nonconstant map of smooth proper integral curves has finite fibres. The total f is proper (closed graph followed by proper projection), so02LS makes it finite.

Each fibre map is flat: at a closed target point its local ring is a discrete valuation ring; the finite module on the inverse image is torsion-free because the source fibre is integral and the nonconstant map is dominant. A finite torsion-free module over a discrete valuation ring is free. At the generic point the assertion is flatness over a field. Both elliptic models are smooth over the base DVR, so all hypotheses of039E hold, and f is flat. Being finite and finitely presented it is finite locally free. Its rank is locally constant on the connected target and equals its generic degree ell, so the special isogeny still has degree ell.

The source special fibre is supersingular by the separately supplied CM reduction input. If the separable degree of the special isogeny were ell, its geometric kernel would have ell points, a group containing a nonzero point of order ell, contradicting supersingularity. Its separable degree is therefore1. II.2.12 factors it through relative ell-Frobenius with a degree-one remaining map, hence an isomorphism. Its scheme-theoretic kernel is thus exactly the Frobenius kernel.

The finite locally free kernel of f has rank ell and is the flat closure of its generic kernel: finite flat schemes over a DVR have schematically dense generic fibre. Thus the raising kernel specializes to that Frobenius kernel. The chosen cyclic N-subgroup is prime to ell and finite etale on the good model; its image under f specializes under the same Frobenius followed by the same isomorphism. Accordingly the reduced elliptic curve with level subgroup is the Frobenius image of the old pair in the coarse modular interpretation, independently of the chosen raising isogeny.

## Boundaries

This proof uses the actual good elliptic models, degree-ell raising maps and their duals, the separately proved supersingularity, and the prime-to-ell level subgroup extension. It does not infer these premises from its own output. It proves only the raising-kernel/quotient specialization; the fixed modular parametrization extends by the separate integral-map input. No isogeny of degree prime to ell is assumed here.
