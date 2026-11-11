# Independent review of the single-coefficient anchor

I accept the anchor transformation in `05-anchor/REPORT.md` and its actual use in the frozen 505-variable candidate, conditional on the inherited curve, index and source statements in Version 11. I found no mathematical error in the new local argument, quaternion-witness application, or affine translation. This review is independent of the author of `05-anchor`; I authored the separate mixed-depth proposal, not the anchor proposal.

This is internal model review of the anchor component. It is not acceptance of the other combined transformations, a new proof of the inherited global arithmetic theorem, or a public-release authorization.

## Frozen objects

| Object | SHA-256 |
| --- | --- |
| `05-anchor/REPORT.md` | `35241c9c15690b79f8340bd600ef83e59424252bcab3d18d3ba7cd5ae2ccbe38` |
| `05-anchor/candidate522-smallcoeff-ir.json` | `26d400464120ebfce388b4b2fff5388c36312ffcacc1fab83bd319208a2b53f5` |
| `10-combination/candidate505-ir.json` | `bd9aca7a4a31476e426660d1a33de33552f2a5019bec06104b45938d59f4b966` |
| `10-combination/polynomial505.json` | `a935109cf0617bc9b2cb12abc147251e039fdb739bde1f6369d3320175edcfcd` |
| `manuscripts/quartic_v11.tex` | `1210d2e6f409e502fc9c95afc248fac16a9df48c760a396143780c20ec80b662` |

I read the actual Version 11 local calculation at `subsec:o8-anchor-subgroup`, the proof of `lem:v5-three-witness-anchor`, the Version 9 shifted-scalar and odd-index construction, and the source and consuming residuals. I did not infer the new claim from an earlier PASS label.

For primary-source checks, I read Silverman's integral formal-group construction and multiplication maps, second edition, Chapter IV Sections 1 and 2, especially Example IV.2.2.3, Example IV.2.2.4 and Proposition IV.2.3(a), printed pages 119–122. The pinned PDF hash is `72ee67bfa1e3fdf582ac7e4b032d7ca0b35a168ed6443ac39c121fbb788cab25`. I also directly inspected [Voight's published 2021 Chapter 14](https://link.springer.com/content/pdf/10.1007/978-3-030-56694-4_14.pdf), Proposition 14.6.7 and the split-algebra qualification 14.6.8, printed page 232. No byte pin of the web-delivered published chapter is claimed.

## The local identity covers every required index

The literal field is K=Q(rho), rho^2=2. At 3 it is unramified quadratic, the residue field is F9, and v(3)=1. The coefficient basis 1,rho remains linearly independent after reduction. In particular, v(a+b rho)=min(v3(a),v3(b)) for rational a,b.

The curve and point are exactly

    E: y^2=x^3-(11-6rho)x,
    P=(57/8-(7/2)rho, -165/8+(417/32)rho).

The discriminant is a 3-unit and the reduction of P is (rho,0), a nonzero point of order two. The tangent doubling formula independently gives

    z(2P)=(3396356159088-4135204317756rho)/3287811625151,
    z=-x/y,
    z(2P)/3 = 2+rho mod 3.

The new argument needs more than the inherited equality v(z(2P))=1. Its specific residue is correct, and (2+rho)^2=rho in F9.

The formal-group coefficients lie in the local integer ring because the displayed Weierstrass equation is integral. Its inverse is exactly -z: on this short equation negation changes (x,y) to (x,-y). Multiplication commutes with negation, so its series is odd. The primary-source linear-term statement therefore gives

    [m](z)=mz+O(z^3)

with integral coefficients for every integer m, including negative m. This is stronger than merely asserting an analytic error term with an unspecified denominator.

For v(z)=r>=1, multiplication by 3 has linear term of valuation r+1, while its remaining terms have valuation at least 3r. After division by 3^(r+1), the error has valuation at least 2r-1>=1. Thus the depth rises by exactly one and the leading residue is unchanged. For a 3-unit integer u, division by 3^r leaves leading residue multiplied by u mod 3, and the error has valuation at least 2r>=2.

Now write any nonzero even n uniquely as n=2*3^k*u, with k>=0 and 3 not dividing u. Apply the preceding multiplication statements to 2P. They prove, without a finite-index or sign restriction,

    z(nP)/3^(k+1) = u(2+rho) mod 3.

The case 3 divides n is exactly the repeated multiplication-by-3 step. Negative n are covered by negative u, or directly by z(-Q)=-z(Q). There is no missing case among nonzero even indices.

The curve identity f=z^2(1-Df^2), D=11-6rho and f=1/x, has second factor congruent to 1 on the formal branch. Since u^2=1 in F3, it follows that

    f(nP)/3^(2k+2) = rho mod 3.

Consequently the two rational coefficients satisfy

    v3(f1)=2+2v3(n),
    v3(f0)>=3+2v3(n).

The second inequality allows f0=0 with valuation infinity. The first proves f1 is nonzero. The assertion is not intended for n=0, where the finite reciprocal coordinate is not the same chart object. That case is excluded in the application: a is odd by the retained odd-coset chart, and the retained scalar subtraction guard excludes a=1. Therefore R=S-P=[a-1]P has a nonzero even index. The stronger guard also excludes a=-1; this causes no defect in the asserted implication on actual source solutions.

## Equivalence to the original semilocal condition

At 2 the inherited integral formal-group calculation places every integral multiple of P in the formal subgroup. The formula

    v(a+b rho)=min(v2(a),v2(b)+1/2)

then makes both rational coefficients of f(nP) 2-integral. This step does not require good reduction or a minimal equation at 2. C=3^(2^25) is a 2-unit.

At 3, the proved inequality v3(f0)>v3(f1) means f1/C is integral if and only if both coefficients divided by C are integral. Thus the new single-coefficient condition is equivalent to the original two-coefficient condition on every permitted exterior solution.

More explicitly, its index inequality is

    2+2v3(a-1) >= 2^25,

or v3(a-1)>=2^24-1. Combined with the already known evenness and nonzero condition, the exact allowed index set remains

    a-1 in 2*3^(2^24-1) Z, a-1 != 0.

There is no rounding error in this threshold. All old height margins and arbitrary further divisibility remain available.

## Rational witnesses and both directions

The source's quaternion convention is i^2=2, j^2=3, ij=-ji, hence (ij)^2=-6. The algebra ramifies precisely at 2 and 3 and splits at the real place. Voight's proposition applies to the quadratic field Q(sqrt(d)), with d=1-2/(3t^2), when d is nonsquare and t is nonzero. The required nonsplitting at all ramified places means exactly that d is nonsquare in Q2 and Q3. The split rational-square case is excluded by the division-algebra condition; t=0 has an explicit separate witness.

I checked the local square tests. If v2(t)>0, d has odd negative valuation; if v2(t)=0, d is 3 modulo 8; if v2(t)<0, d belongs to 1+8Z2 and is a square. At 3, v3(t)>=0 gives odd negative valuation, while v3(t)<0 gives d in 1+3Z3 and hence a square. Therefore exactly t in Z_(2) intersect Z_(3) admits the required embedding and trace-zero representation.

To make the coordinate translation explicit, an embedding produces

    2x^2+3y^2-6z^2 = 1-2/(3t^2).

Set U=3ty, V=tx, W=3tz. Multiplication by 3t^2 gives

    U^2+6V^2-2W^2-3t^2+2=0.

The map is reversible for nonzero t. At t=0, (U,V,W)=(0,0,1) works. This is an indefinite ternary representation, not a claim that all positive rationals are represented by a positive-definite form. There is no sign or real-place restriction missing from the application.

Use t=f1/C and multiply U,V,W by C. The equation is exactly

    u^2+6v^2-2w_old^2-3f1^2+2C^2=0.

For an old exterior solution, its old anchor supplies semilocal integrality, which supplies these new rational witnesses. Conversely the new witnesses supply semilocal integrality of f1/C and hence of both coefficients. Apply the original lemma to A/C^2, where A=f0^2+f0*f1-f1^2, and scale its witnesses by C^2 to recover the old physical anchor. Restore the coordinate A by its displayed polynomial definition.

The old stored anchor is an invertible affine translation of that physical anchor. Explicitly, with S0=C^2,

    u_old=S0+(U-3V+3W)/4,
    v_old=S0/2+V/4,
    w_old=3S0/2+W/4.

Its linear determinant is 1/64. Multiplying the physical residual by 16 gives the stored residual

    U^2-6UV+6UW+15V^2-18VW+7W^2+8S0*U-48A^2.

Thus both witness directions are defined over Q. They preserve every coordinate outside the private anchor witnesses and the deleted A coordinate; a bijection of individual witness tuples is neither needed nor asserted.

## Translation and binding in candidate 505

Substituting w_old=w+C cancels the constant and gives

    u^2+6v^2-2w^2-4Cw-3f1^2=0.

The inverse is w=w_old-C. In the frozen 505 candidate, the actual f1 is coordinate 505, exactly the value `Sscalar.f.1` inherited from the mixed-depth source. The private coordinates are 55,56,57. I checked their incidence: they occur only in the replaced anchor residual. The deleted coordinate 535 and the deleted physical-A definition do not survive. The new residual is exactly the displayed equation, with no hidden scalar rescaling of f1. Its fixed parameter is C=3^(2^25), not S0.

The other component proposals do not alter this field basis, scalar point or root-index parity. Their interaction with their own downstream arithmetic is outside this review, but none changes the input consumed by the anchor equivalence.

## Exact large coefficient

The term -4Cw in the translated residual contributes 16C^2*w^2 to its square. The term -2w^2 contributes 4w^4, not 4w^2. Inspection of the complete 505 table shows:

* the only term quadratic in C is 16C^2*w^2;
* there is no lower-C contribution to its coordinate monomial w^2;
* all linear-C coefficient multipliers have magnitude at most 48;
* all C-independent coefficients have at most 1520 bits.

Since C=3^(2^25), these bounds make the exact maximum absolute coefficient

    16C^2 = 16*3^(2^26).

No expansion of C or C^2 was performed. The presently frozen `05-anchor/REPORT.md` already states 16C^2 correctly. The combination report's reference to correcting an earlier `16C^2+4` claim is historical and does not describe this frozen version; this is an attribution detail, not an error in either frozen polynomial.

## Verification and scope

`check_anchor_review.py` was written for this review and imports neither proposal producer. It independently recomputes the starting point and residue using tangent doubling, checks the literal 505 anchor and its private-coordinate incidence, checks the identity of the f1 coordinate, and inspects the exact parameter-dependent coefficient terms. It passes. Its finite calculations check the base case and artifact binding; the all-index result is the formal-group proof above, not an inference from sampled multiples.

The earlier source arguments are present and were read. The coefficient-specific refinement is proved in the current anchor proposal and is not incorporated into the frozen Version 11 manuscript. Broader historical priority was not investigated and remains unresolved. No shared source, manuscript or acceptance register was edited during this review.
