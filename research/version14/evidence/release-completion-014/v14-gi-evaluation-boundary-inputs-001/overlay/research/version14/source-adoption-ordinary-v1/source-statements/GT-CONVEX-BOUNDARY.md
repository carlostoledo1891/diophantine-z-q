# GT convex boundary estimate

Project paraphrase of Corollary A.2, printed p.1810. The local consumer derivation remains in the frozen proof.

**statement**: For a convex body K contained in [-N,N]^d and 0<epsilon<1, the epsilon N neighborhood of its boundary has volume O_d(epsilon N^d).

**objects**: Bounded convex body in Euclidean d-space and its boundary neighborhood.

**hypotheses**: K is a convex body in the stated box; N>0 and 0<epsilon<1.

**quantifiers**: Every such body and epsilon, for each fixed dimension d.

**parameter_range**: Euclidean dimension d is fixed.

**uniformity**: The implicit constant depends only on d, not on the shape of K.

**constants**: O_d(epsilon N^d).

**normalizations**: Ordinary Euclidean distance and Lebesgue volume.

**exceptional_cases**: The cited corollary does not itself state lattice counts or the empty-interior extension; these are local consumer deductions.

**limit_order**: Fix dimension and bounding box, then apply the boundary-volume estimate at the chosen positive thickness.
