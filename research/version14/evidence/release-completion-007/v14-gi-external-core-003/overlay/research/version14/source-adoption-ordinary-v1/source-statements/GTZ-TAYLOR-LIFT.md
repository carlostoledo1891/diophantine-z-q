# GTZ-TAYLOR-LIFT — bounded source statement

This is a project paraphrase, not the publication.

Source: Ben Green, Terence Tao and Tamar Ziegler, An inverse theorem for the Gowers U^{s+1}[N]-norm, Annals of Mathematics 176 (2012), 1231–1372. Final publisher PDF SHA256 cd320f5c1217df9bb41395e847ae2a924e70521021ca1b01c7abc20550123be1. Locator: Lemma B.9 and Corollary B.10, pp.1337–1338.

**statement**: For a finite downset J in N^d and an adapted polynomial map from Z^d, there is a unique ordered product of binomial monomials with coefficient g_j in G_j. A filtered homomorphism surjective on every layer permits lifting such a polynomial map by lifting its Taylor coefficients.

**objects**: The multidegree filtration on Z^d, a finite-downset target G, an order extending the partial order on J, and a layerwise-surjective filtered map phi:Gprime to G.

**hypotheses**: The actual target and lift filtrations satisfy the Appendix B hypotheses. The coefficient-lifting application checks surjectivity in every required layer.

**quantifiers**: Every adapted polynomial map; every integer input, including negative coordinates; each fixed compatible Taylor order.

**parameter range**: Finite standard dimension and downset; coefficients need not be bounded.

**uniformity**: One finite coefficient list fixed by J. No coefficient-size bound is claimed.

**constants**: Exact algebraic equality, without approximation.

**normalizations**: Ordered product g(n)=product_j g_j^{binom(n,j)}. The lift identity is phi composed with gprime equals g.

**exceptional cases**: A constant coefficient is retained unless g(0)=1. The local uses check the central maximal-layer condition in their taut or shifted target; no unrestricted non-taut extension is inferred.

**limit order**: Check filtration and layer surjectivity, lift coefficients, then form the ordered product.

**Application boundary**: B.10 prints the composition in the wrong order; the coefficient proof gives phi(gprime(n))=g(n). Binomial-to-monomial conversion, cube specialization, diagonal degree bounds, and the finite-dimensional Lie-polynomial model are proved locally, not asserted as the literal published theorem.
