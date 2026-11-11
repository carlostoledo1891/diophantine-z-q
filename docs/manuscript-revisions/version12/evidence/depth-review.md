# Independent review of the mixed-order depth proposal

Reviewer: `astra_quartic_opt02_squares`, November 7, 2026.

Verdict: accepted for the mixed-order transformation, conditional on the inherited arithmetic inputs and the scalar/anchor bounds identified below. I found no gap requiring a change to the proposed mixed-order equations or proof. This is an independent internal model review of `03-depth`; I did not author that proposal. It is not independent acceptance of my own pole normalization, the other changes in `10-combination`, the complete 505-variable theorem, or the manuscript's inherited arithmetic theorems.

The mixed-order route is not incorporated in the pinned Version 11 manuscript. Its final asymmetric-depth section still uses five G9 alternate logarithms and order 40 for every cross-test and the beta test. The correct disposition is that the earlier local, height and completeness arguments are present in Version 11, and the new application is justified in the separate proposal. A later integration must change the source description and the local and completeness consumers together.

## Source pins and scope

All paths below are relative to `work/quartic-optimization-20261107`, except the manuscript and baseline builder, which are in `work/quartic-version6-release/repository`.

| Source | SHA-256 |
| --- | --- |
| `manuscripts/quartic_v11.tex` | `1210d2e6f409e502fc9c95afc248fac16a9df48c760a396143780c20ec80b662` |
| `03-depth/REPORT.md` | `16ef2188f7d7117b9d0c48894b954cb01edf69ee4ccb545fd48d9961b44bb0e9` |
| `03-depth/beta12/build_source.cjs` | `87f00acbfd7295f17148c04bd18a04598203c387cc4855f848ed1b352ce513ae` |
| `03-depth/beta12/final/candidate-ir.json` | `4466bd973383ba404b1cc50deaf2aa4f77361850c090dc8af80b7ba77249d57c` |
| `03-depth/beta12/final/polynomial/polynomial.json` | `d29a7cb7ba2f43ea4930b4e370be040fb25993854c875eaaebca3e524d22fe78` |
| `10-combination/candidate505-ir.json` | `bd9aca7a4a31476e426660d1a33de33552f2a5019bec06104b45938d59f4b966` |

`review-depth-sources.json` records all 14 inspected source pins, including the raw source, first compilation, elimination certificate, baseline builder and combination report. These pins bind this review. A changed application needs a fresh comparison.

I read the actual Version 11 arguments at these locations:

- Lines 9202-9265, `lem:quartic-reciprocal-log`: recurrence, formal identity, factorial tail bound and the range 10 through 64.
- Lines 9268 onward, `lem:quartic-reciprocal-nonzero`: global nonvanishing for every GJ with J at least 2.
- Lines 10772 onward, `lem:v5-point-domains`, and lines 10813 onward, `lem:v5-unramified-log`: domains, valuation normalization, mixed numerator/denominator precisions, and residue-degree independence of the proof.
- Lines 11031 onward, `lem:v5-one-place`: one common place for every field test, for arbitrary positive integer test orders.
- Lines 11215-11336 and their surrounding completeness proof: continuity, ordering of choices, selected primes, real bounds and small-prime pole estimates.
- Lines 19486-19519, `v9:cor:scales` and `v9:eq:height-transfer`: the three-radical implication with exponent 19/k.
- Lines 19600-19638, `subsec:v9-soundness`: the actual two height contradictions and their constants.
- Lines 19641-19657, `subsec:v9-completeness`: root preparation and continuity modulus.
- Lines 19659-19739, `v9:sec:depth`, `subsec:v9-local-depth`, `v9:lem:separation`, and `subsec:v9-deep-completeness`: integrality-first argument and the deeper-primary CRT construction.

These are source-level checks of the changed application. I have not independently re-proved the restricted converse, prime-pattern theorem, product-height theorem, scalar theorem, or anchor theorem.

## Required and constructed objects

At a consumed place above a rational prime p greater than 76176, the field is K=Q(sqrt(2)), the extension is unramified, v(p)=1, and D is a unit. The retained tests put H and the four Ui on the formal branch at the chosen place and put V0 and the four Vi on the formal branch at the conjugate place. At an inert prime this is the same place. Positive valuation of f=1/x gives formal membership on this good integral model. These are the actual points used by the generator, not substitute points.

The retained point charts and subtraction domains give finite nonidentity points with nonzero x and y. The integer labels are H=[h]P, Ui=[ui]P, Qi=[ni]P, V0=[h-1]P and Vi=[ui-ni]P. Thus h and h-1 are nonzero. No integer restriction is imposed on the existential coordinate variables; the integer labels come from the inherited description of 2E(K).

The proposal constructs

```
Li = z(Ui)/z(H),
L1' = conjugate(ell12(V1)/ell40(V0)),
Li' = conjugate(ell40(Vi)/ell40(V0)) for i=2,3,4.
```

It tests L1-L1' and L1-beta at order 12, retains the other three cross-tests and the Lucas test at order 40, and tests f(H) at order 40. The other nine reciprocal-coordinate tests remain order one. The same common place supplied by the one-place lemma satisfies all these orders. Its statement permits different positive integer orders, so regrouping the product by 1, 12 and 40 does not change the domain of that lemma.

## Truncation and normalization

The recurrence is exactly a0=1, a1=-2/5, aj=(4j-5)aj-1/(4j+1). In particular a2=-2/15, so the generated order-12 numerator uses exactly G2=1-(2/5)w-(2/15)w^2. It does not use G3 or omit the quadratic term. The four remaining alternate logarithms use G9. V0 remains the common G9 denominator.

For e=12 put m=3; for e=40 put m=10. The first omitted terms have indices 3 and 10. At formal depth r at least one, v(w)=4r. For 4j+1<p the coefficient is integral. For later j, the source bound gives

```
v(aj w^j) >= 4jr - (4j+1)/(p-1) >= 4jr-j >= 3jr.
```

Those later j are at least 19044, so this exceeds 4mr for both m=3 and m=10 and tends to infinity. Hence the full tails have valuation at least 12r and 40r before multiplication by z. The resulting relative errors are at least 12 and 40. The source lemma's statement for unramified places lists only 16,52,64, but its displayed proof applies with m=3,10 without an additional hypothesis. This is a proved extension of that statement's application range, not a silent invocation of a stronger statement. The split-prime lemma already states the entire required numerical range.

The same proof with the tail starting at j=1 yields log(Q)/z(Q) in 1+p^(4r)O. Neither the coefficient proof nor the normalized formal identity requires residue degree one. Conjugation exchanges the two places at a split prime and preserves the single valuation at an inert prime. The ratios ui/h and (ui-ni)/(h-1) are rational and are unchanged by conjugation.

## Integrality comes before depth twenty

Let ri=ui/h and ri'=(ui-ni)/(h-1). Multiplication identities for the formal logarithm give these exact ratios at the respective places. At least one is integral because the consecutive integers h and h-1 cannot both be divisible by p.

Before asserting any deeper Ui depth, the unit statements above show v(Li)=v(ri) and v(Li')=v(ri'). Each positive-order cross-test therefore transfers integrality from one approximate ratio to the other. It follows that both exact ratios are integral too. This step needs only a positive cross-test order, so 12 works as well as 40.

Now Li integral implies v(z(Ui)) at least v(z(H)). The f(H) test gives v(f(H)) at least 40; the formal identity v(f)=2v(z) therefore gives depth at least 20 for H and then every Ui. The primary approximation error is now relative order at least 80. The alternate ratio has relative order at least min(12,40)=12 for i=1 and 40 for i=2,3,4. Since the ratios have already been proved integral, those relative errors yield absolute congruences.

With k1=12 and k2=k3=k4=40, the cross-tests consequently give Li congruent to ri and ri' modulo p^ki. Multiplying by h and h-1 gives hLi congruent to ui and (h-1)Li congruent to ui-ni; subtracting gives Li congruent to ni modulo p^ki. There is no division by a possibly nonunit integer in this subtraction. I found no circular use of depth or integrality.

## Actual downstream height consumers

The direct Lucas polynomial depends only on L2,L3,L4, whose recovered label congruences remain order 40. Thus its integer value F is divisible to order 40 by every relevant radical. The beta comparison gives n-beta order 12. Since it also proves beta integral at the consumed primes, the denominator in the reduced fraction n-beta is a unit there, and its integer numerator N is divisible to order 12. This denominator check is implicit in the proposal and made explicit here.

These are precisely the orders consumed at Version 11 lines 19624 and 19630. The scalar/anchor inputs required there are unchanged as abstract bounds:

```
H >= 1, H < 2^2093966,
c=|a-1|, log2(c)>25165823.5,
h(beta)<=H*c^(19/32).
```

They imply c>(80H)^10, |a|>(40H)^10, h(beta)<|a|/40 and log(40H)<|a|/40. Indeed 10(7+2093966)<25165823.5 and 80<2^7; the stronger exponent margin also gives c^(13/32)>80H.

For nonzero F, B^2-6<7H|F|^(19/40) and |F|<5B^4 give B^(1/10)<7H*5^(19/40)+6<24H, contradicting B>=|a|>(40H)^10. Once F=0, the retained nonidentity Z gives b nonzero, as required by the inherited Lucas lemma, and hence log(B)>|a|-3.

For nonzero N, |N|<=2 exp(h(beta))B and the order-12 height estimate give B^(5/12)<40H exp((19/12)h(beta)). Thus log(B)<(12/5)log(40H)+(19/5)h(beta)<31|a|/200<|a|-3. This contradiction gives n=beta; integrality of 2X^2+3 forces integral X. Nothing here needs order 40 for L1.

In candidate505, other proposals supply the scalar and anchor bounds. Their validity is outside this review. The mixed-order proof only consumes the displayed bounds, so it combines with those proposals if their separate reviews establish them for the actual scalar point R=S-P.

## Denominators and completeness

The only alternate logarithm used as a divisor is still ell40(V0). Its z factor is nonzero by the retained point domain, and G9 is globally nonzero by the dyadic lemma. G2 also satisfies that lemma, although its occurrence as a numerator does not require nonvanishing to define the mixed quotient. The primary divisor z(H) and all reciprocal x/y domains are unchanged. G2 introduces no new coefficient-denominator primes relative to G9.

For integer input, prepare the odd labels, scalar point and anchor first, then fix the scales. The rational functions with the new G2 numerator are defined at the prepared shared point and have the same type of finite pole loci. Choose the continuity neighborhoods and modulus L for these actual functions before selecting contact primes. This is enough to apply the existing real-progression argument and obtain fixed small-prime lower bounds; it does not require their numerical constants to remain identical to the old functions.

The same separated-prime construction then gives

```
gcd(M-,M+)=1, gcd(M-,L)=16, gcd(M+,L)=1,
gcd(Pi,M+)=1, gcd(Pi,L)=1.
```

Thus h=0 modulo Pi^19 M-, h=1 modulo M+, and h=h0 modulo L are compatible because 64 divides h0. Shared factors between Pi and M- cause no obstruction. The groups used are the doubling images of cardinality d+/4 and d-/4, not full groups inadvertently divided a second time. P is a double, so primary annihilation followed by multiplication by p^19 gives depth at least 20, using the normalized unramified logarithm. Multiplication by the integral label ni cannot decrease that depth.

The opposite points have depth at least one. Their mixed G2/G9 ratio equals n1 to order 12, and their other ratios equal ni to order 40. Primary ratios have order at least 80. Since n1=beta and the Lucas relation holds exactly for the chosen integer labels, all sixteen modified tests have their specified orders.

The pole-completeness calculation at lines 11322-11336 is stated in terms of each positive order mj. Its large-real decay remains lambda^-3, and the small-prime estimate is 3nu+(10mj-8)eta-2c. Substituting mj=12 preserves the conclusion as nu grows. This is the same arbitrary-positive-order product consumed by the one-place soundness lemma. No incompatible choices of L or h are introduced.

## Executable source correspondence

I independently compared the entire generated builder against the pinned baseline builder. There are exactly seven declared text replacements: fixed-S metadata, the V1 logarithm precision, two test-order changes, the added order-12 coefficient group, the changed evaluator degree splits, and multiplication of the extra degree-two factor group. No point-domain or scalar/anchor change is hidden in that builder comparison.

I ran the builder in `02-squares/review-depth-replay`, with its pinned source file. The newly generated raw IR, translated raw IR and census match the proposal's artifacts exactly as JSON values. I then freshly ran the existing independent raw-gate/first-compiler checker, replayed the final constant-pivot and shear certificates, and compared the full final sum of squares. This confirmed 519 coordinates, 488 residuals, degree four and 24,986 monomials for the isolated depth proposal. The exact final polynomial hash is pinned above.

The existing verification driver was copied with only output destinations redirected into this review directory. This is a fresh execution of independent existing engines, not a claim that I authored another independent arithmetic proof checker. `review-depth-driver.py`, `review-depth-checker.json` and `review-depth-verification.json` retain the executable evidence.

Finally, `check_depth_review.py` compared the depth-related equations in the isolated proposal with candidate505. All 254 checked equations are identical, covering parameters/logarithms, tests/shared symmetric coefficients, the three detector polynomial evaluations, W-product assembly, and the q12/q40 output equations. This proves that the reviewed depth changes are the ones consumed in the combined system. It does not assess the correctness of the other combined transformations.

## Disposition

The new mixed-order application is mathematically justified within the stated inherited inputs, and its source implementation and transport into the pinned candidate505 match the proof. No correction to that proposal was needed. The only clarifications added by this review are the reduced-denominator argument for N, explicit extension of the unramified lemma to m=3 and m=10, and the fact that the new continuity modulus must be chosen for the changed functions.

This review does not close a manuscript-integration item. Version 11 remains the all-order-40 source description at the pinned hash. A later manuscript edit must incorporate the mixed definitions, the order table, the e=12 unramified argument and the corresponding local/completeness consumers, then receive a binding review of that edit.
