# Independent publisher core review

Reviewer: `/root/astra_bl_synthesis`. Date: 2026-11-07.

Decision: accept the exact frozen core packet under its stated trusted-process, injected-transport contract. I found no unresolved defect within that scope. This is not acceptance of a deployed protocol gate. The publisher packet contains the core, SQLite generation state, documentation, and tests. It does not contain an authenticated GitHub transport or the deployment's remote generation authority.

Author freeze `publisher/MANIFEST.json` has SHA-256 `6a85426d03f673884a0551ad4dc766f902bd6e1d35e2cc108483607b9fb5fee9`. I checked every listed file against this manifest and reviewed its README's exact interface obligations and limitations. The frozen README has SHA-256 `339b9f7714c7a3e815c8880a47edfa9ed18b418a32b4e9af15258a267efd0985`.

| File | SHA-256 |
|---|---|
| `publisher/app_publisher.py` | `c0cd99c177e414e0b71ad3094c04588dd1f3094c729c92d7202c315f44a30c23` |
| `publisher/generation_state.py` | `ebd4ac0433d3a3af2991e0344b269b82a6af3345b39051138b13383f404d9ab8` |
| `publisher/test_publisher.py` | `f714dabba3cc6070905adf81e6ad78da8968aa033452cef4812e1cf6e1064974` |
| `publisher/test_live_integration.py` | `3f71da3ccf30bc3e976e77db7a0f2252de8ad35958bf5469dbd7f7af09f662a6` |
| `adapter/live_protocol_context.py` | `2fd3449f3af9affbe6ee730dd5a9157361907bae064dee21b07f82c9331465c2` |
| `DEPLOYMENT-DECISION.md` | `d3d5e5aeea47920e7a4fa1475d087f8a2e9d05da75ddf8770afa5774c0d9b0c9` |

Paths are relative to `work/protocol-ruleset-20261107`. `CHECKS.json` records these pins, the additional controller source inspected, reviewer test pin, and test-log hashes. `run_review.py` reruns the tests and rejects a source change during the run. No remote mutation, credential loading, or candidate execution occurred in this review.

## Binding and publisher ownership

The public entry point accepts a head SHA and expected generation. It obtains a live evaluation internally rather than accepting portable result JSON. The production runner calls the actual live evaluator, whose session recheck rereads GitHub state and verifies both protected stores. The publisher checks repository and PR identity, base/head commits and trees, schema, policy and complete-manifest digest presence, observation binding, merge commit and tree, readiness, and base branch. The session fingerprint incorporates the packet and observation digests and both store checkpoints. These fields are also committed through the authority's pre-success barrier.

This is a trusted-process boundary. Python session types, injected runner methods, and typed transport responses are not a sandbox against hostile code inside the controller. The deployment decision correctly keeps candidate execution and candidate imports out of that process. Tests with fake sessions exercise the publisher's field checks; the separate integration tests call the actual evaluator and protected fixture stores.

Before every mutation, the core checks the exact numeric App, installation, and repository identities. It lists only its own exact check name for mutation and rechecks ownership by check ID before updates. Foreign Apps' same-name checks remain untouched. Duplicate own named checks are invalidated and block acceptance. The write response must match App, target SHA, name, ID when updating, status, conclusion, and generation-specific external ID.

These checks depend on the real transport authenticating its actual credential. The core has no code to prove that a supplied `AppIdentity` came from GitHub. Deployment configuration must bind the created App ID 5663093 and its verified installation/repository IDs. The fixture values 42 and 43 are deliberately test identities.

## Freshness, PR ambiguity, and publication targets

The core requires exactly one current open PR using the head SHA, including PRs targeting other bases and drafts in the inventory. A second such PR blocks publication. It compares the whole current context again before success and immediately afterward. The final session recheck rejects changed observations, changed intake/operator checkpoints, and a changed evaluated identity.

Merge-target mode requires an explicit nonempty CI policy. It checks each named CI context from its configured App on that exact merge SHA, using the highest check ID among matching runs, and requires completed success. A head-only CI result cannot satisfy that test. The live evaluator separately retains its stricter workflow provenance checks. The controller must supply the intended eleven contexts and verify its real inventory's ordering and rerun behavior; the core permits other protected configurations for testing and reuse.

The choice of target matters. GitHub documents that when the test merge has a status, its checks govern the PR; otherwise head checks govern. GitHub also permits required checks to be restricted to a particular App. Consequently a live merge-target compatibility test with the eleven existing contexts remains necessary. [GitHub required-check troubleshooting](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks).

The core invalidates known old merge targets and the legacy head target when beginning a new generation. Its history is keyed by head SHA. The controller must therefore revisit previously recorded heads after a PR changes head or closes. Polling only current PR heads would leave old recorded targets unreconciled. The controller must also define how it handles an ambiguous network outcome; returning `published_success=false` locally does not undo an already-applied remote success.

## Generation and durability boundary

SQLite compare-and-swap advances the local generation and token. Each mutation commits an intent before obtaining a write transaction that serializes the final reads and remote write within that local state instance. A stale generation cannot perform a new mutation. Missing state is rejected, existing state cannot be initialized again, and partial malformed snapshot restore rolls back atomically. Target history survives a trusted restore.

The remote authority is mandatory and must raise on rejection. Returning an untrusted boolean does not authorize success. The core calls the authority before mutations, commits the pending snapshot and publication identity through `before_success`, and checks currency again before and after publication. The local authority is explicitly unsuitable for ephemeral runners.

These are interface obligations, not a completed remote durability proof. The deployment's implementation must authenticate the controller state ref, enforce expected-tip compare-and-swap, restore the exact publisher state, preserve known targets, bind the approved controller revision, and reconcile interrupted mutations. The inspected Git state helper is a separate lower layer; no integration of it into the publisher authority is present in this snapshot.

GitHub check writes and state-ref updates are separate transactions. A comment, base change, or generation change can happen after the final read. The code detects changes observable in its immediate post-write checks and attempts revocation. A transport outage after a successful remote mutation yields `uncertain` with revocation unconfirmed. The deployment decision correctly makes no instantaneous invalidation or atomic comment/merge guarantee. A newer generation must reliably reconcile prior targets; the core's `superseded` return does not itself revoke them.

## Verification and remaining deployment evidence

All 34 author core tests, four real-evaluator fixture integration tests, and 18 reviewer-owned adversarial tests pass. The reviewer tests cover wrong installation/repository identity, incomplete inventory types, duplicate and draft same-head PRs, altered merge trees, boolean identity confusion, altered live observations and checkpoints, duplicate own checks arising during evaluation, wrong write responses, barrier ordering and exact target snapshots, authority supersession, newer queued CI, CI failure after a success write, missing local state, and atomic failed restore. The reviewer tests reuse the author's fake fixture classes but contain separate assertions and failure scenarios. They make no real network calls.

Before deployment acceptance, the remaining evidence must cover the actual App credential and repository installation, complete pagination, strict merge-parent/current-ref checks, remote authority integration, and the controller's trusted inputs and secret isolation. GitHub's check-run endpoint defaults to a filtered latest inventory; the transport must explicitly request the complete inventory needed by duplicate detection. It must also verify the actual update behavior when moving a completed run back to `in_progress`; the fake transport assumes the old conclusion is cleared. [GitHub check-run API](https://docs.github.com/en/rest/checks/runs).

A frozen real transport/controller packet and its live readback remain outside this assessment. This report can support their review, but cannot substitute for it or for verifying the enabled rule's exact App binding.
