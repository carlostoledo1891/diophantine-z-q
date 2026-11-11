# Independent review of the reciprocal differences

I accept the two fixed-target reciprocal replacements in proposal 08 on the
inherited arithmetic assumptions of the manuscript. I also accept the scalar
replacement from the frozen 505-variable candidate to the frozen 504-variable
candidate, as an equivalence of projections preserving every coordinate
outside that private scalar chart. This is independent internal model review
of proposals I did not author. It is not an independent revalidation of the
505-variable system, the earlier single-coefficient anchor that I authored,
or the manuscript's global arithmetic results.

No mathematical defect was found in the reciprocal formulas, their guards,
the exceptional-point argument, or the checked implementations. There is one
important transport factor: the old scalar `yProduct.1` coordinate equals twice
the same-named coordinate in 505. The 504 implementation accounts for it.

## Artifacts and checks

The reviewed proposal is `08-denominators/REPORT.md`, SHA-256
`d912036d5744b49d895f92081fcbe23dc35c04f0b2ea64f77ab0fcf81f37e658`.
Its candidate `candidate-521-ir.json` has SHA-256
`4607e9ed9cfefd4fe8f06dcc128c877b7a1d34a063863014deff0cacb4997a9a`.

The 505 baseline has SHA-256
`bd9aca7a4a31476e426660d1a33de33552f2a5019bec06104b45938d59f4b966`.
The reviewed `10-combination/candidate504-ir.json` has SHA-256
`7c17debaff9a726562be6b7ef843dbc6ca6a0a9d17556158c54ffe5c49ddb0cd`.
Its report has SHA-256
`18af40d1235ee2913ce80d2c0459e8c822cd05275af1406753b96ec3cb0510b4`.

I wrote `review_reciprocal_check.py` without importing either proposal's
producer or checker. It performs the following exact checks.

* Six generic polynomial identities, over
  Z[a,b,h,j]/(j^2-h^4+a^4-b^2), including the group-law identities and the
  exceptional minus-P doubling identities, have zero remainder.
* All 22 changed or added residuals in the 521 candidate agree with a fresh
  reconstruction from the stated field equations, up to nonzero rational
  normalization. All 468 other residuals agree with the pinned 523 baseline.
* The complete sum-of-squares expansion equals the saved 521 polynomial.
  It has 521 coordinates, 490 residuals, and 34,467 coordinate monomials.
* All twelve old scalar-chart rows transport to 505 with the single factor
  two described above.
* All eleven changed or added scalar residuals in 504 agree with the freshly
  reconstructed formulas. Every other row agrees with 505. The complete
  expansion equals the saved 504 polynomial: 504 coordinates, 473 residuals,
  and 24,733 coordinate monomials.

The checked hashes and results are in `review-reciprocal-checks.json`.
Run `python -B review_reciprocal_check.py` to reproduce. It writes only in this
review directory. A passing polynomial check does not by itself establish
the arithmetic arguments below.

## Formula, denominator, and exceptional-point review

Set D=a^4-b^2 and c=a^2. In the actual application,

    a=-1+(7/4)sqrt(2), b=39/8-(9/2)sqrt(2), D=11-6sqrt(2).

Thus P=(c,ab) is exactly the manuscript's normalized generator. For the
incoming chart Q=(h^2,hj), put x=h^2, j^2=x^2-D and

    d=cx+D,
    N=aj-bh,
    M=-2aDh(x+c)-bj(cx-D),
    g=N/d, k=M/d^2.

Each real embedding makes c and D strictly positive and x nonnegative.
Consequently d is strictly positive, so both equations involving d uniquely
determine their intended values. There is no additional denominator locus.
The stored d2 equation is genuinely quadratic, as is the M equation: h*x
and j*x are quadratic because x is already a stored coordinate.

The independent quotient-ring checks establish

    M^2+D*N^4=d^4,
    N(aj+bh)=(x-c)d.

The former gives k^2+Dg^4=1. Since D=(3-sqrt(2))^2, k=0 would imply
(3-sqrt(2))*g^2=1 or -1. Taking the field norm gives
7*Norm(g)^2=1, impossible for a rational Norm(g), by the odd 7-adic valuation.
Thus k cannot vanish. This argument does not presuppose the output point.

The rational component of f=g^2 is f0=g0^2+2g1^2. Over rational witnesses,
f0 is nonzero exactly when g is nonzero. The equation f0*s=1 is therefore
an exact one-coordinate guard. No ordered-field assumption is imposed on
the quantified field coordinates; this argument uses that their components
are rational and Q is an ordered field.

For x different from c, write m=(hj+ab)/(x-c). The checked identities imply

    m^2-x-c = d^2/N^2 = 1/g^2,
    m(x-d^2/N^2)-hj = M*d/N^3 = k/g^3.

These are the ordinary subtraction formulas, with the sign appropriate to
Q-P. Hence the new outputs are literally f(Q-P)=g^2 and
z(Q-P)=-g/k. The V0 equation also gives exactly
ell40(Q-P)=(-g/k)*G9(D*f^2), with the same polynomial and no sign change.

If N=0, the second identity and d nonzero force x=c. As a,b are nonzero,
h=+a or -a and j=+b or -b. N=0 selects the two sign choices with hj=ab,
which are exactly Q=P. Conversely those choices make N zero. The guard
excludes exactly the identity difference on this locus.

The remaining sign choices have Q=-P. Independently of any continuity
claim, put h=a,j=-b and q=2ab. Then N=-q and d=c^2+D. The usual tangent
slope for doubling -P is -(3c^2-D)/q. Clearing q^2 and q^3 in its x and y
formulas gives exactly d^2/q^2 and -M*d/q^3. These equal 1/g^2 and k/g^3.
The checker verifies both generic identities. Replacing h,j by -h,-j
negates g,k and leaves the output point and -g/k unchanged. Every sign
choice is covered. The added branch is the true point -2P, not a solution
of an unguarded zero-over-zero slope equation.

## The 521 input-projection argument

The old solutions extend by the displayed rational formulas and s=1/f0.
The old x-c guard ensures Q is neither P nor -P, so all denominators are
nonzero. The existing outputs f,z,ell stay unchanged. This proves the
required completeness direction without any altered prime or real choices.

For soundness, the only newly allowed points occur when an incoming point
equals -P. At such a point the chart produces the actual difference -2P.
The manuscript's `lem:v5-point-domains` requires finite nonidentity points
of 2E(K), with nonzero abscissa and ordinate. The new chart supplies exactly
those objects: its outputs lie on E, are nonzero, and equal the actual
difference of two points of 2E(K). This uses no new rank assumption.

The actual consumers were checked in Version 11. `lem:v9-bridge` consumes
V0=H-P with integer index h-1; `subsec:v9-local-depth` consumes the actual
f(V0), ell40(V0), and ratios (u_i-n_i)/(h-1). At H=-P the index is -2,
not zero. The fact that one of h,h-1 is a unit is still true. The formal
branch hypotheses come from the unchanged pole tests; they do not require
the unrelated inequality h!=-1. The existing quotient equations continue
to guard every used ratio. None of these arguments uses a factor h+1.

The scalar norm and physical anchor consume the actual f(S-P), z(S-P).
The reciprocal scalar replacement preserves these objects as well. Their
statements allow negative nonzero indices; no positivity of a-1 is assumed
in soundness. The old two-coefficient anchor would itself exclude S=-P,
because the genuine f(-2P) has 3-adic depth two, far below the anchor depth.
Thus this scalar exceptional case cannot survive the full 521 equations.

I therefore accept the revised local domains for the 521 soundness proof.
This is a projection argument using the arithmetic consumers, not a claimed
bijection with every old guarded witness tuple. It leaves the source's
height theorem, prime-pattern theorem, and restricted converse unchanged.

## Compatibility and equivalence from 505 to 504

The scalar block in 505 has the same input and output functions as the 523
baseline. The exact row comparison found that

    old scalar.yProduct.1 = 2 * combined scalar.yProduct.1.

Its defining coefficient changes from -1 to -2 and its two z-consumer
coefficients double consistently. All other scalar-chart coordinates
transport by their names. This is a harmless private-coordinate scaling,
and the 504 replacement deletes that coordinate entirely. Treating all
same-named coordinates as equal would nevertheless give an incorrect
verification, so recording this factor is necessary.

The 505 anchor is the displayed quadratic condition

    u^2+6v^2-2w^2-4Cw-3f1^2=0, C=3^(2^25).

By w_old=w+C it is the three-witness criterion for f1/C to be integral at
2 and 3. On the only extra scalar branch, S=-P and R=-2P. The exact local
calculation at 2P, and f(-2P)=f(2P), give v3(f1(R))=2. Thus f1(R)/C has
negative valuation and contradicts this retained anchor. This exclusion
uses the computed exceptional output, not a conclusion about a prospective
large index, so there is no circular assumption of chart equivalence.

Every 504 solution therefore has x(S)!=x(P). Restore the ordinary difference
inverse, slope, square, and ordinate products, including the factor two.
All 505 rows then hold with the same retained coordinates. Conversely,
every 505 solution has the displayed unique lift to the new scalar chart.
This proves equivalence of the two complete rational solution projections.
No new global argument, contact-prime choice, or compatibility of separate
existence constructions is required for this last step.

The scalar change saves one coordinate and one residual. At V0, the 505
system has already saved one coordinate using the half-trace guard, so the
reciprocal V0 chart would not provide another count saving. Leaving that
block unchanged, as 504 does, is consistent.

## Scope of acceptance

The field, coefficient basis, point, integral valuation normalization, and
all exceptional points have been matched to the constructed system. All
new divisions have explicit nonzero proofs. The mapped objects are exactly
those consumed downstream. The 521 argument covers the slightly larger
chart domain; the 504 argument restores the old scalar domain using the
retained anchor. Completeness follows from existing solutions in each case.

This review accepts those relative transformations and their frozen
implementations. It does not manufacture a repository acceptance record,
change any historical disposition, or approve the broader inherited
arithmetic theorem. Earlier source inputs were found at the cited manuscript
passages; historical priority of these reciprocal formulas is not assessed.
No shared file was modified.
