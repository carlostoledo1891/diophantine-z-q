# Exact private-anchor unscaling: 320 to319

Author: `/root/astra_quartic_opt01_elimination`, November 7, 2026. This component has **319 total variables, 318 witnesses, 289 quadratic residuals and 5659 quartic monomials**. The degree is four and integer content is one. Its largest coefficient is `186624*3^(2^26)+64`. Independent review is required. No predecessor, released manuscript or controller was edited.

This is an exact change of private coordinates and elimination of a uniquely defined coordinate. Both maps below are polynomial when expressed using the already retained inverse tau. They introduce no exceptional branch and require no new arithmetic lemma, real choice, prime restriction or height estimate.

## Frozen input and output

| Object | SHA256 |
| --- | --- |
| Accepted320 IR | d1171bc47ed8ec15aac10ca6708208e9de9c2dfa7a973732ede76269a1bee02f |
| Independent320 review | 7bc8fa06ef2483dccc1e26d5c83b6a94c510e27e3718bf0c52effa7693840c15 |
| candidate319-ir.json | 847d21a2d0a45571f043b82289df0da55f4e814167844bdc39fc134e4f4c2676 |
| polynomial319.json | 8320b69d290a37017060e34742fb025cbc1c13e40a5b7d750893e9912d3796ef |

The source folder is `work/quartic-under300-20261107/10-combination/combined320`. Its review is `work/quartic-optimization-20261107/resume-sol-review320-20261107/REVIEW.md`. The input remains the original coordinate0. C=3^(2^25) remains a fixed coefficient, not a quantified variable.

## Literal source block

Set g0=v543, g1=v544, tau=v549 and

    q=48*v83Â²+48*v87Â²+432*v89Â².

The unchanged guard is g0*tau=1. The source's private block is

    Q=q,
    B=2g1+C*Q*tau,
    UÂ²+6VÂ²-2WÂ²-4C*tau*W-3BÂ²=0.

Here Q=v903, B=v904 and U,V,W are55,56,57. Every occurrence of these five coordinates is in rows903,904,504. This exhaustive boundary is checked against the literal source, not inferred from their names.

The replacement has four private coordinates u,v,w,T, stored at55,56,57,903:

    T=2g0*g1+C*q,
    uÂ²+6vÂ²-2wÂ²-4C*w-3TÂ²=0.

Delete coordinate904 and row904; replace rows903 and504; rename the four retained private coordinates. All other coordinate objects and residuals are identical. Both displayed residuals are quadratic in the quantified variables because C is fixed. There is no g1Â² substitution and no changed quaternion parameter.

## Forward and reverse maps

From any source solution define

    u=g0*U, v=g0*V, w=g0*W, T=g0*B.

Keep all nonprivate coordinates, including g0,g1,tau and the input, and forget the old Q. The guard makes T=2g0g1+Cq. Multiplying the old anchor by g0Â² and using g0*tau=1 gives the new anchor.

Conversely, from a new solution define

    Q=q, B=tau*T,
    U=tau*u, V=tau*v, W=tau*w.

Keep every nonprivate coordinate. Then B=2g1+Cq*tau by the new T equation and guard. The old anchor is tauÂ² times the new one. Q has its required value. These maps are mutual inverses on their respective solution sets because g0*tau=1 and Q=q. In particular they preserve the exact input projection and all detector, logarithm, scalar and height data. They do not rely on identifying any root point or proving any parity statement again.

For an explicit polynomial certificate, let RQ,RB,RA be the source rows903,904,504, let NT,NA be the new rows903,504, and let G=g0*tau-1. With pullback by the forward map,

    NT = g0*RB + C*RQ + C*Q*G,
    NA = g0Â²*RA + 4C*g0*W*G.

With pullback by the reverse map,

    RQ=0,
    RB=tau*NT+2g1*G,
    RA=tauÂ²*NA.

The checker verifies all five identities as unconditional sparse polynomial identities. Thus zero-set equivalence follows from the actual guard without an unproved denominator condition.

## Finite verification and coefficients

Run `python -B build.py`, then `python -B verify.py`. The verifier imports no producer. It checks hashes, all changed and unchanged objects, complete private-coordinate consumers, the guard, both map certificates, quadratic degree, active coordinates, and every coefficient of the primitive-integer residual sum of squares.

The table has 5662 coefficient-power entries but 5659 actual monomials after fixing C. The three collisions are the pure fourth powers of slots83,87,89. In particular the coefficient of v89^4 is186624CÂ²+64. All other CÂ² coefficients have smaller absolute leading coefficient, C-linear coefficients have magnitude at most1728, and constant coefficients have fewer than2048 bits. Since C>2^2048, the displayed maximum is exact. A constant coefficient1 remains, so integer content is one. No decimal expansion of C is needed.

An ordinary-coefficient presentation can restore one Q=q gate and use the existing 16-coordinate squaring chain for C. Its equations T=2g0g1+C*Q and the unscaled anchor are quadratic, giving 336 variables by a circuit prescription. No ordinary coefficient table is claimed here.

## Scope and earlier attempts

The pending358 proposal on359 also saves one private anchor coordinate but changes the numerator to g1Â²+Cq. This component instead retains exactly g0B=2g0g1+Cq and works directly on accepted320. The two savings are alternatives and cannot be added. The previously recorded357 attempt imposed a new exact3-adic valuation and had an unresolved completeness modulus; it is not used here.

The initial boundary scan found that the retained inverse tau already permits the forward and reverse unscaling maps. Keeping q as a separate coordinate after unscaling was unnecessary because its coefficient C is fixed. No broad ideal or heavy numerical search was required. The result remains above the below 300 publication threshold and awaits a non-author review of these exact files.
