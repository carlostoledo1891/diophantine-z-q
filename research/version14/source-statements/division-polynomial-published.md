# Division-polynomial scalar input

## Published source

For a nonsingular short Weierstrass curve in characteristic zero, Silverman, The Arithmetic of Elliptic Curves, second edition2009, ExerciseIII.3.7 pp105–106 defines the positive-index division polynomials by their initial values and odd/even recurrences. Parts(a)–(b) give polynomial parity and degrees, (c) gives coprimality of phi_n and psi_n^2, (d) gives the scalar-coordinate formulas, and (f) identifies the zeros of psi_n as the nonidentity n-torsion points. This is an explicitly stated published exercise, not a claim that its proof is printed there.

The official 2011 errata, p4, corrects the printed plus in the omega numerator to minus. The retained 2022 errata, entries for pp105–106, corrects the even parity factor and requests the missing small-index conventions. Here psi0=0 and psi(-1)=-1; alternatively n=1,2 are checked directly. Only the short model is used.

## Short-model conventions and actual connection

Set a1=a2=a3=a6=0 and a4=A, so y^2=x^3+Ax. The published initial values specialize to psi1=1, psi2=2y, psi3=3x^4+6Ax^2-A^2, psi4=4y(x^6+5Ax^4-5A^2x^2-A^3). Put psi_n=f_n for odd n and psi_n=2y f_n for even n. Substitution in the two recurrences gives exactly the current f_n formulas, with D0=(2y)^4=16(x^3+Ax)^2. All cancellations occur as polynomial identities before specialization.

Use the corrected short-model numerator 4y omega_n=psi_(n+2) psi_(n-1)^2-psi_(n-2) psi_(n+1)^2. The even recurrence yields psi_(2n)=2 psi_n omega_n for n>=3; n=1 and n=2 follow from the displayed initial values and the identity/duplication formulas. Therefore 2y([n]P)psi_n(P)^4=psi_(2n)(P), and x([n]P)psi_n(P)^2=phi_n(P).

If P is nonidentity in the supplied torsion-free carrier and n>0, it is not n-torsion, so part(f) gives psi_n(P)!=0. Hence the two cleared equations recover the coordinates uniquely. Neither carrier torsion-freeness nor the inverse-norm field encoding is supplied by this result.

For negative indices define psi_(-n)=-psi_n and phi_(-n)=phi_n. Group negation on the short model changes the ordinate sign. Since psi_(-n)^4=psi_n^4 and psi_(-2n)=-psi_(2n), the cleared ordinate identity has exactly the required negative sign. Scalar zero and identity input use the separate identity branches; no affine denominator is evaluated on those branches.

## Scope

This replaces the Sutherland lecture-note supplier for main278–304 and the source input to elementary-inputs-current/PROOF.md19–22. It reuses the existing normalization and guard derivation, keeps the historical note unchanged, and does not assert a new torsion or generator theorem.
