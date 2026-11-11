# Reciprocal auxiliary points with half-integral free indices

Author: agent05, 2026-11-07. This is a conditional arithmetic extension and two proposed quadratic ratio equations. It is not independent acceptance of an implementation. There is no frozen new IR, no certified coordinate saving, and no claim that the proposed addition equation is sufficient. The addition obstruction below is unresolved in this packet.

## Sources and exact scope

The baseline is `resume-anchor-shared314-20261107/anchor-gamma313/candidate313-ir.json`, SHA256 `6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a`.

The published source is `work/quartic-version6-release/repository/manuscripts/quartic_v13.tex`, SHA256 `9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd`. Relevant passages are lines 19539-19564, squareclasses and the group decomposition; 20830-20900, rational logarithms, identity units and ratio transfer; 20924-20934, the sign of the shared primary parameter; 21054-21156, the enlarged H domain, exceptional points, global approximant nonvanishing and integral group identities. The shared314 source proof is `resume-depth-20261107/shared314/PROOF.md`, SHA256 `a8b3adc8ed7103aea1fc65cff5654632534fe151ec5ba157ad4413f79cceb4eb`; its pre-H residue classes and H bootstrap are consumed here. The earlier three-group proof is `resume-depth-20261107/three326/REPORT.md`, SHA256 `766427b1e75cf10823b0119b9d3a415a8460b49cbebb31c1b2b8483502f3baf8`.

Use K=Q(rho), rho^2=2, d=3-rho, D=d^2, E:y^2=x^3-Dx. The published group calculation gives E(K)=Z R0 plus E[2](K), P=2R0, and 2E(K)=Z P. All four roots Q_i=n_i P and their odd, nonzero integer labels remain as in the accepted system. H and V0=H-P retain their accepted charts and global exclusions. Only U_i and V_i=U_i-Q_i, i=1,...,4, are enlarged from 2E(K) to E(K).

This last group-law equality is a REQUIRED INPUT, not a consequence of the proposed single addition equation. Roots are not enlarged by this proposal. Their squareclass witnesses and root-height conclusions may not be silently discarded.

## Raw reciprocal point and zero-safe ratios

For one auxiliary point introduce f,h,Y satisfying

    Y=f^2,       h^2=f-D*f*Y.

If f is nonzero this gives the exact E-point (x,y)=(1/f,-h/f^2). If f=0, the equation forces h=0 and we interpret the point as O. Thus this affine chart covers E(K) except the point (0,0). The other two nonzero 2-torsion points are present, at f=+/-1/d and h=0. No square root of f is assumed.

The raw equation h*z=f is unsafe at O: it leaves z arbitrary. Likewise h*L+f*S=0 leaves L arbitrary there. The shared parameter in the published convention is S=-1/z(H). Replace these equations by

    (1-D*Y)*z = h,
    (1-D*Y)*L + h*S = 0.

Each is quadratic in the stored coordinates. At O their coefficient is 1, so z=0 or L=0, respectively. Away from O and the two finite 2-torsion points, h^2=f(1-DY) gives z=f/h=h/(1-DY), and hence L=-S*z=z/z(H). At finite 2-torsion both equations degenerate. They must not be divided there; those branches are excluded by the local low tests before ratios are used, as proved below.

For comparison with the old square chart, put f=r^2, h=-J*r and Y=r^4, where J^2+D*r^4=1. The new point equation is r^2 times this old conic. Its primary residual has the exact identity

    (1-D*r^4)*L-J*r*S
      = J*(J*L-r*S) - (J^2+D*r^4-1)*L.

Its alternate residual has the identity

    (1-D*r^4)*z+J*r
      = J*(J*z+r) - (J^2+D*r^4-1)*z.

These provide the forward map for every old witness, including either identity sign J=+/-1. The reverse map does not in general recover r in K. This is an arithmetic domain extension, not equality of private witness projections.

## Valuation periods before logarithms

Let q be any consumed place above p>76176. It is unramified, has integer-valued valuation and D is a unit. For a nonzero f the associated E-point gives the following exhaustive cases.

* If v(x)<0, then v(x^2-D)=2v(x), so 2v(y)=3v(x). Hence v(x) is even and v(f) is positive even.
* If v(x)>0, then v(x^2-D)=0, so 2v(y)=v(x). Again v(x) and v(f) are even.
* If v(x)=0, v(f)=0.

At O the leaf is zero and is omitted from the unique-minimum argument. Thus the published periods for f^2, f^4 and f^8 remain valid BEFORE assuming formality, an integral L, a deep H or any index congruence. This argument also applies to conjugated alternate points at the opposite place. All other group leaves are arbitrary fourth powers, whose periods never required point squareclasses.

Consequently the accepted shared314 residue proof still gives its same common successful place, its positive low f bounds and its bounds on the comparison leaves, provided the stored caches really are the powers stated above. A positive v(f) means v(x)<0 and hence reduction to O. The two finite 2-torsion points have v(f)=0 at every consumed place and cannot survive a low test. The point (0,0) is absent from the chart. Thus every auxiliary point needed in the local argument is either O or a non-torsion formal point. In particular 1-DY is a local unit there, and the zero-safe ratio equations give the exact ratios.

The successful-place argument does not require a new prime to exist: the retained root-height/anchor contradiction handles the all-empty-radical branch, exactly as before. It depends only on the retained roots, scalar anchor and H/V0 tests, not on an auxiliary square root. No L or logarithm is used to get that contradiction. H and V0 retain their pre-ratio exclusions.

## Integral identities and half-integral labels

Write H=m R0+T_H and U_i=k_i R0+T_i, where m,k_i are integers and T_H,T_i are 2-torsion. Let h0=m/2 and u_i=k_i/2 denote rational free indices only. Then

    V0=(m-2)R0+T_H,
    V_i=(k_i-2n_i)R0+T_i.

The identities that kill BOTH torsion terms are

    [2m]U_i=[2k_i]H,
    [2(m-2)]V_i=[2(k_i-2n_i)]V0.

Using the source's smaller coefficients without this extra factor 2 would be unjustified for general T_i. All points to which a logarithm is now applied are formal at the relevant place. The logarithm is a homomorphism there. The existing exclusions give m nonzero and m-2 nonzero, and the formal logarithms of H and V0 are nonzero. Taking logarithms gives the SAME full ratios u_i/h0 and (u_i-n_i)/(h0-1). The extra factor 2 cancels exactly. Zero indices cause no division by zero: a formal torsion point is O, and its logarithm and z are zero. The source analytic unit A(O)=1 supplies the unit-ratio formulas.

Both u_i and h0 are p-integral because their denominators divide 2. At least one of h0 and h0-1 is a p-unit. At the primary and conjugated alternate places, the source unit ratios therefore give an integral full ratio on one side. The positive-order cross-test transfers integrality to both approximate ratios, hence to both full ratios. This uses depth-one units, not yet a deep H.

The shared314 H bootstrap is unchanged: L2,L3,L4 are integral; F(L2,L3,L4) is positive-order and F(0,0,0)=-1, so one L_i is a unit. Its exact z(U_i)=L_i*z(H) and its depth-at-least-10 primary point force H depth at least10. The primary error is then at least40, the alternate V1 error at least12, and the other alternate errors at least40. Identity values have exact zero error. Multiplication by h0 and h0-1 and subtraction gives precisely the old congruences to the INTEGER ROOT LABELS n_i. The proof never needs u_i integral over Z; local integrality at odd p suffices. The root height and Lucas steps still receive exactly their previous integer labels, scales and exponents.

## Denominators, real conditions and completeness

The rational approximant's numerator N and denominator Q are globally nonzero on K by the published no-root certificates modulo71 and modulo7. This matters because general E(K) points need not have 0<=Df^2<=1 at both real embeddings. No positivity interval is substituted for the global certificate. The V1 polynomial G2 has no variable denominator, and is a local unit at the successful formal place. The unchanged V0 chart and its globally nonzero ell0 supply all alternate denominators. The new raw point-ratio coefficient 1-DY is used only after its local unit property is proved. At that point it is also a nonzero element of K.

Completeness uses the old U_i,V_i in 2E(K), not arbitrary new cosets. The explicit substitution f=r^2,h=-Jr,Y=r^4 above provides every new auxiliary coordinate and both new ratio equations. The old choice of H, contact primes, real neighborhoods and all finite congruences is unchanged. Thus no new simultaneous approximation assertion, no additional H-index congruence, and no new real positivity requirement is needed. All raw values remain bounded on the same chosen neighborhoods. This establishes completeness ONLY if the eventual new addition equations hold identically for these exact point pairs and do not remove either identity branch.

## Actual obstruction in the current addition proposal

The proposed equation for c=x(Q_i) is

    c*(Y+Yalt-2Z)=(f+F)*(1-DZ)+2*h*k,
    Z=f*F.

It cannot be used as the required group-law input. On F=f and k=-h, both sides vanish for EVERY c. This includes genuine opposite non-torsion points. A concrete example is U=R0=(1+rho,2rho), V=-R0. Its f=rho-1 has norm -1, so f is not a square in K. Its h=8-6rho, F=f and k=-h satisfy both raw curves. The true difference is P, with c=(57-28rho)/8, but the displayed equation also permits c=1 and every other value. Hence this is not merely a forbidden torsion case, and neither the enlarged-domain argument nor the ratio repair fixes it.

The supplementary relation c*((f+F)*(1-DZ)-2hk)=(1+DZ)^2 determines the correct doubled abscissa on this branch, but it is cubic in the proposed stored coordinates. This packet neither counts it as quadratic nor adds an uncounted product witness. A separately verified oriented addition chart is still required, including O and the opposite-point branch.

The potential saving is therefore unconfirmed. This proposal removes one arithmetic obstacle to dropping the auxiliary square witnesses; it does not authorize dropping root squareclasses, replacing the addition graph by its biquadratic closure, or claiming a 305/297-variable candidate.
