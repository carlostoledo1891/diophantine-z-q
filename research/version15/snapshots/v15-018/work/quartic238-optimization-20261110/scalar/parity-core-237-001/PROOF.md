# Three-residue scalar core: 237-variable proposal

Status: author proposal, independent review pending. No V14/V15 file is changed.
Parent: accepted raw238 IR 736b5953cdcd8d7fd2d8a35099d825170a71ca6d4461f3cc5e1ebaab07f762c0. The accepted sparse238 is an invertible affine/row presentation of that parent; this proposal starts before those optional sparse transformations.

## Exact changes and meanings

Use parent IDs until renumbering. Let R=x142>0, R2=x139=R², u=x128, v=x129, D1=x135=v², w=x138. The actual formal ratio is Z=R(u+sqrt(2)v), and the actual scalar pole W is w/R². These are exactly the accepted raw238 signed-rescaling meanings. Let H0=x86,H1=x87; f(H)²=H0+2H1 sqrt(2). Thus H0²−8H1²=F² with F=Norm(f(H))!=0.

Delete coordinate137 and its defining row82. Repurpose coordinate136 as C. Replace parent row88 by

    u²−R C=0.

Replace parent row83 by

    C²+R D1+H0²−8H1²−R2 w=0.

All other rows are retained, including D1=v², R2=R², the literal forced-positive normalizer, the scaled W-square and every scalar-pole conic. Renumber coordinates above137 and rows after deleted82. This gives237 coordinates and211 quadratic residuals. The two nonzero original ratio coefficients remain; no coordinate is silently removed through an input specialization.

Equivalently, in unscaled arithmetic variables,

    W = Z0^4/R^10 + Z1²/R^5 + F²/R^4,
    b = R(R+9792) W².

This is a new scalar criterion, not a bijection between old and new scalar witnesses. All non-scalar interfaces retain their accepted meanings. Both defining-equivalence directions are proved below using the same arithmetic premises as the parent.

## Local soundness, including zeros

At a scalar contact prime p>76176 or p=149, put nu=v_p(R)>0 odd. The number9792 is a unit. The inherited pole obstruction, unchanged, applied to the nonzero b gives v_p(W)>−nu/2. Since R>0 over Q, D1=v²>=0 and F²>0, the new numerator C²+RD1+F² is strictly positive, so w,W,b are nonzero; this does not assume a p-adic extraction conclusion.

For an actual finite point H on y²=x³−Dx at good odd unramified p, every finite valuation of f(H)=1/x(H) is even. Indeed when v(x)>0, the unit D makes2v(y)=v(x); when v(x)<0,2v(y)=3v(x); otherwise v(x)=0. Therefore v_p(F) is even: at split primes it is the sum of two even valuations; at inert primes it is twice an even valuation. This also applies before excluding the exceptional H classes; the H chart already provides an actual point with x and f nonzero.

The three numerator terms have valuations

    4v_p(Z0)−6nu,     2v_p(Z1)−nu,     2v_p(F).

The first lies in2+4Z, the second is odd, and the third lies in4Z. They cannot cancel. If Z0 or Z1 vanishes, omit its term (its required lower bound is automatic); the F term never vanishes. Consequently all finite term valuations exceed7nu/2. Hence

    v_p(Z0)>19nu/8,
    v_p(Z1)>9nu/4,
    v_p(F)>7nu/4.

In particular H is formal at some place over p. The unchanged zero/two-torsion translation argument for S and identity[2m]S'=[4a]H yield v_p(a)>=v(Z)>9nu/4. There is no extra assumed divisibility of m. Thus every contact prime contributes exponent at least3 to a.

## Forced prime, height, and uniformity

The scalar normalizer and input polynomial are unchanged, so v149(R)=2N+1 or2N−1 exactly as in the parent. The new F bound excludes the same finite exceptional H classes, whose reciprocal-abscissa norms are149-adic units. This justifies all subsequent ratio/log interpretations in the same order as before. The root chart already ensures a!=0.

Write c=|a| and L'_N=floor(9(2N−1)/4)+1. For positive sufficiently large N,

    149^(L'_N) M5(beta)^3 divides c,
    h(beta)<=C3*149^(-L'_N)*c*(1+log(c)/3).

The base cubic-log height theorem is unchanged. All five-factor comparison tests, both aggregate contacts, the first rationality/Lucas-defect contradiction, and the integral Lucas equation are unchanged. For the final n−beta contradiction, substitute L'_N in the existing upper bound log B<=C'+7C3*149^(-L'_N)c(1+log(c)/3). The same lower bound log B>=(c−4)log(c−1) contradicts it uniformly once N is sufficiently large. Since L'_N increases without bound, one fixed (still ineffective) N0 works for every larger N. Nothing asserts N>=53 is a defining threshold; it is only the separately verified coefficient threshold.

## Integer completeness

For each integer input, choose the same compact real neighborhoods for H and S as in the accepted scalar-S completeness proof. On them Z0,Z1,F are uniformly bounded. Since R>=A_N/(1+149²) tends to infinity uniformly,

    W=O(R^-4),       b=O(R^-6).

Moreover W,b>0, so0<b<17 eventually, uniformly in the input. The same scalar rational R has exactly the same local squareclass R(R+9792), square reduced denominator, and preparation valuations at2,3,17 as before. At the finite support choose H first sufficiently formal, and then a still more divisible, making F and both Z coefficients arbitrarily deep. The three displayed terms defining W can therefore all be made arbitrarily deep despite their fixed R denominators. Make W integral at every odd-valuation numerator prime and sufficiently deep at2,3,17. At other primes b has even valuation because b=R(R+9792) times a square. These are exactly the inherited pole-realization hypotheses.

The same compact-group recurrence meets the real neighborhoods and finite scalar congruences. After fixing S, continuity preserves them for H in a fixed progression. The later contact-prime selection avoids this finite support; its choice order, nonzero Lucas labels, opposite-order conditions and all four U_i,V_i constructions are unchanged. Fill C=u²/R, D1=v² and w=R²W, together with the existing scaled pole auxiliaries. Every changed row holds exactly. R!=0 follows from the unchanged positive normalizer even when the input is zero. Thus every integer still has a rational witness for sufficiently large N.

## Verification scope

The finite checker expands the entire211-row sum of squares, verifies degree4/content1/all237coordinates, and records the exact parameter profile. All209 unchanged parent residuals are transported only by the explicit deletion map. Finite valuation and rational-core tests support the formulas; they are not substitutes for the preceding arithmetic proof. No premise is strengthened, no effective bound for N0 is claimed, and no independent acceptance is claimed by this file.
