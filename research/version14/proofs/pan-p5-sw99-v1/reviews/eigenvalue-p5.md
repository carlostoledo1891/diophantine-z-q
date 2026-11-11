# Independent review of the Pan 4.3.10 eigenvalue step

Reviewer `/root/astra_v14_assertions_arithmetic`, a distinct model agent from author `/root/sol_protocol_final_review`. I reconstructed the linear-algebra and topological arguments from the pinned proof and actual Pan passages, using local file reads, PDF text extraction and exact hashing. I did not use the author's verdict as evidence. The available runtime does not expose a more specific model identifier for this review; none is invented.

Decision: accept the author's exact PROOF.md SHA256 `66a26b41a2d1bcbae23262f79a769687da3c43884085d0fdd5f97321775dfc93` for the bounded distinct-eigenvalue existence assertion. Author manifest `bec5028db89f810d68e04dfc25c8695a92314650d354b47a4940fa5d64b3b71c` and all six source/proof pins match. This is independent acceptance of that elementary connecting proof under Pan's standing setup. It does not qualify Pan's final journal text, accept all of Lemma 4.3.10, or accept any SW99 transfer.

## Actual source and consumer

I read the pinned Pan author PDF SHA256 `590171129d28a65749cf92b1f6099dbacaa90cc6698828f0a4dfd3da943f4824`, pp. 38–40 and 51–53. Section 4.1.1 makes F totally real and p completely split, and requires chi(c)=-1. A nice prime contains p. Sections 4.1.4 and 4.1.9 give the irreducible lattice realization over A=k[[T]], with coefficient field K=k((T)) of characteristic five in this application. The determinant of r(c) is therefore -1 in K. This is not the characteristic-zero representation to which the eventual Fontaine–Mazur statement is applied.

The exact consumed conclusion on p. 52 is the existence of sigma_0 in G_(F(zeta_(5^infinity))) such that r(sigma_0) has distinct eigenvalues. The surrounding branch is called non-dihedral in Pan. The author's expression “nongeometric occurrence” distinguishes the characteristic-five auxiliary representation; it is not a new assumption that Pan imposed. The proof actually establishes the existence assertion without needing the non-dihedral restriction.

The p. 52 reference to the third nice-prime condition does not itself provide the missing argument in the non-dihedral case, since that condition is conditional on a dihedral inducing field. The new proof supplies this inference directly. The p. 53 dihedral constituent choices remain separate: existence of one regular semisimple element does not select an invariant line in each required adjoint constituent.

## Reconstruction of the proof

Absolute irreducibility follows from the actual odd involution, not from a general implication from irreducibility. Since r(c)^2=I and det r(c)=-1, its eigenvalues are +1 and -1, distinct in characteristic five, with K-rational one-dimensional eigenspaces. Any invariant line after algebraic coefficient extension must be one of those two eigenspaces. Its descent to K would contradict the given irreducibility. This also covers a finite extension used later to split a matrix characteristic polynomial.

If a matrix in r(H), H=G_(F(zeta_(5^infinity))), has a repeated eigenvalue, that eigenvalue is tr(r(h))/2 in K and is nonzero. Dividing by it gives either I or I+A with A²=0 and rank A=1. Multiplication by a scalar does not affect distinctness of eigenvalues or projective fixed lines. Thus the fact that the normalizing scalar need not belong to r(H) causes no gap.

For two nonzero nilpotents with different kernel lines, take those lines as basis vectors. A and B then have respectively upper and lower off-diagonal entries a and b, with ab nonzero. Direct multiplication gives determinant one and trace 2+tab for (I+tA)(I+B). Each t in F5 is represented by an integer power of I+A, so its projective class belongs to the actual projective image of H. The five traces are distinct, whereas x²=4 has only two roots. At least one product therefore has nonzero characteristic-polynomial discriminant. This contradicts the repeated-eigenvalue assumption. No eigenvalues are assumed to lie in K in this final product; nonzero discriminant is precisely the needed separability/distinctness assertion over a splitting field.

It follows that every nonidentity element of the projective H image fixes the same line, if that image is nontrivial. A nontrivial unipotent has exactly one fixed projective line. Normality of H implies that any g in G_F carries that unique common line to another such common line; uniqueness makes it the same line. This contradicts absolute irreducibility.

If the projective H image is trivial, the projective representation factors continuously through G_F/H. Continuity of this factor is justified because the quotient is a quotient of a compact profinite group and PGL_2(K) is Hausdorff. For each n, Q(zeta_(5^n))/Q is totally ramified at five. Every intermediate field has a unique prime above five with local degree its global degree. Since five splits completely in F, any subfield of F embeds in Q5 through a completion of F. Thus the intersection of F with this cyclotomic layer must have degree one. The quotient is Z_5^×.

The product decomposition Z_5^×=mu_4×(1+5Z_5), with the second factor isomorphic to Z_5, proves procyclicity: choose a generator in each factor and apply the Chinese remainder theorem at every finite quotient of orders 4 and 5^n. This verifies the author's procyclic claim; the product of arbitrary procyclic groups would not suffice without these relatively prime finite orders.

Lift a topological generator of this quotient to G_F. Its matrix has an eigenline over a finite extension K'/K, equipped with the extended T-adic topology. The stabilizer of that line in PGL_2(K') is closed, since it is defined by the condition that the wedge of a line generator with its image vanishes. It contains all integer powers of the chosen projective generator. Continuity and density then put the whole projective image in this stabilizer, contrary to absolute irreducibility. This uses no discrete-topology assumption on K or K'.

The resulting element remains an element of the original H. Passing to a splitting field only interprets its eigenvalues; it does not change the element, representation or nonzero discriminant. Pan may work with G_(F,P) because the representation is unramified outside the prescribed set. Pulling back to G_F and then projecting the resulting element gives the same matrix and cocycle-domain element; the cyclotomic kernel condition is retained.

## Nine application checks and affected uses

| Check | Finding |
|---|---|
| Hypotheses | Irreducibility, oddness, characteristic five, continuity and complete splitting of five are actual standing premises. |
| Objects | r is the same characteristic-five nice-prime representation over k((T)); H is the full cyclotomic-tower kernel. |
| Domain and indices | t ranges over five distinct elements of F5; cyclotomic levels are all positive n. |
| Connecting maps | Scalar normalization, projectivization, quotient by H and extension K'/K are explicitly compatible with the original representation. |
| Identity of consumed object | The final sigma_0 lies in the required original group and has nonzero discriminant under the actual r. |
| Normalizations | tr/2 and determinant-one normalization are legitimate in characteristic five; projective scalar changes preserve eigenvalue multiplicity. |
| Local conditions | Complete splitting gives F∩Q(zeta_(5^n))=Q. No potential semistability or characteristic-zero local condition is imported. |
| Exceptions | The five-trace count is specific to this p5 proof; no arbitrary-prime claim is accepted. The scalar-projective case is separately handled. |
| Downstream | Accepted only as sigma_0 existence in the p52 non-dihedral branch. The cocycle adjustment, irreducibility of the adjoint, invariant/coinvariant comparison, finite-length induction and prime selection remain external to this review. |

The related-use audit includes the repeated-eigenvalue sentence on p. 52 and the superficially similar p. 53 constituent selection. The latter needs additional information and receives no approval here. I did not review or adopt the separate SW99 R2 geometric argument mentioned by the author. No manuscript has been edited, and incorporation of this proof remains an integration task.
