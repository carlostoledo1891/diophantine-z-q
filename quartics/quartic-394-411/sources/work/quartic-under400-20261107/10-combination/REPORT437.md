# Eliminating H.j after rescaling the V0 coordinate

The frozen candidate `primary437-ir.json` has SHA256 `e488bf3c4e70fda6e0484a51a3a5421cb5b4b0540d3f4cfc3a4192471b00739e`. It has 437 total variables, 436 witnesses, 414 quadratic residuals and 6,503 quartic monomials. Its polynomial SHA256 is `1a77fe61c5d77f5d83a049aaf6b8779c0b6a5bb4a2a2288c91d26123e813067d`. The source is `combined439-ir.json`, SHA256 `403c4126d532fd3403ce0d87a258790d6b78c1a46cf09716aab0df3a7e84c4df`. Both this new two-coordinate reduction and the final439 transport require their stated independent reviews before promotion.

Agent03 suggested eliminating H.j using the new common reciprocal s. Its obstruction was a cubic V0 square equation. The combination agent resolves that obstruction using the retained f(H) coordinate, constructs this candidate and supplies the exact checks below.

## Formulas

Write the H coordinates as h,j,x, with x=h^2, f=1/x and hs=j. The existing V0 reciprocal coordinate is g and f_V=g^2. The source uses the fixed constants a,b,D and d=a^2*x+D, with

    dg=aj-bh,
    T=-2Dh-abj+2Db*g,
    T*ell0+a*(aj-bh)*R0=0.

Keep h,x,f,s,f_V,ell0,R0. Remove j's two rational coordinates and reinterpret g's two slots as v=g/h. Replace the displayed and H-curve equations by

    s^2-x+D*f=0,
    d*v=a*s-b,
    v^2=f_V*f,
    T'*ell0+a*(a*s-b)*R0=0,
    T'=-2D-ab*s+2Db*v.

All these component equations are quadratic. Delete the two hs-j rows. The existing x=h^2 and xf=1 rows remain unchanged. The old g slots700 and701 become `V0.reciprocal.gOverH.0` and `.1`; the removed H.j IDs are19 and20.

## Both rational witness maps

In every new or old solution, xf=1 and x=h^2 imply x and h are nonzero. Thus the forward map v=g/h is defined. Keep all other retained coordinates. The old equation hs=j gives the removed j value. The old curve j^2=x^2-D, multiplied by f, yields the new s equation. The old g^2=f_V, multiplied by f, yields v^2=f_V*f. The old d and logarithm equations have a common factor h after substitution; cancel it.

Conversely set j=hs and oldg=hv. Then the new equations imply all old equations by multiplication with nonzero h or x and use of the retained x and f rows. All fields and rational components remain unchanged. These maps are mutually inverse. No new nonzero condition on s, v, T', R0, ell0 or f_V is needed for this equivalence.

For an explicit polynomial certificate put E_X=h^2-x and E_F=xf-1. The substituted old H curve equals

    x*(s^2-x+D*f)+E_X*s^2-D*E_F.

The substituted old V0 square equation f_V-(hv)^2 equals

    x*(f_V*f-v^2)-f_V*E_F-E_X*v^2.

The substituted old d and logarithm equations are respectively h times their new equations. The old hs-j equation vanishes identically. These identities establish the reverse direction without using the arithmetic interpretation of a newly introduced point.

## Complete consumer check

The entire source consumer set of j or oldg is exactly ten rows: the two H curve rows, two hs-j rows, two V0.f rows, two V0 reciprocal d rows and two logV0 rows. No outside row refers to a removed or reinterpreted coordinate. In particular the scalar fusion already removed the former scalar consumers of H.j.

`build_primary437.py` verifies the old formulas before changing them. The separate producer-free `verify_primary437.py` matches all old and new rows, checks both retained x and f definitions, verifies the displayed polynomial reconstruction identities, checks every unchanged row and coordinate, and expands the full sum of squares. It passed. The quartic has content one and maximum coefficient exactly16*3^(2^26), with the same fixed C=3^(2^25).

The actual H point, V0 point, primary ratios, logarithms, all root points and all scalar values are preserved. This is an exact rational witness equivalence, not a new approximation or arithmetic-domain extension. Non-author review is pending. No published file was changed.
