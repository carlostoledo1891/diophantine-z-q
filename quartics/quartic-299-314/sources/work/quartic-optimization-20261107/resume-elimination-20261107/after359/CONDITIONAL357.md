# Conditional guard deletion after the unscaled anchor

Status: **not accepted and not counted as a reduction**. Author: `/root/astra_quartic_opt01_elimination`. This note records a valid local calculation and an unresolved global completeness obligation. No candidate polynomial is asserted to define the integers.

Let L=2^24, C=3^(2L), and X_A,X_T,X_Z be the physical imaginary abscissa coefficients from accepted359. Starting from opt10's proposed358 construction, one might delete the inverse of g0 and introduce only

    Q=4(X_A²+X_T²)+36X_Z²,
    T=g1²-C+3C*Q,

where Q is an expression, not a coordinate. Use the old unscaled quaternion form with constant 3C and numerator T. Its normalized parameter is

    t=T/(3C)=(g1²-C)/(3C)+Q.

This is quadratic with fixed C. At3, if k=v3(g1)<L, the first summand has negative odd valuation 2(k-L)-1. If k>L or g1=0, it has valuation -1. If k=L, it is integral because the square of a3-adic unit is1 modulo3. The root terms have valuations in0+4Z and2+4Z. Consequently the quaternion condition forces k=L exactly and all root indices odd. It excludes g1=0 before identifying the scalar difference, so the retained reciprocal chart then excludes S=P and gives the actual nonzero scalar point. The even-index coefficient lemma implies g0 is nonzero and restores its inverse and the old scalar anchor. At2, the same abscissa bounds as359 make Q integral, and the proposed358 scalar-domain argument makes g1 integral. The local calculation itself has no identified defect.

The problem is completeness. The requirement k=L means the scalar index must satisfy v3(s)=L-1 exactly. In the actual preparation construction, after choosing H0, the scalar index s must also be divisible by a finite-depth modulus N0. This modulus includes entry into formal subgroups at every prime dividing cr, not just the primes2,3,17. At a prime p other than3 this can require divisibility by the order of P modulo p, whose3-part contributes to v3(N0). The inspected argument supplies no bound v3(N0)<=L-1 uniformly over the unbounded integer input. Fixed values of v3(r) and v3(c) do not bound these cross-prime reduction-order factors.

There is also an uninspected3-part in the real component index m0 used by the simultaneous progression lemma. One cannot assert that s congruent to3^(L-1) modulo3^L is compatible with the full modulus merely because the local depth required at3 is small. A new proof controlling these factors, or a different preparation construction that avoids them, is needed. This note does not claim a counterexample to every possible completeness construction; it identifies the missing implication in this one.

The unscaled358 proposal keeps only a lower bound on v3(s) and therefore does not have this obstruction. No frozen359 or proposed358 author file was modified.
