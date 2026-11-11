# Geometric isogenies in the discriminant-210 fiber

Author proposal by /root/astra_v14_source_review. Arithmetic is the independent reviewer. The manuscript and prior proof packets remain unchanged.

## 1. Objects and incoming statements

Retain the actual discriminant-210 quaternion division algebra B/Q, chosen maximal order and positive datum, entire canonical principal-three curve Y, and fiber surfaces over the splitting field L constructed in H5. The normalizer acts on this same all-component curve. Every geometric homomorphism between these fiber surfaces is defined over this same L.

The accepted full-cover proof, Sections 6-7, identifies integral marked objects with rational PEL quadruples and identifies their canonical normalizer action. The accepted Hodge-centralizer calculation identifies the full geometric endomorphism algebra as B in the non-CM case and M_2(k) in the CM case. The H5 Hom argument supplies simultaneous descent to L. The chosen integral datum and the normalizer-orbit description of the actual fiber remain incoming statements.

## 2. Geometric isogeny

Fix an embedding into C and a fiber surface A. In the rational PEL description, right multiplication of the finite-adelic level coordinate by a normalizer element changes the represented integral lattice and leaves the rational Hodge object fixed. The two lattices are commensurable. They agree with standard lattices at all but finitely many primes, so one nonzero integer clears their local denominators.

Section 6 of the full-cover proof realizes the new lattice by a finite torsion subgroup quotient after clearing denominators. Thus the integral objects have isogenous underlying abelian varieties. Compose with the rational PEL identification if changing representatives requires one. Section 7 identifies this action with the canonical normalizer action on the same Y. Hence this applies to the actual conjugate fiber surfaces A and A_sigma. These operations are algebraic in that comparison. The retained algebraic-closure descent for homomorphisms identifies their complex and geometric Hom groups. Choose a geometric isogeny f:A -> A_sigma. No degree bound or choice coherent in sigma is asserted.

## 3. Endomorphism algebra

Use the full geometric endomorphism algebra. The retained centralizer proof starts with rank-one left B-homology and right complex structure J. It obtains B tensor K^op, where K=B intersect R[J], and proves K=Q or K imaginary quadratic. In the non-CM case K=Q. The published Hodge equivalence and separately proved algebraic-closure descent therefore give End^0(A)=B. The same holds for A_sigma by transport through f. The CM case is not used below.

## 4. Specified quadratic embeddings

Let E be the chosen abstract quadratic field, with specified embeddings i:E -> End^0(A) and i_sigma:E -> End^0(A_sigma). Put

    j(x)=f^(-1)i_sigma(x)f in End^0(A)=B.

The images i(E),j(E) are quadratic subfields, and i(x) -> j(x) is a Q-algebra isomorphism. Voight, Quaternion Algebras, published 2021 edition, Corollary 7.1.5 and its direct proof on page 97 provide b in B^* with

    j(x)=b^(-1)i(x)b for every x in E.

Set g=f b^(-1). Then

    g i(x)=i_sigma(x)g for every x in E,

since b^(-1)i(x)=j(x)b^(-1) and f j(x)=i_sigma(x)f. This respects the specified identification of E, not just the two unlabelled subfields.

Choose a positive integer n clearing the denominators of g in Hom(A,A_sigma) tensor Q. The geometric homomorphism h=ng satisfies the same identity. It is an isogeny: clear denominators of its rational inverse to obtain compositions equal to multiplication by nonzero integers. Therefore h is surjective with finite kernel. No integral embedding of the whole field E is required.

## 5. Same field L and current conclusion

The existing simultaneous Hom statement applies to h, so h is defined over L. It also applies to endomorphisms and their rationalizations. Thus both E-actions and the intertwining identity are defined over L. Each selected non-CM conjugate surface has an E-linear isogeny over L, and E embeds into its endomorphism algebra over L. Since E has degree two and the variety is a surface, this supplies GL2-type over L.

This is the pairwise compatibility at current lines 7833-7839. It does not choose a cocycle-compatible system of isogenies, construct a compatible system of Galois representations, bound an isogeny degree, or descend a GL2-type variety to Q. The separate bounded descent conclusion remains separate as the current paragraph states.

## 6. Source and review scope

The first-edition errata dated August 5, 2026, page 2 item 19, corrects the unit-group notation in the proof of Corollary 7.1.5 and removes an optional splitting-field parenthesis. We use the separable-closure proof with that correction. The quadratic fields here have characteristic zero; the corollary's embedding conclusion is unchanged. The published chapter and later errata are separately pinned.

This author previously reviewed the full-cover construction and contributed related Hodge-source work. Earlier decisions are used only at their existing scopes. This packet claims no independent acceptance of its new connection or ordinary-record adoption.
