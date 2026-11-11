# Frozen Version13 candidate with 394 variables

The selected research candidate has 394 total variables, 393 witnesses, 364 quadratic residuals and 6,338 quartic monomials. Its degree is four, integer content is one and largest coefficient is exactly 16*3^(2^26). Its ordinary integer-coefficient companion has 411 total variables, 410 witnesses, 381 residuals and 6,388 quartic monomials. Final mathematical and release-artifact reviews remain separate acceptance records.

| Artifact | SHA-256 |
|---|---|
| Accepted predecessor combined395-ir.json | 440282e5b3b8a9a19d5d7009399736257a5279105485a1bec073138a64758e6a |
| Final combined394-ir.json | 7eb02f9913b55d60a790a287616f1bb80d9f93523e9f11e12481c9ab955746a5 |
| Final combined394-polynomial.json | 39e1f5c05a1a26be26b006703bccc2e1c23b8a15876fbd6d43749d5d464d3193 |

The predecessor was independently accepted by agent03 in integrated395/REVIEW.md, SHA c8db82b3b77886a7a289e7eb81ecefc39c8a6fc05928cd3176e4bc2d81a216bf. Its full interfaces are recorded in the unchanged REPORT395.md, REPORT399.md and REPORT396.md. The final change is the independently reviewed anchor rescaling in inputs/anchor-rescale398-ir.json, with review inputs/anchor-rescale-review.md, SHA 0e7082164559fa84f38435b188ea3eaa673e7c2ccca5666a21adedcccdf9f1be.

## Final anchor change and order of proof

Let g=g0+g1*sqrt(2) be the unchanged scalar reciprocal coordinate and F=2g0g1 the old coefficient of f(S-P). The old equations F*sigma=1 and

```
u^2+6v^2-2w^2-3F^2-4Cw=0
```

are replaced by g0*tau=1 and

```
U^2+6V^2-2W^2-12g1^2-4C*tau*W=0.
```

Delete F and its definition. Forward, tau=1/g0 and (U,V,W)=(u,v,w)/g0. For the reverse direction, first use the unchanged S odd-root chart, the unchanged scalar reciprocal equation and g0!=0 to identify R=S-P as a nonzero even multiple of P. This uses no H-domain argument, anchor size or inverse of F. The inherited coefficient lemma then gives F!=0. Restore sigma=1/F and (u,v,w)=g0*(U,V,W). The exact polynomial scaling identity restores the old anchor.

Only after this restoration is the independently accepted395 proof invoked, including its pre-ratio H exclusions and scalar index bounds. This order prevents a circular use of the anchor. The S=-P branch is allowed in the restoration and gives R=-2P; the coefficient lemma covers every nonzero even index. The equivalence is a full-source statement, not an equivalence for arbitrary isolated rational g.

verify394_interfaces.py checks the changed anchor, replaced inverse guard, deleted coefficient definition and every private-coordinate incidence and the preserved physical S/scalar-domain equations. verify_anchor_combination.py 394 replays the pinned component and every quartic coefficient. The unique C-squared coefficient is now on W^2*tau^2. It is 16C^2, with no other contribution to that monomial. All C-linear multipliers have magnitude at most96 and all remaining coefficients have fewer than2048 bits.

## Compact and ordinary artifacts

The release394 directory holds an exact byte copy of the frozen394 source, its polynomial, physical coordinate maps, compact residual systems and complete JSON/text coefficient tables. Compact coordinate indices are 1 through the total count, and x1 is the input. ARTIFACTS.json binds every file and records all counts. These are prepared files, not a publication action.

The ordinary companion adds c0=3^1024 and cj=c(j-1)^2 for j=1,...,15, so c15=C. Because the final anchor contains C*tau*W, it also adds t=C*tau and replaces that term by t*W. This seventeenth coordinate is required to keep all residuals quadratic. The ordinary count is therefore411, not410. No enormous expansion of C is used.

prepare_release394.py constructs the artifacts. The independent verify_release394.py checks all seventeen added equations, the exact original-row substitutions, the full two polynomials, coordinate coverage, both compact remaps and every text-table row. The ordinary maximum coefficient has3247 bits; its exact expression 3^2048+delta and full decimal coefficients are recorded in ARTIFACTS.json and the ordinary tables.

No later optimization is included. All earlier frozen candidates, including395 and the397 alternative, remain unchanged. The manuscript and repository release remain the parent task's responsibility after final review.
