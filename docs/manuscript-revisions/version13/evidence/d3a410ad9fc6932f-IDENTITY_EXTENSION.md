# Identity-inclusive comparison charts

Reviewer: `/root/astra_bl5_models`.

This is an arithmetic source-application review of the proposed reciprocal charts for U1 through U4 and V1 through V4. It is not acceptance of a frozen candidate polynomial. No such candidate was supplied for this review. The proposed equations came from author02. The supplementary guard-free exclusion of V0=O below was proposed in this review and requires a separate reviewer before promotion.

The identity extension is valid under the precise conditions below. It preserves the integer input projection by a refreshed soundness proof and the retained completeness construction. It is not a bijection with the old finite-point witness space.

## Exact sources and scope

The source read is `work/quartic-version6-release/repository/manuscripts/quartic_v12.tex`, SHA256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`.

The relevant source applications are:

- Lines 19331–19408, Proposition `v9chart:prop:chart`: the finite h,j chart and its particular-field identification. Its finite nonidentity domain does not itself include O.
- Lines 10815–10862, Lemma `lem:v5-unramified-log`: the formal equation, full logarithm series and tail estimates. Its relative-quotient statement is expressly for nonidentity points. The extension here uses its series identity, not a claim that the original relative statement already allows O.
- Lines 11038–11068, Lemma `lem:v5-one-place`: the detector conclusion permits arbitrary field tests, and its proof explicitly handles a zero test.
- Lines 19497–19526, Corollary `v9:cor:scales` and equation `v9:eq:height-transfer`: the product-height implication for the three root scales. It does not assume nonzero comparison points or use logarithm ratios.
- Lines 19835–19986, the v12 retained inputs and mixed local proof: labels, denominator domains, the order-one and order-forty tests, and transfer of integrality before improved primary depth.
- Lines 20200–20223 and 20523–20589: the nonzero scalar anchor and subsequent numerical margins. The scalar point is unchanged by the proposed comparison-chart extension.
- Lines 20595–20672: completeness chooses nonzero comparison points already, so it supplies witnesses inside the enlarged domain without a new prime or lifting assertion.

The current research source has shortened the first comparison and input tests to order 10 and replaced the V0,V2,V3,V4 G9 polynomials by the reviewed rational approximation. These are already scoped in `REVIEW.md` and `REVIEW453.md` in this directory. The latter gives the exact rational approximation and bounds. The present extension keeps those changes: the first alternate precision 12 remains sufficient for order 10, and the other alternate precisions remain 40. It does not revert to the v12 order-12 input test.

The current 435 packet was read to distinguish its beta shift and positive scalar correction from the earlier v12 values. Its frozen IR is `c4c8a0623be27e675f73363043ce2bc44956bd128257060e471abca9b53a0859`. The identity argument changes neither beta, the scalar point, the anchor, the root labels, nor the detector scales. Candidate-level transport and every outside consumer must still be checked against the actual chosen starting packet.

## Proposed equations and point interpretation

Work in K=Q(sqrt(2)), D=(3-sqrt(2))^2. For a fixed root Q=(c,ab), retain c=a^2 and b^2=c^2-D, with a,b nonzero. The proposed primary chart is

    f=r^2,    J^2+D*f^2=1.

For r nonzero recover h=1/r, x=1/f, j=J/f. These satisfy the old finite chart. Its already proved particular-field identification supplies U in 2E(K). For r=0, J=+1 or -1, and both branches are interpreted as U=O. Thus U=[u]P still has an integer label, now permitting u=0. No arbitrary square-abscissa criterion on other curves is being invoked.

The proposed difference equations are

    d=c+D*f,
    d*g=a*J-b*r,
    u_aux=c*r+b*g,
    d*k=b*J-2*a*u_aux,
    fV=g^2,    k*zV=-g.

Here d is positive at both real embeddings, since c=a^2 is positive and f=r^2 is nonnegative. In particular it never vanishes. Direct reduction by J^2+D*r^4=1 and b^2=a^4-D gives

    k^2+D*g^4=1.

Both J and k are nonzero at every rational component solution. For example, k=0 implies D*g^4=1; positivity implies (3-sqrt(2))*g^2=1, whose norm says 7*Norm(g)^2=1, impossible over Q. The identical argument applies to J. Consequently zU=-r/J and zV=-g/k are defined everywhere on these charts.

For r,g nonzero the equations give the actual difference U-Q, with coordinates (1/g^2,k/g^3). The independently written `identity-extension-check.py` checks its abscissa and ordinate against the usual subtraction formula as polynomial identities after clearing denominators. It also checks the reciprocal conic. Its only dependencies are the Python standard library. All four checks passed; output is in `identity-extension-check.json`.

These identities give the correct exceptional branches as well. At r=0,

    g=J/a,    k=-b*J/c,    zV=a/b,

so V=(c,-ab)=-Q for either sign of J. At g=0, a*J=b*r. Substituting into the primary conic gives

    (c*r^2-1)*(c+D*r^2)=0.

The second factor is positive, so r^2=1/c. Hence U=(c,ab)=Q and V=O. The sign choices do not change this orientation. At remaining equal-abscissa cases the reciprocal formulas are regular and agree with subtraction on a dense open of the smooth integral primary curve; equality with the group-law morphism extends. Equivalently these are the usual doubling limits when U=-Q. Thus no arbitrary point or free slope is introduced at the boundaries.

The proposed primary ratio equation is

    J*L_i=r*s,    s=j_H/h_H.

Since J and the retained h_H,j_H are nonzero, it gives exactly L_i=z(U_i)/z(H), including L_i=0 when U_i=O. This remains a rational field equation, not a componentwise division.

## Formal coordinates at O

The rational functions f=1/x and z=-x/y extend regularly to O, both with value zero. We use these regular extensions; we do not assign a finite affine x-coordinate to O. Put f(O)=z(O)=0 and log_E(O)=0. The formal identity

    f=z^2*(1-D*f^2)

then remains valid. A nonidentity point with positive valuation of f is formal by the retained good-model argument. O is formal by definition.

Write A(Q) for the formal power series factor satisfying log_E(Q)=z(Q)*A(Q), with A(O)=1. This is the analytic factor defined by the series, not the undefined fraction 0/0. At a nonidentity formal point of depth r0, A(Q) lies in 1+p^(4*r0)O. At O its difference from 1 is exactly zero.

For the retained G2 numerator define T_2(Q)=G2(D*f(Q)^2)/A(Q). For a rational-approximation numerator define T_R(Q)=R(D*f(Q)^2)/A(Q). Both are units, and both equal 1 at O. Their differences from 1 have orders at least 12 and 40, respectively, on nonidentity formal points of depth at least one. At O the difference is zero. The rational approximation has numerator and denominator equal to 1 at w=0, so it introduces no denominator problem there. Its established positive bounds on [0,1] include this endpoint.

Define every approximate numerator logarithm by z*G2 or z*R. Its value at O is zero. The order-40 approximation therefore extends by an exact zero error at O; no finite-depth estimate is extrapolated by dividing by zero.

## Local transfer including zero numerators

First establish H and V0 nonidentity as in the next section. Their actual denominator parameters and logarithms are then nonzero. Write H=[h]P and V0=[h-1]P, so h is neither 0 nor 1. Let U_i=[u_i]P and V_i=[u_i-n_i]P, allowing either latter point to be O. The rational full ratios remain

    r_i=u_i/h,    r'_i=(u_i-n_i)/(h-1).

The exact identity for the primary ratio is

    L_i=r_i*A(H)/A(U_i).

The alternate identity is r'_i multiplied by the conjugated unit T_i(V_i)/T_0(V0). These identities hold also when r_i or r'_i is zero; then the corresponding approximate ratio is exactly zero. Set v(0)=+infinity when stating valuation comparisons.

At least one of h,h-1 is a p-unit, so one full ratio is integral. Its approximate ratio is integral by the exact unit identity. The positive-order cross-test transfers integrality to the other approximate ratio, and hence to the other full ratio. This argument does not require either numerator to be nonzero.

If U_i is nonidentity, integrality of L_i now forces its depth to be at least the depth of H, which is at least 20 from the retained order-40 f(H) test. If U_i=O, no depth assertion is needed: its primary error is already zero. Thus the primary congruence has order at least 80, while the alternate congruence has order 12 for i=1 and 40 for i=2,3,4. The current cross-tests then give L_1 congruent to r_1 and r'_1 modulo p^10, and L_i congruent to r_i and r'_i modulo p^40 for the other indices. Multiplying by h and h-1 and subtracting yields the same congruences with n_i, without dividing by either integer.

This also covers split places with conjugation and inert places. In particular, if V_i=O then r'_i=L'_i=0, not a free coordinate once the denominator has been justified. If U_i=O then r_i=L_i=0. The odd nonzero root Q_i prevents both points from being O simultaneously.

## The missing V0 argument and two repairs

The earlier V0 proof cannot be reused unchanged. It excluded V0=O by combining ell0*LP1=z(V1)*G2 with V1 nonidentity. Once V1=O is allowed, this inference fails. The old source-domain statement therefore does not by itself prove guard-free soundness.

One safe algebraic repair is an inverse of the rational coefficient f(V0)_0. The V0 reciprocal chart gives this coefficient as g0^2+2*g1^2, positive exactly when g is nonzero. With that guard, the chart gives actual nonidentity V0, k is nonzero by the norm argument, and R(w0) is nonzero by the established real bounds. Therefore ell0=z(V0)*R(w0) is nonzero. In the rescaled 437 chart the actual f(V0), rather than the rescaled g alone, must be used; the retained f(H) factor is already nonzero.

There is also a guard-free arithmetic repair, proposed here. It uses the root-height implication before the ratio argument, in this order:

1. The retained H chart makes H a finite nonidentity point. The reciprocal V0 chart identifies V0=H-P even at its identity boundary. If its g vanishes, H=P.
2. At this point the actual f(H) equals

       1/c_* = 8*(57+28*sqrt(2))/1681.

   Its numerator and inverse have denominators supported only at 2 and 41, so it is a unit at every place above p>76176. In particular it cannot satisfy positive valuation at such a place.
3. For any prime in any of the three odd-contact radicals, the unchanged zero-tolerant one-place detector lemma forces all field tests at one place, including the order-40 test f(H). This contradicts the preceding unit statement. Hence all three contact radicals are 1. This step needs no interpretation of the potentially free LP_i slots when ell0=0.
4. Apply the root-scale height implication with N=1. Divisibility by the three radical powers is now automatic, and it gives B^2-6<7*Hcal. The scalar anchor and its independent margins give B>=|a|>(40*Hcal)^10, with Hcal>=1, a contradiction.

Thus V0=O is impossible in a full solution even after V1 through V4 are allowed to be O. The argument uses no logarithm ratio to obtain its height bound: the product-height corollary depends only on unchanged odd root points, their three scales, and contact radicals. The scalar anchor concerns S-P, not a comparison identity, and is also available before ratio transfer. This prevents a circular appeal to local soundness.

After this exclusion, the actual V0 logarithm equation and the nonzero rational approximation restore ell0!=0, so the local argument above applies to every rational solution. A candidate omitting the new guard must explicitly carry this revised proof; it is not a finite old-witness reconstruction. This guard-free addition is being sent to author05 for independent review.

## Height, completeness, and final boundary of this review

The height targets are the four unchanged odd root points Q_i and their abscissae, so no height of x(O) is ever used. Their integer labels remain nonzero. The scalar point S-P and its nonzero coefficient guard are unchanged. Once the local label congruences have been proved, the two existing height contradictions run with the current test orders and beta value. Allowing a comparison label u_i=0 or u_i=n_i changes none of their estimates.

Completeness already chooses a large common h with U_i=[h*n_i]P and V_i=[(h-1)*n_i]P, where the n_i are nonzero and h avoids 0,1. Those witnesses remain in the finite part of both reciprocal charts. Reciprocal reparameterization preserves their f,z values and all existing rational approximation values. No identity point is needed for completeness and no new contact-prime selection is required. If a guard on f(V0)_0 is retained, the same chosen witnesses satisfy it.

Conclusion: the identity extension is arithmetically viable for both primary comparison points and differences. Either retain one explicit V0 guard, or obtain separate approval for the guard-free V0 exclusion just given. Before accepting a concrete polynomial, inspect every actual consumer, verify that no removed r/g inverse is still required, verify the denominator logarithm equation and root/anchor/height blocks, and bind the new source proof to the frozen candidate. This report does not approve any numerical coordinate count or unexamined candidate.
