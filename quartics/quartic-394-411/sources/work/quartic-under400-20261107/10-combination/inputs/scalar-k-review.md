# Independent review of the scalar k elimination

I accept the scalar k-coordinate elimination in the frozen
`10-combination/scalar496-ir.json`, SHA-256
`c208de39c5d90b9ceff951f730ce557fd6c5c8c3169c9f73007aaa709b0b4c13`.
It is an exact rational equivalence preserving every coordinate outside
the eliminated pair. I did not author this transformation. This review is
relative to the published 498-variable source, not a new global arithmetic
audit.

I read both the producer and the producer-free verifier, compared the
displayed identity with the source field equations, and reran the complete
verifier after suppressing its output-file write. All checks passed. No
file in the author's directory was modified. The rerun uses the author's
separately implemented checker; it is not described as a new checking engine.

Use the actual fixed constants a=-1+(7/4)sqrt(2),
b=39/8-(9/2)sqrt(2), D=11-6sqrt(2), and put

    d=a^2*x+D,
    N=a*j-b*h,
    T=-2D*h-a*b*j+2D*b*g.

The source equations are

    G=d*g-N=0,
    K=a*d*k-T=0,
    Z=k*z+g=0.

The replacement retains G and uses L=T*z+a*N instead of Z, deleting k
and K. Direct expansion in the commutative field gives

    L=a*d*Z-z*K-a*G.

For any old solution, this proves L=0. Conversely, for any new solution
set k=T/(a*d). This gives K=0, and the same identity, together with G=L=0,
gives a*d*Z=0. Thus Z=0 as soon as a*d is nonzero.

The needed nonvanishing is already valid on every retained source point
chart. The field constant a is nonzero. Each real embedding gives
x=h^2>=0, a^2>0, D=(3-sqrt(2))^2>0, and therefore d>0. No division by T,
z, g, or a variable norm is used in this reverse map. In particular no
zero or exceptional branch is silently omitted. Every other scalar guard,
including the reciprocal-abscissa guard, remains present.

T and N are affine expressions in the actual h,j,g component coordinates.
Therefore T*z+a*N has degree at most two. The source verifier checks those
semantic values, including x=h^2, against the actual retained equations.
It also verifies that the deleted k pair occurs only in the two K equations
and the two changed Z equations. No hidden consumer is left behind.

The two scalar coordinates and two equations are removed. The checked
artifact has 496 total variables, 465 quadratic residuals, and a quartic
sum of squares with 24,705 symbolic terms. Its fixed parameter is unchanged,
its content is one, and its maximum coefficient remains 16*3^(2^26).
The complete coefficient table was checked, not sampled.

This transformation is disjoint from the five comparison guard removals
in this reviewer's separate proposal: its variables and changed rows lie
only in the scalar block. Exact composition still requires checking the
composed artifact, but no additional arithmetic assumption or domain
extension is introduced by this scalar step.
