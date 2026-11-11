# General-type first-order connection for the proposed Hu–Tan route

Author: `/root/astra_v14_baseline_compiler`, 2026-11-08. This is a new author proposal. It preserves compiler002, followup003, auxiliary-transfer004 and the independent RED bridge review. No independent acceptance or current manuscript incorporation is claimed.

## 1. Exact scope

The O2 proposal identifies locally algebraic vectors at arbitrary-target supercuspidal characteristic-zero points. That is a zero-order statement. The general-type Breuil–Mezard criterion also requires a first-order bound, and the dimension of a K-type in a smooth representation is a separate input. This packet proves two small connecting lemmas, states exactly how they enter the original criterion, and retains the other published theorem imports. It does not reprove full Breuil–Mezard, Hu–Tan or their global patching theorem.

Use G=GL2(Q5), K=GL2(Z5) and a sufficiently large finite coefficient field E. All Banach representations below are admissible and unitary, and have fixed central character zeta. Banach exact sequences have closed embeddings and the quotient topology. Absolute irreducibility means irreducibility after every finite coefficient extension. Locally algebraic vectors are denoted by the subscript alg. No assertion is made about residual irreducibility.

## 2. The exact Dospinescu import and its domain

The pinned 44-page author text has SHA256 a7e5be90904309fa74ef0b074e60376a217c13d05e854c39636cfbc0f06524c2. Its page2 defines a supersingular Banach representation as absolutely irreducible and not a subquotient of a continuous parabolic induction of a unitary torus character. This is the nonordinary Banach condition, not the smooth supercuspidal condition and not a condition on mod5 reduction. Page3 relates this category, at p>=5, to absolutely irreducible two-dimensional Galois representations with determinant epsilon*zeta. Nonzero algebraic vectors correspond to de Rham representations with distinct weights. The same finite coefficient field and the same actual Banach object are used throughout.

Retain the exact Theorem1.3 and Propositions1.4–1.5 on author page5. The first identifies the span of self-extensions with dense algebraic vectors with the fixed-determinant de Rham extension space. The second says the dimension is one except for its defined special Galois case. That special case is potentially crystalline and its Weil–Deligne representation is a sum of two characters with ratio norm or inverse norm. Proposition1.5 says precisely that this special case occurs if and only if Pi_alg is reducible. In that case Pi_alg has the displayed Steinberg-by-algebraic extension. It must not be confused with a noncrystalline smooth special-series factor, which can have irreducible Pi_alg.

These are imports of the inspected author statements. The final article is Compositio151 (2015),1462–1498, DOI10.1112/S0010437X14007921. No exact final-text comparison is claimed. The published metadata is not a proof of unchanged numbering or statement. This qualification remains even if the connecting proof below is accepted.

## 3. Uniform nonordinary RED connection

Let Pi be nonordinary and absolutely irreducible, with nonzero irreducible Pi_alg. Let R(Pi) be the E-linear span inside Ext1_{G,zeta}(Pi,Pi) of extension classes

    0 -> Pi -> X -> Pi -> 0

for which the induced sequence on algebraic vectors is exact. This is exactly BM Definition4.17, not the whole Banach Ext group.

For each generator, the already independently accepted exactness-to-density lemma implies that X_alg is dense in X. To recall the full topological reason, put C=closure(X_alg). The first Pi_alg lies in X_alg, and its closure in the embedded Pi is Pi by topological irreducibility. Hence Pi is contained in C. The quotient C/Pi is closed in X/Pi, since its inverse image under the quotient map is C. Exactness on algebraic vectors implies that this quotient contains the dense Pi_alg of X/Pi. Thus C/Pi=X/Pi and C=X. This does not assert that an arbitrary image of a closed subspace is closed.

Every generator therefore lies in Dospinescu's dense-algebraic extension set. Passing to linear spans gives

    R(Pi) subset Ext1_alg(Pi,Pi).

By Proposition1.5, irreducibility of Pi_alg excludes the special Galois case. Theorem1.3 and Proposition1.4 then give dimension_E Ext1_alg(Pi,Pi)=1. Consequently dimension_E R(Pi)<=1: Pi satisfies RED.

The determinant in this application is fixed over E[t]/(t^2), equal to epsilon*zeta. It is not the determinant of the underlying four-dimensional E-vector space. The theorem is applied to the same fixed-central-character category. The split extension represents zero and introduces no exception. Taking spans does not assume that each vector in a span has a separately selected dense representative. No converse from density to exactness is used, including the converse questioned in the author's Remark1.6.

This proves RED for every nonordinary Pi with irreducible nonzero Pi_alg, including nonordinary principal-series and noncrystalline special-series cases. It does not cover ordinary Banach representations, and it makes no bound for the excluded reducible Pi_alg case. It can replace the nonordinary part of BM Theorem4.19 once its exact source import and this new application receive independent acceptance. It does not delete the original Section7 proof or alter its historical status.

## 4. Direct conversion of RED to the first-order type bound

Here Pi may be ordinary or nonordinary, provided RED has been supplied in its own scope. Assume Pi_alg is irreducible, End_G(Pi)=E, and V is a finite-dimensional locally algebraic K-type with

    dimension_E Hom_K(V,Pi)=1.

The last equality is a retained multiplicity statement, not a consequence of the O2 inertia criterion alone. Let

    0 -> Pi -> X -> Pi^m -> 0

be an exact Banach sequence with dimension_E Hom_G(Pi,X)=1. We prove dimension_E Hom_K(V,X)<=2 directly.

Choose a nonzero j:V->Pi. Pullback along j defines a linear map

    alpha: Ext1_{G,zeta}(Pi,Pi) -> Ext1_{K,zeta}(V,Pi).

We only need the kernel interpretation: an extension class is in ker(alpha) exactly when j has a K-equivariant lift into that extension. Such a lift has image in X_alg because V is locally algebraic on K and K is open in G. The G-span of its image therefore consists of algebraic vectors. Its image in the quotient Pi contains j(V), so it equals Pi_alg by irreducibility of Pi_alg. The algebraic sequence is consequently exact. Exactness at its left and middle follows from the definition of algebraic vectors and the closed G-equivariant inclusion. Hence every class in ker(alpha) is a generator allowed in R(Pi), and

    dimension_E ker(alpha)<=dimension_E R(Pi)<=1.

We do not need the converse assertion R(Pi)=ker(alpha).

Apply Hom_G(Pi,-) to the displayed sequence. The map End_G(Pi)->Hom_G(Pi,X) is injective between one-dimensional spaces, hence is an isomorphism. The connecting map

    delta: Hom_G(Pi,Pi^m)=E^m -> Ext1_{G,zeta}(Pi,Pi)

is therefore injective. Applying Hom_K(V,-), and identifying Hom_K(V,Pi^m) with E^m using j, gives the connecting map beta=alpha composed with delta. Thus dimension ker(beta)<=dimension ker(alpha)<=1. The initial part of the Hom_K exact sequence has kernel Hom_K(V,Pi), of dimension one. It follows that

    dimension_E Hom_K(V,X)=1+dimension_E ker(beta)<=2.

This argument uses only the pullback splitting property of Yoneda Ext; it does not presume exactness of the functor of algebraic vectors, projectivity of V in the full Banach category, or flatness of a deformation module. If Hom_K(V,Pi)=0, the Hom_K exact sequence instead gives Hom_K(V,X)=0 immediately. Finite coefficient extension may be used to arrange the stated endomorphism equality.

## 5. Precise entry into the original type and cycle arguments

BM author4.14 requires a multiplicity-at-most-one theorem for the K-types, in addition to the inertia detection criterion. The O2 proof uses only detection and cannot silently replace that stronger multiplicity input. Retain Henniart as quoted in the actual BM proof. The nonsupercuspidal irreducible Banach cases use Colmez VI.6.50; the ordinary reducible cases use final Image12.5/12.6 and the stated completion arguments. The ordinary citation in BM4.14 to Image11.5 is corrected only at that occurrence, as in compiler002. BM4.20's separate Image11.5 citation is a correct Galois Hom input and remains.

BM4.16 gives irreducibility of Pi_alg away from finitely many points under its exact condition: either the residual representation is not the indicated extension with diagonal delta*omega,delta, or the weight gap is greater than one, or inertia is not scalar. The exceptional weight-gap-one scalar situation is not swept into this lemma. BM4.15 and its Fontaine–Laffaille argument treat that case separately. Irreducible Pi_alg is therefore an actual supplied hypothesis at the points where Sections3–4 are used, not an inference from irreducibility of the Banach representation.

BM4.21 supplies the exact first-order object X as the closure of algebraic vectors in Pi(R_n/n^2). The original proof uses its Galois Hom calculation4.20 and the faithful functor map to show Hom_G(Pi1,X) has dimension one, where Pi1 is the closed irreducible socle. It obtains the exact sequence 0->Pi1->X->Pi1^m->0. Retain that construction and its maps. Section4 then supplies the required bound2. No claim is made that arbitrary first-order cohomological base change preserves such a sequence.

The criterion BM2.42 consumes both the bound1 at the zero-order characteristic-zero closed points of its dense set and the bound2 at these first-order points, along with its projectivity, Cohen–Macaulay and mod-p hypotheses. BM6.5/6.6 identify the original annihilator quotient and the cycles. The sum is over all irreducible smooth mod5 K-representations occurring in the semisimplified reduction of the entire chosen type, with their original multiplicities. The auxiliary single Serre weight does not replace that sum.

For Hu–Tan M1, final4.2 applies BM6.5/6.6 to the original non-split residual extension with diagonal1,omega and its own envelope N1. For M2, final4.9 gives the almost-all zero-order type test on the original pseudodeformation fiber; final4.10 uses the same first-order criterion and explicitly verifies the remaining regular-sequence/Cohen–Macaulay input for N2. Its Remark4.8 says N2 is not flat over the pseudodeformation ring. The above Hom argument asserts no such flatness. Final5.11 combines those results with5.5 to give the full non-generic cycle formula. All pseudodeformation-to-versal/framed maps and multiplicities in those statements remain unchanged.

This gives the exact connecting path for the new O2 and RED inputs. The original general-type criterion, module constructions and cycle theorems are retained theorem imports, not newly approved proofs of every source ancestor. The needed source contracts and qualifications are enumerated separately. O4 owns the subsequent global modularity theorem applications; O5 owns the residual branch coverage for the original rational representation.

## 6. Source limits and current status

The new Sections3–4 await independent review. The earlier exactness-to-density sublemma has its own independent decision, which is preserved. The new broader nonordinary application is not covered merely by the older decision for the supercuspidal special-case exclusion.

The current BM pin remains arXiv1209.5205v3; final Duke164 (2015),297–359, DOI10.1215/00127094-2861604, has not been compared. The new official University of Duisburg-Essen publication-record check labels its fulltext open access but actually links arXiv, not a final Duke copy. The Dospinescu primary author links still return the44-page author text; its final37-page Compositio article has not been obtained. No publisher abstract or bibliography has been substituted for an exact theorem comparison.

There are therefore two different remaining tasks: independent review of these new connections, and resolution or honest retention of the specific source-version qualifications. A failure to retrieve a final PDF is not a mathematical counterexample. Acceptance of these lemmas would not by itself close the full BM/HT proof tree or authorize the current manuscript replacement.
