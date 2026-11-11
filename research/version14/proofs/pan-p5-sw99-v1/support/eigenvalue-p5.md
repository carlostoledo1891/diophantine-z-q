# Distinct eigenvalues in Pan 4.3.10 at p=5

Author /root/sol_protocol_final_review. This is a separate connecting proof awaiting independent review. It neither adopts the SW99 transfer nor changes a manuscript. It concerns the characteristic-5 nice-prime representation, not the characteristic-zero 5-adic representation that is the eventual modularity target.

## Available and needed conclusions

The pinned Pan author PDF has SHA256 590171129d28a65749cf92b1f6099dbacaa90cc6698828f0a4dfd3da943f4824. Section 4.1.1, p38, takes F totally real with 5 completely split. Sections 4.1.4 and 4.1.9 take the irreducible nice-prime representation r over K=Frac(k[[T]]), with k a finite field of characteristic 5 and with the given continuous lattice realization. Its determinant on complex conjugation is -1. Lemma 4.3.10, p52, needs an element of H=G_(F(zeta_(5^infinity))) whose image under r has distinct eigenvalues. The printed non-dihedral paragraph refers to the third condition of 4.1.4. That condition is phrased for an inducing field when the representation is dihedral. The proof below supplies this distinct-eigenvalue step without using that clause.

The later p53 dihedral argument needs more than distinctness. It requires a rotation and a nontrivial coset element yielding fixed lines in two different adjoint constituents. The separately authored SW99 R2 geometric argument supplies those choices through field disjointness. This proof is for the earlier p52 nongeometric occurrence and does not replace either p53 constituent check.

## Proof

The representation is absolutely irreducible. A complex conjugation acts as an involution of determinant -1, with distinct K-rational eigenvalues 1 and -1. A line invariant after extending coefficients must therefore be one of its two K-rational eigenlines, and would contradict irreducibility over K.

Assume every element of r(H) has a repeated eigenvalue. Because 2 is invertible, that eigenvalue is half the trace and is in K. It is nonzero. In projective terms the image is either the identity or a nontrivial unipotent. Suppose two such nontrivial images have different fixed lines. Take one lift normalized to U=I+A and the other to V=I+B, with A and B nonzero rank-one nilpotent operators. Use their respective kernel lines as a basis. Then A and B are strictly upper and strictly lower triangular respectively, with nonzero off-diagonal entries a,b. For each t in F5, the projective class of U^t V is represented by the matrix (I+tA)(I+B), since A squared is zero. These are classes of images of elements of H, even though the normalization scalars need not themselves be image values. Each displayed matrix has determinant one and trace 2+tab. As t ranges over F5 these are five distinct values in K, and at most two satisfy trace squared equal to four. Some matrix has distinct eigenvalues, a contradiction.

Consequently, if the projective H image is nontrivial, all of its nontrivial elements share a unique fixed line. As H is normal, this line is stable under all of G_F. It contradicts absolute irreducibility.

If the projective H image is trivial, the projective G_F image factors continuously through Gal(F(zeta_(5^infinity))/F). For every n, Q(zeta_(5^n)) is totally ramified at 5, by the Eisenstein polynomial Phi_(5^n)(1+X). Its nontrivial intermediate fields are ramified at 5, whereas every completion of F at 5 is Q5. Hence F has trivial intersection with every layer and with their union. The quotient is therefore the full group Z_5^times, which is procyclic since it is the product of cyclic order four and a topologically cyclic pro-5 group. Choose a lift in G_F of a topological generator of that quotient. A matrix representing its projective image has an eigenline over a finite extension K'/K. The stabilizer of that line is closed in PGL2(K'), since preserving a line is a closed matrix condition. It contains every power of the generator's image, hence by continuity the entire projective image. This again contradicts absolute irreducibility.

Therefore H contains an element whose image has distinct eigenvalues. The assertion can be tested in K by its nonzero discriminant, so using an algebraic extension to discuss eigenlines does not change the resulting element or conclusion.

## Consumer boundary

This proves only the distinct-eigenvalue existence needed for the p52 nongeometric argument. The subsequent cocycle adjustment, invariant and coinvariant comparison, finite kernel/cokernel induction, and prime selection retain their own source obligations. No assumption is made here about Pan's final journal wording. The proof uses the actual characteristic-5 coefficient field and cyclotomic splitting hypotheses, and makes no claim for arbitrary odd primes.
