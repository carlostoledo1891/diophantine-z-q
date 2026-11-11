# Independent acceptance of the 432 norm-root composition

Reviewer: agent01. Decision: accepted for the frozen research composition,
relative to the accepted 433 source and independently reviewed root449 component.
I authored neither the norm-root transformation nor this combination.

## Frozen scope

| Artifact | SHA-256 |
| --- | --- |
| `10-combination/combined433-ir.json` | `207218ebbcd15fa97f69580fce71629a50e34129549e80a9568dbed57ae28832` |
| `00-root/REVIEW433.md` | `1f67647179bc2ddb522af5b4f3454f2b7a476fd1115ba09946c3bc1689641ca1` |
| `06-product/scalar-redesign/root449/candidate449-ir.json` | `02ce0dcbeeba90a52bfba28c6968f09bcd3471c4b76847b57987f72cb6175549` |
| `05-anchor/review-scalar-root.md` | `ef0daf4038d42faafeb57ec8b735cb20b2a4df127d68dd978292eeb84e2eb5f9` |
| `10-combination/combined432-ir.json` | `92418e21d6903cf5a80def3848c3c3da603ec03673c207cf7c40a1a2dec105a2` |
| `10-combination/combined432-polynomial.json` | `e622e2fb7574f18319b84595d230509f843a5789e14ebaeb26722d1f7101ac19` |

The result has 432 total rational variables,431 witnesses,409 quadratic
residuals and 6496 quartic monomials. Its content is one, degree is four, and
largest coefficient is 16*3^(2^26), with fixed C=3^(2^25). This review does not
yet accept the subsequent depth 24 composition.

## Exact finite transport

My `check.py` imports no producer, compiler or other checker. It derives the
component delta directly from the pinned 450 and 449 files, verifies every
changed preimage on 433, and checks the full resulting coordinate and residual
tables against 432. Only coordinate 536 and its constant-node equation are
deleted; only the root equation changes. The deleted coordinate has no hidden
consumer. All row metadata and IDs are checked, and all surviving mathematical
rows agree up to a nonzero rational normalization.

The independent physical checks establish beta=2X²+2403, not the earlier
unshifted beta. Expanding the three retained contact intermediates gives
exactly r=beta(beta-1)(beta-2401)(32beta+343)(2beta-1). The five correction rows
are the same positive choices with generators 3,11,17,35,91. The q-square
expression is exactly Norm(f(H))², using the actual retained field components.
The denominator chain and ratio equations still give

```text
B=(z0²+r*z1²)/r^64,
W=B²+q²/r.
```

The root coordinate 542 has only its defining equation and W-square row as
consumers. Checking the actual corrected-r, W-square and pole-product equations
gives b=c*r*W². The pole slot has its old negative normalization b=-K*v526
with K>0; the retained equation 1+K*v526*v528=0 guards this same nonzero b.
There is no inference from the sign of the stored coordinate.

The source 433 has already established the current meanings of the scalar
ratio slots 508/509 and the common reciprocal after eliminating H.j. None of
their equations or consumers changes here. The full transport check also
preserves every beta-comparison, detector, height and anchor equation.

I independently expanded every primitive integer residual square and compared
the complete polynomial coefficient table. The only quadratic-C coefficient
is 16 at v57², with no lower-C contribution to that monomial. All other integer
coefficients have fewer than 2048 bits before multiplying by at most C. This
proves the displayed maximum without expanding C. An isolated coefficient-one
monomial proves content one. Exact support includes all 432 coordinates.

## Mathematical interfaces

I read the full root449 argument and agent05's review, rather than only its
acceptance. I also read the relevant pole, scalar-preparation, doubled-point
logarithm, and anchor passages in the released quartic_v12.tex, SHA-256
`5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`.
The principal locators are 7720-7748,10520-10560,20264-20361 and 20534-20635.

The new root proof applies to the actual objects preserved by 433. At each
consumed prime p>76176, the correction is a unit, and odd eta=v_p(r) is positive:
a negative valuation of beta would instead make eta=10*v_p(X) even. The two
root terms have opposite valuation parity. Together with the nonzero pole
obstruction this gives v_p(q)>eta/4 and v_p(B)>-eta/4. The ratio numerator then
gives both rational coefficient valuations at least 32. The nonzero q input
follows from the unchanged inverse relation for f(H), not from an unproved
positivity of a field norm.

The positive norm valuation selects a place where H is formal. The ratio
bound makes z(R) small, but R can be near O or near the nonzero two-torsion
point. The reviewed proof retains both cases and applies the logarithm to 2R
and the exact relation[h](2R)=[2s]H. Thus the original order 32 divisibility and
its height/anchor consumers remain available. No change to those consumers
is being justified merely by the old name W.

For completeness, r>0 and q²>0 imply the new W>0. The ordered preparation
permits the finite coefficient bounds used to make W integral at every prime
on the support of cr. Integrality, positivity and the nonzero square W² give
the exact pole-completeness hypotheses: square reduced denominator and the
same local squareclasses at 2,3,17. The lost claim that W is a unit is not used.
Continuity preserves those finite bounds before contact-prime selection, in
the same order of global choices as the source. Fresh pole witnesses are
required and supplied; old numerical pole witnesses are not asserted to survive.

These are the same interfaces agent05 accepted, now checked on the literal 433
objects. The source's later algebraic ratio, guard and H.j changes add no new
premise or missing case. This is an internal non-author composition review,
not a new independent proof of all inherited arithmetic theorems.

## Reproduction

Run `python -B check.py 432` in this directory. `CHECKS432.json` binds all read
inputs and records the finite result. No shared or released file is modified.
The user requested release only below 400 total variables; this acceptance is
for research integration and is not a publication recommendation.
