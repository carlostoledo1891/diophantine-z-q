# Independent review of input-comparison orders 10 and 11

I accept the arithmetic claim in `03-depth/lower-precision/ARITHMETIC.md`,
SHA-256 `aa9ae90056186ad76c97099ba388b80238c2ba2a19beb501155d69473ef45185`.
Both input-comparison orders 10 and 11 suffice with the unchanged G2/G9
alternate logarithm ratio and unchanged order-40 Lucas tests. This is an
independent review of the arithmetic modification, conditional on the
accepted mixed-depth argument and the manuscript's inherited inputs.
It is not a review of a new weight circuit or a claim of a variable saving.

## Local statements and numerator divisibility

The affected tests are exactly L1-L1' and L1-beta. The denominator of L1'
remains ell40(V0), and its numerator remains ell12(V1). No claim that the
shorter logarithm has order 10 or 11 is required: it already has error of
order at least 12 at the alternate formal point.

At every consumed unramified place, the retained order-one tests imply
formal membership and the order-40 f(H) test implies depth at least twenty
for H. The full logarithm ratios remain u1/h and (u1-n)/(h-1). At least one
is integral because at least one of h,h-1 is a unit. Before any new depth
deduction, the approximate ratios have the same valuations as their full
ratios. A cross-test of either positive order transfers integrality to both.

Only then does L1 integral imply depth at least twenty for U1. The primary
relative error has order at least 80, and the G2/G9 alternate relative error
has order at least 12. Integrality converts these to absolute errors.
For k=10 or 11, the cross-test therefore gives L1=n modulo p^k by the same
multiplication by h and h-1 and subtraction used in the source. The beta
test gives beta integral and n-beta in p^k at that place. As both labels
are rational, its reduced numerator is divisible by p^k. This is exactly
the input required for each of the three contact radicals.

This argument covers split and inert unramified places with the unchanged
valuation normalization v(p)=1. It does not infer depth before proving
integrality, change a quotient domain, or divide by a nonunit integer index.

## Height calculation

I checked the actual `v9:eq:height-transfer` statement in Version 11. For
any nonzero integer N divisible by the k-th powers of the three contact
radicals it gives

    B^2-6 < 7H |N|^(19/k).

Its exponent k is not restricted to a multiple of four. In this application
N is the reduced numerator of n-beta. With B>4,

    |N| <= 2 exp(h(beta)) B,
    B^2-6 > (5/8) B^2.

For k=10 or 11, 19/k<2. Hence

    B^(2-19/k)
      < (56/5) 2^(19/k) H exp((19/k)h(beta))
      < 48H exp((19/k)h(beta)).

The numerical slack is valid: (56/5)*4=224/5<48. Since 2k-19>0, taking
natural logarithms and dividing preserves the inequality direction:

    log B < k/(2k-19) log(48H) + 19/(2k-19) h(beta).

The unchanged anchor gives c=|a-1|>(80H)^10 and |a|>=c/2, with H>=1.
It already yields h(beta)<|a|/40. To check the other margin without confusing
natural and binary logarithms, put y=80H>=80. Then

    log(48H) < y < y^10/80 < c/80 <= |a|/40.

Consequently the last upper bound for log B is less than

    ((k+19)/(40(2k-19))) |a|.

For k=10 this is (29/40)|a|; for k=11 it is |a|/4. The first is less than
|a|-3 as soon as |a|>120/11, and the second as soon as |a|>4. The retained
anchor gives much more than |a|>11. Both contradict the unchanged Lucas
bound log B>|a|-3. Thus n=beta, and the existing beta=2X^2+3 argument forces
X integral. The order-40 argument proving the Lucas equation is untouched.

## Completeness and implementation boundary

The old mixed-depth completeness construction produces both affected
congruences to order 12, so it also produces them to order 10 or 11.
The changes in detector normalization do alter their rational functions;
one must fill the poles for the new test orders, rather than claim that
every old pole witness remains a solution. The inherited pole construction
already handles fixed positive orders. Its real decay remains lambda^-3,
and its small-prime estimate becomes 3nu+(10k-8)eta-2c, which still increases
without bound in the freely chosen nu. Thus no additional prime or real
condition is introduced, and positive detector inputs remain available.

The new q_k values must be q1*e^(2k-2), with exponents 18 and 20. The existing
q12 circuit has exponent 22 and cannot simply be renamed. The note states
this boundary correctly. This review does not approve the separate source
replay or any proposed replacement Laurent chain, which need their own
exact residual and consumer checks.

The relevant manuscript inputs are the same as for mixed depth:
`subsec:v9-local-depth`, `v9:eq:height-transfer`, `subsec:v9-soundness`, and
`subsec:v9-deep-completeness`, in the Version 11 file with SHA-256
`1210d2e6f409e502fc9c95afc248fac16a9df48c760a396143780c20ec80b662`.
No manuscript, source artifact, or acceptance register was changed.
