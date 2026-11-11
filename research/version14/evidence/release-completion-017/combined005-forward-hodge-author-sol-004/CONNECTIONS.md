# Forward rank and Hodge comparison connections

## Kummer corank

Fix the actual elliptic curve A over Q. The selected finite Kummer sequences use the localization map at all places. Taking their filtered direct limit at powers of 2 gives the exact sequence
A(Q) tensor Q2/Z2 -> Sel(2-infinity,A/Q) -> Sha(A/Q)[2-infinity],
with the first arrow injective. Kolyvagin supplies both the finite Sha and the equality rank A(Q)=r for r=0 or 1. The finite group on the right has Z2-corank zero. The torsion subgroup of the finitely generated A(Q) tensors to zero, and its free rank-r subgroup tensors to (Q2/Z2)^r. Thus the middle group has corank r. This uses the rank equality as well as finiteness of Sha.

## Torsion and descent

The surface A is defined over Qbar. Let u be an integral complex endomorphism of its complex base change. Every torsion point is algebraic over Qbar, and its image under u is again torsion. Hence for every automorphism sigma of C over Qbar, u and its conjugate sigma(u) agree on all torsion points. On the complex torus, the points represented by rational multiples of lattice vectors are dense. They therefore form a Zariski-dense subset of A. Two morphisms into the separated A that agree on this subset are equal.

The invariant graph consequently descends to Qbar. One explicit formulation uses the ideal of the graph in affine charts chosen over Qbar. Fix a monomial order. The reduced Groebner basis of the ideal over C is unique and is preserved by all automorphisms of C over Qbar. Its finitely many coefficients are fixed and lie in Qbar. The invariant chart ideals glue, giving the descended graph and the same morphism over Qbar. Here the fixed-field assertion follows by extending isomorphisms of transcendence bases in an algebraic closure over the algebraically closed subfield Qbar. Multiplying a rational endomorphism by a positive integer reduces to the integral case. No assertion that a polarization must be preserved is used.

## Quaternionic Hodge centralizer

Write B for the actual rational quaternion division algebra and identify the rational homology of the surface with its rank-one left B-module. The complex structure acts by right multiplication by a real element J satisfying J squared equal to minus one. Under the standard central-simple identity
B tensor B-opposite = End_Q(B),
write a rational endomorphism using a Q-basis in the left B-factor. Commutation with right multiplication by J is equivalent, coefficient by coefficient after real extension, to commutation of each right coefficient with J. The centralizer of J in M2(R) is R[J]. Thus the rational Hodge endomorphism algebra is B tensor the opposite of K, where K=B intersect R[J].

If K has no noncentral element, K=Q and this algebra is B. Otherwise choose a noncentral b in K. Inside R[J], b has a nonzero J-coefficient, so its quadratic minimal polynomial has negative discriminant. It generates an imaginary quadratic field k. The centralizer of b in B has dimension two and equals k. Since K is commutative and contains b, K=k. A maximal quadratic subfield splits B, so B tensor k is M2(k). The opposite on this commutative factor makes no difference. The published Hodge equivalence and the separately established Qbar descent identify this Hodge algebra with the full geometric rational endomorphism algebra.

The central-simple tensor identity, its double-centralizer dimension formula and the splitting by a maximal subfield are retained standard algebra inputs of this local calculation, as explicitly recorded by the bounded source review. This projection does not create a recursive source review for them.

## Picard quotient boundary

The actual finite map X1(N) -> X0(N) -> A supplies a norm on line bundles and hence a Q-homomorphism J1(N) -> Pic0(A). The identity on A identifies Pic0(A) with A. Surjectivity is checked after geometric base change using a geometric P0 and the image of divisor classes [P]-[P0]. A rational preimage or rational cusp is not required. The finite forgetful map, Picard representability and compatible norm are named inputs. This paragraph describes the exact pending application. The separate root review is not independent acceptance.

## Optional Kato branch

Only when the analytic rank is zero does the selected Kato corollary supply an alternative. Its actual quotient J1(N) -> A must first be supplied. The extension is Q over Q and the character is trivial. The nonzero central value is the rank-zero hypothesis. The source uses the full Selmer convention at all rational primes, including 2. It supplies no rank-one result and no converse from Selmer corank to analytic rank.

