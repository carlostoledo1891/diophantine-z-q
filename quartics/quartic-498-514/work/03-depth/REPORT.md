# A 519-variable mixed-depth candidate

This construction has 519 total rational variables, including the input, 488 quadratic residuals, and a quartic sum of squares with 24,986 monomials. The fixed coefficient is still S = 3^(2^26). Its largest absolute coefficient is 64 S^2. It saves four variables against the 523-variable baseline.

The algebraic certificates and complete sum of squares have passed the independent existing checker, with only its fixed-parameter metadata changed from the historical exponent 27 to the current exponent 26. The arithmetic argument below has not received an independent review. It uses exactly the inherited arithmetic inputs identified in the current manuscript, with their existing qualifications. This is a research candidate, not a release or an independent acceptance of the manuscript's main arithmetic theorem.

## Change to the source

Retain the Version 9 asymmetric construction, including all primary parameters z(U_i), the order-40 test on f(H), all point domains and guards, the scalar block, the three height scales, and the anchor. Change only the alternate logarithm belonging to the input label and the two associated orders.

Write k_1 = 12 and k_2 = k_3 = k_4 = 40. Define

    L_i  = z(U_i)/z(H),
    L'_1 = conjugate(ell_12(V_1)/ell_40(V_0)),
    L'_i = conjugate(ell_40(V_i)/ell_40(V_0)), i = 2,3,4.

Thus ell_12(V_1) = z(V_1) G_2(D f(V_1)^2). The other four alternate logarithms still use G_9. The test groups are:

| Order | Tests | Number |
| --- | --- | ---: |
| 1 | f(U_1),...,f(U_4), conjugate(f(V_0)),...,conjugate(f(V_4)) | 9 |
| 12 | L_1-L'_1, L_1-beta | 2 |
| 40 | f(H), L_2-L'_2, L_3-L'_3, L_4-L'_4, Lucas residual | 5 |

Here beta = 2X^2+3 and the Lucas residual is the same polynomial in L_2,L_3,L_4 as in the baseline. Every quantified variable remains rational. No integer-witness restriction is added.

## Soundness of the changed local application

At a consumed unramified place above p > 76176, use v(p)=1. All order-one tests give formal membership. The order-40 test on f(H) gives r_H = v(z(H)) >= 20. The exact full logarithm ratios are

    r_i = u_i/h,       r'_i = (u_i-n_i)/(h-1).

At least one of h,h-1 is a p-adic unit, so at least one of these two ratios is integral. The normalized formal logarithm has the same valuation as z. Both G_2 and G_9 are units at the consumed formal points. Therefore the approximate ratios have the same respective valuations as the exact ratios, before any depth conclusion for U_i is used. Since the cross-test has positive order k_i, it transfers integrality to both approximate ratios and hence to both exact ratios.

Now L_i integral implies v(z(U_i)) >= r_H >= 20. The primary relative error is at least 80, by log_E(Q)/z(Q) in 1+p^(4r_Q) O. The alternate relative error is at least k_i: the numerator has precision 12 or 40, and the common denominator has precision 40. Integrality changes these relative error bounds into absolute error bounds. Consequently

    L_i = r_i = r'_i mod p^(k_i).

The last equality incorporates the order-k_i cross-test. Multiplication by h and h-1 and subtraction give

    L_i = n_i mod p^(k_i).

This works unchanged at inert places, where conjugation preserves the sole local valuation. The resulting integer Lucas residual has order 40. The numerator of n-beta has order 12. These are precisely the two orders consumed by the existing Version 9 height contradictions; the stronger baseline order-40 beta tests were not needed downstream.

The changed logarithm introduces no global zero denominator. The only denominator logarithm remains ell_40(V_0). The manuscript's dyadic G_J nonvanishing argument also covers G_2, even though numerator nonvanishing is not needed for that quotient guard.

## Explicit height inequalities

Keep H < 2^2093966, c = |a-1|, and log_2 c > 25165823.5. The existing scalar and anchor arguments give

    h(beta) <= H c^(19/32),
    c > (80H)^10,
    |a| >= c/2 > (40H)^10,
    h(beta) < |a|/40,
    log(40H) < |a|/40.

The comparison 10(7+2093966) < 25165823.5 verifies the displayed anchor margin without expanding S.

For B = max(|n|,|a|,|t|,|b|), B > 4, the unchanged polynomial F satisfies |F| < 5B^4. If F is nonzero, order 40 and the product-height estimate give

    B^(1/10) < 7H 5^(19/40)+6 < 24H.

This contradicts B >= |a| > (40H)^10. Therefore F=0. The unchanged nonzero condition on b permits the Lucas lemma and yields log B > |a|-3.

If n-beta is nonzero, its reduced numerator N satisfies |N| <= 2 exp(h(beta)) B. The order-12 conclusion proved above gives

    B^(5/12) < 40H exp((19/12)h(beta)),
    log B < (12/5)log(40H)+(19/5)h(beta)
          < (31/200)|a| < |a|-3.

This contradiction gives n=beta, so beta is an integer. Writing X=u/v in lowest terms, beta integral implies v^2 divides 2 and hence v=1. Thus every rational solution projects to an integer input.

## Completeness

For an integer X, use the exact Version 9 construction of the odd root labels, scalar index, Lucas witnesses, fixed scales and continuity modulus L. All are chosen before the contact primes. The new G_2 numerator is a polynomial function of the same point coordinates, so the continuity argument still applies. No change to the denominator guards or the exceptional-point avoidance is required.

Choose the primes by the same separation lemma and choose h satisfying

    h = 0 mod Pi^19 M_-,
    h = 1 mod M_+,
    h = h_0 mod L.

The same coprimalities give compatibility. Set U_i=[h n_i]P and V_i=[(h-1)n_i]P. At the primary places H and U_i have depth at least 20, so L_i equals n_i to order at least 80. At the alternate places the three G_9/G_9 ratios equal their labels to order 40, while the mixed G_2/G_9 ratio for i=1 equals n_1 to order 12. Since n_1=beta, both order-12 tests hold. All three other cross-tests and the Lucas residual hold to order 40. All remaining order-one, scalar and anchor conditions are unchanged.

The pole-realization argument already handles these fixed positive orders. Its real decay remains lambda^-3 and its small-prime estimate is 3nu+(10m-8)eta-2c. In particular m=12 needs no new analytic input. This constructs a rational solution for every integer input.

## Application contract and source comparison

The revised application consumes the manuscript's reciprocal-logarithm lemma at e=12 for V_1, and e=40 for V_0 and V_2,V_3,V_4. Its required input is a nonidentity formal point at an unramified place with p > 76176 and v(p)=1. The retained tests and point-domain guards give exactly those objects. The full logarithm is the same normalized log_E with z=-x/y and coefficient recurrence a_0=1, a_1=-2/5, a_j=(4j-5)a_(j-1)/(4j+1). The numerator/denominator maps are explicitly displayed above; the consumed objects are the actual L_i and L'_i, not related substitute ratios.

The source lemma is stated for split primes in `lem:quartic-reciprocal-log`. The proof of `lem:v5-unramified-log` extends its factorial-tail argument to unramified places, including inert places. Although that latter statement lists 16,52,64, the proof with m=ceil(e/4) applies verbatim at 12 and 40; this is the same extension already used by Version 9. For e=12, m=3 and the tail starts at j=3; for e=40, m=10 and it starts at j=10. These substitutions do not change the coefficient ring, valuation normalization or logarithm identity.

Historical justification is present in the actual Version 9 local-depth and soundness arguments, not merely in an audit verdict. The revised mixed-order route is new and requires fresh independent acceptance before any release. The existing arithmetic-source qualifications remain in force. No shared manuscript, audit register or acceptance record was edited.

Relevant current-manuscript labels are `lem:quartic-reciprocal-log`, `lem:quartic-reciprocal-nonzero`, `lem:v5-unramified-log`, `v9:eq:height-transfer`, `subsec:v9-soundness`, `subsec:v9-local-depth`, and `subsec:v9-deep-completeness`. The Version 9 addition and the archived `ASYMMETRIC_LOGARITHMS.md` were also read. Exact source hashes are in `SOURCES.json`.

## Compiler and certificates

`experiment.py` modifies the frozen asymmetric builder using exact single-occurrence replacements. The order-12 group has degree two. Its evaluation uses q^2 plus two component outputs; the order-40 group now has degree five and uses split 3. The order-one group keeps its degree-nine split-5 evaluation. The existing weight chain already computes q_12 and q_40, so restoring the smaller test group needs no additional weight coordinates.

| Compiled block | Baseline | Candidate | Change |
| --- | ---: | ---: | ---: |
| Parameters and logarithms | 106 | 100 | -6 |
| Tests and shared coefficients | 99 | 89 | -10 |
| Three detector blocks together | 129 | 141 | +12 |
| Total | 532 | 528 | -4 |

There are 536 raw coordinates. `finish.py` transports the first five existing final elimination identities by exact coordinate and row names and checks every resulting identity. It then regenerates four shears of shared evaluation coefficients, two for each of the order-one and order-forty groups. A subsequent exact pivot substitution removes one coordinate per shear. The result has 519 coordinates and 488 quadratic residuals.

Forward algebraic maps apply the inverse shears and forget pivot coordinates. Reverse maps process operations backwards, reinserting each pivot's polynomial value and undoing the corresponding shear. The pivot coefficients are nonzero rational constants. No division by a variable or additional rational-domain restriction occurs. Clearing rational scalar denominators and taking the sum of squares preserves the rational zero set in both directions.

`verify.py` imports no producer. It runs the existing JavaScript checker on the raw source and first compilation, independently replays every final certificate operation, and calls the independent existing sum-of-squares checker on the full final table. It also checks the exact relation between the candidate residuals and their normalized final residuals. All 519 coordinates occur. Degree is exactly four and primitive content is one.

The copied compiler and checker differ from their frozen originals only by replacing the historical fixed-parameter metadata `3^(2^27)` with `3^(2^26)`. `verify.py` checks this equality for both files. There is no expansion of S. All S-independent coefficients have at most 1520 bits; the largest coefficient of S is 768 and the sole coefficient of S^2 is 64, with no lower-S term on that monomial. Thus the largest actual absolute coefficient is exactly 64 S^2.

Reproduce with the working Python executable:

    python -B finish.py
    python -B verify.py

The final coefficient table is `beta12/final/polynomial/polynomial.json`. Its SHA-256 is `d29a7cb7ba2f43ea4930b4e370be040fb25993854c875eaaebca3e524d22fe78`. The final report is `beta12/final/VERIFICATION.json` and the reversible elimination certificate is `beta12/final/modulo-certificate.json`.

## Limits of further depth reduction

For the current product-height input, a uniform Lucas precision k gives B^(2-76/k) bounded in terms of H when F is nonzero. This needs k>38. Replacing G_9 by G_8 gives only precision 36 at depth one, so it cannot support this contradiction. Its first omitted coefficient a_9 is a p-adic unit at every consumed p, so there is no uniform extra divisibility to recover the missing orders. Precision 39 still needs G_9 and gives an exponent 2/39, which does not close with the present fixed anchor bound alone. This is a limitation of that direct inequality argument, not an impossibility theorem for other constructions.

Making both primary and alternate points uniformly deep would require incompatible divisibility of h and h-1 by p. No such assumption is used here. The improvement is obtained by restoring the precision actually needed for the input label, while retaining asymmetric depth for every primary point.
