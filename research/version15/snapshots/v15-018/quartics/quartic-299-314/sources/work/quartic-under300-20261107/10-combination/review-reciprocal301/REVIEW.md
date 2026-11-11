# Independent review of reciprocal301

I accept the frozen307-to301 alternate-ordinate elimination, relative to the independently accepted307 source and its explicitly inherited arithmetic. This review includes the new global redundancy argument for the removed raw ratios, rather than assuming that polynomial substitution alone recovers them. No correction was needed.

Reviewer: `/root/astra_quartic_opt10_combination`. The new elimination and301 compiler are by agent01. I contributed to parts of the earlier307 construction and independently reviewed agent05's auxiliary-domain argument. I do not represent those earlier algebraic contributions as newly independent here. The present scope is agent01's new six-coordinate elimination, its actual consumers, the nonzero-denominator application and full301 polynomial. The separate proposed S-oriented299 construction is outside this acceptance.

## Frozen inputs

Paths are relative to `work`.

* Source `quartic-optimization-20261107/reciprocal307-20261107/candidate307-ir.json`: `0b94aaf7669b3fe89cdf48f4718750991cfea4dd289695543f29b0cd533f29a1`.
* Source independent review `quartic-optimization-20261107/resume-review-reciprocal307-01/REVIEW.md`: `055f82695b4757c534f5d8a915afe2ede778730f3291fd2b1da6d69564d472e8`.
* Candidate `quartic-optimization-20261107/resume-elimination-20261107/reciprocal301/candidate301-ir.json`: `ecc9bb4e2e4b5a5a2109524a40c4140317f036d9811b580b04711e4a89cb25e6`.
* Candidate polynomial in the same directory: `738893f68014f1b92852585fcda5e32946cdcdb702fe37f6f7c584d4f97be76f`.
* Author report in the same directory: `f6041a0d8668eba3effe260373e2794ba8c967b808fc3083c52ba386908f34bb`.

I read the author report, the actual source and candidate rows, the auxiliary-domain proposal `b4641d8f2d6c50824956de216ff7055e31b9c9ab79249d41ee5567300a3ee750`, its independent review `7af494b74875f9f6035584bd5ae374a98658153685513f565b376314aa4ee53b`, and the accepted shared314 successful-place/low-test argument. This is source-specific acceptance, not a new proof of the inherited global arithmetic inputs.

## Reconstruction and the denominator

Use the actual negative reciprocal convention. Let d=f-F, reconstruct k=s*d-h, and write

    P=h^2-f+D*f^3,
    T=2*s*h-c*d-1+D*(2*f^2+f*F),
    R=s^2-c+D*(f+F).

The reviewer-owned exact expansion verifies

    k^2-F+D*F^3 = P-d*T+d^2*R,
    s*(h-k)-1+D*(f^2+f*F+F^2) = T-d*R.

The retained caches are exactly Y=f^2 and B=F^2, with the physical imaginary components scaled by2. Thus the primary curve, new T row and retained R row recover the old secant, divided-difference and alternate curve equations at every point, without division. This includes the tangent branch and either identity point. The307 oriented group-law closure and root reconstruction are then available before auxiliary ratios are interpreted.

For A=1-D*F^2 and the retained regular residual g=A*z-k, the third independently expanded identity is

    A*(k*z-F)=k*g+(k^2-F+D*F^3).

The missing raw ratio follows only after A is known to be nonzero. The proof supplies that fact in the correct order. Root and scalar/anchor rows are literally unchanged. The root-height/anchor contradiction therefore excludes all-empty contact radicals before auxiliary ratios or logarithms are used. At a required contact, the now-restored point curves give even reciprocal valuations; the exact cached powers and all detector, norm, trace and pole rows are unchanged. The shared314 argument consequently gives positive valuation of each nonzero alternate F at the successful place. This conclusion precedes the integral-ratio and H-depth steps. It requires the point curves and cache values, not the omitted equation k*z=F.

At that place D is a unit, so A is a unit. If F=0 then A=1 directly. Thus A is a nonzero element of K, the identity recovers the raw ratio, and every307 residual holds. In particular the finite two-torsion branch A=0 is excluded by the unchanged low test; it is not dismissed by an assumed generic denominator. No new prime-selection or approximation condition is needed.

Forward projection deletes the three k pairs. The source secant determines them uniquely and the source equations imply both new equations. Reverse reconstruction restores those unique values and the preceding global argument restores all old rows. These maps preserve every outside witness and the input. The statement is about the complete rational zero sets; a standalone local conic with no low tests would not justify it.

## Literal and numerical verification

`check_finite.py` imports no author code. It reconstructs the old and new field equations from their physical rational coordinates, including the distinct T-root scaling, checks both caches and all old k consumers, and compares every other row, coordinate and metadata object. It verifies deletion of exactly114,115,130,131,138,139; exactly18 rows are removed and12 are replaced. No residual ID is reused or silently lost. The S interface, H/V0, scalar, root, common-scale, logarithm and detector equations stay unchanged.

The checker independently expands every primitive integral residual square and matches the complete candidate table. It finds301 total variables,300 witnesses,277 quadratic residuals,6423 quartic monomials, degree4 and content1. The exact maximum coefficient is186624*C^2, C=3^(2^25), attained at x89^4. Coefficient dominance is checked using C>2^2048, without expanding C. `check_identities.py` separately verifies the three universal identities above. Their evidence is in `FINITE-CHECKS.json` and `IDENTITIES.json`.

The author packet was read only. This acceptance does not approve publication, an ordinary lift, the proposed299 extension, or a later modification of the301 bytes.
