# Fork-capable live evaluation profile

`live_protocol_context_forks.py` admits the same-repository reader and the fork reader. Both live profiles pin the reviewed reader sources. This revision uses the versioned PR-state projection described below while preserving the exact origin, required CI, intake, source and ledger checks.

Use the same `evaluate_session(packet, recorder, live_reader, selected_reports, blob_reader)` interface. For fork support supply `github_fork_context.ForkReadContext` as the strict live reader and use that same protected policy for the recorder's `AuditObservationSource`. Returned sessions retain defensive `.binding`, `.observation` and `.result` properties plus the repeatable, failure-latching `.recheck()` method.

The fork reader obtains the head repository identity from GitHub's authenticated PR response, verifies exact base-repository pull/head and pull/merge refs, reads all objects through the base repository, and binds CI provenance to the actual fork identity. The final observation retains the fork identity and pull refs. Its strict workflow/attempt/job requirements are otherwise unchanged. No fork code runs with controller credentials. Details and live endpoint observations are in `FORK-AND-RESTORE.md`.

The full evaluator still verifies collector signatures, current durable intake, exact independent operator receipts, all core obligations/dependencies and actual evidence blobs. Every final recheck repeats collector/intake reconciliation under current trust keys, rejects changed protected policy, repeats the strict full GitHub observation, and verifies both current checkpoints. It does not accept an unsigned JSON result as authority.

The test suite repeats every live evaluator end-to-end and race test with a fork head, plus exact fork identity/ref assertions and a changed-pull-ref failure. This is fixture coverage, not an assertion that current public PRs 5 or 6 pass the gate. The sampled actual PR run has absent jobs/association and correctly fails the strict reader. Independent review of the reader, profile and composition remains required before deployment.

`restore_verified_stores.py` is separately available to create ephemeral local mirrors under remote-authoritative checkpoints. A controller may restore those stores, construct the recorder and strict reader, then call this profile. Remote state transport, actual operator observation capture, the isolated publisher, success-check target/generation policy and ruleset activation remain outside this profile. Results continue to deny automatic merge authority.

## Versioned PR-state projection

The state record carries `projection_schema: github-pr-state/v3`. Both readers use it during capture, evaluation and every freshness check. At the PR response root, only `mergeable`, `mergeable_state` and `rebaseable` are excluded. Raw merge readiness is still checked separately by the publisher.

At the exact repository-object slots, the projection excludes repository-wide activity fields: `size`, `open_issues`, `open_issues_count`, `stargazers_count`, `watchers`, `watchers_count`, `forks`, `forks_count`, `network_count`, `subscribers_count`, `updated_at` and `pushed_at`. A star, fork, new issue or unrelated branch push can change these without changing the reviewed content. These counters and activity timestamps are not proof or CI identities. The saved capture and a subsequent owner-credential PR10 read differed only in star/watch counters and nested repository `updated_at`. The failed App read was not preserved, so this comparison does not establish its exact response bytes.

The repository slots are `pr.base.repo` and `pr.head.repo`, and each CI run's `repository`, `head_repository`, `pull_requests[*].base.repo` and `pull_requests[*].head.repo`. This applies to the selected run and collected run inventory. No arbitrary recursive stripping occurs. The `fork` boolean, identity, visibility, privacy, permissions, configuration and unknown fields remain. The PR's own timestamps also remain.

Title, body, draft/open/merged state, labels, requested reviews, users, commits, trees, branch and pull refs, source pins, complete intake and current required CI retain their checks. All run IDs, attempts, events, associations, workflow identities, jobs and required success conditions remain checked. The publisher still requires raw `mergeable is True` at its readiness boundaries.

Signed older captures remain historical evidence. Do not edit or rehash them as v3 captures. This schema change requires fresh authenticated captures under the reviewed reader and dependency pins. Keep all original records, decisions and findings. New observations do not themselves accept changed semantic evidence.
