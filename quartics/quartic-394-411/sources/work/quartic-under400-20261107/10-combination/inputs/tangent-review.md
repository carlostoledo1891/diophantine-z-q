# Independent review of the complete tangent-compatible comparison charts

Reviewer: `astra_quartic_opt02_squares`, November 7, 2026.

Verdict: accepted as an internal, non-author review of the five-guard transformation in the pinned `05-anchor` proposal, relative to the inherited point-chart and arithmetic inputs of Version 12. I found no mathematical or implementation gap requiring correction. This review is not an independent proof of the inherited global arithmetic theorem and does not approve an unexamined later composition or publication.

The transformation may also be applied independently to only V1,V2,V3,V4. This is the appropriate subset when V0 is replaced by the separately reviewed fixed-target reciprocal chart. Acceptance of that subset does not authorize combining the V0 tangent equations with a circuit that has deleted their slope or ordinate coordinates.

## Source pins

The complete source list and hashes are recorded in `review-tangent-checks.json`.

| Source | SHA-256 |
| --- | --- |
| Published `quartics/quartic-498-514/candidate498-ir.json` | `7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a` |
| Published semantic mixed-depth precursor | `4466bd973383ba404b1cc50deaf2aa4f77361850c090dc8af80b7ba77249d57c` |
| `05-anchor/candidate493-ir.json` | `30dae02b01c79ee0f088d55ce45091a8014e376b24562de405fd60a913333a5f` |
| `05-anchor/polynomial493.json` | `e3ed059d08b100cf65cf37aeae240baec312f338d905dbd8fd88f977771453d3` |
| `05-anchor/REPORT.md` | `39bb00aa8428413254e2e6d5415c320a8908f32c940084c8a6095435ffb1b790` |
| `05-anchor/build_tangent.py` | `cdf01055cf76f066484558dfcae0999625464fd586b2929f9c381c13c1482e71` |
| `manuscripts/quartic_v12.tex` | `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9` |

I read the actual proposal and builder, the published half-trace argument at Version 12 lines 20016-20057, the point-domain lemma at line 10780 and the inherited square-abscissa chart argument, the retained inputs at lines 19837 onward, the mixed local argument at lines 19940-19985, and the soundness/completeness consumers at lines 20524 onward. I did not infer acceptance from an earlier PASS label.

## 1. Required inputs and actual constructed points

The field is K=Q(sqrt(2)), with basis 1,sqrt(2), and the curve is y^2=x^3-Dx with D=11-6sqrt(2). The incoming and target points are the actual source points

```
V0 = H-P,
Vi = Ui-Qi for i=1,2,3,4.
```

Their source charts describe finite nonidentity points in 2E(K). The inherited equality 2E(K)=ZP, with P of infinite order, and the point-domain lemma supply nonzero incoming ordinates. The fixed point P satisfies the same curve equation; the review checker verifies its literal rational components.

This nonzero-ordinate hypothesis is essential. Without it, the coincident-abscissa branch would not force a unique tangent slope. It is available from the existing charts and is not an added condition on the rational witness variables.

## 2. Literal equations and coefficient normalization

For each block, let Q1=(x1,y1), Q2=(x2,y2), d=x1-x2. The actual retained component equations give

```
md = y1+y2,
q = m^2,
xR = q-x1-x2,
yR = m(x1-xR)-y1.
```

The new field residual is

```
q(x1+x2-2xR) - 2m*yR - (x1^2+x1*x2+x2^2-D).
```

Both components are quadratic in the existing source coordinates. The checker reconstructs x1,y1,x2,y2,m,q,xR,yR from the pinned semantic precursor, transports them by exact coordinate names, and matches each slope, square and ordinate component to its literal retained residual up to a nonzero rational constant. This checks, in particular, the factor two in multiplication over Q(sqrt(2)) and the compiler's non-unit normalizations of imaginary components.

The checker also matches the literal equations for f(Vi)=1/xR in all five blocks and z(Vi)=-xR/yR in V1 through V4. V0's logarithm consumes yR directly instead of storing a separate z coordinate. Every such source row is unchanged by the candidate.

## 3. Chord identity and old-to-new completeness

After substituting q=m^2 and the ordinate expression, the added residual is

```
T = 2m*y1 - m^2*d - S,
S = x1^2+x1*x2+x2^2-D.
```

Put A=md-y1-y2 and Ei=yi^2-xi^3+Dxi. Direct expansion gives

```
d*T = E1-E2-A(2y2+A).
```

The review checker verifies this identity as a polynomial identity in six independent variables. In every published source solution, E1=E2=A=0 and the retained half-trace inverse makes d nonzero. Therefore T=0. Delete the five private inverse coordinates and retain every other witness. This gives a new solution for every old solution, including the particular witnesses for each integer input.

Completeness therefore needs no additional prime choice, continuity argument, tangent realization theorem or simultaneous avoidance condition. The old simultaneous witness tuple already works.

## 4. The d nonzero branch, including purely imaginary d

When d is nonzero, multiplication by d is invertible in K. The slope equation uniquely gives m=(y1+y2)/d. The retained xR,yR formulas are the usual coordinates of Q1-Q2.

Nothing in this argument requires the rational coefficient of d to be nonzero. In particular, d=b*sqrt(2) with nonzero rational b is a nonzero field element, with norm -2b^2 and inverse sqrt(2)/(2b). The proposed system correctly admits such a branch. It does not retain the stronger half-trace restriction implicitly.

The group difference is nonidentity: Q1=Q2 would force d=0. The secant formula is consequently an affine formula for a finite point in 2E(K).

## 5. The d zero branch

The retained slope equation gives y2=-y1 when d=0. Since y1 is nonzero, Q2=-Q1 and Q2 is not Q1. The added residual reduces exactly to

```
2m*y1 = 3x1^2-D.
```

Thus m is the unique tangent slope at Q1. The retained square and ordinate formulas give [2]Q1, which is exactly Q1-Q2. There is no arbitrary-slope solution and no extra off-curve point.

Because Q1 is a nonidentity point of the torsion-free group 2E(K)=ZP, [2]Q1 is nonidentity. It remains in 2E(K), so the inherited point-domain lemma supplies nonzero xR and yR. This is the actual reason all downstream inverse and logarithm equations retain their intended domains. Nonzero incoming y alone would not rule out every possible torsion issue on an arbitrary unrelated elliptic curve; the inherited 2E(K) statement closes that point here.

The branch Q1=Q2 is still excluded by the slope equation, which would read 0=2y1. Thus the new chart does not admit an identity difference.

## 6. Downstream objects and labels

The new chart always supplies the actual finite nonidentity difference. Therefore

```
V0=[h-1]P with h-1 nonzero,
Vi=[ui-ni]P with ui-ni nonzero.
```

The full logarithm ratios remain ui/h and (ui-ni)/(h-1). The existing mixed local proof only requires h and h-1 to be nonzero integers and at least one to be a p-adic unit, together with the actual point and logarithm domains. It never divides by h+1 or ui+ni.

In particular, H=-P is now a valid tangent branch giving V0=-2P and h-1=-2. Similarly Ui=-Qi gives Vi=-2Qi. These cases do not invalidate the integrality-first argument, the primary depth conclusion, or the label congruences. The one-place field tests still concern exactly the same f, z and logarithm functions of the actual difference points.

The order-40 Lucas and order-12 beta consumers and their height inequalities depend on those recovered labels, not on distinct incoming abscissas. The scalar reciprocal chart R=S-P and its separate anchor exclusion of S=-P are untouched. The input, root charts, scalar source, anchor and product-height scales are unchanged.

This explains why soundness extends to the larger chart domain. It would be incorrect to claim that every new solution can recover the deleted half-trace inverse, since a purely imaginary d has zero half-trace and the tangent branch has d=0. The proposal correctly claims preservation of the input projection through the arithmetic point interpretation instead.

## 7. Incidence and whole-system checks

`check_tangent_review.py` imports no proposal producer or proposal verifier. It uses separately implemented sparse rational arithmetic already present in this reviewer's folder.

The check establishes the following on the exact pinned files:

- Each deleted inverse coordinate has exactly one consumer, its own guard equation, and that equation is a nonzero rational multiple of 1-gamma*Re(d).
- The removed coordinate set is exactly {100,108,116,124,132}.
- The candidate retains every other coordinate unchanged.
- Every old row except the five inverse rows is unchanged after primitive integer normalization.
- Exactly the two reconstructed tangent components are added in each block, with no additional assumptions or hidden consumer changes.
- All candidate residuals are at most quadratic and every surviving coordinate occurs.
- An independent upper-triangular sum-of-squares expansion matches every term of the candidate polynomial.

The resulting system has 493 variables, 472 residuals, degree four, 25,219 coordinate monomials and content one. The checker passed. Evidence is saved in `review-tangent-checks.json`.

## 8. Four-block use in the current combination

Each proof and each coordinate deletion is local to its comparison block. Applying the transformation only to V1 through V4 is valid and saves four coordinates. It adds eight tangent residuals and deletes four inverse residuals, for a net increase of four residuals.

This is compatible in principle with a separate V0 reciprocal replacement, because none of the four selected blocks uses V0's private inverse, slope or ordinate coordinates. A composing checker must still reconstruct the actual semantic expressions in its current source and verify the retained equations and incidence, as the review checker does for the published source. The present review does not substitute for that final transport check, nor does it approve the separate rational-logarithm proposal.

## 9. Disposition

The arithmetic extension and its implementation are accepted for the pinned proposal, subject to the original manuscript's explicit arithmetic qualifications. No repair was needed. The pure-imaginary and tangent branches are intentional and valid, not exceptions to be discarded.

The historical half-trace argument remains correct for its published source. The tangent-compatible replacement is a different, larger chart domain and requires this new soundness argument. It is not incorporated in the pinned Version 12 manuscript. No repository file, published source, approval record, or earlier optimizer packet was edited by this review.
