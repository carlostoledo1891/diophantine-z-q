# Independent review of the scalar-root extension

Accepted for integration, relative to the inherited source arithmetic and the
separately reviewed positive-contact/correction change. I found no gap in the
replacement of the old scalar root by

    W = B^2 + q^2/r,
    q = Norm(f(H)),
    B = (z0^2+r*z1^2)/r^64,
    z0+z1*sqrt(2) = z(R)/z(H).

This is a non-author mathematical and implementation review of the frozen
450-to-449 extension. It is not a new independent audit of the source's global
arithmetic inputs, or of the preceding five-generator correction theorem.
The change has projection equivalence through soundness and a fresh
completeness construction. It is not a rational bijection between every old
and new witness tuple; the pole input changes.

## Frozen packet and reviewed sources

The reviewed files are under `06-product/scalar-redesign/root449`.

| File | SHA-256 |
|---|---|
| Parent `candidate450-ir.json` | `31d5e21d5101f31fd47352dea36dae7eb0faa5498a22cab26ebb62799d9be7e6` |
| `candidate449-ir.json` | `02ce0dcbeeba90a52bfba28c6968f09bcd3471c4b76847b57987f72cb6175549` |
| `polynomial449.json` | `70bea702b8e5ddef1690ab08ecb29ade8aac46339ee2aeb1c41059ee56bc2a36` |
| `REPORT.md` | `1bcd3140a837f2b7a17e28887f591fc1cbf2fe25df95bc1cb9314934265e2e9e` |

I read the report, producer, checker, actual residuals, the parent report and
consumer bindings, and the relevant source proofs. In the assembled
`manuscripts/quartic_v12.tex`, SHA-256
`5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`, these are:

* `hyp:o8-pole`, lines 7720–7748, including the exact seven-witness predicate
  and the permitted degenerate witnesses.
* `v5:scalar32-bridge`, lines 10429–10561, including arbitrary coefficient
  depth at every prime on the support of cr, and the subsequent continuity
  argument with the scalar point fixed.
* `subsec:v12-scalar` and `lem:v12-scalar-sound`, lines 20222–20362, including
  the one-place norm argument, both branches for R, and the actual logarithm
  identity.
* `subsec:v12-completeness`, lines 20594 onward, for the ordering of scalar
  preparation, root choices and subsequent congruences.

Historical disposition: the pole theorem, depth preparation and logarithm
transition are existing source inputs. The new norm-root bounds and the
replacement of the old unit assertion by integrality are new connecting
arguments, checked below. The published manuscript remains unchanged.

## Soundness and every odd-contact prime

The parent input is beta=2X^2+2403. For rational X all five factors of

    r=beta*(beta-1)*(beta-2401)*(32beta+343)*(2beta-1)

are strictly positive. Thus r is nonzero. At an odd prime, any negative
valuation of beta equals 2v_p(X), hence is even. At a consumed prime
p>76176, all displayed nonzero fixed coefficients are p-units. If beta had
negative valuation, all five contact factors would have that valuation,
and v_p(r)=5v_p(beta) would be even. If beta is integral, all factors are
integral. Consequently an odd value eta=v_p(r) at a consumed contact prime
is necessarily positive. Removing the constant-left leaf loses no step
needed to establish eta>0.

The parent correction c has support at primes at most 17. Hence it is a
p-unit here. The unchanged scalar pole predicate, applied to its retained
nonzero input b=crW^2, implies

    eta+2v_p(W)>0.

This inequality is strict because its left side is odd and the pole theorem
excludes negative odd valuations. In the new W, the valuations of B^2 and
q^2/r have opposite parity. The norm q is nonzero: f(H)=1/x(H) is a nonzero
element of K on the retained point domain, and a field norm of a nonzero
element is nonzero. Thus no cancellation can invalidate

    v_p(q)>eta/4>0,               v_p(B)>-eta/4.

Allowing a zero B does not affect this argument. In the defining numerator
of B the two summands again have opposite parity when both are nonzero.
The resulting bounds are

    v_p(z0)>(32-1/8)*eta,
    v_p(z1)>(32-5/8)*eta.

Because eta is a positive integer and the coefficient valuations are
integers, both valuations are at least 32. Zero coefficients have valuation
infinity and satisfy the conclusion.

At a split prime, v_p(q) is the sum of the valuations of f(H) at the two
places. At an inert prime it is twice the single valuation. Thus there is
at least one place where f(H) has positive valuation, making H formal at
that place. Since the extension is unramified and rho is integral there,
the two rational coefficient bounds imply

    v(z(R)) >= v(z(H))+32 > 0.

This does not assert that R is formal. The source's exact identity

    z(R)^2=x(R)/(x(R)^2-D)

allows either v(x(R))<0, near O, or v(x(R))>0, near (0,0). The case
v(x(R))=0 cannot give positive v(z(R)). With p odd and D a unit, the
duplication formula in the source gives in either permitted case

    v(x(2R))=-2v(z(R))<0,         v(z(2R))=v(z(R)).

All relevant numerators and denominators are nonzero by their unequal
term valuations and the retained nontorsion point domain. Both H and 2R
are therefore in the same positive-depth formal group. The exact identity

    [h](2R)=[2s]H

and the unchanged formal logarithm isometry yield

    v_p(s/h)=v(z(2R))-v(z(H))>=32.

The nonzero integer h has nonnegative p-valuation, so v_p(s)>=32. This
checks every prime in the same five-contact radical and proves the exact
consumer statement M5(beta)^32 divides s. The exponent-19 height theorem
then supplies the same h(beta)<=H*|s|^(19/32). No downstream anchor or
comparison estimate requires the stronger old lower bound for v_p(q).

## Global sign, completeness and the lost unit assertion

On every rational assignment satisfying the retained point domain,
r>0 and q^2>0. Therefore W=B^2+q^2/r>0. This gives global nonvanishing
without an appeal to a local unit calculation. The positive correction c
then makes the semantic pole input b=crW^2 strictly positive.

For an integer input, r and c are positive integers. Let S0 be the support
of cr, and use the original ordered depth construction. First choose H
sufficiently deep at all places above S0. Then choose the positive index s
of R sufficiently divisible, and large enough for the unchanged anchor.
The source explicitly permits arbitrary finite lower bounds on all the
relevant rational coefficient valuations, including at ramified and bad
primes. Thus the following requirements are legitimate simultaneously.

At p dividing r, write eta=v_p(r)>0. Require both coefficients of f(H) to
have valuation at least eta, and both ratio coefficients to have valuation
at least 32eta. Then

    v_p(q)>=2eta,
    v_p(q^2/r)>=3eta,
    v_p(B)>=0,
    v_p(W)>=0.

At p dividing c but not r, require the same coefficients to have positive
valuation. Since r is a p-unit, both summands of W are integral. The
coefficient 2 in the field norm does not spoil these lower bounds at p=2;
it can only increase the relevant valuation. Cancellation likewise can
only increase these lower bounds, so no unit claim has been used.

It follows that b has nonnegative valuation at every prime in S0. Outside
S0 its valuation is 2v_p(W), which is even. Therefore its reduced
denominator is a square. Multiplication by the nonzero rational square
W^2 preserves the squareclasses of cr in Q2, Q3 and Q17. Together with
b>0, these are exactly the completeness hypotheses of `hyp:o8-pole`.
That theorem does not demand that W be a unit. Fresh scalar pole witnesses
therefore exist.

With R fixed, the coefficient functions of H remain defined at the prepared
point, and their lower valuation bounds persist in sufficiently small
local neighborhoods. The source's finite-index congruence construction
thus yields the required modulus L. Positivity of W holds globally on the
point domain. No new real approximation, local squareclass, or simultaneous
realization premise is inserted. The subsequent root and detector choices
remain in their original order.

The existing transformations to the preparation conic and factored scalar
pole accept every such positive semantic b, including their permitted
zero-valued private witnesses. They do not need the old numeric value of b.
This is why completeness must choose fresh pole witnesses rather than copy
the old ones. Conversely every solution of the new equations reconstructs
the same exact pole predicate at the new nonzero b, so the soundness
application above has the required input.

## Physical equations and downstream transport

The new checker `review_scalar_root_check.py` is my own implementation and
imports no producer. It independently eliminates the three physical contact
intermediates and proves that the affine expression for r is precisely the
displayed five-factor polynomial at beta=2X^2+2403. In particular, the
negative coefficients of its stored affine form do not reverse its sign.

The shared slots satisfy

    v311=v140^2+2v141^2,          v312=v140*v141,
    v311^2-8v312^2=(v140^2-2v141^2)^2=q^2.

The checker verifies all six power-chain steps to r^64, the actual
z0=v508 and z1=v509 ratio slots, and

    r^64*v540 = v508^2+r*v539,    v539=v509^2,
    v541=v540^2,
    r*v542 = v311^2-8v312^2+r*v541.

Only coordinate 536 and its defining constant-node row disappear. The
new root row replaces the old root row. Every other row is unchanged up
to its harmless nonzero rational normalization. Coordinate 536 had no
hidden consumer. The root slot v542 has only its own row and the existing
W-square row as consumers.

Using the pinned depth519 semantic-value table, the checker also verifies
the actual corrected-r row, the W-square row and the b-product row. Their
semantic composite is exactly c*r*W^2. In particular the pole slot v526 is
negative-scaled: b=-K*v526, with positive K recorded exactly in
`review-scalar-root-checks.json`. The retained inverse row is
1+K*v526*v528=0, so it guards this same nonzero b. There is no confusion
between positivity of semantic b and the sign of its stored coordinate.

The primitive integer sum of squares was recomputed independently and
matched every polynomial coefficient. The frozen extension has 449 total
variables, 448 witnesses, 426 quadratic residuals and 6,582 quartic monomials.
It saves one coordinate and one row relative to its 450-variable parent.
The fixed coefficient parameter is unchanged. Combining this extension
with a separately changed scalar-ratio representation requires rechecking
that the new B slot still denotes the same rational coefficient norm.

## Verdict and reproduction

The extension is accepted at the hashes above. Its new arithmetic
obligations are satisfied: odd contact valuation is positive without the
constant leaf; the new parity estimates imply the same order-32 consumer;
and global positivity plus local integrality replace every needed use of
the former unit-root assertion.

Run `python -B review_scalar_root_check.py` from this directory to reproduce
the finite checks. They pass and write `review-scalar-root-checks.json`.
Those checks verify the finite encoding and source bindings; the
valuation and completeness proof is the argument above. No source,
candidate, earlier report, or published file was modified by this review.
