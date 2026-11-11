# Common-scale detector with an eighth-power guard

Author: `/root/astra_quartic_opt03_depth`, November 7, 2026. Agent01 supplies the separate compiler and literal consumer audit. This is a new, unaccepted arithmetic proposal. It preserves the published arithmetic inputs. It does not assert independent acceptance, and its count must be bound to the compiler packet before use.

The intended source is accepted315, `work/quartic-under300-20261107/10-combination/combined315/candidate315-ir.json`, SHA256 `d450a34735fe84bab0900abb3931740d4f7cedb1004ede7a81e1a09c4249f8b8`. The underlying three-group theorem is `../three326/REPORT.md`, SHA256 `766427b1e75cf10823b0119b9d3a415a8460b49cbebb31c1b2b8483502f3baf8`, and the chain-only change is `../chain323/REPORT.md`, SHA256 `828cd7cfb7649b1e93cb3fbe22d1d5dc50f7d8ed1b71c20242b3634029417b15`.

The corrected common-scale arithmetic is `../common-scale/RECIPROCAL-VARIANT.md`, SHA256 `e233eaaa7f45f44411731719f8b9412d8f38c448e9a6ca5d7e10a2a7320874c1`. Agent05 accepted that source-level argument in `resume-review-common-scale-20261107/REVIEW.md`, SHA256 `9f5475d58311f49234a6a80804aac58be4a66f247f209bcc86e7095b49bb3d6f`. That review explicitly excludes the H-bootstrap used here. The original156 proposal remains rejected. No earlier review is being extended to this proposal.

## Exact new interface

Use a new nonzero rational gamma, unrelated to the fixed large anchor coefficient. For each detector retain its actual R=F5(A*lambda) and E=1/R. Retain every point, input, root, scalar, anchor, pole and product definition outside the changed detector groups and power gates. In particular, all three R values remain independent functions of the original scales. No integrality or disjoint-support assertion is made about the other R values at a prime consumed by one detector.

Write H0=f(H), H1=L2-L'2, H2=L3-L'3, H3=L4-L'4, H4=F(L2,L3,L4), M0=L1-L'1 and M1=L1-beta. Write Pi=f(Ui)^2, U=H0^2, Z1=conjugate(f(V1)^4), and Tj=conjugate(f(Vj)^8) for j=0,2,3,4. These are the actual source objects, including the signed pre-H interpretation of U and the independently reconstructed V0 test.

Repurpose the nine private square-output pairs as

    ZHi=Hi^4/gamma^160, i=1,2,3,4;
    ZMi=Mi^4/gamma^40, i=0,1;
    ZP2=P2^2/gamma^160;
    ZP3=P3^2/gamma^80; ZP4=P4^2/gamma^80.

Add one field pair ZP1=P1^2. All these definitions are quadratic after using the retained square inputs. They are not substitutions into any other consumer. At each detector use exactly

    G0=1+R ZH1+R^2 ZH2+E U+E^4 Z1+gamma^16 E^8;
    G1=1+R ZH3+R^2 ZH4+R^3 ZP2+E^4 ZP4+E ZP1+E^8 T0;
    G2=1+R ZM0+R^2 ZM1+R^3 ZP3+E^8 T2+E^4 T3+E T4.

Keep W=G0 G1 G2 and the source norm, trace and pole equations. The exact E powers and R powers are local scalar coordinates, so each displayed term is quadratic. The shared chain has nine rational coordinates gamma,gamma2,gamma4,gamma8,gamma16,J,gamma40,gamma80,gamma160. It imposes successive squares through gamma16, gamma16*J=1, gamma40*J=gamma16*gamma8, and two final squares. Thus gamma is nonzero in every rational solution, and all common powers have unique values. This proposal does not rely on the separate unreviewed algebraic gamma-zero exclusion.

## Local classes before point reconstruction

At a consumed prime p>76176, let alpha=v(R)>0 be odd and c=v(gamma) be any integer. No sign or size bound on c is assumed yet. The periods and local exponents of the terms are

    G0: (4,1),(4,2),(4,-1),(8,-4),(16,-8);
    G1: (4,1),(4,2),(8,3),(8,-4),(8,-1),(16,-8);
    G2: (4,1),(4,2),(8,3),(16,-8),(16,-4),(16,-1).

The exponent is multiplied by alpha. Each period includes the possible valuations of its field leaf. All gamma exponents are divisible by that period. The last G0 term has residue16c-8alpha=8 modulo16. Thus every listed class is nonzero and distinct from the other classes in its group for every odd alpha and arbitrary c. Zero leaves are omitted. This establishes the unique-minimum argument without H, log or integer-label conclusions. `check_classes.py` verifies all residue cases, but the displayed periods themselves give the unbounded assertion.

The source trace/pole proof therefore applies unchanged. At one common place each term of every group has valuation greater than -alpha/2. This is one place for the whole product, not a separate choice for each test. In particular the rational guard gives

    16c-8alpha > -alpha/2, hence c>15alpha/32.

For alpha=1 this forces c>=1; for alpha=3 it forces c>=2; for odd alpha>=5 the displayed strict inequality suffices. The high comparison terms have lower bounds

    4v(Hi)>160c-(r+1/2)alpha, r=1 or2.

At alpha=1 the smaller bound is157.5; at alpha=3 it is312.5; at alpha>=5 it is greater than72.5alpha. Hence every Hi has valuation at least40. The middle terms similarly give4v(Mi)>40c-(r+1/2)alpha for r=1 or2. The worst bounds are37.5,72.5 and16.25alpha respectively, so both Mi have valuation at least10.

The primary-square bounds are

    4v(f(U2))>160c-3.5alpha;
    4v(f(U3))>80c-3.5alpha;
    4v(f(U4))>80c+3.5alpha.

They imply respectively v(f(U2))>=40, v(f(U3))>=20 and v(f(U4))>=22. For U3 and U4 use the even valuation of f at a genuine formal point, after the low positivity first establishes formality. Before that conclusion their positivity is already enough for the source point-chart criterion. The alpha=1 right sides are156.5,76.5 and83.5. For alpha=3 they are309.5,149.5 and170.5. For alpha>=5 they exceed71.5alpha,34alpha and41alpha. These bounds cover all odd positive alpha.

Every other original low formality test still follows. E U forces2v(H0)>alpha/2. E ZP1 forces4v(f(U1))>alpha/2. E^4 Z1 forces4v(conjugate f(V1))>3.5alpha. The three eighth-power alternate tests have positive right sides from E^8,E^4,E. Thus all required f-values have positive valuation at the appropriate place. The conjugation is the original one and must not be dropped by the compiler.

The changed T0 weight remains E^8 exactly. Consequently the source pre-H unit exclusions, including both signed fixed branches of the squared-H chart, still work before reconstructing H. If every relevant odd support is empty, the independently established anchor/root-height argument supplies the old contradiction. This proposal adds no assumption that a consumed prime already exists and does not use the later H-depth conclusion to obtain one.

## Recovering H depth without the old high H0 test

This is the new application requiring independent review. The exact logarithm source is Version13 `manuscripts/quartic_v13.tex`, SHA256 `9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd`, around lines20885-20900, together with the accepted half-index H extension and exact primary relation z(Ui)=Li*z(H). The initial formality just proved suffices for every full logarithm to equal z times an analytic unit; at the identity use unit1. The known index denominators divide2, a unit at the consumed prime. At least one of h and h-1 is a unit. Thus at least one of the primary and alternate full ratios is integral. The positive-order cross-test forces both approximate ratios to be integral, and multiplying by the relevant units then gives integrality of both full ratios. This step uses no high H depth.

In particular L2,L3,L4 are integral at the common place. The H4 test says F(L2,L3,L4) has positive valuation, while

    F(A,T,B)=T^2-A(A-2)TB+(A-2)^2B^2-1

has F(0,0,0)=-1. At least one of L2,L3,L4 is therefore a unit. Its exact relation z(Ui)=Li*z(H) shows that Ui is not the identity. Each of U2,U3,U4 is formal of depth at least10 by the preceding f bounds. Hence H is formal of depth at least10. All other integral primary Li then imply the same depth for nonidentity Ui. Identity points have zero approximation error.

The primary log correction now has relative order at least40, since its first error is order4v(z). The alternate G2 approximation supplies order12, and the other alternate rational approximations supply order40. Integral ratios turn these into the required absolute errors. The middle and high comparisons therefore give exactly the old order10 input-label precision and order40 Lucas-label precision. The unchanged height and Lucas arguments receive their original objects and hypotheses. The reasoning is noncircular: only F(L) modulo the prime is used to recover H depth; F on the integer labels is proved afterward by height.

## Completeness and choice order

Keep the original Pi^19 progression and its source bounds. At a selected successful place alpha=1, choose c=1. Source completeness gives primary f valuations at least40 or identity values, high Hi valuations at least40, and middle Mi valuations at least12. The latter uses the actual alternate G2 error12, not merely the weaker order10 theorem statement. With c=1, the high term margins are1 or2, middle margins at least9 or10, P2 has margin3, P3 and P4 have margins at least83 and76. The promoted P1 term has margin at least159. The guard margin is8. Unchanged alternate values give positive margins with their new, no larger, E exponents. Identity leaves are zero and satisfy the same conditions. No increase of Pi or alternate truncation order is used.

Choose gamma exactly as in the corrected common-scale proof: gamma/lambda in(1,2), v(gamma)=v(lambda)=-nu_p at2,3,17, and v(gamma)=1 at every selected contact prime. The finite CRT prescription on gamma/lambda requires valuation0 or1 at selected primes and valuation0 at2,3,17. Denominators congruent1 modulo the finite prime-square product and numerators in a sufficiently long interval realize this simultaneously. Repeated contact primes prescribe valuation1 only once. No pairwise-disjoint support is assumed.

For eta_j=v(A_j), the actual source formula is v(E_j)=5(nu_p-eta_j). The new common coefficients have valuations

    v(gamma^-160 R)=155nu_p+5eta_j;
    v(gamma^-160 R^2)=150nu_p+10eta_j;
    v(gamma^-160 R^3)=145nu_p+15eta_j;
    v(gamma^-40 R)=35nu_p+5eta_j;
    v(gamma^-40 R^2)=30nu_p+10eta_j;
    v(gamma^-80 R^3)=65nu_p+15eta_j;
    v(gamma^-80 E^4)=100nu_p-20eta_j;
    v(gamma^16 E^8)=24nu_p-40eta_j.

All grow to positive infinity with the old freely chosen preparatory divisibility. The eta_j and lower bounds on the test values are fixed first by the original finite neighborhoods. The unchanged low terms also tend to zero. Thus W tends to1, the trace to2, and the old small-prime squareclasses and pole inequalities hold.

At each real embedding R_j is asymptotic to A_j^5 lambda^5. Uniformly for gamma/lambda in(1,2), the corresponding coefficients decay with lambda exponents -155,-150,-145,-35,-30,-65,-100,-24. They are positive, and all leaves are even powers divided by even powers. Thus the real groups and trace are positive and the unchanged pole is asymptotic to1/(4R_j). The required real bound can be fixed before prime selection. Then select contact primes, choose gamma by CRT, and select the final H in the original finite/real progression. Nothing chosen last changes the already fixed bounds. Primes introduced by gamma cause no new odd-denominator obligation where v(R_j) is even, because the pole valuation differs from v(R_j) by an even integer.

## Count and limits

The joint circuit starts from315, removes four old scalar coordinates per detector and keeps five local coordinates E,R^2,R^3,E^4,E^8. It adds nine common scalar coordinates and one field pair ZP1. The proposed total is315-12+9+2=314. The nine existing private field pairs are rescaled in place. U and all alternate caches keep their actual old meanings. Agent01 must bind this arithmetic note to the emitted IR, verify every changed and unchanged consumer, reconstruct the full sum of squares, and freeze the exact count. A successful finite check does not independently accept the new H-bootstrap or changed guard argument.

This proposal does not claim that common-scale sharing yields a large reduction. The only proposed gain over315 is one rational coordinate. The previous317 cost witness, failed156 construction, guarded-packing obstructions and accepted323 packet remain preserved.
