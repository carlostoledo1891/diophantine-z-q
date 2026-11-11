# Identity-inclusive primary charts composed at 423 variables

The frozen `combined423-ir.json` has SHA256 `3c19ce0d46ae80732e76fd243b7fd1c91599f4274e1c67b9a4ac6c5bd86899bf`. Its polynomial SHA256 is `a6342d78d4ac081f59dfd11599e725e93f52f945b21b7f1d54391c2779045689`. There are423 total variables,422 witnesses,392 quadratic residuals and6,172 quartic monomials. Content is one and the maximum coefficient remains16*3^(2^26).

The accepted source is431, SHA256 `180968baa12a26f0171eeeb337df61b293a3a122786929e28b9fc94c55ba5573`. Its non-author review is copied to `inputs/composition431-review.md`. The new component is the guard-free435-to427 primary replacement copied to `inputs/identity-chart427-ir.json`. Its non-author arithmetic and implementation review is `inputs/identity-chart-review.md`. The exact component source is the earlier435 system; `combine_primary423.py` checks every affected source row and coordinate meaning before transporting it to431. `verify_combination.py 423` independently reconstructs the whole result and full polynomial. Both passed.

## New point interpretation

For each i=1,...,4 the reciprocal primary pair r,J satisfies f(U_i)=r^2 and J^2+D*r^4=1. If r is nonzero it represents the same finite doubled point as before. If r=0, both J=1 and J=-1 represent the identity O, with the canonical values f(U_i)=z(U_i)=0 and integer label u_i=0.

For each unchanged odd root Q_i=(c,ab), c=a^2, the component's quadratic g,k and auxiliary equations give exactly V_i=U_i-Q_i, including U_i=O, V_i=O and U_i=-Q_i. The denominator c+D*r^2 is positive in both real embeddings; k cannot vanish by the norm-seven argument. Thus f(V_i)=g^2 and z(V_i)=-g/k are defined, taking value zero at the identity. The primary quotient equation J*L_i=r*s_H gives the original ratio, including its zero numerator case.

These are new arithmetic domains. No assertion that every identity witness lifts to the old finite affine chart is made. Completeness can retain the old nonidentity witnesses; soundness uses the accepted extended interpretation.

## H reconstruction and the required V0 exclusion

The431 source has already eliminated H.j and rescaled its V0 coordinate. Its retained h,x,f_H,s_H satisfy x=h^2, x*f_H=1 and s_H^2=x-D*f_H. Hence h is nonzero, j=h*s_H reconstructs the old H chart, and oldg=h*v reconstructs the former V0 reciprocal coordinate. The exact identities in `REPORT437.md` and its non-author review prove that the actual H point, V0 point, f values and logarithm output are preserved. All these equations remain unchanged in423.

The old proof that V0 is nonidentity through V1 nonvanishing is unavailable because V1 may now be O. The accepted replacement argument precedes all division by logarithms. If V0=O, the reconstructed H is P. Then

    f(H)=8*(57+28*sqrt(2))/1681,
    Norm(f(H))=64/1681.

It is a unit at every consumed place over p>76176. The unchanged order40 f(H) test and one-place detector statement then exclude every prime from each of the three contact radicals. All three radicals equal one. The unchanged root-height estimate applied with the nonzero integer N=1 gives B^2-6<7*Hcal, Hcal<2^2093966. But the scalar anchor still gives log2|s_index|>25165823.5 and B>=|s_index+1|. These inequalities contradict. Thus V0 is nonidentity and ell0 is nonzero by the positive rational-log factor and nonzero z(V0).

This argument uses no primary or alternate logarithm quotient, so it is not circular. It remains valid after the scalar depth change: the anchor and root-height inequality are unchanged, and the accepted depth24 scalar proof retains their required height margin. It also remains valid after the scalar f1 guard replacement because that review preserves the actual nonzero even scalar orbit and its anchor value. The four odd-norm augmentations preserve the actual root points and odd nonzero root labels.

## Local ratios with zero numerators

Once V0 is excluded, the denominators z(H) and ell0 are nonzero. At U_i=O or V_i=O, the corresponding exact group logarithm and approximation are both zero. The accepted identity-extension proof writes approximate ratios as the exact rational index ratios times units, choosing the unit to be one in the zero case. For the remaining points it uses the prior formal-series estimates. Thus equal valuations include infinity, integrality transfer still holds, and the same integer-index subtraction gives the label congruences. No finite valuation is assigned to zero and no nonzero numerator is divided out.

The source431 scalar changes concern only the preparation of beta and scalar pole input. They preserve the primary and alternate ratio definitions, the order10/40 tests, the rational-log functions and their nonvanishing on 0<=w<1. At identity w=0 those functions equal one. The root-height contradiction, Lucas contradiction and final beta-integrality conclusion therefore have the same premises after the extended local argument.

## Remaining review

The finite transport is complete. The final non-author composition review must verify the interaction between this renewed V0 argument and the H rescaling, scalar f1 guard and depth24 source; it must not merely reuse the old V1-based nonzero proof. This report records those interfaces explicitly. No later input-label or correction proposal is included, and the below400 publication threshold has not been reached.
