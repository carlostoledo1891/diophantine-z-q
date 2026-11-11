# Use the even H valuation: 330-variable component

Author: `/root/astra_quartic_opt03_depth`, November 7, 2026. This separate candidate improves the pending332 construction by two coordinates. It has **330 total rational variables**, **329 witnesses**, **300 quadratic residuals**, **5792 quartic monomials**, degree four and integer content one. The fixed symbolic constant and maximum coefficient remain C=3^(2^25) and16C². Neither332 nor this extension is declared independently accepted here. No previous packet was modified.

## Exact bindings

| Object | SHA-256 |
|---|---|
| Source `../four-groups/candidate332-ir.json` | `27dfc0e11bcdaceb2c71b6562bb3e9a0f3dfd5147338a4a4ffd14d1f53ba4c63` |
| Source `../four-groups/REPORT.md` | `a23811d6368fea51e5f9a8ed9fc5fdf5908fce7e77470f204cd4c764967c1cfa` |
| `candidate330-ir.json` | `41602bf9d25d52ae6e461f958eb21e1d752190ef71a72c1cc7c444f4e0a9fff6` |
| `polynomial330.json` | `c4fcd50ed0322c4e7b0ce6bf48bed6e2321e5d8610c061bb4dd1ac4e56981f81` |

The ultimate accepted source is366, SHA `0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56`. All its arithmetic sources and independent acceptances are pinned in the332 report. This component uses their unchanged pole and root-height inputs, with the new local and completeness arguments below. The unreviewed332 report is a proof dependency to inspect, not an authority substituted for independent review.

## Changed groups and exact accounting

Use the notation of the332 report. There H0=f(H), H4 is the Lucas polynomial test, P_i=f(U_i)², and T_j=conjugate(f(V_j)^8). Replace only G0 and G2 by

    G0=1+E^79 H4²+E^158 H2^4+E^4 P1²+E^8 T0,
    G2=1+E^19 M0²+E^158 H0²+E^4 P3²+E^8 T3.

Keep

    G1=1+E^79 H1²+E^158 H3^4+E^4 P2²+E^8 T2,
    G3=1+E^19 M1²+E² P4+E^4 Z1+E^8 T4.

Every test is still present. The H4 test moves from the quartic leaf H4^4 to its already stored square H4². The H0 test moves from a generic square-weight slot to the valuation-multiplicity-four slot. Delete the now unused H4^4 pair824/825 and its defining rows737/738. The twelve component rows for G0/G2 across the three detectors are the only other changes from332. No new coordinate or row is added.

In physical coordinates H0²=v311+2rho*v312 and H4²=1-2v253+v319+rho*(4v320-4v254). Hence both replacements are quadratic in the existing coordinates and weights. The total is332-2=330 variables, with the same distinguished input. All other332 coordinates and residuals are retained verbatim.

## Why the new local class is valid before any height conclusion

At a consumed prime p>76176, the generic squared-H equations recover a nonzero f with U=f² and a genuine curve point x=1/f,y=S/f. The explicit Kummer-to-curve identity and all denominator conditions are given in the332 report. This recovery precedes any logarithm or height use and does not divide by c+Df. Since y²=x(x²-D) and D is a unit, v(x) is even by the three cases v(x)>0, v(x)=0, v(x)<0. Therefore v(f) is even and

    v(H0²)=v(U) belongs to4Z.

On the pre-H branch U=0 this leaf is zero. On the other exceptional branch U=-v² the fixed values v=(3+2rho)/4 or(-36+16rho)/49 are units, so the valuation is zero and still belongs to4Z. Thus every branch needed in the noncircular detector argument gives the class4Z or infinity. No arbitrary nonsquare field element has been assigned a fourth root.

At an odd positive contact valuation alpha, the four nonconstant terms of each G still have, modulo16 and after multiplication by alpha inverse, the disjoint classes

    odd; 2 modulo4; 4 modulo8; 8 modulo16.

The new G0 uses the ordinary square H4² in the first class. The new G2 uses H0² of class4Z with weight158 in the second. All other classes are unchanged. The source332 proof of a unique minimum, W!=0, Re(W)!=0, z!=0, the trace bound, and one common place with every term valuation>-alpha/2 therefore applies literally.

At that common place the new high terms give

    2v(H4)>78.5alpha, hence v(H4)>=40,
    v(U)>157.5alpha, hence v(U)>=160 and v(f)>=80

in the generic branch. The latter is stronger than the old required order40 on f(H). On the exceptional branches T0 remains the same fixed unit, so the unchanged T0 term excludes every nonempty required radical before any H meaning is assumed. The old root-height/anchor contradiction then excludes those branches. All other old orders follow as in332. The unchanged downstream logarithm, Lucas and scalar24 argument consequently establishes integer-input soundness.

## Stronger completeness choice and its compatibility

The old complete witnesses only guarantee f(H) has valuation at least40. For the new weight158, that is insufficient. We explicitly choose primary formal depth40, so f(H) has valuation at least80 and U=f(H)² at least160.

In the pinned released Version13 TeX, SHA `9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd`, lines20631-20649 give

    gcd(M_-,M_+)=1, gcd(M_-,L)=16, gcd(M_+,L)=1,
    gcd(Pi,M_+)=gcd(Pi,L)=1.

Thus the simultaneous congruences remain compatible with

    h=0 mod Pi^39 M_-,  h=1 mod M_+,  h=h0 mod L

instead of the source exponent19. The common divisor with L is unchanged, and the same h0 handles it. No factor Pi is added to the opposite h-1 congruence. The original reduction-order argument first makes H formal of depth at least1; multiplication by p^39 then gives depth at least40 via the retained unramified formal-logarithm isometry. Integral multiplication preserves this subgroup, so U_i=[n_i]H also remains formal to at least that depth for every integer label, including zero and negative labels.

All roots, scales, finite neighborhoods, scalar conditions and real comparison bounds are chosen in the old order before contact-prime selection. The larger exponent changes only the final progression. The source real-density argument applies to it because the same residue/modulus divisibility by m0 remains true. Its positive tail meets the same nonempty compactly contained real neighborhood. Thus the final H has the new primary depth while preserving every old scalar local condition and real bound.

At a selected successful place alpha=1, the new H4² term has valuation at least80-79=1. The new H0² term has valuation at least160-158=2. All other nonconstant terms have the positive margins proved in332. Hence each G has residue1. At the opposite place the same disjoint-class argument gives inverse residue0 or1. The trace is a unit with residue1 or2 and B has positive odd valuation1. Away from the selected primes its valuation is even, because the same R and square denominator formula remain in use.

At2,3,17 the unchanged continuity neighborhoods bound all tested functions and their powers below in valuation. All weight exponents are positive, and v(E)=5(nu-v(A)) tends to positive infinity under the same freely prescribed denominator divisibility. The new G terms therefore tend to zero along with the old ones. W tends to1, T tends to2, the same local squareclasses persist, and the preparation-zero valuation thresholds follow. These choices occur before the contact primes and are preserved by h mod L.

At each real embedding H4² and H0² are nonnegative on the actual complete witnesses. The same positive E tends to zero uniformly against bounded functions, so W>0, T>0 and B tends to zero through positive values as in332. One large common lambda gives all three B in(0,17), and the existing pole realization supplies their witnesses. Thus every integer input is realized. The claim is equality of rational input projections; arbitrary old detector witnesses need not be preserved.

## Finite evidence and review status

`verify330.py` imports no producer and verifies the resulting system directly against accepted366. It checks every retained outside row, all removed-coordinate consumers, the55 new row expressions, actual normalized test squares, cached alternate powers and every coefficient of the full primitive SOS. All330 coordinates are active; there are300 residuals and5792 quartic monomials. C-independent coefficients have at most1520 bits, and the old C-dependent terms are unchanged, giving maximum16C² without a decimal expansion.

`build330.py` separately records the two-coordinate/twelve-row component delta from332. The stronger primary-depth premise is explicit in this report and is not attributed to the old completeness witnesses. Independent review must cover both the332 grouping proof and this changed H class/completeness application before330 is accepted. No publication below the required strict300 threshold is claimed.
