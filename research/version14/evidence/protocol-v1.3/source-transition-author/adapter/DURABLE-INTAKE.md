# Durable audit intake candidate

This component records actual collected GitHub material and all reports in the protected operator ledger, retains their historical revisions, and checks that every retained item has an explicit operator-recorded classification. Registered findings cannot disappear from the candidate. It also preserves authenticated complete-manifest provenance. It does not yet create a `VerifiedContext`, select independent acceptance receipts, publish a check, or authorize a merge.

The new files are `audit_intake.py`, `audit_intake_store.py`, `durable_intake.py`, and the bounded live compatibility probe `probe_github_payloads.py`. Accepted components remain unchanged. The test runner binds exact files and records the tests; independent review is required before accepting this candidate.

## Trust and storage

The recorder runs under the same explicit isolation requirement as the accepted store. Its code, configuration, keys, configured reader/transport, collector signer registry, databases and external current checkpoints must be outside candidate control. Path checks prevent configuration mistakes; they do not install OS permissions or isolate an account. No production key or intake database was created here.

The intake log has a distinct `research-audit-intake/v1` HMAC domain. Each signed entry binds its ledger ID, position, preceding entry hash, operator identity and complete event. The configured key registry authenticates the operator. It does not attest to a model provider or prove that an operator classification is mathematically correct.

`AuditStore` is a separately versioned derivative of the accepted store. It uses canonical records, SQLite transactions, expected-checkpoint compare-and-swap, and the separately trusted current anchor. It adds bounded database reads and reports a recoverable committed checkpoint if advancing the anchor raises an exception. The limits are 10,000 entries, 32 MiB per signed entry, and 256 MiB total canonical signed entries. Exceeding them blocks the operation; there is no silent archive eviction or incomplete success.

Database commit and anchor advance are not a distributed atomic transaction. An interrupted advance blocks reads until explicit forward recovery verifies both the old trusted prefix and the signed tail. Restoring the database alone behind its current external checkpoint is detected. Restoring both database and checkpoint to an old matching state is outside the guarantee. Backups do not become rollback-protected merely because they contain signed entries. Operator-ledger and intake-ledger checkpoints are checked before and after reconciliation; the two stores and GitHub do not become one atomic transaction.

## Capture and full-manifest provenance

`IntakeRecorder.capture` first verifies each complete manifest with the accepted manifest-transport verifier. The expected numeric repository ID comes from protected reader policy; the collector code SHA-256 and allowed signer keys come from protected recorder configuration. A candidate cannot replace them with its own values. The signed envelope binds the full canonical manifest, including every raw SHA-256, size, mode and Git object ID. This closes the gap where Git tree matching alone cannot authenticate unused raw-digest metadata.

Only an actual isolated full collector may hold a collector signing key. The accepted `seal` function by itself does not prove that a caller read every blob: possession and correct use of that key are part of the trusted collector boundary. Candidate-generated envelopes or a collector code hash asserted by candidate JSON do not establish that boundary.

The recorder then invokes the configured GitHub reader directly. It has no argument for importing an unsigned saved GitHub observation. The configured reader and transport are executable trusted dependencies, not a `verified` boolean. The recorder reads the complete operator-ledger report inventory from its verified current store, including negative, self-authored and superseded reports. It checks that store again before and after the durable append.

The signed capture retains the observation, report inventory and checkpoint, exact packet digest and schema-2 binding, and both full-manifest canonical hashes and authenticated transport envelopes. The original candidate manifests remain external content-addressed inputs. A later reconciliation requires the same exact packet and re-verifies its manifests against the saved envelopes and current configured collector keys and code hash. Removing a trusted collector signer therefore blocks reconciliation rather than silently preserving its authority.

`AuditObservationSource` offers an archive-only path using the accepted reader's origin, approved-source, complete-pagination and pre/post state checks. It does not request CI and explicitly says `ci_evaluated: false`. This lets the recorder preserve objections while CI fails. It still conservatively requires a valid configured open PR, exact base/head/merge state and approved policy sources. The normal accepted reader can also be used when a complete strict CI observation is wanted. Neither form makes the intake result a successful live-gate decision.

## Historical material and findings

A material identity includes its source and complete canonical record digest. Edited GitHub comments become additional revisions. Previously captured text remains when a later snapshot omits a deleted comment. Every captured report from the protected operator ledger likewise remains, including old negative decisions after a new positive report. Explicit `external_registered` events retain audits conducted elsewhere, their source identity, original body and the operator's observation evidence.

This history starts with what the recorder actually observes or what a trusted operator explicitly registers. It cannot recover a comment deleted before any capture and cannot discover an unregistered external audit. Deployment still needs an explicit registration policy and cutoff. No statement of complete historical or external discovery is made.

`finding_registered` preserves the original finding body and links it to existing material IDs. A registered finding ID cannot be overwritten or removed. Corrections and duplicates remain explicit candidate dispositions. Each material revision must receive a `classified` event, with original operator observation evidence, a reason, and either the exact linked finding IDs or an explicit empty list meaning the operator found no finding in that material.

The classification context commits to the exact candidate packet, repository/PR/base/head binding, current operator checkpoint and full report inventory, complete accumulated material history, and registered finding set. New material, new findings, changed packet contents or changed operator state invalidate previous classifications. Repeated identical capture and deletion of already archived material do not discard old text or require a fictitious new finding.

Reconciliation requires every historical material item to have a classification for the current context. Every registered source/finding link must appear in that classification. The candidate's finding set and original body hashes must match the registry exactly, and each finding needs a disposition and reason. The accepted schema-2 core will still have to check independent receipts, detailed disposition rules and downstream dependencies in the later bridge integration.

Source classification is an explicit trusted-operator semantic act. It is not inferred from CI, a reviewer name or a candidate flag, and this module does not independently prove that an empty finding list is correct. A deployment must review that intake mapping as part of the complete audit procedure. The current candidate deliberately leaves `verify_context` unimplemented, so this remaining semantic and receipt integration cannot be bypassed by plugging an intake-consistency dictionary into the bridge.

## Live compatibility observations

The bounded probe imports the existing version7 GitHub helper only after checking an explicitly supplied source hash. It obtains the existing operator credential through that helper and uses the accepted fixed-host, bounded GET client. It performs five read-only requests: repository, one run-list page, that run, its workflow, and one attempt-specific job page. It neither logs nor writes the credential. Response digests and selected nonsecret shape fields are saved; the JSON output is an unsigned observation record, not a portable authenticated receipt.

Approved read-only escalation succeeded for both repositories. Sampled push runs 42436243502 and 42436248846 had `.github/workflows/research-checks.yml` as both workflow and run path, with `run_attempt` present on all 11 jobs. This supplies concrete evidence for those two previously uncertain payload-shape assumptions. The sampled public PR run 42384892642 had no jobs and an empty PR-association list, so the strict accepted reader would reject it. No weaker PR-association rule was introduced. These bounded samples do not establish full current-PR gate compatibility, complete CI evaluation, or future API behavior.

`GITHUB-COMPATIBILITY.md` remains preserved as the earlier review's uncertainty statement. New live summaries retain observation times and probe-source digests where available. They do not constitute deployment acceptance. Current basic GitHub protections remain unchanged; the full protocol gate remains inactive.

## Reproduction and outstanding integration

Run `python -B test_durable_intake.py` or `python -B run_intake_checks.py` in this directory. Tests create temporary stores and fixture keys only. They cover exact collector authentication, unused raw-digest tampering, retained edits/deletions/negative reports, explicit external registration, stale classifications, every registered finding and source link, current checkpoint changes, interrupted anchor advance, tampering and resource limits.

The remaining live integration must protect actual operator/agent observation capture, bind a fresh GitHub snapshot to the final reconciled intake and selected independent receipts, invoke the existing complete schema-2 check, and handle freshness immediately before publication. The separate App publisher, deployment isolation and any reviewed extension to existing rulesets remain outside this component. Every returned result retains `merge_authorized: false` and `deployment_eligible: false`.
