# Ordinary companions with explicit coefficient caps

Author: `/root/astra_quartic_opt01_elimination`, November 7, 2026. These are exact ordinary-coefficient lifts of the frozen symbolic319 construction. They retain C=3^(2^25) and its original anchor parameter. They do not import the changed positive-anchor premise of the earlier379 proposals. No frozen symbolic file or production file was modified. Independent review is required.

The smallest construction delivered under the requested 8193-bit coefficient cap has **334 total variables,333 witnesses,304 quadratic residuals and5701 quartic monomials**. Its largest coefficient has 6496 bits and 1956 decimal digits. Under the tighter released-artifact 3247-bit cap, the delivered construction has **336 variables,335 witnesses,306 residuals and5707 monomials**, with a 1627-bit largest coefficient. The intermediate 335 construction is included to show the sharp transition just above that cap.

| Ordinary variables | New constant gates | Extra root-sum gate | Residuals | Monomials | Maximum coefficient bits | Decimal digits |
| --- | --- | --- | --- | --- | --- | --- |
| 336 | 16 | 1 | 306 | 5707 | 1627 | 490 |
| 335 | 15 | 1 | 305 | 5704 | 3250 | 979 |
| 334 | 14 | 1 | 304 | 5701 | 6496 | 1956 |

All three polynomials have degree four and integer content one. These are actual expanded artifacts, not count estimates. A restricted chain lower bound is proved below; no unrestricted minimum over every possible Diophantine presentation is claimed.

## Exact artifacts

The source is `../exact319/candidate319-ir.json`, SHA256 `847d21a2d0a45571f043b82289df0da55f4e814167844bdc39fc134e4f4c2676`. Its polynomial is `../exact319/polynomial319.json`, SHA256 `8320b69d290a37017060e34742fb025cbc1c13e40a5b7d750893e9912d3796ef`.

| File | SHA256 |
| --- | --- |
| 336/candidate-ir.json | 72ef14cca86d1b4a817f93c5c2abf15b3a88a479ad7477f19b96c619daee6c39 |
| 336/polynomial.json | 0b87575e8d9539935fd9f073903e1d8a7babd6c1d11b5606e575100354d27f03 |
| 335/candidate-ir.json | 0985485cfda55f03b3dbde5949141fbad0846cd33fc0109aec7af024527fd217 |
| 335/polynomial.json | 6e2f547800d23c794801583ef3f5afced5e70daf9b0f0895f15bedb04c44a166 |
| 334/candidate-ir.json | 8cfc3dbbd900d5393a23572d2d4571b49fa1927a02a1297dcab281017c252951 |
| 334/polynomial.json | 7d71c71c5f1b243b3c6cf46a6d0179e695bb5342bc04ebffa9cb228bbfccd18d |

## Weighted squaring chains

Instead of imposing only c_i=c_(i-1)^2, allow a fixed integer multiplier:

    c_0=3^a_0,
    c_i=3^a_i*c_(i-1)^2.

These are quadratic equations with modest ordinary integer coefficients. They have unique rational solutions c_i=3^e_i, where

    e_0=a_0, e_i=2e_(i-1)+a_i.

There is no square-root sign branch because each equation defines its output linearly. The final exponent is2^25 in all three chains. No computation forms the enormous final value C in decimal.

For 336, use 16 gates with multiplier exponents

    (513 repeated9 times, 2, 0 repeated6 times).

The exponent after the first 9 entries is262143. The next step gives524288=2^19, and six squarings give2^25.

For 335, use 15 gates with

    (1025 repeated10 times, 2, 0 repeated4 times).

The first 10 entries give1048575. The next step gives2097152=2^21, followed by four squarings.

For 334, use 14 gates with

    (2049, 2048 repeated11 times, 0, 0).

After entry 11 the exponent is2^23. The last two steps give2^24 and2^25. Thus the shorter chain also exposes the square and fourth roots of C as exact earlier constants, if a future independently checked transformation can use them.

## Quadratic lift and both maps

The source's only C consumers are rows504 and903:

    u^2+6v^2-2w^2-4C*w-3T^2=0,
    T-2g0*g1-C*q=0,
    q=48*x83^2+48*x87^2+432*x89^2.

Add one coordinate Q with Q=q. Put the last chain coordinate c_last in place of C, and write

    u^2+6v^2-2w^2-4c_last*w-3T^2=0,
    T-2g0*g1-c_last*Q=0.

Both residuals and all chain equations are quadratic. All other source rows and coordinates are unchanged. The input is still coordinate0. New coordinate1000 is Q; the chain occupies1001 through1000+n, for n=16,15,14 respectively. Metadata marks C as a coordinate and every residual term has sPower=0.

From any source319 solution, assign Q its displayed quadratic value and assign the unique chain values. This gives the corresponding ordinary solution. Conversely, induction on the chain forces c_last=C in every ordinary solution. Eliminate the uniquely defined Q and forget the chain to recover exactly the source319 rows and every source coordinate. Thus these are bijective extensions of the source solution set. No arithmetic, nonzero guard, point, prime, local valuation or real approximation argument is changed.

The extra root-sum gate cannot be silently omitted: directly replacing C by a variable in C*x83^2 produces a cubic residual. This packet uses the explicit Q gate rather than making that degree mistake.

## Exact coefficient maxima

Let K be the coefficient of the constant monomial in the frozen source polynomial319.json. Its exact integer is stored in `INHERITED-CONSTANT.json`, together with the source hash; it has 1514 bits. This notation avoids reproducing a long decimal number in the report.

The exact maxima in the table are, respectively,

    3^1026+K, 3^2050+K, 3^4098+K.

They occur in the constant monomial, where the first chain equation contributes3^(2a_0) to the unchanged constant coefficient K. All other coefficients were compared as exact integers in the full expanded tables. In particular the maxima are not merely pure powers of3. Their bit counts are 1627,3250,6496. Every coefficient in all three artifacts is written as an ordinary decimal integer in its polynomial table.

## What the chain lower bound proves

Fix a bit cap B on the expanded polynomial's coefficients. Consider only explicit acyclic monomial constant chains starting from fixed integer powers of3, where each new coordinate is a fixed power-of3 multiplier times a product of at most two earlier coordinates. Outputs are defined linearly, as above; each multiplier exponent has absolute value at most A. Within this model, the largest positive exponent available after n new gates is at most

    A*(2^n-1).

This follows by induction: one gate adds at most A to twice the previous maximum. Multiplying two different earlier coordinates cannot beat that bound. The squared multiplier contributes a nonnegative degree-four coefficient in this isolated constant chain, so the polynomial coefficient cap implies bit_length(3^(2A))<=B. This gives a necessary bound even before the additional inherited constant K is included.

At B=3247, A<=1024. Fifteen gates can reach at most33553408, strictly below2^25=33554432. Thus at least 16 such constant gates are needed, and 336 attains that bound with the one fixed Q lift.

At B=8193, A<=2584. Thirteen gates can reach at most21165544, again below2^25. At least 14 such gates are needed; 334 attains it. The335 artifact explains why increasing the tighter cap by only three bits can remove one gate.

These are lower bounds for the stated constant-chain architecture with the Q lift retained. They do not rule out a different algebraic presentation, shared nonconstant gates, a complete rescaling of other modules, or a different exact encoding of a constant. A universal minimum is not asserted.

## Additional local pass and its boundary

The separately executable `local_census.py` checks every quadratic part of the frozen319 residuals. Every one of its319 coordinates occurs quadratically, so there is no coordinate appearing only linearly in all consumers. After removing anchor rows903 and504, the remaining287 C-free quadratic parts have rank287 over Q. The removed rows have unique quadratic monomials g0*g1 and T^2 respectively, so the full rank is289 for every fixed value of C. Therefore no nontrivial scalar linear combination of these residuals yields an affine relation. This is a bounded zero-gain result, not an ideal-theoretic impossibility claim.

A trial to absorb C into scaled root abscissae avoided the extra Q product in the anchor but introduced negative constant powers in other consumers and nonquadratic products on clearing them. No globally valid scaling was obtained, and no saving from that trial is counted. The existing g0 inverse remains necessary in the proved maps; the earlier exact-valuation guard deletion is still blocked by its recorded completeness-modulus obligation.

Run `python -B build.py`, `python -B verify.py`, and `python -B local_census.py`. The verifier imports no producer, checks all source consumers and chain coefficients, proves the final exponent by integer arithmetic, and independently expands every primitive residual square. Full source319 acceptance and an independent review of this exact ordinary lift remain separate requirements.
