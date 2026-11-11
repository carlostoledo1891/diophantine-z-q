# Proposed connection from BP diagrams to the fixed-center envelope

This is a bounded author proposal, not an independent acceptance or a final-edition comparison. Its source is Breuil–Paškūnas, author-hosted *Towards a modulo p Langlands correspondence*, Section9, especially Theorem9.8 and Corollary9.11 on author pp58–59. Its consumer is Paškūnas BM, author p29, the opening paragraph of Theorem5.2. The source text and its predecessor references remain separate publication and proof obligations.

The consumer needs a smooth admissible G=GL2(Q5)-representation Omega with central character zeta containing the absolutely irreducible supersingular representation pi, such that Omega restricted to K=GL2(Z5) is the injective envelope of soc_K(pi) in the fixed-zeta category. The source corollary is phrased with the scalar uniformizer acting trivially and with an injective envelope in the full smooth K-category. It is therefore necessary to check both the scalar twist and the restriction to a central character.

## 1. Scalar uniformizer and the center

Permit a finite extension of the residual coefficient field k at the outset. Choose c in that extension with c^2=zeta(5)^(-1). The unramified character mu of Q5^times with mu(5)=c is trivial on Z5^times. Replace pi by pi tensor (mu composed with determinant). The scalar matrix 5 acts on this representation by zeta(5)mu(25)=1. Its restriction to K is unchanged. The extra property(S) assumption in BP Corollary9.11 occurs only at p=2, so it is absent here.

Apply the diagram construction to this twisted representation, provisionally granting the source statement over the chosen coefficient field as addressed below. It gives an embedding into a smooth G-representation Omega0 whose restriction to K is the full injective envelope of the K-socle. It does not yet give the prescribed action of every central unit.

Let zeta' be the twisted central character, and define Omega1 to consist of the vectors v in Omega0 satisfying z v=zeta'(z)v for every z in Z. This is G-stable because Z is central, and it contains the twisted pi. Since scalar 5 already acts trivially, the only additional conditions are those on Z intersect K.

The inclusion from the smooth fixed-zeta' K-category into the full smooth K-category is exact. Its right adjoint is the zeta'-eigensubspace functor. A right adjoint to an exact functor takes injective objects to injective objects: the adjunction identifies Hom into the eigensubspace with Hom into the original injective object after the exact inclusion. Thus Omega1 restricted to K is injective in the required fixed-center category. The socle inclusion remains essential. Every nonzero K-submodule of Omega1 is also a submodule of the full injective envelope and intersects its socle nontrivially. Hence Omega1 restricted to K is the fixed-center injective envelope of that same finite socle.

Untwisting by mu composed with determinant restores the original zeta. It preserves all assertions and is trivial on K. This supplies the exact central-character form required by BM, rather than assuming that the full K-envelope already had scalar central action.

## 2. Admissibility and the G-socle

The K-envelope of a finite semisimple socle is admissible. To see the required finite-dimensional invariant spaces directly, let H be an open subgroup of K. The smooth representation Ind_H^K(1) is finite dimensional, hence of finite length. For an injective envelope I of a finite semisimple socle, Hom_K(S,I) is finite dimensional for each irreducible S: every simple submodule lies in that socle. Exactness of Hom_K(-,I), and induction on the finite length of Ind_H^K(1), gives finite-dimensional Hom_K(Ind_H^K(1),I)=I^H. This also works in the fixed-center category by starting with the full envelope and then taking its subspace. Thus Omega1 is admissible for G.

Every nonzero G-subrepresentation of Omega1 is a nonzero K-subrepresentation and intersects soc_K(pi), hence intersects pi. Irreducibility of pi forces it to contain pi. Consequently soc_G(Omega1)=pi. These are the two additional properties used in BM5.2 before its homological construction of x.

## 3. Finite coefficient field in the source construction

The displayed BP source convention uses an algebraic closure of the residual field. One must not obtain a finite-field admissible envelope by merely restricting scalars from that algebraic closure. Instead the construction of Section9 can be performed over the chosen finite field k in this Q5 case, after the finite scalar extension already allowed in Section1.

Here are the actual points to check. The tame diagonal group H in BP9.1 has characters valued in F5^times, so it is split over k. The irreducible representations of GL2(F5) occurring in the K-socle are the determinant twists of Sym^r(k^2), 0<=r<=4; they are absolutely irreducible over k. Thus all the finite socle constituents used here are already split.

Injective envelopes and the needed direct-summand decompositions exist in the smooth k-category. Their formation for these finite socles commutes with extending k to its algebraic closure. One can check the latter using the injective cogenerator C(K,k): continuous functions on compact K have finite image, so C(K,k) tensor kbar equals C(K,kbar). Decompose this injective object by its absolutely irreducible socle constituents and use uniqueness of injective envelopes. This is also the argument of Paškūnas's completion paper, author Lemma3.8 on p10.

BP9.2 uses only that the finite group generated by H and the edge reflection has order 2(5-1)^2, invertible in k. Its averaging argument therefore works over k. In BP9.5 the induced injective envelope and its extension of the edge-stabilizer action are constructed over k. The remaining dimension equality in BP9.6, between the chi and reflected-chi invariant spaces in the K-injective envelope, descends from the source equality over kbar by the preceding base-change compatibility. These invariant spaces are finite dimensional by admissibility. The isomorphisms between equal-dimensional spaces, their inverses, and the identity on fixed-character spaces can all be chosen over k. No infinite coefficient extension is required for these choices.

The resulting two compatible stabilizer actions are glued by the same tree/diagram construction used in BP9.8. BP9.9 then checks injectivity on the vertex component, and Corollary9.11 gives the desired embedding. The source's finite-group symmetry equalities and its tree-gluing results remain explicit source inputs; this paragraph checks their coefficient-field use, not their entire proofs.

## 4. Limits

The source final-edition comparison is still open. The argument above is a proposed application connection, conditional on the precise Section9 construction and its stated symmetry and gluing inputs. It is not a replacement proof for all of BP9.11.

The separate elementary-suppliers proposal proves the integral lifting step after BM has constructed Coker(x). It does not provide this G-compatible injective enlargement. Conversely the present bridge does not establish BM's Ext calculations, regular element, or crystalline reducedness. Both proposals require independent review, and neither implies full C10, Hu–Tan, Pan, or manuscript acceptance.
