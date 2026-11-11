# Auxiliary residual representation and conditional local transfer

Project proof supplement, version 1. Sections 1–5 below preserve the mathematical text of the independently reviewed conditional auxiliary construction. The local envelope input referred to in Section 5 is supplied separately in proof-v1.md, on its listed source premises. Its application to the actual global and arbitrary-target setting remains conditional on the modular-curve, minimal-type and classical local-global inputs. The statement does not certify Hu–Tan, Pan, or the manuscript's modularity claim.

## 1. The precise problem and the source restrictions

Hu–Tan's final paper uses the description of locally algebraic vectors in the p-adic local Langlands correspondence. The unresolved part identified in the previous map is the identification of the smooth factor with the correct supercuspidal local Langlands representation. Nonvanishing of locally algebraic vectors does not identify that factor. The scalar closed-image supplement for Pan Lemma 3.5.9 proves a different assertion and supplies none of this identification.

CEGGPS is Caraiani–Emerton–Gee–Geraghty–Paškūnas–Shin, Compositio Mathematica 154 (2018), 503–548, DOI 10.1112/S0010437X17007606. The exact files currently read are its accepted arXiv v2 and the official Emerton-hosted author PDF. Neither file has been authenticated as the final journal typesetting. The author's current publication page identifies the published article; that metadata does not establish equality of editions. A bounded title/DOI/corrections search found no relevant correction, which is not a universal no-erratum claim.

In the accepted text, Assumption 2.2 requires scalar endomorphisms and excludes every twist of the extension with subcharacter omega and quotient 1. It permits the nonsplit extension with subcharacter 1 and quotient omega. Section 6.27 explicitly treats scalar semisimplification as speculative, not as a theorem. Theorem 7.4 additionally requires an odd absolutely irreducible global residual representation, irreducibility over Q(zeta_p), no vexing primes, and exactly the minimal tame level N of that residual representation. Remark 7.1 expressly warns against arbitrary tame-level substitutions. The quaternion generalization in Remark 7.8 contains its own unchecked-details qualification and is not used here.

The direct Hu–Tan comparison must also account for CEGGPS's inverse-cyclotomic adjustment to Paškūnas's modified Colmez functor in Section 6. Thus merely matching the written matrices in Assumption 2.2 to Hu–Tan's written matrices is insufficient. Even before that adjustment, an entire projective-envelope module cannot be replaced by a lattice change in one characteristic-zero point.

For orientation only, Hu–Tan M1 uses the nonsplit extension 0 -> 1 -> rho_1 -> omega -> 0 (final Sections 3.2.1 and 4.1). M2 is a different projective-envelope/pseudodeformation construction, not the universal deformation of that one lattice. For an absolutely irreducible characteristic-zero representation with two distinct residual characters, invariant lattices at the two ends of its fixed segment in the Bruhat–Tits tree yield both nonsplit orientations. Indeed the fixed subtree is bounded, since an unbounded ray would give an invariant line over the coefficient field. An endpoint with split reduction has at least two invariant neighboring vertices and is not an endpoint. The two endpoints give opposite invariant residual lines. One may enlarge the coefficient field first. This familiar lattice argument does not cover scalar residual semisimplification and does not identify M2 with M1.

The construction below avoids all these direct residual restrictions: its auxiliary representation has absolutely irreducible residual representation at 5. It proves a local smooth-factor statement and transports it by the published filtration-independence theorem. It does not apply Theorem 7.4 directly to the manuscript's r_5 or to the whole Hu–Tan M2 family.

## 2. Normalizations that must be kept explicit

Use the CEGGPS body convention HT(epsilon) = {-1}. Write the two labels as u < v. Body Section 2.1 assigns sigma_{A,B} = det^A Sym^B to weights (1-A,-A-B). Solving gives

    B = v-u-1,     A = 1-v.

Thus its algebraic factor is Sym^(v-u-1) det^(1-v). This also follows from its central character: the Banach representation has central character det(r) epsilon, whose algebraic exponent on units is 1-u-v; the displayed factor has exponent (v-u-1)+2(1-v)=1-u-v.

There is an actual mismatch in the author/accepted introduction. Example 1.2 on page 2, and the introductory AA3 formula, print det^(1-a) for ordered weights a<b. That is inconsistent with body Section 2.1. The official author's pages 2 and 8 were rendered and read. This proposal uses the body definition and the central-character calculation. It makes no claim about an unread final journal version.

Emerton's 2006 published Theorem 7.4.2 gives the classical factor as (Sym^(k-2))^dual tensored with the diagonal Tate character. If the positive-Sen labels are a>b, its factor is Sym^(a-b-1) det^(b+1). Under u=-a and v=-b this equals the preceding body formula. This is a change of numerical labels for the same representation, not an unannounced dualization. The draft 2011 proof's det^b must not be substituted for this factor.

For the Hu–Tan/Paškūnas convention, let V have positive-Sen weights h_1<h_2 and determinant epsilon*psi. Their algebraic factor is Sym^(h_2-h_1-1) det^(h_1), with central character psi. CEGGPS states explicitly that its modified Colmez functor is Paškūnas's functor followed by an inverse-cyclotomic twist. Consequently the same Banach object is labelled in CEGGPS by

    r = V tensor epsilon^(-1).

Its CEGGPS weights are (1-h_2,1-h_1), so the body formula gives exactly the Hu–Tan algebraic factor. Its central character is det(r) epsilon = det(V) epsilon^(-1) = psi. The Weil–Deligne representation of a cyclotomic twist is an unramified Weil twist. Therefore this adjustment preserves the inertial type and the vanishing of monodromy, which are the precise smooth-factor data consumed by Hom_K in Hu–Tan 4.9. This paragraph does not assert an equality of differently normalized full Frobenius parameters without making that twist.

## 3. An explicit auxiliary residual representation with no vexing primes

Set p=5, L=Q(sqrt(-2)), and q=193. The ring of integers is Z[sqrt(-2)]. Rounding both rational coordinates gives a remainder of norm at most 1/4+2/4=3/4, so the norm is Euclidean. In particular the class group is trivial and the units are {1,-1}. The prime 5 is inert, since -2 is not a square modulo 5. The prime 193 splits: 34^2=-2 modulo 193. Fix one prime qfrak over 193.

Let W=det^m Sym^n be any irreducible Serre weight of GL_2(F_5), with 0<=m<4 and 0<=n<=4. If n=4, replace the pair (m,n) temporarily by (m,0); the irreducible local representation below has both weights det^m and det^m Sym^4, by the explicit weight list in CEGGPS Lemma 2.15. Otherwise retain (m,n). Put k=n+1, so 1<=k<=4 after this replacement.

The ray class group of modulus (5)*qfrak is

    (F_25^* x F_193^*) / image{1,-1}.

Choose the character on F_25^* so that local class field theory gives the fundamental inertia character omega_2^k. One chooses its inverse if necessary according to the Artin convention; its value on -1 is in either case (-1)^k. Choose a generator character beta of F_193^*, and use beta^j with j=1 for k odd and j=2 for k even. Its value on -1 is (-1)^j=(-1)^k. The product is trivial on the diagonal global unit -1 and hence defines a ray class character theta. Its order at qfrak is 192 or 96. All values lie in a finite field of characteristic 5; F_(5^16) already contains roots of unity of orders 24 and 192. Global class field theory gives a continuous finite character of G_L unramified outside 5 and qfrak.

Define

    rho_bar = Ind_(G_L)^(G_Q)(theta) tensor omega^(m-1).

At 5, induction is from the unramified quadratic extension. The inertia characters are omega^(m-1)omega_2^k and omega^(m-1)omega_2^(5k). They are distinct because 24 does not divide 4k for 1<=k<=4. Frobenius interchanges them, so this local representation is absolutely irreducible. Its Serre weights include W by the explicit formula of Lemma 2.15, including n=4 by the replacement just described. In particular it has scalar endomorphisms and satisfies Assumption 2.2.

The global representation is odd: complex conjugation exchanges the two induced lines and has determinant -1; the scalar cyclotomic twist changes that determinant by a square equal to 1. It is absolutely irreducible. More strongly, it remains absolutely irreducible over Q(zeta_5). To see this directly, L and Q(zeta_5) are disjoint since the unique quadratic subfield of Q(zeta_5) is the real field Q(sqrt(5)). At qfrak, theta is ramified with order 192 or 96, while its conjugate character is unramified. The extension Q(zeta_5)/Q is unramified at 193. Thus theta and its conjugate remain distinct after restricting to G_(L Q(zeta_5)). The induction restricted to G_(Q(zeta_5)) is irreducible by the index-two induction criterion.

Its only possible tame ramified primes are 2 and 193. Neither is -1 modulo 5. There are consequently no vexing primes in the exact sense of Theorem 7.4, regardless of the local shape at 2. At 193 the local representation is a sum of one ramified and one unramified character, since L splits there. The Artin conductor exponent is 1. Thus the minimal tame conductor N is divisible by 193. We always work at this N; no arbitrary-level version of Theorem 7.4 is being used.

The usual Gamma_1(N) modular curve is torsion-free because N>=193. More explicitly, any finite-order rational matrix stabilizing the adelic level has eigenvalues roots of unity and trace in {-2,-1,0,1,2}; the Gamma_1 congruence forces trace=2 modulo 193, hence trace=2 and the finite-order matrix is the identity. The finite-level coverings used below are therefore coverings of curves rather than orbifolds. This is the needed neatness property for this GL_2 situation.

## 4. The fixed-level type-lifting lemma

Let K=GL_2(Z_5), let H_s be completed degree-one etale cohomology with O/pi^s coefficients at the fixed tame level Gamma_1(N), localized at the maximal ideal of rho_bar, and let H_hat=lim_s H_s. Cohomology is over an algebraic closure of Q. The two elementary cohomological inputs are the comparison theorem for finite local systems on a smooth affine complex curve and Hochschild–Serre for a finite-level covering. Such a curve has the homotopy type of a finite graph, so its cohomology in degree 2 vanishes for every finite local system.

For a finite smooth O/pi^s[K]-module M, use its exact O/pi^s-dual M^dual as a local system on the base curve. At sufficiently small level at 5 this system is constant. The Hochschild–Serre sequence, followed by the direct limit over these levels, gives

    Hom_K(M,H_s) = H^1(Y(K Gamma_1(N)), M^dual)_m.

Here the H^0 terms have vanished after localization. To justify that vanishing for these coefficient systems, pull to a finite cover trivializing M. Its H^0 consists of functions on connected components tensored with a finite coefficient module. The prime-to-level Hecke eigensystems there are Eisenstein, namely sums of characters. They cannot equal the trace system of an absolutely irreducible rho_bar. Pullback on H^0 is injective, so H^0 on the base local system also vanishes at m. Direct limits of these finite coefficient spaces are exact. This is the precise non-Eisenstein boundary input in the displayed identification.

The functor M -> M^dual is exact because O/pi^s is a finite self-injective principal local ring. The cohomology long exact sequence, H^0_m=0, and H^2=0 show that the displayed Hom functor is exact. Thus H_s is injective in the category of smooth O/pi^s[K]-modules. The coefficient long exact sequences also identify H_s with H_(s+1)[pi^s] and give the compatible reduction maps; there is no hidden degree-two obstruction.

Suppose tau is a finite-dimensional irreducible locally algebraic K-representation over E, Theta is a K-stable lattice, and a Jordan–Holder constituent W of Theta/pi embeds in H_1. Exactness of Hom_K(-,H_1) gives a nonzero map Theta/pi -> H_1. The fact that W may be only a constituent, rather than a submodule of Theta/pi, causes no problem: apply the exact Hom functor successively to a composition series.

Lift this map compatibly to every Theta/pi^s. Given a lift at s, identify Theta/pi^s with pi Theta/pi^(s+1), and H_s with the pi-divisible image inside H_(s+1). This defines a map on the submodule pi Theta/pi^(s+1). Injectivity of H_(s+1) extends it to Theta/pi^(s+1). Reducing that extension gives the prescribed map at s. Taking the inverse limit gives a continuous K-map Theta -> H_hat with nonzero reduction. After inverting pi this is nonzero, since H_hat is O-torsion-free by the same coefficient sequences. As tau is irreducible, tau -> H_hat[1/pi] is injective.

For the auxiliary rho_bar of Section 3, the required embedding W -> H_1 is supplied at this exact minimal level by CEGGPS Corollary 7.5 and Proposition 6.21(i). Its local residual representation is irreducible, so kappa(rho_bar|G_Q5) is the supersingular pi, and W embeds in pi by Lemma 2.15(v) and Frobenius reciprocity. A nonzero vector in the additional global rho_bar factor gives the required K-map. This does not require assuming that the original manuscript representation has a particular residual Serre weight.

## 5. The conditional local reconstruction

Let r be a two-dimensional absolutely irreducible potentially crystalline E-representation of G_Q5 with distinct body-convention weights u<v and irreducible Weil–Deligne representation. Let sigma be a minimal K-type for its supercuspidal smooth representation, and set

    tau = sigma tensor Sym^(v-u-1) det^(1-v).

The type theorem for GL_2 supplies irreducibility of sigma and says that a smooth irreducible representation containing it is an unramified twist of the prescribed supercuspidal representation. Tensoring with the algebraic factor preserves irreducibility on K: restriction to an open subgroup on which sigma is trivial is algebraically irreducible, and then the remaining finite action acts on its multiplicity space through sigma.

Choose any constituent W of a lattice in tau, and construct rho_bar and N as in Section 3. Section 4 injects tau into completed cohomology at this fixed minimal level. The space of such K-maps is finite-dimensional: the smooth type is trivial on an open subgroup and the algebraic factor reduces its computation to degree-one cohomology of a finite-level curve with a fixed finite-rank algebraic local system. The away-from-5 Hecke algebra preserves it. After a finite scalar extension it has an eigenvector, giving an eigenpoint x.

Use the actual published Emerton 2006 Theorem 7.4.2 to identify locally algebraic completed cohomology with the sum of classical cohomology tensored with the dual algebraic factors and diagonal Tate characters. The eigenpoint is classical, with the weights specified above, and is cuspidal because the localization is non-Eisenstein. Its smooth local factor contains sigma, so is an unramified twist of the target supercuspidal factor. Its local Galois representation r_x is irreducible, potentially crystalline with those weights, and has the corresponding irreducible Weil–Deligne representation. Classical local-global compatibility at 5 is a separate published input here, not a consequence of the mere existence of x.

Theorem 7.4, with its homology duals exactly as written, identifies specialization at x with P tensor_(R_p) r_x,global^dual. Taking the continuous E-dual identifies the corresponding completed-cohomology eigenspace with B_C(r_x) tensor r_x,global. The comparison with B_C is the one in CEGGPS Theorem 6.18 and Corollary 6.19, with its explicit inverse-cyclotomic functor normalization. In particular this gives the weak auxiliary eigenpoint map without the unpublished X(theta) construction.

The published classical decomposition identifies the locally algebraic part of the target with finitely many copies of the same supercuspidal factor tensored with the required algebraic representation and r_x,global. Colmez's published VI.5.7 says that a nonzero locally algebraic part is irreducible or is the specified special-series extension. The special-series case cannot inject into copies of a supercuspidal representation. Colmez VI.6.18 supplies nonvanishing for this de Rham representation. A nonzero coordinate projection of the resulting injection therefore gives an isomorphism

    B_C(r_x)^lalg = pi_sm(r_x) tensor Sym^(v-u-1) det^(1-v).

This argument does not need a newvector multiplicity-one assertion at the tame conductor. It only uses finite multiplicity and the absence of special-series constituents in a direct sum of supercuspidals. Absolute irreducibility and a finite coefficient extension ensure the coordinate projection is legitimate.

An unramified twist aligns the Weil–Deligne representations of r_x and r. It can be taken unitary: determinants of the two continuous Galois representations are unitary, so the square of the needed unramified character is unitary, hence so is that character. A finite coefficient extension supplies its square root when needed. The published Colmez VI.6.42 filtration-independence statement now transports the locally algebraic representation between the two admissible filtrations with the same Weil–Deligne module and weights. Undoing the unramified twist proves the same displayed formula for r. Extension of the coefficient field can be retained throughout the Hu–Tan application; no unproved descent of an arbitrary chosen isomorphism is needed.

This is the proposed replacement connection. It uses an auxiliary global representation only, never an extra hypothesis on the manuscript's r_5. It covers supercuspidal types of irreducible Hu–Tan M1 and M2 characteristic-zero specializations after the normalization in Section 2. Reducible characteristic-zero specializations, special series, and self-extension estimates retain their separate original arguments. Scalar residual semisimplification of the target is not an obstruction to this auxiliary construction, since the auxiliary residual representation is unrelated to it. No claim is made that Theorem 7.4 itself covers a scalar block.

## 6. Retained conditions

The local envelope argument is proof-v1.md. The modular-curve theorem at the exact minimal tame level, the classical type criterion, and classical local-global compatibility at the auxiliary point remain separate source inputs. The exact source-edition qualifications are in SOURCE-QUALIFICATIONS.md. In particular, a nonzero Banach fiber alone does not identify its locally algebraic smooth factor, and a local result for an auxiliary irreducible residual representation does not directly prove a general-type assertion in the target residual block.

The chronological proposal and its independent conditional review are pinned in the incorporation record. No final-edition comparison or full modularity approval is inferred from their existence.
