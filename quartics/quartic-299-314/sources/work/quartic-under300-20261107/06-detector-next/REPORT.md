# Three tests in one fourth-power valuation sum

Author: `/root/astra_quartic_opt06_product`. This candidate reduces accepted366 to354 total rational coordinates, with324 quadratic residuals and5903 quartic monomials. It changes the arithmetic detector, rather than preserving its old rational fibers. Independent arithmetic review is pending. The released manuscripts and all predecessor packets are unchanged.

## Frozen inputs and outputs

| Object | SHA256 |
| --- | --- |
| `../01-elimination/s-odd366/candidate366-ir.json` | `0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56` |
| `candidate354-ir.json` | `cf62d9dc594e037e26d2569563f36a4d51a02197b7a3285740338441981e121a` |
| `polynomial354.json` | `3d159cab0b036eea9c4321d5bbb7f1a29727b2ad8baae85bf7e5eef44535189c` |

The current366 source is independently reviewed in `../03-depth/review366/REVIEW.md`, SHA `409e919e31b68f8efa7c2ec8cac441c20720b118456988cd7978e74a6e4708e2`. Its scalar parity restoration is unchanged. The detector construction used here is `../10-combination/unweighted372/REPORT.md`, accepted by `../01-elimination/review372/REVIEW.md`, SHA `3e5a5fe8a14025979b27bbb45c55f35d55c0237082f4fd7a299babc9b3e9d997`, with the conditional guard removal in `../10-combination/REPORT369.md`. The new argument below proves the changed local step in full.

The squared-H branch classification is `../01-elimination/squared-h/REPORT.md`, whose frozen candidate390 has SHA `c986ee02f33aef0cf729bfbd73e590ac9672941be6c8f92dc3f389247daeaced`, and acceptance `../03-depth/review390/REVIEW.md` has SHA `61b755da24b3934ca8725159ac96c59c8b5090a4c7a032fe5487646853e7a667`. The retained eight primary/difference square-output identities are proved in `../../quartic-under400-20261107/02-squares/point-charts/biquadratic/REPORT411.md`. They are consequences of unchanged quadratic rows and require no H interpretation. These inherited inputs retain their existing acceptance status; this report does not author a new acceptance record for them.

Published arithmetic inputs are unchanged. The inherited manuscript source is `quartic_v12.tex`, SHA `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`, specifically its one-place and radical/height argument around lines11038 onward and simultaneous-prime/real construction around11217 onward. This proposal adds only the elementary valuation lemma proved below and replaces one internal detector application. It does not appeal to a new external theorem.

## Exact quadratic construction and physical bindings

Let K=Q(rho), rho squared=2, and D=(3-rho)^2. For each existing detector let R=F5(A*lambda), E=1/R, where F5 and all three scales A are unchanged. The existing coordinates already supply E squared and E cubed and use them in the E^19/E^79 weight circuit. Keep those coordinates, all higher-order factors, every later product, the norm equation and the pole rows.

Write the nine order-one leaves as Y=f^2 with their existing conjugations. Replace each group of three old factors by

    G(Y1,Y2,Y3)=1+E*Y1+E²*Y2+E³*Y3.

This is a K-valued equation with two rational quadratic components. The three ordered groups are

    [conjugate(f(V0)^2), f(U1)^2, f(U2)^2],
    [conjugate(f(V1)^2), f(U3)^2, f(U4)^2],
    [conjugate(f(V2)^2), conjugate(f(V3)^2), conjugate(f(V4)^2)].

Their literal coordinate expressions, in that order, are

    [v178−2rho*v179, v255+2rho*v256, v257+2rho*v258],
    [v190−2rho*v191, v259+2rho*v260, v261+2rho*v262],
    [v196−2rho*v197, v208−2rho*v209, v220−2rho*v221].

For detector0 the E,E²,E³ coordinates are350,361,362, and the three outputs are634+rho*635,636+rho*637,638+rho*639. For detector1 the powers are398,409,410 and outputs654..659. For detector2 they are446,457,458 and outputs674..679. All downstream multiplication and mixed-order rows retain these exact output interfaces.

Delete coordinates608..611,614..617,620..623. These are the two old K-valued elementary coefficient outputs per triple. Delete their twelve defining rows568,569,571,572,574,575,577,578,580,581,583,584. The eighteen changed rows are595..600,617..622,639..644. Their exact ordered leaves and powers are in `CERTIFICATE.json` and independently reconstructed in `verify.py`. There are no other consumers of deleted coordinates. Every retained row outside these eighteen is byte-for-byte the corresponding source object, and every remaining coordinate object is unchanged.

The complete new W is the product of these three G values and all unchanged order10/order40 factors. The same retained equations are

    Norm(W)=2*Re(W)*z,
    B*(R+E+2)=z².

Thus whenever W is nonzero these imply Re(W) and z are nonzero, T=Tr(W^-1)=1/z, and B=R/[T²*(1+R)²]. The proof at a required contact prime below establishes these domains before using this formula. At real complete witnesses they follow from positivity.

## Valuations of the actual leaves

Here is a direct elementary lemma. At a place above p>76176, the field K is unramified and 2D is a unit. Normalize the discrete valuation by v(p)=1. For a genuine finite point on

    y²=x*(x²−D)

with x nonzero, v(x) is even. If v(x)>0, the second factor is a unit, so2v(y)=v(x). If v(x)<0, the x² term strictly dominates D, so2v(y)=3v(x), again forcing v(x) even. For v(x)=0 the conclusion already holds. Consequently v(f)=−v(x) is even, and v(f²) is divisible by4. The same holds at a conjugate place and therefore for conjugated leaves. A zero f or leaf is treated as valuation infinity and contributes no term; no division by it is made.

The eight Ui/Vi leaves with i=1..4 are actually fourth powers already, before constructing H. The unchanged scaled biquadratic identities give YUi=(V_i/a_i)^4 and YVi=(Q_i/a_i)^4, with a_i nonzero from its retained root equation. This gives divisibility by4 even on their identity branches, independently of any later index or logarithm claim.

For V0, use the exact squared-H classification before applying a detector. In its generic branch U and Q_H are nonzero, the displayed rational formulas in the squared-H report recover f=fH, F and the source Kummer equations. Here f is nonzero, fF=v², and the retained affine S expression satisfies S²=1/f−D*f. Thus x=1/f, y=S/f is a genuine point on y²=x*(x²−D), and the elementary lemma gives even v(f). If F is nonzero, then v is nonzero and v(F)=2v(v)−v(f) is even. If F=0, its leaf is zero. Consequently the leaf conjugate(F²) has valuation in4Z or is zero. This argument does not require F to have the meaning f(H−P): that interpretation may await the exclusion of the later c*x(H)+D=0 branch. No height or logarithm conclusion is used here. In the branch U=0, the V0 leaf is the conjugate of1/c² and is a unit at every consumed place. In the branch Q_H=0 it is the conjugate of−v² for either fixed value v=(3+2rho)/4 or v=(−36+16rho)/49. Each is a unit at these places. Thus its valuation is0, still divisible by4, on both exceptional branches. A fourth root of these exceptional leaves is neither asserted nor needed.

## Local detector implication and exceptional branches

At a prime in any required positive-contact radical, alpha=v(R)>0 is odd, and1+R is a unit. For each packed G, its nonzero terms have valuations

    0, 4k1−alpha, 4k2−2alpha, 4k3−3alpha.

These are pairwise distinct modulo4 because alpha is odd. After omitting zero leaves, there is a unique minimum, so G is nonzero and its valuation is exactly that minimum, in particular nonpositive. This is the only new local argument. All unchanged higher-order factors have nonconstant term of odd valuation, so they too are nonzero with nonpositive valuation. Their classified minus signs on the H exceptional branch do not alter this fact.

Consequently W is nonzero at a required contact prime and hence in K. Its retained norm row forces Re(W) and z nonzero. Put Lambda=max_w v_w(W) over places above p. Integrality of trace gives v_p(T)>=−Lambda. Thus

    v_p(B)=alpha−2v_p(T)<=alpha+2Lambda.

This valuation is odd. The unchanged pole obstruction excludes negative odd valuation, so v_p(B)>0 and Lambda>−alpha/2. Choose a place attaining Lambda. Since each factor has nonpositive valuation, each G has valuation at least Lambda. Every nonzero Yj term of this G then has valuation greater than−alpha/2. Hence

    v(Yj)>(j−1/2)*alpha, for j=1,2,3.

Since alpha>=1, these are positive valuations. Their divisibility by4 gives v(Yj)>=4 and v(fj)>=2, which implies the required order-one condition v(fj)>=1. Zero leaves already satisfy that condition. For the unchanged order10/order40 factors, the original same-place argument gives their original orders at this very same place. No differing successful places are combined.

On U=0 or Q_H=0, the first group's V0 leaf has valuation0, contradicting this implication at every prime in any required radical. Thus all three radicals must be1 on either branch. The unchanged pre-H root-height/anchor contradiction then excludes both branches, exactly as in accepted390 and accepted366. This uses the parity/anchor restoration of366, which does not depend on an H point or these detector outputs. It uses neither the scalar height upper bound nor a logarithm quotient. After the branch exclusion, the genuine H reconstruction and all subsequent local comparison, logarithm, Lucas, height and scalar arguments receive the identical required test orders. Therefore every new witness has integer input by the inherited proof.

This argument is conditional on a prime belonging to a required radical. It does not claim that all arbitrary rational solutions have W nonzero when every radical is empty. It retains the guard-free369 treatment of that case; none of the old removed inverse guards is silently restored.

## Simultaneous completeness

Use the same point/root/scale choices, initial finite neighborhoods, contact-prime construction and final H progression as accepted372. The new low-order leaves are the same functions on these points. At every selected contact prime for this detector, v(R)=1 and at the designated successful place the inherited construction gives v(fj)>=1. The elementary even-valuation lemma improves this to v(fj)>=2, so v(Yj)>=4. For j=1,2,3 the term E^j*Yj has positive valuation. Thus every G has residue1 at the successful place.

At the other place, the distinct-modulo4 argument applies without a success hypothesis. If G has valuation0, its constant term is the unique minimal term and G has residue1. If G has negative valuation, G^-1 has residue0. Therefore G^-1 has residue0 or1 at that place. The unchanged higher-order inverse factors have the same property. The inverse full product W^-1 consequently has residue1 at the successful place and0 or1 at the other. The retained trace T has residue1 or2, is a unit, and B has positive odd valuation1. At an inert prime there is just the successful place and the residue of its field trace is2, also a unit. All selected primes exceed the fixed exceptional-prime bound.

Outside selected contact primes, the same global construction gives even v_p(R). The denominators T² and(1+R)² alter valuation by even integers. Hence B has square reduced denominator, since its only odd valuations are positive at selected primes. New prime divisors of the rational sums G create only even valuation contributions through T². They need no prior finite support restriction.

At p=2,3,17 retain the old fixed point neighborhoods and their uniform bounds v(Yj)>=−c_p. With the denominator divisibility parameter nu freely enlarged after these bounds, accepted372 gives v(E)=5*(nu−v_p(A)) tending to positive infinity. Every new term E^j*Yj for j>=1 tends to0 uniformly. Hence each G tends to1 and T tends to2 with arbitrarily large precision. R and B have exactly the same local squareclasses as in372 because B/R is a rational square. The valuation identity v(B)=−v(R)−2v(T) still gives the same preparation-zero thresholds. This uses the existing order of choices; no finite neighborhood is chosen after the contact primes.

At each real embedding the leaves are squares and are nonnegative on genuine complete witnesses. For large positive lambda, R~(A*lambda)^5>0 and E>0. Thus every new G is positive and1+O(lambda^-5), uniformly in the same bounded real H neighborhood. The unchanged factors have the same behavior. Therefore W is positive at both embeddings, T=2+O(lambda^-5) is positive and nonzero, and B~1/[4*(A*lambda)^5]. For one sufficiently large lambda all three new B values satisfy0<B<17 simultaneously. The same preparation-zero lemma and exact normalized pole conversions provide the new pole witnesses. The scalar conditions and all other rows still use the same final H, since their neighborhoods and progression were untouched.

This constructs a full witness for each integer input. The new detector outputs, z,B and pole witnesses are recomputed; they are not asserted to equal their old values. Combining this completeness argument with soundness proves the same exact integer projection, subject to independent review of this packet and its stated inherited dependencies.

## Finite verification and scope

`verify.py` imports no producer. It pins the source and candidate, writes each of the eighteen expected quadratic rows directly from the physical Y expressions, checks all deleted-coordinate consumers, compares every other row and coordinate, checks degree and coordinate coverage, and independently forms the full primitive SOS using upper-triangular products. It matches every coefficient of `polynomial354.json`. The quartic has integer content1 and maximum coefficient16*3^(2^26). Finite odd-alpha residue checks are only sanity checks; the universal proof is the distinct-residue argument above.

The initial alternative identity using A(E)^2+E*B(E)^2 for a triple gives no saving in its direct realization. Four K-valued outputs per evaluation replace one, while shared elementary inputs still cost two K pairs and missing unsquared tests need recovery. E²/E³ are already required by the weight circuit. This negative finding concerns that direct realization only. No general circuit lower bound is claimed.
