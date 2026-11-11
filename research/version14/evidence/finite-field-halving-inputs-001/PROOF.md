# Finite-field norm fibers and a necessary halving condition

## Finite-field norm fibers

Let ell be an odd prime. A finite subgroup G of the multiplicative group of a field is cyclic. Indeed let m be its exponent. For each prime dividing m, choose an element whose order has the maximal corresponding prime power and take its prime-primary part. Multiplying these commuting elements gives an element of order m. Every element of G is a root of X^m-1, so the polynomial root bound gives |G|<=m; Lagrange gives m<=|G|. Thus |G|=m and that element generates G.

If -1 is a square in F_ell, the invertible change (x,y) to (x+i y,x-i y) changes x^2+y^2 to a product. A nonzero product has ell-1 representations, while zero has 2ell-1. If -1 is not a square, adjoining i gives the field F_(ell^2). Its Frobenius sends i to -i, so the norm of x+i y is x^2+y^2=(x+i y)^(ell+1). The cyclic multiplicative group has order ell^2-1; this power map has kernel of order ell+1 and image of order ell-1. Its image lies in F_ell^times and hence is all of it. A nonzero norm has ell+1 representations, and zero has only the zero representation. These are exactly ell-chi(ell) nonzero fibers and ell+(ell-1)chi(ell) zero fibers used in main17572–17575.

The argument uses only finite abelian group orders, the polynomial root bound, and the Frobenius of a finite field. It does not supply the later sieve estimates or the remaining count summations.

## Necessary condition for halving a two-torsion point

Let k be a field of characteristic different from two and E be y^2=(x-e_1)(x-e_2)(x-e_3), with distinct e_i in k. Suppose Q=(u,v) in E(k) satisfies 2Q=(e_i,0). Then v is nonzero: a point with v=0 is killed by two. The tangent at Q is not vertical and, by the chord-and-tangent group law, its third intersection is -(e_i,0)=(e_i,0). Write it as y=m(x-e_i). Here m is nonzero, since m=0 would give v=0.

Substituting the line in the cubic, the monic intersection polynomial has a simple root e_i and a double root u, counted with multiplicity. Therefore

(x-e_1)(x-e_2)(x-e_3)-m^2(x-e_i)^2=(x-e_i)(x-u)^2.

After canceling x-e_i and evaluating at either other root e_j, we obtain m^2(e_i-e_j)=(e_j-u)^2. Thus e_i-e_j is a square in k. It is nonzero by distinctness. This proves only the necessary condition used in main17037–17042, not a sufficiency assertion.

For the actual roots 0,ell,-3ell over F_p, with p not dividing 6ell, p congruent to one modulo four, and ell a nonsquare, the differences -ell,ell,-4ell are nonsquares. Each nonzero two-torsion point therefore has no half. In a finite abelian two-primary group, if the subgroup killed by two has four elements and the whole group has more than four, an element of order at least four exists and yields a half of a nonzero two-torsion point. Thus the actual two-primary subgroup has order four. This last application retains the preceding prime choices, good reduction and identified curve from the caller.

The chord-and-tangent group law and the nonsingular split cubic model are explicit incoming elliptic-curve premises. This note does not establish those premises, the selected prime existence, or the later root-number conclusion.
