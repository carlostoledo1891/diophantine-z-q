# Independent acceptance of exact319

I accept the exact320-to319 private-anchor transformation as an algebraic equivalence of its guarded rational solution sets. It preserves the input and every nonprivate coordinate. No new arithmetic application is needed, and none is inferred from the separate358 proposal.

Reviewer `/root/sol_protocol_final_review`, November 7, 2026. Author `/root/astra_quartic_opt01_elimination`. I did not author or repair this transformation. Exact serving-model metadata is not independently attested.

## Exact files

| Artifact | SHA-256 |
| --- | --- |
| Candidate report | `2cd2a61828a8d3dd34a73ff00079d192bb2619856fdcfba34373a95302bbc2a8` |
| Source320 IR | `d1171bc47ed8ec15aac10ca6708208e9de9c2dfa7a973732ede76269a1bee02f` |
| Candidate319 IR | `847d21a2d0a45571f043b82289df0da55f4e814167844bdc39fc134e4f4c2676` |
| Candidate polynomial | `8320b69d290a37017060e34742fb025cbc1c13e40a5b7d750893e9912d3796ef` |

The source is the exact320 system accepted in my prior report with SHA-256 `7bc8fa06ef2483dccc1e26d5c83b6a94c510e27e3718bf0c52effa7693840c15`. This review concerns only the present transformation, keeping that prior review unchanged.

## Boundary and guarded maps

The source coordinates55,56,57,903,904 occur only in rows504,903,904. I checked all terms of all source rows. In the new system, coordinates55,56,57,903 occur only in rows504,903. Every other row and all nonprivate coordinate objects are identical. The four retained private coordinates change only their names;904 and its row disappear. The original g0*tau=1 row remains literally unchanged, so g0 and tau are nonzero everywhere on both solution sets.

Write q=48v83²+48v87²+432v89². The source equations are Q=q, B=2g1+C*Q*tau and the source anchor. The new equations are T=2g0g1+Cq and the unscaled anchor. My checker matches all of these to the actual rational monomials.

The forward map sets u=g0U, v=g0V, w=g0W and T=g0B, retains every nonprivate coordinate and drops Q. The inverse sets Q=q, B=tau*T, U=tau*u, V=tau*v and W=tau*w. Both maps are polynomial using the already retained tau. They impose no new denominator, square-root, sign or zero restriction.

I verified the five unconditional identities exactly as sparse polynomials, treating C as a formal fixed coefficient. With G=g0*tau-1 and source residuals RQ,RB,RA, the forward pullbacks are

```text
NT = g0*RB + C*RQ + C*Q*G
NA = g0²*RA + 4C*g0*W*G.
```

The inverse pullbacks are

```text
RQ = 0
RB = tau*NT + 2g1*G
RA = tau²*NA.
```

These identities prove preservation of every changed row. Every unchanged residual is fixed by both substitutions because it has no private-coordinate consumer. The compositions are identity on the solution sets, using G=0 and Q=q. Thus this is a full guarded solution-set equivalence, not merely equality of possible input values.

The source320 root-parity restoration, detector semantics, Π^39 completeness choice and private quaternion argument can be used through these exact maps. No new choice of rational witnesses or Hasse–Minkowski application is introduced by319 itself. The new T has the same value g0B as in the source; it is not replaced by a different numerator involving g1².

## Full polynomial and coefficient specialization

The independent checker imports neither producer nor author verifier. It checks all source/candidate differences, complete consumers, the five identities, active coordinates and the primitive normalization of all289 residuals. It independently expands the full sum of squares and matches every coefficient-power entry.

The result has319 total variables,318 witnesses,289 quadratic residuals and degree four. There are5662 symbolic coefficient-power entries and5659 ordinary monomials after fixing C. The only collisions are the pure fourth powers of83,87,89. Their coefficients are respectively

```text
2304*C² + 64
2304*C² + 64
186624*C² + 64.
```

All other absolute C² coefficients are strictly below186624. C-linear coefficients have magnitude at most1728 and C-independent coefficients have at most1520 bits. Since C=3^(2^25)>2^2048, these lower terms cannot overcome even a unit gap in the leading C² coefficient. The maximum absolute specialized coefficient is therefore exactly186624*C²+64. A monomial with constant coefficient1 remains, so content one survives specialization. This review counts the actual specialized monomials rather than confusing them with coefficient-power entries.

CHECKS.json records these results. The author verifier also passed with its sole output redirected into this directory. AUTHOR-UNMODIFIED.json confirms that every author file retained its bytes. Prior reviews and released files were not changed.

## Decision and scope

No unresolved algebraic or implementation defect was found. This exact319 transformation is accepted on accepted320. It introduces no arithmetic hypothesis and does not strengthen the inherited full-manuscript or publication status. The separate326 and prospective326/359 composition remain distinct artifacts requiring their own integration review. The strict below300 publication threshold remains unmet.

Reproduce the independent finite audit from the workspace root with `python -B work/quartic-optimization-20261107/resume-sol-review319-20261107/check.py` using a recorded compatible interpreter.
