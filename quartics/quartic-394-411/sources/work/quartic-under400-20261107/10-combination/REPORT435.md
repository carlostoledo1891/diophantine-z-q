# Guard and positive correction combined at 435 variables

The frozen `combined435-ir.json` has SHA256 `c4c8a0623be27e675f73363043ce2bc44956bd128257060e471abca9b53a0859`. Its polynomial SHA256 is `3367f07f7045f4fac1fa41018893b344e4b0a8452e3f64586cc48a3293647173`. The exact totals are435 variables,434 witnesses,412 quadratic residuals and6,572 quartic monomials. Content is one and the maximum coefficient is16*3^(2^26). The fixed coefficient remains C=3^(2^25).

The accepted source is439, with parent review copied to `inputs/composition439-review.md`. Two independently reviewed components are applied:

- The scalar f1 guard replaces the f0 guard and removes its private f0 coordinate, saving one. Its non-author review is `inputs/scalar-guard-review.md`. Reverse reconstruction uses f0=g0^2+2g1^2>0; forward reconstruction uses the inherited exact nonvanishing of f1 on the nonzero even scalar orbit. The439 odd-norm changes preserve the actual root points and their odd indices, so that orbit premise remains available.
- The label becomes beta=2X^2+2403 and the scalar correction chain uses five positive generators3,11,17,35,91, saving three. Its non-author review is `inputs/scalar-shift-review.md`. That review checks the simultaneous32 local squareclasses, positivity, the unchanged contact/height estimates and the actual completeness order of choices. It is a new arithmetic label and correction construction, not an old-witness bijection.

`combine_positive435.py` transports both pinned component deltas with exact old-equation, coordinate-semantic and private-consumer checks. `verify_combination.py 435` independently reconstructs the result and checks every quartic coefficient. Both passed.

The extra `verify435_consumers.py` checks the complete physical input-square interface after scalar fusion. Starting from the guard-only438 intermediate, it rediscovers every row containing Y, rather than trusting the earlier component's list. Every non-correction row is exactly its predecessor with Y replaced by Y+1200, except `inputSquare.definition`, which remains Y=X^2. It found15 shifted rows and checks all five new correction equations. Its result is `consumers435.json`.

The scalar f1 guard changes no input-square consumer or scalar point value. The positive correction changes no point chart, no scalar f1 or anchor value, and no shared reciprocal identity. Their proofs therefore compose with the already accepted439 source. Final non-author composition review is pending; the candidate is not promoted merely because its finite checks pass.

The separate437 H.j-rescaling candidate starts from439 and has not been included here. Its review remains pending. The proposed further norm-tree saving is also not included. The below400 release threshold has not been reached, and all published files remain unchanged.
