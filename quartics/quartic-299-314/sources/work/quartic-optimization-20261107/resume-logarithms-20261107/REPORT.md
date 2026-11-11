# Logarithm and reciprocal-chart search on327

No smaller candidate is established. This bounded search rules out a direct quadratic logarithm gate in a larger fixed interface than the earlier two-gate searches considered. It includes the scaled point chart and cached primary powers. The result is an exact local algebraic obstruction, not a lower bound on all quartic definitions or all possible logarithm circuits. No source, accepted artifact, manuscript or controller file was changed.

Author: `/root/astra_quartic_opt05_anchor`, November7,2026. This new obstruction has not received independent review.

## Source and actual opportunity

The source is `../resume-depth-20261107/chain327/candidate327-ir.json`, SHA256 `d7f0ce856f2844486043d0d16388a4e72f4cf2da05736c3e9379d9bd50518665`. Parent identified it as accepted; this search does not repeat that acceptance. Its report describes327 total variables. `RESULT.json` contains the complete residual incidence of every current logarithm coordinate examined here.

The ordinary high-order blocks V2,V3,V4 have eight scalar coordinates each: two for f(V)², two for w², two for w⁴ and two for the rational approximation R(w). Their actual pairs are196/197,198/199,200/201,204/205 for V2;208/209,210/211,212/213,216/217 for V3; and220/221,222/223,224/225,228/229 for V4. V0 also has its two common-log output coordinates188/189. V1 retains its shallow approximation and is not treated as a high-order block.

The w⁴ caches have real outside consumers in the four-group detector. Deleting a logarithm gate without transporting those detector terms would not be a valid saving. In the ordinary blocks the relevant equations have the semantic form

    K*z=-Qpoint,
    Qpoly(w)*R=N(w),
    z*R=ell0*LP.

Here K and Qpoint are scaled chart outputs. The root scale a is variable, with `K=a*k`, `Qpoint=a*g`, `k²=1-D*g⁴` and `w=D*g⁴`. It cannot be silently treated as a fixed coefficient. Direct substitution generally turns the quadratic equations cubic or quartic. Eliminating the R pair in each of these three blocks would nominally save six variables, but no such replacement was obtained.

I read the earlier `quartic-under300-20261107/03-depth/LOG-SEARCH.md` and `10-combination/log-gate-bound/REPORT.md`. They exclude two sequential rational gates for G(w), or an implicit quadratic G relation with only w and w². They do not exclude using the already stored curve coordinates. This search addresses that narrower omission without asserting that the previous bounds covered it.

## Why the square-root shortcut is not a replacement

Writing `G(w)=sqrt(1-w)*H(w)` suggests replacing zG by gH and dropping a denominator. The chart has both sign branches. Replacing the stored k by the positive square root of1-w is not a rational map on the source and can reverse the logarithm's sign. With the physical scale a present, even a branch-correct formula introduces products involving a, the output and the approximation denominator. It does not automatically remove a field pair at degree two.

The bound below includes k, g and the root scale in their actual stored forms. It therefore checks possible quadratic identities that could implement such a cancellation without choosing a square-root sign. Failure on the single formal branch used in the calculation already obstructs a universal replacement valid on every source branch.

## A larger exact quadratic model

Normalize D to1 for this algebraic calculation. Over an algebraic extension choose t with t⁴=D, replace g by t*g, a by a/t and b by b/t², and apply the corresponding nonzero constant scalings to the other coordinates. These transformations preserve polynomial degree. A universal quadratic identity at the original fixed nonzero D would therefore give one in the normalized model.

Set `c=a²`, `b²=a⁴-1`, and use a formal g with

    k=sqrt(1-g⁴),  z=g/k,
    r=(a*k-b*g)/(c+g²),
    ku=[b*k*(c-g²)+2a*g*(1+c*g²)]/(c+g²)².

The scaled chart coordinates are

    V=a*r, Qpoint=a*g, I=a*ku, K=-a*k, W=r*g.

The script verifies their actual conic, product, slope and z equations as formal series. The sign of K agrees with `K*z=-Qpoint`. Also include `w=g⁴`, `w2=w²`, `w4=w⁴`, `Y=r⁴`, and `Y2=r⁸`. Y is the primary squared-output leaf and Y2 is the higher primary cache available in three groups. Giving it to every block makes the model more permissive than necessary.

The true logarithm for this sign convention is

    ell(g)=sum[n>=0] binom(2n,n)*g^(4n+1)/(4^n*(4n+1)).

Indeed `d ell/dg=1/sqrt(1-g⁴)` and ell(0)=0. The inherited precision40 contract requires a replacement output `L=ell(g)+O(g^41)` at a depth-one formal point.

Consider every polynomial of total degree at most two in the15 variables

    a,b,c,V,Qpoint,I,K,W,z,w,w2,w4,Y,Y2,L.

There are136 monomials including the constant. Substitute the displayed series and require the coefficients through g^40 to vanish. The coefficient unknowns are fixed field constants; a,b,c remain variables in the quadratic polynomial.

`full_chart_search.py` imposes these necessary equations at a=2,3,4,5,6, with both signs of `b=sqrt(a⁴-1)`. It stores each coefficient as its rational and b components. Equating both components is justified by testing both b signs, so the argument also applies to coefficients in a larger characteristic-zero constant field. The nonzero constant denominators c make every specialized series well-defined.

Exact rational row reduction gives rank124 and a12-dimensional kernel. The script records the entire kernel in `FULL-CHART-RESULT.json` and separately verifies that every unit functional selecting an L-containing monomial belongs to the row space. Thus every polynomial passing these necessary jets is independent of L. The kernel consists exactly of the following existing relations, up to signs:

    a²-c,
    c²-b²-1,
    V*Qpoint-c*W,
    a*I-b*V-c*Qpoint-V*W,
    a*K+b*Qpoint+c*V+Qpoint*W,
    I²+c*Y-c,
    K²+c*w-c,
    K*z+Qpoint,
    V²+Qpoint²+W²+2b*W-1,
    w²-w2,
    w2²-w4,
    Y²-Y2.

These are genuine identities, not merely relations caused by the five specializations. Conversely, five exact specializations suffice for the obstruction because any universal identity must pass them; no interpolation assertion is needed.

If a quadratic P defined an output L=ell+O(g^41), all other listed series are regular at g=0, so `P(ell)-P(L)=O(g^41)`. Hence P(ell) would pass the tested jets. The calculation forces P to contain no L at all. Such equations cannot constrain L. The argument covers any number of quadratic equations with this same variable interface and no extra auxiliary, and it permits implicit algebraic equations rather than assuming a rational output gate. The derivative-order tests retained in the script are redundant additional checks, not needed for this simpler conclusion.

The earlier `search.py` tests a smaller scaled-point interface and passes as well. The full model supersedes its restricted result while preserving that first experiment. The larger calculation completed in under ten seconds with standard-library rational arithmetic and one process. It expands no giant anchor integer.

## Scope and consequences

The established saving is zero. The calculation rules out replacing the separate approximation gate by a direct log-output gate using only the listed current point/cache coordinates at the same formal precision. It also shows why merely adapting the denominator to k²=1-w does not supply that deletion within this interface.

It does not rule out a different auxiliary function, changing the primary chart or power caches, coupling several points, using the shared H/ratio coordinates in an essential way, relaxing the required formal precision through a separately proved arithmetic argument, or changing the downstream logarithm protocol. It does not prove that every source rational solution is captured by the chosen formal branch. Only a universal replacement must work there. In particular this is not an impossibility proof for a V0-specific construction with fixed translation point.

No approximation was adopted, so the existing positivity, zero-point interpretation, local integrality and uniform precision claims remain unchanged. There is no new candidate or witness-equivalence claim requiring those properties to be transferred.

Reproduce with `python -B search.py` and `python -B full_chart_search.py` in this directory. The JSON outputs contain exact ranks, kernel coefficients and source incidence. `SOURCE-PINS.json` binds the source and earlier obstruction reports.
