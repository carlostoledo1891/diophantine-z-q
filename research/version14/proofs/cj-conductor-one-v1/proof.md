# A direct conductor-one reduction argument

This is an authored, conditional replacement for the exact A028 reduction interface. It is not an independent acceptance, a proof of the general Cornut–Jetchev theorem, or a qualification of its unavailable final edition. The separate geometric description of supersingular pairs currently assigned to A052 remains an explicit input with an open final-source qualification.

## Statement and retained inputs

Let F be an imaginary quadratic field with maximal order O, with O^times={+1,-1}. Let q be an odd inert prime, unramified in F. Let N be positive, coprime to q*disc(F), and assume every prime of N splits in F. No squarefreeness of N is assumed. Fix embeddings into C and an algebraic closure of Q_q, including a reduction place. Fix the CM type on O and one of the two O-stable cyclic p^e subgroups for each p^e exactly dividing N.

The source X is the set of isomorphism classes of CM triples (A,C,iota), with End(A)=iota(O), the fixed CM type, and the chosen level orientations. Isomorphisms preserve the labelled O-action. The target is the set of supersingular triples (Abar,Cbar,j), with Cbar cyclic of order N and j:O -> End(Abar,Cbar), up to isomorphism preserving j. Fix the orientation at q induced by the chosen reduction of the CM type, and the specified orientations at all p dividing N.

The claim is that geometric reduction gives an equivariant bijection between these two sets for the ideal-class action of Pic(O). Restriction to the fiber of any fixed underlying supersingular pair gives a bijection onto the corresponding conjugacy classes of embeddings with that orientation. The multiplicity is one.

The retained inputs are explicit:

1. Complex uniformization of CM elliptic curves, the CM ideal-class action, and its identification with the class-field action used to define x_D^[a] in (O.1). This is the existing CM reciprocity convention; it is not deduced from reduction.
2. CM elliptic curves have potentially good reduction and, at a prime inert in the CM field, their geometric reduction is supersingular. The needed forward inert-prime assertion is stated in the final Gross–Zagier *On singular moduli*, printed p.199, first paragraph. Its setting is the CM elliptic curve of the preceding p.198. A finite extension for a good model and an algebraically closed residue field suffice here. No uniqueness of a CM lift is used.
3. For good elliptic curves over a strictly henselian discrete valuation ring of residue characteristic q, prime-to-q torsion is finite etale. Specialization identifies its geometric generic and special fibers. Endomorphisms and isogenies of good elliptic curves extend, and a prime-to-q subgroup quotient commutes with specialization. These are the usual good-reduction functor properties already needed for the modular correspondences in A052. They are not a CM lifting/surjectivity theorem.
4. The geometric realization of supersingular enhanced elliptic curves by the Eichler class set B^times\Bhat^times/Rhat^times, including End(Abar,Cbar)=R_z and the compatible prime-to-q Tate lattice description. This is A052, at current lines 14128–14138, currently citing Jetchev–Kane. Its open final-source qualification is retained. A028 is not being used to justify this input.
5. Rational Skolem–Noether for maximal quadratic embeddings in B, the centralizer equal to F, and elementary local lattice classification. The manuscript already uses the rational embedding/local calculation before its first A028 invocation. We repeat the required local calculation below rather than assume a global reduction bijection.

Only after these inputs does the direct argument below apply. It supplies the reduction/orientation connection missing from a bare appeal to the word “torsor”.

## 1. The source torsor, independently of reduction

By complex uniformization an O-linear CM elliptic curve of the fixed type is C/Lambda for a fractional O-ideal Lambda. Two are O-linearly isomorphic exactly when their lattices differ by an element of F^times. Thus the ideal classes act freely and transitively. Choosing a level orientation at each p^e||N specifies C uniquely: O tensor Z_p is Z_p x Z_p, and the cyclic O-stable subgroup of order p^e is in one of the two eigensummands. The choice does not identify two ideal classes. Thus X is a Pic(O)-torsor before considering any reduction.

Every ideal class has an integral representative a prime to Nq. For completeness, choose a fractional ideal I in the inverse class. By the Chinese remainder theorem choose x in I with v_P(x)=v_P(I) at every prime P over Nq. Then a=(x)I^(-1) is integral and has valuation zero at each such P. This choice is only a representative; it does not constrain the ideal class.

For this representative the ideal action can be realized by the isogeny A -> A/A[a]. With the usual lattice convention its target lattice is a^(-1)Lambda. Using the inverse convention everywhere changes the action by [a] -> [a]^(-1), which will be tracked explicitly in the finite sum.

## 2. The target torsor, without reduction surjectivity

Work with embedded pairs, not pairs of conjugate embeddings. Choose a rational embedding i:F -> B and a finite adelic z_0 realizing one fixed tuple of integral local embeddings. At the reference tuple one may take i from the actual reduced reference CM curve. At other tuples the local calculation gives z_0; the geometric existence of its underlying pair is input 4.

Away from Nq a maximal-order O_p-stable lattice is a rank-one torsion-free module over the maximal quadratic order O_p. In the field case this is a fractional ideal of a discrete valuation ring; in the split case it is a pair of rank-one lattices. It is principal in either local algebra. There is one orbit under F_p^times. This includes ramified primes dividing disc(F).

At p^e||N, both lattices in an O_p-stable Eichler pair split under the integral idempotents of Z_p x Z_p. If their quotient is cyclic of order p^e, its two elementary exponents are (e,0) or (0,e). The exponent is not divided between two nonzero summands, because such a quotient would not be cyclic. Each choice is one F_p^times orbit. This argument works for all e>=1 and for p=2; it uses integral idempotents, not division by 2 in a chosen matrix formula.

At q, F_q/Q_q is unramified quadratic and B_q is division. A local cyclic presentation has B_q=F_q+F_q*Pi, with Pi*a=bar(a)*Pi and Pi^2 a central uniformizer times a unit. The maximal order has residue field F_(q^2). Conjugation by its units fixes that residue field, while Pi induces its nontrivial automorphism. The two O_q embeddings are consequently the two local unit-conjugacy classes. They are distinguished by their residue embeddings, or equivalently by the parity of reduced-norm valuation of a conjugating element. There is no identification of these classes.

Rational Skolem–Noether allows the field embedding of any target pair to be conjugated to i. Its remaining rational stabilizer is the pointwise centralizer F^times, not the full normalizer. The local calculations show that the adelic representatives of one tuple are exactly Fhat^times*z_0*Rhat^times. Their quotient is

    F^times \ Fhat^times / (Fhat^times intersect z_0 Rhat^times z_0^(-1))
       = F^times \ Fhat^times / Ohat^times = Pic(O).

The intersection is Ohat^times because the embedded order is maximal at every prime. This proves the target component is a free transitive Pic(O)-set. It does not use a map from CM points, a count of their reductions, or the desired surjectivity. The geometric interpretation uses input 4, which remains separate.

## 3. Geometric reduction and the same ideal action

Start with the actual reference CM triple x_0=(A,C,iota), not an arbitrary class in an adelic quotient. Choose a good model after a finite extension at the fixed q-adic place. Its reduction is supersingular by input 2. The labelled action of O and the prime-to-q cyclic subgroup C specialize. The resulting map j:O -> End(Abar,Cbar) is injective: a nonzero O endomorphism is an isogeny, its composition with its dual is multiplication by its positive degree, and that multiplication remains nonzero on the special elliptic curve. It therefore cannot specialize to the zero homomorphism. Since O is maximal, its image is optimal. The q-orientation is the reduction of the fixed CM type on the one-dimensional tangent space. Denote this actual target triple by y_0.

For a prime-to-Nq ideal representative a, the kernel A[a] is a prime-to-q finite etale subgroup in the good model. One can describe it by the simultaneous kernels of finitely many generators of a inside A[m], for a positive integer m in a with q not dividing m. Specialization respects this kernel, its O-action, and its quotient. It also respects the image of C under the quotient isogeny. Therefore

    red(a*x_0) = a*red(x_0) = a*y_0

as labelled enhanced curves, with a single fixed choice of inverse convention on both sides.

This is also the ideal action in section 2. On each prime-to-q rational Tate module the ideal quotient replaces the O_p lattice Lambda_p by a_p^(-1)Lambda_p, exactly the multiplier defining the local adelic action. At q the ideal is a unit and the prime-to-q isogeny is an isomorphism on the q-divisible group. At p dividing N it is an isomorphism on the level torsion, preserving the selected eigensummand. Thus it preserves every orientation of y_0. On the tangent space at q its differential is nonzero, so it intertwines the same residue embedding rather than its conjugate. There is no exceptional pure-inseparable ideal action in this argument because the representatives were chosen prime to q.

The equality uses the same chosen reduction place for every class. It does not choose independent places or lifts for different points.

## 4. Bijection, fibers, and every orientation tuple

An equivariant map between nonempty torsors for the same group is bijective: every source is a*x_0, every target is a*y_0, and freeness gives uniqueness. Applying this elementary fact proves the claimed reduction bijection for the reference tuple. Restricting this already proved bijection to the projection onto a fixed supersingular pair gives the fiber assertion. It is not a claim that the map to unlabelled supersingular curves is injective.

Every other tuple used in the coefficient sum has a geometric anchor. At a prime power p^e||N, the geometric Atkin–Lehner operation uses the p^e quotient and its dual subgroup. It exchanges the two cyclic eigensummands at that prime, preserves the other primary subgroups, and has degree prime to q. It lifts in characteristic zero and commutes with reduction. Starting with x_0 gives the anchors with all possible level orientations and the same q-orientation. The description is valid for powers of two as well.

For the other q-orientation, apply q-Frobenius to the reduced enhanced curve and its labelled O-action. The tangent residue embedding is conjugated; the level-primary choices are transported, since N is prime to q. This is the division-uniformizer operation under input 4. Consequently it is a genuine geometric anchor for the other component, not merely an abstract adelic representative. It is not necessary to assert that this other q-component is the image of the same fixed CM-type reduction map. That assertion would be false. The existing coefficient comparison pairs the components by Frobenius instead.

Alternatively a conjugate CM type gives that opposite q-orientation, with the corresponding level choices. In both descriptions the two q-signs remain distinct. On the coarse supersingular pair set defined over F_(q^2), Frobenius and inverse Frobenius have the same action. This statement concerns the geometric operation on the pair and its value under the rational modular parametrization; it does not identify the two labelled embeddings.

## 5. The finite sum and the unchanged weights

Choose z_0 in the target to represent y_0, the reduction of the actual reference Heegner point. For the quadratic class character chi used in (O.1), the established equality gives

    sum_[a] chi([a]) P_M(a*z_0)
      = lambda_M( overline( L * sum_[a] chi([a]) pi(x_D^[a]) ) ).

Specialization, the fixed multiplication L, and the same additive lambda_M commute with this finite sum. If CM reciprocity uses inverse Artin labels, reindex the complete sum by [a] -> [a]^(-1). The quadratic character is unchanged. No class-group cardinality or stabilizer is divided out. All terms are evaluated in the same F_(q^2) domain supplied by input 4 and the current construction of lambda_M.

For a fixed underlying target pair, the stabilizer of a labelled optimal O embedding under R_z^times is R_z^times intersect F^times=O^times={+1,-1}. Thus its orbit has |R_z^times|/2 elements, even when the supersingular curve has extra automorphisms. The existing weight 1/|R_z^times| leaves exactly 1/2. The trace-zero vectors x and -x determine opposite residue embeddings at q. Unit conjugation acts trivially on the residue field, so it does not identify them. This recovers the precise stabilizer and two-orientation convention of the current proof.

The equality of contributions from the other tuples still uses the project's explicit Schwartz and parametrization transformations. At p^e||N both factors change by w_(p^e)*chi_hstar(p)^e, whose product is one. At q the residue-weight sign is (-1/q)=-1 and the norm character is chi_hstar(q)=-1, while lambda_M has Frobenius sign +1. These are retained inputs at current lines 14993–15023. The torsor argument supplies multiplicity one and the geometric sum connection; it does not prove those independently constructed character formulas. Their product yields the same c_0*2^omega(N) coefficient after all 2^(omega(N)+1) tuples are counted.

## Scope

In the current use, F=Q(sqrt(D*h_star)), q=ell_0, and O is maximal because D*h_star is an odd fundamental discriminant. The support gives q inert, q not dividing NDh_star, and F split at every prime of 2N. The field has no extra units. Every premise matches the conductor-one use; none grants the general nonmaximal-order conductor-changing theorem.

This proof is proposed for independent review. It can remove the use of A028/Cornut–Jetchev in the conductor-one comparison while retaining A052, CM reciprocity, and the foundational good-reduction inputs explicitly. It does not close A052's unavailable final-edition comparison, reprove its entire geometric class-set realization, or qualify the final Cornut–Jetchev text. The original source and current manuscript remain unchanged.
