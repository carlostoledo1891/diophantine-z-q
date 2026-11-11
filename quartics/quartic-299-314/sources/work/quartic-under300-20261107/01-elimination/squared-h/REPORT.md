# Squared H Kummer presentation

Author: `/root/astra_quartic_opt01_elimination`. This is a proposed two-coordinate reduction from accepted392t. It is not independently accepted. All earlier candidates and the frozen Version13 release remain unchanged.

The candidate has 390 total rational variables, 389 witnesses, 360 quadratic residuals and 6989 quartic monomials. It has degree four, integer content one and maximum coefficient 16*3^(2^26). The larger monomial count buys two fewer coordinates. The below-300 target is not reached.

## Frozen artifacts and source

| Object | SHA-256 |
|---|---|
| Source `03-depth/candidate392t-ir.json` | `846660e49d0cef6d0f7d562625adcf9ffb72c00542bc5c666fca93dbb363d1ba` |
| Source review `01-elimination/review392t/REVIEW.md` | `054a137adf03fa23f58ecb1f75e2365d2e2a32f0382d6da4cb3d3949edfb2923` |
| `candidate390-ir.json` | `c986ee02f33aef0cf729bfbd73e590ac9672941be6c8f92dc3f389247daeaced` |
| `polynomial390.json` | `c9fce25cf9d1bdbe9ff488236d79c6ad56dfc4c86d09e550fbcf274128073bc7` |

The accepted392t source reconstructs accepted394, whose mathematical review is under400 `03-depth/integrated394/REVIEW.md`, SHA `0d2be6af0bde35995ca0dfa6334aab1368ea298fd6974a4a231478f34c3c080f`. The underlying manuscript is `quartic_v12.tex`, SHA `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`. The new branch argument below uses the proof of `lem:v5-one-place` at lines11038–11068, the pre-ratio root-height implication `v9:eq:height-transfer`, and the independently restored scalar anchor from the accepted394 review. It does not assume that the source one-place lemma already covers arbitrary nonsquare leaves.

## Equations and exact interface

Work over K=Q(rho), rho squared=2, with D=11-6rho and fixed P=(c,ab), where

    a=-1+7rho/4, b=39/8-9rho/2, c=a^2=(57-28rho)/8,
    b^2=c^2-D.

The source392t has f=fH, F=fV0, v and t, with

    c*(f+F)+D*v^2+2*b*v=1, v=f*t, F=v*t.

Its stored square outputs are U=f squared and V=F squared. U is coordinate311+2*coordinate312*rho; V is coordinate178+2*coordinate179*rho. The factor two in each second component is essential. The only consumers of f and F are these square definitions and the three displayed field equations.

Delete the pair F at160/161 and repurpose the former f pair140/141 as W. Keep v700/701 and t142/143 unchanged. Define the fixed affine expression

    Q=(1-D*W-2*b*v)/c.

The four new field equations are

    W=v^2,                U*V=W^2,
    Q^2=U+V+2*W,          t*(U+W)=Q*v.

They are quadratic because Q is affine. All other coordinate objects and residuals are unchanged. In particular every old S consumer still uses the source affine expression S=(b+c*t+D*v)/a. No new substitution is made in a logarithm, ratio, detector or scalar-pole row.

## Reconstruction on Q,U nonzero

Set

    f=(U+W)/Q,       F=(V+W)/Q.

Writing E=UV-W squared and H=Q squared-U-V-2W, the exact polynomial identities are

    (U+W)^2-U*Q^2 = -U*H-E,
    (V+W)^2-V*Q^2 = -V*H-E,
    (U+W)*(V+W)-W*Q^2 = -W*H+E.

They give f squared=U, F squared=V and fF=W=v squared. The sum equation gives f+F=Q. Since U!=0, f!=0; the last new equation gives ft=v, and then F=v*t. The definition of Q restores the source Kummer equation. Thus every source392t residual is recovered, fixing every outside coordinate.

Conversely take a full source392t solution. Set W=v squared and retain its square outputs U=f squared,V=F squared. Since fF=v squared, all four new equations hold with Q=f+F. The source has f!=0. Also Q cannot vanish: F=-f would give v squared+f squared=0, impossible at a real embedding unless f=v=0. Hence Q,U are nonzero. The reverse formulas recover f,F, and the maps are inverse on full solution sets once the two new exceptional branches below have been excluded.

## The two possible new branches are fixed

If U=0, UV=W squared gives W=0 and W=v squared gives v=0. Then Q=1/c and V=1/c squared. This branch has no presumed H point or logarithm interpretation. Its actual low-order V0 detector leaf is the conjugate of V, a unit square at every consumed place because c and its inverse are integral outside2 and41.

If Q=0, the first numerator identity implies U=-W. The sum equation then gives V=-W. Since W=v squared, both newly free square outputs are negative squares,

    U=V=-v^2,       D*v^2+2*b*v-1=0.

The fixed relation b squared+D=c squared gives exactly

    v=1/(c+b)=(3+2rho)/4,
    or v=-1/(c-b)=(-36+16rho)/49.

Indeed c+b=12-8rho has norm16, and c-b=(9+4rho)/4 has norm49/16. Each v is therefore a unit at every place above p>76176. These placewise unit statements follow from the displayed denominators and norms of the integral building blocks, not from a norm-only cancellation argument at split primes.

## Signed one-place argument, only on the fixed branches

Here is the precise extension of the source proof needed for Q=0. Suppose every factor of the retained detector product has the form

    1+epsilon_j*R*(D_j/R^m_j)^2,

where epsilon_j is +1 or -1, D_j lies in K, the source nonzero product/trace guards hold, and the same pole certificate holds for B=R/Tr(product^-1)^2. At an unramified consumed prime put alpha=v_p(R), assumed odd. For D_j!=0 the nonconstant summand has the nonzero odd valuation alpha+2(v(D_j)-m_j*alpha), unchanged by epsilon_j. Thus the factor valuation is its minimum with zero. For D_j=0 the factor is1. Every factor valuation is nonpositive.

Let lambda be the maximum product valuation over the places above p. Integrality of trace gives v_p(B)<=alpha+2lambda. Its valuation has the odd parity of alpha. The same pole obstruction excludes negative odd valuation, so alpha>0 and lambda>-alpha/2. At a place attaining lambda every factor has valuation at least lambda. Therefore

    v(D_j)>(m_j-3/4)*alpha >= m_j-3/4,

and integrality gives v(D_j)>=m_j; a zero D_j already satisfies the conclusion. This is the full source valuation proof with unit signs retained. It uses no square root of an arbitrary nonsquare field element and no stronger arithmetic input.

Apply it only after assuming Q=0, where the new U and V are demonstrably -v squared. Use D_H=v with sign minus for the order40 H leaf, and conjugate(v) with sign minus for the order1 conjugate V0 leaf. All other test outputs remain actual squares: the unchanged root/biquadratic charts recover their f-square outputs without H, and the other cross/input/Lucas test-square equations square their stored field expressions even before those expressions have ratio meanings. They have sign plus. The actual high-order U factor is explicitly checked in each of the three detector evaluations. The signed conclusion forces positive valuation of the unit v, a contradiction.

On the U=0 branch use the ordinary, unsigned version: take the H test value zero and the conjugate V0 test value 1/conjugate(c). All other tests are squares as above. The actual low-order factor is checked in all three detector products, including its optimized cubic coefficient with V treated as an arbitrary field element. The conclusion forces positive valuation of the unit 1/conjugate(c), again a contradiction.

These contradictions show that no prime can lie in any of the three height contact radicals on either branch. The required product, trace and pole nonzero domains belong to the unchanged three height-detector blocks; their proof needs no H or logarithm interpretation. No scalar pole is used in this step.

## Closing the branch exclusion before H is defined

With all three radicals equal1, the unchanged root-height implication with N=1 gives

    Bmax^2-6 < 7*Hcal.

The four odd root points remain unchanged. The scalar root, its reciprocal g0 guard and rescaled anchor are also unchanged. As in the accepted394 review, they identify a nonzero even scalar index independently of H, use the unconditional coefficient lemma to restore f1 and its inverse, and restore the old anchor. Thus

    Bmax >= |a_index| > (40*Hcal)^10,      Hcal>=1,

which contradicts the preceding bound. This argument uses no scalar height upper bound, scalar W positivity, H coordinate, or logarithm quotient. It establishes Q!=0 and U!=0 first. Only then do the rational formulas reconstruct all of392t and permit its full soundness argument to be applied.

Completeness simply maps every old complete witness forward as above. There is no new choice of points, real neighborhood, prime, correction, or pole witness. The candidate therefore has the same integer input projection if the new branch argument is independently accepted.

## Exact evidence and remaining review

`verify.py` imports no producer. It checks the complete incidence of the four removed/repurposed coordinates, every outside object, all four new field equations, the three reconstruction identities, fixed branch constants and norms, and the actual high- and low-order factors in all three height detectors. In the low-order cubic check V is arbitrary; it is not silently substituted by a field square before verifying the identity. The full primitive SOS matches every coefficient of `polynomial390.json`.

All coordinates occur. The term count has no collisions between different C powers on one coordinate monomial. The unique maximum term remains 16*C squared*W_anchor squared*tau_anchor squared, with no lower-C contribution there; other C-linear multipliers are at most96 and constant coefficients have fewer than2048 bits. No huge coefficient is expanded.

The finite checks pass. Independent mathematical review must specifically audit the signed-factor one-place proof, its restricted use on Q=0, the actual two detector factors, and the pre-H availability of the anchor/height contradiction. This report is the author's proposal, not its approval. Run `python -B verify.py` to reproduce `VERIFICATION.json`; `build.py` reproduces the candidate and polynomial.
