# Independent acceptance of the 423-variable composition

Accepted for the frozen research composition below. I authored neither
combined423 nor its accepted combined431 source. This review checks the
renewed interfaces between the identity-inclusive comparison charts, H.j
rescaling, the scalar f1 guard and the scalar depth-24 construction. It
includes independent finite transport and full polynomial verification.
The inherited global arithmetic inputs remain dependencies.

| Object | SHA-256 |
|---|---|
| Source `combined431-ir.json` | `180968baa12a26f0171eeeb337df61b293a3a122786929e28b9fc94c55ba5573` |
| Component source `combined435-ir.json` | `c4c8a0623be27e675f73363043ce2bc44956bd128257060e471abca9b53a0859` |
| Component `inputs/identity-chart427-ir.json` | `6e23d292a93d49037d63a72f4dddca33179404a9e8e4467397c168d3862a0ea4` |
| Author `REPORT423.md` | `2b97f78a85ff62ef3ee5b498388e52efda03257d9d218c9152ccb6e349034f6e` |
| Result `combined423-ir.json` | `3c19ce0d46ae80732e76fd243b7fd1c91599f4274e1c67b9a4ac6c5bd86899bf` |
| Polynomial `combined423-polynomial.json` | `a6342d78d4ac081f59dfd11599e725e93f52f945b21b7f1d54391c2779045689` |

These paths are under `10-combination`. The result has 423 total variables,
422 witnesses, 392 quadratic residuals and 6,172 quartic monomials. It has
degree four, content one and largest coefficient exactly 16*3^(2^26).

## Sources reviewed and finite binding

I read the author report, builder and verifier, the accepted 431 composition
review, the depth-24 argument and review, and the H.j-rescaling argument and
review. I compared them with the source applications already examined in
`review-identity-extension.md`, in particular the actual formal-log and
one-place proofs, product-height corollary, scalar anchor and final height
consumers in `manuscripts/quartic_v12.tex`, SHA-256
`5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`.

The new `review_composition423_check.py` imports no producer or other checker.
It rediscovers the component delta from the 435 and 427 files and checks its
preimages against the actual 431 source. It verifies every changed row,
deleted row, added row, coordinate removal and coordinate reinterpretation.
It also checks the complete incidence of reinterpreted and removed
coordinates against their component-source meanings. Every outside row
and retained coordinate record matches its proper source object.

The physical delta removes coordinates 92–99 and reinterprets forty old
coordinate slots. Sixteen same-named rows change, 56 old row names disappear,
and forty new row names appear, for a net removal of sixteen rows. The
changed row IDs in the combined file are checked for uniqueness; they need
not equal the component's row IDs. Input and fixed-parameter data are
preserved. The independent sum-of-squares expansion matches every frozen
coefficient and every coordinate occurs in the polynomial.

## Current H and V0 interface

The 431 source no longer stores H.j. In the actual 423 equations, write h,x,f,s
for H.h, H.x, f(H), and the common negative reciprocal of z(H). They satisfy

    x=h^2,                       x*f=1,
    s^2-x+D*f=0.

The checker matches both rational components with their actual scaling;
in particular the second component of x is twice coordinate 91. Thus h and
x are nonzero. Set j=h*s. This reconstructs j^2=x^2-D, so it reconstructs
the same finite H as in the accepted source. Its nonzero j domain follows
from that source's curve argument; it does not come from an individual
rational-component guard.

Let v denote the current V0 slots 700/701, which store g/h, not the older g.
The actual equations are

    d*v=a_*s-b_*,                 d=a_*^2*x+D,
    v^2=f(V0)*f,
    Tprime*ell0+a_*(a_*s-b_*)*R0=0,
    Tprime=-2D-a_*b_*s+2D*b_*v.

The checker verifies these rows using the literal rational approximation
output R0 in slots 186/187. Setting oldg=h*v and j=h*s recovers the old
V0 reciprocal and logarithm equations. The factors canceled are h or x,
already nonzero on the whole domain; no division by v, ell0, or a numerator
has been introduced. This reconstruction is therefore valid at v=0 too.
The primary ratio parameter remains s=j/h=-1/z(H), exactly the one consumed
by J*L_i=r_i*s in the new primary charts.

## V0 exclusion before interpreting logarithm ratios

The old V1-nonzero proof is not reused. If the current V0 represents O,
its reciprocal square is zero. Since f(H)!=0, v^2=f(V0)*f(H) gives v=0
and hence oldg=0. The reconstructed old equations imply H=P, with the
correct ordinate orientation. Algebraically their remaining factor is
(x-c_*)(c_*x+D)=0, and the second factor is strictly positive.

Consequently the actual retained f(H) is

    8*(57+28sqrt(2))/1681,

with norm 64/1681. It is a unit at every place above every consumed prime
p>76176. The unchanged one-place detector lemma nevertheless forces the
retained order-40 f(H) test at any prime in any of the three contact
radicals. This is impossible. The one-place theorem allows arbitrary
field tests, including zero; it does not require the other approximate
ratios to have been interpreted. All its detector nonzero domains and
pole equations are unchanged by the composition.

Thus all three radicals are 1. The root-scale height corollary, applied
with N=1, gives B^2-6<7Hcal. Its inputs are precisely the unchanged odd root
points Q1,...,Q4, their product, and their three positive rational-square
scales. It contains no primary or alternate logarithm ratio.

The unchanged physical scalar anchor gives log2(kappa)>25165823.5 for
kappa=|s_index|. The root label a=s_index+1 satisfies B>=|a|>=kappa-1.
With Hcal<2^2093966 and Hcal>=1, the retained exact comparison

    10*(7+2093966)<25165823.5

still implies |a|>(40Hcal)^10. This contradicts B^2-6<7Hcal. The exclusion
uses neither the scalar contact-height upper bound nor any L or LP
congruence. In particular the reduction of scalar divisibility from 32
to 24 cannot invalidate or make circular this argument.

It follows that V0 is nonidentity. Its actual logarithm equation then
gives ell0=z(V0)*R0!=0 by the same positive rational approximation factor
on 0<w<1. Both denominator functions z(H) and ell0 have now been justified
before any numerator-zero case is analyzed.

## Identity points and local comparison consumers

For i=1,...,4 the exact transplanted charts have the same interpretation
as the accepted component: U_i is finite if its reciprocal r_i is nonzero,
and is O for r_i=0. The computed V_i is U_i-Q_i, including V_i=O, U_i=O
and the equal-abscissa doubling case. The root Q_i remains nonidentity.
The relevant denominators d_i and k_i keep their positivity and norm-seven
proofs because their root inputs and field D are unchanged.

The actual primary equation gives L_i=z(U_i)/z(H), including L_i=0.
Every alternate-log row and every rational approximation row is literally
unchanged from the accepted 431 source. These rows are also unchanged
from the accepted component wherever needed by the component's zero-value
argument. At V_i=O their live fused consumer is ell0*LP_i=0, so LP_i=0.
The common ell0 is now nonzero. No removed affine x-coordinate is consumed
elsewhere and no zero logarithm is divided out.

The source-level unit identities use the regular series A with
log(Q)=z(Q)*A(Q), A(O)=1, and the regular truncation factors T(O)=1.
They give each approximate ratio as its rational index ratio times an
explicit unit, even when the index ratio is zero. One of h,h-1 is a p-unit,
so one index ratio is integral; the positive-order cross-test transfers
integrality to the other before the improved depth of U_i is used.
For U_i=O its error is exactly zero. Otherwise the unchanged order-40 f(H)
test and integrality give depth at least twenty and primary precision 80.
The alternate precisions are still 12 and 40, which suffice for the actual
cross orders 10 and 40. Multiplying by h and h-1 and subtracting yields the
same root-label congruences, including both zero cases and both split and
inert completions.

## Scalar depth, f1 guard, odd labels and final height arguments

The checker separately matches the current scalar equations

    Q=q^2=v311^2-8*v312^2,
    r^32*B=z0^2+r*z1^2,
    r^32*W=B^2+r*Q,

and each remaining power-chain row. The z0,z1 slots remain the actual
scalar ratio coefficients from accepted 431. The primary comparison-chart
change alters none of the scalar reciprocal, ratio, pole, correction,
f1-inverse or anchor rows. In particular the literal anchor remains

    v55^2+6*v56^2-2*v57^2-4*C*v57-3*v505^2=0.

Coordinate 505 remains the same scalar f1, and its guard is unchanged.
Thus the nonzero even scalar orbit and the anchor's subgroup interpretation
are preserved, despite the independently enlarged comparison-point domain.

The accepted scalar argument still gives M5(beta)^24 dividing s_index and
h(beta)<=Hcal*kappa^(19/24). The exact comparison

    (5/24)*25165823.5>2093966+7

still supplies the needed h(beta)<|a|/40 margin. The independent logarithmic
margin is retained as well. The four odd-root equations, their actual
points and their height-product rows are unchanged. Therefore the same
order-40 Lucas contradiction and order-ten input contradiction apply
after the extended local comparison proof. This packet still uses
beta=2X^2+2403; no later odd-input or single-correction proposal is included.

For completeness, use the accepted 431 scalar preparation and its current
positive pole input first. The accepted comparison construction can choose
the same nonidentity U_i=[h*n_i]P and V_i=[(h-1)*n_i]P with h!=0,1. Their
reciprocal reparameterizations supply every new chart witness and preserve
all outside values. No identity point or additional prime-selection
theorem is needed to construct witnesses for an integer input.

## Conclusion and reproduction

The domain extension and current scalar/H representations compose on the
literal final objects. The guard-free V0 proof has been renewed against
this source rather than inferred from its former nonidentity assumptions.
The resulting rational input projection is the same intended integer
predicate, on the accepted inherited arithmetic inputs.

Run `python -B review_composition423_check.py` from this directory. The
standard-library-only checker writes `review-composition423-checks.json`
and passes the independent full delta, incidence, interface and polynomial
checks. No source, candidate, earlier review or published file was modified.
