# Restricted CEGGPS envelope and arithmetic action

Project proof supplement, version 1. This file records the restricted local envelope and arithmetic-action argument on the selected source inputs in RETAINED-INPUTS.json. Its intended auxiliary object is constructed in auxiliary-route-v1.md. Publication-version qualifications are explicit in SOURCE-QUALIFICATIONS.md. This is a local mathematical assertion; the separate global and arbitrary-target applications retain their stated hypotheses.

## Statement and scope

Let k be a sufficiently large finite field of characteristic five and let O be the ring of integers in a finite extension E of Q5 with residue field k. Let rbar be the absolutely irreducible two-dimensional local representation constructed at five in the auxiliary quadratic-induction argument. Enlarging the finite coefficient field is allowed. Write G=GL2(Q5), K=GL2(Z5), R_p for the universal unframed deformation ring in the CEGGPS convention, and pi for its associated supersingular smooth representation. Let Ptilde^psi be the fixed-central-character projective envelope used by Paškūnas, and let 1_univ be the universal character used in CEGGPS Section 6. With the selected source statements recorded in `RETAINED-INPUTS.json`, the following argument proves that

    Ptilde = Ptilde^psi completed-tensor_O 1_univ

has its indicated R_p action, is the projective envelope of pi^vee in the category without fixed central character, and satisfies the four body-version arithmetic-action axioms with d=0. This is the same envelope and action used by CEGGPS Theorems 6.18 and 7.4.

For each characteristic-zero point x with residue field E_x finite over E, its continuous dual fiber B_x is the actual Colmez Banach representation B_C(r_x), with the single convention change V_P=r_x tensor epsilon. The assertion includes topological and group-equivariant identification. Equality of the images under a Galois functor alone is not the conclusion.

Here are the four axioms in the conventions actually used. For a K-stable lattice sigma^o in sigma=det^a tensor Sym^b E^2, b>=0, put M(sigma^o)=Hom_cont,O[[K]](Ptilde,(sigma^o)^d)^d, where d denotes the O-linear continuous dual. The Hodge–Tate weight of epsilon is -1.

* AA1: Ptilde is finite over R_p[[K]].
* AA2: Ptilde is projective in the pseudocompact O[[K]] category.
* AA3: the action on M(sigma^o) factors through the crystalline quotient R_p(sigma) for weights (-a-b,1-a); the module is maximal Cohen–Macaulay, and its generic fiber is locally free of rank one on its support. In this construction the support is the full nonempty crystalline generic fiber. If the type is incompatible and the quotient is zero, the module is zero.
* AA4: the natural H(sigma) action on M(sigma^o)[1/5] equals the map eta to R_p(sigma)[1/5]. This is the body formulation in CEGGPS Section 3.1. It avoids importing the different introductory determinant exponent.

Under the separately selected CEGGPS uniqueness theorem, the same fiber identification holds for a module with arithmetic action over R_p[[x_1,...,x_d]] after specialization to its underlying R_p point. The auxiliary modular-curve theorem is a separate external input. No assertion here proves the general-type Breuil–Mézard theorem for the original representation, all Hu–Tan M1/M2 inputs, residual modularity, Pan, or the manuscript's final modularity claim.



## 1. Conventions and irreducibility

Throughout this proof p=5, K=GL2(Z5), and the residual local representation is the absolutely irreducible representation constructed in Section 3 of the explicitly retained auxiliary-route-v1.md. This is an auxiliary representation, not a strengthened hypothesis on the manuscript's original r5. Finite coefficient extensions are permitted and do not change these assertions.

Every characteristic-zero lift of this residual representation is absolutely irreducible. Indeed, an invariant line after a finite coefficient extension intersects a stable lattice in a saturated rank-one sublattice. Its reduction is a nonzero proper invariant line in the scalar-extended residual representation, a contradiction. Thus the reducible characteristic-zero cases in Paškūnas BM Proposition 4.9(ii) and the reducible residual blocks in *Image* Sections 8 and 10 are outside the present construction.

Let psi be the Banach central character. Write V_P for the Galois representation in Paškūnas's convention, and r_C for CEGGPS's representation. Then

    V_P = r_C tensor epsilon,
    det(V_P) = psi epsilon,
    det(r_C) = psi epsilon^(-1).

CEGGPS explicitly introduces the additional inverse-cyclotomic twist after Theorem 6.18. The same Banach space is used under these two Galois labels. The check-V operation on the compact dual also involves the dual and determinant twist described in *Image* Section 5.7; its two-dimensional identification with V_P uses V_P^*(det V_P)=V_P. One must not apply the extra epsilon twist twice.

For a pure algebraic representation sigma=Sym^B E^2 tensor det^A, with B>=0, the CEGGPS body convention gives weights (1-A,-A-B). In increasing order these are u=-A-B and v=1-A. Hence A=1-v and B=v-u-1. This is the body convention already fixed in the predecessor, not the conflicting introductory formula. The required crystalline type has trivial smooth inertial type. A fixed central-character mismatch makes the corresponding module zero; CEGGPS 6.12–6.14 treats this case explicitly. Otherwise a character delta trivial modulo the maximal ideal adjusts psi to psi delta^2, and the remaining universal character is unramified on the type module. The square-root adjustment is legitimate at p=5.

## 2. The exact Banach fiber

The citation to Kisin `[41, 2.3.8]` in *Image* Proposition 6.2 has old numbering. The published Astérisque 330 article has the relevant conclusion as Corollary 2.11, with the stronger lattice construction in Proposition 2.8 and Corollaries 2.9–2.10. The published proof, rather than the bare statement of 2.11, is needed here.

In the irreducible residual case, Kisin's deformation problem starts with the supersingular mod-5 representation pi. Proposition 2.8 constructs an admissible Banach lattice with this exact reduction at the twisted-benign points. The proof uses local crystalline or trianguline constructions, the compatibility of their reductions, and Lemma 2.7 to obtain the prescribed lattice. Corollaries 1.12–1.13 supply fixed-determinant density, and 2.9 extends the deformation construction to the whole fixed-determinant space. Corollary 2.10 then gives the lattice for each lift. The residual exclusion in these statements is automatic for our absolutely irreducible residual representation; the additional p=3 exclusion does not occur.

For a general unitary psi, Kisin 2.8 first changes it by a square of a character trivial modulo 5 so that its inertia restriction is an integral cyclotomic power. Density is used after that change, and twisting returns to the original psi. The argument does not assume the original character is locally algebraic. The final printed central character is det(V_P) epsilon^(-1); the superscript minus sign is lost in some text extraction and was checked on the page image.

The exact mod-5 reduction matters. A complete invariant lattice Theta with Theta/pi Theta=pi absolutely irreducible gives an absolutely topologically irreducible Banach representation. For a nonzero closed invariant subspace W, scale a nonzero vector to obtain a primitive element of W intersect Theta. The image of this intersection in pi is nonzero, hence all of pi. Successive approximation lifts every element of Theta modulo pi^n into W intersect Theta. Closedness and completeness give W intersect Theta=Theta, hence W is the whole Banach space. The same argument applies after finite coefficient extension. This verifies the multiplicity-one residual-lattice requirement in *Image* 5.56(iii), not merely the existence of a Banach object with the right Galois image.

The remaining inputs of *Image* 5.56 in this block are explicit. Colmez VII.5.2, restricted to the irreducible supersingular atom, gives injectivity on Ext1. Its proof uses VII.1.2(iv), VII.1.10 and VII.2.1 to pass from a split Galois extension to a split Borel extension and then a split GL2 extension. This is a mod-p argument. It does not use the characteristic-zero supercuspidal locally algebraic identity. Paškūnas's published supersingular-extension Theorems 10.7 and 10.13 give the isolated block and Ext1 dimension three; 10.14 and *Image* 6.23 handle the additional relation calculation, including the Iwahori Serre weights. We do not discard r=0 or r=p-1: the auxiliary construction may produce those weights.

Thus *Image* 6.2 gives the surjection to the fixed-determinant deformation ring, and 6.3 identifies the endomorphism ring and universal Galois deformation. Its proof uses the noncommutative algebra criteria 3.39, 3.41 and 3.43 and the preceding Ext computations. It does not invoke the later Theorem 12.7.

The actual Banach fiber is identified by *Image* Corollary 6.8 and Theorem 4.36, not by equality of Colmez images alone. The finite-length Banach category in the supersingular block at a maximal ideal n is anti-equivalent to finite-length modules over the n-adic completion of the fixed-determinant deformation ring. It has one irreducible object. The specialization of the projective generator at the residue field is that object. Lemma 5.53 makes its Galois representation the specialization of the universal representation. The preceding Kisin lattice is in this exact block, with this exact point, so is isomorphic to this irreducible fiber.

One further endpoint is needed before applying Colmez's theorems on locally algebraic vectors: this fiber must be his actual constructed Pi(D), not just an unspecified Banach representation with the same V-image. The direct reconstruction gives it. Set B=Theta[1/5] for the Kisin lattice and D'=D(B). The beta_P1 target has central character delta=psi^(-1), as specified in IV.3.2; thus it is D' boxtimes_(psi^(-1)) P1. Each Theta/pi^n has a filtration with all factors equal to the supersingular pi, and therefore has no finite subrepresentation or quotient. Colmez IV.3.2(iii) says that beta_Qp maps its dual onto D'^natural boxtimes Qp; IV.4.7 gives the compatible G-equivariant beta_P1 and its kernel, which is the SL2-invariant part of the dual and is zero here. Use the integral and Banach extensions explicitly stated in IV.3.3 and IV.4.9. At the integral step these are the compatible O/pi^n-valued duals with coefficient reduction, giving the Schikhof dual. They are not an inverse system formed by dualizing quotient maps into a fixed torsion target. Compactness gives the compatible lifts, and inverting 5 gives the stated Banach-dual map.

Since D' is irreducible of rank two, I.3.11 makes the bounded natural and sharp Qp-modules equal after inverting 5. The kernel of Res_Qp on D' boxtimes P1 is (0,D'^nr), by II.1.14(iv), and D'^nr=0 in this irreducible case. Thus the image of beta_P1 is exactly D'^natural boxtimes P1: its projection is the whole bounded natural Qp-module after inverting 5, and projection is injective on the ambient space in question. The compact integral maps and their bounded scalar extensions give the topological identification, not merely an abstract vector-space bijection.

By the definition of the contravariant D functor preceding IV.2.14,

    D'=D(V_P^*(epsilon))=D(V_P) tensor psi^(-1).

The pairing of II.2.11–12 and the rank-two construction II.3.1 therefore identify this beta image with the continuous dual of Colmez's Pi(D(V_P)). Taking duals identifies B with that actual representation. This supplies the endpoint without importing the broad *Image* 11.1 classification of other residual blocks. Corollary IV.4.11 by itself would only give D(Pi(D))=D and is insufficient. Universal character twisting now gives the CEGGPS fiber for r_C.

Accordingly the intended C07 chain is CEGGPS 6.18 plus its projective-generator comparison, *Image* 6.3/6.8 and 5.53, followed by CEGGPS 6.19's Galois calculation. Corollary 6.19 by itself supplies only nonvanishing and the Galois image. *Image* 12.7 is deliberately excluded: its proof invokes the supercuspidal identification under investigation.

## 3. The fixed-center injective enlargement

The next construction supplies the enlargement used in BM Theorem 5.2, conditional on the selected BP Section 9 symmetry and tree-gluing statements. The argument works over a finite residual field and proves the needed admissibility.

Permit a finite extension of the residual coefficient field k at the outset. Choose c in that extension with c^2=zeta(5)^(-1). The unramified character mu of Q5^times with mu(5)=c is trivial on Z5^times. Replace pi by pi tensor (mu composed with determinant). The scalar matrix 5 acts on this representation by zeta(5)mu(25)=1. Its restriction to K is unchanged. The extra property(S) assumption in BP Corollary9.11 occurs only at p=2, so it is absent here.

Apply the diagram construction to this twisted representation, provisionally granting the source statement over the chosen coefficient field as addressed below. It gives an embedding into a smooth G-representation Omega0 whose restriction to K is the full injective envelope of the K-socle. It does not yet give the prescribed action of every central unit.

Let zeta' be the twisted central character, and define Omega1 to consist of the vectors v in Omega0 satisfying z v=zeta'(z)v for every z in Z. This is G-stable because Z is central, and it contains the twisted pi. Since scalar 5 already acts trivially, the only additional conditions are those on Z intersect K.

The inclusion from the smooth fixed-zeta' K-category into the full smooth K-category is exact. Its right adjoint is the zeta'-eigensubspace functor. A right adjoint to an exact functor takes injective objects to injective objects: the adjunction identifies Hom into the eigensubspace with Hom into the original injective object after the exact inclusion. Thus Omega1 restricted to K is injective in the required fixed-center category. The socle inclusion remains essential. Every nonzero K-submodule of Omega1 is also a submodule of the full injective envelope and intersects its socle nontrivially. Hence Omega1 restricted to K is the fixed-center injective envelope of that same finite socle.

Untwisting by mu composed with determinant restores the original zeta. It preserves all assertions and is trivial on K. This supplies the exact central-character form required by BM, rather than assuming that the full K-envelope already had scalar central action.

The K-envelope of a finite semisimple socle is admissible. To see the required finite-dimensional invariant spaces directly, let H be an open subgroup of K. The smooth representation Ind_H^K(1) is finite dimensional, hence of finite length. For an injective envelope I of a finite semisimple socle, Hom_K(S,I) is finite dimensional for each irreducible S: every simple submodule lies in that socle. Exactness of Hom_K(-,I), and induction on the finite length of Ind_H^K(1), gives finite-dimensional Hom_K(Ind_H^K(1),I)=I^H. This also works in the fixed-center category by starting with the full envelope and then taking its subspace. Thus Omega1 is admissible for G.

Every nonzero G-subrepresentation of Omega1 is a nonzero K-subrepresentation and intersects soc_K(pi), hence intersects pi. Irreducibility of pi forces it to contain pi. Consequently soc_G(Omega1)=pi. These are the two additional properties used in BM5.2 before its homological construction of x.

The displayed BP source convention uses an algebraic closure of the residual field. One must not obtain a finite-field admissible envelope by merely restricting scalars from that algebraic closure. Instead the construction of Section9 can be performed over the chosen finite field k in this Q5 case, after the finite scalar extension at the start of this section.

Here are the actual points to check. The tame diagonal group H in BP9.1 has characters valued in F5^times, so it is split over k. The irreducible representations of GL2(F5) occurring in the K-socle are the determinant twists of Sym^r(k^2), 0<=r<=4; they are absolutely irreducible over k. Thus all the finite socle constituents used here are already split.

Injective envelopes and the needed direct-summand decompositions exist in the smooth k-category. Their formation for these finite socles commutes with extending k to its algebraic closure. One can check the latter using the injective cogenerator C(K,k): continuous functions on compact K have finite image, so C(K,k) tensor kbar equals C(K,kbar). Decompose this injective object by its absolutely irreducible socle constituents and use uniqueness of injective envelopes. This is also the argument of Paškūnas's completion paper, author Lemma3.8 on p10.

BP9.2 uses only that the finite group generated by H and the edge reflection has order 2(5-1)^2, invertible in k. Its averaging argument therefore works over k. In BP9.5 the induced injective envelope and its extension of the edge-stabilizer action are constructed over k. The remaining dimension equality in BP9.6, between the chi and reflected-chi invariant spaces in the K-injective envelope, descends from the source equality over kbar by the preceding base-change compatibility. These invariant spaces are finite dimensional by admissibility. The isomorphisms between equal-dimensional spaces, their inverses, and the identity on fixed-character spaces can all be chosen over k. No infinite coefficient extension is required for these choices.

The resulting two compatible stabilizer actions are glued by the same tree/diagram construction used in BP9.8. BP9.9 then checks injectivity on the vertex component, and Corollary9.11 gives the desired embedding. The source's finite-group symmetry equalities and its tree-gluing results remain explicit source inputs; this paragraph checks their coefficient-field use, not their entire proofs.

## 4. The integral projective cover

Let O be the coefficient discrete valuation ring with uniformizer pi. Write eta for the prescribed continuous central character on compact modules. Let R be the quotient of O[[K]] by the closed ideal generated by z-eta(z) for z in the central compact subgroup. In the BM application, eta=zeta_BM^(-1), because C(O) consists of Pontryagin duals of smooth representations with central character zeta_BM. This compact character is distinct from the smooth-side zeta notation in Section 6. We use compact profinite R-modules and continuous maps. R and its matrix rings are pi-adically complete. Let M be such a module, O-torsion-free, and suppose M/pi M is a finite projective R/pi R-module. Then M is a finite projective R-module, and any given projective-cover map M/pi M onto a finite semisimple module lifts to a projective-cover map from M.

Here are the details needed in BM 5.2. Express M/pi M as the image of an idempotent e0 in a finite matrix ring over R/pi R. Idempotents lift to R: starting from any lift e, replace it successively by

    e + (1-2e)(e^2-e).

The new idempotency error lies in the square of the previous error ideal. These expressions are polynomials in e, so their calculation is valid in the noncommutative matrix ring. Pi-adic convergence gives an idempotent lifting e0. Let P be its image in the corresponding finite free module. Thus P is finite projective and P/pi P is the specified reduction of M.

Projectivity lifts the chosen reduction isomorphism to a continuous map P to M. Its cokernel C is compact and C/pi C=0, so compact Nakayama gives C=0. This version of Nakayama follows directly by mapping to every finite continuous O-quotient: a finite pi-primary module cannot satisfy C=pi C unless it is zero. O-torsion-freeness of M gives Tor_1^O(M,O/pi)=0. Reducing the kernel sequence therefore shows that the compact kernel L satisfies L/pi L=0. The same argument gives L=0. Hence P is isomorphic to M. This also proves finite generation; it need not be assumed separately for M.

If the reduction map is a projective cover, compose M to M/pi M with that map. For a closed submodule L of M whose image is the entire finite semisimple target, the projective-cover property modulo pi implies L+pi M=M. The compact quotient M/L satisfies (M/L)/pi=0 and is zero by the same argument. This is the essential-epimorphism property, so M is the projective cover of the target in the compact category. All maps respect the fixed central character because the calculation takes place over R.

In BM Theorem 5.2, M is Coker(x). The displayed snake-lemma argument there proves O-torsion-freeness; its reduction is the dual of the K-injective envelope, hence the projective envelope of the finite K-socle dual. This reduction is finite projective, not just an unspecified projective object. Indeed, lift finitely many generators of its finite semisimple target to the projective cover Pbar. The image of the resulting continuous map (R/pi R)^n to Pbar is compact, hence closed, and surjects onto that target. Essentiality of the cover makes this image all of Pbar. The surjection splits by projectivity, so Pbar is a finite projective R/pi R-module. The argument above gives precisely the concluding integral-projective-envelope inference attributed to Paškūnas 2010 Proposition 4.6. It does not establish the prior existence of that K-injective envelope, the endomorphism x, or the exact sequence producing it. Those remain separate dependencies.

Apply this to the exact Coker(x) in BM Theorem 5.2. Section 3 supplies the admissible fixed-center enlargement; the homological construction of x and its snake-lemma sequence are the retained BM proof inputs. Thus the two replaced supplier steps and the retained construction have the same module and central-character domain. This is not a new assertion that arbitrary compact modules have finite projective reduction.

## 5. All-point spherical support

Paškūnas BM Proposition 4.14 as printed is broader than needed and cites Emerton's supercuspidal identification. Here is the restricted argument in its place.

Let Pi be a fiber in the preceding supersingular block, and let sigma be the specified pure algebraic K-representation. Any K-map sigma to Pi lands in Pi_lalg. The infinitesimal character fixes the algebraic factor. Colmez VI.5.7 describes the remaining smooth representation as irreducible or as the specified special extension. Nonzero locally algebraic vectors first imply the distinct-weight almost-de-Rham condition by VI.5.1. Theorem VI.6.13, printed p450, then gives the stronger implication that D is de Rham: its contrapositive says Pi_lalg is zero when D is not de Rham. Its local proof uses VI.6.12 and VI.4.9. This forward step is required before applying VI.6.30 and VI.6.50 in their de-Rham domain. Conversely, VI.6.18 supplies nonvanishing for the de-Rham representation with distinct weights.

If Hom_K(sigma,Pi) is nonzero, the remaining smooth factor has K-invariants. A supercuspidal smooth representation has no such vectors, and a twist of Steinberg has no such vectors. The possible exceptional extension is the reducible unramified principal series, not a new supercuspidal case. Compact averaging is exact in characteristic zero. Thus the spherical case has a one-dimensional K-fixed space and a two-dimensional normalized smooth Jacquet module J0. Colmez VI.6.30(ii) identifies that normalized smooth J0 with D_crab, and VI.6.50(i), using the explicit calculation in VI.6.33, identifies its smooth Weil parameter. Sphericity makes this parameter unramified with zero monodromy. Hence V_P has the corresponding crystalline type, and the single conversion V_P=r_C tensor epsilon in Section 1 gives exactly the R_p(sigma) type for r_C.

Conversely, if V_P has that corresponding crystalline type, its crystalline module has dimension two. It is also its crystabelline module. VI.6.30(ii) therefore gives normalized smooth J0 dimension two, and VI.6.50(i) identifies Pi_lalg with the local Langlands representation of this module, with the algebraic factor fixed above. Its unramified smooth principal series has a one-dimensional K-fixed space. This direction uses VI.6.30; it is not obtained by reversing the implication in the statement of VI.6.50(i).

This proves, on the restricted fibers,

    dim Hom_K(sigma,Pi)=1 exactly on the specified crystalline locus,
    dim Hom_K(sigma,Pi)=0 off that locus.

The argument includes nonsemisimple crystalline Frobenius and the reducible smooth principal-series exception. It does not replace the supercuspidal identity for arbitrary K-types. The relevant classical input here is only the unramified principal-series/Jacquet calculation; the separate supercuspidal minimal-type theorem in the predecessor is still a different source obligation.

Throughout this section J0 is the smooth normalized object in Colmez Section VI.6. Its dimension two is not the dimension of the full algebraic-tensored Jacquet module. The weight conversion of Section 1 is applied once in passing between V_P and r_C.

## 6. The principal-series self-extension bound

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

The generic crystalline points selected in Section 7 below exclude coincident Frobenius roots and the two reducibility ratios. In the normalized unramified principal-series parameter their two inducing characters are distinct; their common normalization factor does not change equality of the two characters. The selected points also have irreducible smooth principal series. The calculation above therefore replaces exactly the invocation of the Schneider–Stuhler resolution for dimension one in BM 4.19. BM 4.11's passage from smooth representations to the algebraic tensor factor remains its own stated input. The universal-completion and first-order Galois arguments remain separate inputs. No assertion is made at coincident-character or reducible principal-series points.

## 7. Reducedness on the crystalline locus

Paškūnas BM 6.4 uses the projective-envelope regular element from 5.2, the K-projectivity statement 5.3, and the commutative-algebra Lemma 2.33 and Proposition 2.29. For a nonzero type module this gives a Cohen–Macaulay module of dimension two over the fixed-determinant deformation ring. Its annihilator quotient is equidimensional and has no embedded associated primes. The zero module causes no problem and must be kept separate. These steps do not use the locally algebraic supercuspidal identity.

Proposition 2.32 requires a dense set with fiber dimension one and first-order fiber dimension at most two. It does not require the self-extension estimate at every point. The support is the crystalline locus by Section 5 and BM 2.22, which identifies the fiber of the compact Hom module with the dual of Hom_K. We can discard finitely many points of this one-dimensional characteristic-zero support.

The following extra restriction is useful for keeping the source chain short. In the **unframed** fixed-determinant crystalline deformation space with fixed distinct weights, the points with repeated Frobenius roots or root ratio p or p^(-1) form a finite set. Here is the direct calculation. The determinant and weights fix the nonzero product of the two Frobenius roots. Each of the three specified ratio conditions therefore fixes their unordered pair up to finitely many choices. With distinct roots, a filtration giving an irreducible representation has its nontrivial line off both eigenlines; otherwise the filtered module decomposes and weak admissibility gives a proper Galois subrepresentation. The diagonal centralizer acts transitively on the remaining lines. With a repeated root, scalar Frobenius cannot be weakly admissible with distinct weights: its higher-weight filtration line is stable and violates the slope inequality. A nontrivial Jordan block has one eigenline. The admissible irreducible filtration avoids it, and the Jordan centralizer acts transitively on its complement. Thus there are finitely many isomorphism classes of the filtered modules in question. Classification of crystalline representations then gives finitely many points. This assertion would be false for framed matrices, which retain conjugacy parameters; no framed space is being used here.

On the remaining dense set the smooth factor is irreducible unramified principal series, and the Frobenius roots are distinct and nonexceptional. The published Berger–Breuil construction applies. Its Theorem 4.3.1 identifies the completion by a finitely generated invariant lattice. Theorem 5.2.7 compares the Banach dual with the inverse-limit (phi,Gamma)-module. Corollaries 5.3.1–5.3.4 give nonvanishing, topological irreducibility, admissibility, and commensurability of invariant lattices. Therefore Pi is the universal unitary completion of its locally algebraic part at these points. This is precisely the principal-series input used in BM Theorem 4.19.

For completeness, the published Paškūnas 2009 paper covers the repeated-root completion by a local limiting argument in Theorem 4.4 and Corollary 4.5. It was retrieved and read, but the selected dense-set proof does not require that extra case. Its Section 5 also refers to a local Colmez crystalline calculation. No use of that paper's mere title or of a global modularity theorem is made here.

The principal-series paragraph of BM 4.19 injects the relevant Banach extension classes into extensions of the locally algebraic representation by itself. BM 4.11 removes the algebraic tensor factor at fixed central character. Section 6 proves directly that the smooth unramified principal-series self-extension space at fixed central character has dimension one at these distinct-character points. Thus the Schneider–Stuhler resolution is not needed for this selected estimate. These steps give condition RED on the selected dense set. The supercuspidal paragraph, which cites Dospinescu, and BM Section 7 on special series are unused in this local proof.

BM Lemma 4.20 bounds the relevant Galois Hom space by one through the fixed-determinant tangent-space calculation. The injectivity of the Banach Hom map is supplied by the supersingular block equivalence and its universal Galois representation, also expressed by *Image* 11.7 in this branch. Lemma 4.18 and the proof of Corollary 4.21 then give the first-order Hom_K bound two. Applying 2.32 gives reducedness of the annihilator quotient. The all-point support calculation of Section 5 identifies that reduced quotient with the crystalline deformation ring, which is the restricted assertion of BM 6.5.

There is no appeal here to the full BM cycle formula 6.6. In particular this does not close Hu–Tan's independent use of the full Breuil–Mézard theorem for arbitrary types.

## 8. The unframed Hecke map and its action

### Exact statement and normalization

Theorem4.1, author p31, interpolates the action of the type Hecke algebra on the one-dimensional type space in the classical locally algebraic representation attached to each potentially crystalline point. Its target is the generic fiber of the framed local deformation ring of that fixed type. The theorem does not assert an identification of the locally algebraic vectors in a p-adic Banach representation.

The source conventions in Section1.5, author pp5–6, use geometric Frobenius, Hodge–Tate weight -1 for epsilon, and

    r_p(pi) = rec_p(pi tensor |det|^((1-n)/2)).

Its algebraic representation is the dual of the highest-weight representation associated to the ordered Hodge–Tate weights. For n=2 and increasing weights u<v, the highest weight before taking the dual is (v-1,u). The dual has highest weight (-u,1-v), hence is

    Sym^(v-u-1) E^2 tensor det^(1-v).

This is exactly the CEGGPS body convention for the pure algebraic type used in the restricted route. It is not the conflicting introductory formula already excluded in the predecessor. The distinction between this negative-epsilon convention and the Paškūnas Galois label V_P is still handled by V_P=r_C tensor epsilon in Section 1 above.

The algebraic Hecke identification in the proof of Proposition4.2, author pp34–35, sends an endomorphism-valued Hecke function to its product with the algebraic representation. Its Bernstein-center twist is |det|^((1-n)/2). Thus its stated interpolation uses the same r_p normalization, rather than rec_p without this twist. The natural action on Hom_K is retained; no transpose or inverse character is silently substituted.

### Framed-to-unframed descent and the actual Hecke generators

Write R=R_p(sigma) for the unframed crystalline deformation ring of the auxiliary absolutely irreducible residual representation, with coefficients in O. Absolute irreducibility makes its residual endomorphisms scalar. Choose a representative of the universal unframed representation and a basis lifting the fixed residual basis. Changing this frame modulo scalar automorphisms gives the usual formally smooth three-dimensional frame space. Consequently the framed crystalline ring is noncanonically R^square=R[[x_1,x_2,x_3]]. The crystalline condition is invariant under change of basis, so this description descends from the unrestricted rings to the indicated crystalline quotients. The chosen universal frame defines a section s:R^square -> R of R -> R^square. This argument uses actual frames of the universal representation; it does not posit an invariants-ring identity.

Let eta^square:H(sigma) -> R^square[1/5] be the map supplied by CEG+16 Theorem 4.1. Define eta=s composed with eta^square. At every characteristic-zero closed framed point, forgetting the frame preserves the isomorphism class of the crystalline Galois representation. The interpolation character of the classical type space therefore agrees for that framed point and for the chosen frame of its underlying unframed point. Thus eta^square and the base change of eta have identical evaluations at every such point. The framed generic-fiber ring is reduced and Jacobson, as in the regular crystalline deformation-space input used by the theorem. Their difference on each Hecke element vanishes in the intersection of maximal ideals, hence is zero. This proves descent, its interpolation property, and independence from the choice of universal frame. It does not require the forgetful map to be injective on framed points.

The concrete formulas in CEGGPS Propositions 2.5 and 2.9 remove any remaining generator convention ambiguity. Set sigma=det^a tensor Sym^b, with b>=0. Its Galois weights in the negative-epsilon convention are r=-a-b and s=1-a. The algebra H(sigma)=E[S,S^-1,T] uses the algebraically normalized functions supported on diag(5,5) and diag(5,1), respectively. At a crystalline point let t and d be the trace and determinant of crystalline Frobenius. For unramified characters chi_1,chi_2 with chi_1(5)+chi_2(5)=t and chi_1(5)chi_2(5)=d, the smooth induction Ind_B^G(|.|chi_1 tensor chi_2) has the required normalized Weil parameter. Its unweighted double-coset eigenvalues are t on diag(5,1) and 5^-1 d on diag(5,5). The algebraic Hecke identification multiplies them by 5^(a+b) and 5^(2a+b). Therefore

    eta(T)=5^(a+b)t,       eta(S)=5^(2a+b-1)d.

Here t and d initially denote the universal analytic trace and determinant. The descended map shows that the displayed combinations lie in R[1/5]; division by the indicated powers also puts t and d in that generic-fiber ring. No integrality in R is claimed. Reducedness and the Jacobson property give the same formulas as ring identities, not just equality on a chosen dense subset. Every characteristic-zero lift of our absolutely irreducible residual representation is irreducible, so the indecomposability required in the filtered-module descriptions of Lemmas 2.6 and 2.7 holds at the relevant points. The comparison of the action alpha in Proposition 6.17 may now be made with this unframed eta on the same ring.

### Proof dependencies actually used

The local proof occupies author pp30–38, before the return to the global patched-module setting. Its stages are as follows.

1. A Weil–Deligne representation varies analytically over the fixed-type deformation space. Proposition4.2 uses the family result labelled Chenevier Corollaire3.19 and its pseudotrace description of the Bernstein center, then proves the needed generation statement in Lemma4.5. These concern classical Weil and smooth-representation parameters. They do not identify Banach locally algebraic vectors.
2. Proposition4.2 combines that family map with the algebraic Hecke identification and the explicit r_p twist. Classical type theory identifies the character on the type space. The proof uses its own Section3, including the classical local Langlands correspondence. A mention of a smooth supercuspidal Bernstein component in this argument is not an invocation of the disputed p-adic supercuspidal identity.
3. Lemma4.8 bounds the relevant Hecke eigenvalues. Its inputs are Hu2009 Theorem1.2(ii) versus (iv), Proposition3.2(2), and the locally analytic Jacquet formula of Emerton2006a Proposition4.3.6. The source bibliography identifies the latter as *Jacquet modules of locally analytic representations of p-adic reductive groups. I*, Ann. Sci. ENS39(2006), 775–839. This is not the Emerton2011 local-global compatibility manuscript. The use is the Jacquet formula for an algebraic tensor a smooth representation and its weak-admissibility inequalities.
4. Propositions4.10–4.12 extend the bound to the type Hecke algebra. Kisin2008 Theorem3.3.8 supplies generic-fiber regularity. The bounded-functions result of de Jong1995 Proposition7.3.6 then places the rigid-analytic values in the algebraic generic-fiber ring, proving Theorem4.1.

I read the stated proof and its direct citations at these locators. This is an incoming-edge audit, not a new independent proof of all of the cited classical type theory, family comparison, or rigid geometry. The Chenevier item was labelled a preprint in this old author PDF. A chapter with that title is now published in *Shimura Varieties*, LMS Lecture Note Series457, pp266–296, DOI10.1017/9781108649711.011. That bibliographic fact is not a completed statement-by-statement final-edition comparison.

No call to Emerton2011's disputed supercuspidal locally algebraic identity occurs in the bounded proof read here. This conclusion is based on the proof stages and their actual references, not on an assertion that any occurrence of the name Emerton is harmless. It does not cover other sections of the paper or all of its transitive ancestors.

### Connection at CEGGPS Proposition6.17

CEGGPS author pp33–34 define alpha using the rank-one type module. Its proof checks alpha=eta on a dense set of crystalline points. For the auxiliary absolutely irreducible residual block, all characteristic-zero Galois lifts are irreducible. The reducible-Galois branch citing Breuil–Emerton is therefore not used.

At the selected distinct-root nonexceptional crystalline points, the fiber construction in Section 2 supplies the actual Colmez Banach fiber, not merely equality of its Galois image. Berger–Breuil supplies the locally algebraic principal-series embedding with the indicated parameter. The type space has dimension one, so the Hecke character on the Banach type space is the character on this embedded classical type space. Theorem4.1 identifies that character with eta evaluated at the same point. Reducedness and density then give equality with alpha. These source inputs remain explicit in the present composition.

The unramified character variable does not change the two-Frobenius-root ratio. The nonexceptional dense set in the fixed-determinant one-dimensional space therefore remains dense after adjoining that variable. The reduced generic-fiber ring and its faithful rank-one module are the objects used to pass from pointwise equality to equality of ring maps.

For later integration, the dimension-two Jacquet statement in the all-point spherical argument means the normalized smooth J0 in Colmez's notation. It does not mean the entire Jacquet module after tensoring by an algebraic representation. This clarification records the independent review's scope; it changes no frozen predecessor bytes.

## 9. The four axioms and the common envelope

CEGGPS 6.10 removes the fixed central character using the universal character. The proof uses the pro-5 Iwahori subgroup, its central subgroup, and the determinant splitting at p>2. After adjusting the square root of psi, the completed tensor product of the two pro-free modules is pro-free over the Iwahori algebra. This is a compact-module argument and has no supercuspidal locally algebraic input.

CEGGPS 6.12 identifies the pure algebraic type module with the fixed-central-character type module tensored with the one-variable unramified character ring. The restricted BM 6.4/6.5 argument therefore gives the module and support claims of 6.14. The regularity of the crystalline generic fiber, together with Auslander–Buchsbaum, gives local freeness. The all-point Hom_K calculation in Section 5 gives rank one.

For 6.17, equality of the two Hecke maps need only be checked on a dense set. Use the distinct-root nonexceptional crystalline set in Section 7, now with the unramified character parameter retained. The fibers are the actual Banach objects identified in Section 2. Berger–Breuil supplies the embedded locally algebraic principal series. Its spherical Hecke character is exactly the one attached to the crystalline Frobenius parameter, with CEGGPS's body normalization. The rank-one module makes equality on this dense set imply equality of the two ring maps. The reducible-Galois paragraph involving Breuil–Emerton is outside our auxiliary block.

The four arithmetic-action axioms in 6.18 are then supplied by BM 6.1's finite generation, 6.10's projectivity, 6.14's crystalline type modules, and 6.17's Hecke compatibility. The uniqueness theorems 4.30/4.32 and the exact functor calculation in 6.19 remain part of the CEGGPS construction. They are not replaced by the assertion that a nonzero fiber has the desired image under check-V.

More explicitly, BM Proposition 6.1 makes the residual R_p-fiber finite over O[[K]]. Compact Nakayama makes Ptilde^psi finite over R_p^psi[[K]], and tensoring the rank-one universal-character module gives AA1. The fixed-center K-projectivity obtained from Sections 3–4 is the input to the determinant/pro-Iwahori calculation of CEGGPS 6.10, which gives AA2 without changing the envelope. The zero-type case and the square-root central-character adjustment in 6.12 are retained. Sections 5–7 give the fixed-center crystalline support, dimension and reducedness needed for 6.14; adjoining the unramified character parameter preserves the indicated Cohen–Macaulay property. Crystalline regularity and Auslander–Buchsbaum then give AA3, and the fiber calculation gives rank one. Section 8 gives AA4 on precisely this module, through its natural Hecke action.

CEGGPS Theorem 4.32 with d=0 now identifies this very module with the projective envelope in the category without fixed center. Theorem 4.30 gives uniqueness of its arithmetic action. These uniqueness statements remain selected source inputs. They do not furnish the Banach identification by themselves: that identification is Section 2, transported by the same character tensor product. At a point (y,z) of R_p^psi completed-tensor Lambda, the Banach fiber is B_y tensor (1_univ,z composed with determinant). Functor compatibility with character twisting gives r_x=r_y tensor 1_univ,z; the explicit Pi(D) construction in Section 2 and this twisting give B_C(r_x). CEGGPS Corollary 6.19 records the matching Galois image and nonvanishing, rather than serving as a substitute for that topological identification.


## 10. Exact auxiliary and manuscript consumers

The immediate consumer is `auxiliary-route-v1.md`, Sections 4–5. Its fixed-conductor type-lifting lemma produces an auxiliary characteristic-zero eigenpoint with the prescribed K-type. CEGGPS Theorem 7.4 identifies completed homology using the projective envelope and the dual global representation. Dualizing with those exact conventions gives the weak map for the local Banach fiber. Sections 2 and 9 supply the previously required local identification with B_C(r_x); it is the same R_p action and the same point, not an unrelated Banach representation chosen after specialization.

The remaining route uses the independent auxiliary construction over Q(sqrt(-2)), its conductor with ramification at two and 193, and absolute irreducibility at five. The original r5 is not assumed to have this residual type. The type criterion at the auxiliary classical point and classical local-global compatibility identify its supercuspidal factor and Weil–Deligne parameter. Colmez's filtration-independence statement then transfers the locally algebraic identity to the original target with the same parameter, after the stated unitary unramified twist. These are precisely the conditional C01–C09 connections in the predecessor. The present local theorem supplies their envelope input; it does not independently adopt every global input.

The current manuscript still uses Pan/Calegari at lines 830–863 and 7393–7409 of source 63db4260c5d918c91935461a814e1296378f051f12c61b12c6f3d896df8a3503. The byte-pinned consumer excerpts in this packet keep those occurrences separate from the proposed Hu–Tan alternative. Their existence does not establish the residual cyclotomic irreducibility required by that alternative. The finite-character and weight-two arguments following them also remain separate.

The precise next application question is whether the restored local supercuspidal identity, together with the retained general-type BM results, supplies the actual M1 and M2 inputs in Hu–Tan. The local theorem here does not eliminate those general-type results, the corrected Kisin/Gee–Kisin patching inputs, or the complementary residual branches. An independent application audit must make that connection before any manuscript replacement is proposed as unconditional.

## 11. Source and review boundaries

The theorem is conditional on the exact selected source statements in RETAINED-INPUTS.json. The component-review scopes and current incorporation status are recorded in REVIEW-STATUS.json. Their source qualifications are retained. No component decision is treated as a review of an enlarged mathematical conclusion.

The final editions of CEGGPS, Paškūnas BM, BP, CEG+16 and the indicated Chenevier family statement have not all been compared with the author texts used. Those qualifications remain explicit. The direct Ext calculation replaces the selected Schneider–Stuhler resolution invocation. The direct integral lift replaces the selected Paškūnas 2010 Proposition 4.6 invocation. The fixed-center BP bridge proves the finite-coefficient and admissibility connections while retaining BP's actual symmetry and tree-gluing inputs. These replacements do not assert equivalence with inaccessible final editions.

The restricted path excludes Image Theorem 12.7, Emerton 2011's disputed supercuspidal locally algebraic identification, Dospinescu's supercuspidal self-extension bound and BM's special-series branch. It retains local crystalline and mod-p sources, the general commutative-algebra arguments, and the specific classical Hecke-map inputs. The incoming-edge audit is not a claim that every ancestor has been proved anew. The later modular-curve factorization may use Emerton 2011 Section 5.5 through a different classical/density argument; a shared author or section number does not identify it with the excluded theorem.

Full source PDFs are not part of this supplement. The source versions used and the unresolved final-edition comparisons are recorded in SOURCE-QUALIFICATIONS.md.

