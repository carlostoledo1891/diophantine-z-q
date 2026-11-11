# Independent review of scalar preparation zero

Accepted for the frozen 442-to-439 research change below. The new real-small
and locally deep construction uses one pair of rational points and one final
shared index satisfying the full CRT. The source's stronger G0 open-set
statement supplies the needed approximation. It is not an inference from
independent real and local solutions. The numerical specialization also
matches the actual scalar pole input.

This accepts the new application and finite encoding on the inherited
arithmetic inputs. It does not re-audit every external theorem in the source.
Every new solution lifts to the old system; completeness constructs fresh
witnesses and does not specialize every arbitrary old preparation witness.

## Frozen files and source statements

All component files are under `06-product/scalar-redesign`.

| Object | SHA-256 |
|---|---|
| Source `deterministic442/candidate442-ir.json` | `e163f864feb6b235f5bd3b80c6ef77abeb636ca27a88308a7ca400575ba26f86` |
| `preparation-zero439/REPORT.md` | `918d33e53edbd7d481ad5fe97a7d369eb6f1e3cec01c36a4dca0a043bb83363a` |
| `preparation-zero439/candidate439-ir.json` | `135c10f2b3d4c38cde375435055e626a3f49f364370aa9e29fc9237ad225b3d3` |
| `preparation-zero439/polynomial439.json` | `0347a66d00cc80282c2cca559bbeba190550c676dfdb9c3f00002ff9a53adcb1` |

I read the component report, producer, checker and actual rows; the source
deterministic-correction report; and the actual statements and proofs in
`manuscripts/quartic_v11.tex`, SHA-256
`1210d2e6f409e502fc9c95afc248fac16a9df48c760a396143780c20ec80b662`:

* `v5:scalar32-bridge`, especially lines 10514–10553, supplies simultaneous
  arbitrarily deep finite-place preparation by integer divisibility and
  the subsequent continuity modulus.
* `v5:preparation-zero-bridge`, lines 10556–10629, requires b>0, square
  reduced denominator, local squareness at 2,3,17, b<17, and valuations
  at least 3,1,2 at those respective primes. It concludes the exact pole
  specialization with original preparation U=b and permits zero private
  witnesses.
* `v5:real-progression-bridge`, lines 10631–10700, includes the G0 open-set
  conclusion, not just a uniform boundedness conclusion.
* `v9:lem:separation` and `subsec:v9-deep-completeness`, lines 19700–19742,
  give the exact primary/opposite CRT after all fixed data, including L,
  have been chosen. The earlier Gaussian congruences explain the claimed
  coprimality with every fixed odd prime factor of L.

The same normalized curve, point P and its two real embeddings are used
throughout. No distinct point or independently chosen local model is
substituted in the real step.

Historical disposition: these approximation and pole inputs already exist
in the source. Making the scalar pole input real-small and preserving that
condition through the final shared-point choice is a new connecting
argument. It is proved and reviewed here. No published file was modified.

## Actual scalar function and global nonzero domain

For the frozen source, the input is

    beta=51(2X+1)^2+2504,
    r=beta*(beta-1)*(beta-2401)*(32beta+343)*(2beta-1),
    c=r+4896.

For every rational X, beta>=2504, so r>0 and c>0. The retained point domain
gives f(H)!=0; hence q(H)=Norm(f(H))!=0. The actual scalar equations are

    z(R)/z(H)=z0+z1*rho,
    B=(z0^2+r*z1^2)/r^32,
    W=(B^2+r*q(H)^2)/r^32,
    b=c*r*W^2.

Thus W>0 and b>0 on every rational solution, independently of the deleted
preparation inverse. This fact is essential for the new-to-old lift.
The independent checker derives the raw contact polynomial from the
literal intermediate definitions and matches the actual W and b equations.

For an integer input, c and r are fixed positive integers before any point
choice. The source calculation gives v2(cr)=4, v3(cr)=2, and r and c are
units at 17. The independent finite checks exhaust all required residue
classes: r=4 modulo 32 for every odd 2X+1, r is 3 or 6 modulo 9, and r=15
modulo 17. Since 4896 is divisible by 32,9,17, these are also the needed
unit comparisons for c. They prove the stated valuations and that cr is
square in Q2,Q3,Q17. These checks are over complete residue sets, not a
finite sample of integer inputs.

## One simultaneous initial preparation

Let G be the closure of the paired real integer orbit of P, let G0 be its
identity component, and let m=|G/G0|. This finite m is fixed by P, not by
later contact primes. Work at

    S*=supp(cr) union {2,3,17}.

Including 17 explicitly is necessary: here it does not divide cr.

First choose a positive integer M divisible by 64 and m, and by the indices
of sufficiently deep formal subgroups at every finite place over S*.
Every nonzero multiple [Mk]P then satisfies the chosen coefficient bounds
for f(H). This is the integer-divisibility construction in the source,
and remains valid at ramified or bad primes. Apply the actual G0 clause
to the progression 0 modulo M. Its positive tail is dense in G0.

The functions f and z extend continuously to O with value zero. Hence
q(H)=f(H)f(H)^sigma tends to zero as the paired point tends to (O,O).
A neighborhood of (O,O) in G0 is nonempty. Choose h0>0 in the progression
with H0=[h0]P in such a neighborhood, making q(H0) as small as needed.
This H0 already has all finite-place bounds. It is not O in either real
embedding, because P has infinite order and h0!=0. Its two z denominators
are nonzero on the retained point domain.

With H0 fixed, choose a positive integer N divisible by 6 and m and by
sufficiently large finite-place subgroup indices to prepare R=[s]P relative
to that same H0. This imposes the ratio coefficient bounds, the scalar
anchor and any required further divisibility. These are all fixed before
choosing s. The progression 0 modulo N again has dense positive tail in
G0, with arbitrarily large positive indices. Choose s there so that R is
sufficiently close to (O,O) and satisfies the anchor size requirement.

This makes z(R)/z(H0) small at both real embeddings. The coefficient maps

    z0=(ratio_plus+ratio_minus)/2,
    z1=(ratio_plus-ratio_minus)/(2sqrt(2))

are continuous linear maps, so both rational coefficients are small.
Consequently B^2/r^32 can be made arbitrarily small after H0 has already
made q(H0)^2/r^31 small. Explicitly choose their sum less than
sqrt(17/(4cr)). Then b(H0,R)<17/4. The fact that W has no constant summand
is what makes this possible.

The same integers h0 and s satisfy the real requirements, finite-place
requirements, anchor and sign conditions. There is no appeal to weak
approximation on E, nor an assumption that independently chosen local
points have a global realization. The dense integer progressions are the
global realizations.

## All finite hypotheses of the specialized pole theorem

At p|r, write eta=v_p(r)>0. The permitted bounds are at least 8eta on both
coefficients of f(H0), and at least 24eta on both coefficients of the ratio.
They imply

    v_p(q)>=16eta,
    v_p(B)>=16eta,
    v_p(W)>=0.

At p|c with p not dividing r, positive coefficient depths also make W
integral. Thus b has nonnegative valuations throughout supp(cr), while
outside that support its valuation is even. Its reduced denominator is
a square. Multiplication by the nonzero square W^2 preserves the local
squareclasses of cr.

In particular v2(b)>=4 and v3(b)>=2, exceeding the specialized theorem's
requirements. At 17, r and c are units and the separately imposed positive
coefficient depths give v17(q)>=2 and v17(B)>=2. Therefore v17(W)>=4 and
v17(b)>=8. No unit-root assertion is used. The coefficient 2 in the field
norm can only improve these lower bounds at 2.

These statements concern the actual semantic b, which is positive although
its stored coordinate has a negative scale. Together with b<17 they supply
every hypothesis of `v5:preparation-zero-bridge`.

## The final shared point preserves both real and finite conditions

Fix R. Continuity supplies a nonempty open neighborhood U of H0 in G0
where all scalar functions are defined and 0<b(H,R)<17. Their finite
coefficient bounds persist on h congruent to h0 modulo a sufficiently
divisible L. Require 64|L and m|L. Since m|h0, this congruence fixes the
identity component of the paired real orbit.

Now fix the remaining Lucas labels, the four roots and their height
scales, as in the source. Increase L to cover the fixed local continuity
requirements. Every such increase preserves the previous conditions and
m|L. The comparison functions are now a fixed finite family. Their poles
are contained in the source's finite unions of inverse images of finite
sets under nonzero multiplication and translation maps on the real
factors. The source proves that these sets have Haar measure zero in G0.
They cannot cover the nonempty open U. Choose U' with nonempty interior
and compact closure inside U away from the poles. All comparison functions
are uniformly bounded on that compact closure. This bound is fixed before
the contact-prime and lambda choices.

Only now choose contact primes, using the unchanged prime theorem and
separation argument. The source's Gaussian congruences exclude every odd
prime factor of L from both reduced orders; the prime 7 has its explicit
separate calculation. The 2-adic parts give

    gcd(Mminus,L)=16,             gcd(Mplus,L)=1,
    gcd(Mminus,Mplus)=1,
    gcd(Pi,L)=gcd(Pi,Mplus)=1.

Thus adding the fixed factors m and the additional 17-depth to L does
not invalidate the asserted CRT. The congruences

    h=0 mod Pi^19*Mminus,
    h=1 mod Mplus,
    h=h0 mod L

are compatible because 64|h0. Let their solution progression be h1 modulo T.
Since L|T and h1=h0 modulo L, both h1 and T are divisible by m. The G0
clause therefore applies to this final progression too. Its positive tail
meets U' infinitely often. Choose one sufficiently large h there.

This single H=[h]P has the scalar finite bounds by its L congruence, the
strict real bound by membership in U', all comparison domains and uniform
real bounds by the same membership, and the required primary/opposite
depths by the other CRT congruences. The large-lambda detector estimates
still use the uniform bounds fixed before the primes. The scalar bound
is independent of lambda and so is unaffected by that choice.

Apply the preparation-zero theorem to this final b. Its conclusion gives
fresh remaining pole witnesses with original U=b. The existing factored
second-conic conversion applies because this same b is positive; its
allowed zero branches are unchanged. All the field points used in the
polynomial are the globally chosen H,R and their specified multiples.

## Exact numerical specialization and reverse lift

The independent checker reads K from the old literal inverse row. With
the same positive K, the three old rows are exactly

    U^2=K^2*v531,
    1+K*v526*J=0,
    K*v526+K^2*J*v531+V^2=0.

The semantic values are b=-K*v526 and preparation square K^2*v531.
The new equation v531=v526^2 therefore sets the preparation square to
b^2. It deletes U,J,V, coordinates 50,528,529. No other row changes.

For any new rational solution, b>0 was proved above from the unchanged
point and scalar equations, without the deleted inverse. Define

    U=b,                         J=1/b, V=0.

All three old rows hold. For an exact polynomial check, after substituting
U=-K*v526, v531=v526^2 and V=0, the first old row vanishes and the third
equals K*v526 times the second. Choosing J=1/b makes the latter zero.
All outside coordinates, including the factored pole witnesses, are
preserved. This proves soundness by lifting to the source for every
rational new solution. Completeness is the fresh simultaneous construction
above, not a claim about specializing arbitrary old private witnesses.

The full incidence check confirms that the three deleted coordinates have
no other consumers. Every retained coordinate record and outside residual
is preserved. The checker also verifies the actual positive-input identity
b=crW^2 from the current deterministic correction and W-square normalizations,
and independently expands every primitive residual square.

The frozen result has 439 total variables, 438 witnesses, 417 quadratic
residuals and 6,658 quartic monomials. The coefficient tower is kept symbolic;
degree four, content one and maximum coefficient 16*3^(2^26) are unchanged.

## Reproduction and boundary of acceptance

Run `python -B review_preparation_zero_check.py` in this directory. It writes
`review-preparation-zero-checks.json`. The finite checks pass and bind the
source manuscript, source candidate, report and result. They check the
algebra, normalization, complete residue sets, incidence and polynomial;
the simultaneous real/finite-place application is justified by the proof
above. The accepted result is this exact packet, with its current scalar
function and deterministic correction. A later composition must preserve
or recheck these inputs and the real/CRT choice order.

No source, candidate, earlier review or published file was edited by this
review.
