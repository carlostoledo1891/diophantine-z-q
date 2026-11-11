# Ordinary companions of reciprocal307

These three exact algebraic lifts use the frozen reciprocal307 IR. The source's new arithmetic remains subject to its separate review, and these new transport artifacts require independent review. No claim of independent source acceptance is made here.

| Total variables | Witnesses | Quadratic residuals | Quartic monomials | Constant gates | Maximum bits | Decimal digits | Text bytes |
|---|---|---|---|---|---|---|---|
|324|323|312|6486|16|1627|490|189891|
|323|322|311|6483|15|3250|979|197918|
|322|321|310|6480|14|6496|1956|218382|

All polynomials have degree four and integer content one. The324-variable lift satisfies the published coefficient bound below2^3247. The323-variable lift exceeds that bound by three bits. All three satisfy the8193-bit comparison bound. These are expanded table counts, not predicted savings. None meets the next publication threshold of fewer than300 total variables.

## Pinned source and unchanged interface

Source: `work/quartic-optimization-20261107/reciprocal307-20261107/candidate307-ir.json`, SHA256 `0b94aaf7669b3fe89cdf48f4718750991cfea4dd289695543f29b0cd533f29a1`. Source polynomial: SHA256 `90256d39e58b84a00b06003a4457ed56c1b282cd80a0c21c882a93411c660106`.

The source contains307 coordinates,295 residuals and6438 quartic terms. Rows504 and1903 are byte-equivalent JSON objects to the accepted313 source's corresponding rows and are its only consumers of the fixed parameter C. All reciprocal-slope equations, scalar inputs and detector outputs are left exactly as supplied. Input coordinate0 remains the protected input; every original coordinate object is retained. Only rows504 and1903 and fixed-parameter metadata change in each lift. Every other source object is checked exactly.

The weighted chains are the previously reviewed exact319 chains, whose review is `work/quartic-optimization-20261107/resume-sol-review-ordinary-chains-20261107/REVIEW.md`, SHA256 `6e9aaeb3530cce90f8d060a565c345927138a57a9c4343024f5620a96aa0c6d3`. The earlier313 transport review is `resume-review-ordinary313-20261107/REVIEW.md`, SHA256 `0d754cc8c86ac94f2e2ad246c13e8b42824a6eb2b0a6dfce7cec1735ea54cdfd`. These reviews are provenance, not automatic approval of the new files.

## Exact maps

Add coordinate1000, defined uniquely by Q=48x83^2+48x87^2+432x89^2. Add a constant chain c0=3^a0 and c_j=3^a_j*c_(j-1)^2. The three exponent lists are

    [513]*9+[2]+[0]*6;
    [1025]*10+[2]+[0]*4;
    [2049]+[2048]*11+[0,0].

The recurrence e0=a0, e_j=2e_(j-1)+a_j ends at2^25 in each case, so the final coordinate is exactly C=3^(2^25). The new rows504 and1903 are

    x55^2+6*x56^2-2*x57^2-4*C*x57-3*x903^2=0,
    x903-2*x543*x544-C*Q=0.

Every residual is quadratic in all quantified variables. Substitution of the unique Q and C recovers both original rows exactly. Forward extension is unique; reverse projection forgets precisely the added coordinates. No division, new guard, or arithmetic hypothesis is needed. New coordinate IDs and residual IDs1000 through1016 (or a shorter prefix) do not collide with retained source IDs. The inverse-anchor chain1101 through1108 and the common scale remain unchanged.

## Executable verification and exact coefficients

`build.py` constructs all three lifts and complete decimal JSON/text polynomial tables. `verify.py` imports no producer: it independently checks the literal constant recurrences, exact source-row recovery, all retained objects, active variable coverage, primitive residual normalization, complete sum of squares, degree, content, maximum coefficients and parsed text tables. `check_source.py` independently reconstructs the full source polynomial, checks all variable consumers and verifies that504/1903 are its only C-dependent rows and agree with313. Both checks pass.

Let K be the source polynomial's constant coefficient, recorded exactly in `INHERITED-CONSTANT.json`. It has1514 bits. The exact maxima are3^1026+K,3^2050+K and3^4098+K. Full decimal values are in the certificates and polynomial tables; no expansion of the enormous fixed C is performed. `MANIFEST.json` records each file's SHA256 and byte length, and pins all source/component inputs. `SUMMARY.json` and `VERIFICATION.json` record the numerical results above.

The source packet and all previously accepted artifacts remain unchanged. This packet is frozen for a separate, source-conditional finite transport review.
