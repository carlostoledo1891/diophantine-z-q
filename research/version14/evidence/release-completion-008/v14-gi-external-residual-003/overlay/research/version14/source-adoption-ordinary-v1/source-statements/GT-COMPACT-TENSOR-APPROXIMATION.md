# GT-COMPACT-TENSOR-APPROXIMATION

Project paraphrase, not a copy of the publication.

Source: Ben Green and Terence Tao, Linear equations in primes, Annals of Mathematics 171 (2010), 1753–1850. Final publisher PDF SHA256 ec126f9c9e189cc0308b83fb4f9f93c29a47d11ad875391aff4ce4c42aef1001. Proof of Proposition 11.2, compactness step p.1799 and Stone–Weierstrass tensor approximation p.1801.

**statement**: On the fixed compact cube-constraint space, a continuous composed test is uniformly approximable by a finite linear combination of products of bounded Lipschitz coordinate tests. Compactness of a fixed bounded Lipschitz class supplies a finite uniform net, so the number of terms and finite coefficient bounds can be fixed for that class.

**objects**: The compact set Sigma, its coordinate projections to a fixed compact nilmanifold, a continuous P and tests F composed with P.

**hypotheses**: The coordinate-test algebra contains constants, is closed under conjugation and separates points. The input test class has fixed norm and Lipschitz bounds on a compact metric space.

**quantifiers**: Every positive tolerance and every test in the specified bounded class.

**parameter_range**: Fixed compact spaces and a fixed finite number of coordinate factors.

**uniformity**: Finite approximation data can be chosen uniformly over the bounded test class; they do not bound varying nilmanifold geometries.

**constants**: Retain the finite sum of coefficient magnitudes and the factor bounds; rescaling factors transfers magnitude to coefficients.

**normalizations**: Uniform error on the entire compact constraint space, before evaluating any orbit or averaging.

**exceptional_cases**: Without point separation or bounded-class compactness the corresponding conclusion is not asserted.

**limit_order**: Choose the compact geometry and test bounds, a finite uniform net and approximants, then evaluate on arbitrary orbits.

Application boundary: Only the compact approximation argument is imported. The later published averaging-domain transition is not used. For two quotient factors the local proof separately verifies their joint injection and hence point separation. Local proofs explicitly retain coefficients even when using normalized factors.
