# The scalar anchor already forces S to have odd index

This proposed reduction deletes the three private witnesses of the S odd-index chart from accepted369. The candidate has 366 total rational variables, 365 witnesses, 336 quadratic residuals and 6,527 quartic monomials. Its degree is four, integer content one and maximum coefficient 16*3^(2^26). Independent mathematical review is required. No released or earlier frozen file was changed.

Author: `/root/astra_quartic_opt01_elimination`. This is a new parity argument and an exact global sign normalization. It does not repeat the unsuccessful primary squared-output elimination. The maps preserve the input projection; they need not preserve every retained witness value.

## Frozen files

Paths are relative to `work/quartic-under300-20261107`.

| Artifact | SHA-256 |
|---|---|
| Source `10-combination/candidate369-ir.json` | `b359a64365d05c86ad009b2b93664bd491bc1830e0077383030a0b48556e7095` |
| Source acceptance `01-elimination/review369/REVIEW.md` | `908c25a0676875eef83cbe6fc5a94c152b5fcf94056fcdcf9537adfe73b66d89` |
| Candidate `candidate366-ir.json` | `0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56` |
| Polynomial `polynomial366.json` | `f9219fb79cc687a5af567e6e8cc7b7591ccb1ea4d8f803b7d7189122412e5e64` |
| Producer-free `verify.py` | `15201e21d4f40a1c2d997f19674f151ae0b9c792698b56dbbf96bd2850b83921` |

The only deleted coordinates are70,71,72, and the only deleted rows are690,691,692. These are exactly S.odd.a0, S.odd.a1, S.odd.normRoot and their three equations. Every retained coordinate and residual object is identical. The complete incidence and SOS are checked by `verify.py`, which imports no producer.

The inherited arithmetic source is `quartic_v12.tex`, SHA256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`. The relevant inputs are its squareclass homomorphism and group decomposition around lines19539–19581, reciprocal scalar subtraction including equal-abscissa cases around20385–20445, and the actual anchor equation around20200. The accepted odd-norm component is described in under400 `03-depth/review-odd-norm.md`, SHA256 `f554c3930f8849355d64fc774a935eca169c4fd1d1e0ba35282d8664efe0eaf8`. None of those inputs asserts the new redundancy; it is proved below.

## 1. The base S chart already gives an integral index

Write K=Q(rho), rho²=2, d=3-rho and D=d²=11-6rho. The retained S chart has

    x=h², j²=x²-D, S=(x,hj).

Its physical fields are h=v5+v6*rho, j=v7+v8*rho and x=v84+2*v85*rho. The real embeddings show h!=0: h=0 would imply j²=-D. Thus x!=0 and S is a finite elliptic-curve point.

Use the inherited decomposition E(K)=Z*R0+E[2], with P=2R0 and R0=(1+rho,2rho). The squareclass homomorphism alpha satisfies alpha(R0)=[1+rho], alpha(T0)=[-1], alpha(T_d)=[d]. These three classes are independent: taking norms of a putative square gives (-1)^m*7^f a rational square, forcing m even and f even; the real embeddings then exclude the remaining class[-1].

Since alpha(S)=[x]=[h²]=1, its R0 coefficient is even and its torsion component is zero. Hence S=[a]P for an integer a, without using any odd-chart equation. S is finite and P has infinite order, so a!=0. Oddness has not yet been assumed.

## 2. The scalar reciprocal chart works before parity is known

For the fixed point P=(c,aP*bP), use

    aP=-1+7rho/4, bP=39/8-9rho/2, c=aP²=(57-28rho)/8.

Rows513,514 are exactly the components of

    (c*x+D)*g=aP*j-bP*h,

with g=v543+v544*rho. Both c and x are positive at each real embedding, so the denominator c*x+D is nonzero. The reciprocal subtraction identity therefore identifies

    R_scalar=S-P=[a-1]P,       f(R_scalar)=g².

For x!=c this is ordinary subtraction. If S=P the numerator is zero and contradicts the retained guard g0*tau=1. If S=-P, the same formula gives g²=f(-2P) by the explicit duplication formula; no anchor consequence is needed to handle that case. These cases exhaust x=c. Consequently R_scalar is a nonzero integral multiple of P before proving a odd.

The checker matches the literal scalar rows and verifies the generic reciprocal-abscissa identity without an odd-index assumption. It also checks the retained g0 inverse and the anchor formula. No equation involving H or a detector is used here.

## 3. An even a contradicts the anchor at 3

The curve has good reduction at3: D reduces to2 in F9=F3[rho]/(rho²-2), and the discriminant64D³ is a unit. The literal point P reduces to

    x(P)=rho, y(P)=0, f(P)=2rho.

This is a nonidentity point of order two. If a were even, s=a-1 would be odd, including when s is negative. The reduction homomorphism would then give [s]P reducing to P. Thus f([s]P) is integral with residue2rho. In the unramified basis1,rho its rational coefficient F=f1([s]P) is a3-adic unit, with F=2 modulo3. Since f([s]P)=g², this coefficient is exactly F=2*g0*g1.

The actual rescaled anchor is

    U²+6V²-2W²-12g1²-4C*tau*W=0,   g0*tau=1,
    C=3^(2^25).

Put u=g0*U, v=g0*V, w=g0*W and F=2g0g1. Multiplication by g0² restores

    u²+6v²-2w²-4Cw-3F²=0.

This restoration does not use F!=0 or an old F-inverse. The unconditional polynomial difference is 4C*g0*W*(g0*tau-1), checked exactly. Completing the square gives

    u²-2(w+C)²+6v²=3F²-2C².

Here is a direct local obstruction, avoiding any parity assumption in an anchor-coefficient lemma. For rational u,w', the nonzero value u²-2w'² has even3-adic valuation, because its binary form is anisotropic modulo3. The nonzero value6v² has odd valuation. Their valuations cannot tie, so the valuation of their sum is their minimum. If F is a3-adic unit and C is divisible by3, the right side3F²-2C² has valuation1 and, after division by3, residue1.

The left side can have valuation1 only if v is a unit and u²-2(w+C)² has valuation at least2. After division by3 its residue is then2*v²=2, a contradiction. Zero values of either summand do not change the argument. Therefore a cannot be even. We have proved a is odd before any root-height, H-domain or logarithm argument is used.

The checker verifies the exact reductions of P, the inverse residue2rho, good reduction, and the two finite-field facts used in this obstruction. The valuation argument above, rather than a finite numerical test, supplies the statement for every rational witness.

## 4. Why a sign normalization is necessary

Oddness of the point S alone does not guarantee the old private odd chart for both stored representations(h,j) and(-h,-j). For example these two representations of P can give half-abscissa norm classes-1 and-7. It would be incorrect simply to invoke the odd-point characterization while claiming to fix every outside coordinate.

The candidate has the following exact involution. Negate coordinates

    5,6,7,8, 25,26,27,28, 55,56,57, 120,121, 543,544,549,

and fix every other coordinate, including the input. In words, negate S.h and S.j; the V2 biquadratic fields V,I,W; all three private anchor witnesses; the scalar reciprocal g; and its rational inverse tau. The V2 fields Q,K, all root abscissae, all L/z values, all test squares and all detector quantities remain fixed.

Every retained residual is either fixed or negated by this map. `verify.py` proves this by checking the parity of every monomial in every residual, including all scalar ratio and primary-chart consumers. It records the complete affected-row list and each multiplier in `VERIFICATION.json`. This is a symmetry of the entire candidate, not merely its S subblock. The point S=(h²,hj), its scalar difference and all relevant physical point values are unchanged.

## 5. Reverse and forward maps

Given a full candidate366 solution, first prove a odd as above. Choose the inherited half-point T=[a]R0=(A,B), so2T=S. It is nontorsion, so A and B are nonzero. Since alpha(T)=[1+rho]^a=[1+rho], choose r in K with A=(1+rho)*r².

Define

    t=B/A, h_star=(A²+D)/(2B), j_star=t²/2-x.

The exact duplication identities give h_star²=x and h_star*j_star=y(S). Hence (h_star,j_star) is either(h,j) or(-h,-j). If the second case occurs, apply the global involution from the preceding section. All retained equations still hold and the stored S representation now equals(h_star,j_star).

Reinsert coordinates70,71 as the rational components of A and coordinate72 as Norm(r). The deleted equations are exactly

    A²-2(x+j_star)A-D=0,      Norm(A)+Norm(r)²=0.

The first follows from A*t²=A²-D and x+j_star=t²/2. The second follows from Norm(1+rho)=-1. The checker matches these field equations to the exact three deleted rows. Therefore every full candidate366 solution gives a full source369 solution with the same input. This map may apply the stated involution and chooses a field square root existentially; it is not claimed to be a rational-function bijection fixing all retained witnesses.

Conversely, forget coordinates70,71,72 from any source369 solution. Every retained equation is unchanged, so this is a candidate366 solution with the same input. These two maps prove equality of input projections if the new parity and normalization argument is accepted. Completeness needs no new prime, point or real-neighborhood construction.

## Verification boundary

Run `python -B build.py` and `python -B verify.py` in this directory. The builder reproduces the candidate and polynomial. The producer-free verifier checks complete private incidence, all outside objects, every retained equation under the involution, the literal scalar and anchor interfaces, the generic subtraction identity, local residue facts, deleted odd-chart meanings, and every coefficient of the primitive SOS.

The finite checks pass. The new arithmetic steps requiring independent review are the initial integral-index deduction without the odd chart, the3-adic anchor parity contradiction, and the half-point reconstruction with the global sign normalization. The proposal is not accepted merely by those finite checks and does not meet the below300 release threshold.
