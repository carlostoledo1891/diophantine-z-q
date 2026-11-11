# Two scalar reciprocal coordinates can be eliminated

This independent proposal starts from the released498 residual source, hash `7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a`. The resulting scalar496 candidate has 496 total variables, 465 quadratic residuals, degree four, 24,705 monomials, primitive content one, and the unchanged maximum coefficient `16*3^(2^26)`. It has not been published and requires a non-author review.

Use the existing scalar reciprocal notation. The fixed field is Q(sqrt(2)), a=-1+(7/4)sqrt(2), b=39/8-(9/2)sqrt(2), D=(3-sqrt(2))^2, c=a^2, and x=h^2. Put

```
d = c*x+D
N = a*j-b*h
T = -2D*h-a*b*j+2D*b*g.
```

The released equations are G=d*g-N=0, K=a*d*k-T=0, and Z=k*z+g=0. The field pairs g and z are retained; delete both components of k and both components of K. Replace Z by

```
L = T*z+a*N = 0.
```

Every component is quadratic: T and N are affine expressions in retained coordinates, and a,b,D are constants. The exact identity

```
L = a*d*Z-z*K-a*G
```

proves the forward implication. Conversely, a is nonzero and d=(a*h)^2+(3-sqrt(2))^2 is positive under either real embedding, hence nonzero. Set k=T/(a*d). Then K=0; the identity with G=L=0 gives a*d*Z=0, hence Z=0. This is a unique rational-field lift. No new nonzero guard, completeness restriction, or arithmetic input is introduced.

`build_scalar496.py` constructs the new equations and checks the polynomial identity and source normalization. `verify_scalar496.py` imports no producer. It separately checks the incoming x=h^2 source equations, D as a nonzero square, the exact field identity, the complete incidence of the deleted coordinates, every preserved residual, every coefficient of the sum of squares, and the degree and coefficient bounds. Both scripts passed.

The deleted coordinates and rows are private to the scalar reciprocal block. This change preserves f(S-P), z(S-P), the scalar ratio, the anchor, all detector inputs, and every output consumed elsewhere. It is disjoint from the order-ten weights, four second-conic factorizations, and comparison-point guard changes. Any future combination still needs a full exact residual check.

The candidate hash is `c208de39c5d90b9ceff951f730ce557fd6c5c8c3169c9f73007aaa709b0b4c13`; the polynomial hash is `ee1e5edc49f763973de535448e10d82ad2f880b2954505a5e52b2c154ffcc456`. The under400 publication threshold remains unmet.
