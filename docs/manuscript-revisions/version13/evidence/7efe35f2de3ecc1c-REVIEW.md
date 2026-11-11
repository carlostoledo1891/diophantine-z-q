# Independent review of the enlarged H domain

Accepted as an arithmetic source enlargement and a two-coordinate deletion on the pinned 437 source below. This review does not approve a later combined polynomial or a publication count. The change preserves the integer input projection; it does not assert that every new witness lifts to the old square-abscissa H chart.

Reviewer: `/root/astra_quartic_opt01_elimination`. I did not author this enlargement. I read its frozen proof, the source passages identified below, the identity-extension argument and its independent review, and the actual H/V0 residuals. I independently checked the finite-field calculations, exceptional-point arithmetic, physical equations and generic subtraction identities. The two local checkers import no producer code.

## Bindings

| Object | SHA-256 |
|---|---|
| `00-independent470/H-domain/REPORT.md` | `a1c586873dd2a2f0dfad529ea979ec506a1d42c273e4eaa9160ae8189fbb641a` |
| Author `check.py` | `f98dfe234d0e4eecafea197b705d718a0db7ba1d46179a4a29480b95a50436e3` |
| `10-combination/primary437-ir.json` | `e488bf3c4e70fda6e0484a51a3a5421cb5b4b0540d3f4cfc3a4192471b00739e` |
| Released `manuscripts/quartic_v12.tex` | `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9` |
| `00-independent470/IDENTITY_EXTENSION.md` | `d3a410ad9fc6932fcb45cae0ec83616e44a7dbdbd7d6938fd20d5f0efea07f32` |

The identity-inclusive comparison charts are separately reviewed in `05-anchor/review-identity-extension.md`. Their allowance of zero numerators is an input here. The scalar depth-24 constants, when that variant is used, remain a separately reviewed input; this argument changes the group identity used to transfer any positive scalar depth.

## Physical change and exact point interpretation

Coordinates 17 and 18 are H.h0 and H.h1. Their complete incidence is precisely residuals 32 and 33, imposing x=H.h squared. Deleting those coordinates and those two residuals leaves x*f=1 and S squared=x-D*f. Thus H=(x,x*S) is a finite point on y squared=x cubed-D*x, with x nonzero. A retained H square root is not used implicitly.

The physical x expression is coordinate90+2*coordinate91*sqrt(2), not the unscaled pair suggested by its old names. The independent checker accounts for this and matches, up to a nonzero rational normalization in each component, both deleted equations, both retained curve equations, x*f=1, fV*f=v squared, d*v=N, and the V0 logarithm equation. The last equations are exactly

    d=c*x+D, N=a*S-b, T=-2D-a*b*S+2D*b*v,
    d*v=N, fV*f=v^2, T*ell0+a*N*R=0.

Here a,b,c are the fixed coordinates of P, with c=a squared and b squared=c squared-D. All other residuals remain unchanged in the proposed deletion. A later transport must check their preservation again.

## The exceptional-point exclusion is available before ratios

I checked the source generator proof at lines 339–418, the one-place lemma at 11038–11068, the three-scale height implication at 19497–19526, and the independent anchor bound. The source supplies 2E(K)=Z*P and a half R0 of P; hence, for any H, write 2H=mP and conclude H=mR0+T with 2T=0. This deduction also establishes the claimed decomposition without an additional generator assumption.

The one-place lemma is explicitly valid when other tests vanish. It operates on their field values and the detector/pole equations before any LP slot is interpreted as a logarithm ratio. For a fixed H whose f value is a unit at every consumed place, any contact prime contradicts its retained positive-depth f(H) test. All three contact radicals must therefore be 1. The root-height theorem then gives B squared-6<7*Hcal, whereas the independently available scalar anchor gives B>=|a|>(40*Hcal)^10. Since Hcal>=1, these contradict each other. This uses no scalar height bound for beta and no H ratio, so the order is not circular.

The exceptional points are all finite points in E[2], P+E[2], and -P+E[2]. O and T0 are already excluded by the affine chart and x*f=1. For the others, my checker verifies the norms of d0,c,c-d0,c+d0 and their possible bad primes separately. The abscissae of the three translates are -D/c, d0*(c+d0)/(c-d0), and -d0*(c-d0)/(c+d0). Each building block and its inverse is integral outside {2,3,7,17,41}; consequently these abscissae and their inverses are units at each consumed place. This is a placewise argument, not the invalid inference from a unit norm alone at split primes.

It follows that m is not 0 or either of +2,-2. In particular H and H-P are nontorsion, S is nonzero, and both H=P and H=-P have been excluded before using ordinary subtraction.

For d=0, the curve equation gives x=-D/c and S=+b/a or -b/a, precisely the excluded translates by T0. For N=0 the independent polynomial check gives

    x*(a*S-b)*(a*S+b)=(x-c)*(c*x+D),

so again only excluded points occur. Thus d,N,v are nonzero. The independently reduced generic subtraction identities give x(H-P)=1/(x*v squared) and y(H-P)=T/(a*d*x*v cubed). Their use is valid because x!=c has already been proved. Since H-P is nontorsion, its ordinate and T are nonzero. Therefore fV and z(V0)=-a*N/T have their claimed actual meanings.

## Global nonvanishing replaces the lost positivity argument

General H can have negative real abscissa, so the old bound w0 in [0,1] is not available. The replacement argument is valid and necessary. I independently read the actual approximation coefficients from `03-depth/approximation.json`, reduced them modulo 71 and 7, and evaluated at every residue. N8 has no root modulo 71; Q2 has no root modulo 7. In each case all coefficients are integral and the leading coefficient is a unit. The two roots of 2 are 12,59 modulo 71 and 3,4 modulo 7.

At either selected split prime K embeds into Q_p. A root of a polynomial with integral coefficients and unit leading coefficient cannot have negative valuation: the leading term would have strictly smaller valuation than every other term. Hence a K-root would give an integral Q_p-root and then a residue-field root, contrary to the exhaustive checks. This proves absence of K-roots; it neither requires nor asserts irreducibility over the residue field. Both N8 and Q2 are globally nonzero on K. Thus R(w0) is defined and nonzero, and the actual retained equation forces ell0=z(V0)*R(w0) nonzero.

The formal local error estimate remains valid: at a formal point w0 has positive valuation and the same coefficient/tail proof applies, independently of the point's real component. Other comparison points retain their old double-point domain. No real positivity conclusion about this new H or V0 is carried over.

## Half-indices and both local transfers

Set h=m/2 as a rational number, not as an asserted multiplication operation on P. At every consumed odd prime, h and h-1 are integral and one is a unit. For U_i=u_i*P and V_i=(u_i-n_i)*P, the exact integral group identities are

    [m]U_i=[2u_i]H,
    [m-2]V_i=[2(u_i-n_i)](H-P).

The two-torsion term is killed in both equations. Apply the formal logarithm only to the formal points in these identities, never to R0 or T. Its nonzero denominator values give the full ratios u_i/h and (u_i-n_i)/(h-1). The accepted zero-numerator analytic-unit identities remain valid. A unit denominator first supplies integrality for one ratio; the positive-order cross-test supplies it for the other. Only then is improved primary depth inferred. Multiplying the resulting congruences by h and h-1 and subtracting gives the same integer-label congruences. This works for half-integral h because these multipliers are p-integral; division modulo p by m is not used. At split places the alternate identity is evaluated at the conjugate place, and at inert places conjugation preserves the valuation.

The scalar transfer needs its own replacement, which the frozen proof includes. For Rscalar=sP and nonzero even s, the exact identity is

    [m]([2]Rscalar)=[4s]H.

The source's two-branch argument at lines 20302–20343 makes [2]Rscalar formal with v(z([2]Rscalar))=v(z(Rscalar)), whether Rscalar is near O or T0. Formal-log isometry now yields v_p(m)+v(z(Rscalar))=v_p(4s)+v(z(H)). A tested positive depth d therefore implies v_p(s/h)>=d, and integrality of h gives v_p(s)>=d. This includes depths 32 and 24. It does not rely on H being a double or on f(H) being a square. The scalar norm argument requires actual nonzero f(H), which the chart still gives, and the fused ratio's S denominator is nonzero by the preceding exclusion.

## Completeness and acceptance boundary

Every old complete witness still works after forgetting H.h0 and H.h1. Completeness can keep H in 2E(K); there is no need to construct a half-index H, a torsion translate, a new real branch, or new simultaneous-prime data. Soundness is the refreshed argument above on the larger domain.

The proposal therefore removes exactly two rational coordinates and two residuals on the pinned source. A final integrated candidate still needs the actual deletion/consumer comparison, SOS expansion, metadata/count verification, and review of any additional changes. No unexamined combined candidate is accepted by this report. The inherited generator, pole, height and formal-log inputs remain dependencies, not claims newly proved by finite computation here.

Reproduce the local checks with `python -B check_independent.py` and `python -B check_equations.py` in this directory. Their outputs are `independent-checks.json` and `equation-checks.json`. Both passed.
