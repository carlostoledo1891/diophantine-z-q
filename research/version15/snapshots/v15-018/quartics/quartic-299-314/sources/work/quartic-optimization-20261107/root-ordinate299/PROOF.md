# Removing the alternate ordinate and retaining the S orientation

This note records the root agent's proposed S extension of agent01's alternate-ordinate elimination. It is a proof component, not acceptance of a complete 299-variable artifact. The source is the independently reviewed reciprocal307 system, IR SHA256 `0b94aaf7669b3fe89cdf48f4718750991cfea4dd289695543f29b0cd533f29a1`.

Use the negative reciprocal convention f=1/x(U), h=-y(U)/x(U)^2, F=1/x(V), k=-y(V)/x(V)^2. Identity points have f=h=0 or F=k=0. Retain Y=f^2 and B=F^2, the primary curve, and

    s^2-c+D(f+F)=0.

Remove k as a stored field element and define its reconstructed value by

    k=s(f-F)-h.

Replace the old divided-difference row with

    b = 2sh-c(f-F)-1+D(2Y+fF)=0.

Replace the regular alternate ratio by

    (1-DB)z-s(f-F)+h=0.

All these are quadratic in the remaining stored variables. Do not substitute k into the old raw alternate ratio and then count its cubic expression as quadratic. That raw equation must instead be justified as a consequence, as below.

## Exact recovery identities

Write A=h^2-f+Df^3, R=s^2-c+D(f+F), and use Y=f^2, B=F^2. The original divided-difference expression is

    s(h-k)-1+D(f^2+fF+F^2) = b-R(f-F).

The reconstructed alternate point satisfies the exact identity

    k^2-F+DF^3 = A-(f-F)b+R(f-F)^2.

Thus the primary curve, retained slope row, cache definitions and b=0 imply both the old divided-difference row and the alternate curve, without any division or arithmetic hypothesis. The other old slope row holds by the definition of k. The complete reciprocal secant/tangent proof therefore supplies exactly Rpoint=U-V, including the cases U=O or V=O.

The remaining regular ratio is (1-DB)z=k. Multiplying the missing raw ratio gives

    (1-DB)(kz-F) = k((1-DB)z-k) + (k^2-F+DF^3).

Consequently the raw ratio follows whenever 1-DB is nonzero. This nonvanishing is an arithmetic dependency of the elimination and must be discharged in the assembled construction, rather than assumed during the polynomial substitution.

The inherited successful-place argument establishes positive alternate f valuation before using the point ratios. Its inputs are the actual point curves, cache powers, the unchanged pole equations and the retained root/height/anchor system. The all-empty-radical case is ruled out by the root-height and anchor contradiction before any logarithm is used. At such a place F is either zero or has positive valuation, so 1-DF^2 is a unit because D is a unit there. This proves global nonvanishing in K and restores every omitted raw alternate ratio. The literal new system must be checked to preserve all inputs of that argument. This note alone does not certify those consumer checks.

## The S extension

The reciprocal307 construction deletes the root b-coordinate pairs for A, T and Z. It leaves the S interface unchanged because S.root.b is also used in scalar equations. Removing S.root.b is not proposed here.

Instead, retain the complete S root chart a^2=c, bS^2=c^2-D, all S-root coordinates, and every scalar equation. Replace only the S auxiliary-point interface with the reciprocal equations above, eliminating its alternate ordinate k as for A/T/Z. Add the explicit orientation row

    a*bS = D*h-s*(D*f+c).

This is quadratic and introduces no variable. It identifies the actual root ordinate consumed by the scalar block with the ordinate produced by the oriented reciprocal difference. The root curve alone would allow the opposite sign and is not a substitute for this row.

The old S auxiliary interface has five field-valued pairs that become f,h,F,s,k in the reciprocal description. Deleting k saves one field element, or two rational coordinates, while retaining S.root.b. The prospective total is therefore 301 minus two, namely 299. This is only a count plan until the complete literal S consumer audit and expansion have been performed.

For soundness, exact slope recovery and the added orientation identify the same S point in both the auxiliary and scalar blocks. The independently reviewed auxiliary-domain extension already allows all four U_i,V_i to lie in E(K), with half-integral free indices and unchanged integer root labels. Its stated scope therefore includes S, provided all its actual hypotheses and restoration order are retained.

For completeness, use the old complete witnesses and their exact reciprocal maps. Their difference is the old oriented S root, so the new orientation row holds identically. The missing k is its old reciprocal ordinate. This adds no point choice, congruence, real-neighborhood requirement or nonzero guard. No root subgroup is enlarged, and the scalar value g is unchanged.
