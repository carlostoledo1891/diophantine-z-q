# Independent review: normalized scalar pole, 439 to 438

Accepted for the exact frozen packet below. This is an exact rational witness equivalence over the already accepted preparation-zero439 system, fixing the input and all coordinates outside the scalar pole. It introduces no arithmetic premise or new completeness construction.

## Frozen scope

- Source `06-product/scalar-redesign/preparation-zero439/candidate439-ir.json`: SHA256 `135c10f2b3d4c38cde375435055e626a3f49f364370aa9e29fc9237ad225b3d3`.
- Author report `06-product/scalar-redesign/normalized-pole438/REPORT.md`: SHA256 `726ba8026c7afaf133594fdd6e5392f3dfe882826d99ac4071678c40b063809c`.
- Candidate `candidate438-ir.json`: SHA256 `6867a2365bf3bc33225aba4d055d4e698f2fbcd67b958d6f528e477b0e697ea9`.
- Polynomial `polynomial438.json`: SHA256 `e0684677d00d82b700d8442aa71d2c9226b6e000e46bfbfb2ad59bd55e6e253a`.

The source arithmetic acceptance is recorded separately in `review-preparation-zero.md`. That review, including its simultaneous real/local completeness argument, is an explicit dependency. This review does not claim that arbitrary preparations can be specialized by algebra alone.

## Nonzero divisor from unchanged equations

Put x=v526 and let K be the positive coefficient of v51*v531 in the source `scalar.Bh.definition`. The retained semantic scalar input is b=-K*x. The earlier review verified its actual stored normalization, not just the intended formula.

The unchanged input equations give beta=51(2X+1)^2+2504 and
r=beta(beta-1)(beta-2401)(32beta+343)(2beta-1)>0
for every rational X. Also c=r+4896>0. The retained H chart gives f(H)=1/x(H), so q=Norm(f(H)) is nonzero. The unchanged scalar root equations give
W=(B^2+r*q^2)/r^32>0,
and the unchanged b equation gives b=c*r*W^2>0. Thus x<0 and in particular x is nonzero in both systems. This argument uses none of the deleted coordinate531 or the five private pole equations. It therefore rules out an extraneous x=0 component of the candidate.

## Both witness maps, including zero private values

Assign weights one to coordinates 51,52,53,54,532, and weights two to 527,534. From a source solution, set each new private value equal to its old value divided by x to its weight, and discard531. From a candidate solution, multiply each such value by the corresponding power of x and set old531=x^2. All other coordinates are fixed. Both maps are rational and inverse because x is nonzero.

The source `scalar.t2.definition` becomes the identity x^2-x^2=0. Substituting the reverse map into each of the five remaining source pole equations gives exactly x^2 times its candidate equation, coefficient for coefficient, without primitive rescaling. The checked equations are:

- `scalar.p2.definition`;
- `scalar.firstConic`;
- `scalar.Bh.definition`;
- `scalar.q2.definition`;
- `scalar.secondConic`.

In particular, 527 scales by x^2 while 53 scales by x, preserving 527=53^2; likewise 534 and54. Coordinate532 has weight one, not two. The h equation transforms from
17*v51*x+K*v51*v531-17*v52*v532=0
to
17*v51+K*x*v51-17*v52*v532=0.
The first conic's e*x term becomes linear and its x^2 term becomes constant. Its x*527 term remains quadratic. The other three coefficient lists are unchanged.

No division by e, p, s, q, the factored v, or any square slot occurs. All their zero branches are preserved. The negative sign of x is harmless: the maps require invertibility only, and the defining square slots receive x^2.

## Independent finite evidence

`review_normalized_pole_check.py` imports no author producer or verifier. It independently checks the frozen hashes, all five forward polynomial identities, and all five reverse identities as Laurent polynomials in x. It verifies that the seven rescaled coordinates have no consumers outside these five rows, that deleted531 has no consumers outside these rows and its definition, and that every outside row is literally unchanged.

It also checks every retained coordinate's metadata (only the seven prescribed names change), every residual's metadata, all unaffected top-level fields, and the exact removed row and coordinate. Finally it expands the full sum of primitive integer residual squares and compares every coefficient with the frozen polynomial.

The recorded result in `review-normalized-pole-checks.json` is: 438 total variables, 437 witnesses, 416 quadratic residuals, 6,655 quartic monomials, degree four, content one, maximum coefficient 16*3^(2^26). Every listed coordinate occurs in the polynomial. The fixed large constant remains symbolic; no giant integer expansion is needed.

## Conclusion and composition boundary

The exact 438 packet has the same rational input projection as the accepted 439 source. Its one-coordinate saving is accepted. A later composition must rebind the retained b normalization and the unchanged equations proving b nonzero, and must transport all seven private slots with their stated weights. This acceptance does not automatically bind a different combined IR.
