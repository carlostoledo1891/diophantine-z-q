# Compatible classical CM points at the actual conductors

Author: /root/v14_arithmetic_author. Bounded source application; no generic supersingular or integral-model conclusion is supplied.

## Published input

Cai, Chen and Liu, Heegner points on modular curves, Transactions AMS370(2018),3721–3743, published offprint SHA256 fd19f0588bf3cee285f731812ae058dc3f8527d30d26eac7c2b6a21bfa847522, p3721 states the classical X0(N) construction: for the order O_c and an invertible level ideal N with O_c/N isomorphic to Z/NZ, the ideal-class points represented by (C/a,aN^-1/a) are defined over H_c and depend only on the proper ideal class.

The source Heegner condition is (c,N)=1 and the stated split-or-ramified condition on primes dividing N. We use only the all-split case. Its p3727 Example2.1 constructs the admissible normalized embedding and explicitly invokes Shimura reciprocity for the Galois action. Lemma2.1 and Definition2.2 on p3725 identify the ideal construction with the level curve. The prior CM reciprocity theorem remains an imported source theorem, not newly proved here.

Section2.3 on p3730 chooses compatible conductor-raising points by intersecting the level and lattice ideals with the raised order, for a new prime outside6cND_K and the preceding conductor. This is the point system used by its separate Theorem2.15 norm relation.

## Actual specialization

Fix the same imaginary quadratic K and split prime-power orientations at every prime dividing N as in main3720–3740. For each actual old conductor d prime to2ND_K, take c=d and m=1 in the source. All level primes split, so N1=1, N0=N and X_K(N)=X0(N). The source condition on ramified or inert level primes is vacuous; no squarefree or inert-product condition is imposed on d.

Choose at each split level prime the same one of the two prime ideals and contract the resulting level ideal to O_d. Since d is prime to N, its localizations at level primes equal those of O_K, so the quotient is cyclic of order N and the ideal is invertible. Away from N it is a unit ideal. Thus the level ideal has exactly the fixed orientations and satisfies the source hypothesis. Proper invertible lattice ideals give the actual CM point, whose conductor is d and whose field of definition is H_d.

For a permitted new prime ell outside6dND_K, the source intersection construction supplies the compatible point at dell. It preserves the local level ideals because ell does not divide N. Repeated intersections agree when the new primes are taken in either order, so the finite simultaneous families use compatible points rather than independent choices at each conductor. Artin labels are those of the normalized source reciprocity map, with the already separately bound arithmetic-Artin conventions; no new Atkin–Lehner or root-number identity is inferred.

These are the compatible points and orientations required by the current norm application, main3798–3820 and heegner-descent-current/SOURCE-CONNECTIONS.md13–15. Passing through the fixed based elliptic quotient is a separate accepted input. The actual unaveraged norm relation remains the separate CCL theorem application; this construction does not prove that relation from field degrees.

## Boundaries

The inert supersingular reduction statement at arbitrary conductor, extension of the fixed modular parametrization to a good integral model, Atkin–Lehner eigenvalue/intertwining, and Neron-component/local-cohomology inputs are not conclusions of this source application. No quaternionic conductor-one result is substituted for these classical X0(N) points.
