# Independent acceptance of four-group332

I accept the frozen 332-variable candidate below on the inherited arithmetic inputs of accepted366. It has the same rational input projection, 331 existential witnesses, 302 quadratic residuals and 5,764 quartic monomials. Its degree is four, content is one, and maximum coefficient is `16*3^(2^26)`.

Reviewer: `/root/astra_quartic_opt05_anchor`, November 7, 2026. The changed construction was authored by `/root/astra_quartic_opt03_depth`. I did not author it. This is an independent review of the present component, not a fresh review of every external arithmetic theorem or ancestor component. It does not approve a later330 candidate, an anchor composition, a decimal companion, a manuscript or publication. No author file was changed.

## Frozen scope and evidence

Paths are relative to `work/`.

| Artifact | SHA-256 |
|---|---|
| `quartic-under300-20261107/01-elimination/s-odd366/candidate366-ir.json` | `0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56` |
| `quartic-under300-20261107/03-depth/review366/REVIEW.md` | `409e919e31b68f8efa7c2ec8cac441c20720b118456988cd7978e74a6e4708e2` |
| `quartic-optimization-20261107/resume-depth-20261107/four-groups/REPORT.md` | `a23811d6368fea51e5f9a8ed9fc5fdf5908fce7e77470f204cd4c764967c1cfa` |
| `quartic-optimization-20261107/resume-depth-20261107/four-groups/candidate332-ir.json` | `27dfc0e11bcdaceb2c71b6562bb3e9a0f3dfd5147338a4a4ffd14d1f53ba4c63` |
| `quartic-optimization-20261107/resume-depth-20261107/four-groups/polynomial332.json` | `601f2695bcf5d28d927406dfa9d75e3dc1a3f30381c22780f88732c9109d39dc` |

I read the proposal and its implementation, the actual source/candidate rows, the accepted366 parity and sign-restoration proof, squared-H reconstruction and its independent review, the primary squared-output identities, the372 contact-pole proof and review, and the369 conditional guard review. The pinned Version13 manuscript supplies the original simultaneous choice and real-neighborhood arguments at lines20631–20663 and21447–21479; the retained root-height argument is at `v9:cor:scales` and `v9:eq:height-transfer`. `SOURCE-PINS.json` records these exact files. The manuscript's older order12 statement is not mistaken for the current order10 interface: the accepted source reductions supply that interface, with an unchanged, stronger completeness construction.

The independent `check.py` imports no producer or other checker. It checks all57 new residuals733–789 against separate formulas, all49 deleted-coordinate incidence lists, all91 removed rows, every surviving outside row/coordinate and non-status metadata field, all18 literal cache definitions, all three retained Laurent-power circuits, and every coefficient of the primitive sum of squares. It also verifies the actual affine test normalizations, the generic pre-H slope and primary fourth-power polynomial identities, all odd residue classes and every subset of zero summands, and the global scalar sign symmetry. `CHECKS.json` records the results. The finite calculation passed; it is evidence for the exact realization, not a substitute for the following arithmetic argument.

## Actual meanings and domains

Work in `K=Q(rho)`, `rho²=2`, `D=11-6rho`. For each detector the unchanged physical contact circuit gives `R=F5(A*lambda)` for its same positive rational square scale A. The retained equation `ER=1` gives E and R nonzero everywhere. The checked toric rows then give `c=R³`, `E8=E^8`, `E19=E^19`, `E79=E^79`, `E158=E^158`; each new gate gives `E4=(E²)²`. These meanings do not need a trace, a nonzero test or a contact prime.

The primary leaves are `P_i=v[255+2(i-1)]+2rho*v[256+2(i-1)]`. The unchanged biquadratic identities give `P_i=r_i^4` and the analogous alternate squared output `g_i^4`, including r_i=0 or g_i=0. The necessary root denominator a_i is nonzero: a_i=0 would force `b_i²=-D` at a real embedding. The polynomial fourth-power identities use only this root/conic chart, not an H point, logarithm or integer index. Their coefficient-by-coefficient expansions are included in the independent checker.

For each ordinary alternate cache, with literal squared leaf `x+2rho*y`, the stored pair q satisfies

    q0=x²-(1056/193)xy+8y²,
    q1=x²-(193/33)xy+8y².

Its affine conjugate fourth-power output is

    Z=(37249q0-34848q1)/2401 + rho*25476(q1-q0)/2401.

The retained higher pair satisfies `p0=37249q0²+34848q1²`, `p1=-50952q0q1`. Consequently

    Z²=(72097p0+101904p1)/5764801
         -rho*(50952p0+72097p1)/5764801.

This is the literal T_j used for j=0,2,3,4. V1 uses the first Z formula. The checker derives these identities from the actual low and high cache rows, including both components and their normalizations. All divisions are by fixed nonzero rationals. No new point denominator or log approximation is assumed.

The other squares are also the actual stored values. In particular the input-error square uses `beta=204(v0+v248)+2555` and equals

    v307-6v232+6beta-9 + rho*(2v308-6v233),

not the unadjusted historical square pair. The Lucas square is `1-2v253+v319+rho*(4v320-4v254)`. The new high fourth powers are the squares of these correctly normalized square outputs. Thus the mathematical tests and the tests consumed downstream are identical.

## Valuations before interpreting H

At each consumed p>76176, K is unramified and D is a unit. A finite point on `y²=x(x²-D)` has even v(x): positive v(x) gives `2v(y)=v(x)` and negative v(x) gives `2v(y)=3v(x)`. Hence reciprocal abscissae also have even valuation.

For the special V0 cache, this point fact must not be assumed before reconstructing H. On the squared-H branch `U*Q_H!=0`, the retained equations reconstruct f,F with `f²=U`, `F²=V`, `fF=v²`, `v=ft`, and `F=ft²`. The exact slope identity checked here gives `f*S²+D*f²=1` from the Kummer equation, without dividing by `c+D*f`. Therefore `(1/f,S/f)` is a genuine finite curve point even if that latter expression vanishes. Even v(f), together with fF=v², gives even v(F) when F is nonzero. If F=0 its powers are zero. Thus T0 has valuation in16Z or infinity before claiming F=f(H-P).

If U=0, the retained equations instead force `V=1/c²`, a unit at every consumed place. If Q_H=0, they force `U=V=-v²` with v equal to `(3+2rho)/4` or `(-36+16rho)/49`, also units at every such place. Their explicit denominators and norms establish the assertion separately at both places over split primes. T0 is a unit in both exceptions. U itself has even valuation or is zero. The other H and M square outputs are literal field squares in every branch.

It follows that the four groups' nonconstant valuations have multiplicities and E exponents

| Groups | (multiplicity, exponent) |
|---|---|
| G0,G1 | (2,79), (4,158), (8,4), (16,8) |
| G2 | (2,19), (4,158), (8,4), (16,8) |
| G3 | (2,19), (4,2), (8,4), (16,8) |

These are valid before either exceptional branch has been excluded. For G0 the first multiplicity uses U directly on those branches; it does not posit a nonexistent square root of negative U.

## One common place, zeros and consumers

Fix a prime in any required positive-contact radical. Its unchanged contact data give odd `alpha=v_p(R)>0` and `1+R` a unit. After multiplication by the inverse of odd alpha modulo16, the four nonconstant valuation classes are the odd classes, 2 modulo4, 4 modulo8 and 8 modulo16. Together with the constant's class0 they partition all16 classes. This holds because odd multiplication preserves each relevant 2-power subgroup. Omitting zero summands preserves disjointness. Every G is therefore nonzero and has its unique minimum summand valuation, at most zero.

The actual product W is consequently nonzero. The retained norm equation first implies Re(W) and z nonzero; only then define `T=Tr(W^-1)=1/z`. Put `Lambda=max_w v_w(W)`. Trace integrality gives `v_p(T)>=-Lambda`. The unchanged B row gives

    B=R/[T²(1+R)²],       v_p(B)<=alpha+2Lambda.

The valuation of B is odd. The retained normalized/factored pole obstruction excludes a negative odd valuation, so `Lambda>-alpha/2`. At a place attaining Lambda, each of the four group valuations is at least Lambda because the others are nonpositive. Each of its summands is at least the group valuation. Thus every nonzero summand in every group is greater than `-alpha/2` at this same place.

For high squares weighted79 this gives `v(H)>39.25alpha`, hence at least40. For high fourth powers weighted158 it gives `v(H)>39.375alpha`, hence at least40. Middle squares weighted19 give `v(M)>9.25alpha`, hence at least10. For P1²,P2²,P3² and Z1 the 8-divisible valuation exceeds3.5alpha and is at least8; P4's 4-divisible valuation exceeds1.5alpha and is at least4; every T_j's16-divisible valuation exceeds7.5alpha and is at least16. Thus each original low-order reciprocal-abscissa test has valuation at least2. Zero powers imply zero original field values and satisfy the same lower bounds. No places from different groups are combined.

On either pre-H exception the unit T0 contradicts this positive valuation. Therefore all three radicals would equal1. The unchanged root-height theorem gives `Bmax²-6<7*Hcal`; independently the scalar parity/anchor gives `Bmax>=|a|>(40*Hcal)^10`. These conflict for Hcal>=1, without using H, a log quotient or the scalar height upper bound. The global sign map needed to restore the source366 odd-index witnesses remains an exact symmetry of every new row, as the independent checker confirms. Hence this anchor use is available on the actual332 system.

After H reconstruction, the later fixed H/V0 exceptions are excluded by the same renewed tests and pre-ratio height argument. The unchanged log comparison, Lucas order40, input order10, scalar order24 and three-scale height arguments now receive exactly their accepted inputs. A radical-free detector contributes only a vacuous divisibility statement. No global inversion of W, T or1+R is asserted there; in particular the previously allowed R=-1/W=0 auxiliary branch is not silently removed. These facts establish soundness on the same arithmetic hypotheses.

## Completeness with the original progression

Use the source366 construction for a fixed integer input, retaining its order of choices. Fix scalar data, the initial H, odd roots and scales, the finite continuity neighborhoods/modulus, and a compact real subneighborhood avoiding the comparison poles. All comparison functions and their finitely many powers are then uniformly bounded before choosing denominator divisibility and contact primes. The source separation identities allow

    h=0 mod Pi^19*M_minus,
    h=1 mod M_plus,
    h=h0 mod L.

The positive solution progression remains dense in the required real component and reaches the fixed neighborhood at arbitrarily large indices. It gives primary formal depth20 and alternate formal membership at their respective places. The actual comparison errors have at least the retained high order40 and middle order10. The opposite-place conditions supply the conjugated alternate tests at the successful primary place. Formal reciprocal abscissae have valuation at least2, including those needing only order1. Nothing requires formal depth40.

Each selected contact prime has alpha=1. The four new nonconstant terms in each group have valuations at least1,2,4,8 respectively: `2*40-79=1`, `4*40-158=2`, `4*2-4=4`, `8*2-8=8`, and in G3 `2*10-19=1`, `2*2-2=2`. Therefore every G is1 modulo that prime at the successful place. At the other place the disjoint classes make G inverse have residue0 or1. The full inverse product has residue1 at the successful place and0 or1 at the other. Its trace is a unit with residue1 or2 (residue2 in the inert case). The newly computed B therefore has positive valuation1 at every selected prime of that detector.

Away from these primes the same source construction gives even v_p(R). The new trace and `(1+R)` enter only through rational squares, so all negative valuations of B are even. New prime divisors of the group sums or1+R require no additional late support conditions. Real positivity below ensures these rational denominators are nonzero in the constructed witnesses.

At2,3,17 the new powers have fixed lower valuation bounds on the previously selected neighborhoods. All E exponents are positive, so increasing the allowed denominator divisibility makes every nonconstant term tend uniformly to zero. Thus W tends to1 and T to2. The source local squareclasses are preserved by `B/R=1/[T²(1+R)²]`, while `v_p(B)=5*(nu-v_p(A))-2v_p(2)` eventually exceeds every retained preparation-zero bound. These choices precede the contact primes, and the final H congruence preserves all scalar finite conditions.

At both real embeddings all new terms on complete genuine points are nonnegative. For large positive lambda, E>0 and each G>=1; the uniform bounds imply W tends to1, T tends to2, and `B~1/[4*(A*lambda)^5]` tends to zero positively. One common allowed lambda gives0<B<17 for all three detectors. The unchanged preparation-zero and factored-normalized pole conversions supply fresh witnesses, including their zero private factors. The same final H supplies the scalar and point equations. This proves completeness for every integer input with no strengthened simultaneous-prime or approximation assumption.

## Exact count and decision

The deletion/addition count is `366-49+15=332`; the residual count is `336-91+57=302`. The newly computed group outputs, trace/B and private pole witnesses need not equal their old counterparts. The result is equality of rational input projections, not a bijection fixing every old witness.

The full independent expansion matches all5,764 coefficients. The unique C² coefficient is16 on `v57²*v549²`; C-linear multipliers are at most96 and C-independent coefficients have at most1,520 bits. No two C powers share the same ordinary coordinate monomial. Thus the exact maximum is16C² without expanding C. No mathematical or implementation defect remains within this frozen component's scope.
