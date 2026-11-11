# Fixed-target reciprocal differences: a 521-variable candidate

The proposed replacement saves one rational coordinate at each of the two fixed-target differences, `V0 = H-P` and `scalar.shiftedS = S-P`. The resulting explicit candidate has **521 total coordinates, 490 quadratic residuals, and 34,467 monomials in its quartic sum of squares**. Its coefficients are integers, represented symbolically in the same fixed integer `S = 3^(2^26)`. The fixed-S content is one: the coefficient of the input's fourth power is exactly one, independent of S.

This is a candidate with exact algebraic checks and the source-level argument below. No independent acceptance of this change is claimed. The released files, manuscript, audit register, and source builders are unchanged.

## Formula and domain

Work in `K = Q(sqrt(2))`, with `D = 11-6 sqrt(2)`. Write

```
P = (a^2, a b),
a = -1 + (7/4)sqrt(2),
b = 39/8 - (9/2)sqrt(2),
c = a^2 = 57/8 - (7/2)sqrt(2).
```

Thus `b^2 = a^4-D`. The incoming chart point is
`Q = (x,hj)`, with `x=h^2` and `j^2=x^2-D`.

Use the affine expression `d=c x+D`. Introduce three field coordinates `g`, `d2`, and `k`, and impose

```
d g = a j - b h,
d2 = d^2,
d2 k = -2 a D h(x+c) - b j(c x-D).
```

Each displayed field equation consists of two rational equations of degree at most two. In particular, the right side of the third equation is quadratic because `a,b,c,D` are constants and `x` is already a coordinate.

Retain the two existing coordinates for `f`, but replace their inverse equations by

```
f = g^2.
```

Introduce one rational coordinate `s` and impose

```
f_0 s = 1.
```

The subscript denotes the rational component. Since
`f_0 = g_0^2 + 2 g_1^2`, this last equation is equivalent to `g != 0` over rational witnesses. This is the reason one rational guard suffices.

At the scalar difference, replace the parameter equations by `k z = -g`. At `V0`, no separate parameter is stored in the current 523-variable circuit. Replace its combined logarithm equations by

```
k ell_40 = -g G_9(D f^2).
```

The polynomial `G_9` and its existing circuit are unchanged. Its output is affine in stored coordinates, so these equations also remain quadratic.

The incoming chart implies that `x` is positive under both real embeddings. Both `c` and `D` are positive under both embeddings. Consequently `d` is never zero. The new equations uniquely fix `g,d2,k,f`, and then `s` whenever `g != 0`.

The polynomial identity

```
k^2 + D g^4 = 1
```

holds after the defining equations. If `k=0`, then `(3-sqrt(2))g^2` is either `1` or `-1`. Taking the field norm gives `7 Norm(g)^2=1`, impossible for rational `Norm(g)`. Thus `k != 0`. No unguarded division remains.

## Identity with the actual group difference

Let `N=a j-b h`, `M=-2aD h(x+c)-b j(c x-D)`, so `g=N/d` and `k=M/d^2`.

For `x != c`, use the ordinary subtraction formula

```
m = (h j + a b)/(x-c),
x_R = m^2-x-c,
y_R = m(x-x_R)-hj.
```

The exact identities checked in `check_reciprocal.py` give

```
x_R = 1/g^2,
y_R = k/g^3.
```

Therefore `f=1/x_R` and `-g/k=-x_R/y_R`. The logarithm output is precisely the old `ell_40(R)`, with no scalar or sign change.

For the formerly excluded case `x=c`, the chart gives `h=+/-a` and `j=+/-b`. The identity

```
(a j-b h)(a j+b h) = (x-c)(c x+D)
```

shows more generally that `g=0` occurs exactly when `Q=P`. The guard excludes that identity difference. The other two sign choices give `Q=-P`. Direct substitution in the formulas gives the coordinates of `R=-2P`; the exact arithmetic check compares them to the ordinary doubling formula for `-P`. Simultaneously replacing `(h,j)` by `(-h,-j)` replaces `g,k` by `-g,-k`, leaving `1/g^2`, `k/g^3`, and `-g/k` unchanged.

Thus every new solution supplies exactly the reciprocal abscissa and local parameter of the true finite nonidentity point `Q-P`. It does not introduce a fake point at the old slope's `0/0` branch.

## Witness maps and downstream use

Every old solution extends to a new one by the formulas for `d,g,d2,k`, setting `f=g^2` and `s=1/f_0`. The old guard `x != c` ensures `Q != P`, so this map is defined. Keep all other witnesses and the existing `f`, `z`, and logarithm outputs.

Conversely, every new solution with `Q != -P` reconstructs the old difference block by `m=(hj+ab)/(x-c)`, its square, the old ordinate, and the old inverse of `x-c`. The reciprocal identities prove that all preserved outputs agree. At `Q=-P`, the old *coordinate chart* cannot be reconstructed, but the new outputs are those of the valid point `-2P`.

That last distinction is material. This replacement is not claimed to give an all-witness bijection to the old guarded straight-line program. Its input-projection argument uses the arithmetic proof's actual consumers:

* `manuscripts/quartic_v11.tex`, `lem:v5-point-domains`, lines 10773 onward, needs the differences to be finite nonidentity points of `2E(K)` with nonzero abscissa and ordinate. The new chart supplies exactly that. Both incoming points are in `2E(K)`, and so is their difference. The displayed reciprocal identity and the guard give nonzero coordinates directly.
* `docs/quartic-523-540/addition.tex`, lines 104-112, consumes `V0=H-P` with index `h-1`. This equality remains literal at `H=-P`; its index is then `-2`. The fact that one of `h,h-1` is a unit is unchanged. No division by `h+1` occurs there.
* The asymmetric comparison at addition lines 495-527 uses precisely `f(V0)` and `ell_40(V0)`, and the ratio `(u_i-n_i)/(h-1)`. These are unchanged functions of the genuine group difference. Its nonzero denominator conditions are preserved.
* The scalar block and anchor consume `R=S-P`, `f(R)`, and `z(R)`. These also remain literal and nonzero. In particular `S=-P` gives the genuine point `R=-2P`, not an artificial slope output. The same anchor and scalar statements apply to that point. Their eventual large-divisibility consequence would exclude this small index; no such consequence was used to define the new chart.
* Completeness needs no new real or prime selection argument. The old choices already avoid the old excluded loci, and the forward witness map carries every old solution into the new system.

The repository's audit protocol requires a separate reviewer before this revised route is accepted or released. The mechanical scripts do not claim to satisfy that independent-review requirement, and this work does not alter the earlier arithmetic source qualifications.

## Exact count and files

For each fixed-target occurrence, the old local block has two coordinates each for the `x`-difference inverse, slope, slope square, ordinate, reciprocal abscissa, and parameter or combined logarithm. This is twelve rational coordinates.

The new block has two coordinates each for `g,d2,k,f` and the parameter or combined logarithm, plus one rational guard. This is eleven. Both instances are disjoint, so `523-2=521`.

`build_candidate.py` starts directly from the released, already reduced 523-coordinate IR. It removes coordinates `100..107` and `500..507`, adds fourteen coordinates, changes the eight reciprocal and output equations, and checks that every surviving coordinate is active. It therefore measures the saving after the published eliminations, rather than only in an unreduced builder.

* `candidate-521-ir.json`: explicit 521-coordinate system with integer residuals.
* `candidate-521-polynomial.json`: complete sparse quartic sum of the residual squares.
* `candidate-checks.json`: count, degree, coefficient, removed-coordinate and changed-row checks.
* `checks.json`: exact reduced polynomial identities, exceptional-point check, and inventory of all original inverse witnesses.
* `check_reciprocal.py`: independent standard-library rational-field identity checks.
* `build_candidate.py`: reproducible local replacement and polynomial expansion.

Run both scripts using the supplied Python runtime with `-B`. They need no third-party packages and write only into this directory.

## Other inverse directions examined

The source contains six field slope guards, eleven field reciprocal-abscissa witnesses, three rational detector half-trace guards, and the scalar rational inverse. The slope-guard witnesses are used only in their defining rows. The reciprocal abscissae and scalar inverse have live downstream uses.

Deleting a slope guard is unsound as a local replacement. At `Q=-P`, put `m=0` in the unguarded old slope equations. They admit `x_R=-2c`, `y_R=ab`, which is not a point of the curve. The exact curve defect is `3894993/512 - (681645/128)sqrt(2)`. Nonzero `x_R` and `y_R` do not repair this issue.

A generic norm guard for an arbitrary field denominator uses a norm coordinate and its rational inverse, still two coordinates. Combining independent nonzero guards in a product chain gives no saving unless some product coordinates already exist. No such shared products were found among the six slope denominators.

The three detector `w0` guard replacements and the other agent's five half-trace replacements were not attempted. The scalar preparation already absorbs its former separate inverse. The scalar inverse itself is used by its five-step squaring chain and by norm-tree leaves, so treating it as a guard alone would overlook live uses of its coordinate.
