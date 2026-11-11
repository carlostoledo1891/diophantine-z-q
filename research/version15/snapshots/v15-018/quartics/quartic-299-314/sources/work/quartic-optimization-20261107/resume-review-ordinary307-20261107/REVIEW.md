# Independent review of ordinary reciprocal307 lifts

I accept the exact constant-chain transport and expanded tables in the three frozen ordinary reciprocal307 lifts. This acceptance is conditional on independent mathematical acceptance of the pinned source307. It does not review or approve that source's new point-domain or addition arguments.

Reviewer: `/root/astra_quartic_opt05_anchor`, November 7, 2026. Lift author: `/root/astra_quartic_opt10_combination`. I did not author these lifts. I authored the auxiliary-domain lemma consumed by source307, so this review expressly excludes that lemma and the full source307 mathematics. Agent01's separate source review supplies any acceptance of those obligations. This report does not infer its outcome.

## Frozen objects

The author folder is `work/quartic-under300-20261107/10-combination/ordinary-reciprocal307`. Its report has SHA256 `93f81036962bb8ac96d17dac88dc20b2e08bcf5bb412bc926ed466c4de15a1ba`; its manifest has SHA256 `8a32db7bddcf0dc8d7dcfc55853b37443a7a46991a9c10c42ede826fe71ff1bf`.

The source IR is `work/quartic-optimization-20261107/reciprocal307-20261107/candidate307-ir.json`, SHA256 `0b94aaf7669b3fe89cdf48f4718750991cfea4dd289695543f29b0cd533f29a1`. Its full polynomial table has SHA256 `90256d39e58b84a00b06003a4457ed56c1b282cd80a0c21c882a93411c660106`. I independently expanded its 295 primitive quadratic residuals and matched all 6438 symbolic coefficient entries, including its inherited constant K. I did not merely trust K copied into the author's lift metadata.

| Variables | IR SHA256 | Polynomial SHA256 |
| ---: | --- | --- |
| 324 | `85bcfa08f91ba77219d5d8f2865b7ce84549256bbf22f8caa269e28b18aaa59d` | `0fad0702e756522819aa1bbd4991979813e4358fccfb4373c274c4ba631464fe` |
| 323 | `1758797291df98598df3fcb7617ff25892002079d03abeed0e8f8fa51811630f` | `c0c0c0d398dae2ae6f4f717d6a056c54a0ed0e391f1f8bf90016046d6470f48c` |
| 322 | `fd590d02b6ee8baf291b385d6de029d3684b20234a1e6382163b230661cebd5e` | `cda9710db0963c2127166437dcd358d45b548ead36d2be7c599e8381166395d5` |

All 42 manifest/source pins and all stated byte lengths were checked. `SOURCE-PINS.json` records those pins. No author program was imported or executed. The checker derives from my earlier independent ordinary313 review, with the source, expected counts and frozen manifest changed, and with a full independent expansion of source307 added.

## Exact maps and unchanged consumers

Rows 504 and 1903 are the source's only C-dependent residuals. All 307 source coordinate records remain identical. Every one of the other 293 residual objects remains identical. All unrelated top-level metadata is identical, with only status and fixed-parameter metadata permitted to change. In particular all reciprocal-slope rows, auxiliary ratio equations, scalar equations, detector rows 903/904, and the inverse-anchor chain are retained literally.

The added coordinate and row IDs are exactly 1000 through 1016, or the corresponding shorter prefix. They are disjoint from every source coordinate and residual ID. Coordinate 1000 is uniquely defined by

    Q = 48*x83^2 + 48*x87^2 + 432*x89^2.

The weighted constant chains use the exponent lists

    [513]*9 + [2] + [0]*6,
    [1025]*10 + [2] + [0]*4,
    [2049] + [2048]*11 + [0,0].

The first equation is c0=3^a0; every subsequent equation is c_j=3^a_j*c_(j-1)^2. Their outputs occur linearly with coefficient one, so the new coordinates have unique rational values. The recurrence e0=a0 and e_j=2e_(j-1)+a_j ends at 33554432 in each case. Thus the last coordinate is exactly the original C=3^(2^25), without selecting a square-root branch or adding a nonzero assumption.

The checker independently reconstructs the two new anchor residuals as

    x55^2 + 6*x56^2 - 2*x57^2 - 4*c_last*x57 - 3*x903^2,
    x903 - 2*x543*x544 - c_last*Q.

Substituting the unique Q and the symbolic C recovers both literal source residuals exactly. Therefore every source solution extends uniquely, and forgetting the added coordinates is the inverse projection. Both maps fix the distinguished input x0 and all original witnesses. This is a purely rational coordinate extension, independent of the correctness of any interpretation of those source witnesses.

The root arguments in Q are unchanged. There is no new squareclass choice, root sign choice, valuation premise, logarithm precision or approximation order. Neither C nor Q is identified with the common detector scale or its inverse-anchor parameter. The source arithmetic is needed only to conclude that the source's rational input projection is the desired set; it is not used to prove this transport equivalence.

## Complete table checks

For source307 and each lift, the reviewer checker clears every residual's coefficient denominators, removes its integer content, expands its square and sums all resulting terms. It checks the resulting full polynomial against the frozen JSON table. For every lift it also parses the entire ASCII decimal table and compares each monomial and integer coefficient against that same independently computed polynomial. It verifies exact variable coverage, degree four, integer content one and absence of any remaining symbolic C power in each ordinary table.

| Variables | Residuals | Quartic monomials | Maximum bits | Maximum decimal digits | Decimal text bytes |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 324 | 312 | 6486 | 1627 | 490 | 189891 |
| 323 | 311 | 6483 | 3250 | 979 | 197918 |
| 322 | 310 | 6480 | 6496 | 1956 | 218382 |

The independently derived inherited constant K has 1514 bits and equals the complete integer in `INHERITED-CONSTANT.json`. Comparing every coefficient proves that the exact maxima are 3^1026+K, 3^2050+K and 3^4098+K, respectively. Each occurs at the constant monomial. This calculation accounts for overlapping constant contributions from all residual squares. It does not mistake a residual coefficient for a quartic coefficient.

The 324-variable lift satisfies the published bound below 2^3247. The 323-variable lift exceeds that bound by three bits. All three are below 2^8193. None is below 300 total variables.

No defect or author repair was found. A one-off checker-generation command initially asserted the presence of an unused replacement string and exited before writing the checker; removing that unused command entry resolved the setup error. The completed checker and its mathematical assertions passed on their first execution. All frozen author files remain unchanged.

Reproduce with `python -B work/quartic-optimization-20261107/resume-review-ordinary307-20261107/check.py`. The recorded run used the supplied Python runtime. This report approves these exact finite transports and tables, conditional on the separate pinned-source acceptance. It does not approve publication, any future source modification, or the source307 arithmetic itself.
