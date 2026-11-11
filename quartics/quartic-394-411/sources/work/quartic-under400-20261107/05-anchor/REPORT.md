# Complete comparison equations remove five guards

This candidate reduces the published 498-variable system to 493 variables.
It removes the five comparison half-trace inverse coordinates, keeps their
slope and ordinate coordinates, and adds two quadratic residuals at each
comparison. The resulting system has 472 quadratic residuals and a quartic
sum of squares with 25,219 coordinate monomials.

This is a new candidate pending independent review. The proof below uses
the published arithmetic inputs and changes only the comparison point
charts. It does not independently revalidate the inherited global theorem.
All work is isolated in this directory.

## Exact replacement

Work over K=Q(sqrt(2)) with E: y^2=x^3-Dx and D=11-6sqrt(2). For each of
V0=H-P and Vi=Ui-Qi, let the incoming and target points be
Q1=(x1,y1), Q2=(x2,y2). The existing chart has field coordinates

    m(x1-x2)=y1+y2,
    q=m^2,
    xR=q-x1-x2,
    yR=m(x1-xR)-y1.

Here q and yR are already stored field coordinates or affine expressions
in those coordinates, and xR is already affine. The y1,y2 values need not
be stored: the retained point charts express them as products h*j in the
existing quadratic slope and ordinate equations.

Delete the single rational inverse coordinate for the rational component
of x1-x2 and its equation. Add the two rational components of

    q(x1+x2-2xR)-2m*yR
        = x1^2+x1*x2+x2^2-D.                         (T)

Every term in (T) is quadratic in existing coordinates. Equivalently its
left side is q(3(x1+x2)-2q)-2m*yR. No new coordinate or division is needed.

The removed coordinate IDs are 100,108,116,124,132 and the removed residual
IDs are 52,60,68,76,84. The builder reads the actual semantic expressions
from the published mixed-depth precursor, transports them by coordinate
name, and verifies the retained slope, slope-square and ordinate equations
by exact rational normalization. This checks the component factors two
that occur in the stored field values.

`candidate493-ir.json` is the exact residual specification. Define its
integer quartic to be the sum of squares of its primitive integer rows.
`polynomial493.json` contains the full symbolic coefficient table. The fixed
parameter is still C=3^(2^25), and the input coordinate is unchanged.

## Chord and tangent proof

The input point charts describe nonidentity points in 2E(K), so y1 and y2
are nonzero by the published point-domain lemma. Set

    d=x1-x2, S=x1^2+x1*x2+x2^2-D,
    A=m*d-y1-y2,
    E1=y1^2-x1^3+D*x1, E2=y2^2-x2^3+D*x2.

After substituting the retained equations q=m^2 and
yR=m(x1-xR)-y1, the residual of (T) becomes

    T=2m*y1-m^2*d-S.

The exact polynomial identity is

    d*T = E1-E2-A(2y2+A).

Thus the old chart, where d is nonzero, implies (T). In particular every
published 498-variable solution extends to the new chart by deleting its
inverse witnesses. This proves completeness from the published solution
set without changing the chosen points, primes, real bounds, or poles.

For the converse point interpretation, consider both cases.

If d is nonzero, the retained slope equation gives
m=(y1+y2)/(x1-x2), and the retained xR,yR formulas are exactly the ordinary
formula for Q1-Q2. No condition on the rational component of d is needed.

If d=0, the slope equation gives y2=-y1. Since y1 is nonzero, Q2=-Q1 rather
than Q2=Q1. Equation (T) becomes

    2m*y1=3x1^2-D.

This is exactly the tangent slope for [2]Q1. The retained xR,yR formulas
then give [2]Q1=Q1-Q2. The divisor 2y1 is nonzero. This treats every
coincident-abscissa branch. The forbidden identity difference Q1=Q2 is
already impossible in the retained slope equation, which would say
0=2y1.

Consequently the new chart always gives the actual finite nonidentity
difference Q1-Q2 in 2E(K). Its abscissa and ordinate are nonzero by the same
published point-domain lemma. There is no arbitrary-slope branch and no
fake curve point. These facts also establish that all existing reciprocal
and logarithm outputs remain the intended functions of that difference.

## Projection and downstream consumers

The old half-trace guards were stronger than d!=0: they required the
rational component of d to be nonzero. The new chart permits both a purely
irrational nonzero d and d=0 with Q2=-Q1. Therefore this proposal is not a
bijection onto the old private chart's zero set. Its claim is equality of
the input projections using the published arithmetic proof.

For soundness, replace each invocation of the guarded-difference point
lemma by the proved complete-chart point lemma above. All actual objects
consumed downstream are unchanged:

* V0=H-P has index h-1, which is nonzero because H=P is excluded.
* Vi=Ui-Qi has index ui-ni, which is nonzero because Ui=Qi is excluded.
* The local ratios are still ui/h and (ui-ni)/(h-1).
* The primary and alternate logarithms are the same functions of the same
  group points, so their integrality and depth arguments apply verbatim.
* The order-40 Lucas congruence, order-12 input congruence, three-scale
  height estimates and scalar anchor are unaffected.

For example, H=-P gives the genuine point V0=-2P and h-1=-2, which is a
valid nonzero index. Ui=-Qi gives Vi=-2Qi. Neither local subtraction nor
the height argument divides by h+1 or ui+ni. The proof only needs actual
nonidentity differences, not distinct abscissas of the summands.

Thus every new rational solution yields the same integer-input conclusion
as the published system. Conversely every published integer-input witness
tuple gives a new solution by the chord identity, with all other coordinates
unchanged. Together these prove the same rational input projection.

## Reproduction and scope

Run `python -B build_tangent.py`. It verifies the generic chord identity,
the actual retained semantic equations in all five charts, the complete
incidence of each deleted inverse coordinate, coordinate coverage, residual
degrees, content one, and the complete coefficient expansion. It never
expands C as an integer. `CHECKS.json` and `tangent-contracts.json` record
the counts, bindings and exact equations.

The published source is
`quartics/quartic-498-514/candidate498-ir.json`, SHA-256
`7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a`.
The semantic precursor is
`quartics/quartic-498-514/work/03-depth/beta12/final/candidate-ir.json`, SHA-256
`4466bd973383ba404b1cc50deaf2aa4f77361850c090dc8af80b7ba77249d57c`.
No changed statement about an external arithmetic theorem is needed. A
separate reviewer must nevertheless check the expanded chart domain and
its consumers before this candidate is integrated or released.

The anchor already has only three private coordinates and no constant
chain in the symbolic version. Removing those coordinates alone cannot
provide a large reduction. No smaller semilocal predicate or shared-anchor
construction has been justified in this packet. The five complete
comparison charts are the concrete saving found so far.
