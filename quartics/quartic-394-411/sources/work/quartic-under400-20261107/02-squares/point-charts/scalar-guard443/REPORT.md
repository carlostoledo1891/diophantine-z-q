# One smaller scalar nonzero guard

The isolated change takes the frozen 443-variable source to 442 variables, 441 witnesses, 419 quadratic residuals and 6,611 quartic monomials. It deletes the unused real coefficient of the scalar value f and moves its inverse guard onto the retained irrational coefficient. The degree remains four and the content is one. This packet awaits independent review; the source's own pending review remains a separate dependency.

## Frozen files

- Source: `10-combination/scalar443-ir.json`, SHA256 `9002b711f5083d6cb70d1fa3ebff0f17d5be7d2e0ad85c0384f63e7814ed37b1`.
- Result: `candidate442-ir.json`, SHA256 `7c8bcbb20289e92e790a0728a96428b451516842420454355731e64a950d7c3b`.
- Polynomial: `polynomial442.json`, SHA256 `8fdc5a0d7fcf0ed90a0028d9585dba23f02fbc59a1de52a257da5952502a4f90`.
- Arithmetic source: repository `manuscripts/quartic_v12.tex`, SHA256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`. The necessary nonvanishing is Lemma `lem:v12-anchor-coefficient`, lines 20115–20129, proved immediately thereafter. The reciprocal-chart group interpretation and exceptional cases appear at lines 20385–20445.

The other new odd-root replacement is not included in this source or this isolated saving. This guard change is disjoint from its private coordinates.

## Exact equations and consumers

The source contains, in rational coordinates,

    f0 = g0² + 2 g1²,
    f1 = 2 g0 g1,
    f0 * sigma = 1.

Their coordinate IDs are f0=504, f1=505, g0=543, g1=544, sigma=549. The full source has exactly two consumers of coordinate 504: its first displayed definition and the inverse equation. Coordinate 549 occurs only in that inverse equation. Coordinate 505 is also consumed by the physical anchor and remains unchanged.

Delete coordinate 504 and its definition. Replace only the inverse equation by

    f1 * tau = 1,

reusing coordinate 549 for tau. Every other residual, coordinate and fixed parameter remains exactly the source object. In particular no scalar ratio, norm, point, height, anchor or detector value changes. The source already removed z_S by an equivalence preserving all retained values; its recovery z_S=-rho/s remains available.

## Completeness from the source

The source's accepted inherited point and reciprocal-chart arguments identify the scalar difference as R=[s]P for a nonzero even integer s. Specifically the scalar input is an odd point S, its difference is R=S-P, and the source's f0 inverse excludes g=0 and hence S=P. The rational difference formula and its x=c exceptional case are precisely those checked in the cited reciprocal-chart proof. The permitted S=-P case, if considered before the anchor, still gives the nonzero even index s=-2. There is no dependence here on the proposed replacement guard.

For every such nonzero even s, the cited anchor-coefficient lemma proves

    v3(f1([s]P)) = 2 + 2 v3(s),

so f1 is nonzero. Set tau=1/f1, forget f0 and the old sigma, and retain all other coordinates. All new equations hold. This argument uses the full source's integer-orbit semantics: it would not assert that every arbitrary rational g with g0²+2g1² nonzero has 2g0g1 nonzero.

## Soundness and all zero branches

From any rational solution of the new system the new guard gives f1 nonzero. The unchanged definition f1=2g0g1 makes both g0 and g1 nonzero. Define f0=g0²+2g1². Rational squares show f0>0; in particular its inverse exists. Restore sigma=1/f0. This recovers the old f0 definition and inverse equation. All other old equations are unchanged and therefore hold. No group theorem is needed for this direction.

Thus no solution with g=0, g0=0, g1=0, f1=0 or f0=0 survives the new guard. Conversely none of these branches occurs in a full source solution, by the source guard together with the exact nonvanishing lemma. Every denominator used in either map is proved nonzero before division. This is an equivalence of full rational solution sets projected onto all coordinates except the removed f0 and the repurposed inverse. The input is fixed. The two inverse values are uniquely determined by the remaining g coordinates.

## Executable certificate

Run `python -B build_guard.py` and `python -B verify_guard.py`. The verifier imports no producer, matches all four displayed literal equations, checks the complete incidence of both private coordinates, compares every outside row and metadata object, verifies coordinate coverage and quadratic degree, and independently expands the entire primitive sum of squares. Its result is `verification442.json`; all checks passed. The arithmetic nonvanishing dependency is stated above rather than being disguised as a polynomial identity.
