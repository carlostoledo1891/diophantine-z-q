# Polarization pairing input for the two original callers

Author proposal. This is a source-level input to the already reviewed determinant calculation, not a new modularity argument.

## Published source

Milne, Abelian Varieties, in Arithmetic Geometry, Springer (1986), pp.103-150, Section16: the opening and Lemma16.1 on p.131 give the nondegenerate Galois-module torsion pairings and compatibility; p.132 constructs the Tate pairing and defines its composition with a homomorphism lambda. Lemma16.2(e), p.132, places the line-bundle pairing in Hom(wedge^2 T_l A,Z_l(1)); Proposition16.6, p.134, also identifies the skew-symmetric condition for a line-bundle homomorphism when char(k) is different from 2 and l. This is the published 1986 scan, SHA256 86259344a576e4ef75a9d81e9bf43143f872a72b14cf8fcc2703f3aea6349136. The 2022 corrected text was used to locate the statement and is not substituted for this edition.

## Available pairing

For an abelian variety A over a number field F and an F-defined polarization lambda, the canonical torsion pairings yield an F-Galois-equivariant perfect pairing of rational Tate modules V_5(A) x V_5(A^dual) into Q_5(1). Composing in the second argument with V_5(lambda) gives a nondegenerate alternating pairing on V_5(A) with values in Q_5(1).

## Connection and exceptional cases

A is projective over F, so an ample F-line bundle supplies an F-defined polarization if none was fixed already. After base extension to an algebraic closure, this polarization is the line-bundle homomorphism to which Lemma16.2(e) applies. Alternation can be checked after that extension. The torsion pairing and lambda are defined over F, so their composition is G_F-equivariant. The compatible perfect torsion pairings give a perfect rational Tate pairing. Because lambda is an isogeny, V_5(lambda) is invertible: an isogeny inverse up to a nonzero integer becomes an inverse after tensoring with Q_5. Thus the composition is nondegenerate even when 5 divides the degree of lambda. No principal polarization, prime-to-5 degree, or good reduction at 5 is required. G_F acts on Q_5(1) by epsilon_5, which is the multiplier of this alternating form.

## Actual consumers

For each original caller separately, use its own A and the finite field F on which its normalized representation restricts to the actual Tate representation, as in the generic lemma proof. The beta caller retains t=a/beta; the b caller retains t=a/b. This source supplies only the pairing premise of ARITH-IMPORT-BETA-POLARIZATION-DETERMINANT and ARITH-IMPORT-B-POLARIZATION-DETERMINANT at main lines635-642. Their already reviewed exterior-square determinant calculation then applies. This record neither supplies nor replaces the two-copy Tate restriction, which is a separate normalized-family input. It does not enlarge a controlled field in a quantitative conclusion.
