# H-D5 comparison-representation clarification

Reviewer: /root. Author: /root/astra_v14_assertions_arithmetic. The object clarification was requested by /root/astra_v14_baseline_gaussian; I did not propose it. This is a separate independent check of that clarification, not a reapproval of Gaussian's entire local-period argument.

The exact target is h-d5-ramified-arithmetic-002, manifest 38c98e7f3a8dc7921bacfe93ea5d0cb39ae2d5f62ed2d3f306fa75ec3e591bf6, proof bbf66d6c3ab7452d511fd5934d3b4d80485e33c5658f0010c1f5b21cc9efbdc1. I read both proof versions, the explicit difference, the application record, the full Gaussian review, the previously reviewed U04 proof, and final Kisin pp.630-633. Page 633 was also checked visually in the final published PDF.

## Actual required objects

Final Kisin Theorem 3.3.5 begins with a target rho whose residual representation is modular, while rho itself is not yet known to be modular. Its local Barsotti-Tate property and determinant are hypotheses. The proof constructs an eigenform f with residual representation isomorphic to the restriction of the target's residual representation. It does not assert an initial characteristic-zero isomorphism rho_f = rho. Later changes of form and field preserve specified residual and local information; the final modularity conclusion comes only after applying Proposition 3.2.9.

On p.630, the local assertion about a p-divisible group and the assertion about semistability of a special form both explicitly concern the representation attached to the chosen eigenform f'. The subsequent type changes on pp.631-632 concern new eigenforms. These are precisely the modular comparison representations to which H-D5 may apply Skinner's theorem before the final modularity result.

The successor now names rho_f and rho_g as those comparison representations. For a fixed comparison form pi, its already attached arithmetic representation and r_pi = rho_pi^vee from U04 have the same characteristic-zero Hecke polynomials at almost all places, with the same coefficient embedding. Chebotarev and the retained characteristic-zero character criterion identify their semisimplifications. The residual nonsolvability assumption supplies the irreducibility needed to identify the actual two-dimensional representation. Restricting this global isomorphism allows the new local comparison theorem to be used on that same modular representation.

None of this reasoning identifies the target rho with a modular representation from residual equality alone. Such an inference would be invalid. The explicit successor excludes it and retains the target's separately supplied local hypotheses. The theorem and its proof on final Kisin p.633 confirm that the target and modular comparison remain separate until the final lifting application.

## Decision

Accept the one-paragraph object clarification and the corresponding objects, hypotheses and exceptional-cases fields in the application record. It correctly identifies the object consumed by the local argument, preserves the target's independent hypotheses, and removes the potential circular reading without weakening the local conclusion actually needed for the modular comparison forms.

Gaussian's independently reconstructed period-module, inertia, monodromy and Hodge-weight arguments remain at their own exact reviewed scope. This decision covers the clarification that reviewer requested. It does not prove local automorphic base-change compatibility, ordinary/nonordinary type changes, the required field constructions, or the final modularity lifting theorem. Those remain separate obligations. No live manuscript or earlier record is modified.

The attached checks bind both proof versions, the final published source, the exact difference and the application fields. Their successful result establishes preservation and provenance, not mathematical correctness by itself.
