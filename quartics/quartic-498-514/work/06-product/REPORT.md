# Scalar norm reduction to 518 variables

This candidate replaces the scalar norm tree in the 523-variable system. It has 518 total variables, 517 witnesses, 487 quadratic residuals, and a degree-four sum of squares with 35,031 monomials. The fixed coefficient remains S = 3^(2^26). The content is one and the largest absolute coefficient remains 64 S^2. The algebra checker passed. The new arithmetic argument below requires independent review; this report does not claim that review has occurred.

## Exact source and scope

The baseline is `quartics/quartic-523-540/final523_540/symbolic523/candidate-ir.json` in the supplied repository. Its hash is recorded in `candidate518-ir.json`, under `variant.baselineSha256`. The relevant source passages are manuscript `quartic_v11.tex`, lines 10422-10558, the scalar32 bridge; lines 10912-10950, its source equations; and the Version 9 addition, especially `lem:v9-bridge`, `v9:sec:labels`, and `subsec:v9-completeness`. All point charts, guards, the physical anchor, finite correction, detector products, height scales, and asymmetric logarithm equations are retained.

Only scalar rows 481-493 are removed, and row 495 is rewritten to attach the new root to the existing scalar pole input. Coordinates 515-527 are removed. Eight new coordinates 540-547 and eight new rows 608-615 replace them. The original inverse guard r != 0 remains, as do the scalar pole preparation equations that force b != 0. The two coefficients of f(S-P) remain because the physical anchor consumes them.

This is a change to the arithmetic certificate, not an algebraic equivalence between the old and new scalar trees. Soundness and completeness must be established anew for that block. The inherited arithmetic theorems retain their existing qualifications.

## New equations

Write R = S-P = [s]P with s = a-1, and H = [h]P. Let

    f(H) = f0 + f1 sqrt(2),
    z(R)/z(H) = z0 + z1 sqrt(2),
    r = beta(beta-1)(beta-2401)(32 beta+343)(2 beta-1),
    beta = 2 X^2+3.

The retained inverse chain supplies i32 = r^(-32). Introduce eight rational coordinates q,A,U,V,V2,B,B2,W and impose

    q = f0^2 - 2 f1^2,
    r(A-1) = q^2,
    U = z0 i32,
    V = z1 i32,
    V2 = V^2,
    B = U^2 + r V2,
    B2 = B^2,
    W = A^2 + r B2.

The existing coordinate `scalar.W2.quadratic` has a fixed nonzero rational scale k. Replace its old defining row by k * scalar.W2.quadratic = W^2. All later equations continue to impose exactly b = c r W^2, with the original correction c and original pole predicate. The builder reads k from the pinned baseline semantic value, so it does not guess this large normalization constant.

Equivalently, with N_r(u,v)=u^2+r v^2, the new tree is

    W = N_r(N_r(1,q/r), N_r(z0/r^32,z1/r^32)).

The input coordinate X is unchanged.

## Local soundness of the new tree

Fix any consumed rational prime p > 76176. The finite correction c is a p-unit. Put rho = v_p(r), which is odd at these primes by the same contact computation used in the original scalar proof. Let v = v_p, normalized by v(p)=1. Since the scalar pole predicate forces the odd valuation of b to be positive,

    rho + 2 v(W) > 0.

At every norm node, the two nonzero summands have opposite valuation parity, so their valuations cannot cancel. Zero summands cause no problem, with valuation +infinity. The constant leaf follows the all-left path. Thus if rho < 0, v(A) <= 0 and v(W) <= 0, contradicting the displayed inequality. Hence rho > 0 and v(W) > -rho/2.

Descend the two levels. The left node has v(A) > -rho/4; its right leaf q/r has valuation > -5rho/8. The right node has v(B) > -3rho/4; its leaves U,V have valuations respectively > -3rho/8 and > -7rho/8. Consequently

    v(q) > 3rho/8 > 0,
    v(z0) > (32-3/8)rho,
    v(z1) > (32-7/8)rho.

As rho is a positive odd integer and rational valuations are integral, v(q) >= 1 and v(z0),v(z1) >= 32.

## One suitable place is enough

The rational number q is Norm_{K/Q}(f(H)), with K=Q(sqrt(2)). At p>76176 the extension is unramified. If p splits, v_p(q) is the sum of the two local valuations of f(H). If p is inert, it is twice its single local valuation. Since v_p(q)>0, there is at least one place w above p with v_w(f(H))>0. Hence H is formal at w, with t=v_w(z(H))>=1. Both rational coefficients of z(R)/z(H) have valuation at least 32, so

    v_w(z(R)) >= t+32 > 0.

We do not need R itself to be formal. The following doubling calculation is the reason the two old f(R) leaves can be omitted.

For the curve y^2=x^3-Dx, with D=(3-sqrt(2))^2 a unit at w, write m=v_w(x(R)). The retained point domains give x(R), y(R) nonzero. Since

    z(R)^2 = x(R)/(x(R)^2-D),

positive valuation of z(R) excludes m=0. If m>0 then v_w(z(R))=m/2. If m<0 then v_w(z(R))=-m/2. The exact duplication formula is

    x([2]R) = (x(R)^2+D)^2 / (4x(R)(x(R)^2-D)).

For either sign of m, its valuation is -2 v_w(z(R))<0. Thus [2]R is formal and

    v_w(z([2]R)) = v_w(z(R)).

The numerator and denominator in this calculation cannot vanish when m != 0: D is a unit and the competing terms have unequal valuations. Also [2]R is nonidentity since s != 0 and P has infinite order. No omitted torsion or zero-denominator case is being filled by an arbitrary quotient witness.

The formal logarithm is a homomorphism and isometry on these unramified odd-prime formal groups, exactly the same source application as the original bridge. The global identity

    [h]([2]R) = [2s]H

gives

    v_p(h) + v_w(z([2]R)) = v_p(s) + v_w(z(H)),

because 2 is a p-unit. Therefore v_p(s/h)>=32. Since h is a nonzero integer, v_p(s)>=32.

This proves M_5(beta)^32 divides a-1, the sole downstream divisibility conclusion of the old six-leaf scalar tree. The exponent-19 height theorem and the unchanged physical anchor consequently give the same scalar bound and the same two final height contradictions. All remaining soundness arguments are unchanged.

## Completeness

For integral X, repeat the original scalar preparation: r is a nonzero integer; choose c, a sufficiently divisible positive h0, and a still deeper sufficiently divisible positive s=a-1, with the same physical anchor and all parity requirements. The old proof can make every original normalized leaf integral at p dividing r and divisible by p at p dividing c but not r. Those choices are stronger than needed here.

At p dividing r, both coefficients f0,f1 have valuation at least v_p(r), so q/r is integral. The two retained ratio leaves are integral. The constant-left tree has A=1 modulo p and W=1 modulo p. At p dividing c but not r, all original nonconstant leaves are divisible by p, so q/r and the retained ratio leaves are divisible by p, again W=1 modulo p. Hence the new W is a unit on the support of cr and is nonzero. The new b=crW^2 is positive, has square reduced denominator, and has exactly the same local squareclasses at 2,3,17 as cr. The existing pole-completeness lemma supplies fresh pole witnesses for this b.

After the roots are fixed, the new scalar functions are continuous at the chosen shared point. The same sufficiently small congruence neighborhood of h0 preserves the finitely many valuation conditions. The global prime selection, asymmetric formal depth, and real progression arguments therefore still construct complete witnesses. This constructs a solution for every integer X; it does not assume the old scalar pole witnesses work for the new b.

Together with soundness, the candidate has the same exact Z-in-Q projection, conditional only on the inherited manuscript results already used by the 523-variable source. The changed local argument introduces no prime-pattern assertion or arithmetic conjecture.

## Checks and reproduction

Run from this directory, with Python 3 and Node available:

    python -B prepare_tools.py
    python -B build_candidate.py
    python -B verify_candidate.py
    python -B compile_ir_s26.py candidate518-ir.json polynomial --no-reduce
    node checker_s26.cjs --input candidate518-ir.json --compiled polynomial/compiled-ir.json --certificate polynomial/reduction-certificate.json --coordinate-map polynomial/coordinate-map.json --quartic polynomial/polynomial.json --report independent-check.json

`prepare_tools.py` makes local copies of the repository compiler and independent algebra checker, changing only their historical S exponent from 27 to 26, including the corresponding integer exponent constant. The original files are not edited. The candidate explicitly marks all noninput coordinates as residual-system coordinates, not gates, because it does not claim a gate-program equivalence for the altered arithmetic certificate. The independent checker reports zero gate identities and checks the actual quadratic residual system, row normalizations, SOS coefficients, support, content, and coefficient bound.

`verify_candidate.py` independently checks that all retained baseline rows are exact, reconstructs the eight new equations and new W-squared attachment, verifies the duplication numerator identity, and checks the valuation bounds for a finite range as a regression test. Its finite valuation test supports the displayed proof; it is not a substitute for it.

The generated sparse polynomial is `polynomial/polynomial.json`. `independent-check.json` records the successful exact algebra checks. `polynomial/compiler-report.json` records all counts. No expanded giant integer is needed.

## Other product directions considered

The odd-product height identity itself cannot be replaced by its field norm using that identity alone. The source proves a common weak valuation sign at each individual place, not a common sign between two split places. A field norm can cancel their contributions. Likewise a fixed positive rational quadratic combination of the two product coefficients has rational fibers with unbounded denominator height, so its positivity alone supplies no replacement for both height scales. This candidate leaves that part untouched and uses a norm only for the weaker local existential conclusion that at least one place is formal.
