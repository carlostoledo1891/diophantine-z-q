# Input comparison orders 10 and 11 are sufficient

The accepted mixed-depth construction may replace both order-12 tests by order k, for either k=10 or k=11. The two tests are L1-L1' and L1-beta. Keep every logarithm unchanged: the V1 numerator is ell12=zG2, its common V0 denominator is ell40=zG9, and every primary logarithm is the uncorrected parameter z. All order-one and order-forty tests remain unchanged. This is an arithmetic source modification, not an assertion that the old and new witness spaces coincide.

## Local implications and completeness

The accepted local argument transfers integrality using the cross-test before deducing depth of U1. Any positive k permits that transfer. H still has primary depth at least twenty, so both primary parameters have relative error at least eighty. The alternate G2/G9 quotient has relative error at least twelve. Consequently the cross-test of order k gives L1=n modulo p^k for k<=12. The beta test gives the same order k for the reduced numerator of n-beta. Nothing changes for the three Lucas labels, which still have order forty.

For completeness, use exactly the same prepared points, primes and CRT as before. Their G2/G9 quotient gives order twelve, which implies either weaker order k. The pole-realization argument applies to these fixed positive orders; its small-prime estimate becomes 3nu+(10k-8)eta-2c and still tends to infinity. No new prime selection, point domain, real condition or quantified-domain restriction is needed.

## New explicit height inequality

Use the same constants H<2^2093966, c=|a-1|, log2(c)>25165823.5 and c>(80H)^10. In particular,

    h(beta)<|a|/40,
    log(48H)<|a|/40.

For the latter inequality, put y=80H>=80. Then log(48H)<y, whereas c/80>y^10/80>y and c/80<=|a|/40. This uses exactly the existing anchor. The proof of h(beta)<|a|/40 is unchanged.

The order-forty Lucas contradiction is unchanged, so F=0 and log B>|a|-3. Suppose n-beta is nonzero with reduced numerator N. Then |N|<=2 exp(h(beta)) B and the same product-height inequality gives

    B^2-6 < 7H |N|^(19/k).

For B>4, B^2-6>(5/8)B^2. Also 19/k<2 for k=10,11, so 2^(19/k)<4. Therefore

    B^(2-19/k) < (56/5) 2^(19/k) H exp((19/k)h(beta))
                < 48H exp((19/k)h(beta)).

Since 2k-19 is positive, this yields

    log B < k/(2k-19) log(48H) + 19/(2k-19) h(beta)
          < (k+19)/(40(2k-19)) |a|.

For k=10 this coefficient is 29/40. For k=11 it is 1/4. Both are less than 1, and the existing enormous anchor gives, in particular, |a|>11. Thus either upper bound is smaller than |a|-3, contradicting the Lucas lower bound. Hence n=beta and X is an integer exactly as in the accepted construction.

This proves soundness and completeness for both k=10 and k=11 under the same inherited arithmetic inputs. The logarithm degree remains two for V1. The only prospective implementation savings are in the weights q_k=q_1*e^(2k-2), namely exponents 18 and 20 instead of 22. This note claims no coordinate saving without a separately verified weight circuit.

## Scope and compatibility

The proof reads the same local ratios, scalar bound, anchor subgroup, product-height estimate and Lucas lower bound as the accepted 519-variable mixed-depth argument. The subsequent pole, guard, anchor and scalar improvements do not alter those conclusions when used under their accepted interfaces. In particular the 501-variable combination can use this change if its toric circuit is rebuilt for the new exponent. Simply relabelling q12 without rebuilding its equations would be incorrect.

This note is authored by the mixed-depth proposer and awaits independent review. The old 519-variable artifacts and prior reviews are unchanged.
