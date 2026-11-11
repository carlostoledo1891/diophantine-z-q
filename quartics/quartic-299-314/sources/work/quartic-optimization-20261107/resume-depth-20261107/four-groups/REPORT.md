# Four-group cross-order detector: 332 variables

Author: `/root/astra_quartic_opt03_depth`, November 7, 2026. Independent arithmetic review is pending. This candidate is built directly from accepted366 and has **332 total rational variables**, **331 witnesses**, **302 quadratic residuals**, and **5764 quartic monomials**. Its degree is four, content is one, and maximum coefficient remains16C² for the fixed C=3^(2^25). It does not incorporate a new anchor. No released or previously frozen file was modified.

Unlike the separate340 construction, this design requires no increase of the completeness progression's primary depth. The existing Pi^19 progression suffices. The saving is a regrouping of tests with different valuation multiplicities and orders, using cached alternate powers.

## Exact source and result

| Object | SHA-256 |
|---|---|
| Source `work/quartic-under300-20261107/01-elimination/s-odd366/candidate366-ir.json` | `0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56` |
| Its independent review `03-depth/review366/REVIEW.md` | `409e919e31b68f8efa7c2ec8cac441c20720b118456988cd7978e74a6e4708e2` |
| `candidate332-ir.json` | `27dfc0e11bcdaceb2c71b6562bb3e9a0f3dfd5147338a4a4ffd14d1f53ba4c63` |
| `polynomial332.json` | `601f2695bcf5d28d927406dfa9d75e3dc1a3f30381c22780f88732c9109d39dc` |

The source conventions and unmodified arithmetic inputs are those of the accepted366 lineage. In particular, the bounded contact-polynomial pole is `10-combination/unweighted372/REPORT.md`, hash `f81c3e6b170881c54019cb876173de1fda651a17474376257152797426669daa`, with review `01-elimination/review372/REVIEW.md`, hash `3e5a5fe8a14025979b27bbb45c55f35d55c0237082f4fd7a299babc9b3e9d997`. Guard-free use is reviewed in `01-elimination/review369/REVIEW.md`, hash `908c25a0676875eef83cbe6fc5a94c152b5fcf94056fcdcf9537adfe73b66d89`. These relative paths are under `work/quartic-under300-20261107`.

The relevant H classification is `01-elimination/squared-h/REPORT.md`, hash `18682f8f61cbf7642e074a7e47641fb91aa1023b8c81c29edf233ca232d4f02a`, independently accepted by `03-depth/review390/REVIEW.md`, hash `61b755da24b3934ca8725159ac96c59c8b5090a4c7a032fe5487646853e7a667`. The released Version13 source has hash `9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd`; its source-level simultaneous choices are at lines20631-20663 and21447-21479. Later accepted reductions change the detector and low order to10 but preserve these choice interfaces.

## Four exact sums

Let rho²=2, K=Q(rho), D=11-6rho and retain R=F5(A*lambda), E=1/R for each of the same three rational square scales A. Let P_i=f(U_i)², Z_1=conjugate(f(V_1)^4), and T_j=conjugate(f(V_j)^8) for j=0,2,3,4. Let

    H0=f(H), H1=L2-L'2, H2=L3-L'3,
    H3=L4-L'4, H4=F(L2,L3,L4),
    M0=L1-L'1, M1=L1-beta.

The H tests require order40, M tests order10, and the primary/alternate f tests order1 in the source. Use

    G0=1+E^79 H0²+E^158 H2^4+E^4 P1²+E^8 T0,
    G1=1+E^79 H1²+E^158 H3^4+E^4 P2²+E^8 T2,
    G2=1+E^19 M0²+E^158 H4^4+E^4 P3²+E^8 T3,
    G3=1+E^19 M1²+E² P4+E^4 Z1+E^8 T4.

Set W=G0 G1 G2 G3 and keep the actual source equations

    Norm(W)=2 Re(W) z,       B(R+E+2)=z².

There are no new global nonzero guards, roots, constants or denominators. The new powers and products have unique rational values once the old outside coordinates are specified. The new W, z, B and pole witnesses are recomputed in completeness; no equality of old and new detector fibers is asserted.

## Literal realization and witness count

P_i is v[255+2(i-1)]+2rho*v[256+2(i-1)]. H0²,H1²,H2²,H3² are v[j]+2rho*v[j+1] for j=311,313,315,317. The final high square is

    H4²=1-2v253+v319+rho*(4v320-4v254).

The middle squares are

    M0²=v305+2rho*v306,
    M1²=v307-6v232+1224(v0+v248)+15321
           +rho*(2v308-6v233).

These are the actual affine normalizations, not unadjusted historical names. The checker proves their square identities from the source rows with beta=204(v0+v248)+2555 and the translated Lucas output.

For the four retained w^4 coordinate pairs a=182,200,212,224, corresponding to V0,V2,V3,V4, the exact cached output is (D*f(V_j)²)^4. Dividing by D^4 and conjugating gives

    T_j=(72097*v[a]+101904*v[a+1]
           -rho*(50952*v[a]+72097*v[a+1]))/5764801.

The shallow V1 cache gives directly

    Z1=((37249v192-34848v193)+25476rho*(v193-v192))/2401.

No new alternate powers are needed. The new shared coordinates are the three field pairs H2^4,H3^4,H4^4 at820..825 and the three field pairs P1²,P2²,P3² at826..831. Every pair is defined by squaring an existing affine field value, so each component equation is quadratic. The only new detector power is E^4=(E²)², at832/833/834. E²,E^8,E^19,E^158 already have their required meanings in the retained toric chain.

Each detector retains twelve of its twenty old private evaluation/product coordinates: eight for G0..G3 and four for G0G1,G2G3. Their product goes into the unchanged final W pair380/381,428/429,476/477. Delete all22 shared coefficient coordinates, eight obsolete evaluation/product coordinates per detector, and three unused E^237 coordinates. Add twelve shared square components and three E4 variables:

    366-22-24-3+12+3=332.

CERTIFICATE.json lists all49 removed coordinates and their91 removed residuals. There are57 replacement residuals. The entire incidence of deleted variables is checked, not only rows selected by their names. Every outside source row and surviving source coordinate object is unchanged, including scalar24, beta, root indices, S parity and the anchor.

## Valuation facts without circular H assumptions

At any consumed place p>76176, K is unramified and D is a unit. For a finite point y²=x(x²-D), the valuation of x is even. If v(x)>0 the second factor is a unit; if v(x)<0 its x² term strictly dominates D. The resulting equations2v(y)=v(x) or2v(y)=3v(x) both give evenness. The unit case is immediate.

The unchanged biquadratic chart identities already make the eight primary/difference squared leaves fourth powers before any integer-label conclusion. Hence P_i has valuation in4Z or is zero, P_i² in8Z, Z1 in8Z, and the ordinary alternate T_j in16Z. These statements do not use logarithmic comparison or a height contradiction.

For V0 before its difference-point meaning is known, use the actual squared-H equations. On the generic Q,U nonzero branch they recover f,F with U=f²,V=F²,f!=0,fF=v²,F=ft², and

    c f(1+t²)+D f²t²+2bf t=1.

The retained S=(b+ct+Dft)/a, c=a², satisfies

    c(fS²+Df²-1)
      -(c+Df)*(c f(1+t²)+D f²t²+2bf t-1)
       =f(b²-c²+D)=0.

Thus x=1/f,y=S/f is a genuine H point without dividing by c+Df. Its even abscissa valuation gives even v(f), and fF=v² gives even v(F) when F!=0. For F=0 all relevant powers vanish. Therefore the formal T0=conjugate(F^8) has valuation in16Z or infinity, without claiming F=f(H-P) yet.

On U=0, V=1/c² is a unit. On Q=0, U=V=-v² and v is (3+2rho)/4 or(-36+16rho)/49, both units at every consumed place. Hence T0=conjugate(V^4) is a unit on both exceptional branches. H0²=U has even valuation or is zero. Every other H square and M square is the actual square of a retained field expression. Squaring H2²,H3²,H4² gives valuation in4Z in every branch. These are all the input classes used in the new detector proof.

## Same-place soundness

At a prime in a required positive-contact radical, alpha=v_p(R)>0 is odd and1+R is a unit. The nonconstant terms in each G have valuation classes modulo16 which, after multiplication by alpha inverse, are

    odd; 2 modulo4; 4 modulo8; 8 modulo16.

For G0/G1 the exponents and leaf multiplicities are (79,2),(158,4),(4,8),(8,16). For G2 they are (19,2),(158,4),(4,8),(8,16). For G3 they are (19,2),(2,4),(4,8),(8,16). Odd multiplication preserves each subgroup of multiples of2,4,8,16. Together with the constant's residue0, these classes are disjoint and exhaust all16 residues. Every nonzero summand therefore has a distinct valuation class, including the constant. Zero leaves can be omitted. Each G is nonzero and its valuation is its minimum summand valuation, at most zero.

Consequently W!=0. The norm row forces Re(W)!=0 and z!=0. Put T=Tr(W^-1)=1/z and Lambda=max_w v_w(W). Trace integrality gives v_p(T)>=-Lambda. The unchanged pole row yields B=R/[T²(1+R)²] and

    v_p(B)<=alpha+2Lambda.

The valuation of B is odd. The retained pole obstruction excludes a negative odd valuation, hence Lambda>-alpha/2. At one place attaining Lambda, each G has valuation at least Lambda, since all other G valuations are nonpositive. Every nonzero summand of every G then has valuation greater than-alpha/2 at that same place.

For high squares weighted79 this gives2v(H)>78.5alpha and v(H)>=40. For high fourth powers weighted158 it gives4v(H)>157.5alpha and again v(H)>=40. For middle squares weighted19 it gives2v(M)>18.5alpha and v(M)>=10. P1²,P2²,P3² and Z1 have8-divisible valuations greater than3.5alpha, hence at least8. P4 has4-divisible valuation greater than1.5alpha, hence at least4. Each T_j has16-divisible valuation greater than7.5alpha, hence at least16. Thus all original primary and alternate f tests have valuation at least2, stronger than order1. Zero tests also satisfy the required lower bounds. Every old order holds at one common place.

In either pre-H exceptional branch, T0 is a unit, contradicting its forced positive valuation at any required radical prime. All three radicals would therefore be1. The unchanged366 anchor/parity and root-height argument excludes that possibility before any H logarithm is consumed. The generic H reconstruction is valid, and the same order implications also supply the old later H/V0 exceptional-point exclusions. All downstream logarithm, index comparison, Lucas, scalar24 and input-integrality arguments now have precisely their accepted inputs. New rational solutions therefore have integer input on the retained arithmetic hypotheses.

## Ordered completeness, including every pole condition

Use the existing366 choice order and the existing Pi^19 progression. The source fixes the integer input, scalar data, odd roots and scales, initial H, finite continuity neighborhoods, modulus L and a compact real neighborhood avoiding comparison poles before selecting contact primes. The source coprimalities make h=0 modulo Pi^19 M_-, h=1 modulo M_+, and h=h0 modulo L compatible. This construction and its real-density step are unchanged.

At every selected successful place, the old witnesses give v(H_j)>=40 and v(M_i)>=10. They give primary/alternate formal points with reciprocal-abscissa valuation at least2, by the even-valuation lemma; the original primary depth20 is more than sufficient. Thus in G0/G1 the four nonconstant term valuations are at least1,2,4,8 respectively. In G2 they have the same lower bounds. In G3 they are at least1,2,4,8 as well. Every G is1 modulo the selected prime.

At the other place over the same prime, distinct valuation classes give either negative v(G), so G^-1 has residue0, or v(G)=0 with its constant term uniquely minimal, so G^-1 has residue1. Hence W^-1 has residue1 at the successful place and0 or1 at the other; T has unit residue1 or2. At an inert prime the trace of residue1 is2. Therefore B has positive odd valuation1 at selected primes. Away from them the unchanged construction has even v_p(R), and T²(1+R)² has even valuation. B has square reduced denominator. New zeros of sums or of1+R require no additional finite-support hypothesis because they appear through those squares.

At p=2,3,17, all new leaf powers have uniform lower valuation bounds on the already fixed neighborhoods. The accepted R construction has v_p(E)=5(nu-v_p(A)) tending to positive infinity as denominator divisibility nu increases. All exponents2,4,8,19,79,158 are positive. Thus every nonconstant term tends uniformly to zero, W tends to1, and T tends to2. The squareclass identity B/R=1/[T²(1+R)²] preserves the required local classes. The exact valuation of B tends to positive infinity as in accepted372, so the same preparation-zero thresholds hold. These divisibilities are chosen before the contact primes. The scalar conditions are preserved by the same h modulo L.

At each real embedding all complete-witness terms after the constant are nonnegative. This includes high fourth powers and primary squares; no sign of an unsquared test is assumed. For sufficiently large positive lambda, E>0 tends to zero and the test functions and their fixed powers are uniformly bounded on the chosen compact neighborhood. Hence G_j>=1, W>0, T>0 and T tends to2. The same B is asymptotic to1/[4(A*lambda)^5] and tends to zero positively. One common sufficiently large lambda gives0<B<17 for all three detectors. The unchanged preparation-zero and normalized pole realization supply fresh pole witnesses for those B values. No new real restriction is imposed on the integer input or on the old scalar construction.

Thus every integer input has a full rational witness. The proof establishes equality of input projections, not fixed detector-witness equivalence. There is no extra condition on quantified variables and no strengthening of the published arithmetic assumptions.

## Checks and status

Run `python -B verify332.py` in this directory. It imports no builder. It verifies all57 new equations against independently written formulas, all removed-coordinate consumers, every unchanged residual and retained coordinate record, the normalized middle/high square identities, and the cached alternate-power formulas. It checks each odd residue class as finite confirmation of the universal argument and independently expands the full primitive SOS. All5764 coefficients match; all332 coordinates are active. C-independent coefficients have at most1520 bits and the old C-dependent terms are unchanged, proving the stated coefficient bound without expanding C.

The capacity search in the parent directory suggested four groups by allowing ordinary squares and primary leaves to be raised selectively. Its answer was only a grouping relaxation and omitted weight gates. The actual count above includes every shared square and all three new E4 gates. It improves on the separate340 construction by eight coordinates, but those two savings are not additive. Independent review of this exact332 packet, its exceptional branches, common-place implication, and simultaneous completeness is still required. The next manuscript threshold below300 has not been reached.
