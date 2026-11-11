# Oriented S auxiliary extension: proposed299

This frozen revision has299 total rational variables, including the input,298 witnesses,279 quadratic residuals and6630 quartic monomials. The primitive integral sum of squares has degree4, content1 and exact maximum coefficient186624*C^2, where C=3^(2^25). This is an author proposal pending independent acceptance. It changes no production manuscript and includes no ordinary-coefficient companion.

Agent01 constructed the301 elimination and this299 compiler. The root agent proposed applying the reciprocal construction to the S auxiliaries while retaining the scalar root and adding its orientation equation. The earlier reciprocal closure and arithmetic extension retain the authorships recorded in the accepted307 report. Agents03 and10 are independently reviewing this new application; their comments and checks are not represented here as already completed acceptance.

## Frozen inputs and correction history

The source is sibling `reciprocal301/candidate301-ir.json`, SHA256 `ecc9bb4e2e4b5a5a2109524a40c4140317f036d9811b580b04711e4a89cb25e6`. Its report is `f6041a0d8668eba3effe260373e2794ba8c967b808fc3083c52ba386908f34bb`. Agent10 independently accepted301 in `work/quartic-under300-20261107/10-combination/review-reciprocal301/REVIEW.md`, SHA256 `ab035cfec699f36adddff3792a0de89a30c6719e59deef3f4361198bac2bd6aa`.

The new targetIR SHA256 is `8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815`. The polynomial SHA256 is `e208b503cad67bb53eb42fd78e64b3ebe9e99223692af91dd6c6b5b5b405ca3c`.

The initial unaccepted attempt used the wrong S alternate-cache indices202/203. Both the author producer-free verifier and agent03's independent checker detected the undeclared coordinates. That candidate, SHA256 `ab42bc98539b072ff99f5b6e1a70a1867735175612782b26b2fba169b47581fd`, and its table are preserved under sibling `reciprocal299`, explicitly marked rejected. This revision uses the actual cache196/197. The builder and verifier both check the complete active-coordinate inventory. The verifier also deliberately inserts202/203 as a negative fixture and requires rejection. No acceptance attaches to the rejected bytes.

## Exact S coordinates and equations

Work over K=Q(rho), rho^2=2, D=11-6rho. Retain the scalar root coordinates

    a=v5+rho*v6, b=v7+rho*v8, c=v84+2*rho*v85.

The two old root conditions a^2=c and b^2=c^2-D remain unchanged, as do every scalar consumer of a,b,c and the oriented root point Q=(c,a*b). No scalar root squareclass or sign is dropped.

Repurpose only the S auxiliary slots

    f=v25+rho*v26, h=v27+rho*v28,
    F=v118+rho*v119, s=v120+rho*v121.

Delete122/123, the former alternate K pair. The retained caches and outputs are

    Y=v257+2*rho*v258, B=v196+2*rho*v197,
    L=v236+rho*v237, z=v168+rho*v169.

Let N be the unchanged affine shared normalizer -1/z(H), in coordinates142,143,700,701. Its exact physical expression is the one already used in307 and301 and is explicitly reconstructed in both programs. The new S equations are

    Y=f^2, B=F^2,
    h^2=f-D*f*Y,
    2*s*h-c*(f-F)-1+D*(2*Y+f*F)=0,
    s^2=c-D*(f+F),
    a*b=D*h-s*(D*f+c),
    h*L+f*N=0, (1-D*Y)*L+h*N=0,
    (1-D*B)*z=s*(f-F)-h.

All are quadratic. The orientation equation is essential because b occurs in the scalar subsystem. Merely recovering an unspecified ordinate above c would be insufficient.

The four old biquadratic pairs708--715 become the primary curve, reduced divided difference, root abscissa and orientation pairs. Rows209/210 and148/149 define the two caches. Rows188/189 and120/121 become the raw primary and regular alternate ratios. New rows2220/2221 give the regular primary ratio. Thus16 existing row objects change and2 are added. Every other old row is identical; every remaining coordinate is identical except the names of the eight repurposed slots.

## Algebraic reconstruction and orientation

Define k=s*(f-F)-h. Exactly the universal identities proved and checked in301 recover

    k^2=F-D*F*B,
    s*(f-F)=h+k,
    s*(h-k)=1-D*(Y+f*F+B).

These are polynomial consequences, with no division and no genericity assumption. The accepted307 reciprocal closure therefore gives actual points U,V with negative reciprocal ordinates h,k and the actual group difference

    U-V=(c,D*h-s*(D*f+c)).

The new orientation equation identifies this point with the already retained scalar root Q=(c,a*b). This includes chord, tangent and identity-point branches. For equal f,F the closure forces k=-h and h nonzero, and gives the tangent. If U=O it gives F*c=1 and U-V=-V; similarly for V=O. Both O are impossible. Finite two-torsion has no unexamined opposite-point branch in this closure. The root agent's algebraic note `work/quartic-optimization-20261107/root-ordinate299/PROOF.md`, SHA256 `69ddd3063b571c19a481272a31268ce093411c0c5519d62aef65878d52a4a7d0`, states the same reconstruction and orientation boundary.

All root nonzero and parity arguments are retained. In particular the actual common height-product inverse still excludes c=0; the S root square chart has not even been removed. The complete inherited S sign action flips5,6,7,8,543,544,549. My checker verifies that every new row is fixed and only the original scalar rows474,475,513,514 change by an overall minus sign. Thus the existing half-sign freedom and all scalar point meanings survive.

## Soundness and the pre-logarithm order

The new raw S auxiliary curves may describe E(K) points outside2E(K). This is the same arithmetic extension already accepted for A/T/Z in307, now applied to the last auxiliary pair. It is not a claim that every new S auxiliary value has the old square-root lift.

The required domain proposal is `work/quartic-optimization-20261107/resume-auxiliary-domain-20261107/PROPOSAL.md`, SHA256 `b4641d8f2d6c50824956de216ff7055e31b9c9ab79249d41ee5567300a3ee750`. Its conditional independent review is `work/quartic-under300-20261107/10-combination/review-auxiliary-domain313/REVIEW.md`, SHA256 `7af494b74875f9f6035584bd5ae374a98658153685513f565b376314aa4ee53b`. That proposal explicitly covers all four auxiliary pairs while retaining every integer root label and the scalar root orientation. The new equations provide these conditional inputs for S.

The order is substantive. First reconstruct k and both actual points polynomially, and establish the oriented difference with Q. The old scalar root, anchor and height argument then exclude the all-empty-radical branch without using the missing raw alternate ratio. The reconstructed curve already gives even valuations of each nonzero reciprocal f,F at good places. Thus the unchanged caches still give the original fourth/eighth/sixteenth valuation periods before formality or logarithms. The unchanged low tests force each relevant nonzero F to have positive valuation at a successful place. Consequently A=1-D*B is nonzero globally; for F=0 it equals1. The identity

    A*(k*z-F)=k*(A*z-k)+(k^2-F+D*F*B)

now recovers the raw alternate equation k*z=F. This cancellation is not used to obtain the successful-place argument. At O the regular equation already gives z=0. Finite alternate two-torsion is excluded by the low tests before any division. The primary regular equation gives the corresponding zero-safe L value. The unchanged H/V0 exclusions remain before ratios.

The remaining domain argument uses the known decomposition E(K)=Z*R0+E[2], P=2R0, with auxiliary free indices k_i/2 and H index m/2. The identities with coefficients2m and2k_i kill both torsion terms; all these rational free indices are integral at the consumed odd primes. The prior cross-test and H-bootstrap proof therefore yields the same congruences to the retained integer root labels. The S scalar argument sees exactly its old oriented Q because a,b,c and every scalar row are unchanged. Global rational-approximant nonvanishing uses the existing modulo71/modulo7 certificates, not an unproved real positivity interval for the enlarged cosets.

Thus the rational input projection is unchanged. The301 A/T/Z elimination has an exact inverse on all full rational zero sets. The additional S extension in299 instead has a forward witness map and an arithmetic reverse implication to integer input; it does not assert a bijection to all old S square-root fibers. No new arithmetic assumption or exceptional root domain is introduced.

## Completeness and exact forward map

For any complete301 witness, its old S auxiliary chart has normalized r=V_old/a, J=I_old/a and g=Q_old/a, K=K_old/a, with a nonzero. Set

    f=V_old^2/c, h=-I_old*V_old/c,
    F=Q_old^2/c, k=-K_old*Q_old/c.

The source point meanings imply Y=f^2 and B=F^2. The verifier binds the actual source cache equations I_old^2=c*(1-D*Y) and K_old^2=c*(1-D*B), and the source ratios I_old*L=V_old*N and K_old*z=-Q_old. These imply both new primary ratios and the regular alternate ratio, including identities.

The old actual relation U-V=Q gives a finite s by the chord formula if f!=F, or by the tangent formula if f=F. Its ordinate is the unchanged a*b, so the orientation row holds. Keep every outside value and delete122/123. No new real neighborhood, finite congruence, contact-prime choice or anchor witness is selected. Hence the prior simultaneous completeness choices are preserved exactly.

## Executable checks and remaining review boundary

`verify.py` imports no producer. It reconstructs all18 changed/new rational components, binds the actual old cache/ratio equations, checks all old and new private-coordinate consumers, checks every unchanged object, checks the S sign action, verifies the universal reconstruction identities and recomputes the entire primitive sum of squares. Full active-coordinate equality and the rejected-cache negative fixture are mandatory. The resulting299-coordinate/279-residual/6630-monomial checks pass, as does the exact maximum-coefficient comparison without expanding C.

These are author checks. The frozen candidate still requires independent acceptance of the new S domain application, the orientation and scalar interfaces, and the literal finite construction. The manifest records the reviewed bytes; the rejected earlier attempt remains separate.
