# Right-coset periodicity, independent scoped review

Reviewer: `/root`, a model-based Codex agent. The proof author is `/root/astra_v14_baseline_compiler`; `/root/sol_protocol_final_review` identified the orientation problem and suggested using the right difference. I did not author that repair. I derived the denominator argument from the actual source formulas and read its exact implementation in DF002, rather than accepting Sol's verdict as a proof.

Accepted within the scope below. Target manifest `final-source-gtz/local-proof-df-compiler-002/MANIFEST.json`, SHA256 `ae285f6bda9bd47ac2303b44a4df94086060861cfec0786b33e146296771491b`. Target proof SHA256 `0d59971c920c4bd9c81bb36679cc8af13f1ad5f08a26ffa14bc174bb1c44cfa6`, lines 240–259, read with its object declarations and the surrounding closure lemma and consumer.

## Source comparison

I read Green–Tao's final *The quantitative behaviour of polynomial orbits on nilmanifolds*, PDF SHA256 `8c7ea5eced84dc5da97508f4eda39fa84c958d3e659a797ab402645c1c207c8f`, Lemma 6.7 and its proof at pp. 501–502, coordinate definitions and Lemmas A.2–A.3 at pp. 526–528, and Lemmas A.11–A.12 at pp. 534–535. I also inspected the rendered final p. 535 to check the quotient order, since text extraction alone can obscure it.

Lemma A.12's displayed proof controls the coordinates of gamma(n+r) gamma(n)^{-1}. Integrality of that left difference alone does not imply equality of the right cosets gamma(n+r) Gamma and gamma(n) Gamma for a nonnormal lattice. The theorem's existence-of-period conclusion is not disproved by this observation. The DF002 argument derives the period in the needed orientation directly and does not use the invalid implication.

The published coordinate formulas are sufficient. Lemma 6.7 supplies fixed finite polynomial coordinate degree for a sequence in the fixed filtered group. Lemmas A.2–A.3 give rational polynomial coordinate changes, multiplication and inversion. Their degree and coefficient denominators depend on the fixed rational group data. The repair needs bounded denominators, not bounded coordinate numerators.

## Reconstructed derivation

Let B be a standard positive common denominator for the Mal'cev coordinates of the standard discrete overgroup Lambda constructed immediately before the reviewed paragraph. Let D_0 be the fixed coordinate degree of gamma. Each value psi(gamma(j)), for 0 <= j <= D_0, belongs to B^{-1} *Z^m. The inverse of the fixed Vandermonde matrix at these integer nodes has rational entries with a standard common denominator. Thus the monomial coefficients of every coordinate of gamma lie in B_1^{-1} *Z for a standard B_1. The coefficients can have arbitrarily large internal integer numerators; that causes no problem.

Compose these coordinate polynomials with n+r and with the fixed rational polynomial inversion and multiplication laws. This gives R(n,r)=psi(gamma(n)^{-1} gamma(n+r)), whose finitely many coefficients have a positive standard common denominator A. All substitutions and products have fixed finite degree, so neither the number of factors nor their denominator powers depends on the hyperinteger n or on N.

The group identity at r=0 gives R(n,0)=0 as a polynomial identity. Equivalently, the coefficients with r-degree zero vanish. Every remaining term is a coefficient in A^{-1} *Z multiplied by n^i r^j with j >= 1. Setting r=A therefore makes every term integral for every internal integer n, positive or negative. Hence R(n,A) belongs to *Z^m. The adapted Mal'cev lattice convention gives gamma(n)^{-1} gamma(n+A) in *Gamma. Multiplication on the left by gamma(n) yields exactly gamma(n+A) Gamma = gamma(n) Gamma.

This is the same derivation as the actual new proof. There is no extra limit, passage from pointwise to uniform denominators, assumption of normality, or requirement that gamma itself lie in Gamma. The common denominator for Lambda is supplied by the explicit preceding rational-coordinate construction; it is not inferred from mere pointwise rationality. Constant sequences and the zero-dimensional group give R=0 and may take A=1.

## Adverse example and consumers

In the Heisenberg group with multiplication (x,y,z)(u,v,w)=(x+u,y+v,z+w+xv) and integer lattice, take gamma(n)=(1/2,n,0). Its left difference at r=1 is (0,1,0), in the lattice, while its right difference is (0,1,-1/2), outside it. At r=2 the right difference is (0,2,-1), in the lattice. Thus the orientation distinction is substantive, and the corrected conclusion still holds. This example tests the disputed implication, not the general theorem.

The exact consumer is the periodicity clause of DF-D4, propagated through the closure lemma and minimal-subgroup descent and then consumed by the one-variable D6 factorization argument. The result is a standard positive period valid for all internal integers. This local review accepts that clause under the proof's fixed-group, fixed-degree and common-coordinate-denominator premises. It does not independently reaccept every construction of the overgroup, the rest of DF-D4, DF-F1, the Gaussian Sections 9–11 argument, or any multivariable equidistribution theorem.

The final GT2014 erratum is a separate source in the packet. No correction to A.12 was found in the bounded textual search for that lemma. The acceptance here rests on the direct proof above, not on an assertion that the source has no other errors.

## Record obligations and limits

The supplying and needed statements now use the same right cosets. The domain is all internal integers and the lattice is the one defined by integral adapted coordinates. Rational coefficient conventions and uniform denominators have been checked explicitly. There are no additional local or ramification conditions in this finite coordinate argument. Degenerate constant and trivial-group cases are covered. The proof gives the standard-period strength the consumer requests; it makes no new explicit numerical bound. Historical DF001 and its orientation objection remain preserved. This is scoped mathematical acceptance, not complete inventory coverage, whole-GI acceptance, or release approval.
