# A quadratic reciprocal secant and tangent closure

This note records the root agent's contribution to the reciprocal-coordinate optimization. It is not a certificate for a complete new polynomial. The reciprocal construction was proposed by the horizontal-repair agent. Agent10 contributed exceptional-case analysis and related slope equations. Independent review of the combined construction is assigned separately to agent01.

Let K be a field of characteristic zero and D a nonzero element. Use E given by y^2=x^3-Dx, with T0=(0,0). For a finite point U with nonzero x-coordinate set

    f = 1/x(U),       h = -y(U)/x(U)^2.

The minus sign is part of the convention. At U=O set f=h=0. These coordinates satisfy h^2=f-Df^3. Conversely a pair satisfying this cubic represents the stated finite point if f is nonzero and represents O if f is zero. The excluded point is T0. The translated point U+T0 has coordinates (-Df,-Dh), including the case U=O. This follows directly from the chord formula with T0.

Write (F,k) for the same coordinates of V. Introduce s and a desired root abscissa c. Require

    s(f-F) = h+k,
    s(h-k) = 1-D(f^2+fF+F^2),
    s^2 = c-D(f+F).

If stored coordinates Y=f^2 and Yalt=F^2 already exist, each of these equations is quadratic in the stored variables. The pairwise product fF is itself quadratic and needs no stored coordinate. Thus s can replace a stored product coordinate, with no added variable.

Define

    yR = D*h - s*(D*f+c).

The following is an identity over the polynomial ring with integer coefficients. Put

    r1 = s(f-F)-h-k,
    r2 = s(h-k)-1+D(f^2+fF+F^2),
    r3 = s^2-c+D(f+F),
    r4 = h^2-f+Df^3.

Then

    yR^2-c^3+Dc
      = D^2*r4 - D*(Df+c)*(r2-s*r1)
        + r3*(c+Df)*(c+DF).

`check_identity.py` expands both sides independently as sparse integer polynomials and checks equality of every coefficient. No division or genericity assumption is used in the identity. Therefore the stated equations give a genuine E-point R=(c,yR).

For f different from F, s is precisely the slope from U+T0 to -(V+T0). The final equation is the usual abscissa formula, and yR is its ordinate formula. The resulting point is U-V.

For f=F, the first equation forces k=-h. If h were zero, the curve would give f=0 or Df^2=1. The second equation would instead give 3Df^2=1, contradicting either case. Thus h is nonzero. The second equation reads 2sh=1-3Df^2, which is exactly the tangent slope at U+T0. The resulting point is again U-V.

If f=h=0, the second equation becomes -s*k=1-DF^2 and the first becomes -s*F=k. Together with the last equation these imply F*c=1. The resulting point is -V, as required for U=O. Interchanging the inputs treats V=O. Both inputs cannot be O, because the second equation would read 0=1. These cases also follow from the finite translated-point chord and tangent formulas, since translation maps O to T0.

The resulting root ordinate has the correct orientation for the stated negative h,k convention. Reversing U and V sends s to -s and negates yR. Using h=+y(U)/x(U)^2 would require changing this orientation; the convention must therefore be bound to the actual compiler map.

## Application boundary

If the old root has a retained square witness a^2=c and c is nonzero, set b=yR/a. Then b^2=c^2-D, exactly restoring the old root square chart. This use requires a proof that c is nonzero in the complete new system. The proposed implementation retains the old product-height chain: a zero root forces its total field product to zero, then coordinate391 and its following powers vanish, contradicting inverse row352. Agent01 must check the literal scaled field coordinates in the new IR before accepting this implication.

The new auxiliary points need not admit the old square-root witnesses. Recovering the root square chart therefore does not establish equivalence to the old full private-witness system. The separate arithmetic extension in `resume-auxiliary-domain-20261107/PROPOSAL.md` must be checked and consumed. The intended implementation leaves the S-root and scalar block unchanged, modifies A/T/Z only, and has a nominal saving of six rational coordinates. That count remains subject to complete IR validation.
