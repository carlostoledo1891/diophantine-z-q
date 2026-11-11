# Quartics with 394 and 411 variables

The symbolic-coefficient quartic has 394 total rational variables, 393 witnesses, 364 quadratic residuals and 6,338 monomials. Its fixed integer is C=3^(2^25), and its largest coefficient is 16*3^(2^26). The ordinary decimal-coefficient companion has 411 variables, 410 witnesses, 381 residuals and 6,388 monomials. Its maximum coefficient has3247 bits. ARTIFACTS.json records the exact maximum as 3^2048 plus an explicit integer.

Both polynomials have degree four and integer content one. Compact physical coordinates are numbered1 through the total variable count, with x1 the input. The JSON and text tables contain every coefficient. The compact IR files contain the corresponding quadratic residuals. The source-ID IR files preserve the exact reviewed candidate bytes.

The ordinary construction uses16 repeated-squaring variables beginning with c0=3^1024, followed by one variable t=C*tau. The seventeenth variable keeps the rescaled anchor quadratic. Merely treating C as a variable without this multiplication gate would not give a quartic sum of squares.

## Verification

Run `python -B verify_lineage.py` from this directory. Python's standard library is sufficient. The verifier checks every file in SOURCE-MANIFEST.json, replays27 source-level finite verification stages beginning with the published498-variable baseline, verifies all final coefficient expansions and checks the compact and ordinary transformations. Its historical absolute certificate paths are mapped strictly to the corresponding copied files under sources. It does not need the original workspace, a network connection or the old repository location.

The sources tree includes the precise component inputs, certificates, producers, checkers, mathematical reports and review copies. The pipeline is more than a final-IR expansion: it checks order10 circuit replacement, hybrid polynomial identities and elimination certificates, reciprocal and rational-log transformations, all subsequent relative component deltas, and the final constant lift. Arithmetic validity depends on the accompanying mathematical arguments and independent reviews, not on finite polynomial checks alone.

## Review records and immutable outputs

The final mathematical composition review is reviews/mathematical-review.md. The separate compact/table/ordinary-lift review is reviews/artifact-review.md. ACCEPTANCE.json binds both to the exact files. ARTIFACTS.json was frozen before these reviews and retains its historical pending-status string; it is not the current acceptance record.

The independently accepted predecessor395 and397 alternative, when referenced in the source reports, remain separate research snapshots. Neither is substituted for the final394 file. Later improvements are outside this packet. Publication and manuscript approval are separate parent-task actions.
