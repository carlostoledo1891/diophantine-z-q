# Independent review of the common-scale arithmetic

I do not accept the original 156-power guarded construction. Its claimed disjoint residue classes fail. I accept the arithmetic interface in the separately frozen reciprocal variant, relative to the retained 323/326 source assumptions and with the nonzero rational common parameter and all displayed equations imposed exactly. This is a source-level arithmetic conclusion. No common-scale candidate IR, variable reduction, quadratic compilation, sum-of-squares table or later composition is accepted here.

Reviewer: `/root/astra_quartic_opt05_anchor`, November 7, 2026. Arithmetic author: `/root/astra_quartic_opt03_depth`. The reciprocal circuit idea is credited in the author note to `/root/astra_quartic_opt01_elimination`. I authored neither proposal. The original residue defect was discovered and reported by author03 while this review was underway. I confirmed it independently. The author preserved the original report and withdrew its validity claim in a separate erratum. No reviewer-supplied strengthening of the hypotheses is used below.

## Exact scope

The original `common-scale/REPORT.md` is SHA256 `973c42e11e86abed56a5a732757c5d79cb0251e87df174c152c7b6eeff70000b`. The independently considered `RECIPROCAL-VARIANT.md` is `e233eaaa7f45f44411731719f8b9412d8f38c448e9a6ca5d7e10a2a7320874c1`. Paths are under `work/quartic-optimization-20261107/resume-depth-20261107`.

The source 323 IR is `dc804a0f236f81c29753c5f3496254641df0fa527dd522923f4dfa331e8d2ecd`. The unchanged arithmetic source is the reviewed three326 packet. `SOURCE-PINS.json` binds these files, their independent reviews, the original contact372 argument, the erratum, and the source manuscripts. The new H-bootstrap proposal in the same author directory is outside this review.

I write **gamma** for the new common nonzero rational parameter. This avoids confusing it with the fixed anchor coefficient C=3^(2^25). The elliptic constant D=(3-sqrt(2))², the auxiliary inverse 1/gamma and the denominator used in the prime-pattern construction are also distinct objects. The fixed anchor coefficient and all point, logarithm, scalar and height data stay unchanged.

## The original defect

In G2, P2²=f(U2)^4 has valuation in 8Z, not merely a generic fourth-power class. The original replacement gamma^-156 E P2² has valuation

    4c-alpha mod8,

where c=v_p(gamma) and alpha=v_p(R) is positive odd. The unchanged E P4² term has class -alpha mod8. If c is even, these classes coincide. In particular, alpha=1 and c=2 are allowed by the guard. Taking v(f(U2))=78 and v(f(U4))=0 makes both terms have valuation -1, while the guard itself has valuation 20. The proposed unique-minimum proof cannot be applied.

This disproves the claimed residue separation, not the integer projection of a compiled system. No full rational counterexample is asserted. It would be an additional restriction to require c odd, and the original equations do not do so. The erratum correctly preserves this distinction.

The unguarded-product obstruction is separate and remains valid. My checker independently replays [2377]P modulo 76249 cubed using a separate projective addition implementation. It verifies the curve equation, a unit X and exactly one factor of p in Z, the opposite nonzero finite reduction, and the reported reduction group order 76064. Thus the two abscissa valuations are -2 and 0. Four equal odd root points yield the stated scale valuations 0,-16,-32 and R valuations 1,-75,-155 for lambda=p. This is an obstruction in the actual root/scale domain, not a full-system witness. It supplies no missing hypothesis about other R values in raw soundness.

## All reciprocal residue classes

The reciprocal variant replaces high coefficients by gamma^-160 R² and gamma^-160 R³, middle coefficients by gamma^-40 R, and the H0² coefficient by gamma^-80 R. The guard is gamma^16 E^12. Every low coefficient is unchanged.

At a consumed unramified place, the source pre-H argument gives exactly the leaf valuation classes used in three326. The H0² leaf is in 4Z on the generic branch, zero on one exceptional branch, and a fixed unit on the other. This statement does not use a later H-index interpretation. The P2²,P3²,P4² classes are in 8Z, and the alternate eighth-power leaves are in 16Z. These finer classes must be retained.

Normalize residues modulo 16 by multiplying by the inverse of odd alpha. For arbitrary integer c, including zero and negative c, the nonconstant term classes are:

| Group | Classes in source term order |
|---|---|
| G0 | 2 mod4; 3 mod4; 1 mod4; 8 mod16; 12 mod16; guard 4 mod16 |
| G1 | 2 mod4; 1 mod4; 8 mod16; 4 mod8; 3 mod4 |
| G2 | 2 mod4; 1 mod4; 8 mod16; 3 mod8; 4 mod8; 7 mod8 |

Within each row these sets are disjoint and avoid zero, the constant term's class. Together with the constant they partition the 16 residues. The exponent 160 is divisible by 8, so the P2² class is independent of c. `check.py` independently constructs the sets for all eight odd alpha residues and all sixteen c residues. All 128 cases pass for all groups; the original c=2,alpha=1 collision is retained as an explicit negative control.

Zero leaves remove a term and do not invalidate the partition. Hence every group is nonzero at every consumed place, with valuation at most zero and a unique minimal term. This remains true before deducing anything from the guard.

## Same-place guard and raw soundness

Fix detector j and a prime in its required positive odd contact radical. Use only alpha=v_p(R_j)>0 odd. No condition on R_k for another detector is needed or inferred.

Write W=G0 G1 G2 and let ell be the maximum of v_q(W) over the places q above p. The retained norm row, together with W nonzero in K, forces both its rational real component and the auxiliary z to be nonzero. It then gives T=Tr(1/W)=1/z. Since each term of this trace has valuation at least -ell, v_p(T)>=-ell. The unchanged pole equation gives

    v_p(B)=alpha-2v_p(T) <= alpha+2ell,

because 1+R_j is a unit. This valuation is odd. The retained pole obstruction forbids negative odd valuation, so ell>-alpha/2.

Choose one place attaining ell. Every group valuation is nonpositive, and their sum is ell. Each group valuation is therefore at least ell. Each individual term has valuation at least its group's unique minimum. Consequently **all terms, including the guard, lie above -alpha/2 at this same place**. Inert primes cause no change; then there is only one place.

The rational guard has valuation 16c-12alpha at that place, hence c>23alpha/32. For alpha=1, integrality of c gives c>=1. The high, Lucas/high, middle and H0 inequalities respectively become

    4v(high) > 160c - (5/2)alpha,
    4v(high) > 160c - (7/2)alpha,
    4v(middle) > 40c - (3/2)alpha,
    2v(H0) > 80c - (3/2)alpha.

At alpha=1 the lower bounds are 157.5,156.5,38.5,78.5. They force orders 40,40,10,40; for H0, use its source even-valuation fact. The P2² term has the second coefficient and forces f(U2) depth at least 40. For odd alpha>=3, substitution of the strict guard inequality gives lower bounds 112.5alpha,111.5alpha,27.25alpha,56alpha. Even at alpha=3 these exceed the preceding thresholds, so no larger-alpha case is lost.

The unchanged low terms receive the same -alpha/2 bound as in three326. In particular, a fixed-unit T0 exceptional leaf is still impossible at a required contact prime. If there are no required primes at any of the three scales, the retained pre-H root-height and anchor contradiction applies. Thus the H reconstruction, later logarithm denominators, integrality-transfer and scalar24 arguments get their source hypotheses in the original order. A radical-free detector is not assigned an unsupported global trace inverse.

## Literal source conventions

The review checker reads the actual 323 equations, rather than treating the names F or q as mathematical definitions. It independently composes the quadratic F-square, F-middle and F-output rows with each retained E equation. In all three cases the extracted affine R is exactly

    F5(t)=t(t+1/2)(t+1)(t-1/2399)(t+32/407).

The three physical t values in the stored coordinates are v37, 4v391 and v37+32v439. In particular, the factor four in detector1 and the affine combination in detector2 cannot be omitted. The source t and scale rows give A0=1, A1=4v343 and A2=1+32v344+256v345=(1+16v342²)². These are the actual positive square scales; their small-prime valuations include all fixed powers of two. The affine R coefficients and source row IDs are recorded in `CHECKS.json`.

This is a check of the source interface. A future common-scale IR must still bind its new coefficient gates and guard to these exact R values, preserve the true primary and alternate cached powers, and prove the existence of the nonzero rational gamma used here. Formal power names alone will not suffice.

## CRT choice and denominator support

For completeness retain the source's lambda=u/v, with v=D0²w² a rational square and u the common zero-contact prime. The five forms within each detector are distinct; repeated forms across detectors retain their incidences. Selected primes avoid the fixed scale and contact denominators and differences. At every consumed contact v_p(R_j)=1. Each selected prime has v_p(lambda)=1 if it is the common zero contact, and zero otherwise.

Choose q=gamma/lambda after these primes are fixed, prescribing v_p(q)=0 at the zero contact, v_p(q)=1 at other selected contacts, and v_p(q)=0 at 2,3,17. Then v_p(gamma)=1 at every selected contact and v_p(gamma)=v_p(lambda)=-nu_p at the three small primes. Repeated incidences do not add valuations to gamma.

Here is an elementary construction showing that q can also lie in (1,2). Take pairwise coprime square prime-power moduli and prescribe numerator residue 1 for valuation zero or p for valuation one. Let M be their product, choose a positive denominator N congruent to 1 modulo M with N>M, and take a representative of the numerator CRT class strictly between N and N+M. It lies below 2N. The denominator is a unit at every prescribed prime, so cancellation cannot alter those exact valuations. This argument works for any finite selected set and adds no congruence on the point index h. The checker supplies a rational fixture with two distinct verified primes greater than 76176 and the three small primes.

New primes in q's numerator or denominator are allowed. They do not create a new odd-denominator obligation: globally in the complete witnesses,

    B=R_j/[T²(1+R_j)²],

so v_p(B) is congruent to v_p(R_j) modulo two wherever the expressions are defined. The prime-pattern construction and positive square A_j show R_j is a product of its five selected primes times a rational square. Therefore v_p(R_j) is even off that detector's selected contacts. At a selected contact T and 1+R_j are units, giving v_p(B)=1. This proves square reduced denominator, regardless of the extra primes introduced by q. It does not assert this special support for arbitrary soundness witnesses.

## Finite and real choice order

The roots, true scales and finite continuity neighborhoods are fixed before choosing contact primes. Let eta_j=v_p(A_j); the source bounds every relevant test valuation below throughout the fixed progression for H. Choose the preparatory denominator divisibility nu_p large enough that F5's leading term dominates at p=2,3,17. Thus v_p(R_j)=5(eta_j-nu_p).

With v_p(gamma)=-nu_p, the four changed coefficient valuations and guard valuation are

    150nu_p+10eta_j,
    145nu_p+15eta_j,
    35nu_p+5eta_j,
    75nu_p+5eta_j,
    44nu_p-60eta_j.

Every slope in nu_p is positive. The fixed negative test bounds can therefore be absorbed before prime selection. This is uniform over all unit parts of q, so choosing q later does not invalidate the estimates. All groups tend to 1 and T tends to 2 with any needed small-prime precision. The unchanged pole then has the old preparation thresholds and the squareclass of R_j. The latter is unchanged by the common parameter, because its remaining factors are rational squares. No independent local point choice is made after fixing the final progression.

For the real estimates, use the retained compact neighborhood of the same H in the real orbit component, avoiding the finite comparison pole sets. All tests are bounded there before prime selection. For q in (1,2), gamma=q lambda, and the changed coefficients have uniform decay powers -150,-145,-35,-75 and -44 as lambda tends to positive infinity. R_j is then positive. Every coefficient and every even-power real leaf is nonnegative, so each group is at least 1 at both real embeddings. Hence W is positive at both embeddings and T=Tr(1/W)>0 globally. Also 1+R_j>0. The pole is defined and tends to zero through positive values, eventually lying in (0,17) simultaneously for the three detectors.

Choose these real bounds and the finite divisibility first. Apply the existing prime-pattern and separation input next. Choose q by the preceding CRT construction after the primes are known. Finally choose H in the original compatible Pi19/continuity progression and the previously fixed real neighborhood. The source real-progression argument uses both residue and modulus divisible by the component-group order; the common parameter adds no new restriction to that progression. Primary formal depth 20, actual G2 precision 12 and the retained higher precisions still supply the three326 positive margins. At each selected contact gamma has valuation 1, so the changed coefficients have exactly their old valuations and the guard has valuation 4. At the opposite place each group inverse again has residue zero or one. Thus T has residue one or two and is a unit. The retained normalized pole construction supplies the required witnesses.

The same H realizes the finite, real, scalar and point conditions. There is no swap to separately chosen local or real points in this argument. All literature, prime-pattern and restricted-converse qualifications of the accepted source remain in force.

## Decision and verification limits

The original guarded construction is rejected as proved. The reciprocal variant has a valid source-level replacement argument with the stipulated equations and nonzero gamma. Its added CRT choice is elementary and its estimate changes introduce no stronger point, prime-pattern or height premise. This acceptance does not extend to the new H-bootstrap proposal or an optimization which drops or changes the guard, low weights, nonzero domain or literal source leaves.

The independent checker verifies the residue classes and negative control, exact threshold coefficients, small-prime and real exponent arithmetic, all three source R normalizations, an explicit CRT fixture and the bounded actual-point obstruction. It imports no author program and writes only this review's files. During checker development a proposed CRT fixture modulus 76273 was found composite; it was replaced by the verified prime 76253 and explicit primality checks were added. This was a reviewer test-fixture correction, not a defect in the source CRT argument.

No common-scale IR or complete coefficient table was supplied for this scope. A later implementation needs a separate non-author review of exact gates, all outside consumers, zero branches, counts and full finite expansion. The original direct 336 upper count is neither a saving nor an accepted replacement. All author files and prior accepted candidates are unchanged.
