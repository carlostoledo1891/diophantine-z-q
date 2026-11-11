# Independent review of the ordinary299 lifts

I accept all three frozen ordinary-coefficient lifts of the accepted reciprocal299-r2 source. The acceptance covers their exact witness maps, complete active-variable inventories, primitive sum-of-squares polynomials, decimal tables and actual coefficient bounds. No correction was needed.

Reviewer: agent03. The lifts and their current transport were authored by agent10; the earlier weighted-chain construction was authored by agent01. I did not author either. I have contributed to earlier arithmetic in the symbolic source's dependency chain. This review therefore accepts the new exact algebraic lifts relative to the already accepted299 mathematics; it does not independently reapprove that entire mathematics, claim a global variable lower bound or approve publication.

## Frozen objects

The reviewed packet is `work/quartic-under300-20261107/10-combination/ordinary-reciprocal299`. Its report SHA256 is `2139ab1681a9ec6ec63c547ea3278b8ea981cf9311c36893713ae291b685e809`; its manifest SHA256 is `904ccb6a91c8fae93071a8009c2403f852bf546db4fc6da2457d91f09f139e05`.

The symbolic source is `work/quartic-optimization-20261107/resume-elimination-20261107/reciprocal299-r2/candidate299-ir.json`, SHA256 `8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815`. Its polynomial SHA256 is `e208b503cad67bb53eb42fd78e64b3ebe9e99223692af91dd6c6b5b5b405ca3c`. Its complete independent review is `work/quartic-under300-20261107/10-combination/review-reciprocal299/REVIEW.md`, SHA256 `f51b3e1f571820f2d3b5bf6fb7b60e8b3a7506457bca0a72cbd3a3cfd8feb699`.

| Variables | IR SHA256 | Polynomial SHA256 |
|---|---|---|
|316|`07b84f80f2bcbd21f2ad9d7fa41d7bdaea12ff8fd8ec9092729c7e83fb51059f`|`cf01b5e68c9cefb4c11d06176ca97101b458391876d5960958b87c229397b13b`|
|315|`f9a6fab1b59cb744db80df93c0231b4075f654d8dbf80f4720c24d99036d3e4a`|`c53b8e0f61c37ebd94a44494b142329a7a72a937853adfa629eba838301fdefe`|
|314|`02b8b6a8b13a566ef520c7a65ec58fd6e63bafa9d7d447e323864b1bae29a5f7`|`2ea9fb17223a2e2a4fbf98f113d9e0e1da7019a74f4d2c7cefdb31e5b4637028`|

My checker verifies all33 manifest-listed packet and source objects against their exact hashes and byte lengths, and rechecks their hashes after the computation. It imports neither an author builder nor an author verifier. Author files are unchanged.

I read the prior weighted-chain review `work/quartic-optimization-20261107/resume-sol-review-ordinary-chains-20261107/REVIEW.md`, SHA256 `6e9aaeb3530cce90f8d060a565c345927138a57a9c4343024f5620a96aa0c6d3`. The present approval comes from checking the new299 transport itself, not from extending that older exact319 approval automatically. Its restricted lower-bound claims are outside this review.

## Exact maps and degree preservation

Only source rows504 and1903 contain the fixed symbol C. The independent reconstruction of the complete6630-term symbolic source polynomial confirms this source binding. Add the rational coordinate Q at1000, with

    Q=48*x83^2+48*x87^2+432*x89^2.

For a multiplier list a0,...,a(n-1), define coordinates successively by

    c0=3^a0,
    cj=3^aj*c(j-1)^2.

The lists are nine513s, then2 and six zeros for316; ten1025s, then2 and four zeros for315; and2049 followed by eleven2048s and two zeros for314. I verify every actual coefficient in every chain row. The exact recurrence e0=a0, ej=2e(j-1)+aj ends at33554432=2^25 in each case. Thus the final coordinate is exactly C=3^(2^25). No expansion of this enormous C is used.

Each new coordinate appears linearly as the output of its defining equation. Induction therefore gives a unique rational value, with no square-root sign choice. The lift changes the two source rows to

    x55^2+6*x56^2-2*x57^2-4*c_last*x57-3*x903^2=0,
    x903-2*x543*x544-c_last*Q=0.

All residuals are quadratic. The separate Q coordinate prevents a cubic product of the final C coordinate with a root square. Substituting the uniquely forced Q and final C restores both literal symbolic rows coefficient by coefficient. Every other source row and source coordinate record is unchanged. The added coordinate and residual IDs1000 through the appropriate final ID have no collision with the source.

Consequently any symbolic-source witness extends uniquely to each lift; conversely every lifted witness projects to the exact source witness. The input coordinate remains0. These inverse maps preserve complete rational solution sets. They introduce no new arithmetic premise, root or auxiliary-point domain, nonzero guard, local condition, or simultaneous approximation choice. Clearing denominators and dividing each quadratic residual by its integer content preserves its zeros. Over the rationals the resulting sum of squares vanishes exactly when every residual vanishes.

## Full tables and coefficient bounds

The independent checker recomputes every primitive quadratic square and compares every coefficient in each JSON polynomial. It separately parses each complete ASCII decimal text table and checks the same polynomial. Every coefficient is an ordinary integer; all symbolic C powers are zero. All declared variables occur, and there are no undeclared variables or duplicate IDs or monomials. Each polynomial has degree4 and integer content1.

| Total variables | Witnesses | Quadrics | Monomials | Constant gates | Maximum bits | Decimal digits | Text bytes |
|---|---|---|---|---|---|---|---|
|316|315|296|6678|16|1627|490|194399|
|315|314|295|6675|15|3250|979|202426|
|314|313|294|6672|14|6496|1956|222890|

Each row also uses the one Q gate. The exact maximum absolute coefficient occurs at the constant monomial. It is respectively

    3^1026+K,  3^2050+K,  3^4098+K,

where K is the1514-bit constant coefficient of the pinned symbolic source polynomial. I independently extract K from that reconstructed source polynomial and compare it with the full integer in the packet's `INHERITED-CONSTANT.json`, SHA256 `bc63d617d824783d6f64da1eb308419f8ddac1a8a6b14386e4bfadcf2b7b315a`. The maxima are checked against every other coefficient, not estimated from chain multipliers.

For the selected314-variable lift the exact maximum satisfies

    2^6495 <= 3^4098+K < 2^6496.

Its text-table SHA256 is `efb34a9664a3a2c5b0abe548463e646ba18d6f7e5ab5d9eff9e80bb8b461291e`. The correct advertised coefficient bound is strictly below2^6496. The old below2^3247 bound is false for this lift. The315-variable alternative also exceeds that older cap; only316 among these three satisfies it. All three satisfy the broader below2^8193 comparison cap.

The counts distinguish the299-variable symbolic polynomial from its314-variable selected ordinary companion. Nothing in this review describes the ordinary companion as having fewer than300 variables.

`check.py` and `CHECKS.json` in this review directory contain the independent evidence. The checker completes using the standard library and modest integers, without expanding C. No source, candidate or release file was edited.
