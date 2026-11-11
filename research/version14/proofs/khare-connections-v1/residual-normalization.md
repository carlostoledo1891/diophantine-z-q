# Residual ordinary normalization for the actual level-one callers

Author: /root. Draft author proposal, not an independent acceptance.
This replaces the particular KC-NORMALIZE inference using the weight
definitions in the final published Serre paper. It does not treat Khare's
author Lemma 5.2 as stating an endpoint case that it excludes.

## Statement and incoming assumptions

Let P be an odd prime. Let r be a continuous two-dimensional representation
of G_Q over a finite field of characteristic P, odd and absolutely
irreducible, unramified outside P. Write omega for the mod-P cyclotomic
character. Suppose the actual Serre weight k of r is even, with
8 <= k <= P+1. Coefficients may be enlarged finitely for the local analysis.

Then either the original local representation r|G_QP is ordinary with
an unramified quotient and inertia diagonal (omega^(k-1),1), or
8 <= k <= P-1 and r tensor omega^(P+1-k) has actual Serre weight
P+3-k. At k=P+1 the first alternative necessarily holds. More precisely,
at that endpoint the representation has the very ramified extension
shape with diagonal (omega*eta,eta) for the same unramified character eta.

Here ordinary means existence of a G_QP-stable line with the specified
unramified quotient. It does not mean that the local extension splits.
This statement produces no characteristic-zero lift. If a twist lies
in an already proved lower-weight modularity range, the existing global
twist compatibility of modularity disposes of that branch; otherwise the
original ordinary representation is the input to construction14.

## 1. Read the final weight formulas, with the order of the characters

The source is Serre, Duke Mathematical Journal 54 (1987), printed
pp.183-187, Sections 2.2-2.5. We use the actual integer weight, not just
its congruence class modulo P-1. In the tame niveau-two case the digits
are 0 <= a < b <= P-1 and the weight is 1+Pa+b. In the tame niveau-one
case the digits are 0 <= a <= b <= P-2, with the same formula except that
(a,b)=(0,0) has weight P.

For nontrivial wild inertia there is a unique wild-invariant line D,
stable under the decomposition group. The quotient character is
omega^alpha*eta_1 and the line character omega^beta*eta_2, with
0 <= alpha <= P-2 and 1 <= beta <= P-1. Put
a=min(alpha,beta), b=max(alpha,beta). The ordinary formula is 1+Pa+b.
In the exceptional beta=alpha+1, very ramified case it is
(alpha+1)(P+1). The same case requires eta_1=eta_2, as stated in
Section 2.4, Remark (1), printed p.186.

These ordered conventions matter: the quotient exponent is alpha.
Exchanging the line and quotient in a nonsplit extension is not allowed.

## 2. The tame cases

In niveau two, k<=P+1 forces a=0, because a>=1 and b>a give
1+Pa+b>=P+3. Thus b=k-1 and k<=P. Since k is even and P is odd,
k<=P-1. Let psi be a fundamental character of niveau two. The two
inertial characters are psi^b and psi^(Pb), and omega=psi^(P+1).
Twisting globally by omega^(P-b) gives exponents

    b+(P+1)(P-b) = P(P+1-b),
    Pb+(P+1)(P-b) = (P^2-1)+(P+1-b).

Hence the new inertial pair, modulo P^2-1 and up to interchanging its
two entries, is psi^(P+1-b), psi^(P(P+1-b)). Its digits are
(0,P+1-b). Since k>=8, k even, and this branch has k<=P-1,
the new digit satisfies 3<=P+1-b<=P-6<=P-1. The new weight
is 1+(P+1-b)=P+3-k. The exponent P-b is P+1-k, as claimed for these
callers.

In tame niveau one, a>=1 would give weight at least P+2. The scalar
unramified exception has odd weight P. Thus in our even range a=0,
b=k-1 with 1<=b<=P-2. Frobenius preserves each of the two distinct
niveau-one inertia characters, so their eigenspaces are stable under
G_QP. Choosing the omega^b eigenspace as the line gives an unramified
quotient. The original representation is ordinary. No residual twist
or lower-weight comparison is required in this branch.

## 3. Wild inertia and the endpoint

In a wild case governed by 1+Pa+b, the bound k<=P+1 again forces a=0.
Since beta>=1, alpha=0. The quotient is therefore unramified, and the
line has inertia omega^(k-1). This is the required ordinary ordering.

In the very ramified case, k=(alpha+1)(P+1)<=P+1 forces alpha=0.
Consequently beta=1, k=P+1, and the two unramified factors are equal.
Conversely, no tame case or other wild formula above has even weight
P+1. Thus the endpoint has exactly the asserted ordinary, very ramified
shape. This is a direct application of final Serre Section 2.4, not an
application of Khare Lemma 5.2 beyond its printed range k<P.

## 4. Global and coefficient compatibility

The local analysis is over an algebraic closure of the finite coefficient
field; the finitely many matrix entries and eigenspaces involved are
defined over a finite extension. The global cyclotomic twist is defined
over the original prime field and preserves ramification outside P and
absolute irreducibility. It preserves oddness because its value on
complex conjugation has square one. It preserves the projective image,
so a nonsolvable image remains nonsolvable.

Modularity of a cyclotomic twist implies modularity of the original
representation by the existing global twisting interface for residual
modular forms. That published interface is an incoming assumption here,
not a conclusion derived from the local weight definitions.

## 5. The six actual caller ranges

All actual callers have k>=8, so the unused k=2 edge is excluded.
The lower-weight branch in the tame niveau-two case is as follows.

| Caller | P | Actual input weights | Possible nonordinary weights | Twisted weights | Previously established upper weight |
|---|---:|---|---|---|---:|
| W8 | 7 | 8 | none | none | 6 |
| W10-W12 | 11 | 10,12 | 10 | 4 | 8 |
| W14-W20 | 19 | 14,16,18,20 | 14,16,18 | 8,6,4 | 12 |
| W22-W30 | 29 | 22,24,26,28,30 | 22,24,26,28 | 10,8,6,4 | 20 |
| W32 | 31 | 32 | none | none | 30 |

For the general caller put B=p_n>=31. Assume P>B is an odd prime,
P<2B, and B+2<=k<=P+1 with k even. At the endpoint the original
representation is ordinary. Otherwise any nonordinary branch has
twisted weight P+3-k. Since B is odd, k>=B+3. Therefore

    P+3-k <= P-B < B <= B+1.

It is at least 4, since the nonordinary case has k<=P-1. Thus it is an
even weight in the previous induction range. The stronger arithmetic
inequality used by the general prime-selection step implies P<2B, but
existence of that prime and the returned-type choice remain separate.

## 6. Scope

This provides the exact either-lower-weight-or-original-ordinary
connection needed before the initial weight-two construction. It does
not assume that local reducibility alone proves global modularity, does
not require an unramified twist to be globally available, and does not
claim the unavailable final Khare text has been checked. The historical
author Lemma 5.2 is used only to identify the inference being replaced.

The existing lower-weight modularity cases, global modular-form twisting,
prime selection, the actual characteristic-zero constructions, ordinary
lifting theorems and the full Serre theorem are distinct inputs or later
steps. This proposal needs source and independent review before adoption.
