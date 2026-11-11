# Dual exponential and finite trace

Let K be a finite extension of Q_p, let L/K be finite, and let V be a finite-dimensional continuous de Rham representation of G_K. Use V restricted to G_L, not an unrelated representation. The application uses the original representation of the fixed elliptic newform. This is a rational finite-extension statement, not an integral lattice or infinite-tower comparison.

The published input is Kato, Astérisque 295 (2004), section9.2 and section9.3, printed p187 (the definition of the cyclotomic logarithm continues on p188). Section9.2 identifies D_dR(L,V) with L tensor_K D_dR(K,V). Section9.3 defines exp* by the natural coefficient map H1(K,V) -> H1(K,B_dR^+ tensor V), followed by the inverse of cup product with log(chi_cyclo) from H0(K,B_dR^+ tensor V). Its target is D_dR^0(K,V). We use exactly this normalization at both fields.

Put M=B_dR^+ tensor V and alpha=log(chi_cyclo). The class alpha on G_L is the restriction of the class on G_K. Finite-coset corestriction commutes with the coefficient map V -> M. It also satisfies cor(res(alpha) cup m)=alpha cup cor(m), for m in H0(L,M). This is the degree-one projection formula: expand corestriction as the finite sum over coset representatives; the cocycle identity for alpha separates the alpha(g) term, while the terms involving logarithms of the representatives are a coboundary. This argument applies to continuous cochains with this topological coefficient module because the sum is finite; it does not invoke a discrete-coefficient approximation to B_dR^+.

If z belongs to H1(L,V) and m=exp*_L(z), the image of z in H1(L,M) is res(alpha) cup m. Applying corestriction and the preceding formula shows that the image of cor(z) in H1(K,M) is alpha cup cor(m). Inverting Kato's same cup-product isomorphism gives exp*_K(cor(z))=cor(m).

On H0(L,M), corestriction is the sum of the conjugate embeddings. Under the section9.2 identification L tensor_K D_dR(K,V), this is Tr_(L/K) tensor1: the second factor is G_K-invariant and the first factor is acted on by the embeddings of L. Thus exp*_K(cor(z))=Tr_(L/K)(exp*_L(z)). The sum preserves filtration zero, so this statement has the stated target D_dR^0(K,V).

For a finite product of completions, apply this identity to each field factor and add. Localization of a global corestriction is the sum of these local corestrictions, with the usual finite-coset decomposition. Therefore the character-weighted finite corestriction in current main13591–13596 becomes the unnormalized sum of the conjugate dual exponentials. No factor equal to the field degree or character-group order is divided out.

The input supplies only finite-extension functoriality. The actual reciprocity value, retained smoothing, coefficient inverse limits, cyclotomic norm-compatible classes, and local periods remain separate inputs or calculations.
