# V14 protected-controller preparation

This is an author proposal for independent review. It is not a live controller configuration or gate result. No source commit, PR number, report identity, observation, approval or check result has been invented. The files named `*.template.json` intentionally contain `$required` markers and are not deployable. Runtime anchor: 268cc244786568f4a63a02ca1108ad81c2763937. All imported implementation files are pinned in RUNTIME-PINS.json.

## Known versus unbound

The public/private repository identities, App5663093, installation179741595, governing protocol1.4 digest and existing signer key IDs come from the deployed source and operation record. The substantive gate profile is `protocol-coverage-policy/v2`; it is NOT the public `RELEASE-PROFILE.json`. The stable coverage application ID remains `protocol-v1.3-coverage` even for1.4. Do not rename it.

KNOWN-RECORDS.json freezes a bounded set of existing arithmetic/assembly inputs. They are source records, not automatically final-target ledger acceptances. This is not a complete proof inventory. Complete claims/proof paths, final source applications, coverage dossier, connecting records and related findings must come from the independently reviewed current inventory. The profile uses substantive mode and cannot hide mathematical changes behind a non-substantive classification.

## Binding inputs

Copy bindings.template.json to a new reviewed input location. Every inputs entry must be an exact raw `{path,sha256,bytes}` pin relative to `--input-root`. JSON roles are:

- pull_request: original authenticated GitHub PR readback, with actual open number, base/head SHAs and repository identity.
- base_manifest, head_manifest: full manifests from the deployed `adapter/git_manifest.py`; the binder independently recollects both from the local repository and compares canonical full objects. No candidate program is executed.
- applications, changes, findings: reviewed schema2 lists. Every change needs explicit application ownership. No automatically favorable obligation is generated.
- policy: actual reviewed TrustedPolicy, including the old runtime policy identity and reviewed source_transition where needed. The governing protocol digest is a different field.
- profile_scope: complete claim_ids, proof_paths and connection_record_path. Their coverage review is mandatory input; the binder does not infer completeness.
- selected_reports: exact target-name to actual observed report-ID map, including every application/finding and assembly:complete.
- existing_operator_events and new_operator_events: ordered actual run_observed, target_frozen and report_observed events. Retain negative and superseded reports. Existing events are only used for local consistency; only new events go in the proposed ingress batch. The deployed signed history remains authoritative.
- external_materials, intake_findings, classifications: new actual ingress records only. An empty list is permissible only when the actual intake warrants it; never synthesize no-finding classifications. Every supplied entry needs its original observation bytes.
- finding_inventory: actual full intake list of `{id,body_sha256}`, separately checked against all packet findings.
- required_merge_ci: actual protected check-name/AppID list for the selected target mode.

scope_review, policy_review and observation_provenance are pinned original text records, not boolean approval fields. They need independent review of their contents. The script verifies their presence and bytes, not their truth. Unknown model metadata or absent original captures must be resolved from actual records; no placeholder model or newly composed observation may replace them.

The exact observed freeze targets can be computed with the existing `ledger_evidence_bridge.targets(packet)` and `offline_manifest_gate.binding` routines. Obtain the actual final-target reviewer observation after this identity is known. Do not rewrite an old observation's binding to make it match. The accepted report body must already be a byte-identical file in the source tree; protected observation events can bind that body to the final source without introducing a circular source-commit hash.

## Command

`python -B bind.py --bindings REAL_BINDINGS.json --bindings-sha256 REAL_SHA256 --input-root INPUT_ROOT --repo SOURCE_REPOSITORY --deployment PINNED_CONTROLLER_CHECKOUT --output NEW_OUTPUT_DIRECTORY`

The binder rejects required markers, duplicate keys, changed input/runtime bytes, absent original observations, stale target/dependency/source bindings, self-review, superseded selections, missing source-tree report bodies and local full-manifest mismatch. It runs the existing offline record, coverage and connecting-record checker using explicitly UNVERIFIED supplied observations, then the protected runtime job loader. Those local checks never authenticate the observations or replace real ingress and evaluation. The result retains `authentication: NOT CHECKED`, `merge_authorized: false` and `deployment_eligible: false`.

Output is an unsigned single-job PROPOSAL with packet, selected reports, inline profile, ingress batch, exact input pins and structural result. Review it independently. Do not overwrite a later controller config containing other jobs with this single-job proposal; preserve active jobs through an explicit reviewed integration. Signer key availability is checked by the deployed runtime, not by local secret inspection. The script reads no credential configuration and creates no keys or approvals.

## Remaining protected operation

After the actual reviewed proposal is integrated into private controller main, use the existing approved-revision process. Dispatch existing protocol-ingress.yml with the new exact batch path, then evaluate with operate_controller.py. Do not use that helper's old hardcoded ingress-public/private shortcuts. Capture/finalize selection follows actual intake state; finalize still performs complete durable reconciliation. Real source-policy, live CI, App, current comments, signed histories and state-cutoff checks remain with the deployed controller. No command here dispatches, publishes, pushes or modifies rulesets.

Keep post-gate results outside the source commit and bind them through R10's external bundle. A later source/PR-head change requires the corresponding new binding and gate evaluation; never relabel a historical passing result.
