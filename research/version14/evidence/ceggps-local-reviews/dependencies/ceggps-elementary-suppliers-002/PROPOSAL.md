# Two proposed elementary supplier replacements

This is a new author proposal by `/root/astra_v14_source_review`, not an independent acceptance. It supplements `ceggps-source-closure-003` without altering that packet. Its intended consumers are the two explicitly open steps in Sections 4 and 6 of that report: the fixed-central-character smooth principal-series self-extension dimension and the integral lifting of a finite projective module. The Breuil–Paskunas injective-enlargement construction is not replaced here. Neither are the other remaining crystalline, patching, or source-version obligations.

## 1. Smooth principal-series self-extensions

Let F=Q5 and let E be a finite extension of Q5, enlarged to contain a square root of 5 if necessary. Smooth representations here have E-vector spaces with the discrete topology for the group action. Put G=GL2(F), let B=TN be the upper triangular Borel, and put delta(diag(a,d))=|a/d|_5. Fix a smooth character zeta of the center Z. All categories and extensions below have exactly this central character; the center acts as the scalar zeta on the middle term as well as its endpoints.

Let chi=chi1 tensor chi2 be a smooth character of T restricting to zeta on Z. Let I(chi) be normalized induction, realized by locally constant functions f on G satisfying f(bg)=delta(b)^(1/2) chi(b) f(g), with G acting by right translation. Write r(V)=delta^(-1/2) V_N for normalized Jacquet coinvariants. Assume chi differs from w chi, where w interchanges the two diagonal entries. We claim

    dim_E Ext^1_(G,zeta)(I(chi), I(chi)) = 1.

The Ext group is in the full smooth fixed-central-character category. In particular it computes the smooth extension space needed by the principal-series paragraph of Paškūnas BM Theorem 4.19 whenever its irreducible principal series has distinct inducing characters. No supercuspidal statement is used.

First, r is exact. The additive group N is the increasing union of compact open subgroups. Coinvariants by each compact subgroup are exact over E, since averaging on the finite quotient fixing a given vector splits invariants and coinvariants. Taking the filtered colimit proves exactness for N. The modulus twist preserves exactness and the central character.

Normalized induction is exact. For a surjection of smooth B-modules, a locally constant induced function has values in finitely many local trivializations of the compact space B\G. Refining to a finite partition by compact open subsets and lifting their values gives a smooth induced lift. Injections are pointwise injections. Evaluation at the identity gives the usual adjunction

    Hom_G(V,I(W)) = Hom_T(r(V),W).

This statement includes non-character smooth T-modules W with central character zeta. Since r is exact, its right adjoint I sends injectives to injectives. The smooth fixed-central-character categories have enough injectives: smooth coinduction from the prescribed one-dimensional Z-action is the right adjoint of the exact forgetful functor to E-vector spaces and supplies an embedding into an injective. Apply I to an injective resolution of W; exactness of I makes it an injective resolution of I(W). Therefore

    Ext^1_(G,zeta)(V,I(W)) = Ext^1_(T,zeta)(r(V),W).

For completeness, the rank-two Jacquet calculation is explicit. Restrict I(chi) to B on the right. Bruhat decomposition has the closed cell B and the open cell BwN. Evaluation on the closed cell gives one quotient; its kernel is C_c^infinity(F,E) on the open cell. On this kernel the right N-action is translation. Integration against an E-valued Haar measure identifies its N-coinvariants with E. Indeed, a compactly supported locally constant function is a finite sum of indicators of cosets of a common compact open additive subgroup. A zero-integral sum is a sum of differences of such indicators, and each difference is a translation difference.

The closed-cell quotient gives chi after normalizing r. On the open cell, right multiplication by t=diag(a,d) sends w n(x) t to diag(d,a) w n(xd/a). Its multiplier before integration is |d/a|_5^(1/2) (w chi)(t); the change of variable in the integral contributes |a/d|_5. The subsequent factor delta(t)^(-1/2) cancels the remaining modulus. Thus the open-cell coinvariant is w chi. Exactness of N-coinvariants gives an extension with constituents chi and w chi. It splits when these characters differ: an element of the abelian group T on which their values differ has distinct eigenvalues, and its two eigenspaces are T-stable. Consequently

    r(I(chi)) = chi direct-sum w chi.

The same central-element argument splits every extension between these two distinct characters. It remains to compute Ext^1_(T,zeta)(chi,chi). Twist by chi^(-1). The center then acts trivially, so this becomes Ext^1 of the trivial character of T/Z=F^times by itself. A two-dimensional extension has matrices (1 c(t); 0 1), where c is a locally constant additive homomorphism F^times to E. Changing the lift of the quotient does not change c. Compactness of O_F^times makes its image under c finite, hence zero in the characteristic-zero additive group. Therefore c factors through the valuation F^times to Z, and is uniquely determined by c(5). This extension space is E. The asserted dimension follows.

An extension of two admissible smooth representations is admissible, since invariants under a compact open subgroup are exact in characteristic zero. Thus computing in the full category has not enlarged the extension set relevant to admissible principal-series objects. If the coefficient field is extended finitely, the calculation and its dimension persist directly over that extension.

The generic crystalline points selected in Section 4 of `ceggps-source-closure-003` exclude coincident Frobenius roots and the two reducibility ratios. In the normalized unramified principal-series parameter their two inducing characters are distinct; their common normalization factor does not change equality of the two characters. The selected points also have irreducible smooth principal series. The calculation above therefore replaces exactly the invocation of the Schneider–Stuhler resolution for dimension one in BM 4.19. BM 4.11's passage from smooth representations to the algebraic tensor factor remains its own stated input. The universal-completion and first-order Galois arguments remain separate inputs. No assertion is made at coincident-character or reducible principal-series points.

## 2. Integral projective lifting

Let O be the coefficient discrete valuation ring with uniformizer pi. Let R be the compact completed group algebra with the prescribed continuous integral central character, namely the quotient of O[[K]] by the closed ideal generated by z-zeta(z) for z in the central compact subgroup. We use compact profinite R-modules and continuous maps. R and its matrix rings are pi-adically complete. Let M be such a module, O-torsion-free, and suppose M/pi M is a finite projective R/pi R-module. Then M is a finite projective R-module, and any given projective-cover map M/pi M onto a finite semisimple module lifts to a projective-cover map from M.

Here are the details needed in BM 5.2. Express M/pi M as the image of an idempotent e0 in a finite matrix ring over R/pi R. Idempotents lift to R: starting from any lift e, replace it successively by

    e + (1-2e)(e^2-e).

The new idempotency error lies in the square of the previous error ideal. These expressions are polynomials in e, so their calculation is valid in the noncommutative matrix ring. Pi-adic convergence gives an idempotent lifting e0. Let P be its image in the corresponding finite free module. Thus P is finite projective and P/pi P is the specified reduction of M.

Projectivity lifts the chosen reduction isomorphism to a continuous map P to M. Its cokernel C is compact and C/pi C=0, so compact Nakayama gives C=0. This version of Nakayama follows directly by mapping to every finite continuous O-quotient: a finite pi-primary module cannot satisfy C=pi C unless it is zero. O-torsion-freeness of M gives Tor_1^O(M,O/pi)=0. Reducing the kernel sequence therefore shows that the compact kernel L satisfies L/pi L=0. The same argument gives L=0. Hence P is isomorphic to M. This also proves finite generation; it need not be assumed separately for M.

If the reduction map is a projective cover, compose M to M/pi M with that map. For a closed submodule L of M whose image is the entire finite semisimple target, the projective-cover property modulo pi implies L+pi M=M. The compact quotient M/L satisfies (M/L)/pi=0 and is zero by the same argument. This is the essential-epimorphism property, so M is the projective cover of the target in the compact category. All maps respect the fixed central character because the calculation takes place over R.

In BM Theorem 5.2, M is Coker(x). The displayed snake-lemma argument there proves O-torsion-freeness; its reduction is the dual of the K-injective envelope, hence the projective envelope of the finite K-socle dual. The argument above gives precisely the concluding integral-projective-envelope inference attributed to Paškūnas 2010 Proposition 4.6. It does not establish the prior existence of that K-injective envelope, the endomorphism x, or the exact sequence producing it. Those remain separate dependencies.

## 3. Source status, authorship and intended review

The immediate consumer is the already pinned author version of Paškūnas BM, especially author pp26 and29. Its final Duke edition remains unverified. The new arguments above are proposed replacements for two of its supplier invocations, not claims that final publication comparison has occurred.

For comparison, the retrieved Paškūnas completion author PDF has arXiv identifier 0805.1006v1 and a regenerated title-page date of October 30, 2018. It has 44 pages; its Lemma 3.6 and Proposition 4.6 occur on author pp10 and14–15. It is not represented as the final 31-page Representation Theory article. The AMS final-PDF endpoints returned HTTP403.

The retrieved Schneider–Stuhler file from the author's publications page has 17 author-numbered pages, rather than the final journal pages19–32. It is not represented as a final scan. The first theorem definitions use complex smooth representations; the new calculation above works directly over E and explicitly fixes the central character.

Breuil–Paškūnas Corollary 9.11 was read in the author-hosted text, author p59 with its proof through Theorem9.8. Its hypothesis that the scalar uniformizer act trivially can be achieved by an unramified determinant twist after a finite coefficient extension; one chooses a square root of the inverse scalar. Twisting back preserves the K-envelope because the twist is trivial on K. The p=2 property(S) condition does not arise at p=5. This observation does not certify all of the diagram-gluing construction or identify the author PDF with the final Memoirs edition. That supplier remains open.

All these comparisons were made after the earlier source inventories and the restricted C10 review. This is a disclosed follow-on author phase, not a new blind reconstruction. The two new proofs require independent review. They do not change any earlier source bytes, acceptance, manuscript, or release artifact.
