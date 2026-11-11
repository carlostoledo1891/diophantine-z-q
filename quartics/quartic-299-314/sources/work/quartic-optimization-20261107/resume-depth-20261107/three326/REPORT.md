# Three mixed-residue groups: 326 variables

Author: `/root/astra_quartic_opt03_depth`, November 7, 2026. Independent review is pending. This candidate has 326 total rational variables, 325 witnesses, 296 quadratic residuals and 5787 quartic monomials. It improves the separate327 circuit by one variable. It uses only the original Pi^19 completeness progression, rather than the stronger Pi^39 choice used in330/327. No frozen source or release was changed.

## Exact inputs and outputs

| File | SHA-256 |
|---|---|
| `../chain327/candidate327-ir.json` | `d7f0ce856f2844486043d0d16388a4e72f4cf2da05736c3e9379d9bd50518665` |
| `../chain327/REPORT.md` | `025ccfce6b15e7eef4428ab9b1e1a61c39aa4002c2d0d8096bf7e295f7730706` |
| `../four-groups/candidate332-ir.json` | `27dfc0e11bcdaceb2c71b6562bb3e9a0f3dfd5147338a4a4ffd14d1f53ba4c63` |
| `../four-groups/REPORT.md` | `a23811d6368fea51e5f9a8ed9fc5fdf5908fce7e77470f204cd4c764967c1cfa` |
| `candidate326-ir.json` | `48cf6abbc2bd5393b14413314e1297c8bf235bd990202c7bb97ac203b7387c84` |
| `polynomial326.json` | `a9d9d35484420aa9a2075a3ffbdfef2cf31287e3448b09fe4709c3fa88ffa4a7` |

The332 source review is `work/quartic-optimization-20261107/resume-review332-20261107/REVIEW.md`, SHA `23c56ae01584e21db03d5a7ad9464680414f733eeab360e7788572f73d761526`. The ultimate accepted366 IR and unchanged arithmetic sources are pinned in the332 report. The released Version13 manuscript has SHA `9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd`. Its local log/CRT interfaces and later rational logarithm formulas are used with their original domains. This packet makes a new detector application and requires its own review; the earlier332 review does not accept it automatically.

## The new sums

Use K=Q(rho), rho^2=2, D=11-6rho, and R=F5(A*lambda), E=1/R separately for each of the three unchanged rational square scales. Retain the332 meanings

    H0=f(H), H1=L2-L'2, H2=L3-L'3,
    H3=L4-L'4, H4=F(L2,L3,L4),
    M0=L1-L'1, M1=L1-beta,
    P_i=f(U_i)^2,
    Z1=conjugate(f(V1)^4), T_j=conjugate(f(Vj)^8).

Define

    G0 = 1 + E158 H1^4 + E157 H4^4 + E39 M0^4
           + E8 T0 + E4 T4,
    G1 = 1 + E158 H2^4 + E79 H0^2 + E8 T2
           + E4 Z1 + E P1,
    G2 = 1 + E158 H3^4 + E39 M1^4 + E8 T3
           + E157 P2^2 + E4 P3^2 + E P4^2.

Here Ek denotes E^k. Set W=G0*G1*G2. Keep the same two norm/pole equations

    Norm(W)=2 Re(W) z,       B(R+E+2)=z^2.

The only new scalar power is E157=R*E158. The retained equation RE=1 makes this identity exact for every rational solution. E39 is the actual repurposed chain coordinate in327, not the historical E38 coordinate. Its defining equation E39*R=E19^2 and all other327 power equations remain unchanged.

## Local residue argument, before H and the integer labels

At a consumed unramified place above p>76176, let alpha=v(R)>0 be odd. Each of the four generic high tests and each middle test is an element of K; its fourth power has valuation in4Z or is zero. Primary f(U_i) has even valuation on the retained curve chart, including negative valuations. Thus P1 has valuation in4Z and P_i^2 in8Z. The alternate caches T_j and Z1 have valuations in16Z and8Z respectively.

For H0^2 use the separate pre-H argument, not the eventual integer-index conclusion. In the generic squared-H branch, the retained equations recover f and F with U=f^2, V=F^2, fF=v^2, F=f*t^2. Writing c=a^2 and b^2=c^2-D, the identity

    c*(f*S^2+D*f^2-1)
      -(c+D*f)*(c*f*(1+t^2)+D*f^2*t^2+2*b*f*t-1)
      = f*(b^2-c^2+D),
    S=(b+c*t+D*f*t)/a,

recovers the genuine H curve point without dividing by c+D*f. The valuation cases in y^2=x(x^2-D), with D a unit, show v(f) is even. Hence U=H0^2 has valuation in4Z. On the exceptional U=0 branch the leaf is zero; on the Q=0 branch U=-v^2 and the classified v is a fixed unit, so its valuation is0. These are precisely the branches and constants established in the accepted squared-H proof and rechecked in332. No sign or square-root choice is imposed here.

Multiply all valuations modulo16 by the inverse of alpha. The nonconstant terms have the following disjoint residue classes within each row:

| Group | Term classes modulo16 |
|---|---|
| G0 | 2 mod4; 3 mod4; 1 mod4; 8 mod16; 12 mod16 |
| G1 | 2 mod4; 1 mod4; 8 mod16; 4 mod8; 3 mod4 |
| G2 | 2 mod4; 1 mod4; 8 mod16; 3 mod8; 4 mod8; 7 mod8 |

None contains0, the class of the constant. Each nonzero sum has a unique term of smallest valuation, and v(Gj)<=0. This applies also when some test is zero. In particular W is nonzero at a consumed contact. Its global field norm row then forces Re(W) and z nonzero, giving T=Tr(1/W)=1/z there. Put lambda=max(v_q(W)) over the places q above p. The trace bound gives v_p(T)>=-lambda. Since R+E+2=(1+R)^2/R, the pole has

    v_p(B)=alpha-2v_p(T)<=alpha+2lambda.

Its parity is odd. The inherited pole condition excludes negative odd valuation, so lambda>-alpha/2. Choose a place attaining lambda. Because every v(Gj)<=0, each v(Gj)>=lambda, and the unique minimum argument then puts every individual term above -alpha/2 at this same place. The argument is unchanged at an inert unramified prime, where there is a single valuation and the trace estimate still holds.

The resulting inequalities give the following minimum depths at that common place:

| Tests | Forced depth |
|---|---:|
| H1,H2,H3 | 40, from 4v>157.5alpha |
| H4 | 40, from 4v>156.5alpha |
| H0 | 40, from 2v>78.5alpha and even v |
| M0,M1 | 10, from 4v>38.5alpha |
| f(U2) | 40, from 4v>156.5alpha and even v |
| f(U1),f(U3),f(U4), all alternate f | at least2 |

All are at least the required332 orders. The stronger U2 requirement is harmless in soundness and will be supplied explicitly in completeness below.

The pre-H exceptional branches are still excluded without circular use of the height conclusion. In both branches V=f(V0)^2 is a fixed unit at every consumed prime, so T0=conjugate(V^4) is a unit. Its E8*T0 term contradicts the just-proved common-place strict bound if any of the three required radicals is nonempty. If all are empty, the unchanged root-height inequality and independent scalar anchor already contradict that possibility. Thus the generic H meaning, the logarithm denominators, and the original integer-label/height argument can be restored in the same order as332. This yields integer-input soundness. The proof does not first infer the desired label equality or H formality in order to justify a valuation class.

## Completeness with the original progression

Use the original complete witnesses for every integer input, the same root/parity and scalar choices, and the same prime-pattern inputs as332. Choose

    h=0 mod Pi^19 M_-,  h=1 mod M_+,  h=h0 mod L.

The established coprimalities and fixed overlap with L are unchanged. Hence H and every nonzero U_i=[n_i]H have primary formal depth at least20. Their f-values have valuation at least40. A zero U_i contributes exact zero. The primary parameter ratios equal the integer labels to order80. At the alternate place the G2 ratio has order12 and the rational-G9 ratios have order40. Thus M0 has valuation at least12, M1 at least80, H1,H2,H3 at least40, and the exact Lucas relation on the integer labels gives H4 at least40. This uses the actual G2 precision, not an unsupported order40 claim for M0.

At a selected successful place alpha=1, the nonconstant term margins in G0 are at least 2,3,9,8,12. In G1 they are at least 2,1,8,4,79. In G2 they are at least 2,281,8,3,156,159. Every margin is positive. In particular E157*P2^2 has margin160-157=3 because U2 has formal depth20; no new congruence on h is needed. Consequently all three Gj have residue1 at the successful place. At the opposite place the same disjoint classes imply each inverse Gj has integral residue0 or1. The trace has residue1 or2 and is a unit, so the retained B has odd positive valuation1 at selected contacts. Elsewhere its valuation is even whenever v(R) is even, by the unchanged square-denominator formula. The original contact-pattern support statement handles the remaining primes.

The change introduces the weight E itself in two terms, but every exponent is still positive. At2,3,17 the same finite neighborhoods bound all test functions and their displayed powers below. Increasing the preparatory denominator divisibility gives v(E)=5*(nu-v(A)) tending to positive infinity. Hence all new nonconstant terms tend to zero, W tends to1, and T tends to2 with any prescribed finite accuracy. This preserves the source small-prime squareclasses and preparation/pole thresholds. No threshold is justified merely by the old minimum weight exponent; the freely chosen divisibility is enlarged if needed before contact-prime selection.

At either real embedding, all displayed leaves are even powers of real test values. E>0 for the sufficiently large positive real parameter used in the source. Thus Gj>=1, W>0, T>0 and the pole is defined. The tests remain bounded on the fixed compactly contained real neighborhoods, so every E^k term tends uniformly to0 as the real parameter grows. B tends to0 through positive values and may be placed in(0,17) simultaneously for all three scales. Fix these bounds and finite neighborhoods first, then choose the contact primes, and finally use the source real-density statement on the same h progression. This ordering preserves both the real and local conditions. The unchanged pole realization provides all remaining witnesses.

The conclusion is equality of rational input projections. General old and new detector witnesses need not map to each other; the proof reconstructs complete witnesses for each integer input and proves every new witness has integer input.

## Literal accounting and verification

The nine shared field squares are H1^4,H2^4,H3^4,H4^4,M0^4,M1^4,P2^2,P3^2,P4^2. They use18 rational coordinates. Five field squares used10 in327. Reuse820/821 for H2^4,822/823 for H3^4,828/829 for P2^2,830/831 for P3^2, and repurpose826/827 from P1^2 to H1^4. Add835..842 for the remaining four squares. Add843,844,845 for the three E157 values.

For each detector beginning at b=634,654,674, use b..b+5 for its three group values and b+6,b+7 for G0*G1. Put (G0*G1)*G2 in the unchanged final W pair. Delete b+8..b+11. The net change is

    327 + 8 shared coordinates + 3 scalar weights - 12 evaluations = 326.

The literal normalizations of H4^2, M1^2, primary squares and cached conjugated alternate powers are those proved in332. The new code repeats their exact affine formulas, including the shifted M1 square and division by D^4 followed by conjugation. No nonexistent high power is treated as a free cache.

`verify326.py` imports no producer. It constructs all51 new residuals independently, compares every retained outside row, checks every deleted or repurposed coordinate incidence, verifies the complete active inventory, and checks all16 residue patterns and inferred/completeness depths by exact integers. It then independently expands all296 primitive residual squares and matches every one of the5787 output coefficients. The degree is four and content is one. C-independent coefficients have at most1520 bits. The five C-dependent terms are unchanged; with C=3^(2^25), the exact maximum coefficient is still16C^2.

The preceding bounded search is recorded separately in `../three-groups-search`. Its capacity and residue computations suggested this construction, but they are not substitutes for the arithmetic proof above. Neither a global optimality claim nor a sub300 construction is asserted. Independent review remains required before this component is combined or published.
