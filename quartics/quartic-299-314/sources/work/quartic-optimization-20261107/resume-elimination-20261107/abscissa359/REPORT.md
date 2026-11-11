# Root parity from retained abscissae

Author: `/root/astra_quartic_opt01_elimination`, 2026-11-07. This is a new research proposal, pending independent review. Released Version13, the frozen362 packet, and all detector packets are unchanged.

The candidate has **359 total variables, 358 witnesses, 329 quadratic residuals and 6416 quartic monomials**. Its degree is four, content one and largest coefficient is `16*3^(2^26)`. It saves seven variables from accepted366. It replaces, rather than adds to, the four-variable saving in the proposed362 anchor. No composition with340 is asserted here.

| File | SHA256 |
| --- | --- |
| Source366 IR | 0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56 |
| Source366 independent review | 409e919e31b68f8efa7c2ec8cac441c20720b118456988cd7978e74a6e4708e2 |
| candidate359-ir.json | 282fbc534713ddf056f1c8ed3d8b6dd933b95cad234fa9367896559e982c78d1 |
| polynomial359.json | a48baf563cfb8b490fdab230dd60079067d7f19f0185ef13bfca22548882af3d |

The source is `work/quartic-under300-20261107/01-elimination/s-odd366/candidate366-ir.json`; its review is `03-depth/review366/REVIEW.md` in the same research tree. The arithmetic source is `quartic_v12.tex`, SHA `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`, especially the group/squareclass discussion and `lem:v12-anchor-coefficient` around lines20115ff. The earlier362 report is relevant history, not independent approval of this new application.

## Exact delta

Write rho²=2, D=11-6rho, P=2R0, C=3^(2^25). For each root point i=A,T,Z let X_i be the rho coefficient of x(i). These are already retained rational expressions:

    X_A=2*v83, X_T=2*v87, X_Z=2*v89.

The physical abscissae are v82+2*v83*rho, 2*v86+2*v87*rho, and v88+2*v89*rho respectively. The factor two in T's real coordinate has no effect on the new expression, which uses only the imaginary coefficient.

Delete the nine private odd-chart coordinates66,67,68,74,75,76,78,79,80 and rows687,688,689,693,694,695,696,697,698. Add only two rational coordinates Q=v903 and B=v904 with equations

    Q=12(X_A²+X_T²)+108X_Z²,
    B=2g1+C*Q*tau.

Here g0=v543, g1=v544 and tau=v549. Keep g0*tau=1. In row504 replace -12g1² by -3B². Thus the anchor becomes

    U²+6V²-2W²-4C*tau*W-3B²=0.

The literal Q row is v903-48*v83²-48*v87²-432*v89²=0. All other residual and coordinate objects are unchanged. Multiplication of the anchor by g0² gives the inherited quaternion criterion with parameter

    t=(g0*B)/C=F_s/C+Q,
    F_s=2g0g1=f1([s]P), s=index(S)-1.

The criterion is valid for every rational t, including zero: rational anchor witnesses exist exactly when t is integral at2 and3. The new consumer is t=F_s/C+Q; no altered local-global theorem is assumed.

## Uniform abscissa valuation before parity

The retained square-abscissa root charts imply A,S,T,Z are nonzero integral multiples of P by the inherited group decomposition and independent squareclasses. They do not need any odd-chart equation for this conclusion. The retained scalar reciprocal chart and g0*tau=1 identify S-P=[s]P with s a nonzero integer. Equal-abscissa subtraction at S=-P uses the source duplication identity; S=P is excluded by the guard. These are the same pre-height facts used in the accepted366 proof.

For any nonzero integer n, write X_n for the rho coefficient of x([n]P). We claim

    v3(X_n)=0                    when n is odd,
    v3(X_n)=-2-2v3(n)           when n is even.       (1)

At3 the curve has good reduction and P reduces to the nonzero2-torsion point (rho,0) over F9. Odd multiples therefore have x congruent to rho, proving the first case. For n=2m with m=3^k*u and u a3-unit, the actual source formal calculation gives

    z([n]P)/3^(k+1) = u(2+rho) modulo3.

The formal Laurent expansion x(z)=z^-2+O(z²), with integral coefficients at3, then gives

    3^(2k+2)*x([n]P) = u^-2*(2+rho)^-2 = 2u^-2*rho modulo3.

The last equality is in F9: (2+rho)^-2=3/2-rho over K, whose residue is2rho. Its rho coefficient is nonzero, proving the second case. This also proves X_n is nonzero; no separate inverse or nonzero assumption is needed. The argument applies equally to negative n.

We need a separate2-adic statement only for completeness:

    v2(X_n)=-1 for odd n.                            (2)

The exact z(P)=(232+86rho)/357 has rational component valuations3 and1. Normalize the ramified field valuation by v(2)=1, so v(rho)=1/2 and v(z(P))=3/2. The integral odd multiplication series gives z([n]P)=n*z(P)+O(z(P)^3). For odd n, the error has field valuation at least9/2, hence rational real component valuation at least5 and rho coefficient valuation at least4. The leading component valuations remain3 and1. If z=a+b*rho with those valuations, then

    coefficient_rho(z^-2) = -2ab/(a²-2b²)²

has valuation1+3+1-2*3=-1. The correction x(z)-z^-2=O(z²) has field valuation at least3, so its rho coefficient has valuation at least3 and cannot cancel that term. This proves (2). Both Laurent and multiplication series are those of the integral Weierstrass model y²=x³-Dx; good reduction at2 is not asserted or required for their integral formal coefficients.

For the scalar coefficient F_n=f1([n]P), the inherited source gives

    v3(F_n)=0 for odd n, and 2+2v3(n) for even n;

it also gives2-integrality for every nonzero n. The odd case follows directly by reducing f to2rho. These facts are applied before knowing s is even, with the odd case included explicitly.

## Reverse map

Start with any rational zero of the new system. The anchor gives t integral at3. The valuation of F_s/C lies in2Z. By (1), each X_i has an even nonpositive valuation. The binary sum X_A²+X_T² is anisotropic modulo3, so its valuation is twice the minimum valuation of X_A,X_T and belongs to4Z. Therefore the three summands

    F_s/C, 12(X_A²+X_T²), 108X_Z²

have valuations in2Z, 1+4Z and3+4Z, respectively. These classes are disjoint. A negative minimum cannot cancel. All three summands are integral, and the last two force v3(X_A)=v3(X_T)=v3(X_Z)=0: a negative even valuation is at most-2 and would give a negative valuation after either shift1 or3. Equation (1) now proves that all three root indices are odd.

We have also proved F_s/C is3-integral. Its2-integrality follows from the scalar point and C being a2-unit. Apply the unchanged quaternion criterion to F_s/C and replace only the three private anchor witnesses by old anchor witnesses. This restores row504 with the original g0,g1,tau. This step uses no H interpretation, detector inequality, root-height theorem or integer-input conclusion.

Restore each deleted odd chart using the inherited half point [n]R0 for the now-odd root [n]P. Its abscissa has norm minus a rational square after the source squareclass choice. The exact doubling formulas give

    A_half²-2(x+j)*A_half-D=0,
    Norm(A_half)+normRoot²=0,

up to the choice of signs of the stored h,j pair. The following complete involutions fix the physical root point and correct those signs when necessary:

| Root | Coordinates negated |
| --- | --- |
| A | 1,2,3,4,21,22,23,24,112,113 |
| T | 9,10,11,12,29,30,31,32,128,129 |
| Z | 13,14,15,16,33,34,35,36,136,137 |

Every new residual is fixed or negated by each involution, as checked on its entire monomial support. The X_i, Q, B, input and physical root points are fixed. Choose the needed signs and insert the nine half-chart witnesses. The result is a complete source366 solution with the same input. This is an existential projection map; it does not claim to fix the old private anchor witnesses.

## Forward map

Start from a source366 solution. Its odd charts make A,T,Z odd multiples of P. By (1), all X_i are3-units, so Q is3-integral. By (2), each X_i² has2-adic valuation-2; both12 and108 have2-adic valuation2. Every summand of Q is therefore2-integral. The old anchor gives F_s/C integral at2 and3. Thus t=F_s/C+Q is integral at both places.

Apply the same quaternion criterion to t, choose its three rational witnesses and divide them by nonzero g0 to obtain U,V,W. Set Q and B to the displayed expressions and discard the nine private odd-chart coordinates. All other source coordinates stay fixed. This gives a new solution with the same input. No stronger choice of primes, labels, real neighborhood or detector precision is required.

## Finite verification and scope

Run build.py then verify.py with Python. The verifier imports no producer. It checks the exact source/output pins, deleted-coordinate incidence, all unchanged objects, physical root normalization, the two new rows, anchor identities, every sign consumer, local starting constants and the full primitive-integer residual sum of squares. All359 coordinates occur. The329 residuals are quadratic in quantified variables; C is fixed. The expansion has6416 monomials. Its only C² coefficients are16 and1; C-independent coefficients have fewer than2048 bits. The exact maximum remains16C² without expanding C's decimal representation.

The ordinary construction adds the inherited16-coordinate C chain and one shared product C*tau, giving376 variables by an exact circuit prescription. No ordinary coefficient table is supplied or numerically approved here.

The new mathematical obligations are the abscissa coefficient statements (1),(2), their consumption by the three disjoint3-adic classes, and restoration of the original source before any height argument. The earlier362 proposal used three inverse-F1 gates. Those gates are absent here, and its pending review does not approve this change. Independent review is required before composition or acceptance. The below300 publication threshold is not reached.
