# Scalar reciprocal chart gives 504 variables

This separate candidate adds only the scalar half of the `08-denominators` proposal to the frozen505 system. The 505 files remain unchanged. The new quartic has 504 variables including input, 503 witnesses, 473 quadratic residuals, degree four, 24,733 monomials, content one, and largest coefficient `16*3^(2^26)`. The fixed parameter remains `C=3^(2^25)`.

`candidate504-ir.json` has SHA-256 `7c17debaff9a726562be6b7ef843dbc6ca6a0a9d17556158c54ffe5c49ddb0cd`.
`polynomial504.json` has SHA-256 `a1764c08277b953c2dada7cd031fb2f4ce34d66887c8c59d77bee992fe420ac4`.

## Exact change and finite checks

Remove the eight old scalar difference coordinates for the field inverse of x(S)-x(P), slope, slope square, and ordinate product. Add the two components of each of g, d2, k and a rational f0 inverse. Preserve both components of f(R) and z(R), with R=S-P. The new equations are exactly those in `08-denominators/REPORT.md`, with no change to the V0 block.

The mixed-depth compiler had scaled the private `scalar.shiftedS.yProduct.1.quadratic` by two relative to the baseline523 compiler. The transport explicitly checks this factor before removing that coordinate. The f(R), z(R), S.h, S.j, and S.x semantic values have identical scales after the name map. A naive coordinate-name replacement without the private factor would fail the old z equation check.

`build504.py` checks those source identities and builds the complete table. `verify504.py` separately constructs the new field equations from the mixed-depth semantic values, compares every changed and unchanged row, verifies coordinate coverage, and expands every coefficient independently. It also verifies the reciprocal-curve, reciprocal-abscissa, reciprocal-ordinate, and zero-numerator factorization identities in Q(sqrt(2))[h,j]/(j^2-h^4+D). These exact checks passed.

Reproduce with `python -B build504.py` and `python -B verify504.py`.

## Source review and stronger reverse map

I accept the scalar reciprocal transformation on the inherited assumptions and the accepted505 anchor argument. Its compatibility here is stronger than the general extended-domain argument in08: every504 solution reconstructs an actual505 solution, because the retained anchor excludes the one additional branch.

Use the literal constants a=-1+(7/4)sqrt(2), b=39/8-(9/2)sqrt(2), c=a^2, D=11-6sqrt(2), and incoming S=(x,hj) with x=h^2, j^2=x^2-D. Both real embeddings make c,D positive and x nonnegative. Thus d=cx+D is nonzero. The new equations give g=(aj-bh)/d, d2=d^2, and k=(-2aDh(x+c)-bj(cx-D))/d^2. The rational guard is f0*s=1 with f=g^2, so f0=g0^2+2g1^2 and g is nonzero. The exact identity k^2+Dg^4=1 forces k nonzero: if k=0, then (3-sqrt(2))g^2=+1 or -1, whose norms give 7*Norm(g)^2=1, impossible over Q.

For x different from c, the checked identities show that 1/g^2 and k/g^3 are precisely the ordinary coordinates of S-P; hence f=g^2 and z=-g/k are the actual unchanged outputs. If x=c, the incoming chart has h=+a or -a and j=+b or -b. The g guard excludes S=P. The only remaining case is S=-P, and direct substitution gives the genuine point R=-2P. The general08 proof checks this exceptional branch against the exact doubling formula.

In the present system that branch cannot occur. The retained505 translated anchor is equivalent, by shifting w to w+C and dividing by C, to the three-witness criterion for f1(R)/C in Z_(2) intersect Z_(3). At R=-2P the already checked local starting calculation gives v3(f1(R))=2, since f is unchanged by negating a point. But v3(C)=2^25. Thus f1(R)/C is not 3-integral, contradicting the anchor. This argument uses only the genuine exceptional output and the retained anchor; it does not assume the desired large-index conclusion while defining the new chart.


Consequently every504 solution has x(S) different from c. Restore the old slope (hj+ab)/(x-c), its square, the old ordinate products, and the field inverse of x-c. Restore the private ordinate-product coordinate with its correct compiler factor two. The checked identities ensure that f(R) and z(R) are exactly the retained values. All505 equations then hold. Conversely every505 solution has x(S) different from c and extends by the displayed rational formulas, with the guard supplied by g nonzero. The new and old scalar private witnesses are uniquely determined by these outputs. This proves equality of input projections and in fact preserves every coordinate outside this private chart.

## Application obligations and limits

The source inputs are the incoming505 odd chart and its already justified interpretation as a point of 2E(K), the exact reciprocal identities, the three-witness criterion from Version11, and the local valuation calculation already reviewed for05. All use K=Q(sqrt(2)), the literal normalized curve and point, rational coefficient basis, and v3(3)=1. Every h,j sign combination over x=c was considered. The only new divisions are by d, g, k, and the positive rational f0; each has the nonzero justification above. The outputs consumed by the scalar norm and anchor are precisely f(S-P) and z(S-P). No change to primes, logarithms, scalar divisibility, or completeness choices is required, because the reverse map reaches the505 system itself.

The five V0/V1/... guard improvements and all other505 transformations remain intact. This scalar chart does not use q12 or detector chain variables, so it is disjoint from a prospective mixed-depth toric improvement. Its combination with a newly changed toric circuit still needs exact verification.

This is my independent internal review of08's scalar argument and my own composition. A separate reviewer must accept the504 composition before release. The source qualifications and unresolved global arithmetic matters in REPORT.md remain unchanged. No shared repository or505 artifact was edited.
