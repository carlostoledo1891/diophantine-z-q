# Root and biquadratic component typing

This note concerns the chart replacement already printed in the frozen manuscript. It does not identify the full 259-variable and 248-variable systems by a witness bijection.

For one root, write Q=(c,ab), c=a^2, b^2=c^2-D. All five stored comparison values V,Q',I,K',W use ordinary field components. The dictionary records the exceptional real factor 2 for c_T as well as the factor 2 in every stored rho component of c.

Put r=V/a, g=Q'/a, J=I/a, k=K'/a. The cross equation forces W=rg. Define

    d=c+D r^2, e=c+D g^2,
    T=c(r^2+g^2)+D r^2 g^2+2brg-1,
    G=dg-aJ+br,
    E'=ak+bg+er,
    H'=dk-bJ+2a(cr+bg).

The other three retained field equations give T=G=E'=0. Direct polynomial expansion modulo c=a^2 and D=c^2-b^2 gives

    a^2(J^2+D r^4-1)=dT-G(dg+br+aJ),
    a^2(k^2+D g^4-1)=eT+E'(ak-bg-er),
    dE'=aH'+DrT-bG.

The checker verifies these three identities by exact expansion, not sampled values. Since a is nonzero, they recover both conics and H'=0. Conversely the old primary conic and G=H'=0 imply T=E'=0 because d is positive. Thus V=ar, Q'=ag, I=aJ, K'=ak and W=rg give inverse field maps on the chart.

The retained square equations are I^2-c+D c Y_U=0 and c-K'^2-D c Y_V=0. Hence Y_U=r^4 and Y_V=g^4 since D c is nonzero. Packet024 checked their exact rational components and all later power/factor uses.

No zero stratum of r or g is discarded. At r=0 the first point is O and the second is -Q. At g=0 the second is O and the first is Q. The regular formulas include U=-Q. The original proof's comparison with the group law is still the source of this geometric interpretation; the three polynomial identities alone are not a new point-membership theorem.

The common H chart differs from a square-abscissa root chart: it gives chi*f=1 and S_H^2=chi-Df, with H=(chi,chi*S_H). It can contain two-torsion locally. S_H!=0 and the fixed-subtraction denominators are established by the later forced149 argument. In particular D is a square in K, so a claim that S_H=0 is excluded because D is nonsquare would be wrong.

The alternate-ratio check expands LP_i*N_H-z_i*D_H for every i. Interpreting it as a quotient retains the separately proved H exceptions and fixed-subtraction certificate. Arbitrary solutions of a cleared equation do not themselves prove a denominator nonzero.
