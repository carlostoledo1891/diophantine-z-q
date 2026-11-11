# Combined 453-variable research candidate

The frozen candidate `rational453-ir.json` has SHA256 `f90ee69b7f26d43e94f6a7bb255d3cf2e040d5a2746d79c3b13e08a35185998f`. It has 453 total variables, 452 witnesses, 430 quadratic residuals and 6,584 quartic monomials. Its content is one and its maximum coefficient is exactly 16*3^(2^26), with fixed C=3^(2^25). The polynomial SHA256 is `b297f9ee23af09293433620cdcd77959e464c1e5125754d610f97eacd50ea422`.

All component transformations have received non-author mathematical review. Exact final transport, physical-consumer checks and full coefficient expansion pass. A fresh non-author review of the complete final composition is requested. The publication threshold is strictly below 400 total variables, so this is not a release candidate and Version12 remains unchanged.

## Frozen lineage

The published498 source is pinned in `inputs/released498.json`. Its reviewed order-10, factored-pole, scalar-k, scalar-conic and forward-power changes give `combined486-ir.json`. The exact certificate records those source deltas, and `reviews/bl5/REVIEW.md` independently accepts their composition.

The reordered triple detector circuit gives479, followed by nine constant-pivot eliminations giving470. `inputs/accepted470-ir.json` is an exact copy of agent01's final candidate with SHA256 `eff9369864da6bd2ed46fa300f51f5a0cc9217d3b790380713644ee31f512b72`. `reviews/triple/REVIEW.md` independently accepts the complete circuit equivalence and all eliminations. The unchanged source486 remains the arithmetic dependency.

From470, two reviewed point-chart changes give `combined461-ir.json`, SHA256 `73d16931a8e6fb9c50927b2d059899eb77157ef76ab6d9e38fb6536a5601c99a`:

- Replace V0's seven private slope-chart coordinates by two reciprocal coordinates, saving five. `V0_REPORT.md` gives the formulas. `inputs/v0-review.md` is the non-author acceptance, including all four equal-abscissa sign cases.
- Remove only the four V1 through V4 half-trace guards and add their tangent-compatible equations. `inputs/tangent-review.md` independently accepts this arithmetic extension. `verify_tangent_subset.py` checks that the integration input is exactly this four-block restriction of the reviewed five-block proposal.

`combine_extensions.py` checks source equations, coordinate semantics, deleted-coordinate consumers and ID collisions before applying these changes. `verify_combination.py 461` independently reconstructs both deltas and the entire polynomial.

Finally `build_rational.py combined461-ir.json` replaces four G9 evaluations by the reviewed N8/Q2 rational approximation, saving eight. `inputs/rational-review.md` independently accepts its arithmetic argument and the same implementation on the published498 source. `verify_rational_component.py 453` independently derives N from QG9, checks positivity and coefficient denominators, reconstructs the exact four circuits and every outside consumer substitution, and expands the entire final polynomial.

## Composition obligations

The V0 reciprocal proof excludes g=0 using the actual retained equation ell0*LP1=z(V1)*G2(w1). Its contradiction needs a genuine nonidentity doubled point V1 and the nonzero G2 value, not the historical half-trace guard itself. The tangent review proves precisely that V1 still is the actual nonidentity difference, including the opposite-point doubling case and nonzero abscissa differences with zero rational component. Consequently the V0 proof survives the V1 guard deletion. The polynomial G2 at V1 and this ratio equation are unchanged.

The reciprocal V0 output is z=-g/k, with dg=N, T=adk and k nonzero. Replacing G0 by R0 therefore requires the literal equation T*ell0+a*N*R0=0. `verify453_interfaces.py` checks both components in the final IR. It also checks that the actual surviving LP2,LP3,LP4 rows are ell0*LP_i-z(Vi)*Ri=0. No stale semantic entry for an eliminated standalone ell_i is used. All these R outputs are the actual quotient N8/Q2.

Every V_i remains a nonidentity doubled point. Thus 0<w_i<1 under both real embeddings. The rational-log review proves N8 and Q2 strictly positive on this interval, so R_i is defined and nonzero. The same review proves the relative precision40 at every relevant split or inert place, and addresses the remaining finite places through nonzero evaluations and continuity. Its completeness argument rebuilds the comparison and pole witnesses with the new functions. It does not claim that old comparison values are retained.

The old order-10 tests remain valid with the unchanged G2 numerator of precision12 and the new denominator of precision40. The factored pole completeness argument still receives positive inputs from the same rebuilt witness construction. No new arithmetic assumption is added by combining these arguments.

The470 triple eliminations depend on six retained logarithm-square rows. The rational implementation deliberately retains their original scaled w-squared coordinates and equations. `verify453_interfaces.py` compares rows132,133,144,145,150,151 with the exact470 source and verifies they are unchanged. Only old cube slots are reused as literal fourth powers; the middle pairs are deleted; the polynomial slots are recentered to the literal R outputs. Every outside consumer of the latter is transformed by the fixed nonzero affine coefficient map.

## Verification and limits

Run `verify_tangent_subset.py`, `verify_combination.py 461`, and `verify453_interfaces.py`. The last command includes `verify_rational_component.py 453`. Each imports no producer. They check all final coefficients, quadratic residual degree, quartic degree, coordinate support and exact source hashes. They handle the enormous fixed C symbolically and verify its unique squared anchor contribution separately.

`STATUS.json` records the current reviewed baseline, candidate lineage, exact hashes and remaining review interface. All older files remain frozen. This candidate improves the research bound to453 subject to the requested final composition audit; it does not reach the user's next publication milestone.
