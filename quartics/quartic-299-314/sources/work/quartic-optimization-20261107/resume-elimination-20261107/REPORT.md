# Three root parities in the quaternion anchor

Author: `/root/astra_quartic_opt01_elimination`, 2026-11-07. This is a new research reduction requiring independent review. No repository, released manuscript or controller file was changed. The released Version13 baseline remains394 symbolic /411 ordinary variables; this work builds on the separately accepted366 research construction.

The exact candidate has **362 total variables,361 witnesses,332 quadratic residuals and6428 quartic monomials**. Its polynomial has degree4, integer content1 and largest absolute coefficient `16*3^(2^26)`. This is a net saving of four variables from366. It is not yet an accepted result and does not reach the below300 publication threshold.

| Artifact | SHA256 |
| --- | --- |
| Source366 IR | 0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56 |
| Source non-author review03 | 409e919e31b68f8efa7c2ec8cac441c20720b118456988cd7978e74a6e4708e2 |
| candidate362-ir.json | edf0f50212f51da251bedd4b75305ce6fd00902e790487a158760bcbc9f331d3 |
| polynomial362.json | a92e0e84b31cec7dd4c96ae443892aeace1251618f6141a4995e41794d1a8a24 |

SOURCES.json pins the released baseline, guide, coefficient-lemma source, source366 argument and its independent review, and the earlier failed primary-square search. The latter search was not repeated.

## Exact replacement

Keep C=3^(2^25) fixed. The retained scalar data have g=g0+g1*rho, g0*tau=1 and g^2=f(S-P), with rho^2=2. Thus the rho coefficient F_s=f1(S-P) is2g0g1. The old anchor is

    U^2+6V^2-2W^2-4C*tau*W-12g1^2=0.

For each of the three root points A,T,Z introduce u_i=1/f1(i). Introduce two more rational coordinates

    Q=3072(u_A^2+u_T^2)+27648u_Z^2,
    B=2g1+C*Q*tau.

Replace the last term of the anchor by -3B^2. Delete all nine private coordinates of the A,T,Z odd-index charts and their nine defining rows. All other source rows and coordinates remain identical. The new five coordinate IDs are900..904, in the order u_A,u_T,u_Z,Q,B. The deleted coordinates are66,67,68,74,75,76,78,79,80; rows687..689,693..698.

For a root with physical x=x0+2x1*rho,

    f1=-2x1/(x0^2-8x1^2),

so u=1/f1 is imposed by the quadratic equation

    2x1*u+x0^2-8x1^2=0.

A and Z use physical real coordinates82 and88. T uses physical real coordinate2*86, so its literal new row has4*86^2, not86^2. The imaginary slots are83,87,89. Every root chart gives a nonzero field element x; consequently its field norm is nonzero. The new equation therefore also excludes x1=0 and forces the exact inverse. It introduces no denominator-zero branch.

Multiplying the new anchor by g0^2 and using g0*tau=1 gives precisely the old translated quaternion form with numerator g0*B. Its normalized parameter is

    t=(g0*B)/C = F_s/C + Q.                         (1)

This is still the original quaternion form, not a new local-global theorem. The source criterion says it has rational witnesses exactly when t belongs to Z_(2) intersection Z_(3), for every rational t including zero. Its exact input and consumer are restated here because the parameter has changed.

## Local input before height or oddness

The retained square-abscissa charts imply that A,S,T,Z are nonzero integral multiples of P. This uses the source group decomposition and squareclasses only. It does not use any of their private odd charts. The retained g0 inverse excludes S=P; the reciprocal subtraction identity identifies R=S-P, including S=-P through its duplication value. Hence R=[s]P for a nonzero integer s, before a parity inference.

For every nonzero integer n, let F_n be the rho coefficient of f([n]P). Then

    v3(F_n)=0                     if n is odd,
    v3(F_n)=2+2v3(n)              if n is even.        (2)

The odd case follows from the source good reduction calculation: P reduces to the nonzero2-torsion point with x=rho over F9, so f([n]P) reduces to2rho. The even case is exactly `lem:v12-anchor-coefficient`, quartic_v12.tex lines20115ff. In particular F_n is nonzero and its3-adic valuation is even for every nonzero integral index. This uniform statement justifies applying the calculation to s before knowing s is even and to A,T,Z before knowing their indices are odd.

The same source formal-group proof at2 establishes2-integrality of F_n for all nonzero integral n. For odd n we need the more precise statement

    v2(F_n)=5.                                      (3)

Here is its direct proof. The literal starting value is

    z(P)=(232+86rho)/357,

whose rational-component valuations are3 and1. The field valuation normalized by v(2)=1 is3/2. For odd n the integral odd multiplication series is [n]z=nz+O(z^3). The error has field valuation at least9/2; its real coefficient has valuation at least5 and its rho coefficient at least4. Thus the two leading valuations remain3 and1. The rho coefficient of z([n]P)^2 has valuation1+3+1=5. The curve identity f=z^2(1-Df^2) gives f-z^2 field valuation at least9, so it cannot alter that leading coefficient. This proves(3) for positive or negative odd n without a numerical sampling premise.

## Reverse implication and noncancellation

Start with any rational zero of the new system. The new anchor gives t integral at3. By(2), v3(F_s/C) is an even integer, since v3(C)=2^25 is even. Also v3(u_i)=-v3(F_i) is even and nonpositive.

The binary form u_A^2+u_T^2 is anisotropic modulo3, so

    v3(u_A^2+u_T^2)=2*min(v3(u_A),v3(u_T)),

which is a multiple of4. The valuations of the three summands in(1) therefore lie in the three disjoint sets

    2Z,   1+4Z,   3+4Z.

No pair has the same valuation. The least valuation occurs only once, so cancellation cannot raise it. Integrality of t forces each summand to be integral. In particular F_s/C is3-integral. Since a negative even v3(u_i) is at most-2, either 1+2v3(u_i) or3+2v3(u_i) would then be negative. Thus all three v3(u_i) are zero. Equation(2) forces the indices of A,T,Z to be odd.

The2-integrality of F_s/C follows independently from the retained scalar point and the fact that C is a2-unit. Apply the unchanged source quaternion criterion to F_s/C and choose old private anchor witnesses. This restores the old anchor with the same g0,g1,tau, independently of the values of the new private witnesses. None of this argument invokes the root product-height theorem, Lucas conclusion, detector acceptance or either global height contradiction. This avoids the circular approach of deriving missing root parity only after a theorem that already requires it.

It remains to restore the deleted half-abscissa witnesses. If a root is [n]P with n odd, take its half [n]R0, where P=2R0. The same exact doubling/squareclass argument used in the accepted366 sign-restoration proof gives a half-abscissa with norm minus a rational square and with the required root h,j values up to simultaneous sign. The equations being restored are exactly

    a_half^2-2(x+j)*a_half-D=0,
    Norm(a_half)+normRoot^2=0.

The source's three literal physical normalizations are checked in verify.py. A simultaneous root h,j sign change can be extended to the following involutions of every new residual:

| Root | Coordinates multiplied by -1 |
| --- | --- |
| A | 1,2,3,4,21,22,23,24,112,113 |
| T | 9,10,11,12,29,30,31,32,128,129 |
| Z | 13,14,15,16,33,34,35,36,136,137 |

These sets are disjoint. The verifier checks every monomial in every residual, recording whether each row is unchanged or multiplied by-1. Physical root points, their x coordinates, inverse F_i values, the new anchor coordinates and the input are fixed. Perform whichever of these involutions the half-abscissa normalization needs, then add the three half-abscissa/norm witnesses for each root. The result is a full old366 solution with the same input. The old accepted soundness applies only after this restoration.

## Forward implication

Start from a full old366 solution. Its root odd charts make A,T,Z odd multiples; F_i are nonzero by(2). Set u_i=1/F_i. Equation(3) and v2(3072)=v2(27648)=10 show that every term of Q is2-integral. Equation(2) shows that all u_i are3-units, hence Q is3-integral. The old anchor gives F_s/C integral at both2 and3. Therefore t=F_s/C+Q is integral at both places.

Use the unchanged quaternion criterion with parameter t to choose new rational anchor witnesses, divide the unscaled witnesses by nonzero g0, set B=2g1+CQtau, and forget the nine old odd-chart coordinates. This satisfies all new rows. The three original private anchor witnesses may change; they have no other consumers. All nonprivate source coordinates can remain fixed in this direction. Thus both constructions have exactly the same rational input projection, although the reverse direction permits the explicit sign involutions and neither map claims a fiberwise identity on all witness coordinates.

## Verification, ordinary presentation and remaining review

Run `python -B build.py` to reproduce the candidate, polynomial and certificate, then `python -B verify.py`. The latter imports no producer. It checks source pins, exact row/coordinate deletion and all outside consumers, the T scaling, the anchor identities, the three complete sign involutions, the local starting constants, and the full primitive-integer sum of squares. All362 coordinates occur. All332 residuals are quadratic and the full expansion has6428 distinct monomials. The only C^2 terms have coefficients16 and1; every C coefficient is at most96, and every constant coefficient has fewer than2048 bits. Therefore the exact maximum remains16C^2.

An ordinary-coefficient presentation uses the same16-coordinate squaring chain for C and one product tauC=C*tau. It replaces C*tau*W and C*Q*tau by tauC*W and tauC*Q, both quadratic. This gives379 total variables by an exact circuit prescription; no ordinary numerical table is claimed or reviewed in this packet.

The new review obligations are the uniform valuation statement before parity, the changed quaternion parameter, its three-way noncancellation, the odd-index2-adic coefficient calculation, and the global half-chart restoration. The finite checks do not prove these arithmetic statements. The positive365 anchor route changes the same anchor and is not additive with this reduction as written. Pending detector reductions may have disjoint equations, but their composition requires a fresh consumer/sign review. No stronger group, prime-pattern, height or analytic assumption has been added.

The earlier one-root inverse-linear proposal and the primary-square degree obstruction remain preserved in their original folders. A four-root packing was considered initially, but accepted366 has only three retained odd charts, so the actual gain is four variables. No broad ideal search or unbounded worker was run.
