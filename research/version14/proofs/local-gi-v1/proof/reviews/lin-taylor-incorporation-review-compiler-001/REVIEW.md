# LIN Taylor-coordinate incorporation review

The proposed replacement of the proof of `lem:Pi` faithfully incorporates the reviewed finite-Taylor construction. Its exact replay and input checks are recorded separately. This is a bounded source-incorporation decision, not a whole linearization approval.

The full proposed proof and its surrounding text were read directly. It preserves the increasing-order Taylor recovery, the power-map proof of smooth exponential coordinates, the weighted tangent-space identification and the pointwise bracket and exponential. The added terminal case follows from the trivial zeroth group of the shifted filtration. The subgroup clarification uses finite BCH and uniqueness of the connected subgroup with its Lie algebra. Smoothness into the prescribed subgroups uses their embedded charts.

The corrected contract explicitly restores the connectedness already required by the original setup. It preserves the old assertion separately and changes only the hypothesis, normalization and constant fields. The step bound is the nilpotence class of G; no class(P_0)<=s assertion is introduced. The ordinary BCH identification and basic local Lie/calculus inputs remain explicit. The subsequent real-clock integration, lattice, metric and limit arguments remain separate.

Compiler contributed the finite-evaluation embedding justification and does not independently approve that proof step here. Its exact mathematical input is the complementary SourceReview decision b4586a68273ca00a55218cd528be113ee1c48cc5f071829972364076217926e7, whose complete report was read. Compiler's separate remainder review is 103117397d90fc005aabce28c5b11f3c070966933d7d7912dcc758bc04a8f7e2. This review checks their faithful incorporation and the stated new clarifications. It does not convert either component decision into a whole-proof or whole-source approval.

No live source was changed. Publication, downstream source transport and compilation are outside this decision.
