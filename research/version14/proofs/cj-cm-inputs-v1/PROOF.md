# Retained CM inputs for the conductor-one comparison

This is an authored source-to-application supplement. It supplies the retained CM inputs of the conductor-one proof with SHA256 `67fde89bb38f6bd50c4588a359de143480978c2e802eed64a1ef013fbdfd8ed8` and of the separately reviewed good-reduction proof with SHA256 `37d6c76b3ccb37096421ae2d083b3a470af5129744c2e9f3cd041d6d781c2921`. It does not assert the full conductor-one comparison independently of its other premises.

## 1. Domain and labelled objects

Let F be an imaginary quadratic field, O its maximal order, and fix an embedding phi:F→C. Fix algebraic closures inside C and at an odd rational prime q, together with the reduction place. Assume q is inert and unramified in F. Let N≥1 be prime to q disc(F), with every prime dividing N split in F. The conductor-one application also assumes O×={±1}; the arguments below do not divide by this group. All isomorphisms of triples preserve the O-labels pointwise. The type condition is d iota(alpha)=phi(alpha) on the tangent space for every alpha∈O.

For every p^e exactly dividing N, select one of the two prime ideals P over p and put n=∏P^e. Thus O/n≅Z/NZ. The selected subgroup of an O-labelled elliptic curve A is C=A[n], meaning the simultaneous kernel of all iota(alpha), alpha∈n. This specifies a subgroup, not a generator or full level structure. The fixed type is retained under Galois automorphisms fixing F. No assertion identifies the two conjugate types or changes the chosen reduction place.

## 2. Uniformization, the ideal action, and degree

Use final Silverman, VI.4.1 and Corollary VI.4.1.1, VI.5.1.1 and VI.5.3, with the official 2015 corrections. They identify complex elliptic curves with lattices and origin-preserving morphisms with complex scalars carrying one lattice into the other. For a curve of the fixed type, its uniformizing lattice Lambda is stable under phi(O). Its rational span is a one-dimensional F-vector space: it has Q-dimension two and a faithful F-action. Choosing a nonzero vector and scaling identifies Lambda with a fractional O-ideal. Since O is the full ring of integers, this ideal is invertible. This is also the correspondence in Silverman C.11.1, p426.

For two fractional O-ideals I,J, a complex scalar u with uI=J belongs to F×: choose nonzero x∈I and note ux∈J⊂F, so u=(ux)/x∈F. Conversely multiplication by an element of F× preserves every O-label and the selected subgroup. Hence fixed-type labelled triples, with this fixed n, are indexed by Pic(O).

For an integral nonzero ideal a, the identity on C induces the O-linear isogeny

    C/Lambda → C/(a^(-1)Lambda).

Its kernel is a^(-1)Lambda/Lambda=A[a]. Indeed, alpha z∈Lambda for all alpha∈a is equivalent to z∈a^(-1)Lambda; this follows locally from the fact that both ideals are principal over each O_P. Its cardinality is [a^(-1)Lambda:Lambda]=|O/a|=Norm(a), by the same local calculation. Characteristic zero makes the map separable, so its degree is Norm(a). This gives the action [a]*A=C/(a^(-1)Lambda); a principal ideal acts by an isomorphism. Composition multiplies the ideals. Multiplication of invertible ideal classes is free and transitive, so this is a torsor, not a sum with multiplicities.

The selected subgroup is n^(-1)Lambda/Lambda. Its local factor at each selected P has order p^e and is cyclic, so the full subgroup has order N and is cyclic. If a is prime to N, the a-isogeny carries this subgroup isomorphically to n^(-1)a^(-1)Lambda/a^(-1)Lambda, since locally at every p|N it is an isomorphism. This includes arbitrary exponents e and p=2 when 2 splits. The argument is not restricted to squarefree N.

Every ideal class has an integral representative prime to any specified finite set S of prime ideals. To see this without a prime-distribution theorem, choose an integral ideal I representing the inverse class. For each P∈S choose x_P∈I with valuation v_P(I). The Chinese remainder theorem on I/(∏_{P∈S}P)I gives x∈I having these images in I/PI. Then a=(x)I^(-1) is integral, represents the desired class, and has valuation zero at every P∈S. In particular one can require a to be prime to Nq and any additional finite bad set.

## 3. Integrality and a common finite diagram

The existing final Fowler source, §2.1 pp612–613, associates to every imaginary quadratic order discriminant Delta a monic polynomial H_Delta(T)∈Z[T] whose roots are its singular moduli. The definition at p607 uses the usual elliptic j-invariant. Every A above has Delta=disc(F), so j(A) is an algebraic integer. No class-number estimate, exceptional discriminant, or effectiveness result from Fowler is used. Silverman C.11.2(a), p426, independently states the same integrality for maximal orders.

Consequently every j(A) is integral at the fixed q-adic place. The good-reduction supplement applies Silverman VII.5.5 to each curve in a fixed finite diagram, takes a common finite extension, and then uses BLR and EGA to extend the arrows and all O-labels. The present argument supplies its integral-j premise and its characteristic-zero ideal quotient with degree Norm(a). It does not replace any of that supplement's extension, kernel-specialization, or quotient arguments. The field may depend on the finite diagram; no finite field containing all torsion or all diagrams is required.

## 4. Reciprocity and the inverse convention

Silverman C.11.2(c),(d), p426, says that H=F(j(Lambda)) is the Hilbert class field and that all the j-values for Pic(O) lie in it. C.11.4, p427, gives

    j(Lambda)^(Frob(P)) = j(Lambda P^(-1))

provided there is an H-model with that j-invariant having good reduction at every prime above P. This hypothesis must not be dropped. We retain the printed Frobenius convention of C.11.4 in this formula. That passage does not itself define the residue action. The manuscript's arithmetic convention means x↦x^(Norm(P)); the already used Milne class field notes v4.03, Introduction p7 and Chapter I p20, explicitly define this convention. These are qualified author notes, used here only to record that definition. We do not promote the notes to a final published comparison of Silverman's convention. The bounded consumer is invariant under one global switch to inverse Artin, as proved below.

There are finitely many j-values. Silverman III.1.4(c), p45, supplies an H-model for each. Exclude from F the primes below all their bad primes. This is a finite set: an elliptic curve given by a Weierstrass equation over a number field has a smooth integral model away from the finitely many denominator and nonzero-discriminant primes. Enlarge this set by the primes dividing Nq. Section 2 supplies an integral ideal a representing each class and avoiding this set. Factor a into prime ideals. At every successive factor, C.11.4 applies to the corresponding j-value because all models' bad primes were excluded. The commuting Frobenius automorphisms multiply to Art(a) in the source convention, and induction gives

    j(Lambda)^(Art(a)) = j(a^(-1)Lambda).

The Artin map for the Hilbert class field factors through Pic(O); thus this formula holds for every class, independently of its chosen good representative. This uses the ordinary Hilbert class field Artin isomorphism implicit in the source, not a new distribution statement about prime ideals. No claim that the chosen H-model has good reduction at q is made.

This equality of j-invariants lifts to the required labelled triple. Silverman III.1.4(b), p45, gives an origin-preserving isomorphism g over the algebraic closure between the two elliptic curves. A characteristic-zero endomorphism is determined by its tangent scalar, as follows already from VI.4.1. Because Art(a) is represented by an automorphism fixing F, the conjugated O-action has the same type phi. Thus g iota(alpha) g^(-1) and the target's labelled iota(alpha) have identical tangent scalar phi(alpha), and are equal for every alpha. The isomorphism is O-linear and therefore carries A[n] to the target's n-kernel. This proves

    (A,A[n],iota)^(Art(a)) ≅ [a]*(A,A[n],iota).

It also shows that these labelled isomorphism classes are fixed by G_H: the same argument applies when the j-invariant is fixed. Models and arrows may still require a finite extension, which the good-reduction supplement permits. We do not infer a full chosen torsion basis or an isomorphism defined over H from equality of j-invariants.

Final Cai–Shu–Tian supplies an independent published compatibility check. At p2524 its P_b is C/b→C/(bn^(-1)), and is defined over the ring class field. At pp2527 and2531 it gives the Artin map and the equality of the Galois and Hecke actions on CM points. In conductor one its P_b equals our [b^(-1)]*P_O. Accordingly P_b^(Art(a))=P_(a^(-1)b) in the convention just fixed. We use the explicit Silverman formula to fix this inverse, rather than infer it from the bare word “reciprocity.” CST's automorphic height hypotheses are not imported into the elementary lattice action.

If the manuscript's bracket convention uses inverse Artin, reindex the entire class sum by a↦a^(-1). Its genus character is quadratic, so chi(a^(-1))=chi(a). This preserves the unaveraged sum and the chosen reference point. All quotient actions and target class labels must be changed together. It does not permit changing a reduction place separately for different classes. The genus-character construction itself is a separate existing input.

## 5. Forward inert reduction

Final Gross–Zagier, On singular moduli, p198 sets O=Z[tau] and F=Q(tau), and p199, the first paragraph, states that (Delta/q)=-1 gives supersingular reduction at all primes above q. This general forward sentence cites Deuring; it appears in the proof of Corollary 2.5(2), whose further congruence conclusions concern q<12. Only the general forward sentence is used, not those small-prime congruences. The current Delta=disc(F) is fundamental, so an integral basis writes O=Z[tau]; q inert and unramified gives exactly that Legendre-symbol condition. Use the good models already obtained after the common finite extension. Their geometric special j-invariants are the reductions of the same integral singular moduli, so the elliptic curves are supersingular. This is independent of the finite extension used to obtain good reduction. The statement includes q=3; no argument here requires q≥5.

This application is solely forward. It does not assert that every oriented supersingular embedding lifts, that a lift is unique, or that reduction is surjective or injective on an oriented class set. In particular we do not use Gross–Zagier Proposition 2.7 as a unique-lifting theorem. The conductor-one proof obtains the class-set bijection from its distinct torsor and equivariance arguments, with its remaining geometric premises.

## 6. Exact joins and remaining boundaries

For the conductor-one proof, Sections 1–2 above supply its Section 1 fixed-type source torsor and prime-to-Nq ideal isogenies; Section 4 supplies the reciprocity interpretation needed in its Section 5 weighted sum; Sections 3 and5 supply the integral-j and forward-supersingularity premises of its Section 3. For the good-reduction proof, Sections 2–3 above supply precisely the assumed characteristic-zero quotient, degree and j-integrality. Its reviewed geometric specialization then gives the same-place O-equivariance, q-divisible and tangent labels, and selected N-level images.

The enhanced supersingular Eichler class set, rational Skolem–Noether, local lattice/Dieudonne classification, existence of the target reference object, right-uniformizer Frobenius description, genus-character identity, and final weighted theta comparison remain separate applications. Nothing here asserts a completed review of their transitive sources. Source reuse is deliberate: historical A065 already used Fowler integrality, A027 already used final CST, and the good-reduction supplement already pinned final Silverman with errata. The new records expose the present consumers and connecting derivations; they do not reclassify missing exposition as a false theorem.
