# Revision 3 implementation wording

Author /root/sol_protocol_policy_review. The six-document revision 2 remains unchanged at ../r2 with manifest SHA256 d9db42389044175f7b86b957d94473dd6b439d2b0311025069208054017171bc.

Only one paragraph in the contributor guide changes from revision 2. It replaces the preparation-time statement that the deployed earlier gate lacks v1.3 checks with the configuration required for a v1.3 acceptance. It does not claim that this configuration is already deployed.

Read the reviewed gate contract in gate-author/adapter/COVERAGE-V1.3.md, its independent GATE-REVIEW.md, and the prepared runtime-r2 controller path. The runtime accepts an inline protected profile, validates it against the packet, and passes it into the live evaluator. The coverage application and its authenticated receipt bind the dossier. The paragraph distinguishes the substantive record checks from non-substantive scope-only acceptance and leaves source completeness, chronology, prior-exposure truth and mathematical adequacy as reviewer attestations. It instructs the operator to verify the reviewed live configuration and result before merging.

All other five candidate documents are byte-identical to revision 2. The supplied normative protocol remains byte-identical to the owner's source, and exact historical v1.2 is preserved. No AGENTS, workflow-source pin, repository checkout, v1.2 rollout, commit or deployment changed. This narrow guide update awaits independent review before use in actual PR heads.

R2-TO-R3.patch shows the only repository-file change since the accepted revision 2. CHANGES.patch remains the full six-document diff from the frozen v1.2 baselines. The packet preparer accepts an explicit --document-manifest path; actual revision-3 preparation must use this manifest rather than an older default.
