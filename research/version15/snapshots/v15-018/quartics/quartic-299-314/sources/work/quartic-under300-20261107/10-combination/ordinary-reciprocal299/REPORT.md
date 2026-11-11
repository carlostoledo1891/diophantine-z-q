# Ordinary companions of accepted reciprocal299-r2

These are exact ordinary-coefficient lifts of the independently accepted299-variable source. The new lift artifacts require a separate finite transport review; their author does not approve them independently. Every symbolic source witness extends uniquely to each lift, and projection forgets only the new constant-chain and root-sum coordinates.

| Total variables | Witnesses | Quadratic residuals | Quartic monomials | Constant gates | Maximum bits | Decimal digits | Text bytes |
|---|---|---|---|---|---|---|---|
|316|315|296|6678|16|1627|490|194399|
|315|314|295|6675|15|3250|979|202426|
|314|313|294|6672|14|6496|1956|222890|

All polynomials have degree four and integer content one. The316-variable lift satisfies the previous published coefficient bound below2^3247. The315-variable lift exceeds that bound by three bits. The smallest lift has314 variables and requires6496-bit coefficients; it is below2^6496 and hence below the8193-bit comparison cap. Choosing it must not silently retain the old3247-bit bound. All three alternatives are retained. The symbolic source has299 variables; these are its larger ordinary companions.

## Pinned source and exact maps

The source is `work/quartic-optimization-20261107/resume-elimination-20261107/reciprocal299-r2/candidate299-ir.json`, SHA256 `8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815`. Its polynomial has SHA256 `e208b503cad67bb53eb42fd78e64b3ebe9e99223692af91dd6c6b5b5b405ca3c`. The full source review is `work/quartic-under300-20261107/10-combination/review-reciprocal299/REVIEW.md`, SHA256 `f51b3e1f571820f2d3b5bf6fb7b60e8b3a7506457bca0a72cbd3a3cfd8feb699`.

The reused weighted chains were independently reviewed at `work/quartic-optimization-20261107/resume-sol-review-ordinary-chains-20261107/REVIEW.md`, SHA256 `6e9aaeb3530cce90f8d060a565c345927138a57a9c4343024f5620a96aa0c6d3`. This is a new transport of that exact algebraic construction, not automatic acceptance of the present artifacts.

Add Q in coordinate1000 with Q=48x83^2+48x87^2+432x89^2. Add the uniquely specified constant chain c0=3^a0 and c_j=3^a_j*c_(j-1)^2, using respectively

    [513]*9+[2]+[0]*6;
    [1025]*10+[2]+[0]*4;
    [2049]+[2048]*11+[0,0].

The exact exponent recurrence ends at2^25, so the final coordinate equals C=3^(2^25). Only source rows504 and1903 contain C. They become

    x55^2+6*x56^2-2*x57^2-4*C*x57-3*x903^2=0,
    x903-2*x543*x544-C*Q=0.

These are quadratic in all quantified variables. Substituting the unique Q and C recovers the literal symbolic rows. This proves both directions of the witness map without division, a new guard, or a new arithmetic application. The original input coordinate0 and all299 source coordinates remain unchanged. Every other source row and all other metadata objects are checked exactly. Added coordinate and residual IDs1000 through1016, or a shorter prefix, have no collision. In particular the S orientation, all four reciprocal interfaces, corrected196/197 cache, scalar input and inverse-anchor gamma chain are unchanged.

## Complete tables and verification

`build.py` emits each IR, complete decimal polynomial JSON, complete tab-separated text table and certificate. `verify.py` imports no producer. It checks the exact chain values and source-row recovery, every retained object, complete active-variable inventory, primitive residual normalization, full sum of squares, degree, content, maximum coefficients and text-table parsing. `check_source.py` separately reconstructs the complete6630-term symbolic source table and checks the exclusive C-consumer set. All checks pass.

The source constant coefficient K is recorded in full in `INHERITED-CONSTANT.json` and has1514 bits. The exact maxima are3^1026+K,3^2050+K and3^4098+K. Full decimal coefficients appear in the certificates and tables. The enormous fixed C itself is never expanded. `SUMMARY.json`, `VERIFICATION.json` and `MANIFEST.json` bind actual counts, byte lengths and SHA256 values.

The rejected first299 draft and all accepted source artifacts remain untouched. No publication or manuscript change is made by this packet.
