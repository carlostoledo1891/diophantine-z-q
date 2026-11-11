# Kummer replacement for the auxiliary H abscissa

This candidate saves two rational coordinates from accepted394. It has392 total variables,391 witnesses,362 quadratic residuals and6366 quartic monomials. It has not received independent arithmetic acceptance. No release file or earlier frozen packet was changed.

The change replaces the H/V0 equations by a Kummer relation and removes the H abscissa pair. It keeps every logarithm, ratio, test, scalar value and root unchanged. The possible new branch f(H)=0 is excluded using the already retained order-one test on conjugate f(V0), before any logarithm ratio is interpreted. No lower truncation depth or stronger prime theorem is assumed.

## Frozen artifacts

| Object | SHA256 |
| --- | --- |
| Source `work/quartic-under400-20261107/10-combination/combined394-ir.json` | `7eb02f9913b55d60a790a287616f1bb80d9f93523e9f11e12481c9ab955746a5` |
| `candidate392-ir.json` | `72cc362707f6c87ebcbd1ed2dc88ec0631791f39e261356a78b7ae2f98457550` |
| `polynomial392.json` | `da6e8172570d1a1803d5e9d3009de8322df01927bb6ca79ddc18bedb38d35ebf` |

The accepted source composition is reviewed in `work/quartic-under400-20261107/03-depth/integrated394/REVIEW.md`, with its predecessor argument in `integrated395/REVIEW.md`. In particular the latter explains which height and detector conclusions are available before ratios. The unchanged arithmetic source is `work/quartic-version6-release/repository/manuscripts/quartic_v12.tex`, SHA256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`. Relevant inputs are `lem:v5-one-place`, `v9:eq:height-transfer`, and `lem:v12-anchor-coefficient`.

## Actual old and new equations

Work over K=Q(rho), rho^2=2. Put D=(3-rho)^2. The fixed P chart is P=(c,ab), with a=-1+7rho/4, b=39/8-9rho/2, c=a^2=(57-28rho)/8, and b^2=c^2-D. These are fixed field constants, not extra coordinates.

Write f=fH, F=fV0, v for the existing rescaled difference parameter, and S for the existing negative reciprocal of z(H). The source equations are

    x*f=1,
    S^2=x-D*f,
    (c*x+D)*v=a*S-b,
    v^2=f*F.

The physical x is v90+2*v91*rho; f is the pair140,141; F the pair160,161; S the pair142,143; v the pair700,701. Delete90,91. Replace the first three field equations by

    c*(f+F)+D*v^2+2*b*v=1,
    a*f*S=b*f+(c+D*f)*v.

Keep v^2=fF. These are three quadratic field equations in place of four, so the reduction is exactly two rational coordinates and two rational equations. The V0 logarithm equation is unchanged, including its N=aS-b and Tprime=-2D-abS+2Dbv expressions.

## The polynomial identity

For scalar indeterminates define

    d=c+D*f,
    B=b*f+d*v,
    A=a*f*S-B,
    E=v^2-f*F,
    K=c*(f+F)+D*v^2+2*b*v-1,
    H=f*S^2+D*f^2-1,
    R=b^2-c^2+D.

When c=a^2, the following is an unconditional polynomial identity:

    c*f*H = f*d*K+c*d*E+R*f^2+A*(a*f*S+B).

`verify392.py` checks it in independent indeterminates over Q. For the fixed P constants R=0. Thus if the new equations hold and f is nonzero, H=0 because c is nonzero. Set x=1/f. The old H curve equation follows from H=0; the old difference equation follows by dividing the new A equation by f. Every source equation is then restored, with every outside coordinate fixed.

Conversely, in a full accepted394 solution f is nonzero, and the accepted pre-ratio exceptional-H exclusion gives c*x+D nonzero. Therefore d=f*(c*x+D) is nonzero. The old equations imply H=A=E=0, and the identity yields K=0 by division by f*d. Forgetting x gives a new solution. The scalar denominator d is used only in this forward implication from the already accepted full source. In the reverse implication no division by d is needed.

The only remaining issue is to prove f nonzero for every full new solution. The following argument does that before using the source H-domain or logarithm argument.

## Excluding the new zero branch

Suppose f=0 in a new full solution. The retained equation v^2=fF gives v=0 because K is a field. The new Kummer equation then gives F=1/c. This is a fixed field value:

    F=8*(57+28*rho)/1681.

Both c and 1/c are integral outside2 and41, and are inverses there. Thus F and its conjugate are units at every place over every consumed p>76176.

The actual detector leaves still include conjugate F at order one for each of the three height detectors. This is checked from the literal final equations, not inferred from the coordinate name. The old `logV0.fSquare` rows give the stored square components178=F0^2+2F1^2 and179=F0F1. Hence u=(178,-2*179) is conjugate F squared. The order-one group0 coefficient equations form the elementary symmetric functions of u and the two other stored squared leaves. The optimized cubic coefficient uses the unchanged w^2 values but is identically their triple product. Finally the actual evaluation equations in all three detectors are

    1+(u+p+q)*t+(up+uq+pq)*t^2+(upq)*t^3
      =(1+u*t)*(1+p*t)*(1+q*t).

`verify392.py` derives both elementary symmetric coefficients, checks the optimized cubic after substituting the actual F-square and w-square equations, and matches these three evaluation pairs. All remaining detector circuit equations are unchanged. The accepted detector interpretation therefore supplies exactly the factor for the order-one test conjugate F, including on this new branch.

The one-place lemma applies to arbitrary field test values and explicitly permits zero values of other tests. Its nonzero detector products, traces and pole inputs are established in the unchanged detector block. It does not require an H point or interpretation of LP. Consequently a prime in any of the three contact radicals would force positive valuation of conjugate F at some place, contradicting its unit value. All three contact radicals must equal one.

The unchanged root-height implication then gives Bmax^2-6<7*Hcal. The scalar anchor is independently available here: the unchanged S root and scalar reciprocal g0 guard give a nonzero even scalar point; the unconditional coefficient lemma restores the f1 inverse and the old anchor exactly as in the accepted394 review. None of that argument involves H or fH. Therefore Bmax>=|a_index|>(40*Hcal)^10, contradicting the preceding height bound.

This excludes f=0 without assuming that H is already defined, without a scalar height upper bound, and without any denominator logarithm. It also works if the scalar W or pole input were to vanish on the hypothetical new branch, since their positivity is not an input to this contradiction. Only the three unchanged height-detector pole blocks are used.

## Soundness, completeness and exceptional cases

For every new rational solution, the previous argument proves f nonzero. Restoring x=1/f recovers the entire accepted394 system coefficient for coefficient. Its soundness applies, so the input is an integer. This restoration also proves all later nonzero H/V0 denominators by the accepted argument; they are not assumed earlier to exclude f=0.

For every integer input, take a complete394 witness. The accepted H-domain argument establishes its nonzero f and d. The polynomial identity proves the new Kummer equation. Forget x and keep all other values. This supplies a new witness with no change to the real/local/CRT construction, scalar depth24, labels, logarithm approximations, or half-index conventions.

The maps are inverse on full solution sets, since x is uniquely1/f. No new witness or guard is introduced. The reverse algebra remains valid even if d=0; it then recovers an old full solution and the accepted source exclusion rules that branch out. Individual values of S,v or other parameters need not be divided by in the new-to-old map. In particular this proof does not silently use the old positivity of the H abscissa.

## Exact finite result and review boundary

`build392.py` writes the candidate. `verify392.py` is a separately written check of this author's formulas, not a non-author review. It passes the complete90/91 incidence, every unchanged outside record, actual new field rows, the universal recovery identity, the literal conjugate-F detector factor, and the full primitive SOS. The source has six rational rows involving90 or91 and no other consumers. The candidate has392 variables,362 rows and6366 monomials.

The maximum coefficient remains16*C^2 on W_anchor^2*tau^2. The new rows have no C. All constant coefficients have fewer than2048 bits, all C-linear multipliers have magnitude at most96, and the constant/linear contribution to that maximum monomial remains zero. No enormous integer is expanded.

Independent review is required particularly for the new pre-H zero-branch exclusion and its use of the unchanged zero-tolerant height detectors and independently available scalar anchor. This is a concrete two-coordinate proposal, not a claim to have reached the below300 target.
