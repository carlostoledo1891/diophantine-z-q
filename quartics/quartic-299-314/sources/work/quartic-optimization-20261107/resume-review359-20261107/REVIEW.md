# Independent acceptance of the 359-variable abscissa reduction

I accept this exact reduction from accepted366 to candidate359, on the inherited arithmetic inputs of accepted366. The two systems have the same rational input projection. No unresolved mathematical or implementation gap was found in this component.

The candidate has 359 total rational variables, 358 existential witnesses, 329 quadratic residuals, and 6,416 quartic monomials. Its degree is four, its integer content is one, and its largest absolute coefficient is `16*3^(2^26)`.

Reviewer: `/root/astra_bl_horizontal_repair`, November 7, 2026. Author: `/root/astra_quartic_opt01_elimination`. I did not author this reduction or its precursor constructions. My preceding independent362 review does not automatically approve this changed application. I checked the new local coefficient statements and reran all finite checks on the actual359 artifacts. This is internal mathematical acceptance of the component, not a fresh proof of the inherited global arithmetic theorems, human peer review, or release approval. Author files, predecessor reports, the repository, and controllers remain unchanged.

## Exact files and independent check

The author directory is `work/quartic-optimization-20261107/resume-elimination-20261107/abscissa359`.

| Artifact | SHA-256 |
|---|---|
| Author `REPORT.md` | `23f95faa9d5cafbbf571f67c6050b0d86bd17f778f74737372b76e0aff9ffebe` |
| `candidate359-ir.json` | `282fbc534713ddf056f1c8ed3d8b6dd933b95cad234fa9367896559e982c78d1` |
| `polynomial359.json` | `a48baf563cfb8b490fdab230dd60079067d7f19f0185ef13bfca22548882af3d` |
| Source366 IR | `0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56` |
| Source366 author proof | `e2a482e2f08712c6375bfaca4fea78bea35034727946c582ce7b3dde02608c7b` |
| Source366 independent review | `409e919e31b68f8efa7c2ec8cac441c20720b118456988cd7978e74a6e4708e2` |
| Inherited `quartic_v12.tex` | `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9` |
| This directory's `check.py` | `171810c64a1bbd3cef40fd44d53e778509a86f558604dbc11b227691b867933a` |
| This directory's `CHECKS.json` | `3fd92f33c699302350e3482d662e16aeda3900ff8b4515491b50cea58d3c8eb8` |

The source366 files are in `work/quartic-under300-20261107/01-elimination/s-odd366`, and its independent review is `work/quartic-under300-20261107/03-depth/review366/REVIEW.md`. The arithmetic source is `work/quartic-version6-release/repository/manuscripts/quartic_v12.tex`.

I read the actual source366 projection proof, its independent review, the source369 composition proof, the earlier odd-norm-chart proof, and the manuscript's group/squareclass, scalar reciprocal, coefficient, and quaternion arguments during the immediately preceding362 audit. Those exact source hashes remain bound and were rechecked here. I read the complete new359 argument and both author scripts, and checked the actual new and source residuals. The relevant manuscript locations are lines 19539–19581, 20115–20213, and 20385–20445.

This directory's `check.py` is adapted from my independent362 checker, not from an author checker. It imports no producer or other checker. It reruns the complete source comparison, literal identities, sign maps, and coefficient expansion against359. It writes only the local `CHECKS.json` and verifies that every author file has the same hash afterward. It passed under `C:/Users/glaze/.local/bin/python3.14.exe -B check.py`.

## What is available before the new parity test

Keep K=Q(rho), rho^2=2, D=11-6rho, E:y^2=x^3-D*x, R0=(1+rho,2rho), and P=2R0. Each unchanged root chart gives x=h^2 and j^2=x^2-D. Real embeddings exclude h=0. The inherited decomposition `E(K)=Z*R0+E[2]` and independent squareclasses of 1+rho, -1, and 3-rho then imply that A,S,T,Z are nonzero integral multiples of P. No odd-chart equation is needed for this implication.

The retained scalar reciprocal equations and g0*tau=1 identify

    g=g0+g1*rho, g^2=f(S-P), f=1/x,
    S-P=[s]P, s=index(S)-1 != 0.

The source identification works before parity. The denominator c*x+D is positive at both real embeddings. S=P forces g=0 and is excluded by the guard. S=-P has the exact duplication value f(-2P); it is not treated as an arbitrary exceptional output. The independent checker matches the literal scalar equations to their physical S-coordinate expressions.

These initial facts require neither an H interpretation, a height bound, detector acceptance, nor a conclusion about the distinguished input.

## New three-adic abscissa coefficient statement

For a nonzero integer n, let X_n be the rational rho coefficient of x([n]P). The claimed formula is correct:

    v3(X_n)=0                    if n is odd,
    v3(X_n)=-2-2*v3(n)            if n is even.

At three, the curve has good reduction over the unramified quadratic field, and P reduces to the nonidentity point of order two with abscissa rho. Odd multiples therefore have abscissa congruent to rho. This proves the first assertion and nonvanishing for odd n, including negative n.

For even n, put r=1+v3(n). The actual source formal-group computation gives

    z([n]P)/3^r = u*(2+rho) modulo 3,
    f([n]P)/3^(2r) = rho modulo 3,

where u is a 3-unit. Inverting the second congruence gives

    3^(2r)*x([n]P) = 2*rho modulo 3.

Thus the rho coefficient has exact valuation -2r. This independently confirms the author's Laurent-series argument. More explicitly, the inherited lemma gives rational coefficients f0,f1 with v3(f1)=2r and v3(f0) at least 2r+1. The terms of `Norm(f)=f0^2-2*f1^2` have unequal valuations, so its valuation is exactly 4r. Since `X_n=-f1/Norm(f)`, its valuation is -2r. There is no hidden cancellation in extracting the rational coefficient.

The author's leading constant is also exact: `(2+rho)^(-2)=3/2-rho`, whose residue is 2*rho. The checker independently doubles R0 and P, verifies the source z(2P), and checks the normalized abscissa residue. The argument applies to every even nonzero index; a finite computation at 2P alone would not prove that universal statement.

Consequently every X_n is nonzero and has a nonpositive even three-adic valuation. This is derived from the unchanged point chart and group input, rather than from a new inverse guard or an assumed odd index.

## The new two-adic statement and the formal correction

For odd n, the claimed value v2(X_n)=-1 is correct. At the ramified place above two, normalize v(2)=1. The exact parameter

    z(P)=(232+86*rho)/357

has rational coefficient valuations 3 and 1 and field valuation 3/2. The integral odd multiplication series gives

    z([n]P)=n*z(P)+O(z(P)^3).

For odd n, the error has field valuation at least 9/2. Its rational real coefficient has valuation at least 5 and its rho coefficient at least 4. Thus the rational components a,b of z([n]P)=a+b*rho retain valuations 3 and 1. Negative odd n causes no exception.

The norm a^2-2*b^2 has valuation exactly 3, since its summands have valuations 6 and 3. Therefore

    coefficient_rho(z^(-2))=-2*a*b/(a^2-2*b^2)^2

has valuation 1+3+1-6=-1.

The correction can be controlled by an exact identity, without relying only on notation for an asymptotic expansion. From z=-x/y and y^2=x^3-D*x,

    z^(-2)=x-D/x, hence x-z^(-2)=D*f.

On the formal branch f has leading term z^2. This follows directly from the integral equation `w=z^3-D*z*w^2`, with w=-1/y, and f=w/z. Thus v(f)=3 for these odd multiples. Since D is a unit at two, D*f has field valuation 3. Its rational rho coefficient has valuation at least 3, because the two component valuations are an integer and a half-integer and cannot tie. It cannot cancel the valuation-minus-one coefficient of z^(-2). This proves v2(X_n)=-1.

No good-reduction assertion at two is needed. The integral formal neighborhood of the identity on the stated Weierstrass model suffices. The same exact identity also justifies the Laurent correction used at three.

## Actual normalization and quadratic replacement

The retained square-chart equations imply the physical abscissae

    A: v82+2*v83*rho,
    T: 2*v86+2*v87*rho,
    Z: v88+2*v89*rho.

Thus the physical rho coefficients are X_A=2*v83, X_T=2*v87, X_Z=2*v89. The checker derives these from each actual h^2 row, including T's exceptional real scaling.

The new rows are exactly

    Q=12*(X_A^2+X_T^2)+108*X_Z^2
     =48*v83^2+48*v87^2+432*v89^2,
    B=2*g1+C*Q*tau, C=3^(2^25),
    U^2+6*V^2-2*W^2-4*C*tau*W-3*B^2=0.

Only coordinates and rows 903,904 are added; no inverse-coefficient coordinates 900,901,902 remain. The nine private odd-chart coordinates and rows are removed exactly as in362, and row504 is the only changed retained row. Every other source coordinate and residual object is identical.

Multiplication of the last equation by g0^2, with g0*tau=1, gives the original translated quaternion form with numerator g0*B. Its parameter is

    t=(g0*B)/C=F_s/C+Q, F_s=2*g0*g1=f1([s]P).

The checker verifies both identities against the actual guard. C and g0 are nonzero. No division by X_i, B, g1, or F_s is hidden in the new equations.

## Reverse implication, cancellation, and restored depth

Any rational candidate solution gives t integral at three by the inherited universal quaternion criterion. For the scalar coefficient, the inherited even-index lemma and the odd reduction give

    v3(F_s)=0 for odd s, and 2+2*v3(s) for even s.

In particular F_s is nonzero, and v3(F_s/C) is even without first assuming s even. The three summands

    F_s/C, 12*(X_A^2+X_T^2), 108*X_Z^2

have valuations in 2Z, 1+4Z, and 3+4Z. The second assertion uses anisotropy of x^2+y^2 modulo three, so its valuation is twice the minimum of the two X-valuations before the weight is applied. Each X_i is nonzero by the uniform formula; the binary sum is also nonzero over Q. Therefore all three valuations are finite and pairwise distinct. The least one cannot cancel, regardless of the real sign of F_s. An all-zero or t=0 branch is impossible on this derived domain.

Every summand must consequently be integral. A negative X_A or X_T valuation is an even integer at most -2 and makes the paired weighted term have valuation at most -3. A negative X_Z valuation makes its weighted term have valuation at most -1. Hence all three X_i are 3-units, and the three root indices are odd.

We also recover v3(F_s/C) at least zero. The retained scalar point gives 2-integrality of F_s, by the source formal-subgroup argument for all integral multiples, and C is a 2-unit. Thus F_s/C is integral at both required places. The same quaternion criterion now supplies original anchor witnesses with the same g0,g1,tau. The literal incidence check confirms U,V,W have no consumer outside row504.

Before any height or domain argument, the recovered scalar bound forces s even and

    v3(s) >= 2^24-1,
    s in 2*3^(2^24-1)*Z with s != 0.

Thus S is also odd, the old scalar depth is restored, and S=-P is excluded because it would have s=-2. No root-height theorem has been used to obtain one of its own parity premises.

## Sign choices and complete old366 restoration

For an odd root [n]P, choose its half [n]R0=(a,b). The inherited squareclass calculation gives a=(1+rho)*r^2 for some r in K. The point is nontorsion, so a,b are nonzero. Set

    h_star=(a^2+D)/(2*b), j_star=(b/a)^2/2-x.

Duplication gives h_star^2=x and h_star*j_star equal to the stored ordinate. The stored pair h,j is therefore either the starred pair or its simultaneous negative. The following complete involutions provide the necessary choice:

| Root | Negated coordinate IDs |
|---|---|
| A | 1,2,3,4,21,22,23,24,112,113 |
| T | 9,10,11,12,29,30,31,32,128,129 |
| Z | 13,14,15,16,33,34,35,36,136,137 |

My checker transforms every monomial in every actual359 residual. Each row is fixed or negated; all affected rows and multipliers are recorded in `CHECKS.json`. The involutions fix the input, all physical root points and abscissae, X_A,X_T,X_Z, Q,B, the scalar data, and the anchor witnesses. They also preserve the restored original anchor. The three sign choices can be made independently.

Insert a's two rational components and Norm(r) in the deleted slots for each root. They satisfy the exact old equations

    a^2-2*(x+j_star)*a-D=0,
    Norm(a)+Norm(r)^2=0.

The first follows from b^2=a^3-D*a and the displayed formulas; the second uses Norm(1+rho)=-1. The checker verifies the generic denominator-cleared duplication identities and all nine literal old equations, with the physical coordinate scales. We now have a complete old366 witness with the same input. Only at this point is old366 soundness consumed. The map is existential and permits the stated sign changes and new private anchor witnesses.

## Forward implication and local-global completeness

Start with any complete old366 solution. Its odd-norm charts force A,T,Z odd. The new three-adic formula makes their X_i 3-units, so Q is 3-integral. The two-adic formula gives v2(X_i^2)=-2. Since both 12 and 108 have two-adic valuation 2, each weighted square is 2-integral, as is their sum. These assertions require no change to the old root labels or point choices.

The old anchor gives F_s/C integral at two and three. Therefore t=F_s/C+Q is integral at both places. Apply the identical source quaternion criterion to t. For clarity, if its standard-form rational solution is u0,v0,w0, the actual rescaled coordinates are

    U=C*u0/g0, V=C*v0/g0, W=C*(w0-1)/g0.

The C scaling and affine translation of w are part of this use of the criterion; merely dividing a standard-form solution by g0 would omit them. With these exact coordinates, the candidate anchor holds. Set Q and B as above and discard the nine old half-chart witnesses. Every other equation is preserved.

This use of Hasse–Minkowski or the equivalent quaternion embedding criterion has exactly the same scope as the inherited source: every rational t integral at two and three is admitted. The associated real form is indefinite, so there is no added real sign or size restriction on t. No other local integrality condition is introduced. The criterion already includes t=0, though the noncancellation argument rules it out here. The anchor variables are private, so selecting new rational witnesses imposes no extra real, prime, CRT, detector, or approximation requirement elsewhere.

These maps prove equality of rational input projections directly with366. This is a replacement for the362 packing, not an additive saving or a literal forgetful map from arbitrary362 witnesses.

## Finite results and acceptance boundary

The independent checker verified source pins, complete deletion incidence, absence of the three inverse coordinates, all outside objects, physical scales, both new rows, both anchor identities, the scalar reciprocal interface, all sign consumers, generic duplication, local starting constants, and every coefficient of the full primitive-integer sum of residual squares. All359 coordinates occur. The count is 366-9+2=359 variables and 336-9+2=329 residuals.

The full expansion agrees with all 6,416 monomials in the supplied table. Every residual is at most quadratic and the polynomial has exact degree four. Its C-independent coefficients already have gcd one, so content one persists after C is specialized. Distinct symbolic terms have distinct ordinary coordinate monomials. The C-squared coefficients are exactly 16 and 1, the C-linear multipliers have absolute value at most 96, and all C-independent coefficients have fewer than 2048 bits. Hence the largest coefficient remains exactly 16*C^2.

The ordinary376 count is valid as a circuit prescription. The inherited sixteen-coordinate chain fixes C, and one coordinate qTau=C*tau keeps both qTau*W and qTau*Q quadratic. No ordinary coefficient table is supplied or accepted here.

The finite checks do not prove the imported Mordell–Weil or global arithmetic results. The local arguments and witness constructions above prove the new application conditional on those same inherited inputs. Within that scope, this exact359 component is accepted. No composition with another pending reduction, minimum-variable claim, or release authorization follows from this review.
