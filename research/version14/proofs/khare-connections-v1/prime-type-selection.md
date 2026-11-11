# Auxiliary prime and tame-type selection for the actual callers

Author: /root. Author proposal awaiting independent review. This replaces
the arithmetic input to the selected two-family induction. It uses one
published prime-interval theorem and elementary integer arithmetic.
It does not certify Khare's unavailable final Duke version.

## 1. Published prime-interval input

Jitsuro Nagura, On The Interval Containing At Least One Prime Number,
Proceedings of the Japan Academy 28 (1952), 177-181, DOI
10.3792/pja/1195570997, unnumbered Theorem on printed p.180, gives a
prime strictly between x and 6x/5 for x>=25. The official J-STAGE
final PDF is pinned in SOURCES.json. Only this theorem is imported here;
Khare's separate Chebyshev/Ellison estimate and finite prime tables are
not premises of the new prime-selection proof.

## 2. A non-Fermat prime in the required interval

Let B>=31 be prime. Apply Nagura to x=B and choose a prime Q with
B<Q<6B/5. If Q-1 is not a power of two, set P=Q. Otherwise apply
Nagura again to x=Q and choose Q<R<6Q/5.

If 2^a+1 is prime then a is a power of two: if a=bc with b>1 odd,
the factorization of X^b+1 at X=2^c would make it composite. Therefore
two distinct such primes Q<R have exponents a<b with b>=2a, and
R>Q would force R>=(Q-1)^2+1. For Q>31 this is greater than 2Q,
contradicting R<6Q/5. Thus R-1 is not a power of two. Set P=R.

In either case we have an odd prime

    B < P < 36B/25,

and P-1 has an odd prime divisor ell. Fix any such divisor, let r be
its exact valuation in P-1, and put q=ell^r=2m+1 and t=(P-1)/q.
Then m>=1, t is even, t>=2, and gcd(t,ell)=1.

For B>=31,

    36B/25 < (3B-1)/2 <= ((2m+1)B-m)/(m+1).

The first difference is (3B-25)/50>0. The second inequality follows
from ((2m+1)B-m)/(m+1)=2B-1-(B-1)/(m+1), which increases with m>=1.
Consequently

    (m+1)P <= (2m+1)B-m,

and P<2B. This supplies both the stronger returned-weight bound and the
weaker bound used by residual normalization18. No numerical search over
unbounded primes or unproved statement about Fermat primes is used.

## 3. Choose the actual congruence class, not an arbitrary type

Let k be the original even Serre weight. There is a unique integer j
in the half-open interval

    mt < j <= (m+1)t

with j congruent to k-2 modulo t. Explicitly, with least nonnegative
remainder,

    j = mt+1 + ((k-2-mt-1) mod t).

Since t is even, j is even. Since m>=1 and t>=2, this also gives
2<=j<=P-3. In particular omega_P^j is a nontrivial even character.

Fix the same coefficient embedding at ell as in the two-family
construction. Reduction of roots of unity of order P-1 has kernel
exactly the ell-primary subgroup of order q; its prime-to-ell part
of order t reduces injectively. Therefore the congruence modulo t
is exactly what is needed for omega_P^j and omega_P^(k-2) to have
the same ell-adic reduction. Their quotient has order dividing q,
which is odd. Equivalently, the quotient by the Teichmuller lift of
the old residual character has ell-power order. The new whole character
need not have odd order; only that quotient does.

The original finite inertia character is the reduction of
omega_P^(k-2), by construction14 and the determinant/conductor check
in construction15. Thus this j supplies the actual old-character
compatibility required for the prescribed second family, rather than
merely a convenient exponent interval.

## 4. Both returned weights lie in the previous induction range

The independently supplied RETURN statement gives weights j+2 and
P+1-j, with the specified global twist in its second alternative.
Here both are even and at least 2. Using t=(P-1)/(2m+1),

    j+2 <= ((m+1)(P-1))/(2m+1)+2
         = ((m+1)P+3m+1)/(2m+1) <= B+1.

Similarly, since j>m(P-1)/(2m+1),

    P+1-j < ((m+1)P+3m+1)/(2m+1) <= B+1.

The last inequalities are exactly the bound proved in Section2.
This verifies the actual two alternatives with their endpoints; it does
not infer a weight bound merely from the determinant congruence.

Starting from B=31, repeat the construction with the new prime P as
the next B. The resulting strictly increasing sequence of integers is
unbounded. Thus the arithmetic steps themselves leave no gap in the
induction ranges. The modularity induction and its known initial weights
are separate mathematical inputs.

## 5. Small callers and one historical exponent correction

For the finite callers we retain the following valid choices. Here t is
the prime-to-ell part of P-1. Each row satisfies ell^r exactly dividing
P-1, even 2<=j<=P-3, j congruent to k-2 modulo t, and both returned
weights at most the stated previous bound B.

| Caller | P | ell | q | t | original k | j | returned weights | B |
|---|---:|---:|---:|---:|---|---:|---|---:|
| W8 | 7 | 3 | 3 | 2 | 8 | 2 | 4,6 | 6 |
| W10-W12 | 11 | 5 | 5 | 2 | 10,12 | 4 | 6,8 | 8 |
| W14-W20 | 19 | 3 | 9 | 2 | 14,16,18,20 | 8 | 10,12 | 12 |
| W22-W30a | 29 | 7 | 7 | 4 | 22,26,30 | 16 | 18,14 | 20 |
| W22-W30b | 29 | 7 | 7 | 4 | 24,28 | 14 | 16,16 | 20 |
| W32 | 31 | 5 | 5 | 6 | 32 | 18 | 20,14 | 30 |

The historical author text and inherited weight/prime table display j=16
in the W32 case. With P=31, ell=5 and k=32 that choice fails the needed
congruence: 16 is not congruent to 30 modulo 6. Its character has order
15, so its reduction modulo 5 still has order 3; the old finite character
has trivial reduction. It cannot supply the prescribed same-residual
type in this domain. The replacement j=18 has order 5 and reduces to
the old trivial character; both returned weights are already known.

This is a correction to the held author-version caller and our inherited
finite table. It is not a claim that the unavailable final Duke article
contains the same value. Old tables and reviews remain preserved. Any
new caller assembly must use this corrected row and review its exact
transport. The generic constructions and RETURN formulas already allow
j=18; their source statements need no strengthening.

## 6. Boundaries

This supplies auxiliary prime existence, the permitted tame character,
its parity and reduction, and the numerical decrease for the finite and
general callers. It retains Nagura's published theorem, the actual
first/second-family construction contracts, the RETURN theorem, known
lower-weight modularity, global twist compatibility and all separate
lifting/assembly steps. It is not an independent proof of those inputs,
a whole level-one theorem acceptance, TeX incorporation or release.
