# Khare transfer completion002: two Section5 connections

Reviewer: `/root`, model reviewer. Author of completion002: `/root/astra_v14_baseline_theta`. `/root/astra_v14_baseline_compiler` identified and supplied the explanations underlying the two changes. I did not author either connection. I read the actual old and new passages and the relevant final DFG source, rather than treating the compiler's suggested repair as an acceptance.

This review accepts only the two mathematical connections in DELTA.json against the pinned completion001 and completion002 proofs. It assumes the separately reviewed inputs stated in the surrounding argument: an absolutely irreducible rho of rank two, the determinant identity from Section3, the weight and zero-Tate-twist identification from Section4, the specified ordinary or DFG modularity result, and the published full-family compatibility assertion. It does not approve the remaining completion, these retained premises, or the full Item1 route.

## The full member at an omitted coefficient place

The final DFG definition on669 specifies a full collection of realizations and defines L-admissibility using compatible rational Frobenius-semisimple Weil–Deligne representations. No blanket semisimplicity axiom for every Galois realization is provided. The footnote on684 states that the newform object extends to the full category and is L-admissible everywhere. Thus the old blanket appeal to semisimplicity should not stand without an argument.

The new paragraph provides that argument. After fixing the coefficient embedding and the normalization in the following paragraph, let W be the full object's rank-two member at the coefficient place of rho. Its good Frobenius polynomials agree with those of rho dual. Equality concerns characteristic-zero polynomials at the same embedding, not congruences. Chebotarev density and continuity give equality of characters; Brauer–Nesbitt identifies W's semisimplification with the already absolutely irreducible rho dual. Since semisimplification is itself simple and has dimension two, W has length one and is simple. Indeed any proper nonzero invariant subspace would give at least two nonzero composition factors. Therefore W is isomorphic to rho dual itself. This is a connection to the actual full member, not an assertion only about its semisimplification.

The full-family assertion remains the published DFG input, with its named Saito antecedent. The elementary length argument does not prove that source assertion. The source's rank and common coefficient field, and the caller's absolute irreducibility, are essential. The new paragraph retains them.

## Nebentype, duality and order of normalization

I read final DFG printed683, including (16), and visually read684, including (18) and its full-family footnote. I also read (22) on685. Equation(16) gives determinant M_psi(1-k). Equation(18) uses geometric Frobenius and has the inverse finite-character factor in both trace and determinant terms. It therefore must not be equated with the naive dual of an arbitrarily normalized arithmetic realization while the finite character is nontrivial. Equation(22) supplies the finite-character twisting operation on the newform object.

The replacement paragraph treats the two modularity outputs separately. For ordinary lifting, the retained input is the arithmetic representation attached to f. Its determinant is epsilon times chi_p^(k-1), where epsilon is its arithmetic nebentype. Comparing with the already established determinant of rho first gives epsilon=1. Only after that step is DFG's geometric-Frobenius polynomial identified with that of rho dual. At trivial character, geometric Frobenius on the dual has the same eigenvalues as arithmetic Frobenius on the original representation, so both give X^2-a_v X+v^(k-1).

For the DFG lifting output, undo the finite twists using (22) and denote the resulting cohomological form by g. The retained filtration argument has excluded a nonzero Tate twist. The determinant of rho dual is chi_p^(1-k); comparison with (16) forces the one-dimensional finite-character realization M_psi to be trivial, hence psi itself trivial. This does not depend on choosing one of two inverse Artin conventions, because triviality is unchanged by inversion. It does require the actual cohomological representation supplied by the lifting step at the fixed coefficient embedding. With psi=1, (18) then gives the needed good polynomials and the preceding full-member argument applies.

This order avoids a circular normalization: the ordinary determinant is computed in its arithmetic convention before comparison to M_f, while the DFG output is normalized by its own determinant formula before dualizing. Neither paragraph asserts that nontrivial-character M_f is automatically the dual of the usual arithmetic realization.

## Scope and exact binding

Accept these two changes, conditional on the unchanged surrounding inputs just identified. CHECKS.json verifies that applying exactly the two recorded replacements to the pinned001 proof gives the entire pinned002 proof, and binds the actual final DFG PDF and pages read. The checks establish identity, not the mathematical judgment above.

The source editions of Saito and the original Khare article, the local ordinary lemma, the other residual branches, global compatible-system construction, scalar/tame caller integration, all new source/application records outside these two paragraphs, current manuscript adoption, inventory coverage and release approval remain outside this review.
