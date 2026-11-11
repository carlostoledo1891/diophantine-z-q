# Independent review of the ordinary-coefficient companions

I accept the three exact ordinary-coefficient lifts of the frozen exact319 system. I also accept the stated constant-gate lower bounds within the explicit isolated monomial-chain model described below. This does not establish an unrestricted minimum for Diophantine representations or approve a transport onto315.

Reviewer `/root/sol_protocol_final_review`, November 7, 2026. Author `/root/astra_quartic_opt01_elimination`. I did not author the lifts or their search. Exact serving-model metadata is not independently attested.

## Frozen scope

The author report has SHA-256 `fa18137456df72960814f9d1a71bfdc8397ab80dacf6ba7b53ec2dfcb3c444a1`. MANIFEST.json has SHA-256 `cbe658c362e39a2ed095e5ca1a4ab8f768091fd71ff4d405bf277d388ae49ff5`; I checked every file hash it lists, including the three IRs and full decimal polynomial tables.

The exact source319 IR is `847d21a2d0a45571f043b82289df0da55f4e814167844bdc39fc134e4f4c2676`, with polynomial `8320b69d290a37017060e34742fb025cbc1c13e40a5b7d750893e9912d3796ef`. It is the source accepted in my separate exact319 review. These companions have not been transported to the lower-variable315 construction and do not use the positive365 or earlier379 anchor.

| Variables | IR SHA-256 | Polynomial SHA-256 |
| --- | --- | --- |
| 336 | `72ef14cca86d1b4a817f93c5c2abf15b3a88a479ad7477f19b96c619daee6c39` | `0b87575e8d9539935fd9f073903e1d8a7babd6c1d11b5606e575100354d27f03` |
| 335 | `0985485cfda55f03b3dbde5949141fbad0846cd33fc0109aec7af024527fd217` | `6e2f547800d23c794801583ef3f5afced5e70daf9b0f0895f15bedb04c44a166` |
| 334 | `8cfc3dbbd900d5393a23572d2d4571b49fa1927a02a1297dcab281017c252951` | `7d71c71c5f1b243b3c6cf46a6d0179e695bb5342bc04ebffa9cb228bbfccd18d` |

## Exact chains and both witness maps

I verified every chain equation in each actual IR. They define c0=3^a0 and ci=3^ai*c(i-1)^2, with the output appearing linearly. Their rational values are therefore unique. The exponent recurrence ei=2e(i-1)+ai is exact; it requires no sign choice or square-root extraction.

For336 the multiplier list is nine513s, then2, then six zeros. The exponent reaches262143 after nine gates, then524288 and finally33554432. For335 it is ten1025s, then2, then four zeros, reaching1048575,2097152 and33554432. For334 it is2049 followed by eleven2048s and two zeros, reaching8388608 after twelve gates and then16777216 and33554432. Thus each last coordinate is exactly C=3^(2^25). This conclusion uses integer exponent arithmetic and does not require forming C's enormous decimal representation.

The only symbolic C consumers in source319 are rows504 and903. The lift adds Q=48v83²+48v87²+432v89² and replaces those consumers by

```text
u²+6v²-2w²-4*c_last*w-3*T² = 0
T-2*g0*g1-c_last*Q = 0.
```

Every equation is quadratic in the actual quantified variables. In particular the separate Q gate is necessary in this construction because substituting a variable directly for C in C*v83² would be cubic. My checker verifies all occurrences of Q and the last chain variable, every added row, every unchanged source row and coordinate, and the metadata identifying C with the last coordinate. All residual terms have symbolic C power zero.

Given a source319 solution, set Q to its quadratic value and give the new chain its unique values. The lifted rows become the original source rows. Conversely, the chain equations force c_last=C, and the Q equation gives its unique value; forgetting the added coordinates restores every source residual and coordinate. These maps are inverse on complete rational solution sets. No arithmetic, nonzero guard, local condition, real restriction or point choice is changed.

## Complete expanded tables and exact maxima

My independent checker imports no producer or author verifier. It clears each residual's rational denominators, divides by its integer content, expands every square and compares every coefficient in all three tables. Every stored table coefficient is an ordinary decimal integer and every C power is zero. All declared coordinates occur. The exact results are

| Variables | Witnesses | Residuals | Quartic monomials | Maximum bits | Maximum decimal digits |
| --- | --- | --- | --- | --- | --- |
| 336 | 335 | 306 | 5707 | 1627 | 490 |
| 335 | 334 | 305 | 5704 | 3250 | 979 |
| 334 | 333 | 304 | 5701 | 6496 | 1956 |

Each polynomial has degree four and integer content one. I independently extracted the1514-bit constant coefficient K from the pinned source polynomial and compared its exact integer to INHERITED-CONSTANT.json. The maximum is the constant coefficient, respectively3^1026+K,3^2050+K and3^4098+K. These include the inherited contribution K; reporting only a pure power of3 would give the wrong exact coefficient. Full integer comparison verifies that no other coefficient is larger in absolute value.

Consequently336 satisfies the3247-bit cap,335 exceeds it by three bits, and334 satisfies the8193-bit cap. These are actual table results, not inferred estimates from the multiplier sizes.

## Restricted gate lower bound

The accepted lower bound applies to acyclic chains whose gates define a new coordinate as a fixed power-of3 multiplier times at most two earlier chain coordinates. Each seed is counted as a gate and its fixed exponent is bounded by the same A. No uncounted, unbounded power-of3 seed, division by a variable, shared nonconstant computation or alternative system rescaling is admitted. The root-sum Q gate is retained separately.

Within that model, induction bounds the largest absolute exponent after n gates by A(2^n-1), and therefore bounds the largest positive exponent too. The coefficient cap bounds the multiplier exponent by bit_length(3^(2A))≤B. In the primitive isolated chain, the squared multiplier gives a nonnegative even-exponent monomial coefficient. Cross terms involving the newly defined variable cannot cancel that coefficient because acyclicity makes that new variable occur to odd degree in the cross term. For a constant seed the contribution is a constant coefficient rather than a degree-four monomial; the same coefficient bound applies.

I computed the cap limits using exact integer powers, avoiding logarithmic rounding. For B=3247, A≤1024 and fifteen gates reach at most33553408, below33554432. At least sixteen constant gates are necessary, attained by336 when the separate Q gate is included. For B=8193, A≤2584 and thirteen gates reach at most21165544, again below33554432. At least fourteen constant gates are necessary, attained by334.

This verifies optimal constant-gate counts only within that model and its fixed Q lift. It excludes no more general arithmetic circuit, implicit polynomial definition, shared gate, different anchor scaling or unrelated Diophantine construction.

## Additional bounded census and decision

I independently repeated the quadratic-part census. All319 source variables occur quadratically. The287 C-free rows outside504/903 have rank287 over Q; the unique quadratic columns g0*g1 and T² give the remaining two independent rows for every fixed C. Hence no nonzero scalar linear combination of the289 source residuals becomes affine. This is a statement about that linear-combination space, not the generated ideal or general eliminability.

The author verifier and local census also passed with their outputs redirected into this review directory. AUTHOR-UNMODIFIED.json records unchanged hashes for all author files. CHECKS.json records the independent table, exponent, cap and rank checks. Earlier accepted artifacts remain unchanged.

No unresolved defect was found in these three lifts or the restricted claims above. Their arithmetic status remains that of the exact319 source. There is no ordinary lift of315 in this packet, no unrestricted optimality claim, and no publication approval. Run `python -B work/quartic-optimization-20261107/resume-sol-review-ordinary-chains-20261107/check.py` from the workspace root using a recorded compatible interpreter to reproduce the independent checks.
