# The narrow Emerton input: conditional reconstruction and remaining interface

Author: /root/astra_v14_baseline_gaussian. This is an authored proof proposal, not independent acceptance. The direct replacement remains incomplete. No live manuscript was changed. The original 2011 draft is not relabelled as published.

## 1. Exact scope

The target is the smooth supercuspidal factor in the locally algebraic vectors of the local Banach representation. The consumers are Paškūnas BM 4.14, hence Hu–Tan 4.9/4.10, and the separate Paškūnas BM 6.5/6.6 route to Hu–Tan 4.2. Nonvanishing alone does not identify an inertial type. The final Hu–Tan paper and the existing dependency map retain their exact version distinctions. BM was inspected here in its author v3, not an unverified final edition.

I read Emerton's 2011 draft pp19,28,52–55,76–79,82–83,96–98,112–113. Its Remark 6.4.3 obtains a nonzero map from a specialized Hom module X(theta); Remark 7.4.2 then uses the map at an auxiliary classical point. This is narrower than all of Theorem 1.2.1, but it still needs the construction and finiteness properties of X(theta). A definition of X as a Hom space does not prove that its fiber is nonzero.

Two actual final sources were obtained and read:

* Emerton, PAMQ 2(2) (2006), 279–393, DOI 10.4310/PAMQ.2006.v2.n2.a1. The publisher PDF has final pagination and publication front matter. Theorem 7.4.2 is on p364; the associated classical decomposition is Theorem 2.5.1 on p295. This is a different paper from the 2011 draft.
* Colmez, Astérisque 330 (2010), 281–509, the final Numdam scan. Relevant inputs are VI.5.1 p438, VI.5.7 p441, VI.6.18 p452, and VI.6.42 p463 with its fixed-module setup on pp460–462. VI.6.50 and Remark VI.6.51 p466 explicitly retain the Emerton route for the supercuspidal identification. They do not independently prove the target identity.

## 2. Normalization without reusing the discrepant exponent

Fix the actual cohomological representation V_f in Emerton2006. His geometric-Frobenius convention and Tate-normalized smooth local factor are on pp285–289; V_f is the cohomological representation of Theorem 2.5.1. In the positive-Sen convention its weights are 1-k and 0 for a weight-k form. Let x:Q_p^* to E^* be the identity character. His p286 formula is epsilon=x|.|. Twisting the global cohomological representation by epsilon^n therefore contributes det^n to the algebraic factor and |det|^n to the smooth factor at p. The latter is precisely the smooth WD twist and must not be discarded in an equality of full G-representations.

Theorem 7.4.2 gives the algebraic representation (Sym^(k-2) E^2)^vee tensor det^n. The elementary GL2 identity (Sym^d E^2)^vee = Sym^d E^2 tensor det^(-d) changes this to Sym^(k-2) E^2 tensor det^(n-k+2). Put a=n, b=n+1-k. The result is

    W_E(a,b) = Sym^(a-b-1) E^2 tensor det^(b+1),  a>b.

This computation is from the published cohomological formula, not from the conjecture in the same paper. Its pp297–298 Conjecture 3.3.1 is only a consistency check, not an input. In particular, for cohomological weight two and n=0 the algebraic representation is trivial: a=0,b=-1 yields det^0. Substituting det^b instead would produce det^(-1), which is nontrivial on every sufficiently small central open subgroup. An unramified twist cannot remove that error, since it is trivial on Z_p^*.

Consequently the 2011 Section7.4 construction must choose tau = W_E(a,b) tensor sigma and carry that same algebraic factor through the classical target and comparison. The literal det^b expressions on draft pp97–98 cannot be combined with the p28 statement for the same a,b and pi_p notation. This report proposes the consistent replacement det^(b+1) throughout that argument. It does not silently amend the historical draft or claim that all its other steps have thereby been proved.

Numerical Hodge labels must also be translated. If u<v are the negative-Sen/filtration labels with HT(epsilon)=-1, then u=-a and v=-b for the same Galois representation. Thus the same algebraic representation is Sym^(v-u-1) tensor det^(1-v). This agrees with CEGGPS Section2.1's assignment sigma_(A,B)=det^A tensor Sym^B to weights (1-A,-A-B). It does not agree with the literal det^(1-a) in that paper's introductory AA3 for ordered a<b. The latter discrepancy is retained for the separate CEGGPS source audit. No change of labels changes an underlying Galois representation into its dual.

For the Paškūnas convention one must also change the Montreal functor normalization. The 2011 draft p19 footnote6 says its MF omits the cyclotomic twist present in Colmez's V. Conditional on that explicit functor comparison, a Paškūnas representation V_P with positive-Sen weights alpha<beta corresponds to V_E=V_P tensor epsilon^(-1), whose labels are a=beta-1,b=alpha-1. The preceding formula gives Sym^(beta-alpha-1) tensor det^alpha, precisely BM4.14's algebraic factor. The smooth factor simultaneously acquires the WD twist of epsilon^(-1), an unramified character. For the inertial-type test this does not change inertia. For a full smooth G-isomorphism it must remain in the formula. The exact equivalence of the Banach functors is retained as an input, not proved by matching central characters alone. Colmez's VI.2.4/VI.5.1 directly specify his algebraic type, so there is no need to infer the BM factor merely from the inconsistent draft display.

## 3. A complete density-to-all-fibers algebra lemma

This is the precise elementary core of the C.36 argument. It can replace an appeal to that proposition once its module hypotheses have been supplied.

Let A be a Noetherian E-algebra, Gamma a group, and M an A[Gamma]-module. Suppose H is a subgroup with an A-linear averaging projection e_H:M to M^H. Suppose F=M^H is finite over A and generates M over A[Gamma]. Assume a Zariski-dense set D of maximal ideals of A has M tensor_A kappa(m) nonzero. Then M tensor_A kappa(m) is nonzero for every maximal ideal m.

Proof. The splitting M=F direct-sum ker(e_H) persists under tensoring with every residue field. Thus if F has nonzero fiber then so does M. Conversely, generation gives a surjection from a sum of copies of F to M, so if F has zero fiber then M has zero fiber. The two fibers vanish at exactly the same points. Since F is finite, its support V(Ann_A F) is closed in Spec A. It contains D, hence it is all of Spec A. At every maximal ideal m the localized finite module F_m is nonzero, and Nakayama's lemma gives F_m/mF_m nonzero. This is the required fiber. This proof does not need A reduced; reducedness is needed only if one additionally equates full support with faithful action. End of proof.

For a smooth representation of a product of GL2(Q_l), l unequal to p, one may choose a compact open pro-prime-to-p H. On each smooth vector its averaging is a finite sum divided by a p-adic unit, so e_H exists integrally and commutes with base change. Finite generation of the smooth dual over A[Gamma] lets one shrink H to fix a finite set of generators. Admissibility then gives the required finite A-module of H-invariants. This applies only after those finite-generation/admissibility assertions are verified for the actual smooth dual of X(theta).

One also needs the fiber duality E tensor X(theta)[m] = (M tensor_A kappa(m))^vee in the appropriate admissible smooth category. This is an actual base-change and duality assertion, not part of the support argument. The draft obtains it from C.14/C.35; it must be supplied in a direct replacement. A faithful arbitrary module is insufficient: A=E[t] and M=A[1/t] are faithful, have nonzero fibers at every nonzero t, but have zero fiber at (t). The finite-module hypothesis above prevents exactly that failure.

Applied conditionally to the genuine X(theta), this lemma gives the nonzero eigenspace in draft6.4.3 from nonzero allowable classical fibers. Composing a nonzero element with the exact Hom identification (6.3.10) gives the weak map. No full local-global isomorphism, cotorsion-free envelope, or split-local-case machinery is used in this deduction.

## 4. A complete weak-map-to-smooth-factor lemma

Suppose rho is an absolutely irreducible finite-dimensional E-representation of G_Q, and B is an absolutely topologically irreducible admissible Banach representation of G=GL2(Q_p). Suppose B^alg is nonzero. Suppose a continuous nonzero G_Q x G-map j:rho tensor B to H exists, with H Hausdorff, and its target is the eigenspace of one classical cuspidal system. Assume the published classical decomposition identifies

    H^alg = rho tensor S tensor U,

where S=W tensor pi is the corresponding irreducible locally algebraic G-representation, pi is supercuspidal, and U is a multiplicity vector space on which G_Q x G acts trivially. Also assume the local algebraic structure theorem VI.5.7: B^alg is irreducible or has precisely the indicated algebraic-character and algebraic-Steinberg special constituents. These are independent premises, not conclusions extracted from the map.

The kernel of j is closed. Absolute irreducibility of rho implies that the E-algebra generated by its G_Q-action is End_E(rho). Matrix units therefore show that a G_Q-stable closed subspace of rho tensor B is rho tensor B_0 for a closed subspace B_0 of B. G-stability makes B_0 G-stable. Topological irreducibility gives B_0=0 or B; j nonzero excludes the latter. Hence j is injective.

Every locally algebraic source vector maps to a locally algebraic target vector, so j restricts to an injection rho tensor B^alg into rho tensor S tensor U. Applying matrix units again, or Hom_(G_Q)(rho,-), gives an injection B^alg into S tensor U. As an algebraic G-module, S tensor U is a direct sum of copies of the simple module S; it is semisimple and all its simple subquotients are S. Thus VI.5.7's special alternative is impossible, since its algebraic-character and algebraic-Steinberg constituents are not the supercuspidal factor S. Consequently B^alg is irreducible. Choose a nonzero coordinate of the image of a nonzero vector in S tensor U. Projection to that copy of S is a nonzero G-map B^alg to S. Its kernel is zero and its image is S, proving B^alg isomorphic to S. End of proof.

This avoids an unproved change of tame level. Draft6.4.3 initially gives a map into unrestricted tame-level cohomology. It does not by itself say that an arbitrary chosen multiplicity vector is fixed by the tame conductor subgroup K1(N). The argument above works with the full multiplicity U, or any finite level containing the image once that factorization is supplied. It never assumes dim U=1. The published classical eigenspace decomposition, including isolation of the one cuspidal Hecke system, remains required; Theorem7.4.2 by itself does not prove strong multiplicity one.

In the intended application, nonvanishing and the algebraic structure premise are supplied by Colmez's final VI.6.18 and VI.5.7, after identifying the Banach functor. Their proofs and statements were checked at the cited pages. The finite-dimensional algebraic factor W and the smooth representation pi are those of the classical target with the normalization in Section2 above. Finally VI.6.42 transfers the locally algebraic representation between admissible filtrations on the same fixed underlying potentially semistable module and fixed weights. Its setup and its proof do not permit changing the WD module or inertial type. An unramified twist is a separate operation which must be tracked as such.

## 5. First unfilled direct interface

The local-to-global auxiliary construction must first produce a classical point with the required supercuspidal type, correct weights, and the required residual/global hypotheses. A compatible type lift at a fixed minimal level is being authored separately in the CEGGPS route. This report does not assume that candidate is accepted.

Even granting that point, the direct 2011 replacement is not yet closed. The first unfilled connecting inference is:

    the auxiliary point lies in the Hecke spectrum
       implies a nonzero rho(point) tensor B(rho(point)|G_Qp) map into its completed-cohomology eigenspace.

The support lemma proves this only once the actual Hom module has a finitely generated admissible smooth dual, its residue-field duality is established, and its allowable classical fibers are known to be nonzero on a dense set. Draft6.3.12 proves the first assertion using 5.3.11/5.3.14 and AppendixC; 6.3.15–17 use universal unitary completions of nonexceptional crystabelline principal series; 5.4.9 supplies the density. These are substantive premises. They have been located and read in the draft, but their full construction and all needed published suppliers have not been independently rebuilt here. In particular, defining theta as the universal local Banach deformation does not prove its compatibility with the actual cohomological Hom module or its specialized fibers.

This is an incomplete replacement, not a demonstrated false assertion in Emerton's original argument. Colmez final p466 explicitly points back to Emerton for the missing supercuspidal identification, so citing that page as a replacement would be circular. A CEGGPS replacement of the weak map can use Sections2 and4 of this report once its own auxiliary-point hypotheses, dual convention, final-version status and classical target identification are verified. It need not use the unfinished X(theta) reconstruction.

## 6. Coverage, repeated consumers, and limits

The determinant correction affects every tau, target and comparison occurrence on draft pp97–98, not only the final display. The tame-level multiplicity repair affects the transition from6.4.3 to7.4.2. The nonzero-fiber lemma applies to the actual module only under its explicit hypotheses. None of these arguments identifies arbitrary inertial types merely from nonzero locally algebraic vectors.

The same smooth-factor conclusion is needed in both Hu–Tan M1 and M2 branches. The Dospinescu locally algebraic self-extension input, reducible ordinary/special calculations, global patching faithfulness, Kisin corrections and KW modularity remain separate. The actual manuscript's potentially good reduction does not exclude irreducible WD types at5, and therefore does not bypass this node.

The accompanying cards distinguish proved conditional joins from unfilled module/globalization inputs. They contain no independent acceptance. All new PDFs and full-text extraction files remain local-only. The publisher2006 text and Numdam2010 text were inspected, not merely identified from metadata. Bounded correction searches found no separate correction to the cited passages; this is not a universal absence claim. The 2011 draft's determinant mismatch and the CEGGPS introductory mismatch are explicitly retained. No full Emerton, Colmez, Hu–Tan, or global release proof is claimed.
