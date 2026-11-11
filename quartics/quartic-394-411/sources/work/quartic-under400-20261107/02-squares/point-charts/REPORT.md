# Four smaller odd-root charts

This packet replaces each four-coordinate odd-root augmentation by three rational coordinates. Applied to the pinned 453-variable source, it gives 449 variables, 448 witnesses, 426 quadratic residuals and 6,536 quartic monomials. The input is unchanged. The quartic has content one and largest absolute coefficient `16*3^(2^26)`, with the same fixed `C=3^(2^25)`.

Status: candidate awaiting independent non-author review. The only arithmetic inputs used below are the point-chart and squareclass facts already proved and consumed in Version 12. This does not revalidate the manuscript's inherited arithmetic theorem. No published input or earlier packet was edited.

## Pins and scope

The source is `10-combination/rational453-ir.json`, SHA-256

```
f90ee69b7f26d43e94f6a7bb255d3cf2e040d5a2746d79c3b13e08a35185998f
```

The result is `candidate449-ir.json`, SHA-256

```
f5a9471dd06bfdfe382b10481fdcf0c7ddfd7184386f1e667a00efdae4ea115e
```

The complete coefficient table is `polynomial449.json`, SHA-256

```
4589dfb06d75f3b136c6ac2b72809aa110c85c4b61c70abd9f2153ec81a149e1
```

`certificate449.json` pins the source, semantic precursor and whole Version 12 manuscript and records every changed row and coordinate. The semantic precursor has SHA-256 `4466bd973383ba404b1cc50deaf2aa4f77361850c090dc8af80b7ba77249d57c`.

The relevant mathematical sources in `manuscripts/quartic_v12.tex` are the specific square-abscissa chart proof in the Version 9 section; `v9:eq:odd-chart` and `v9:prop:odd-chart`, around lines 19527-19581; and especially the squareclass decomposition around lines 19552-19563. The same inputs are retained explicitly in `subsec:v12-inputs`. The new statement concerns the exact existing h,j,x representations, not only their projected elliptic points.

## Existing and replacement equations

Put K=Q(rho), rho^2=2, epsilon=1+rho, d=3-rho and D=d^2=11-6rho. The retained chart coordinates h,j,x in K satisfy

```
x=h^2,
j^2=x^2-D,
Q=(x,hj).
```

The source proves h,j,x nonzero and Q a nonidentity point of 2E(K), where E is y^2=x^3-Dx. For an odd root, the old private witnesses t,r in K satisfy

```
t^2=2(x+j),
th+x+j=epsilon*r^2.                         (Old)
```

Replace t,r by a in K and u in Q satisfying

```
a^2-2(x+j)a-D=0,
Norm_K/Q(a)+u^2=0.                         (New)
```

The first equation means two rational quadratic equations. If a=a0+a1*rho, the second is the single rational quadratic equation

```
a0^2-2a1^2+u^2=0.
```

Thus three coordinates and three residuals replace four coordinates and four residuals. Make this replacement separately for the roots A,S,T,Z. All h,j,x coordinates and all their consumers remain unchanged.

## Old-to-new map

Given Old, set

```
a=epsilon*r^2=th+x+j,
u=Norm_K/Q(r).
```

Since Norm(epsilon)=-1, the norm equation follows immediately. Write s=x+j. Then

```
a^2-2sa-D = t^2 h^2-s^2-D
            = 2sx-s^2-D
            = x^2-j^2-D
            = 0.
```

This is a polynomial map on the private witnesses and leaves every outside coordinate fixed. There are no denominators.

The exact residual identity checked by the verifier is the following. Let A=x-h^2, B=j^2-x^2+D, C=t^2-2s and K0=th+s-a. Then

```
a^2-2sa-D = h^2 C-2s A-B-2th K0+K0^2.
```

It is also checked that Norm(epsilon*r^2)+Norm(r)^2 vanishes identically in the two rational components of r.

## New-to-old map: constructing a half-point

Suppose New holds. The retained chart has h nonzero. Also s=x+j is nonzero, since s=0 would imply x^2-j^2=0, contrary to D nonzero. The first new equation implies a nonzero for the same reason. Its norm is nonzero, so u is nonzero as well.

Define

```
t=(a-s)/h.
```

The new equation and the retained chart identity give

```
(a-s)^2 = D+s^2 = 2xs = 2h^2s,
```

hence t^2=2s and th+s=a. In particular t is nonzero. The point

```
R=(a,at)
```

lies on E, because a*t^2=a^2-D. Its ordinate is nonzero.

The tangent slope at R is h+t. Indeed 2at(h+t)=3a^2-D. The duplication formulas then give

```
x([2]R)=(h+t)^2-2a=h^2=x,
y([2]R)=(h+t)(a-x)-at=h(t^2/2-x)=hj.
```

Thus [2]R=Q with exactly the retained h,j representation. These are checked polynomial identities, not an appeal to a possibly different half-point.

## Norm condition and the two-torsion ambiguity

The inherited statements are

```
2E(K)=ZP,
P=2R0,
E[2](K)=<T0,Td>,
T0=(0,0), Td=(d,0),
alpha(R0)=[epsilon], alpha(T0)=[-1], alpha(Td)=[d].
```

The squareclass homomorphism alpha sends a point of nonzero abscissa to the class of that abscissa. Every R in E(K) has the form

```
R=mR0+eT0+fTd,
m in Z, e,f in {0,1}.
```

This follows directly from the retained equality 2E(K)=ZP and P=2R0. Consequently

```
[a]=[epsilon]^m[-1]^e[d]^f.
```

Take norms modulo rational squares. Norm(epsilon)=-1, Norm(-1)=1 and Norm(d)=7. New says [Norm(a)]=[-1]. Therefore

```
[(-1)^m 7^f]=[-1] in Q*/Q*^2.
```

The sign forces m odd. The remaining condition forces f=0 because 7 is not a rational square. Hence [a] is either [epsilon] or [-epsilon]. This uses only the existing squareclass decomposition, with its exact field and fixed constants; an arbitrary element of K with negative square norm would not be enough without the elliptic-point condition.

If [a]=[epsilon], choose r in K with r^2=a/epsilon. Together with the constructed t, this gives Old.

If [a]=[-epsilon], use the other root

```
a'=2s-a=-D/a,
t'=-t.
```

The identity a*a'=-D follows from New, so a' is nonzero. It is the abscissa of R+T0, and its squareclass is

```
[a']=[-D]/[a]=[-1][a]=[epsilon].
```

Choose r in K with r^2=a'/epsilon. We still have (t')^2=2s and t'h+s=a'. Thus Old holds with t',r and with exactly the original h,j,x. No outside chart sign is changed. This resolves the two-torsion ambiguity instead of incorrectly inferring [a]=[epsilon] directly from the norm.

The choice of r is an existential square root supplied by the established squareclass equality. This is not claimed to be a unique rational-function inverse on the private coordinates. It proves equality of the rational projections onto every outside coordinate, which is what the construction requires.

## All zero and exceptional cases

- D is the fixed nonzero square (3-rho)^2.
- h is nonzero by the retained specific point-chart proof, so defining t is valid.
- s=x+j is nonzero because (x+j)(x-j)=D.
- a is nonzero because the new quadratic has constant term -D.
- u is nonzero because a has nonzero field norm.
- t is nonzero because t^2=2s.
- R has nonzero ordinate at and is a valid finite point for the tangent formula.
- a' is nonzero because a*a'=-D.
- The sign and rational-square arguments apply equally to negative or positive integer m.

There is no new inverse coordinate, real inequality, integrality assumption on a witness, or prime-selection condition.

## Actual source and simultaneous consumers

The source uses different scalar normalizations for some x components, including the T chart's real component. The builder reads their exact semantic expressions from the pinned precursor, transports them by coordinate name and checks all four old odd equations before replacing them. The verifier independently checks both retained chart equations for every root and the exact old and new component equations.

The old t,r coordinates have no consumers outside their four private odd equations. Every residual outside those sixteen rows is identical in the candidate. In particular the following remain literally unchanged:

- the root point h,j,x values and height-product circuit;
- all comparison slopes or reciprocal-chart outputs and their inputs;
- the scalar point S-P, its norm block and physical anchor;
- every logarithm, test, detector and pole equation.

Thus all four replacements work simultaneously. They are also disjoint from the primary-parameter removal being developed from the same 453-variable source. A future composition must still compare its actual source rows and semantics before combining them.

The numeric savings are from 453 to 449 in this packet. They must not be added twice when another combined source already includes the same replacement.

## Executable checks

Run

```
python -B build_odd_norm.py
python -B verify_odd_norm.py
```

`verify_odd_norm.py` imports no producer. It checks all source hashes, exact chart and odd-equation normalizations, private-coordinate incidence, unchanged outside rows, the generic half-point/duplication/involution/norm identities, surviving coordinate coverage, primitive integer normalization and every coefficient in the complete sum of squares. It verifies degree four, 6,536 monomials, content one and the unchanged maximum coefficient. The output is recorded in `verification449.json`.

These checks passed. The arithmetic use of the inherited squareclass decomposition is separately reviewable in the argument above and is not claimed to follow merely from polynomial expansion. Agent03 has been asked to provide that independent review before this candidate is accepted or combined.
