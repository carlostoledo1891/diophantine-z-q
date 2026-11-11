# Reciprocal slopes for A, T and Z: 307 variables

This proposed construction removes six rational coordinates from accepted anchor-gamma313. It has307 total variables,306 witnesses,295 quadratic residuals and6438 quartic monomials. Its exact maximum coefficient is186624*3^(2^26), without the previous +64. Independent review of this complete candidate is pending at freeze. No release or predecessor is changed.

The construction and compiler are by `/root/astra_bl_horizontal_repair`. The root agent contributed the complete reciprocal secant/tangent closure and its polynomial identity. Agent10 contributed exceptional-case analysis and zero-safe ratio equations. Agent05 contributed the arithmetic extension allowing the auxiliary points to range in E(K). Agent10 independently reviewed that arithmetic extension, with the disclosed scope in its review. Agent01 is assigned independent review of this complete candidate. These contributions are not presented as independent acceptance of their authors' algebra.

## Exact sources and artifacts

All paths below are relative to `work`.

| Object | SHA256 |
| --- | --- |
| `quartic-optimization-20261107/resume-anchor-shared314-20261107/anchor-gamma313/candidate313-ir.json` | `6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a` |
| Same313 directory, `REPORT.md` | `c8c5e7cc7e91a08fe9ec074bdaa450e83c55060bdb4b3cd2bdffbc676a1ad361` |
| `quartic-optimization-20261107/resume-auxiliary-domain-20261107/PROPOSAL.md` | `b4641d8f2d6c50824956de216ff7055e31b9c9ab79249d41ee5567300a3ee750` |
| `quartic-under300-20261107/10-combination/review-auxiliary-domain313/REVIEW.md` | `7af494b74875f9f6035584bd5ae374a98658153685513f565b376314aa4ee53b` |
| `quartic-optimization-20261107/root-reciprocal307/PROOF.md` | `9413e67fc1f54980932758304f561aaac418b037dd3406fcb0b87bbac929da0e` |
| `candidate307-ir.json` in this directory | `0b94aaf7669b3fe89cdf48f4718750991cfea4dd289695543f29b0cd533f29a1` |
| `polynomial307.json` in this directory | `90256d39e58b84a00b06003a4457ed56c1b282cd80a0c21c882a93411c660106` |

I read all three new proof/review notes before binding them here. Their inherited group, logarithm and shared314 inputs remain explicit dependencies, not new theorems established by a compiler check. Their mathematical source is Version13, SHA `9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd`.

The S-root and every scalar, anchor, common-gamma, detector-weight, norm/trace and pole equation remain identical to313. This preserves the independently accepted coupling gamma=1/u. Only the A, T and Z auxiliary point interfaces change. Coordinates3,4,11,12,15,16, the three root j pairs, are deleted. All six root square-root coordinates1,2,9,10,13,14 and their equations a^2=c remain.

## Literal coordinates and signs

Put K=Q(rho), rho^2=2, D=11-6rho and E:y^2=x^3-Dx. For each affected root R and its primary/alternate points U,V, use

    f=1/x(U), h=-y(U)/x(U)^2,
    F=1/x(V), k=-y(V)/x(V)^2.

The negative signs are part of the construction. At O use f=h=0 or F=k=0. These coordinates cover E(K) except T0=(0,0). Keep Y=f^2 and Yalt=F^2 as the existing cache meanings. The new slope is s. It describes R=U-V, not U+V or an unoriented choice.

The retained c and a satisfy a^2=c. Physical pair bases are:

| Root | a | c | f | h | F | s | k | Y | Yalt | L | z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A |1|82|21|23|110|112|114|255|190|232|164|
| T |9|86|29|31|126|128|130|259|208|240|172|
| Z |13|88|33|35|134|136|138|261|220|244|176|

An ordinary pair i means v_i+rho*v_(i+1). Both Y and Yalt have twice the stored imaginary component. The A and Z c pairs have real factor1 and imaginary factor2. The T c pair has factor2 on both components. H below is the unchanged affine primary normalizer, equal to -1/z(Hpoint) after the existing H restoration. Its literal expression is bound in both programs. The ordinary stored LP outputs and their conjugation in the difference tests are unchanged.

The new field equations for each row of the table are

    Y=f^2,                         Yalt=F^2,
    h^2=f-D*f*Y,                  k^2=F-D*F*Yalt,
    s*(f-F)=h+k,
    s*(h-k)=1-D*(Y+f*F+Yalt),
    s^2=c-D*(f+F),
    h*L+f*H=0,                    (1-D*Y)*L+h*H=0,
    k*z=F,                        (1-D*Yalt)*z=k.

Every residual has degree at most2. In particular f*F is multiplied only by the constant D; it needs no helper. The existing logarithm row z*Rlog=ell0*LP and every later ratio/LP consumer remain identical. Both raw and regular ratio rows are included. This avoids relying on a later torsion exclusion to remove any immediate zero ambiguity.

The root-j curve rows are repurposed as the primary reciprocal curves. The old four biquadratic chart pairs become the alternate reciprocal curve and three slope pairs. The cached-square, raw-ratio and z rows are replaced at their existing IDs. Rows2200 through2211 add the six regular ratio pairs. Exactly54 old row objects change and12 are added. `CERTIFICATE.json` lists every ID and physical coordinate map.

## Genuine points and complete oriented addition

If f is nonzero the primary curve gives U=(1/f,-h/f^2) on E. If f=0 it forces h=0 and U=O. The same holds for V. Thus these are actual E(K) points, with no unstated square-root lift. They need not lie in2E(K); the arithmetic extension below addresses that distinction.

Translation by T0 sends U to the finite point (-Df,-Dh), including U=O. The three slope equations are the complete secant/tangent rule for U+T0 and -(V+T0). For f!=F, the first gives their slope and the last their third abscissa. Define

    yR=D*h-s*(D*f+c).

Then R=(c,yR)=U-V. The ordinate has the stated orientation.

For f=F the first row gives k=-h. If h=0, the curve gives f=0 or Df^2=1, while the second gives3Df^2=1, a contradiction. Hence h!=0 and the second row gives2sh=1-3Df^2, exactly the tangent slope. This treats the opposite-point branch which the initial single biquadratic equation failed to constrain.

There is also a universal certificate for the recovered root curve. With

    r1=s*(f-F)-h-k,
    r2=s*(h-k)-1+D*(f^2+f*F+F^2),
    r3=s^2-c+D*(f+F),
    r4=h^2-f+D*f^3,

one has

    yR^2-c^3+D*c
      = D^2*r4-D*(D*f+c)*(r2-s*r1)
        +r3*(c+D*f)*(c+D*F).

The verifier expands this identity over independent indeterminates, including D, and checks every coefficient. It uses no division. Swapping the two inputs changes yR to -yR modulo r1, also checked exactly.

The identity endpoints are covered. If f=h=0, the first two slope equations and the last imply F*c=1, giving R=-V. The other endpoint gives R=U. Both inputs cannot be O because the second equation would read0=1. No secant denominator or nonidentity assumption has been inserted into the equations.

## Recovering the root square chart and the old labels

Each retained root c is nonzero in the full system. The verifier binds the exact scaled height products: cA*cS is v337+2rho*v338; multiplication by cT gives twice v339+2rho*v340; the next multiplication gives twice v341+2rho*v342. A zero root therefore forces v341=v342=0. Row295 gives v343=0, row345 gives v391=0, and rows346-348 force v392=v393=v394=0. Inverse row352 then becomes -1=0. All these rows are unchanged from313.

Since a^2=c!=0, put b=yR/a. The universal curve identity gives b^2=c^2-D. This exactly restores the old root square chart and its oriented point (c,ab). The unchanged squareclass calculation therefore places each affected root in2E(K)=ZP. Its original integer label, parity restoration, nonvanishing and height arguments apply. No root descent condition has been dropped. The new root-a sign freedoms are simply a -> -a, with recovered b -> -b and fixed point R. The verifier checks these sign actions on every new residual.

The S-root is kept in its original coordinates and equations, including the same b in its scalar consumers. There is no need to recover, reorient or reparameterize the scalar point. This avoids transferring a claim about root x alone to a scalar equation that consumes a sign.

## Ratios, auxiliary domain and soundness

At U=O the regular primary equation forces L=0. At V=O the regular alternate equation forces z=0. Thus the raw zero equations do not leave arbitrary ratios. If a finite primary two-torsion point has h=0 and f!=0, the raw primary equation forces H=0; the accepted restoration later excludes it. The alternate raw equation already excludes finite two-torsion because k=0 would force F=0. Away from these cases the two rows give exactly z(V)=F/k and L=z(U)/z(Hpoint), with their original signs.

For the soundness order, the new explicit curves are available before interpreting H or L. At a consumed unramified p>76176 with D a unit, every nonzero f has even valuation. For v(f)>0 this follows from h^2=f(1-Df^2), with the second factor a unit. For v(f)<0 the leading cubic has valuation3v(f)=2v(h). A unit f has valuation0; f=0 is a zero leaf. Thus the cached f^2,f^4,f^8 still have the required periods4,8,16. This applies at conjugate places too. No auxiliary square root or deep-point conclusion is used to get these periods.

The unchanged shared314/313 unique-minimum and pole argument can consequently be applied with the same stored powers. Root restoration and the unchanged scalar anchor give the same all-empty-radical contradiction before ratios. The H/V0 exceptional branches are then excluded in the inherited order. Positive local f bounds exclude finite two-torsion and make1-DY a unit at the successful places. The displayed ratios now have their genuine regular meanings.

The new arithmetic input is precisely the separately reviewed auxiliary-domain extension. In the known decomposition E(K)=Z R0+E[2], write Hpoint=mR0+T_H and U_i=k_iR0+T_i, while roots R_i=n_iP with P=2R0 retain integer n_i. The slope proof gives V_i=(k_i-2n_i)R0+T_i. The valid torsion-killing identities are

    [2m]U_i=[2k_i]Hpoint,
    [2(m-2)]V_i=[2(k_i-2n_i)]V0.

Their full formal logarithm ratios are (k_i/2)/(m/2) and (k_i/2-n_i)/(m/2-1). The free indices have denominators at most2 and so are integral at every consumed odd prime. At least one of m/2 and m/2-1 is a unit. The accepted cross-tests transfer integrality, the unchanged Lucas test forces a primary unit ratio, and the shared314 H bootstrap recovers depth10. The same primary order40, alternate order12 for V1 and order40 for the other alternates then give the original congruences to the INTEGER root labels n_i. Nothing assumes k_i/2 is a global integer.

General E(K) points can leave the old real interval for reciprocal square charts. The domain extension therefore uses the existing global no-root certificates for the rational logarithm numerator and denominator, at71 and7 respectively, rather than transferring a positivity argument to those points. The polynomial G2 is a local unit at a formal successful place. The unchanged V0 domain supplies ell0. All details and their separate independent review are pinned above.

Every hypothesis of that conditional extension is now supplied: actual point curves, regular ratios, complete oriented difference, retained root squareclasses, unchanged H/V0 and scalar blocks, and unchanged cache consumers. This proves integer-input soundness relative to the accepted313 inherited arithmetic. It is not a map from every new private witness to an old auxiliary square-root witness.

## Completeness and simultaneous choices

Take the original complete313 witnesses, including the original doubled auxiliary points and all finite/real choices. For an affected chart its old scaled coordinates satisfy V_old=a*r, I_old=a*J, Q_old=a*g, K_old=a*k_old, where J^2+D*r^4=1 and k_old^2+D*g^4=1. Assign

    f=V_old^2/c=r^2, h=-I_old*V_old/c=-J*r,
    F=Q_old^2/c=g^2, k=-K_old*Q_old/c=-k_old*g.

Keep Y,Yalt,L,z and every outside value. The old raw and regular ratio identities follow directly, including r=0 or g=0. For example the new regular primary residual is I_old/c times the old IL-VH residual. The new alternate regular residual follows from K_old^2/c=1-D*Yalt and K_old*z=-Q_old. The raw equations follow as well.

The genuine old relation R=U-V with finite nonzero R supplies a finite slope s. For unequal f,F take (h+k)/(f-F); for equal f,F use the tangent value (1-3Df^2)/(2h), whose denominator is nonzero by the case analysis above. These choices satisfy all three slope equations and recover exactly the old oriented root ordinate ab. They require no new point choice, congruence, local depth, real neighborhood or nonzero guard. The old root a, all height data, scalar and private anchor values, common gamma and later H are unchanged. Thus the inherited simultaneous completeness construction remains intact.

## Finite verification and scope

`verify.py` imports no producer. It reconstructs all66 changed or added rational components, checks every deleted and repurposed consumer against the entire IR, checks the literal root-nonzero chain and all root-a sign actions, and proves the universal root identity symbolically. It also checks every unchanged coordinate and residual object and inherited top-level datum. The complete S/scalar block is unchanged by object comparison, not merely by a name-based scope assertion.

The verifier independently expands every primitive integer residual square and matches all6438 coefficients of the output polynomial. All307 coordinates occur, every residual has degree at most2, the final degree is4 and the integer content is1. There are no collisions between different C powers on the same monomial. In particular the old three collisions vanish when the old root-j equations are replaced. The coefficient of v89^4 is now exactly186624*C^2, with C=3^(2^25), so the old +64 must not be reused. All other C^2 coefficients are smaller, C-linear coefficients are at most1728 in absolute value and C-independent coefficients have fewer than2048 bits. These facts prove the exact specialized maximum without expanding C.

The author-side checks pass. The report and manifest freeze the proposed307 packet for independent review; they do not mark that review complete. The candidate remains above the strict-under300 target. No ordinary companion or publication is claimed.
