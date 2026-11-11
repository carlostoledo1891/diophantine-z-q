# Enlarging the auxiliary H domain

Author: /root/astra_bl5_models. Proposed two-coordinate saving, awaiting independent review. This is new proof development, not independent acceptance of my own proposal. No candidate polynomial is approved here.

## Exact change and sources

In 10-combination/primary437-ir.json, SHA256 e488bf3c4e70fda6e0484a51a3a5421cb5b4b0540d3f4cfc3a4192471b00739e, H.h coordinates17,18 occur only in H.chart.x.0.definition and H.chart.x.1.definition. Delete them and these two equations x=H.h^2. Keep x*f=1 and S^2=x-D*f, where S is the existing field coordinate formerly j_H/h_H. Then H=(x,x*S) is a finite E(K) point with x!=0. It need not be a double. This enlarges the source, rather than giving a witness bijection.

check.py verifies the exact incidence, the difference identities and the modular nonvanishing certificates using standard-library polynomial arithmetic. All checks passed; output is checks.json. Later composition needs another actual-consumer check.

The manuscript is work/quartic-version6-release/repository/manuscripts/quartic_v12.tex, SHA256 5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9. Its generator proof, lines339-418, gives E(K)=Z*R0+E[2](K), with P=2R0 and full two-torsion. Write H=[m]R0+T, m integer, T in E[2], and h=m/2. Here h is a rational free index, not a group expression [h]P. At every odd prime it is integral. The four torsion points are O,T0=(0,0),T+=(d0,0),T-=(-d0,0), where d0=3-sqrt(2), D=d0^2.

The zero-tolerant proof is ../IDENTITY_EXTENSION.md, SHA256 d3a410ad9fc6932fcb45cae0ec83616e44a7dbdbd7d6938fd20d5f0efea07f32, independently reviewed in05-anchor/review-identity-extension.md. U_i remain in2E(K), allowing O. Q_i remain nonzero odd multiples. Only H is enlarged.

## Exclude fixed exceptional H before ratios

The scalar anchor alone implies |a|>(40*Hcal)^10 from its fixed nonzero index lower bound and Hcal<2^2093966. This needs neither the scalar height bound for beta nor any ratio involving H. The root-scale bound, v12 lines19497-19526, gives B^2-6<7*Hcal if all three contact radicals equal1, with B>=|a|. These inequalities contradict each other.

The unchanged one-place detector lemma therefore excludes any fixed H for which f(H) is a unit at every consumed place above p>76176. Any contact prime would force positive valuation of the retained order40 f(H) test. If no such prime exists, all radicals equal1 and the contradiction applies. The lemma explicitly permits zero values of other tests. No LP interpretation is needed here.

Apply this to every finite point in E[2], P+E[2], and -P+E[2]. O and T0 are already excluded by finite x and x*f=1. Put c=x(P)=(57-28sqrt(2))/8. Direct calculation gives

    Norm(c)=41^2/64, Norm(c-d0)=17^2/64,
    Norm(c+d0)=63^2/64, Norm(d0)=7,
    x(P+T0)=-D/c,
    x(P+T+)=d0*(c+d0)/(c-d0),
    x(P+T-)=-d0*(c-d0)/(c+d0).

The -P translates have the same abscissae. Each abscissa and its inverse are integral outside {2,3,7,17,41}. This proves a unit assertion at each place, not just for a norm allowing cancellation. All these primes are below the cutoff. Thus m!=0,2, H and H-P are nontorsion, S!=0, and H=-P is also excluded.

## Rescaled V0 chart

For fixed P=(c,ab), c=a^2, b^2=c^2-D, the actual437 equations are

    d=c*x+D, N=a*S-b, d*v=N, fV*f=v^2,
    Tprime=-2D-a*b*S+2D*b*v,
    Tprime*ell0+a*N*R(w0)=0, w0=D*fV^2.

The old positivity proof for d is unavailable. If d=0, then x=-D/c and S=+b/a or -b/a, giving H=-P+T0 or P+T0, already excluded. If N=0, the curve equation factors as (x-c)*(x+D/c)=0, again giving excluded points. Hence d,N,v are nonzero.

The independently checked difference identities are

    x(H-P)=1/(x*v^2),
    y(H-P)=Tprime/(a*d*x*v^3).

The check compares both with ordinary subtraction on x!=c. The only equal-abscissa points H=+P,-P were excluded before this step. Thus no limiting argument is hidden here. It follows that fV=x*v^2 is the actual reciprocal abscissa of V0=H-P. Since V0 is nontorsion, its ordinate is nonzero, so Tprime!=0 and z(V0)=-a*d*v/Tprime.

The checker also verifies x*Tprime^2/(a^2*d^2)+D*x^2*v^4=1. Do not replace this by the old K-valued square-root chart: H.h need not exist in K.

## Nonzero logarithm beyond the positive component

Negative real abscissae are now permitted. Thus w0 need not lie in[0,1], and the old positivity argument for R cannot be cited. The actual approximation is N8/Q2 with

    Q2=1-(1526/1073)w+(513/1073)w^2,
    N8=1-(9776/5365)w+(2941/3219)w^2-(1024/13949)w^3
       -(1920/237133)w^4-(1024/711399)w^5
       -(1408/5928325)w^6+(2432/103152855)w^8.

The checker exhaustively verifies that N8 has no root modulo71 and Q2 has no root modulo7. Their coefficients are integral with unit leading coefficient at the respective prime. Both primes split in K: sqrt(2) has residues12,59 modulo71 and3,4 modulo7. A K-root would give a Q_p-root; the coefficient conditions force that root to be integral, contradicting reduction. Thus neither polynomial has a root anywhere in K. No irreducibility assertion is needed.

Therefore R(w0) is defined and nonzero for every w0 in K. The actual logarithm equation gives ell0=z(V0)*R(w0)!=0. Its sign is immaterial. At formal points the same coefficient/tail argument gives relative order40 irrespective of global real component. Other comparison points remain doubles and keep their old positivity bounds.

## Comparison indices with two-torsion

At a consumed place H,U_i are formal at the primary place, and V0,V_i at the conjugate place. At an inert prime conjugation preserves the valuation. Write U_i=[u_i]P and V_i=[u_i-n_i]P. The integral group identities

    [m]U_i=[2*u_i]H,
    [m-2]V_i=[2*(u_i-n_i)]V0

kill the two-torsion T. Apply formal logarithms to them, without applying a formal logarithm to R0 or T. The full ratios are u_i/h and (u_i-n_i)/(h-1). Their denominator logarithms are nonzero by the established exclusions. The exact analytic-unit identities of the identity-extension proof include zero numerators.

At odd p, h and h-1 are integral and differ by1, so one is a unit. The cross-test transfers integrality to both approximate and full ratios. Every nonzero U_i then has depth at least20, while an identity numerator has zero error. The primary order80 and alternate order12/order40 bounds follow. Multiplying the congruences by h and h-1 and subtracting gives the same congruences with n_i. The current order10 first cross-test and order40 others are unchanged. No division by m modulo p is used.

## Scalar height transfer must also be updated

The scalar lemma at v12 lines20302-20343 cannot simply be cited with integral h. Let Rscalar=[s]P for the retained nonzero even scalar index s=a-1. The old local proof that [2]Rscalar is formal and v(z([2]Rscalar))=v(z(Rscalar)) remains valid, including when Rscalar lies near T0. Replace its group identity by

    [m]([2]Rscalar)=[4*s]H.

This is exact since P=2R0 and T has exponent two. Formal logarithm isometry gives

    v_p(m)+v(z([2]Rscalar))=v_p(4*s)+v(z(H)).

For any retained scalar test depth d_scalar>0, the actual ratio test gives v(z(Rscalar))-v(z(H))>=d_scalar. Hence v_p(s/(m/2))>=d_scalar. Since m/2 is integral at odd p, v_p(s)>=d_scalar. This covers the original depth32 and the separately approved depth24. The depth24 height constants are a separate dependency, not reproved here. All other scalar norm and pole steps use actual nonzero f(H), not its being a square. The fused scalar ratio reconstruction uses S!=0, already established.

## Soundness order, completeness and claimed saving

First identify H on E and retain the existing root and anchor data. Exclude the finite exceptional H set by the pre-ratio contact-height contradiction. Then establish d,v,Tprime and ell0 are nonzero, and only then interpret LP. Update both comparison and scalar logarithm identities as above. The downstream root-height arguments prove the same integer input projection with their separately accepted constants and test depths.

Completeness keeps the old choices H in2E(K) and merely forgets H.h. All actual values, CRT choices, continuity conditions and positive-pole witnesses are unchanged. No new half-index or torsion translate needs to be constructed.

This proposes saving two rational coordinates and two residuals on the exact437 baseline. It should compose with identity-inclusive comparison charts, but a frozen composition must still pass the full consumer and arithmetic-interface review. No polynomial or manuscript release is claimed. The one-coordinate Norm(x) alternative is unnecessary if this full-domain proof receives independent approval.
