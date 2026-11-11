# Review of the scalar closed-image replacement

Reviewer: `/root/astra_v14_assertions_arithmetic`, a model agent distinct from the author `/root`. The root proposal was read before the primary-source reconstruction; this was not a blind review. The exact reviewed manifest is SHA-256 `8819a30ada5c85a6eec20414b6a8f7ef5444c9f700b4f68aeedcb62a1478bbb6` in `../pan-closed-image-root/MANIFEST.json`.

Disposition: accepted for the stated conditional interface. A continuous equivariant map with dense image between admissible scalar `E`-Banach representations of a compact p-adic Lie group is surjective, and the proposal proves that its Banach topology is the quotient topology. This supplies the particular surjectivity inference in the pinned Pan Lemma 3.5.9, once its two admissibility assertions and universal-completion map are granted. Those upstream assertions, Pan's other inputs, final-JAMS comparison, and project incorporation remain outside this acceptance.

## Published source and exact reading

I read the actual journal-layout Schneider–Teitelbaum PDF, SHA-256 `e713af9c176a498de80b30496ace6028dc76cb46a09d49efcea7ccb6867bff3a`, including printed pp. 361–364 and 370–374. The header identifies *Israel Journal of Mathematics* 127 (2002), 359–380. The separate author-hosted PDF was not substituted for it. I visually inspected the rendering of printed p. 364, where the compact-module splitting is used, to check the exact category and the dense-image qualification in Proposition 1.3(i).

The published inputs actually used are the scalar Banach duality of Theorem 1.2, its equivariant form Theorem 2.3, the noetherian property stated at the start of §3, the canonical topology and closed-submodule facts of Proposition 3.1, and the admissibility/finite-generation equivalence of Lemma 3.4 and Theorem 3.5. The proof of Proposition 1.3(i) explicitly applies continuous splitting to a surjection between compact torsion-free linearly topologized `O`-modules, citing SGA 3 VII B 0.3.7. The replacement uses precisely this splitting assertion. This review uses that published assertion and does not claim a separate audit of the SGA proof.

Proposition 1.3(i) alone only supplies density of the transpose of a general injection; the source visibly keeps a closure in its quotient statement. The replacement does not misread that proposition as automatic surjectivity. It supplies the extra finite-generation and saturation argument needed for actual surjectivity.

I also read Pan's exact pp. 30–32 in the pinned September 3, 2021 author PDF, SHA-256 `590171129d28a65749cf92b1f6099dbacaa90cc6698828f0a4dfd3da943f4824`, and Emerton's draft pp. 14–15 and 118. Emerton Remark 3.1.5 says that the scalar `A=O` case follows from [77]; [77] on p. 118 is this published Schneider–Teitelbaum paper. The author's `SOURCE-PINS.json` pins p. 119 rather than p. 118 for the bibliography. The whole PDF is correctly pinned, so this is a minor locator omission. The review evidence adds the correct p. 118 passage. No mathematical correction to the proposed proof is needed.

## Reconstruction of the argument

Let `R=O[[H]]`, with `H` compact p-adic Lie. The ring is left noetherian and `varpi` is central. Admissibility and published duality identify the original spaces with `M^d` and `N^d` for finitely generated torsion-free compact `R`-modules. The exponent `d` denotes continuous `O`-linear functionals to `E`, equipped with their sup norms. The rational dual module means `E tensor_O R`, as in the source, and not unrestricted formal series.

The original map `u` transposes to an `R[1/varpi]`-linear map from `N[1/varpi]` to `M[1/varpi]`. To see explicitly that the lattice adjustment preserves the original Banach topology, choose finite `R`-generators of `N`. Their images have a common denominator `varpi^k`. The enlarged lattice `M' = M + f(N)` satisfies `M subset M' subset varpi^(-k)M`. Its dual norm is therefore equivalent to the old one. Proposition 3.1 makes the natural lattice maps continuous for the canonical topologies, and the natural duality identifications identify the new transpose with the same `u`. This verifies the proposal's lattice adjustment, rather than treating an arbitrary algebraic relabeling as topologically harmless.

Density of `u(V)` makes its transpose injective: a continuous functional vanishing on this dense image vanishes on all of `W`. With the adjusted lattice denoted again by `M`, put `A=f(N)`. The injection `N->M` is continuous by Proposition 3.1. Since `N` is compact and `M` Hausdorff, `N->A` is a homeomorphism for the subspace topology. Thus continuous functionals on `N` are exactly those on `A` under this map, including equality of their sup norms.

Put `T=M intersect A[1/varpi]`. It is an `R`-submodule. Noetherianity of `R` and finite generation of `M` imply that `T` is finitely generated; Proposition 3.1 makes it closed. Each generator belongs to `A[1/varpi]`, so a common exponent gives `varpi^r T subset A`. Centrality of `varpi` ensures that this holds for every `R`-linear combination of the generators. This is the uniform bound absent from general dense non-surjective Banach maps.

The quotient `Q=M/T` is compact and Hausdorff because `T` is closed, and it has the quotient linear topology. If `varpi m` is in `T`, then `m` is in `A[1/varpi]` and hence in `T`. Thus `Q` is torsion-free over the discrete valuation ring `O`. The source's compact-module splitting applies to `M->Q`; it gives a continuous `O`-linear section of this surjection, and subtracting its composite with the quotient map gives a continuous retraction `rho:M->T`. Equivariance is unnecessary here.

For a continuous functional `lambda:A->E`, the map `t -> varpi^(-r)lambda(varpi^r t)` is well-defined on `T` and continuous. Indeed, multiplication by `varpi^r` maps `T` continuously into `A` with its actual subspace topology. It agrees with `lambda` on `A`. Composition with `rho` therefore extends `lambda` to `M`. This proves that restriction `M^d -> A^d`, and hence the original `u`, is onto.

The extension is linear in `lambda`, and its norm is at most `|varpi|^(-r)` times the norm on `A`. It is a bounded `E`-linear right inverse. Thus, for any target vector of sufficiently small norm, this chosen lift has a prescribed small source norm. This proves openness and the quotient-topology assertion. It does not produce an equivariant section, and none is claimed or used. The compactness, saturation, splitting, and norm steps all concern the exact topologies specified in the published source.

## Pan's map and the consumed conclusion

Pan p. 30 first allows a finite extension of the coefficient field so that `E(p)=E`. Its `p` in this notation is a maximal ideal and is distinct from the residue characteristic. The space `Pi(p)` is defined as the closure of the specified image of locally algebraic automorphic vectors in the Banach space of completed forms. On p. 31, `Pi_v` is the universal unitary completion of the displayed locally algebraic representation, and the multiplicity `d(p)'` is finite.

The universal property gives the actual continuous equivariant map from `Pi_v` to this closure, with the indicated finite multiplicity. Its image contains the original dense locally algebraic image, so it is dense. The same paragraph asserts admissibility of `Pi_v`, and Lemma 3.5.9's proof asserts admissibility of both source and target. These are inherited premises of the replacement. Restriction to the compact open subgroup `GL_2(O_(F_v))` has the scalar compact-group admissibility used by Schneider–Teitelbaum: the admissible-lattice condition is tested on compact open subgroups and is unchanged by restricting the group. Finite direct sums retain it. The replacement then proves surjectivity of this same map; its original full `GL_2(F_v)` equivariance remains intact.

Immediately afterward Pan precomposes continuous equivariant maps out of `Pi(p)` and obtains the displayed injection of Hom spaces. If two maps have the same precomposition, surjectivity makes them equal on every element of `Pi(p)`. In fact continuity and density already suffice for this particular injection. Pan then compares the two central actions on the target Hom space. This replacement neither changes that Hom space nor asserts equivariance of the auxiliary section. It supplies the quotient assertion and the precomposition step, not the remaining comparison with blocks, Colmez's functor, or the subsequent modularity argument.

The proposal's adverse example also checks: diagonal multiplication by `varpi^n` on `c_0` has dense image containing all finite sequences, while `(varpi^n)` has no preimage in `c_0`. For trivial group action that infinite-dimensional representation is inadmissible. The example correctly shows why admissibility cannot be omitted.

## Coverage and nine checks

| Obligation | Disposition |
|---|---|
| Source hypotheses | Finite p-adic coefficient field and compact p-adic Lie group fit the published source. Admissibility is an explicit inherited premise. |
| Constructed objects | Compact lattices, image `A`, saturation `T`, and quotient `Q` were reconstructed and their topologies checked. |
| Domains and parameters | Scalar `E` only; all residue characteristics allowed. No general coefficient algebra `A` result is accepted. |
| Connecting maps | The lattice transpose is naturally the original map. The extension restricts to the original functional. |
| Actual consumed object | The quotient is the defined closure `Pi(p)` and the downstream Hom spaces are unchanged. |
| Normalizations | `E[[H]]=E tensor_O O[[H]]`; the lattice changes preserve equivalent Banach norms; the dual uses continuous functionals. |
| Local conditions | Restriction to a compact open group changes neither the vector space nor its Banach topology. Full-group equivariance of the original map persists. |
| Exceptions | Zero spaces and multiplicities are harmless. Inadmissible infinite-dimensional dense maps are excluded. |
| Related uses | The immediate Hom injection and the following central-action comparison were read. Other Eme11 uses and upstream representation results remain separate. |

I checked the proposal's literal `Eme11` occurrence inventory against the pinned text and read the associated locating passages at Pan pp. 2–4, 20–22, 29–32, and 124. The inventory correctly separates strategy/history, functor-normalization discussion, and the density argument proved in Pan from the explicit Proposition 3.1.3 appeal. It is a bounded literal-citation inventory; it cannot establish absence of implicit or transitive dependence on the draft. The density proof's other inputs are not discharged here.

The source author reports a bounded correction search. This review does not independently certify a complete errata search. The mathematical reading uses the pinned final journal text and no unstated correction. The exact published splitting premise is identified rather than treated as newly proved.

No blocking defect was found in the replacement. Acceptance is limited to this proof and its conditional Pan application. It does not certify upstream admissibility, final Pan equivalence, incorporation into the main manuscript, or closure of the Pan proof chain.
