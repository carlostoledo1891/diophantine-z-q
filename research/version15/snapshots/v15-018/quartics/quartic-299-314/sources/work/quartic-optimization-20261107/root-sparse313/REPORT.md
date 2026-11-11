# Positive weights for the 313-variable construction

This is an exact compiler change to the reviewed 313-variable residual system. It reduces its expanded monomial count from 6,073 to 5,982. The same change reduces the reviewed 328-variable ordinary companion from 6,115 to 6,024 monomials. It does not reduce the number of variables and does not meet the next publication threshold of fewer than 300 variables.

The author is the root agent. Independent acceptance is pending. These files are research artifacts, not a manuscript update or a new verification of the inherited arithmetic theorem.

## Construction and proof

For each source residual, clear its rational coefficient denominators by their positive least common multiple and divide by the positive greatest common divisor of the resulting integer coefficients. Denote the resulting primitive integer polynomial by r_i. The source compiler forms the sum of r_i squared.

The new polynomial is

    P_w = sum_i w_i * r_i^2.

The 42 changed weights are specified exactly in `integer-weights/WEIGHTS.json`. Every omitted weight is 1. Every weight is a strictly positive integer. There are still 283 source residuals; the number 283 describes the residual system, not an assertion that the new polynomial is a sum of exactly 283 unweighted squares.

For every rational assignment, P_w is zero if and only if every r_i is zero. Indeed every summand is nonnegative in the usual ordering of the rationals, and every coefficient w_i is strictly positive. Clearing a nonzero scalar from an equation preserves its zero set. Therefore this transformation preserves the entire rational zero set, including every fiber of the input projection. It makes no new arithmetic assumption, requires no witness selection and does not modify the coordinates or residual equations.

The changed weights were selected by an exact greedy cancellation search. Search completeness is irrelevant to the equivalence proof; no global minimality claim is made. `positive_weights.py --out integer-weights --denominator-bits 1` reproduces the integer-weight search. The root directory also preserves the earlier rational-weight exploration, with 5,975 monomials and a common denominator multiplier. That alternative is not the selected candidate because it enlarges the coefficients.

## Frozen source and finite checks

The symbolic source is `resume-anchor-shared314-20261107/anchor-gamma313/candidate313-ir.json`, SHA256 `6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a`.

The ordinary source is `work/quartic-under300-20261107/10-combination/ordinary-anchor313/328/candidate-ir.json`, SHA256 `aabaf282330f1f7d8d00f0dfc529020504890fee427dcaf9b0537bf1f2d53748`.

`verify_and_lift.py` imports no producer code. It recomputes each primitive residual and expands its weighted square using unordered term pairs and an explicit factor of two for off-diagonal products. It compares the entire symbolic table against the producer's table, checks content one, degree four, and the occurrence of precisely the source coordinates.

The symbolic table has 5,985 coefficient-power entries and 5,982 monomials. It keeps C = 3^(2^25) unevaluated. For each monomial, its nonzero coefficient polynomial in C has a leading integer coefficient of absolute value at least one. The sum of the lower coefficient magnitudes plus one is below 2^7. Since C is greater than 2^(2^25), the leading term dominates, so specialization cannot remove a monomial.

The maximum coefficient remains exactly

    186624 * C^2 + 64 = 186624 * 3^(2^26) + 64.

The maximizing monomial is x89^4. For every other monomial coefficient p(C), the verifier computes both M(C) - p(C) and M(C) + p(C). Each nonzero difference has a positive leading coefficient, and its lower coefficients satisfy the same leading-term dominance test with a threshold below 2^1520. Thus both differences are strictly positive at the specified C. This verifies an exact maximum, not only a bit-length estimate.

## Ordinary lift

The ordinary companion changes the source rows 504 and 1903 to realize the fixed constant and adds its reviewed constant-chain rows. Neither changed row receives a new weight, and every added row retains weight one. The verifier checks literal equality of all other residual objects between the two source systems. Thus the reviewed constant realization commutes with the positive-weight compiler change.

The complete new decimal table is `integer-weights/ordinary328-polynomial.txt`. It has 6,024 monomials and occupies 209,130 bytes in ASCII, compared with 210,336 bytes for the original 328-variable table. Its maximum coefficient has 6,496 bits. Its JSON form is also included. The exact largest integer can be recomputed directly from either table; this report does not claim it equals the largest integer of the unweighted table.

## Inherited dependencies and review boundary

The rational-zero equivalence established here is relative to the source residual systems. Acceptance of those systems remains governed by their existing arithmetic and construction reviews. In particular, the original 313-variable approximation argument and the underlying height and restricted-converse inputs are not re-proved by the polynomial expansion checks.

The relevant existing reviews are `work/quartic-under300-20261107/10-combination/review-anchor-gamma313/REVIEW.md` and `work/quartic-optimization-20261107/resume-review-ordinary313-20261107/REVIEW.md`. The new finite compiler equivalence requires its own independent review before this alternative is called accepted. No source arithmetic application, release inventory or manuscript is changed by this proposal.
