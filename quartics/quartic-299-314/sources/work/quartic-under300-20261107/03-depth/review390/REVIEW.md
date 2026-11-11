# Independent acceptance of squared H candidate390

Accepted for the exact frozen candidate below, on the inherited arithmetic inputs. It has the same rational input projection as accepted392t, hence defines the integers over Q. There are390 total variables,389 witnesses,360 quadratic residuals and6989 quartic monomials. The degree is four, content one and maximum coefficient16*3^(2^26).

Reviewer: `/root/astra_quartic_opt03_depth`. Author of the new equations and branch proof: `/root/astra_quartic_opt01_elimination`. I previously identified the square-only outside-consumer pattern as a possible target and authored the source392t change. I did not author the new four-equation squared presentation or its signed-factor exclusion proof. This review checks that new application independently, including its physical realization.

## Exact scope

Paths in this table are relative to `work/quartic-under300-20261107`.

| Artifact | SHA256 |
| --- | --- |
| Source `03-depth/candidate392t-ir.json` | `846660e49d0cef6d0f7d562625adcf9ffb72c00542bc5c666fca93dbb363d1ba` |
| Source acceptance `01-elimination/review392t/REVIEW.md` | `054a137adf03fa23f58ecb1f75e2365d2e2a32f0382d6da4cb3d3949edfb2923` |
| Author `01-elimination/squared-h/REPORT.md` | `18682f8f61cbf7642e074a7e47641fb91aa1023b8c81c29edf233ca232d4f02a` |
| Result `01-elimination/squared-h/candidate390-ir.json` | `c986ee02f33aef0cf729bfbd73e590ac9672941be6c8f92dc3f389247daeaced` |
| Polynomial `01-elimination/squared-h/polynomial390.json` | `c9fce25cf9d1bdbe9ff488236d79c6ad56dfc4c86d09e550fbcf274128073bc7` |

I read the author's proof and actual old/new equations, and rechecked the source one-place proof, root-height implication and unconditional scalar-anchor restoration. The source manuscript is the previously pinned `quartic_v12.tex`, SHA256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`. The relevant applications are `lem:v5-one-place`, `v9:eq:height-transfer`, and `lem:v12-anchor-coefficient`, together with the accepted394 anchor reconstruction. The new argument does not require a new published theorem. The extension from squares to signed squares is proved below rather than silently attributed to the old statement.

## Reconstruction and exact squared outputs

Use the same fixed K=Q(rho), rho^2=2, P=(c,ab), c=a^2 and b^2=c^2-D. In source392t the local block is

    c(f+F)+D*v^2+2*b*v=1, v=f*t, F=v*t,
    U=f^2, V=F^2.

The existing output meanings are U=v311+2*v312*rho and V=v178+2*v179*rho. I derived these from the literal old square rows. The imaginary coefficient is twice the named stored coordinate in each case.

The new rows are W=v^2, UV=W^2, Q^2=U+V+2W and t(U+W)=Qv, where Q=(1-DW-2bv)/c. They reuse140/141 as W and delete160/161. The generic identities checked independently are

    (U+W)^2-UQ^2 = -U*(Q^2-U-V-2W)-(UV-W^2),
    (V+W)^2-VQ^2 = -V*(Q^2-U-V-2W)-(UV-W^2),
    (U+W)(V+W)-WQ^2 = (UV-W^2)-W*(Q^2-U-V-2W).

Once Q and U are nonzero, set f=(U+W)/Q and F=(V+W)/Q. These identities give f^2=U,F^2=V and fF=W=v^2. Their sum gives f+F=Q; hence the source Kummer equation follows from the definition of Q. The last new row gives ft=v. Since f^2=U!=0, f!=0 and fF=v^2 then gives F=vt. Thus the entire source392t block is restored, including the true field-square meanings consumed by every other row.

Conversely, for a source solution set W=v^2. The new rows hold with Q=f+F. The source has f!=0. If Q=0, then F=-f and v^2=fF=-f^2, impossible in the real field K unless f=v=0. Thus Q and U are nonzero on every source solution. The maps are inverse on full solutions after the two candidate branches are excluded. No H-sign assumption, scalar pole, or logarithm is needed for this forward nonzero argument.

## Exceptional branches are excluded before reconstruction

If U=0, UV=W^2 gives W=0 and then v=0. The fixed formula gives Q=1/c and V=1/c^2. Thus the actual low-order conjugate-V leaf is the square of the unit1/conjugate(c) at every consumed place p>76176. Both c and its inverse are integral outside2 and41. The high U leaf is zero and poses no difficulty.

If Q=0, the first displayed identity forces U=-W, and the sum gives V=-W. Hence U=V=-v^2, while D*v^2+2*b*v-1=0. The only two field roots are

    v=1/(c+b)=(3+2rho)/4,
    v=-1/(c-b)=(-36+16rho)/49.

I checked both roots, c+b=12-8rho of norm16, and c-b=(9+4rho)/4 of norm49/16. Each root is a unit at every consumed place. This is a placewise assertion justified by the integral building blocks and their inverses, not an inference from a unit norm with possibly nonintegral conjugates.

On Q=0 the two candidate outputs are negative squares, rather than arbitrary nonsquares. This restriction is essential. On that branch use epsilon=-1 and D_H=v for the order40 U factor, and epsilon=-1 and conjugate(v) for the order1 conjugate-V factor. Every other detector leaf is still a genuine square of some field expression: the other point-square outputs follow from their unchanged root/biquadratic blocks without interpreting H; the input, cross and Lucas test squares square their stored field expressions even when no ratio interpretation has yet been established.

For clarity, the signed one-place argument is as follows. A factor1+epsilon*R*(D_j/R^m_j)^2 with epsilon=+1 or-1 and odd alpha=v_p(R) has nonconstant term of odd valuation alpha+2(v(D_j)-m_j*alpha). Its valuation is nonzero, so the factor valuation is its minimum with zero, exactly as in the original proof. A zero D_j gives factor1. Therefore every factor valuation is nonpositive. If lambda is the maximum product valuation over places above p, trace integrality gives v_p(B)<=alpha+2lambda for the same pole input B=R/Tr(product^-1)^2. The pole excludes negative odd valuations, while B has the parity of alpha. Hence alpha>0 and lambda>-alpha/2. At a place attaining lambda every factor has valuation at least lambda, so

    v(D_j)>(m_j-3/4)*alpha>=m_j-3/4.

Valuations are integral at the unramified consumed place, giving v(D_j)>=m_j. The signs are units and change none of these comparisons. This applies to the classified Q=0 branch; it is not asserted for arbitrary U,V.

The high U factor on Q=0 would therefore force positive valuation of a fixed unit v. On U=0, the ordinary unsigned argument forces positive valuation of the fixed unit1/conjugate(c) through the low-order factor. Both are contradictions at any prime in any of the three contact radicals.

My finite checker matches the actual high U factor in all three detector evaluations. It also derives the actual conjugate-V low factor through the shared coefficient rows and optimized cubic evaluation with V treated as an arbitrary field value. Thus the signed argument is bound to the factors the candidate really uses. The remaining detector products, traces and pole domains are unchanged and have their same algebraic nonzero guards; no scalar pole or putative H point is used here.

## The anchor-height contradiction is independent of these branches

Either exceptional branch would make all three contact radicals equal one. The root-height implication with N=1 then gives Bmax^2-6<7*Hcal. The four odd roots and their three scales are unchanged. So are the scalar S chart, its reciprocal g0 inverse and the rescaled anchor. They identify a nonzero even scalar point without H, apply the unconditional coefficient lemma to restore f1 and its inverse, and restore the old anchor. Hence Bmax>=|a_index|>(40*Hcal)^10, contradicting that upper bound.

This is the same independently available anchor used in the accepted394 reconstruction. It needs neither H, interpreted LP coordinates, a scalar height upper bound, nor positivity of the scalar pole input. The proof therefore establishes Q,U nonzero before restoring source392t. Applying the accepted source soundness afterward is not circular.

Completeness maps the old full witnesses forward. It keeps all real, local, correction, CRT and pole choices unchanged. The extra candidate branches are absent from that forward image and have now been excluded for all candidate solutions.

## Independent finite evidence and decision

The local `check.py` imports no author producer or checker. It verifies the frozen report and IR, both old field-square meanings, all four new field rows, every removed/repurposed-coordinate incidence, all unchanged outside records, the reconstruction identities, branch constants, the actual high and low detector factors, and every coefficient of the primitive SOS. All390 coordinates occur and all6989 symbolic terms have distinct ordinary coordinate monomials. The unique C^2 coefficient is16 on W_anchor^2*tau_anchor^2, with no lower-C contribution there. Other C-linear coefficients are at most96 and constant coefficients have fewer than2048 bits.

The checks pass. This exact390 candidate is independently accepted as a two-coordinate reduction from accepted392t. The review does not accept a later composite artifact or alter the frozen Version13 manuscript. Run `python -B check.py` in this directory to reproduce the local `CHECKS.json`.
