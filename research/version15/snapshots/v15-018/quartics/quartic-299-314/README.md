# Quartics with299 and314 variables

The symbolic quartic has299 total rational variables,298 witnesses,279 quadratic residuals and6630 monomials. Its fixed integer is C=3^(2^25), and its maximum coefficient is186624*3^(2^26). The selected ordinary companion has314 variables,313 witnesses,294 residuals and6672 monomials. Its largest coefficient has6496 bits and1956 decimal digits, with strict bound below2^6496. This is a larger coefficient bound than the previous edition's2^3247 bound.

Both polynomials have degree four and integer content one. The canonical JSON and text tables use consecutive physical coordinates1 through the total variable count, with x1 the input. The symbolic text table is228028 bytes and the ordinary text table is264430 bytes. Each JSON/table contains every coefficient. The two coordinate-map files provide exact bijections to the preserved source IDs. The original314 source-ID text, with input x0 and sparse IDs, is separately preserved byte-for-byte as `quartic-314-source-id-coefficients.txt`,222890 bytes.

`candidate299-ir.json`, `candidate314-ir.json`, `polynomial299.json` and `polynomial314.json` preserve the exact reviewed source bytes. `compact299-ir.json` and `compact314-ir.json` give the consecutive-coordinate quadratic systems. `ARTIFACTS.json` binds their hashes, actual counts, byte lengths and maximum coefficients. Its historical pending-remap status is superseded only by the separately pinned artifact review in `ACCEPTANCE.json`; the accepted artifact bytes were not rewritten.

## Verification

Run `python -B verify_lineage.py` from this directory. Only Python's standard library is required. The verifier checks the exact source manifest, replays28 finite verification stages, reconstructs the public tables and both coordinate bijections, parses the complete text coefficients, and checks that the frozen source files remain unchanged. Historical report writes are captured; direct file writes are rejected. Historical absolute paths are redirected only to their exact packaged relative paths. The original workspace and network are not needed.

The finite replay begins with the exact published394-variable baseline and its independent acceptance records. It checks all subsequent source transformations used in the selected branch through392t,390,372,369,366, detector/anchor compositions, shared314, sparse arithmetic, anchor313, reciprocal307, alternate-ordinate301, corrected oriented299 and the ordinary lift. It also replays the final independent ordinary, compact and R6 inventory checks. It does not pretend to re-prove the baseline's inherited arithmetic or its earlier compiler history. The full baseline polynomial is checked against the preserved exact baseline IR.

`SOURCE-MANIFEST.json` pins the source files and mathematical/review evidence, while `VERIFICATION-PLAN.json` specifies the executed stages. Producers and rejected/alternative artifacts are included for provenance but are not executed as accepted verification targets. `PACKAGE-MANIFEST.json` binds this complete frozen preparation packet.

## Exact ordinary lift

The selected lift adds14 uniquely determined constant-chain coordinates and one root-sum coordinate. The chain recurrence is c0=3^2049, then c_j=3^a_j*c_(j-1)^2 with exponent list `[2049]+[2048]*11+[0,0]`. Its final value is C=3^(2^25). The extra root-sum coordinate Q=48*x83^2+48*x87^2+432*x89^2 uses source IDs. It keeps the anchor definition quadratic when C becomes a coordinate. The exact decimal maximum is3^4098+K, with K the1514-bit inherited constant coefficient recorded in the source certificate. Forward extension is unique and reverse projection forgets only the new helpers.

The larger316-variable alternative satisfies the former2^3247 coefficient bound; the315-variable alternative has3250-bit coefficients. Both remain in the packaged source evidence and ordinary-lift review. Neither is substituted for the selected314-variable artifact.

## Review scopes and rejected history

`reviews/mathematical-review.md` accepts the exact corrected299 construction. The301 step has an exact guarded witness reconstruction, whereas the S extension in299 enlarges the auxiliary-point domain and preserves the rational input projection through its reviewed arithmetic argument. It does not give a private-witness bijection back to all old square-root coordinates. `reviews/ordinary-review.md` accepts the exact algebraic lifts, `reviews/artifact-review.md` accepts the consecutive-coordinate serialization, and `reviews/inventory-review.md` accepts the structural R6 record only. None silently supplies independence for its author's earlier mathematics.

The first299 attempt used undeclared alternate-cache coordinates202/203 and is explicitly rejected. Its exact bytes remain under `sources/work/quartic-optimization-20261107/resume-elimination-20261107/reciprocal299`, with the findings and rejection. The selected corrected branch is the sibling `reciprocal299-r2`, which uses196/197. `ACCEPTANCE.json` binds the distinction and the independent reviews.

This package is isolated release preparation. Final manuscript/source-coverage review, installed-wrapper review and publication are separate decisions. No protocol branch, remote or published manuscript is modified by this packet.
