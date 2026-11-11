# Independent review of scaled correction 446

Accepted as an exact rational coordinate equivalence at the frozen hashes
below. The rewrite removes coordinate 524 and preserves the input and every
outside semantic value, including the actual scalar pole input and all its
witnesses. Acceptance of the source's arithmetic theorem remains a separate
dependency. No unexamined single-correction candidate is approved here.

| Object | SHA-256 |
|---|---|
| Source `06-product/scalar-redesign/odd-input447/candidate447-ir.json` | `20e9732f0ce5b493190d4c876fdc1a5c6838627145a72f7ee2bec7e548810189` |
| `scaled-correction446/REPORT.md` | `cb6196998bd96d901ff4b75d9e1d8e3d78c4e6bf8c045e85d8fcbc3898090dff` |
| `scaled-correction446/candidate446-ir.json` | `20699504b0998782752f49e5b2c5ddcadea2f88b073db49418c38f0b55317f8b` |
| `scaled-correction446/polynomial446.json` | `1d5d8b1c1460ff464d6164618c38a91b948fb558cc64ff6655e5106af7c8f6ad` |

I read the frozen report, producer and checker, the actual source and target
rows, and the source odd-input report. I then wrote an independent checker,
`review_scaled_correction_check.py`, which imports no producer or component
checker. Its exact checks pass.

## The required global denominator

The actual source retains Y=X^2 and uses

    beta=4Y+4X+2403=(2X+1)^2+2402.

Thus beta>=2402>2401 for every rational X, including X=-1/2. Each factor of

    r=beta*(beta-1)*(beta-2401)*(32beta+343)*(2beta-1)

is strictly positive. Consequently r>0 on every rational source or target
solution. This claim is independent of the source's final integrality
argument, its correction squareclasses and its scalar-depth theorem.

The independent checker derives the physical affine r directly from the
old corrected-product row, eliminates the three retained contact
intermediates, and compares the result with this literal five-factor
polynomial. It separately verifies Y=X^2. The nonzero premise is therefore
attached to the actual stored expression, not inferred from its name.

## Exact maps and correction branches

The old correction coordinates are c1,c2,c3,c4 in slots 62,63,64,65, with
c0=1 and successive multipliers 33,17,105,273. The equations are

    (ci-c(i-1))*(ci-gi*c(i-1))=0.

Forward, replace each slot by Ci=r*ci. The new initial value is C0=r.
The first equation becomes (C1-r)(C1-33r)=0. Every later equation keeps
its homogeneous quadratic coefficients. After this substitution each
new chain residual is exactly r^2 times the corresponding old residual.

Backward, set ci=Ci/r. These are rational and satisfy the original chain
because r is nonzero. The two maps are inverse on the correction
coordinates. All other retained coordinates are fixed. The first new row
remains quadratic since the stored r is affine; subsequent rows already
have degree two. No nonzero condition on an intermediate correction is
needed for these maps. Its existing nonvanishing also follows from the
chain and the positive multipliers.

## The actual normalized product and pole-input rows

Write M=20619812, A=7895415, K=4A=31581660. The old slot F=v524 satisfies

    c*s0-M*F=0,                  r=-4*(s0+A).

Its old pole-input row is

    (A*c+M*F)*v525-M*v526=0.

It follows exactly, without dividing by any pole witness, that

    r*c=-4M*F-K*c,
    (r*c)*v525+4M*v526=0.

The new output C=v65 is r*c, so the replacement row is

    C*v525+82479248*v526=0.

Coordinate v525 retains its normalized W-square value and v526 retains
its normalized scalar pole input. Thus the actual pole input is unchanged,
including its nontrivial sign convention. The source's preparation and
pole equations continue to consume precisely the same rational number.

The deleted coordinate is reconstructed by

    c=C/r,
    F=-(C+31581660*c)/82479248.

For clarity, the independently checked polynomial identities for the two
directions are as follows. The new pole-input residual after substituting
C=r*c equals -4 times the sum of the old pole-input residual and v525
times the old product residual. Conversely, after the displayed inverse
substitution and clearing r, the old product residual is identically
zero, and the old pole-input residual is -r/4 times the new residual.
This verifies both original equations with the correct affine offset,
not merely the product r*c up to a scalar.

All permitted zero values of private pole witnesses remain untouched.
The maps only divide by r and by the fixed nonzero rational 82479248.
They preserve the retained scalar nonzero guard. No local-global theorem,
new prime choice or fresh completeness construction is needed.

## Consumers, polynomial and scope

The independent incidence check finds that slot 524 occurs only in its
defining row and the old pole-input row. Slots 62–65 occur only in the four
chain rows and those two consumers. All remaining rows are identical up
to their harmless nonzero rational residual normalizations. All remaining
coordinate records are identical except the intentional correction-slot
names. The fixed coefficient parameter and all other top-level source
data are preserved.

The independently expanded primitive sum of squares matches every frozen
coefficient. The result has 446 total variables, 423 quadratic residuals,
6,730 quartic monomials, degree four, content one and maximum coefficient
16*3^(2^26). It saves exactly one variable and one row from the 447 source.
The check retains the coefficient tower symbolically and does not expand
the giant fixed integer.

The algebra applies equally to a one-coordinate correction satisfying
(c-a)(c-b)=0: replace it by (C-a*r)(C-b*r)=0 and use the same product-slot
elimination. In particular a=33 and b=33033 fit the general identity. This
does not establish the arithmetic adequacy of those two correction
choices, or verify an unseen packet's r expression and consumers. A
single-correction implementation requires its own numeric source and
target binding and the relevant squareclass proof.

Historical disposition: this is a new exact coordinate rewrite of the
existing correction/product interface. It does not repair or replace a
source arithmetic argument. The new and old rational projections are
equal independently of whether that common projection has already been
proved to be Z. The latter statement inherits the source's accepted
arithmetic dependencies.

Run `python -B review_scaled_correction_check.py` from this directory.
It writes `review-scaled-correction-checks.json` with the hashes and exact
results above. No source, candidate, earlier report or published file was
modified during this review.
