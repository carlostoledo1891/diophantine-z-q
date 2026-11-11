# Auxiliary classical-point transfer with explicit published inputs

Author: `/root/astra_v14_baseline_compiler`, 2026-11-08. This is an immutable author proposal for independent review. It preserves earlier packets001–003. It does not approve itself, the full Hu–Tan theorem, the complementary residual branches or the manuscript.

## 1. Statement and retained premises

Set p=5 and G=GL2(Q5), K=GL2(Z5). Let r be an absolutely irreducible two-dimensional representation over a finite extension E of Q5, potentially semistable with distinct CEGGPS body-convention weights u<v, where epsilon has weight -1. Assume its Weil–Deligne representation is absolutely irreducible. All irreducibility assertions about smooth or Weil–Deligne representations below are over an algebraic closure, with a sufficiently large finite coefficient field chosen for the finitely many objects used. Put

    W = Sym^(v-u-1) E^2 tensor det^(1-v).

Retain the accepted auxiliary construction and fixed-level lifting argument in `ceggps-route-001`, together with the independently accepted restricted local envelope/fiber result `ceggps-consolidated-003`. Retain CEGGPS Theorem7.4 at its stated minimal tame conductor and the selected published Colmez shape, nonvanishing and fixed-Weil–Deligne filtration comparison. These are exact imports, not theorems reproved here.

This packet supplies the remaining classical point/type/parameter connection using the final published Emerton2006 Theorems2.3.1,2.5.1,7.4.2 and the type criterion explicitly stated in final Hu–Tan2015 page1384. It proves the conditional conclusion

    B_C(r)^lalg is isomorphic to pi_p(r) tensor W,

where pi_p is Tate-normalized classical local Langlands. The same actual Banach representation, not merely its Galois functor image, is required. The only qualification in the word conditional is retention of the specified exact source theorems and previously reviewed constructions. There is no new residual hypothesis on r.

In particular, this connection no longer requires an unread direct statement from Saito1997 or an additional stronger minimal-type theorem. Saito and Henniart remain the published proof-source ancestors explicitly named by the final sources. We do not claim to have independently read Saito's final proof or authenticated the original Henniart appendix. This is a change of the directly consumed statement and an explicit connecting proof, not deletion of their transitive source roles.

## 2. What the final published classical theorem actually says

The final Emerton2006 PDF is SHA256 5b2042b8863162f06ba822c4e463bf4290163ad2b57baca05f5ecb71693243fb. Its Section2.1.2, printed page291, defines pi_p(V) from Fontaine's Frobenius-semisimplified Weil–Deligne representation when V is potentially semistable. Thus the symbol at p has a Galois definition; it is not defined to mean an unspecified automorphic factor.

Section2.3, printed pages292–293, considers cuspidal newforms of arbitrary conductor, explicitly including primes dividing Np, and states potential semistability at p for their Galois representations. Theorem2.3.1 asserts the adelic equality pi(f)=pi(V_f). It includes the p-factor. Section2.5 and Theorem2.5.1, printed pages294–295, identify the actual Galois multiplicity space in parabolic cohomology with V_f and give the equivariant decomposition with pi(V_f). The paragraph following that theorem names Carayol for the places away from p and Saito for p. The statement is therefore a precise published formulation of the needed p-place comparison, not a bare reference to Saito's title.

The conventions are explicit. Section1.3, pages285–286, sends a uniformizer by local reciprocity to geometric Frobenius and writes epsilon(x)=|x|x on Q5^times. Section2.1, page289, uses Tate-normalized local Langlands. Section7.4.1 defines E(n) with both the Galois epsilon^n action and the GL2(A_f) action through epsilon^n composed with determinant. Theorem7.4.2, page364, has the algebraic DUAL (Sym^(k-2)E^2)^dual. These displays were checked on the final page images as well as extracted text.

Nothing here invokes the conjectures in Emerton2006 Section3 or Section7.9, or the unpublished Emerton2011 supercuspidal identity. The directly consumed classical statements predate that input and state their full p-place conclusion.

## 3. A type criterion sufficient for this application

Let D be an irreducible two-dimensional Frobenius-semisimple Weil–Deligne representation with inertia tau. Its monodromy is zero: if a nonzero nilpotent monodromy existed, its one-dimensional kernel would be stable under inertia and Frobenius. Work after a finite coefficient extension that splits the finite inertia representation.

The restriction tau is not scalar. If it were scalar, inertia would act through one character and Frobenius would have an eigenline, contradicting irreducibility of D. Either tau is irreducible of dimension two, or tau is the sum of two distinct characters exchanged by Frobenius. Indeed the isotypic summands of the finite inertia representation are permuted by Frobenius, and irreducibility makes that permutation transitive.

Let sigma=sigma(tau) be the smooth irreducible K-type in final Hu–Tan page1384. That source states that, for every infinite-dimensional smooth absolutely irreducible pi, Hom_K(sigma,pi) is nonzero exactly when the inertia of its classical Weil–Deligne parameter is tau. Because tau is not scalar, sigma=sigma_cr(tau). No uniqueness up to unramified twist is being taken from an unread additional theorem.

A character of G cannot contain sigma. To justify the finite-dimensional exclusion needed to apply the criterion, suppose sigma were a K-character chi composed with determinant. Extend the smooth character chi of Z5^times to Q5^times. Twist an irreducible unramified principal series by that character. Its K-restriction contains sigma through its spherical vector, whereas its inertia parameter is scalar. The cited criterion would force tau to be scalar, a contradiction. Here the existence and spherical-vector characterization of the irreducible unramified principal series are the classical classification explicitly recalled in Emerton2006 Section2.1. Every one-dimensional smooth K-character factors through determinant; for K=GL2(Z5), this follows by elementary row operations, since SL2(Z5) is generated by elementary unipotents and these are commutators using a diagonal unit whose difference from1 is a unit. Thus sigma has dimension greater than one. Emerton2006 Section2.1.1 says the only finite-dimensional irreducible smooth G-representations are characters, so a smooth irreducible containing sigma is infinite-dimensional and the criterion applies.

Now let D' be any two-dimensional Frobenius-semisimple Weil–Deligne parameter with inertia tau. If tau is irreducible, an inertia-commuting nilpotent is scalar and hence zero. If tau is two distinct characters, it is diagonal on the two lines and again zero. Thus D' has zero monodromy. In the first case, identify its inertia action with that of D. The two Frobenius operators differ by an inertia-commuting scalar, by Schur's lemma. In the second case Frobenius must exchange the two character lines, since its permutation is fixed by conjugation on inertia. Write the two matrices as

    F = [[0,a],[b,0]],       F' = [[0,a'],[b',0]].

All four entries are nonzero. Choose c with c^2=a'b'/(ab), and put d=a'/(ca). Conjugating cF by diag(d,1) gives F'. This conjugation commutes with inertia. In either case D' is D tensored with an unramified character nu, after a finite coefficient extension. This proves both irreducibility of D' and the required full-parameter alignment from the stated type criterion.

The same argument handles Frobenius semisimplification precisely. In the irreducible-inertia case, some positive power of Frobenius centralizes inertia and is scalar. In the two-character case, its square is scalar. A matrix whose positive power is a nonzero scalar is semisimple in characteristic zero. Thus an irreducible parameter in these cases is already Frobenius semisimple; no Jordan information is lost in the comparison.

## 4. The actual auxiliary eigenpoint and its Tate twist

Apply the already reviewed fixed-conductor construction to a constituent of a stable lattice in sigma tensor W. It produces the same auxiliary odd residual representation induced from Q(sqrt(-2)), locally absolutely irreducible at5, with only2 and193 in its possible tame ramification and with no vexing primes. Let N be its actual prime-to-5 conductor. Nothing in this proof changes N. The accepted type-lifting argument gives a nonzero K-map from sigma tensor W into completed cohomology at Gamma_1(N), localized at that residual representation.

The finite-dimensionality and Hecke eigenvector step are those already reviewed at this exact fixed level. Theorem7.4.2 expresses the locally algebraic part using classical cohomology. Since

    (Sym^(k-2)E^2)^dual tensor det^n
       = Sym^(k-2)E^2 tensor det^(n-k+2),

the prescribed algebraic factor forces, uniquely,

    k=v-u+1,       n=-u.

The uniqueness may be checked on an open subgroup of K on which sigma is trivial: irreducible algebraic highest weights are determined on that Zariski-dense subgroup. Thus the eigenvector lies in the k,n summand, not an unrelated weight. Non-Eisenstein localization removes the boundary part, exactly as in the accepted fixed-level proof. A nonzero coordinate in the parabolic decomposition therefore supplies a cuspidal newform f. Enlarge E finitely to contain its coefficients and the chosen eigenvalue.

Let x be the resulting point of the global deformation ring. The actual Galois factor of its classical coordinate is

    V_f tensor epsilon^n.

This is the same global representation as rho_x. Both have the same away-from-Np Hecke trace and determinant: CEGGPS Section7 uses geometric Frobenius, and Emerton2006 Definition7.3.2 writes the inverse of its arithmetic Frobenius, which is the same convention. The diagonal action on E(n) changes T_l and S_l by the corresponding first and second character powers. Chebotarev and Brauer–Nesbitt, in the precise form recalled in Emerton2006 Remark7.3.3, identify their semisimplifications. The auxiliary residual representation is absolutely irreducible, so each lift is absolutely irreducible; their semisimplifications are the representations themselves. There is no choice of an unrelated Galois representation with the same type.

At primes away from5 the Tate twist is unramified and is trivial on the unit determinants in the fixed tame compact subgroup. The cuspform has tame level dividing N, while its reduction has conductor N. Equivalently one may invoke the exact no-vexing minimality statement in CEGGPS Remark7.1. Thus the point lies in the actual minimally ramified global deformation problem used by Theorem7.4. It does not require a nonminimal-level version of that theorem.

The GL2(Q5) factor of the same classical coordinate is

    pi_p(V_f) tensor (|.|^n composed with determinant) tensor W.

Indeed epsilon(x)^n=|x|^n x^n: the algebraic x^n factor has already entered det^n, and the smooth |x|^n factor must be retained. This is exactly pi_p(V_f tensor epsilon^n) tensor W. In Fontaine's rank-one calculation, t^(-1) is a basis for the crystalline period of epsilon, and phi(t)=5t, so geometric Frobenius on its Weil parameter is5^(-1). Consequently WD(epsilon) is the unramified character |.|, in these conventions. Tate-normalized local Langlands commutes with character twists. This verifies the smooth factor, not just the algebraic highest weight.

By the published classical theorem, r_x=rho_x|G_Q5 is potentially semistable and its smooth factor has the Fontaine parameter of r_x. The original K-map supplies sigma in that smooth factor. Explicitly, restrict to a sufficiently small open subgroup on which the smooth source type is trivial, use the irreducibility of W on that Zariski-dense subgroup, and apply the algebraic Schur lemma to remove the common W tensor factor. This is the same algebraic/smooth separation as BM Lemma4.10; a nonzero type map cannot disappear when the common algebraic factor is removed. Section3 now shows that its parameter is irreducible, has zero monodromy and is an unramified twist of D=WD(r). Thus r_x is potentially crystalline. Its weights are u,v. One may read them from the k,n classical factor, or from the selected Colmez weight-extraction theorem applied to the actual Banach fiber with algebraic factor W. This second check uses no assumed residual property of r.

## 5. The same Banach fiber and multiplicity

Theorem7.4 identifies completed homology with the same projective envelope tensored over R_p with the dual of the global universal representation. The accepted consolidated003 result identifies the continuous-dual local fiber with the actual B_C(r_x). Specializing the homology at x and taking the continuous coefficient-field dual gives the cohomology eigenspace with factor B_C(r_x) tensor rho_x. This is the annihilator of the specialization ideal, not an assertion of exact arbitrary cohomological base change.

Taking locally algebraic vectors commutes with the finite-dimensional global Galois factor, on which G acts trivially. The classical decomposition from Section4 therefore places B_C(r_x)^lalg into a finite direct sum of copies of pi_p(r_x) tensor W, after choosing coordinates on the finite global/multiplicity factors. The sum is finite because the K-type is trivial on a fixed sufficiently small open subgroup at5 and the tame level and algebraic weight are fixed.

The selected Colmez nonvanishing theorem gives B_C(r_x)^lalg nonzero. His shape theorem says it is irreducible or the indicated special-series extension. The latter has a nonzero special-series constituent and cannot inject into a sum of supercuspidal representations with the same algebraic factor. Removing the algebraic tensor factor reduces this assertion to distinct irreducible smooth constituents. Hence the first alternative holds. A nonzero coordinate projection is then an isomorphism

    B_C(r_x)^lalg = pi_p(r_x) tensor W.

No multiplicity-one assertion at the tame level, and no chosen tame newvector, is needed.

## 6. Unitarity and transfer to the target

Section3 gives WD(r_x)=WD(r) tensor nu for an unramified character nu. Its value c on geometric Frobenius is a unit. A direct reason, avoiding a possible confusion between a Galois determinant and its Weil parameter, is admissibility of the filtered module attached to an actual potentially crystalline representation. Colmez Section VI.6.9, printed page460, explicitly uses t_N(M)=v_p(det(phi)) and the forced equality with the sum of filtration weights. This is the necessary admissibility direction already present in his fixed-module setup; no converse construction of a representation is needed here. Choose a finite extension over which both representations are crystalline. Their weights u,v give equal total Hodge numbers. Twisting the common Weil parameter by nu changes the total Newton number by a nonzero fixed multiple of 2*v_5(c). Equality of Newton and Hodge numbers for the two representations forces v_5(c)=0. In particular, we have not inferred that the Weil parameter of an arbitrary unitary Galois character is itself unitary; epsilon would contradict that shortcut.

The unramified character nu therefore extends continuously to G_Q5. After tensoring r_x by nu^(-1), it and r have the same Weil–Deligne module and the same weights. Twist both representations by the same integral power of epsilon to normalize one weight to zero, as in the setup of Colmez VI.6.9, and undo that common twist at the end. The selected published Colmez VI.6.42 filtration-independence statement applies to these exact objects. This uses VI.6.42 itself, not the modularity-dependent conclusion in Remark VI.6.51(ii). Compatibility with the unitary character twist then gives

    B_C(r)^lalg = pi_p(r) tensor W.

This completes the remaining auxiliary-point/type/parameter connection relative to the listed source statements. In Paškūnas/Hu–Tan notation V=r tensor epsilon, so the existing002 conversion gives Sym^(h2-h1-1)det^h1 and central character psi. The argument imposes no auxiliary residual property on the target V.

## 7. Status of the former O2 obligations

The quadratic auxiliary construction, all twenty Serre weights, no-vexing condition, actual conductor and the fixed-level cohomological lift retain their previous exact independent review. Consolidated003 supplies the newly reviewed local envelope/fiber. CEGGPS7.4 remains an exact theorem import, with its final-edition qualification. Its proof-source edges to minimal deformation and Galois factorization remain recorded. The author's earlier CHT specialization is not needed as a new premise when7.4 itself is imported; this does not relabel it independently accepted.

For the classical p-place, the directly consumed statement is now the final published Emerton2006 Theorem2.3.1 and cohomological Theorem2.5.1, with their explicit definitions. Saito1997 remains a transitive proof-source ancestor, not an unread statement silently assumed equivalent. For the type criterion, the directly consumed published statement is final Hu–Tan page1384; the stronger unramified-class conclusion has been proved in Section3. Henniart's original proof remains a transitive ancestor.

The new connections in Sections3–6 require independent review of this exact packet. Once accepted, no missing mathematical connection in this bounded O2 transfer is being left behind as an unspecified template transport. This does not claim independent validation of every transitive published proof or remove retained edition qualifications. Full general-type BM/HT, the separately reviewed RED bridge and its source qualification, corrected Kisin/Gee–Kisin/KW/Serre, remaining residual branches and actual manuscript adoption are outside this bounded conclusion.
