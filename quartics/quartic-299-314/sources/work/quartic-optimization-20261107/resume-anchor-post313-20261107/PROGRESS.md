# Post313 anchor and parameter reuse search

Author: `/root/astra_quartic_opt05_anchor`, November 7, 2026. No additional reduction is claimed. The source is accepted anchor-gamma313, IR SHA256 `6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a`. Direct elimination and power-chain work is assigned to agent01; this note concerns further arithmetic selection of private witnesses.

## Fixed affine slices of the remaining anchor witness

The retained anchor is

    u^2+6v^2-2z^2=3T^2-2C^2,  C=3^(2^25), z=w+C.

The accepted313 construction uses its two-dimensional freedom to choose u with prescribed local valuations and a real interval, while retaining v,z as rational witnesses. Trying to save v by imposing v=aT+bC changes the condition to

    (u/C)^2-2(z/C)^2 = 3t^2-2-6(at+b)^2,  t=T/C.

The right side must now be a norm from Q(sqrt(2)). At an odd prime p where2 is a nonsquare, every nonzero rational value x^2-2y^2 has even p-adic valuation. To prove this, divide x,y by the smaller power of p in their valuations. At least one resulting coordinate is a unit, and the difference cannot vanish modulo p because2 is a nonsquare. Its valuation is zero before restoring the even power. Thus an odd valuation of the displayed target is a decisive obstruction to that slice.

`check_slices.py` tests all49 pairs a,b in {-2,-1,-1/2,0,1/2,1,2}. For every pair it finds a prime p<=257 with2 a nonsquare and a positive integer t for which the target has valuation exactly1. Every t is33 modulo72, hence1 modulo8 and6 modulo9. In particular each t meets the old quaternion integrality criterion and even the stronger residue conditions available in the313 preparation. All arithmetic in the test uses rational fractions and exact integer divisibility.

Examples are:

| Slice | t | p | Required norm |
| --- | ---: | ---: | ---: |
| v=0 |33|5|3265|
| v=T/2 |249|11|185999/2|
| v=T |249|5|-186005|

These are counterexamples to replacing the standalone quaternion criterion by these fixed slices. They are not full313 circuit witnesses: no assertion is made that the tested t occurs from the actual simultaneously chosen scalar and root data. Therefore this result blocks the argument that the old criterion alone guarantees a slice, but does not prove an unrestricted impossibility or rule out a new argument controlling the actual data. A valid saving would need such an additional construction.

## Shared pole witnesses need their exceptional branches

The actual first normalized detector conic is

    3e^2-34e-289+17B p^2=0.

If two detectors share e and both p values are nonzero, then their B ratio must be a rational square. The current construction does not impose that condition. However p=0 cannot be ignored: the first conic admits e=17 or e=-17/3 in that branch. Hence the ratio observation alone is not a proof that sharing e fails. The remaining normalized pole equations must still be analyzed on both special e fibers before such a proposal can be counted or rejected. No reduction from this route has been claimed.

## Root-chart boundary

The accepted root charts and their complete consumers are unchanged by313. The earlier `resume-elimination-20261107/root-charts315/REPORT.md` already checks the six-coordinate x=h^2, j^2=x^2-D modules, the exact x+j/x-j alternative, the cubic and zero-branch problems in the five-coordinate norm proposal, and the bounded direct-elimination calculation. Repeating those calculations would not be a new reduction. The current task leaves their direct algebraic extension to agent01.

The49 slice obstructions are reproducible with `python -B work/quartic-optimization-20261107/resume-anchor-post313-20261107/check_slices.py`; `SLICE-CHECKS.json` records every exact local witness. Accepted313 and all earlier artifacts are untouched.

## Reusing a pole ordinate as the common parameter

An existing normalized pole ordinate p already has a squared slot. If gamma could be chosen as that p, the gamma square gate could reuse the slot, nominally saving one coordinate beyond313. This is only a conditional circuit count.

For a detector pole this creates a selection cycle: its input B depends on W, W depends on gamma, and gamma would be the pole witness selected for B. The first conic alone then imposes the additional square condition on its discriminant4624-204*B*gamma^2. The old pole-existence theorem does not assert this condition for a preselected gamma. A local or real approximation argument alone cannot replace exact rational solvability.

For the scalar pole, B depends on the final H but not directly on gamma. This avoids that algebraic cycle, but still requires prescribing a pole ordinate's local valuations and real size after fixing B. The actual source proof of the preparation-zero lemma, Version13 lines10563 through10636, obtains the witnesses from the simultaneous elliptic realization lemma near lines7787 onward. That lemma supplies nonzero abscissae in a squareclass on two twists, not arbitrary approximation of a chosen ordinate. No proof of the stronger selection statement is available in this packet. It must not be inferred from the elementary quadric argument used for313: the two pole conics share variables and are not the same rational quadric.

This route is left as an explicit unproved selection problem, with no candidate or variable saving claimed.
