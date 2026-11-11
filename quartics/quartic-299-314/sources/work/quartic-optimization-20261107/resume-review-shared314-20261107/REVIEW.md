# Independent arithmetic review of shared314

I accept the source-level arithmetic argument in the frozen shared314 proof, relative to the existing arithmetic inputs and the exact displayed circuit interface. The H bootstrap is noncircular and supplies the precision needed by the downstream comparisons. This is a fresh review, not an extension of the earlier reciprocal-variant acceptance. Full compiler transport, all changed consumers, the variable count and the complete sum-of-squares table require the separately assigned structural review.

Reviewer: `/root/astra_quartic_opt05_anchor`, November 7, 2026. Arithmetic author: `/root/astra_quartic_opt03_depth`; circuit author: `/root/astra_quartic_opt01_elimination`. I authored neither proposal. No mathematical repair or strengthened hypothesis was supplied by this review.

## Frozen scope

The reviewed proof is `work/quartic-optimization-20261107/resume-depth-20261107/shared314/PROOF.md`, SHA256 `a8b3adc8ed7103aea1fc65cff5654632534fe151ec5ba157ad4413f79cceb4eb`.

The intended source is accepted combined315, IR `d450a34735fe84bab0900abb3931740d4f7cedb1004ede7a81e1a09c4249f8b8`. The emitted compiler candidate, read for limited interface bindings, is `resume-elimination-20261107/shared-scale314/candidate314-ir.json`, SHA256 `7805ee1ebd5fec7ac20b2b5590afe9b5891c85aff8eee5f58b104a888bb9e6f5`. Its report is `ea67fce0404236d1e5d7b9018536a040d07d75591cd83c5c4ca84385523a3f3e`.

`SOURCE-PINS.json` binds the source and candidate, the arithmetic proof, the accepted three326 and combined315 arguments, the previous common-scale review and erratum, and the Version 13 source. The original 156-power construction remains rejected. This review does not erase that adverse evidence or approve a later change to the guard, common scale, grouping or H bootstrap.

## Nonzero common parameter and physical inputs

Gamma is a rational parameter distinct from the fixed anchor coefficient C=3^(2^25). The literal new rows 2000 through 2007 force the successive powers gamma², gamma⁴, gamma⁸, gamma¹⁶, the inverse J=gamma^-16, gamma⁴⁰, gamma⁸⁰ and gamma¹⁶⁰. In particular gamma¹⁶ J=1 excludes gamma=0 before any arithmetic argument. Every nonzero rational gamma has exactly one tuple of these helpers. No choice of a square-root sign occurs.

The promoted P1 test is exactly the square of the physical field value P1=f(U1)²=(v255,2v256). Rows 2008 and 2009 give its ordinary coefficients

    v1109=v255²+8v256²,  v1110=4v255v256.

This is f(U1)^4, including the zero value when U1=O. It is not a square of each rational component separately. The independent checker verifies these literal rows. It also verifies that anchor rows 504 and 1903 and guard 732 remain identical to combined315.

All preexisting R values must retain their exact source normalization as F5(A_j lambda), with E_j R_j=1. The high and middle leaf values, the signed pre-H H0² value, and all conjugated alternate leaves retain their old meanings. The new private outputs divide the stated field powers by nonzero rational gamma powers; they are not replacement definitions of the underlying point or logarithm values. The structural review must bind all these requirements to the remaining emitted rows.

## Local classes before H has its meaning

At a prime in a required contact radical, let alpha=v_p(R_j)>0 be odd and c=v_p(gamma) be any integer. No valuation assumption is made about the other two R values. At every place above this prime, the existing pre-H Kummer argument and primary curve identities give the leaf periods used below. For the exceptional squared-H branches the H0² value is zero or a fixed unit, so it causes no unproved valuation class.

Normalize residues modulo 16 by the inverse of alpha. The complete nonconstant classes in source term order are:

| Group | Classes |
|---|---|
| G0 | 1 mod4; 2 mod4; 3 mod4; 4 mod8; guard 8 mod16 |
| G1 | 1 mod4; 2 mod4; 3 mod8; 4 mod8; 7 mod8; 8 mod16 |
| G2 | 1 mod4; 2 mod4; 3 mod8; 8 mod16; 12 mod16; 15 mod16 |

Every gamma exponent is divisible by the corresponding leaf period. The guard valuation 16c-8alpha is in class 8 modulo 16. Each row's classes are disjoint and avoid zero, independently of c. The independent finite check covers all 256 displayed alpha/c residue combinations. The unbounded assertion follows because every expression factors through these residue classes. Omitting a zero leaf preserves disjointness.

Thus every group is nonzero at a consumed place, has valuation at most zero and has a unique minimal term. With W=G0G1G2, the unchanged norm equation recovers the trace T=Tr(1/W). Let ell be the maximum valuation of W over places above p. Trace integrality gives v_p(T)>=-ell. Since 1+R_j is a unit and the pole excludes negative odd valuations,

    0 < v_p(B)=alpha-2v_p(T) <= alpha+2ell.

Hence ell>-alpha/2. At a place attaining ell, every group valuation is at least ell because the other group valuations are nonpositive. Every term of every group is therefore above -alpha/2 at this **one place**. This includes the rational guard and every test. The inert-prime case uses the same argument with one place.

The guard yields c>15alpha/32. It is not necessary to assume c positive beforehand, assume other R values integral, or combine conclusions from different successful places.

## Depths supplied by the new groups

For alpha=1, the guard forces c>=1. For alpha=3 it forces c>=2. For odd alpha>=5, substitute c>15alpha/32 directly into the strict inequalities.

The worst right-hand sides in the inequalities for four times the valuation are:

| Test | alpha=1 | alpha=3 | strict bound for alpha>=5 |
|---|---:|---:|---:|
| each high H1 through H4 | 157.5 | 312.5 | 72.5alpha |
| each middle M0,M1 | 37.5 | 72.5 | 16.25alpha |
| f(U2) | 156.5 | 309.5 | 71.5alpha |
| f(U3) | 76.5 | 149.5 | 34alpha |
| f(U4) | 83.5 | 170.5 | 41alpha |

The alpha>=5 bounds already exceed the alpha=1 bounds. Integer valuation gives high depth at least 40 and middle depth at least 10. The primary reciprocal values have even valuation, giving respective lower bounds 40,20,22 for f(U2),f(U3),f(U4). Zero values satisfy every bound and mean identity points in the primary chart.

All remaining low tests imply positive reciprocal valuation. In particular, E H0² gives positive valuation of H0 once the generic branch is reconstructed; E P1² gives positive valuation of f(U1); and the unchanged or weakened alternate E powers give positive valuation of each conjugated alternate reciprocal. These are genuine formal points. Since v(f(Q))=2v(z(Q)) for a nonidentity formal point, each of U2,U3,U4 has formal depth at least 10, or is O. This conclusion precedes the bootstrap and requires no H depth assumption.

## Excluding the domains before using ratios

The two newly admitted squared-H branches are excluded exactly by their fixed-unit tests. T0 still has coefficient E^8, and its fixed-unit value contradicts the common-place bound at any required contact. If all three radicals were empty, the retained root-height and independent anchor contradiction applies. Thus the generic H reconstruction is valid before interpreting L or any logarithm denominator.

The further finite H-domain exceptions in E[2] and the translates of E[2] by P or -P have unit f(H) at every consumed prime. The new **positive** f(H) conclusion already contradicts this. Their old exclusion does not require the full numerical order 40; its proof uses only nonunit versus unit. If no required prime existed the same independent height contradiction would apply. Consequently H and H-P are nontorsion, h and h-1 are nonzero, and the retained no-root/subtraction arguments give the actual denominators. This step does not use the H-depth bootstrap.

The root parity and root half-chart restoration still precede this H interpretation. They use the unchanged root/scalar/anchor subsystem. The new group and scaled-output rows must respect the A,T,Z restoration actions; that full literal check belongs to the structural review. Gamma itself stays fixed by those actions.

## The H bootstrap

The Version 13 source around lines 20885 through 20900 supplies a zero-safe analytic unit A(Q) with log_E(Q)=z(Q)A(Q) and A(O)=1. For initial formality, depth one suffices for this unit statement. It does not require the source's later depth-20 conclusion. The G2 and rational-approximant quotients by A are likewise analytic units, equal to one at O.

The retained integral group identities give full ratios r_i=u_i/h and r'_i=(u_i-n_i)/(h-1), with the same half-index convention for h. The only possible denominator in the free index is 2, a unit at these primes. Thus h and h-1 are integral and differ by one; one is a unit. For every i at least one full ratio is integral. Approximate and full ratios have equal valuations because they differ by analytic units, also when a numerator is zero. The positive-order cross-test forces the other approximate ratio integral, hence both full ratios are integral. No high H depth has been used.

In particular L2,L3,L4 are integral. The retained physical polynomial is

    F(A,T,B)=T²-A(A-2)TB+(A-2)²B²-1.

Every nonconstant monomial contains the inputs, while F(0,0,0)=-1. If all three Li lay in the maximal ideal, F(L2,L3,L4) would reduce to -1. This contradicts its positive valuation from the high test. Therefore one of L2,L3,L4 is a unit. This argument uses only F(L) modulo p, not F on the integer labels or the later height conclusion.

For that index, the retained exact primary identity is z(Ui)=Li z(H). H is already a nonidentity formal point, so z(H) is nonzero. A unit Li makes Ui nonidentity and gives v(z(H))=v(z(Ui))>=10. This is why the three independently deep primary points are sufficient even though the unit index is not predetermined. Integrality of every other Li then gives the same depth for each nonidentity primary Ui. Identity points have zero error.

At depth 10 the primary analytic correction has relative precision at least 40. This is weaker than the old source's surplus precision 80, so one must redo this step rather than quote a lemma whose hypotheses explicitly require H depth 20. Precision 40 is nevertheless exactly sufficient: the alternate rational quotients at indices 2,3,4 have relative precision 40, the index-1 G2 quotient has precision 12, and integral full ratios turn all these relative bounds into absolute bounds. Combining with the cross-tests gives precision 40 for the three high label comparisons and precision 10 for the first/middle comparison.

Multiplication by the integral indices h and h-1 followed by subtraction yields the same congruences L_i=n_i modulo the required powers. Polynomial substitution then gives the original order-40 Lucas condition on the integer labels; the middle test gives its original order-10 input-label condition. The unchanged height and Lucas contradictions apply. The scalar depth24 argument uses its existing point/domain and integral-index identities; it does not consume the old excess primary precision 80. No downstream error estimate needs more than the newly proved 40 in soundness.

## Completeness and the common-scale choice

Completeness keeps the original Pi19 progression and the same points. Thus H and every nonidentity primary Ui still have formal depth at least 20 in the chosen complete witnesses; the weaker soundness bootstrap does not weaken these choices. The source gives high test valuations at least 40, M0 at least 12 and M1 at least 80. At a selected contact, alpha=c=1. In the exact source term order the new nonconstant margins are

    G0: 1,2,79,4,8;
    G1: 1,2,3,76,159,8;
    G2: 9,282,83,8,12,15.

They are all positive. Zero leaves only improve this conclusion. The promoted P1 term has margin 159. Hence every group is one modulo the successful place. At the opposite place the same disjoint-class argument gives each group inverse residue zero or one. The trace is therefore a unit with residue one or two, exactly as required by the pole construction.

Choose gamma/lambda in (1,2), with valuation zero at 2,3,17 and at the common zero contact, and valuation one at other selected contacts. This is the same elementary CRT choice proved in the preceding common-scale review. A denominator congruent to one modulo the finite square-prime moduli and a numerator in a sufficiently long positive interval give all exact valuations simultaneously. Repeated contacts impose one condition, not a sum of multiplicities. No new condition is imposed on H's index.

Let nu_p=-v_p(lambda), eta_j=v_p(A_j). The true source formula gives v_p(E_j)=5(nu_p-eta_j) for sufficiently large preparatory divisibility. With v_p(gamma)=-nu_p the eight coefficient valuations have pairs of coefficients of (nu_p,eta_j)

    (155,5), (150,10), (145,15), (35,5),
    (30,10), (65,15), (100,-20), (24,-40).

Every slope in nu_p is positive. The fixed finite neighborhoods already bound all old tests, and also bound the new square P1². Therefore the original freely chosen divisibility makes all nonconstant terms tend to zero, uniformly in the unit parts of gamma/lambda. It gives the same trace limit 2, squareclasses and preparation thresholds at 2,3,17.

At real embeddings the coefficient decay exponents are -155,-150,-145,-35,-30,-65,-100,-24, uniformly for gamma/lambda in (1,2). All coefficients are positive for sufficiently large positive lambda, and all leaves are even powers. The groups and trace are positive at both embeddings, and B is defined, positive and asymptotic to 1/(4R_j). The same compact real neighborhoods give 0<B<17 for all three detectors.

The order is essential: fix roots, scales, finite neighborhoods and compact real bounds; enlarge the preparatory denominator divisibility and choose the real lower bound; select the contact primes using the original input; choose gamma by CRT; finally choose H in its original compatible Pi19/continuity progression and real neighborhood. All estimates were uniform in the later gamma choice. The same H satisfies the scalar and point conditions. No separate local or real H is substituted.

The global pole formula remains B=R_j/[T²(1+R_j)²]. Its valuation parity is that of R_j, independently of primes newly introduced by gamma. Off the detector's selected contacts v_p(R_j) is even; at its contacts the trace and 1+R_j are units and v_p(B)=1. Thus the reduced denominator remains a square. All inherited prime-pattern, source-edition and restricted-converse qualifications remain unchanged.

## Checks and final boundary

The independent `check.py` imports no author program. It checks 256 residue cases, the exact unbounded threshold coefficients and integer rounding, the Lucas constant term, all completeness margins, the finite and real growth coefficients, and the limited literal gamma/P1/anchor bindings listed in `CHECKS.json`. It pins the actual compiler candidate rather than treating the proposed count as an artifact identifier.

No arithmetic gap was found in the frozen proof. The decisive new step is the depth-one integrality argument followed by the unit primary ratio and depth-10 H bootstrap. It replaces the old high-H test's role in soundness without assuming the conclusion it is meant to establish. The separate structural review must still establish the entire literal interface, restoration actions, counts and complete finite polynomial. This report alone does not approve publication or a 314-variable quartic artifact.
