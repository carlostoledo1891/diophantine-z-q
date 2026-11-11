# Independent review of the 439-variable composition

Reviewer: `/root`, parent agent. Decision: accepted for the frozen research candidate. This is a composition review of the accepted scalar443 system with the separately reviewed four odd norm charts. It does not re-audit the manuscript's inherited group or analytic inputs.

## Bound artifacts

The new candidate is `../10-combination/combined439-ir.json`, SHA256 `403c4126d532fd3403ce0d87a258790d6b78c1a46cf09716aab0df3a7e84c4df`. Its full polynomial is `../10-combination/combined439-polynomial.json`, SHA256 `f81c2eaa953a508559a846fd82f4954ffc95de3df9966550dd7d6f5a73e6f171`.

The source443 SHA256 is `9002b711f5083d6cb70d1fa3ebff0f17d5be7d2e0ad85c0384f63e7814ed37b1`. Its independent review is `REVIEW443.md`. The odd-chart component is the 453-to-449 change, candidate SHA256 `f5a9471dd06bfdfe382b10481fdcf0c7ddfd7184386f1e667a00efdae4ea115e`, independently reviewed in `../03-depth/review-odd-norm.md`. I read that review and the author's full chart argument before checking this transport.

The new independent checker is `review_odd_transport.py`. Its complete record is `odd-transport439-receipt.json`. It reads the five pinned artifacts without executing any producer or earlier checker.

## Why the changes compose

The odd-chart replacement changes only private witnesses in the four A, S, T, and Z root blocks. It fixes each block's actual h, j, and x coordinates. Its forward map is polynomial. Its reverse map uses the inherited same-model squareclass decomposition, constructs a half-point, and switches the private half-point by T0 when needed to obtain squareclass epsilon. That switch changes neither h nor j nor x. It is equality of projections onto the outside coordinates, not a claim that all private witness sets are bijective.

The intervening primary and scalar ratio changes preserve those root charts and consume only their retained coordinates. In particular none consumes the old private t or r witnesses. Consequently the same four odd-chart witness maps act on every source443 solution and fix every coordinate used by its newer ratio equations. Conversely each source443 witness has a lift into the new four private blocks by the already reviewed component argument. This proves equality of the input projections without adding a compatibility or simultaneous-choice premise.

The checker establishes this disjointness against actual rows. It derives the full component difference from the pinned453 and449 artifacts. Every changed source object has exactly its old453 value in source443. All sixteen retained root-chart rows remain identical. The complete incidence of the sixteen old private witness coordinates is exactly the sixteen replaced odd rows, in both the original453 and actual443 systems. Thus the two newer ratio replacements have introduced no hidden consumer.

Applying that exact difference to source443 reproduces candidate439. The composition assigns fresh IDs687 through698 to the twelve replacement rows; their names, terms, and all other metadata match the reviewed component. Every outside row retains its original ID and full object. This administrative renumbering is recorded explicitly rather than treated as a changed equation. Every retained coordinate object matches the transported component exactly; no additional coordinate is introduced or reinterpreted.

## Complete polynomial check

The checker independently clears denominators, removes each residual's integer content, and computes the entire sum of squares with a triangular multiplication loop. Every coefficient agrees with the supplied table. It verifies:

- 439 total variables, including the input, and 438 existential witnesses;
- 416 quadratic residuals and a degree-four polynomial;
- 6,568 nonzero monomials;
- content one after specializing the fixed integer C;
- largest coefficient magnitude exactly 16*C² = 16*3^(2^26).

The last two facts use a literal coefficient one at x1^4 and a unique 16*C² coefficient at x57², with no lower-C terms at that monomial. All constant coefficients have bit length below2048, and every coefficient linear in C has multiplier at most48. C remains the fixed integer 3^(2^25), not an extra quantified variable.

All checks passed. This acceptance covers the frozen composition and the cited component reviews. It does not apply to later modifications or justify a manuscript release before the total variable count is strictly below400.
