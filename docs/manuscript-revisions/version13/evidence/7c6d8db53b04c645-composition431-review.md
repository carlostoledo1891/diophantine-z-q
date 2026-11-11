# Independent acceptance of the 431-variable composition

Reviewer: agent01. Decision: accepted for the frozen research composition.
This review combines the already accepted 433 source with the independently
reviewed scalar norm-root and depth-24 changes. I authored neither component.
The acceptance concerns integer projection through their reviewed soundness
and completeness arguments, not a bijection of old and new scalar witnesses.

The result has **431 total rational variables**, including the input, 430
witnesses, 408 quadratic residuals and 6,456 quartic monomials. Its content is
one and its largest coefficient is exactly `16*3^(2^26)`, with fixed
`C=3^(2^25)`. The publication threshold remains strictly below 400.

## Frozen sources and result

| Artifact | SHA-256 |
| --- | --- |
| Source `10-combination/combined433-ir.json` | `207218ebbcd15fa97f69580fce71629a50e34129549e80a9568dbed57ae28832` |
| Source acceptance `00-root/REVIEW433.md` | `1f67647179bc2ddb522af5b4f3454f2b7a476fd1115ba09946c3bc1689641ca1` |
| Norm-root component `root449/candidate449-ir.json` | `02ce0dcbeeba90a52bfba28c6968f09bcd3471c4b76847b57987f72cb6175549` |
| Norm-root review `05-anchor/review-scalar-root.md` | `ef0daf4038d42faafeb57ec8b735cb20b2a4df127d68dd978292eeb84e2eb5f9` |
| Depth component `depth24-448/candidate448-ir.json` | `e9d6622ef87381ed2f735e849aa537ac178ccc30ec1675f32cee0be38b435609` |
| Depth review `03-depth/review-scalar24.md` | `ac3142ee515d79b88ee85dc9951f4d495ee43ca2a6fc16473f2badc5637d8221` |
| Result `10-combination/combined431-ir.json` | `180968baa12a26f0171eeeb337df61b293a3a122786929e28b9fc94c55ba5573` |
| Polynomial `10-combination/combined431-polynomial.json` | `3f9ec023f0c850d0ef39b16f0832f49ce55dc4e5d009bcbd77fa69e1b72c5f50` |
| This review's `check.py` | `ac8558c7fa20f8a5c95fe35c528eefb9b7714de193ed9a04e2ba6f48911d09c5` |
| This review's `CHECKS431.json` | `4746e85b27f6673596fe02bf1f29a799f7158404d75695f74236c20248016ec3` |

Both component acceptances were present and read before this acceptance. The
component directories are under `06-product/scalar-redesign`. The receipt also
pins the earlier component source and all other files consumed by the checker.

## Finite reconstruction and actual meanings

My checker imports no producer, compiler or other checker. Starting from the
pinned 433 file, it derives each component delta directly from the component's
old and new IR files. It checks each changed preimage, coordinate meaning,
deleted or repurposed coordinate's complete incidence, and the entire final
coordinate and residual tables. It checks unique names and IDs, exact metadata,
input preservation, support and fixed-parameter preservation.

The first step removes coordinate 536 and its constant-node row and replaces
the root equation. The second removes coordinate 605 and its r^64 row, changes
the B denominator and root equations, and repurposes coordinate 541 from B² to
Q=q². No outside row reads the old meaning of either removed coordinate or Q.

The physical equations in the final file give

```text
beta = 2*X²+2403,
r = beta*(beta-1)*(beta-2401)*(32*beta+343)*(2*beta-1),
q = Norm(f(H)),
z0+z1*sqrt(2) = z(R)/z(H),
B = (z0²+r*z1²)/r^32,
Q = q²,
W = (B²+r*Q)/r^32.
```

The checker derives the contact polynomial by solving and expanding the
literal three contact intermediates. It verifies the unchanged input-square
equation and all five positive correction choices. It proves Q's normalization
from t=f0²+2f1² and u=f0*f1, since t²-8u²=(f0²-2f1²)². It checks the actual
inverse equations x(H)*f(H)=1, which prove that f(H), and therefore q, is nonzero.
It checks each of the five remaining power equations and all three new scalar
equations individually.

The scalar ratio slots 508/509 retain their meanings from accepted 433; none
of their equations changes. This matters because that source has already
replaced the old z(H) representation and eliminated H.j. The final composition
does not restore a stale ratio definition.

The only consumers of the new W slot are its root equation and W-square row.
The actual corrected-r, W-square and pole-product equations still compose to
b=c*r*W². The stored pole coordinate is negative-scaled, b=-K*v526 with K>0;
the checker verifies that `1+K*v526*v528=0` guards this same nonzero b. It also
verifies the literal anchor equation

```text
v55²+6*v56²-2*v57²-4*C*v57-3*v505²=0.
```

All beta-comparison, detector, point-domain, height and other anchor equations
are preserved by the complete table comparison, rather than selected by an
assumed list of unaffected names.

Finally I independently expand the primitive integer residual squares and
compare every polynomial coefficient. The isolated coefficient-one monomial
v1^4 proves content one. The sole C² coefficient is 16 at v57², with no
lower-C contribution there. Every other coefficient has fewer than 2048 bits
before multiplying by at most C. This proves the exact maximum without an
enormous decimal expansion. Formal terms and specialized monomials both number
6,456, and all 431 coordinates occur in the polynomial.

## Source-to-consumer mathematical audit

I read both full component arguments and both non-author reviews. I also read
the actual pole statement, scalar preparation and continuity argument,
two-branch scalar proof, height-transfer input and anchor consumers in the
released `manuscripts/quartic_v12.tex`, SHA-256
`5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`.
Relevant locators are 7720-7748, 10520-10560, 19229-19325, 19877-19900,
20201-20220, 20264-20361 and 20534-20635. The later accepted order-10 argument
supplies the changed input-comparison consumer; the released text itself still
uses its original order 12 and scalar depth 32.

The following obligations were checked on the final composition.

1. The carrier remains rational witnesses over K=Q(sqrt(2)). The input is
   unchanged. The shifted beta is the one used in the actual r and comparison
   equations. Every contact factor is positive for rational X.
2. The quantified prime set remains every consumed p>76176 in M5(beta). The
   correction is a unit there. Negative valuation of beta would make
   v_p(r)=10*v_p(X) even, so the required odd eta is positive.
3. The pole obstruction applies to the actual nonzero b=c*r*W². It gives
   eta+2*v_p(W)>0. No sign of a stored coordinate is substituted for this
   semantic nonzero input.
4. The two nested numerators have terms of opposite valuation parity. The
   final equations therefore give v_p(B)>63*eta/4, v_p(q)>61*eta/4,
   v_p(z0)>191*eta/8 and v_p(z1)>187*eta/8. Zero terms have infinite valuation.
   The coefficient depths are at least 24, not an unsupported claim of
   24*eta. The checker independently verifies these rational thresholds.
5. The positive norm valuation gives a place above p where f(H) has positive
   valuation, for both split and inert primes with the inherited normalization.
   The rational coefficient bounds imply depth 24 for the same ratio there.
6. Both possible branches of R are retained: near O or near (0,0). The
   duplication identity makes 2R formal and preserves the positive parameter
   valuation in either branch. The actual map consumed by the logarithm is
   [h](2R)=[2s]H. The unramified isometry hypotheses and p-unit factor 2 are
   unchanged. Thus M5(beta)^24 divides the same nonzero integer s.
7. The exponent-19 contact theorem consumes precisely that divisibility and
   gives h(beta)<=H*|s|^(19/24). The unchanged physical anchor has
   log2|s|>25165823.5 and H<2^2093966. The exact inequality
   (5/24)*25165823.5>2093966+7 gives h(beta)<|a|/40, including negative s.
   The independent logarithmic margin remains valid. Order 40 still forces
   the Lucas relation; order 10 then gives the same contradiction for
   n!=beta. Integrality of beta=2X²+2403 still forces X integral.
8. For completeness, choose the single simultaneous positive correction,
   then H sufficiently deep and R deeper, before choosing the continuity
   modulus and contact primes. At p|r the stated coefficient depths 8*eta
   for f(H) and 24*eta for the ratio make W integral. The same conclusion
   holds at correction primes not dividing r. The source explicitly permits
   arbitrary finite depth bounds, including at ramified and bad primes.
9. Since r>0 and q²>0, the new W is globally positive. Consequently b is
   positive, integral at the support of cr, has even valuations elsewhere,
   and retains the local squareclasses at 2,3,17. These are exactly the pole
   completeness hypotheses. The former unit-root assertion is not used.
   Continuity preserves the required finite bounds in the same order of
   global choices. Fresh pole witnesses are supplied for the new b.

These checks establish that the separately accepted arguments compose on the
literal final objects. They do not constitute a new audit of every inherited
global arithmetic theorem. Historical source inputs remain inherited; the
norm-root and depth-24 connecting arguments are the new reviewed applications.
No released manuscript claims to include these research changes.

## Reproduction and limit

Run `python -B check.py 431` here. It writes only this review's receipt and uses
one Python process. All shared inputs remain read-only. The exact frozen
composition is accepted; later reciprocal-chart or identity-domain changes
are outside this review and require their own composition check.
