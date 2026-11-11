# General-field character and trace inputs

This is an author source representation for the exact AC application. It creates no independent acceptance.

## Finite-character reciprocity

For a number field K, global reciprocity identifies finite continuous characters of G_K with finite-order idele class characters. At an unramified finite place choose arithmetic reciprocity, so the Hecke value at a uniformizer is the Galois value at arithmetic Frobenius. A finite character of Gal(L/K) is trivial at a real place that splits in L. Twisting by the inverse Hecke character removes the corresponding Galois tensor character.

The retained published input is Milne, Arithmetic Duality Theorems, second edition (2006), I.1.3 and I.1.6, pp.18–19, local units/unramified quotient at p.26, and I.4.5, p.51, with the separately recorded official addendum. The exact source review is tw-source-table-review-root-001. This representation does not assert that an arbitrary unitary Hecke character has finite order. The finite Galois character here is first constructed by Schur's lemma in AC-CONNECTION section6.

## Qualitative Chebotarev

For a fixed number field and finite Galois extension, every conjugacy-stable nonempty Frobenius condition occurs at infinitely many unramified places outside any prescribed finite set. Consequently Frobenius conjugacy classes are dense for continuous conjugacy-invariant functions on a profinite Galois group, by passage to each finite quotient. Equality of continuous trace functions at almost all Frobenius elements therefore gives equality at every group element. There is no effective bound or uniform choice over varying fields.

The retained source is Serre, Quelques applications du theoreme de densite de Chebotarev, Publications mathematiques de l'IHES 54 (1981), 123–201, section2.1 Theorem1. The frozen source review records scan PDF10/footer331 separately from bibliographic pagination. The independently reviewed Serre book I.2.2 finite-density statement is also copied alongside this record as a precise alternative for the density-to-trace step.

## Characteristic-zero trace algebra

For any characteristic-zero field E, finite-dimensional semisimple representations of an E-algebra with equal trace on every element are isomorphic. Apply the standalone algebra lemma in Serre, Abelian l-adic representations and elliptic curves, I.2.3 p.I-11, to E[G_K]. Equality on group elements extends linearly to the algebra. Apply first to semisimplifications. If the common semisimplification is irreducible of dimension two, each original representation has one composition factor and is itself irreducible.

The exact previously reviewed public source representation is copied as serre-trace-input-v1.md. Its retained printed proof ancestor is Bourbaki, Algebre VIII section12 no1 Proposition3. The surrounding Q-rational compatible-system theorem is not used. No comparison between different coefficient completions is made; fix one finite common coefficient extension first.

## Local two-factor calculation

Fix an odd finite place v, a positive integer j, and 2^j dividing Nv-1. A uniformizer splits F_v^* into its valuation copy of Z and the unit group. Reduction of units onto the cyclic residue multiplicative group has kernel the pro-odd group of principal units. Every continuous character to Z/2^j kills that kernel. The valuation factor gives 2^j characters. Since 2^j divides Nv-1, the cyclic residue multiplicative group gives 2^j characters. With the trivial Galois action, H1 is continuous Hom. Local reciprocity therefore gives exactly 2^(2j) classes. The product count is independent of the choice of uniformizer and of inversion of the Artin map.
