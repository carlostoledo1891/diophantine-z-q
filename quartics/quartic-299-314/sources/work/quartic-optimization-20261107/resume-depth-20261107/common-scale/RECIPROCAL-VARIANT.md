# Arithmetic for the 40,80,160 common-power variant

Author: `/root/astra_quartic_opt03_depth`, November 7, 2026. The circuit proposal was supplied by agent01. This note proves its changed arithmetic interface; it is not an independent acceptance or a claim of variable saving. The original `REPORT.md`, SHA `973c42e11e86abed56a5a732757c5d79cb0251e87df174c152c7b6eeff70000b`, is preserved.

Keep the323 source, three groups, all low tests, all pole equations and the additional guard C^16 E_j^12 in G0. Write D0=1/C. Instead of the earlier common high weights use

    E_j^158 -> D0^160 R_j^2,
    E_j^157 -> D0^160 R_j^3,
    E_j^39  -> D0^40 R_j,
    E_j^79  -> D0^80 R_j.

The first two replacements multiply fourth powers, and their exponents160 are divisible by4. The middle replacement exponent40 and H0 exponent80 are also divisible by4. Their R_j exponents2,3,1,1 have exactly the old residue classes modulo4, since158,157,39,79 have negatives2,3,1,1 modulo4. The additional guard still has class4 modulo16. Thus all disjoint-class and trace arguments in the original report apply before knowing c=v_p(C).

At a consumed prime alpha=v_p(R_j)>0 is odd. The guard forces c>23alpha/32. At the common place each test term lies above-alpha/2. Consequently the four kinds of new weights give

    4v(high) > 160c-2.5alpha,
    4v(high) > 160c-3.5alpha,
    4v(middle) > 40c-1.5alpha,
    2v(H0) > 80c-1.5alpha.

If alpha=1, integrality gives c>=1, and the right sides are at least157.5,156.5,38.5,78.5. These give exactly the required orders40,40,10,40. For odd alpha>=3, substituting c>23alpha/32 gives the respective strict lower bounds112.5alpha,111.5alpha,27.25alpha,56alpha, each larger than the corresponding alpha=1 bound. P2 receives the same sufficient stronger primary depth. All low tests are unchanged, so the pre-H fixed-unit exclusions and restored arithmetic arguments follow as before. No bound on the other two R values is used.

At selected completeness primes choose c=1. Each R_j that is consumed there has alpha=1, giving exactly the old effective exponents158,157,39,79. All the326 positive margins therefore remain valid, and the guard has margin4. Repeated contacts between detector scales cause no problem: C has valuation1 at the prime, not the sum of the multiplicities of the contact forms.

The real and small-prime choices must change from C in(1,2). Instead choose

    1 < C/lambda < 2,
    v_p(C)=v_p(lambda)=-nu_p at p=2,3,17,
    v_p(C)=1 at every selected contact prime.

This is possible after prime selection. All selected primes are units for the fixed scales, and lambda has valuation1 at the common zero contact and0 at a nonzero contact. Thus C/lambda is required to have valuation0 or1 there, and valuation0 at2,3,17. The same elementary CRT numerator/denominator construction puts this rational ratio in(1,2) while satisfying all those local conditions. No new small-prime preparation of the point H is required.

For the finite estimates put eta_j=v_p(A_j), so e_j=v_p(E_j)=5(nu_p-eta_j). With v_p(C)=-nu_p the new coefficient valuations are exactly

    v(D0^160 R_j^2)=150nu_p+10eta_j,
    v(D0^160 R_j^3)=145nu_p+15eta_j,
    v(D0^40 R_j)=35nu_p+5eta_j,
    v(D0^80 R_j)=75nu_p+5eta_j,
    v(C^16 E_j^12)=44nu_p-60eta_j.

All tend to positive infinity with the old freely prescribed preparatory divisibility; eta_j and the test-value lower bounds were fixed first. They therefore give the same limits W->1 and T->2, the same local squareclasses and the same pole thresholds. A general interval proposal k=-v(C)>max(e_j)/80 would have been insufficient for the D0^40 R_j term, which needs40k-e_j>0. The explicit choice k=nu_p above avoids that error and supplies uniform growing margins.

At the real embeddings R_j is asymptotic to A_j^5 lambda^5. Uniformly for C/lambda in(1,2), the four new coefficient types decay respectively as lambda^-150,lambda^-145,lambda^-35,lambda^-75. The guard decays as lambda^-44. All unchanged low weights also decay. They are positive, and the field leaves remain even powers, so the groups and trace are defined and positive. The unchanged B is asymptotic to1/(4R_j) and eventually lies in(0,17). These estimates are uniform over the prescribed ratio interval and fixed test neighborhoods, so they are established before prime selection. Choosing C afterward, then the final H in the original CRT/real progression, preserves them.

Primes introduced by the rational numerator or denominator of C outside the selected set do not create new odd-denominator obligations when v(R_j) is even: the unchanged pole formula has v(B)=v(R_j)-2v(T)-2v(1+R_j). Its parity is still that of R_j. This support argument does not assume arbitrary witnesses have the special completeness support.

Agent01 owns the joint circuit count and any resulting implementation. No gain is inferred from this arithmetic note alone. The required common outputs are D0^40,D0^80,D0^160,C^16. Any quadratic implementation must account for the combined local/common coefficient products, rather than writing cubic residuals implicitly.
