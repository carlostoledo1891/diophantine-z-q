# Eliminating the reference reciprocal while retaining its square

This author proposal starts from the independently accepted raw235/209 system. It preserves that system and its sparse presentation unchanged. The new construction has233 variables and207 quadratic residuals; finite implementation and independent review are pending.

## Notation and exact replacement

Use original raw237 coordinate names throughout this proof:

    K=Q(r), r²=2, D=11−6r,
    f=x19+r*x20, S=x21+r*x22, v=x23+r*x24,
    g=x139+r*x140, B=x86+2r*x87=f²,
    w=x33+2r*x34=v²,
    a=57−28r, b=8−14r, c=88−48r, d=39−36r,
    A=a+c*f, N=8−a*f−2d*g.

The accepted235 system already deleted original coordinates17 and18 and retains the field equations

    F=A*g+b*f*S+d*f=0,
    E=(b*S−d)*g−a*f+8=0.

The remaining occurrences of v are exactly G=g²−f*v=0 and w−v²=0, originally rational rows5–8. Delete the two coordinates of v and those four rational rows. Replace them with the two rational components of

    (a²+2ac*f+c²*B)*w−N²=0.

Because B is an already retained square output, the coefficient of w is affine in the retained coordinates. N is affine in f,g. Thus the replacement has degree at most two. Every other row, including B=f², F, E, the square-output consumers of w, and the original scalar parity core, is retained literally through the deletion map. The count is235−2=233 variables and209−4+2=207 residuals.

In raw235 coordinates, the deleted pair is21/22, B is84+2r*85 and w is31+2r*32. The finite constructor must confirm the complete occurrence census and index map.

## Nonzero denominator established before reconstruction

The exact identity

    F*(b*S−d)−A*E=b²*(f*S²−1+D*f²)

uses no v or w. It therefore holds unchanged after their defining rows are replaced. New solutions satisfy the old H curve and f!=0. The original scalar parity block, also unchanged, then forces v149(Norm(f))>7nu/4>0 in the admitted A_N=149^(2N+1) family, with nu=v149(Rscalar)>0 odd.

If A vanished, f=−a/c would have Norm(f)=(41/56)², a149-adic unit. This is impossible. Thus A!=0 on every new solution before any reconstruction of v. This step depends only on F/E, f/B, and the retained scalar and normalizer equations. It does not assume G or a meaning for w. The detailed scalar valuation argument is the independently accepted direct235 proof, whose implication here uses only those retained inputs.

## New to accepted235

Recover v=N/A. The replacement equation and B=f² give A²*w=N², hence w=v². By construction Q=A*v−N=0. Define R=A*v+b*S*g+d*g. Then R=Q+E=0. The polynomial identity

    F*g−A*(g²−f*v)=f*R

gives A*G=0 and therefore G=0. All four deleted rational rows are recovered. Every other accepted235 row is unchanged.

## Accepted235 to new

On an accepted235 solution, F=E=G=0 and f!=0. The last identity gives R=0, hence Q=R−E=0 and A*v=N. The retained square equation w=v² then implies A²*w=N². Thus deleting the two coordinates of v yields a new solution.

## Maps and scope

Forward, forget v and apply the index deletion. Backward, restore v=N/A in K, with its two rational components, and retain every other coordinate. These maps are inverse because accepted235 solutions also satisfy A*v=N. They fix the distinguished input and A_N. There is no division by g,S,w or either rational component of A; division is by the nonzero field element A. Zero rational components and all other permitted zero strata remain allowed.

This is a fixed-input bijection for the admitted family, not arbitrary symbolic A_N. The sufficient defining threshold remains ineffective. The exact quartic expansion, all-coordinate count, coefficient profile and any sparse presentation require separate finite construction and independent review. No V14/V15 or release file is changed.
