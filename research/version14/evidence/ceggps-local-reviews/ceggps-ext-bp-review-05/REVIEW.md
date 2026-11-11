# Principal-series Ext and BP application review

Reviewer: `/root/astra_quartic_opt05_anchor`, 2026-11-08. I did not author either argument. I read both complete proposals, their actual application cards and all 18 comparison fields. The source reads include BP author text Section 9, pp55–59; Paškūnas completions author text Lemmas 3.5–3.9; and the actual BM author text Theorem 4.19 and the opening of Theorem 5.2. Source versions remain those specified by the author, not final-edition substitutions.

Accept `ELEM-EXT`, Section 1 of `ceggps-elementary-suppliers-003`, manifest `12ebdc095d3b3cdab501ecd5ba754bf5eb63f01889e909999ba494f505f65d87`. Its Section 1 and ELEM-EXT card are byte-identical to the reviewed predecessor002. This decision excludes Section 2/ELEM-LIFT, assigned to the separate root reviewer.

Accept the bounded application connections in `BP-FIXED-CENTER-BRIDGE`, manifest `3b52b9f946160768dd88d3c56bf0744d0c4723b9e3c03ae580aa98b0aa562213`, conditional on the stated BP Section 9 symmetry and gluing inputs. This is not a proof or final-edition qualification of all of BP9.11.

## Ext computation and its consumer

The category fixes the action of the entire center on the middle extension, not just on its two constituents. This removes one of the two torus valuation directions. Smooth here means locally constant group action, so the additive cocycle in the final computation is locally constant, not an arbitrary p-adically continuous logarithm.

The exactness argument for N-coinvariants is valid in characteristic zero: N is an increasing union of compact open additive subgroups, coinvariants for each compact subgroup are exact by finite averaging on smooth vectors, and filtered colimits preserve exactness. Normalized induction is exact using compactness of B\G and local sections with locally constant values. The finite lifting argument can choose a common open stabilizer for the finitely many lifted values. Evaluation at the identity gives the stated adjunction with the half-modulus factors in the indicated directions. Smooth coinduction gives enough injectives in the fixed-center category. Therefore the passage to derived adjunction is valid.

I checked the Bruhat calculation with right translations. The open-cell identity is

`w n(x) diag(a,d) = diag(d,a) w n(x d/a)`.

The induction multiplier, Haar substitution factor and Jacquet twist are respectively `|d/a|^(1/2)`, `|a/d|`, and `|a/d|^(-1/2)`. They cancel. The open-cell constituent is w chi and the closed-cell constituent is chi. Integration identifies the translation coinvariants of compactly supported locally constant functions with the coefficient field; its kernel consists of translation differences. Distinct torus characters split the resulting two-dimensional extension by a separating torus element. The same argument kills their cross-Ext term.

Twisting the self-Ext by chi inverse then gives a two-dimensional extension with trivial central action, hence an additive locally constant homomorphism from T/Z=Q5^times to E. Its restriction to the compact unit group has finite image and is zero in characteristic zero. It is therefore determined freely by its value on 5. This establishes dimension one, including the lower bound by the explicit valuation cocycle. Finite coefficient extension does not change this calculation.

This is the precise smooth fixed-center input used in BM4.19. On the selected crystalline dense set the two normalized inducing characters are distinct and the smooth principal series is irreducible; the previous finite-exception restriction removed repeated roots and reducibility ratios. The common normalization of their Frobenius parameters does not change their equality. Passing to the algebraic tensor factor still uses BM4.11. The Banach completion and first-order Galois arguments are still separate. The proof does not make a new claim about coincident characters, special-series Ext or supercuspidal Ext.

Accordingly this new proof can discharge the previously open *dimension-one smooth Ext connection* in the conditional SC08 review. It does not by itself discharge the remaining BM/CEGGPS publication or other source obligations.

## BP fixed-center and finite-field bridge

The source Corollary9.11 requires the scalar uniformizer to act trivially and gives the full smooth K-injective envelope. Its actual statement does not already give the full prescribed central action required by BM5.2. The proposed bridge correctly treats these as two separate issues.

A finite field extension supplies c with c^2=zeta(5)^(-1). The unramified determinant twist makes the scalar matrix5 act as zeta(5)c^2=1 and does not change K-restriction. In BP9.8's actual construction the scalar uniformizer also acts trivially on the enlarged object. Hence imposing the desired central character there reduces to its central-unit conditions. The resulting eigensubspace is G-stable and contains pi. The eigensubspace functor is right adjoint to the exact inclusion of the fixed-center K-category, so it takes the full injective envelope to an injective object in that category. Every nonzero subobject still meets the same socle, which proves essentiality and identifies the fixed-center envelope. Untwisting restores the original central character.

The finite K-socle supplies admissibility rather than merely suggesting it. For any open H in K, Ind_H^K(1) is finite-dimensional and finite length. Hom into the full injective envelope is exact, and its dimensions on simple constituents are finite because every simple submodule lies in the finite socle. Its H-invariant space is therefore finite-dimensional. The fixed-center subobject inherits that bound. Arbitrary compact-open subgroups of G are handled by intersecting them with K. Every nonzero G-submodule meets the K-socle inside pi, and irreducibility then makes it contain pi. Thus the G-socle is exactly pi, as used in BM5.2.

The finite-field argument proceeds through the construction, not restriction of scalars from an algebraic closure. For K=GL2(Z5), smooth irreducibles factor through the finite residual group and the stated determinant twists of symmetric powers are absolutely irreducible over the chosen field. The same holds for the tame diagonal characters. Continuous functions on compact K have finite image, so the identity `C(K,k) tensor kbar = C(K,kbar)` is valid. The finite decomposition of this injective cogenerator into the envelopes of the split simple objects proves the required base-change identity, as in the actual proof of the cited author Lemma3.8. Invariants commute with this field extension, and admissibility makes the invariant spaces in BP9.6 finite-dimensional.

The finite group in BP9.2 has order 2(5-1)^2=32, invertible in k. Thus its averaging argument works before extending to the algebraic closure. The reflected-character dimension equalities used in BP9.6 are retained as source inputs; once those equalities are known after field extension they hold over k. Choosing inverse pairs of isomorphisms, and identity maps on the self-reflected spaces, uses only finite-dimensional linear algebra over k. The extension of the edge action and the tree gluing are then the same source construction. This checks the coefficient-field application; it does not reprove the imported symmetry identities or the tree results.

The conclusion therefore supplies the central-character, admissibility, G-socle and finite-field interfaces required at the opening of BM5.2. The subsequent Ext computations, regular element and integral projective lift are not supplied by this bridge.

## Scope and bindings

No defect requiring a change was found in these two bounded arguments. BP's final Memoirs edition, the retained symmetry/tree inputs, and the BM/CEGGPS final editions remain qualified. No result concerning the manuscript's original local representation is obtained by imposing the auxiliary residual hypotheses on it. The selected auxiliary domain is unchanged.

The independent checker verifies the three exact manifests, their referenced files/source hashes, the Section 1 identity from002 to003, and the unchanged ELEM-EXT card. It checks bindings only. No author code was run. The 003 changes to compact-character convention and finite projectivity belong to root's ELEM-LIFT review, not this acceptance. The target proposals and earlier adverse/source-history records were not modified.
