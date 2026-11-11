# Shared-scale candidate with 314 variables

This is a frozen research proposal jointly developed by agents01 and03. It has 314 total rational variables, including the input, 283 quadratic residuals, and 6135 monomials in their primitive integral sum of squares. The degree is four and the coefficient content is one. The largest absolute coefficient is exactly `186624*C^2+64`, with the unchanged fixed integer `C=3^(2^25)`. No decimal expansion of C is required.

The candidate is not independently accepted. This report establishes the literal circuit and its relationship to the proposed arithmetic proof. It does not turn a finite checker pass into approval of the new arithmetic argument. Neither author can provide that independent approval.

## Frozen inputs and outputs

The input is accepted315 at `work/quartic-under300-20261107/10-combination/combined315/candidate315-ir.json`, SHA256 `d450a34735fe84bab0900abb3931740d4f7cedb1004ede7a81e1a09c4249f8b8`. Its independent composition review is `work/quartic-optimization-20261107/resume-sol-review315-20261107/REVIEW.md`.

The new arithmetic proof is `work/quartic-optimization-20261107/resume-depth-20261107/shared314/PROOF.md`, SHA256 `a8b3adc8ed7103aea1fc65cff5654632534fe151ec5ba157ad4413f79cceb4eb`. Its local-class checker is `check_classes.py`, SHA256 `da269e74f621b5e061cbca17e701509fb95e7b77c8fb748eaaa40b68d7d0ee79`. This is the exact proof interface implemented here.

The emitted `candidate314-ir.json` has SHA256 `7805ee1ebd5fec7ac20b2b5590afe9b5891c85aff8eee5f58b104a888bb9e6f5`. The emitted `polynomial314.json` has SHA256 `82f10a736855acba8c12a09406a5c954ddefa22825dbffa2d773005a6b6b05e8`. The latter has 6138 entries when powers of C are separated, representing 6135 distinct variable monomials. `MANIFEST.json` pins the remaining packet files and source evidence.

## Exact circuit changes

Write gamma for the new common parameter, distinct from C. New coordinates1100 through1108 mean, in order,

```
gamma, gamma^2, gamma^4, gamma^8, gamma^16,
gamma^-16, gamma^40, gamma^80, gamma^160.
```

Four squares define the first powers. The equations `gamma16*J=1` and `gamma40*J=gamma16*gamma8` define the inverse and gamma40, and two squares define gamma80 and gamma160. Every rational solution therefore has gamma nonzero, and every nonzero rational gamma gives a unique tuple of these nine gates. The new proposal does not use an implicit exclusion of gamma zero.

The source has `P1=f(U1)^2=(x255,2*x256)`. Coordinates1109 and1110 define its square by

```
x1109 = x255^2 + 8*x256^2
x1110 = 4*x255*x256.
```

These are the two ordinary coefficients of `P1^2` in the basis `1,sqrt(2)`.

Nine existing private output pairs are rescaled. H1,H2,H3,H4 and P2 pairs are divided by gamma160; M0,M1 pairs are divided by gamma40; P3,P4 pairs are divided by gamma80. The exact coordinate map is recorded in `CERTIFICATE.json`. Each source defining equation `Z-oldSquare=0` becomes `gammaPower*Z-newSquare=0`. All input values to these squares remain unchanged. Forward and reverse maps on each such private pair are respectively division and multiplication by the indicated nonzero power. The verifier proves these pairs have no consumers outside their own source definitions and the changed detector group rows.

For each detector retain E and repurpose its former E8-seed and E19 coordinates as R2 and R3. The old equation `E*R=1` remains literal and unchanged. The four new local equations are

```
R2=R^2, R3=R*R2, E4*R3=E, E8=E4^2.
```

Since the unchanged equation forces R nonzero, these imply exactly R2=R^2, R3=R^3, E4=E^4 and E8=E^8. The physical R expressions remain affine combinations of the actual source coordinates; `verify.py` independently states and checks all three. In particular, R is not silently identified with a raw, unnormalized scale coordinate.

Using the proof's notation, the new groups are exactly

```
G0=1+R*ZH1+R2*ZH2+E*U+E4*Z1+gamma16*E8
G1=1+R*ZH3+R2*ZH4+R3*ZP2+E4*ZP4+E*ZP1+E8*T0
G2=1+R*ZM0+R2*ZM1+R3*ZP3+E8*T2+E4*T3+E*T4.
```

The physical T and Z1 expressions retain the original field conjugation and source scaling constants. The verifier checks the maps against the original group rows before checking the new rows. W is still the product G0*G1*G2 through the original multiplication gates. All W, norm, trace, pole, point, root, scalar and anchor equations remain literal source rows. Their values are subject to the new groups; no claim is made that W retains its old value.

The circuit deletes twelve source coordinates and adds eleven. It removes24 old power rows, changes18 private square-definition rows and18 group rows, and adds22 quadratic rows. The other225 source rows are byte-equivalent JSON objects. Thus the totals are `315-12+11=314` and `285-24+22=283`. The anchor equation is source row1903, not the unrelated detector row903, and remains unchanged.

## Projection argument and its limits

This is not a bijection of every old and new witness fiber. The detector product has changed. Exact rational gate maps above do not suffice to prove integer projection; the new arithmetic proof is necessary.

For soundness, the proof first applies the unchanged trace and pole interface at one common place. The new guard yields `v(gamma)>15*v(R)/32`. Its residue class is separate from every other term before any point or logarithm interpretation. The resulting comparisons have the old orders40 and10, and all required points are formal. The old signed pre-H exclusions still use exactly E8*T0. The new step recovers H-depth from integral primary ratios and `F(L2,L3,L4)=0` modulo the place: since `F(0,0,0)=-1`, one ratio is a unit, forcing H to have the depth of a deep primary point. The old approximation, height and Lucas arguments then receive their original hypotheses.

For completeness, the proof preserves the original Pi19 progression, chooses the new gamma with valuation1 at selected contact primes, and uses simultaneous finite and real approximation for gamma/lambda. It checks all changed group margins and the small-prime and real pole bounds. The order of these choices, the pre-H exclusions, and the new H-depth recovery are material independent-review obligations. The compiler does not assert them as consequences of its finite tests.

No new number-theoretic premise is proposed. The new work consists of these applications of the existing arithmetic sources and the displayed circuit. A reviewer must assess both; all frozen sources and outputs remain available for that purpose.

## Reproducible checks

Run `python build.py` to reproduce the artifacts and `python verify.py` to check them without importing the producer. The latter checks source/output hashes, all changed equations, source leaf normalizations, private-output incidence, unchanged consumers, exact local powers, nonzero common-power equations, degree, counts, and every coefficient of the full sum of squares. `CHECKS.json` records its result. The maximum-coefficient comparison uses an exact bound `C>2^1522`, not floating-point evaluation.

The arithmetic author separately checks all relevant residue classes. These finite checks do not replace the unbounded arguments in the proof or a non-author review. No released repository, manuscript, accepted315 file, or earlier frozen artifact was modified.
