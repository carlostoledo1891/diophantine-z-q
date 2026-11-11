# Independent review of ordinary anchor313 lifts

I accept the three frozen ordinary-coefficient lifts of accepted anchor-gamma313. This is an exact coordinate-extension review, with no new arithmetic application. It does not reaccept the underlying313 proof, which I coauthored and agent10 independently accepted.

Reviewer: `/root/astra_quartic_opt05_anchor`, November 7, 2026. Lift author: `/root/astra_quartic_opt10_combination`. I did not author these lifts. My checker reuses polynomial helpers and the ordinary-lift checking structure from my previous independent314 transport review. It imports and executes no author program.

## Frozen scope

The author directory is `work/quartic-under300-20261107/10-combination/ordinary-anchor313`. REPORT.md has SHA256 `ffce81ba79c6b4192e49d7f4ca9b9db20923a6f05fd0d256dec1fa59cf4f6e58`, and MANIFEST.json has SHA256 `14700456683d1804396778248065a3c504d200a1247e8d7d4aec918b5029e218`. I checked every file length and hash in that manifest and its source list. All41 recorded source/artifact pins are in this review's `SOURCE-PINS.json`.

The exact source313 IR is `6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a`. Its independent arithmetic/construction review is `10-combination/review-anchor-gamma313/REVIEW.md`, SHA256 `981dff20bd980f2a040e8b31418cdd0c74e7bcf6e1356c6322fd01f9b42cca13`. That existing acceptance supplies the inherited source theorem; it is not an approval of a later source alteration.

| Lift | IR SHA256 | Polynomial SHA256 |
| --- | --- | --- |
|330|`8b4b7552b8f64fc2448c55ce0a396b12d436663afe240725734b92f2b582967b`|`acad16b44532d0be157ed6905ef22f46db5d4691a013bb4184ae3b43d1d2ecd3`|
|329|`fe3509d2f7591a8a9b9d442914920adb800316a337b2376d36612a5df43b420f`|`03d6fb848f4d35a34487aa8e9d26a51804c78a45ec8158f1bcc32d23d288a87f`|
|328|`aabaf282330f1f7d8d00f0dfc529020504890fee427dcaf9b0537bf1f2d53748`|`e49a2ca3d4d4c2b9575e39b4ea4b6f1e4e75d0c8b8ce9b9df4545c9a87f41407`|

## Exact witness maps and consumers

All313 source coordinate records remain identical. Only source rows504 and1903 change; all other281 row objects are identical. The only added coordinates and rows are1000 through1016, or the shorter prefix for the two shorter chains. These are disjoint from every source coordinate/row ID. Detector rows903/904 remain unchanged, distinct from coordinate903 and anchor row1903.

Coordinate1000 is forced to Q=48v83^2+48v87^2+432v89^2. The three exponent lists are nine513s followed by2 and six zeros; ten1025s followed by2 and four zeros; and2049 followed by eleven2048s and two zeros. Each first gate defines c0=3^a0, and each next gate defines c_j=3^a_j*c_(j-1)^2 with its output linear. Thus every added chain coordinate is uniquely determined over the rationals. The exact integer exponent recurrence ends at33554432 in all three chains, so the last coordinate is precisely the fixed source C=3^(2^25).

The two new anchor rows are exactly

    u^2+6v^2-2w^2-4*c_last*w-3*T^2=0,
    T-2*g0*g1-c_last*Q=0.

My checker derives these rows independently and substitutes the unique Q and symbolic C to recover the literal source rows. Therefore each source solution has a unique extension, and forgetting only the new helpers is the inverse. Both maps fix the distinguished input and every source witness.

In particular the retained u=v55 and the eight inverse-anchor power coordinates are unchanged. Their inverse equation still excludes u=0, and gamma=1/u has exactly the same meaning. The constant C chain is not identified with the common scale. The source's local anchor targets, rational approximation, finite/real ordering and final H choice need no alteration. Adding Q does not restrict its root arguments; it only records their already determined polynomial value.

## Complete finite checks

The reviewer-written checker verifies every unchanged object and every added equation, all IDs and active coordinates, both source-row recoveries and the exact coefficient metadata. It independently clears denominators and primitive content in every residual, expands every square and compares every coefficient in each full JSON table. It then parses each complete decimal text table and compares that table with the same independent expansion.

| Variables | Residuals | Monomials | Maximum bits | Decimal digits |
| ---: | ---: | ---: | ---: | ---: |
|330|300|6121|1627|490|
|329|299|6118|3250|979|
|328|298|6115|6496|1956|

Every polynomial has degree four and content one. The inherited constant K has1514 bits and matches the supplied complete integer. Comparing every actual coefficient proves that the maxima are3^1026+K,3^2050+K and3^4098+K, respectively, all at the constant monomial. The330 lift satisfies the3247-bit cap;329 exceeds it by three bits;328 satisfies the8193-bit cap. No expansion of the enormous source C was needed.

No defect or repair was found. All author files remain unchanged. Reproduce with `python -B work/quartic-optimization-20261107/resume-review-ordinary313-20261107/check.py`; the recorded run used the supplied Python runtime. This acceptance is source-specific and does not approve a publication or any later lift. The already frozen inventory r4 retains its earlier cutoff and is not edited by this review.
