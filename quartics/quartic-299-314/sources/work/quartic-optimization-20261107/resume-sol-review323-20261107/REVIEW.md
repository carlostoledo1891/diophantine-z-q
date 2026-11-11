# Independent review of the 323-variable scalar-chain rewrite

Accepted as an exact rational solution-set equivalence relative to the frozen, independently reviewed 326-variable construction. Reviewer /root/sol_protocol_policy_review. Author /root/astra_quartic_opt03_depth. November 7, 2026. No mathematical repair or author-file edit was supplied by this reviewer. Serving-model backend metadata is not independently established.

## Frozen scope

The reviewed report has SHA256 828cd7cfb7649b1e93cb3fbe22d1d5dc50f7d8ed1b71c20242b3634029417b15. The 323 IR has SHA256 dc804a0f236f81c29753c5f3496254641df0fa527dd522923f4dfa331e8d2ecd, its polynomial 0a08b05ce9924038009013f9f3628e19a4a8ee6566676178aeb57554fffb9571, and author verifier 2f1f5b95f878019ebc25df82251e9b9f07623f19632e02c13c6f1542790d6d4f. The source 326 IR is 48cf6abbc2bd5393b14413314e1297c8bf235bd990202c7bb97ac203b7387c84. The parent independent review is 9bc208d22884b33a2777446ddd826017db173aa30b50830f944bbd941a08482c. SOURCE-PINS.json records these bindings.

I read the report, producer, author verifier, literal source and candidate equations, and parent review. The numerical checks below use a new reviewer-owned checker importing neither producer nor author verifier. This review does not independently repeat the source326 arithmetic theorem audit. It proves that this local transformation retains that exact source's rational solutions on the unaffected coordinates.

## Nonzero divisors and both maps

For each detector the unchanged equation is RE=1, where R is the actual linear rational expression in the retained contact coordinates. My checker extracts that expression from the literal row and verifies that it uses no deleted or repurposed helper. Thus R and E are nonzero for every rational solution, including exceptional arithmetic cases.

In the new system write r for the repurposed helper. Its literal equations are

```text
E r = R^2
E4 r = E
E8 = E4^2
E19 r = E8^2
R E39 = E19^2
R E79 = E39^2
E158 = E79^2
E157 = R E158
```

The first equation gives r=R^2/E=R^3=E^(-3), which is nonzero. Every later divisor is therefore already known nonzero. Successive substitution forces E4=E^4, E8=E^8, E19=E^19, E39=E^39, E79=E^79, E158=E^158 and E157=E^157. Each square computes a new coordinate from an already determined value. No square root, sign selection, positivity assumption or additional nonvanishing hypothesis is used.

The source equations independently checked in the literal326 IR give E2=E^2, E4=E2^2, E8=E4^2, E E11=E8 E4 and E19=E11 E8, followed by the same E39/E79/E158/E157 equations. Since E is nonzero, E11=E^11 and all retained outputs have exactly the values stated above.

Given a 326 solution, delete each E2 and replace its E11 helper with R^3. Every new equation then vanishes. Given a 323 solution, restore E2=E^2 and replace r with E^11. Every source equation then vanishes. All other coordinates remain fixed in both directions. On the respective solution sets the two maps undo one another, since the replaced private values are uniquely forced. In particular, the full projection onto all coordinates outside the deleted/repurposed helpers is unchanged, including the input, point coordinates, scalar and anchor witnesses, detector groups, W and trace/pole coordinates.

## All changed, deleted and retained consumers

Exactly coordinates 361,409,457 are deleted. Coordinates 355,403,451 are repurposed from E11 to R3. Exactly rows 313,363,413 disappear. The nine changed rows are 544,546,550,552,556,558,745,760,775.

The independent incidence audit lists every occurrence of all six private coordinates in both systems. Every such occurrence belongs to those changed or deleted rows. No outside consumer remains. All 284 other residual objects are identical, including their terms and metadata. Every retained coordinate record is identical except the three declared helper names. The fixed parameter, schema, partitions and other top-level data are unchanged apart from the research status text. All retained E4/E8/E19/E39/E79/E158/E157 consumers consequently receive the same values. Historical slot names such as q10 and q40 introduce no alternative meaning.

## Full polynomial check

The reviewer checker separately parses C powers and variable monomials, rejects duplicate or malformed terms, clears each residual's rational denominators, removes its integer content, squares the resulting primitive polynomial and sums every coefficient. It matches the entire published table, rather than sampling evaluations or comparing counts alone.

All 323 declared rational coordinates occur, including the protected input coordinate. There are 322 witnesses and 293 quadratic residuals. The complete sum has 5840 monomials, degree four and integer content one. The five C-dependent terms equal those of the source326 polynomial. No two C powers share an ordinary variable monomial. Constant coefficients have at most 1520 bits. The unchanged leading coefficient 16C^2 remains the exact maximum for C=3^(2^25), which dominates the fixed integer and linear-C coefficients.

Over the rationals, a finite sum of squares vanishes exactly when every squared residual vanishes. Clearing a nonzero rational normalization factor changes no residual zero set. Therefore the polynomial encoding preserves precisely the rational-system equivalence established by the two maps.

## Decision and limits

No defect was found in this exact scalar-chain rewrite. It introduces no new arithmetic theorem, place selection, logarithmic precision assertion or exceptional-branch premise. The source326 arithmetic hypotheses and review qualifications remain in force. In particular, this acceptance does not independently establish the global integer-defining claim, approve a later composition, certify a manuscript release or establish an optimal variable count.

The finite search discussed by the author is not part of this proof. The explicit equations, unique solving order, two maps, complete consumer audit and full coefficient comparison supply the acceptance.

Reproduce the independent checks with `check.py` in this directory using a recorded compatible Python interpreter. CHECKS.json records the results. All author artifacts and earlier reviews remain unchanged.
