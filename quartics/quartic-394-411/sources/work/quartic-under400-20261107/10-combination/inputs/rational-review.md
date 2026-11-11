# Independent review of the rational logarithm replacement

I accept the arithmetic replacement in `03-depth/REPORT.md` and its separate
implementation in `10-combination/rational490-ir.json`, under the published
arithmetic inputs. I did not author either proposal. The arithmetic step
changes the logarithm approximation and therefore the comparison values;
it is not an assertion that R equals G9 or that all old witness tuples are
retained. The implementation correctly sends the new value R to the actual
comparison consumers.

The reviewed arithmetic report has SHA-256
`3cb54387332135affff513e7c54c99813fede24a3b990d36af3367574c569961`.
The reviewed 490-variable implementation has SHA-256
`0130aff1b5d4e081f3ffc7f03b295da6cb76870a7d3eec76f270b22714d4d92d`.
Its polynomial has SHA-256
`1c4d49ec3cc4fb392308f66ea4248b7a7847b267c46e4c3a4d0d52a806cab498`.
The implementation starts from the published 498-variable source with
SHA-256 `7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a`.

## Rational identity and all denominator domains

With the manuscript recurrence for a_j, the displayed quadratic Q and
degree-eight N satisfy exactly

    Q(w)G9(w)-N(w)
      = (2970726/254443709)w^10
        -(41697666/6361092725)w^11.

The coefficient computation and all nine displayed Bernstein coefficients
were checked by exact rational arithmetic. In particular the coefficients
of w^7 and w^9 in QG9 vanish. This is the asserted numerator, not a truncated
polynomial chosen from numerical samples.

The actual alternate points belong to 2E(K), K=Q(sqrt(2)). Their nonzero
abscissas are squares in K, hence strictly positive in both real embeddings.
Their ordinates are nonzero. Since y^2=x(x^2-D), each embedding therefore
gives x^2>D and x>sqrt(D). Consequently w=D/x^2 lies strictly between zero
and one. This argument uses the actual doubled-point domain, not every
point of the elliptic curve.

On the larger closed interval [0,1], Q is decreasing because
Q'=(-1526+1026w)/1073<0. Thus Q>=60/1073>0. The Bernstein basis is nonnegative
and sums to one on this interval, and every coefficient of N is at least
83904/10113025>0. Therefore N and Q are nonzero under both embeddings at
every admitted K-point. R=N/Q is defined and nonzero, as is zR because the
point-domain lemma already gives z nonzero.

No nonvanishing on the whole complex elliptic curve is needed or claimed.
The field K has no complex places; its embeddings into C have real image.
Q may have zeros at other complex-curve points outside the used real
domain. This introduces no hidden quantified-domain restriction here.
As an algebraic rational function, the added denominator has a finite
zero set and is not identically zero, so the existing real-progression
argument for finite pole sets remains applicable as well.

At a consumed p-adic place over p>76176, all coefficients of Q,N,G9 and
the displayed error polynomial are integral. Their denominators have no
prime factor greater than 37. A formal point of depth r=v(z)>=1 has
v(f)=2r and v(w)=4r. Hence Q(w) and N(w) both lie in 1+pO and are units.
At other finite places they need not be units. They are nevertheless
nonzero because the evaluation lies in K and is globally nonzero. This
distinction is sufficient: the later completeness argument only requires
finite valuation bounds and continuity at its finitely many prepared
points at those other places.

## Precision and exact downstream ratios

The exact rational identity and the unit Q(w) give

    v(R(w)-G9(w)) >= 40r.

The unchanged full-tail estimate gives v(G(w)-G9(w))>=40r. Thus
v(log_E(V)-z(V)R(w))>=41r. The formal logarithm isometry gives
v(log_E(V))=v(z(V))=r, so zR/log_E(V) lies in 1+p^(40r)O. In particular
its relative error has order at least 40, and its valuation is r.
This uses neither residue degree one nor a split-prime-only identity.
It applies at split and inert unramified places with v(p)=1.

The four changed indices are exactly 0,2,3,4. For i=2,3,4, the numerator
and common denominator approximations both have relative error at least
40. Their ratio therefore approximates (u_i-n_i)/(h-1) to relative order
40 and has the same valuation. For i=1, the numerator stays zG2 with
precision 12 while the denominator has precision 40, giving precision
12 for that ratio. Rational coefficients commute with conjugation, so
the conjugated alternate ratios used by the tests are the intended ones.

As in the accepted mixed-depth proof, one must transfer integrality before
turning relative errors into absolute congruences. The full ratios are
u_i/h and (u_i-n_i)/(h-1), and at least one is integral. The positive-order
cross-test and equal valuations give integrality of both approximations.
Then the primary depth is at least twenty, its relative error is at least
80, and the alternate errors become absolute errors of order 12 or 40.
Multiplication by h and h-1 and subtraction gives the same label
congruences. Nothing in this step divides by a nonunit index.

The scalar estimates, the product-height input, and both final height
contradictions are therefore unchanged. The same argument also supports
the separately reviewed input orders 10 or 11: only the final input
cross-test precision is weakened, while G2 and the new denominator retain
precision 12 and 40. A rebuilt weight circuit is still required there.

## Completeness and projection scope

The new comparisons are rational functions of the same prepared points.
Their denominators are nonzero by the global argument above. Thus the
source may choose sufficiently small local neighborhoods and finite
valuation bounds for these functions before choosing the contact primes.
The separated-prime CRT still gives primary depth twenty and alternate
formal membership. The precision estimates just proved then give every
required test order.

No new real obstruction occurs. N/Q is continuous and bounded above and
away from zero on [0,1], so the old nonzero z-denominator and finite-pole
arguments still provide suitable real bounds. The pole construction has
the same fixed test orders, the same lambda^(-3) decay, and the same
small-prime preparation mechanism. It continues to provide positive
detector inputs. Coefficient denominator primes are below the already
used cutoff.

Consequently completeness reconstructs comparison and pole witnesses
using the new rational functions. It does not keep every old comparison
value unchanged. Soundness follows from their proven congruences and the
unchanged height consumers. Together these establish the same integer
input projection with no new arithmetic premise.

## Implementation review

I read the source modification in `03-depth/build_source.py`, its finishing
driver, and `verify_rational.py`. The e=40 branch evaluates the displayed N
using w,w^2,w^4 and assigns Q*R=N. Its normal and combined V0 output paths
then use R. The e=12 branch is untouched. I inspected the existing 511-source
replay record, but did not perform a new complete replay of that separately
compiled artifact. My complete finite implementation check is instead on
the independently supplied 490-variable presentation.

For that implementation, `review_rational_check.py` reruns the producer-free
full checker with its file write suppressed and adds checks of the physical
output consumers. The full checker independently derives N by convolution,
checks positivity and coefficient integrality, reconstructs all new rows,
checks every outside affine substitution, and compares the entire quartic.
The added checks establish w=D*f^2 from the actual retained square rows,
verify every Bernstein coefficient, and check that no reused old cube or
deleted middle coordinate remains in an unintended consumer.

The implementation retains the scaled old w^2 slots, changes the old cube
slots to literal w^4, removes the middle pair, and changes the old polynomial
pair to literal R. The fixed-coefficient inverse affine substitution for
each old polynomial slot is correct. Its surrounding lower-order terms
cancel in the actual consumers, so they receive R rather than an old scaled
coordinate or a mixture of G9 and R.

The exact checked output equations are

    y(V0)*ell0 + x(V0)*R0 = 0,
    ell0*LP_i - z(V_i)*R_i = 0, i=2,3,4.

The latter is material: the final compiler has eliminated the standalone
ell_i coordinates. The actual surviving consumer is the raw alternate
quotient LP_i, followed by the unchanged conjugation in the tests. Historical
semantic entries for the eliminated ell_i coordinates must not be treated
as active output variables. All eight physical component rows checked.
The G2 input numerator and its LP1 quotient remain intact.

The checked implementation has 490 total variables, 459 quadratic residuals,
and 24,182 quartic monomials. Its fixed parameter and coefficient maximum
remain C=3^(2^25) and 16*3^(2^26), and its content is one. Complete results
are in `review-rational-checks.json`.

This review accepts the arithmetic replacement and the frozen 490-variable
implementation described above. Integration with a different V0 chart,
new test orders, or other component rewrites still requires an exact check
of that composed artifact. The required mathematical interface is simply
the literal R output, its nonvanishing, and its order-40 relative accuracy.
No shared proposal file, published repository file, or acceptance register
was changed.
