# Finite forgetful map and Picard norm at the current modular quotient

Author: /root/v14_h6_coverage. Status: concrete source attachment and connecting argument for independent review. This note does not change the manuscript or its frozen source set.

## Exact caller and boundary

The caller is manuscripts/quartic_v14.tex, SHA-256 1f7bf748843d67c6a67d9863931ff0a15ca2548ae171ec1c1ce34b9002eb70a8, lines 1831–1855. The two previously unbound inputs are the finite surjective rational forgetful map in 1835 and the finite-flat determinant norm inducing the rational Picard morphism in 1846–1851. The already accepted modularity map rho, divisor pushforward, Picard identification of A, and final surjectivity argument remain separate inputs. No finiteness assumption on Sha is used here.

## 1. The actual forgetful morphism

Diamond and Im, Modular forms and modular curves, Canadian Mathematical Society Conference Proceedings 17 (1995), printed pages 77–79, especially section 9.3 on page 79, supplies canonical smooth proper models of X_1(N) and X_0(N) over Z[1/N]. It identifies X_0(N) as the quotient scheme for the natural action of (Z/NZ)^* on X_1(N). For N<=4 the same page records equality of the coarse curves. The action changes the chosen generator of the cyclic subgroup; its quotient is the actual forgetful map, not an unrelated map between curves. These statements were visually checked on PDF pages 39–41, together with the publication title page.

Specialize the quotient to Q. The finite-group quotient map is finite and surjective: on quotient affine charts, each element upstairs satisfies the monic orbit polynomial with invariant coefficients; the finite-type invariant construction gives a finite integral algebra, and lying-over gives surjectivity. Equivalently this is the canonical finite quotient already supplied by the quotient-scheme construction. We use coarse curves, not a claim that the corresponding stack morphism is finite representable. The possible ineffective element -1 does not affect finiteness or surjectivity. For small N the equality of coarse curves suffices. No degree formula is needed.

Thus u:X_1(N)->X_0(N) is a finite surjective Q-morphism. Compose with the already supplied finite surjective rho:X_0(N)->A. Its composite f is finite surjective. Source and target are smooth geometrically integral projective curves over Q. At a closed point of A, its local ring is a DVR. The finite module defining f is torsion-free over that DVR: a nonzero function on A pulls back to a nonzero function on the integral source and cannot annihilate a nonzero section. A finite torsion-free module over a DVR is free. At the generic point it is a finite-dimensional vector space. Therefore f is finite locally free, of a positive constant degree d. This derives the finite-flat hypothesis actually needed below; it is not inferred merely from the word finite.

## 2. Determinant norm and the rational Picard morphism

The Stacks Project, tags 0BD2 and 0BCY, supplies the canonical norm for a finite locally free morphism, compatibility with arbitrary base change, and the induced multiplicative norm on invertible sheaves. In tag 0BD2 the function norm is the determinant of multiplication; tag 0BCY glues the norms of transition functions. Both complete statements and proofs were read directly at their canonical URLs. HTML byte pins, if subsequently obtained, supplement these stable tag locators and do not replace the stated hypotheses.

Here is the explicit identification with the formula used in the manuscript. Locally on the target, a line bundle L on the finite source is trivial over the inverse image of an open set. Write B=f_*O_X on such an open set and choose a generator s of L. Then f_*L is identified with B. Replacing s by u s changes its determinant trivialization by det(m_u), the function norm of u. Dividing by det(B) removes the chosen trivialization of the underlying algebra. Consequently

    N_f(L) = det(f_*L) tensor det(f_*O_X)^(-1)

has exactly the transition functions used by the source construction. Multiplicativity follows from multiplication of these transition functions, not from an incorrect claim that determinant is multiplicative on arbitrary tensor products of vector bundles. Changing bases cancels in the displayed ratio.

For every Q-scheme T, the base change f_T remains finite locally free. Its affine pushforward is restriction of scalars for a finite locally free algebra, which commutes with arbitrary base change on these modules. Exterior powers of finite locally free modules commute with base change as well. The same formula therefore gives N_{f_T}, naturally in T. If M is a line bundle from T, the projection formula gives N_{f_T}(L tensor pi_X^*M)=N_{f_T}(L) tensor pi_A^*(M^d). Hence norms respect the quotient by base line bundles. After fppf sheafification they define a natural homomorphism Pic_{X/Q}->Pic_{A/Q}. This argument uses the Picard sheaf, not an assertion that every rational point of that sheaf has a rationally defined line-bundle representative.

Using the Picard varieties/Jacobians already supplied in the caller, representability and Yoneda turn this natural transformation into a Q-morphism of group schemes. It sends the identity to the identity. After algebraic closure, the connected identity component of Pic_X maps into the connected identity component of Pic_A, so restriction gives a Q-defined homomorphism Pic^0_X->Pic^0_A. This needs no Q-point of X_1(N), no chosen universal line bundle over Q, and no identification of the entire Picard functor with its Q-valued line bundles.

Finally, on a divisor line bundle the norm agrees with divisor pushforward. Locally this follows from the same determinant norm on functions and its valuation formula; this is the already retained Silverman II.3.6(c),(d) input in the caller. Thus the constructed morphism is the displayed f_* rather than a second map with an unspecified relation to it. Its surjectivity is the separate point-difference argument in lines 1852–1855, which is not re-audited here.

## Scope and source access

Published Diamond–Im PDF: work/source-risk-review-20261107/diamond-im-download-root-001/local-only/diamond-im.pdf, SHA-256 31cc7ff62c6d9177d2f02f93bb333ac97a1eacc79eb14fed9eee20b6c5292411. Source URL https://wstein.org/msri06/stein/Diamond-Im-Modular_forms_and_modular_curves.pdf. The scan and page renders stay local-only and are not proposed research-history payloads.

Norm sources: https://stacks.math.columbia.edu/tag/0BD2 and https://stacks.math.columbia.edu/tag/0BCY, read 2026-11-09. The current numbering was Lemmas 31.18.6 and 31.18.2; tags, not mutable numbering, identify the sources. The elementary finite-flat and relative-Picard specializations above are this note's connecting derivation. They require independent review; this author record is not that review.
