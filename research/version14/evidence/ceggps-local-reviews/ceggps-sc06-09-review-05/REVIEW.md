# Restricted SC06–SC09 review

Reviewer: `/root/astra_quartic_opt05_anchor`, 2026-11-08.

Accept the new connections in Sections 3–5 of `ceggps-source-closure-003`, manifest `1e72cdaf9f121322098669eb7e5c97d26679c9a1f181be7870ba20a5759af708`, with the retained inputs and unresolved qualifications stated below. This is a conditional mathematical decision on SC06–SC09, not full C10 closure. The exact report hash is `763b454b79c07f7db5df584549e63abbf4633dff31ba0615a1f500cdfcd5e2da`.

I did not author these connections. I previously reviewed the auxiliary route conditionally. SC01–SC05 are supplied by Gaussian's distinct review, manifest `8b630ead929dbd22d84ab49d3b50838b56ccedfbff83cc0c11f14d5ee2bac72d`; I do not take authorship or renewed review credit for those results. In particular their actual Colmez-construction identification is an input here. Equality of Galois images alone would not suffice.

I read all of Sections 3–5 and their four application cards, the neighboring domain and exclusion statements, and the actual source passages listed in CHECKS.json. These include the pinned CEGGPS author text 6.10–6.18, BM author text 2.32–2.33, 2.42–2.43, 4.18–4.21 and 5.2–6.5, published Colmez VI.5.7, VI.6.13/18/20/30/33/50 and their local arguments, and published Berger–Breuil 4.3.1, 5.2.7 and 5.3.1–5.3.4. I visually checked Colmez printed p466 and Berger–Breuil p207 against extraction. Numdam's official records confirm the published Astérisque identities, not the independent correctness of every ancestor. The private page images are excluded from this review's public artifact list.

## SC06: all-point support

A finite-dimensional algebraic K-type mapping continuously into the Banach fiber supplies locally algebraic vectors. The irreducible algebraic factor and its highest weight determine the type; the smooth factor contributes its K-invariants. This is why a spherical calculation of the smooth factor, rather than the smooth factor's full dimension, is required.

The proposal correctly uses VI.6.13 before the de Rham comparisons. Nonzero locally algebraic vectors first give the distinct-weight almost-de-Rham domain, and VI.6.13 then supplies de Rham. VI.5.7 restricts the smooth possibilities to an irreducible representation or the stated special extension. A spherical irreducible smooth representation is unramified principal series; supercuspidal and Steinberg twists have no K-invariants. In the exceptional extension, exact compact averaging leaves the one-dimensional invariant space of its unramified character quotient. A ramified twist has none.

The two-dimensional Jacquet space in this argument is the smooth factor's space, equivalently Colmez's normalized `J_0(Pi_alg)`. It is not the full algebraic tensor product `J(Pi_alg)`, whose algebraic factor is recorded separately on printed p453. With this convention VI.6.30(ii) supplies the actual isomorphism with D_crab. VI.6.50(i), with the explicit repeated-root calculation in VI.6.33, then identifies the parameter and its zero monodromy. Sphericity forces trivial inertia, hence crystalline rather than merely crystabelline.

Conversely, a crystalline representation of the specified distinct weights has D_crab of dimension two. VI.6.18 and VI.6.30 apply and give `dim J_0=2`; VI.6.50(i) then identifies the unramified smooth representation. Its K-invariants are one-dimensional, including the special principal-series extension and nonsemisimple Frobenius cases. This is an actual converse argument, not a reversal of VI.6.50's displayed implication. The determinant and weight convention remains that of Section 1 and the accepted SC01–SC05 input. Thus the all-point dimension-one/zero assertion checks in this auxiliary block. It does not establish the supercuspidal identity for arbitrary K-types.

## SC07: finite exceptions and density

The fixed determinant fixes the nonzero Frobenius determinant. Repeated eigenvalues or ratio 5 or 1/5 leave finitely many unordered eigenvalue pairs over a finite coefficient extension. For distinct roots, the diagonal centralizer is transitive on filtration lines off the two eigenlines. A filtration along an eigenline splits the filtered module; weak admissibility forces both summands to be weakly admissible, contradicting irreducibility of the Galois representation. For a repeated scalar root, the higher-weight line is stable and violates weak admissibility. For a Jordan block its centralizer is transitive on the complement of its unique eigenline, and a filtration along that eigenline again violates the slope inequality. These observations verify the finite number of filtered-module isomorphism classes.

The unframed condition is essential. In this absolutely irreducible residual domain, the stable lattice is unique up to homothety, and its residual identification is unique up to the scalar centralizer; forgetting a frame introduces no additional family of deformation points over a fixed characteristic-zero isomorphism class. The conclusion would not hold for framed points. The proposal explicitly excludes that interpretation.

For a nonzero type module, the retained BM 6.4/2.33 input gives dimension two, no embedded associated primes and torsion-freeness. BM Remark 2.43 then makes removal of the finite exceptional set dense in every generic component and in the total support. The zero module is separately handled. Thus the finite-set calculation is sufficient for the density needed by 2.32; it does not assume reducedness in order to prove reducedness.

## SC08: reducedness, conditionally on the stated suppliers

On the remaining distinct-root, nonexceptional crystalline set, the smooth principal series is irreducible. Berger–Breuil 4.3.1 gives its completion from a finitely generated invariant lattice. Their 5.2.7 and 5.3.1–5.3.4 give the nonzero irreducible admissible Banach object and commensurability of invariant lattices. The actual fiber identification from SC01–SC05 applies to this object. The repeated-root completion is unnecessary for this dense-set argument; the report does not use the separate 2009 result to cover a hidden remaining point.

The principal-series branch of BM 4.19 takes the relevant Banach extensions into locally algebraic extensions. BM 4.11 removes the algebraic tensor factor at fixed central character. The smooth fixed-center self-extension dimension-one assertion is still a retained input in this exact packet. With that input, RED follows. The supersingular-block Hom comparison, BM 4.20 and 4.18 give the first-order Hom_K bound two by the exact sequence in the proof of 4.21. These are bounds for the first-order fibers used by 2.32, not a claim that every extension in every block has dimension one.

The hypotheses of 2.32 therefore match: equidimensional support without embedded associated primes, a dense set of dimension-one fibers and first-order bound two. Its reduced quotient has the all-point support already identified by SC06. Torsion-freeness and the defining reduced crystalline quotient give the restricted BM 6.5 identification. No cycle formula, special-series RED proof or supercuspidal self-extension estimate is imported.

This acceptance does not close the exact smooth Ext supplier. The newly authored `ceggps-elementary-suppliers-002` is a different target and is not accepted by this decision. Nor does it close the separately listed BP enlargement/projective-lift source comparisons.

## SC09: arithmetic action

The pro-5 Iwahori argument in CEGGPS 6.10 uses the determinant isomorphism on its central pro-5 subgroup. The square-root twist is legitimate at p=5. Its completed tensor product and pro-free conclusion match the stated compact modules. This step is independent of a supercuspidal locally algebraic identity.

The type-module isomorphism of 6.12 retains the unramified character variable and the fixed-center twist; an incompatible central character gives zero on both sides. The conditional SC08 result yields the Cohen–Macaulay crystalline type module. The retained regularity of the crystalline generic fiber and Auslander–Buchsbaum give local freeness; SC06 gives rank one at all its points.

For the two Hecke maps, the excluded fixed-center points become exceptional subsets after adding the unramified parameter, rather than a finite set in the larger space. Their complement is still dense. At its points the actual Berger–Breuil locally algebraic embedding has the prescribed Frobenius parameter. The one-dimensional spherical space identifies the character with the retained eta-map convention. Equality on this dense set implies equality of the maps into the reduced crystalline ring. The rank-one type module makes this the appropriate target ring of endomorphisms. A reducible-Galois Breuil–Emerton branch is not needed, because every lift of this auxiliary absolutely irreducible residual representation is absolutely irreducible.

Thus the restrictions in the report correctly feed the four arithmetic-action axioms. Finite generation, the uniqueness formalism and the final specialization calculation are still explicit CEGGPS inputs. This review does not replace them with a nonzero-fiber assertion.

## Unresolved qualifications and disposition

No new mathematical defect was found in these four restricted connections. Their acceptance is conditional on the named source statements, and the following remain open in this exact record:

- Final CEGGPS and final Paškūnas BM edition comparisons. The author versions remain identified as such.
- The smooth principal-series fixed-center Ext calculation and the BP enlargement/projective-lift source connections, unless later separately reviewed records close them.
- The listed finite-slope/crystalline deformation inputs, generic-fiber regularity and the exact eta-map supplier. This review checked their use, not their whole proofs.
- Patching, minimal-level inputs, the separate supercuspidal minimal-type theorem, classical local-global compatibility, and all other predecessor obligations.

SC01–SC05's independent decision remains separate. SC10, full C10, all Hu–Tan/Pan cases, the final manuscript and release are not accepted here. No source-version gap is transformed into a mathematical closure claim. The proposal's shorthand “Jacquet dimension two” must retain the smooth/normalized J_0 interpretation above in any future integration.

The checker validates seven target records, eight source PDFs and their extraction hashes, the earlier SC01–SC05 review pin, and exact ranges read. Its initial execution exposed a reviewer schema-key assumption (`applications` instead of `cards`); correcting that local reader did not change any target byte. These checks provide reproducible bindings, not a substitute for the mathematical reading.

Official publication records used: [Colmez, Astérisque 330](https://www.numdam.org/item/AST_2010__330__281_0/) and [Berger–Breuil, Astérisque 330](https://www.numdam.org/item/AST_2010__330__155_0/).
