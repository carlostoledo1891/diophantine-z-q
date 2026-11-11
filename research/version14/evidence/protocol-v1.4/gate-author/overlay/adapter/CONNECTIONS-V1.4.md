# Protocol v1.4 recorded connections

This extension checks declared relationships and exact reviewer bindings. It cannot decide arbitrary mathematical implication, find all related arguments or detect every erroneous paraphrase. A successful result is record consistency within authenticated reviewer scope. It is not proof completion, deployment permission or publication authorization.

The schema2 packet, nine application obligations, full file manifests, direct dependency checks, source-first reconstruction, reconciliation, separate coverage acceptance, authenticated author identities, findings intake, assembly receipt and release requirements remain in force. The stable coverage application ID remains `protocol-v1.3-coverage`; it is an identifier, not a version claim.

## Trusted selection

Historical v1.3 profiles keep `schema: protocol-coverage-policy/v1` and `protocol_version: 1.3`, with their exact old governing document. They do not receive v1.4 status. A v1.4 profile uses `schema: protocol-coverage-policy/v2`, `protocol_version: 1.4` and adds `connection_record_path`, a safe repository-relative path. The exact uploaded governing hash is `3d16c4d58d030ff745460386b081eb21c8c0d3f375cbfb06c4f9777c235a12f9`. The existing runtime-policy hash remains required. Profiles come from protected controller configuration, never candidate data.

The coverage dossier retains all prior fields and adds `protocol14_record`, a head file pin at that protected path. Include this pin in the coverage application's files. Both substantive and non-substantive profiles require the record and explicit reviewer reports. Non-substantive mode preserves the existing unchanged-proof and policy/editorial-only constraints, has no connections and cannot clear a substantive mathematical failure.

## Supplemental author record

The exact top-level keys are `schema`, `profile_sha256`, `coverage_sources`, `connections`, `findings`, `scope`, `limitations`. Schema is `protocol-connections/v1`; profile hash is canonical JSON SHA256 under the existing `offline_manifest_gate.canonical` rule. Coverage sources equal the dossier's exact source pins. Required fields are strict; an `accepted: true` author field is rejected.

Every current dependency source-use has exactly one connection with these keys:

| Key | Meaning and check |
| --- | --- |
| `use_id`, `use_sha256` | Exact current source-use ID and canonical hash, including supplier and consumer. |
| `supplier_passage_role` | `statement`, `proof`, `construction`, `application`, `inline_derivation` or `computation_certificate`. A favorable `review` is not a supplier. The existing use binds the supplying location. |
| `available_assertion` | Standard ten-field assertion. Its statement equals the use's supplier statement. All details require mathematical review. |
| `needed_assertion` | Exact equality with the current use's ten-field required assertion. |
| `required_capabilities`, `available_capabilities`, `derived_capabilities` | Unique string IDs for declared required properties and their supplied/derived support. Required IDs must be covered by the union of the latter lists. IDs must be explained in the reviewed contracts; they are not theorem-prover predicates. |
| `connecting_derivation` | Keys `kind`, `location`, `application_id`, `output_assertion`. Kind is `identification`, `derivation` or `reviewed_lemma`. Output assertion equals the required contract. Identification also requires available equals needed, with no derived capabilities. |
| `adverse_cases` | Keys `status`, `reason`, `evidence`. Status `checked` or `not_applicable`; application-specific reason and a nonempty list of exact evidence locations. |
| `consumer_locations` | Exact ordered locations for every passage listed by the current source-use entry. |

The ten assertion fields are `statement objects hypotheses quantifiers parameter_range uniformity constants normalizations exceptional_cases limit_order`. Location objects remain `pin start_line end_line excerpt_sha256`; bytes are verified without normalization. Locations must belong to current application-bound files. A named derivation application must be the matched use application or a direct dependency of its consumer. A null application must match the exact inline argument. Required capability coverage detects a declared missing endpoint or uniformity property, not whether the declared capability is mathematically true. The independent report must assess that implication.

Every tracked finding, including duplicates, rebuttals and scope findings, has exactly one review record. Its keys are `finding_id finding_sha256 classification mechanism search_scope scope_reason exclusions occurrences correction limitations`. The finding hash binds its current disposition and applications. Classification is `substantive_failure` or `not_substantive_failure`; missing classification cannot exempt an objection. Nonempty exact search locations, a mechanism, scope explanation and limits are required. Exclusions have `location reason`.

Each occurrence has `id use_ids location inclusion_reason disposition evidence`. IDs refer to known dependency uses. Disposition is `justified`, `corrected_reviewed` or `inapplicable`; open required occurrences fail. A substantive failure requires at least one occurrence and substantive mode. Evidence locations are nonempty. The reviewer separately assesses whether the bounded candidate list is complete and whether exclusions are justified. This code does not perform that search.

Every `repaired` finding requires a correction. A correction has `rejected_assertion current_assertion canonical_location representations scope limitations`. The two assertions must differ. Each representation has `id location status recorded_assertion reason`; status is `current` or `retired`. Every current recorded assertion must equal the canonical current assertion, and the canonical location must be among current representations. Retired representations remain explicit. Exact matching detects declared stale copies; the reviewer compares actual mathematical meaning, including copied fields and linked proof text. The validator cannot find undeclared copies or dishonest paraphrase labels.

## Independent report format

The existing authenticated coverage receipt and assembly receipt must point to separate exact JSON reports. The normal ledger authenticates report bytes, author identities, target/dependency hashes and candidate snapshot. This extension does not introduce an unauthenticated acceptance channel. Raw `check_records` remains an unverified structural preview.

Each report has `schema scope limitations decisions`, with schema `protocol14-review/v1`. A decision has `subject subject_sha256 outcome review_basis prior_review scope limitations`. Outcome must be `accepted_within_scope`. Review basis is `reconstructed` or `reused_exact_derivation`; the latter requires an exact checked prior-review file pin. The prior report's applicability and independent acceptance are reviewer attestations, not inferred from the file's existence. `consistency_only` is allowed solely for nonfailure finding classifications and non-substantive inventory/assembly decisions. It cannot accept a substantive connection.

The coverage report must contain exactly `connection:<use_id>` for every connection, `finding:<finding_id>` for every finding review, and `inventory`. Each individual subject hashes its exact corresponding object; inventory hashes the complete supplemental record. The assembly report has exactly `assembly`, hashing that same complete record. The coverage reviewer already must be distinct from every ordinary application author; the assembly reviewer is subject to the existing full authorship exclusion. Ordinary application and finding acceptances remain separately required.

No existing verdicts are refreshed or converted automatically. An author prepares records; the reviewer supplies the exact new report. Old accepted derivations may be reused only at their precise scope, with the prior report pinned and the changed context assessed. Missing mathematics remains pending outside a passing closure packet.

## Integration and limits

The operator must bind the extended profile, new record and reports to the final reviewed candidate. Add the new module and document to the controller bundle manifest. Retain v1.3 source and evaluations as history. Keep release-maintenance artifacts, full source inventory, computational certificates, truthful open status and final assembled-proof review in their existing application/receipt chain. This module does not replace any of them or claim to have independently checked a current research proof.
