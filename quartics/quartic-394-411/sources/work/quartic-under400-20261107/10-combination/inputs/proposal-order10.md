# Order-ten toric candidate in 498 coordinates

The frozen 501-coordinate candidate admits a further three-coordinate reduction after changing the two low-precision tests from order twelve to order ten. The resulting system has 498 total coordinates, 497 witnesses, and 467 quadratic residuals. Its primitive integer sum of squares has degree four and 24,712 monomials.

This consists of two different steps. The order change is an arithmetic source change, justified in `03-depth/lower-precision/ARITHMETIC.md`; it is not an algebraic witness equivalence with the 501-coordinate source. Once the order-ten semantic source is fixed, the circuit replacement below has explicit inverse rational witness maps and introduces no arithmetic assumption.

The frozen starting file is `10-combination/candidate501-ir.json`, SHA-256 `6a31040f85e30cc6f9d076bf6c92218be110e0829e93333d7e99f93a6b2f0d9a`. All earlier files under `07-toric/` and `07-toric/mixed/` remain unchanged.

## Exact arithmetic source change

Retain the alternate logarithm G2, which approximates the full logarithm to order twelve. Retain all other logarithms, tests, guards, and fixed data. Change only the beta test and its associated cross-comparison test to order ten. Their grouped polynomial still has degree two and the same coefficients; its weight changes from q12=q E^22 to q10=q E^18. The order-forty weight remains q40=q E^78.

The unchanged primary formal depth gives precision at least eighty, and the unchanged G2 alternate numerator gives precision twelve, which is more than the required ten. The weaker cross test still transfers integrality, after which the local congruence holds to order ten. The beta height contradiction becomes

```
log B < 10 log(48 H) + 19 h(beta)
      < (29/40) |a|
      < |a| - 3.
```

The last inequality follows from the unchanged enormous anchor lower bound. The order-forty Lucas contradiction is unchanged. Completeness retains the existing deeper points and uses the original pole-realization theorem at order ten. See the depth agent's report for the full argument and source qualifications. Independent arithmetic acceptance remains a separate review task.

## Six-coordinate circuit

For each detector let E be eWeight and q be q1. Reuse the existing coordinates Q5=q^5 and R=q10^2. Keep the q10 and q40 output coordinates, and use only four internal coordinates a,b,c,d:

```
E a = q
E b = a^2
q c = b^2
c d = Q5
c q10 = d^2
c q40 = R^2.
```

Every equation is quadratic in the existing or replacement coordinates. They give

```
a = q E^-1
b = q^2 E^-3
c = q^3 E^-6
d = q^2 E^6
q10 = q E^18
q40 = q E^78.
```

The earlier mixed circuit had five internal coordinates and two outputs. This has four internal coordinates and two outputs, saving one coordinate for each of the three detectors. The existing `E1.power5` is q^5 because its retained defining equation multiplies q^2 and q^3. The retained low-group square becomes `E10.power2` by renaming and remains exactly R=q10^2.

## Rational witness equivalence for the order-ten semantic source

Define the semantic source by removing the old internal weight coordinates, retaining every other coordinate and equation with low-group names changed to order ten, and imposing q10=q E^18 and q40=q E^78. These two high-degree semantic assignments are subsequently replaced by the six quadratic equations above.

In every rational solution, the unchanged inverse of w0 and the norm equations imply n is nonzero, since w0^2-2w1^2 cannot vanish with w0 nonzero. The retained equation (E delta) B=n^2 then forces E nonzero. The unchanged definition q delta^3=E forces q nonzero. Neither argument uses an internal coordinate being replaced.

Given any semantic-source solution, retain every outside coordinate, including q10, q40, Q5 and R, and set a,b,c,d to the four displayed Laurent values. Since R=q10^2=q^2 E^36, all six equations hold.

Conversely, in a quadratic-system solution, divide the first two equations by the proven nonzero E to obtain a=q E^-1 and b=q^2 E^-3. Divide the third equation by q to obtain c=q^3 E^-6, so c is nonzero. The next two equations give d=q^2 E^6 and q10=q E^18. The retained R=q10^2 gives R=q^2 E^36, and the last equation gives q40=q E^78. Forgetting a,b,c,d yields exactly a semantic-source solution. The extension is unique. These maps preserve the input and every outside coordinate.

## Checks and files

`check_candidate.py` pins the frozen 501 source hash. It verifies all seven old weight equations and the retained q^2, q^3, q^5, and q12-square equations exactly. It proves that no old internal weight coordinate has any outside consumer. It changes only those internal equations and coordinate slots, plus low-group names, and checks every new residual by exact two-component Laurent exponents.

The checker then constructs `candidate498.json`, clears and primitively normalizes residual denominators, and independently expands their complete sum of squares into `polynomial498.json`. It verifies degree four, counts, and a constant coefficient of magnitude one, which proves content one after the fixed S specialization. `report.json` records the counts and coordinate certificates.

The unchanged seventeen-coordinate constant chain would give 515 total coordinates with ordinary integer coefficients. The earlier 520- and 516-coordinate algebraic results are unaffected.
