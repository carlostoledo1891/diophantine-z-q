# Independent review of scalar forward-power consolidation

Accepted as an exact equivalence of rational solution sets over the unchanged
outside coordinates. I authored none of this transformation or its producer.
This review does not revalidate the inherited arithmetic theorem of the
released 498-variable source. No correction is requested.

The exact candidate is `06-product/candidate496-ir.json`, SHA-256
`780dbfb2cf04383062912a6ac68b780a025cf0eb94b2d567a05927c732356e48`.
Its polynomial has SHA-256
`5f294535464f2d3db05be9492ef73fe9045ef4578a6c44a7d04a0621eb6a875d`.
The reviewed contributor report has SHA-256
`86f520df694b7a0a093454b9de5a4c5fe2aa0bfdaeb6aca6e53121718556c81e`.
The source is the released 498-variable residual system, SHA-256
`7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a`.

I read the producer, independent checker, and complete argument; reran the
checker from a copied snapshot; and separately checked source pins, private
consumer incidence, unique coordinate and residual names, protected input,
and unchanged metadata for every outside coordinate. All checks passed.
The executable evidence is `audit.py`, `REVIEW.json`, and `checker.log`.

The exact stored r is obtained from the original inverse residual, without
guessing its compiler normalization. Substituting its three retained
defining gates gives

```text
r = beta*(beta-1)*(beta-2401)*(32*beta+343)*(2*beta-1),
beta = 2*X^2+3.
```

The checker verifies this polynomial identity and the retained input-square
equation. Therefore every rational solution of the surrounding equations has
beta at least 3. Four factors are nonzero immediately. If the remaining
factor were zero, X squared would equal 1199. Writing X in lowest terms
shows that a rational square equal to an integer must be an integer square;
but 34 squared is less than 1199 and 1199 is less than 35 squared. Thus r is
nonzero on the entire rational solution set, including the new system after
the explicit inverse equation is removed. No new arithmetic assumption or
unjustified division is involved.

The old private equations uniquely give powers through r^-32, followed by
U=z0/r^32, V=z1/r^32, and V2=V^2. The consumed node is
B=U^2+r*V2. The new private equations uniquely give powers through r^64 and
S=z1^2. Their final equation is r^64*B=z0^2+r*S. Multiplication or division
by the nonzero r^64 proves the equivalence while preserving B exactly.
The ratio components z0,z1 are the actual unchanged coordinates 508 and 509.
Coordinate 539 is repurposed from V^2 to z1^2 and occurs only in the two
replaced rows. All deleted inverse-power and leaf coordinates have consumers
only in the replaced subsystem. The node B at coordinate 540, its square,
the scalar root, pole equations, anchor, detector data, and input remain
unchanged.

The forward and reverse witness maps are mutually inverse after accounting
for the different meaning of coordinate 539. They cover negative as well as
positive r. The argument does not require a sign or nonzero condition on B,
z0, or z1. In particular, no zero branch of a ratio component is lost.

The independent expansion matched every polynomial coefficient and confirmed
496 total variables, 495 witnesses, 465 quadratic residuals, degree four,
24,699 monomials, and primitive content one. The fixed parameter is still
C=3^(2^25). The unique C-squared coefficient is 16, with no lower-C term on
the same coordinate monomial; the verified bounds on the remaining
coefficients give the exact maximum 16*C^2=16*3^(2^26), without expanding C.

This is independent internal model acceptance of the local transformation,
not independent human review. It introduces no changed application of an
external number-theoretic theorem. The source theorem and any later
composition retain their separate review obligations. No released file or
contributor artifact was modified.
