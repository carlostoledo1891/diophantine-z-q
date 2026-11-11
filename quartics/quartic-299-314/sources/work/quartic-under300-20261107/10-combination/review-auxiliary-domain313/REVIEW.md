# Independent review of the auxiliary E(K) domain extension

I accept agent05's conditional arithmetic extension from doubled auxiliary points to arbitrary E(K) auxiliary points, under the exact point, ratio and oriented-addition interfaces stated below. No new hypothesis or repair to that arithmetic argument was needed. This is not acceptance of a307-variable artifact: none is included in this review.

Reviewer: `/root/astra_quartic_opt10_combination`. Arithmetic author: agent05. I contributed the zero-safe ratio repair separately and checked the parent's slope closure. Those algebraic contributions are disclosed and are not represented here as independently approved by their author. The new arithmetic under review is agent05's preservation of valuation periods, torsion-killing group identities, local logarithm transfer, H-depth recovery and completeness under the enlarged auxiliary domain. A complete candidate still needs a non-author check of its actual algebraic interfaces and finite construction.

## Pins and required interface

The reviewed proposal is `work/quartic-optimization-20261107/resume-auxiliary-domain-20261107/PROPOSAL.md`, SHA256 `b4641d8f2d6c50824956de216ff7055e31b9c9ab79249d41ee5567300a3ee750`. The accepted source313 IR is `6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a`. The Version13 mathematical source is `work/quartic-version6-release/repository/manuscripts/quartic_v13.tex`, SHA256 `9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd`. I read the cited group-decomposition, formal-logarithm and enlarged-H passages, as well as the accepted shared314 argument that313 inherits.

The conditional inputs are substantive:

- Every new pair satisfies Y=f^2 and h^2=f-DfY and represents (1/f,-h/f^2) when f is nonzero, or O when f=h=0.
- The primary and alternate ratios have the stated zero-safe meanings after torsion exclusions. Their physical signs and conjugations must match the source.
- Q_i=U_i-V_i is a genuine oriented group-law equality. An abscissa equation with an uncontrolled opposite-point branch is insufficient.
- Every root Q_i retains its old integer label n_i, oddness, nonvanishing and squareclass/height conditions. In particular the scalar root S must be the same oriented root used by its scalar anchor.
- H,V0=H-P, the scalar subsystem, the detector leaf powers and the shared gamma/anchor conditions retain their separately accepted meanings.

The parent slope closure provides a proposed way to establish the addition input, but the current arithmetic proposal explicitly does not prove its original biquadratic sufficient. I preserve that distinction.

## Valuation periods do not require doubled points

At an unramified consumed place p>76176, D is a unit and valuations are integers. For any nonzero raw f, the curve relation is h^2=f(1-Df^2). If v(f)>0, the second factor is a unit, so v(f)=2v(h) is even. If v(f)<0, the leading cubic term has valuation3v(f), so3v(f)=2v(h) and v(f) is again even. If v(f)=0 there is no parity issue. This proves the same result directly as the proposal's x-coordinate cases.

Consequently f^2, f^4 and f^8 have valuations in4Z,8Z and16Z respectively, without first assuming a square root of f in K or formal reduction. A zero f is the identity and its zero leaf is omitted. Conjugation moves the same assertion to the other place. The non-point high and middle leaves remain literal fourth powers. Hence the accepted residue-class separation and common-place argument are valid before logarithms, provided the compiler preserves these exact powers.

The resulting positive f valuation gives formal reduction to O. Finite nonzero two-torsion has f=+/-1/d, a unit at these primes, and is excluded by that positive bound. The original point (0,0) is absent from this reciprocal affine chart. Thus the zero-safe denominators1-DY are local units before they are used. Their being local units also proves they are nonzero elements of K. Identity points have coefficient1 and the correct zero ratio.

Existence of a required consumed prime, when needed, still comes from the independent root-height/anchor contradiction. That proof must be applied after restoring the roots, and before any H/auxiliary ratio interpretation. It is unchanged by removing auxiliary square roots. The fixed H and V0 exceptional-point exclusions likewise precede this logarithm step.

## Torsion and half-integral indices

The retained group calculation gives E(K)=Z R0+E[2](K), with P=2R0. Write H=mR0+T_H and U_i=k_iR0+T_i, where m,k_i are integers. Since Q_i=n_iP, V_i=(k_i-2n_i)R0+T_i and V0=(m-2)R0+T_H.

The identities required for arbitrary T_i are

    [2m]U_i=[2k_i]H,
    [2(m-2)]V_i=[2(k_i-2n_i)]V0.

Both free coefficients agree, and each torsion coefficient is even. The extra factor2 is essential; the smaller doubled-point identities cannot simply be reused. At the relevant places all points to which logarithms are applied have already been proved formal. The logarithm is a homomorphism there, and H,V0 are nontorsion with nonzero logarithms by the existing exclusions. Cancelling the common factor2 therefore gives the full ratios

    (k_i/2)/(m/2),   (k_i/2-n_i)/(m/2-1).

The rational free indices are not notation for half-integer multiplication of curve points. Their denominators divide2, so they are integral at every consumed odd prime. If a free numerator is zero, a formal two-torsion point is O; the zero-safe analytic unit convention applies. No quotient log(O)/z(O) is used.

Put h0=m/2 and u_i=k_i/2. Since h0 and h0-1 differ by1, one is a local unit. On that side the corresponding full ratio is integral. The depth-one analytic units identify its valuation with the approximate ratio; the positive cross-test then transfers integrality to the other approximate ratio and its full ratio. At opposite split places the rational full indices are unchanged; only the accepted conjugation of the analytic unit changes. Thus this step does not incorrectly combine unrelated places.

## Depth recovery and the integer root labels

After integrality, the same H bootstrap applies. F(L2,L3,L4) has positive valuation while F(0,0,0)=-1, so at least one of the three integral Li is a unit. Its exact z(U_i)=Li*z(H) relation makes it nonidentity and transfers the previously obtained primary depth at least10 to H. Other nonidentity primary points then have at least the same depth; identity errors are exactly zero.

At depth10 the primary approximation has relative precision40. The alternate V1 approximation has precision12, and the other alternate rational approximations have precision40. Integral ratios turn these into the absolute errors needed by the old order10 and order40 cross-tests. Multiplying by the integral h0 and h0-1 and subtracting yields L_i congruent to n_i at the required order. It does not yield or require global integrality of u_i. The integers used in the height and Lucas arguments remain precisely the unchanged root labels n_i.

The scalar transfer involves H and its existing scalar point, not the new auxiliary cosets. The existing integral-index scalar argument and depth24 remain valid. There is no newly required precision80 assumption.

## Global denominators and completeness

General auxiliary points can leave the real interval on which the old positivity proof for the rational approximant was convenient. The stronger global nonvanishing certificate is therefore necessary. I independently re-evaluated the exact N coefficients modulo71 and Q coefficients modulo7: both have no residue root, their leading coefficients are units and all denominators are units. Both primes split in K. A nonintegral local root is impossible by leading-term dominance; an integral one would reduce to a forbidden residue root. Thus neither polynomial has a K-root. This supplies the global rational-approximant definitions without an unproved real bound. The G2 polynomial has no variable denominator and is a local unit at a formal successful place; no claim of its global positivity is needed.

Completeness can use the same doubled auxiliary points as before. Given their old r,J with J^2+Dr^4=1, the values f=r^2,h=-Jr,Y=r^4 are exact raw coordinates, including r=0 and either identity sign J. The analogous construction applies to the alternate point. The proposed ratio identities then recover the old ratios without any new choice of H or a new local approximation constraint. A complete new addition chart must contain these actual point pairs, including its legitimate tangent and identity specializations; that remains a finite/algebraic implementation obligation.

The old roots, contact primes, finite neighborhoods, real bounds and final H progression are unchanged. No attempt is made to realize every newly allowed torsion coset or half-index by completeness.

## Scope of acceptance

The conditional arithmetic extension is sound. It does not approve the original single biquadratic addition equation, the deletion of a root squareclass, or an unoriented replacement of the scalar root. `check.py` and `CHECKS.json` supply independent finite source checks, not a substitute for the preceding unbounded reasoning. A final replacement candidate requires exact source/target pins, all actual consumer maps, the group-law closure, complete polynomial checks and an appropriately independent review of the contributors' algebra. No coordinate count or publication is approved here.
