# Independent controller runtime review

Reviewer: `/root/astra_bl_synthesis`. Decision: accept the corrected frozen runtime as an implementation, with the deployment boundary below. The reviewed `runtime.py` has SHA-256 `39ec395c8d21227bd3709b1a909dd976fcb6cd2177837f5526c1290801c7c912`. `RUNTIME-CHECKS.json` binds every file and dependency in the author `RUNTIME-VERIFICATION.json`, the independent tests, and execution logs. No remote mutation or deployed credential was used in this review.

This acceptance includes the workflow template, bounded Git state composition, secret decoding, fixed fork-capable live profile, and actual entry-point path. It does not assert that production configuration, Linux dependency installation, deployed secrets, or the final ruleset have been exercised. Those need live deployment readback. The publisher core and real App transport have separate exact-file acceptances in this directory.

## Corrected environment and fork boundaries

The initial runtime decoded every key registry into raw bytes. The root reviewer identified that this was incompatible with the accepted operator codec. I confirmed that both operator and intake registries require attributed records, while the collector registry uses bytes. The earlier fixture tests supplied preconstructed keys and missed the environment path. That initial runtime is not accepted.

The corrected loader requires operator and intake entries with exactly `operator_id` and `secret_hex`, decodes them to `operator_id` and `secret` bytes, and calls the accepted codec's key validator. Collector entries remain hex strings decoded to bytes. Key IDs, attribution, encoding, and size are bounded. Missing attribution and bare hex operator/intake entries are rejected. Identity is preserved rather than invented from a key name.

The initial reader also only handled same-repository PRs. The corrected runtime fixes the fork reader and runner in protected code. The new `live_protocol_context_forks.py` differs from the accepted original only in its module description, import and dependency pin for the fork reader, and exact allowed reader types. It does not admit arbitrary subclasses or load a module named by a packet. The runner requires this profile's exact live session type.

I inspected the fork reader's state and CI methods. All calls stay in the base repository. It verifies base repository identity, authenticated head repository identity, pull head and merge refs, current base ref, commit/tree identities, and ordered merge parents. CI must be a successful `pull_request` run associated with the exact PR, base and head SHAs, and head repository. Workflow sources, attempts, jobs, and steps retain their strict checks. A fork-capable profile also supports same-repository PRs without giving them a different receipt path.

Four reviewer-owned entry-point tests invoke actual `main()`, protected JSON parsing, `load_job`, environment decoding, signed-store restoration, live evaluation, publication, and final durable state. Only HTTP/control API and App signer/transport are replaced. The success case uses a fork fixture. Negative cases reject bare intake keys, changed operator attribution, and an unapproved controller revision before loading the App key. Candidate subprocess execution and real HTTPS are disabled in this test.

## Remote generation authority

`RevisionGuard` requires the approved main commit, expected private controller repository, exact repository ID, and an allowed dispatch/schedule event. It authenticates current remote main repeatedly. A stale controller cannot advance state merely because its local environment still names an approved SHA.

`RemoteState` loads the authenticated `protocol-state` ref through the bounded Git store, requires exactly the operator, intake, and publisher checkpoints, and uses the remote commit as its compare-and-swap cursor. Signed ledger restoration checks complete sequence inventories and canonical bytes. The publisher snapshot is selected by an exact content digest. SQLite files are disposable verified mirrors.

`RemoteGenerationAuthority.begin` verifies the next generation and preserves unrelated generations and historical targets. `before_success` commits the complete pending publisher state, approved controller revision, and publication identity before the App mutation. `assert_current` checks both remote state and the active lease. `finish` commits the resulting local state. Earlier publication snapshots remain immutable in the Git history and state inventory. This is one authoritative ref with signed records, not independent rollback protection; administrative rollback remains outside the threat model.

The reviewer tests inspect the actual remote snapshot from inside the fake App success operation and confirm that the pending state and exact target identity already exist. They reject a substituted snapshot pointer, surplus ledger entry, stale remote cursor, remote advance after the barrier, and a new comment after the barrier. Read-only ledger anchors reject observation append attempts. A fresh ephemeral directory resumes the recorded generation through the author's restart test.

The workflow's single global concurrency group with cancellation disabled complements the CAS checks. It avoids ordinary simultaneous publisher jobs in this controller. CAS still rejects an unexpected external state writer. A state-ref advance or unavailable backend may prevent revocation after an already-applied App write; that remains an uncertain outcome requiring reconciliation, not a confirmed rejection on GitHub.

## Isolation, workflow, and head targeting

The controller token only accesses the configured private controller's bounded Git endpoints. The App credential is passed to the separately reviewed transport and cannot write controller state or mathematical contents. Candidate trees are read through verified Git blobs; the runtime has no candidate checkout, import, script execution, or subprocess path. Protected JSON paths reject traversal and symlink escapes.

The workflow checks out the approved controller commit with a pinned action and no persisted checkout credentials, submodules, or LFS. It installs only hash-locked binary wheels into a fresh environment, and exposes the App and ledger secrets only to the evaluation step. I checked the dependency lock against its included source inventory and target markers. Executing those Linux wheels remains a deployment check, as the author's freeze explicitly states.

Explicit production head mode is acceptable under the stated polling cutoff, trusted-owner model, and retained strict up-to-date requirements. It preserves compatibility with the existing eleven head CI contexts. The publisher still binds live PR, base, head, manifests, policy, observations, and receipts, and rejects multiple current PRs sharing the head. `external_id` does not make a head check intrinsically PR-specific. A new PR or comment after the last read can precede the next polling observation; that limitation must remain documented. Merge mode would need all required contexts on its exact target and is not silently substituted.

Runtime jobs are protected explicit packet selections. A new unconfigured head has no successful protocol result. Operators must keep previously recorded heads available for reconciliation when configurations change or PRs close. The controller does not discover and evaluate every future PR automatically, nor does it generate or invent reviewer receipts. This is consistent with a required fail-closed check, but it is an operational constraint on trusted configuration updates.

## Test result and remaining live checks

The author runtime and Git-state suites contain 24 passing cases. Eight reviewer-owned remote-authority cases and four reviewer-owned actual-entry-point cases also pass. These tests use the real signed codecs, restored stores, fork evaluator, publisher, remote generation authority, and Git CAS implementation. They replace GitHub I/O and App signing, so they establish implementation behavior without claiming a live deployment.

No unresolved implementation defect was found in the corrected freeze. Before claiming an active full gate, verify the deployed source/configuration identities, approved revision, credential scope, state bootstrap and generation persistence, actual App check create/update readback, retained eleven CI requirements, strict up-to-date policy, and required protocol context bound to App 5663093. The runtime acceptance does not certify mathematical claims in the selected evidence.
