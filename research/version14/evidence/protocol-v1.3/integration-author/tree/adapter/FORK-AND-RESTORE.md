# Fork reader and remote-authoritative restoration candidates

These are separate additions. They preserve the accepted same-repository reader, stores and intake modules. They have not yet been integrated into the frozen same-repository live evaluator or approved for deployment.

## Fork-capable reader

`github_fork_context.ForkReadContext` inherits the accepted reader's fixed-host GET transport, pagination, full-manifest origin binding, approved source checks, strict success rules and repeated observation. It overrides only `state` and `ci`.

The base repository remains exactly the protected numeric ID and owner/name. The PR response supplies the actual head repository ID and full name; missing, noninteger or malformed identity fails. For both same-repository and fork PRs, the reader additionally retrieves `git/ref/pull/N/head` and `git/ref/pull/N/merge` from the **base repository**. Each returned exact ref name and commit SHA must match the PR's current head and merge values. It reads head commit/tree/blob objects through that same base repository, never a candidate-provided URL. The merge commit must still have the exact current base/head as its ordered parents.

CI runs must belong to the protected base repository and associate the exact PR, base and head commits. The run's head-repository identity and its PR association's head repository must now match the authenticated fork ID rather than incorrectly requiring the base ID. All other workflow, source, latest-run, current-attempt, job and step-success requirements remain unchanged. An empty association, absent jobs, wrong fork, stale base or unapproved workflow still fails. No fork code executes in this process or with its credentials.

The extra authenticated fork identity and pull-ref bindings remain in the observation. Existing schema-2 records still bind the base repository/PR and exact base/head commits, trees and manifests. A change in fork origin during evaluation changes the full observation and fails freshness comparison.

Actual bounded authenticated GETs on 2026-11-07 confirmed `refs/pull/5/head`, `refs/pull/5/merge`, `refs/pull/6/head` and `refs/pull/6/merge` in the public base repository, and that its commit endpoint resolves both fork head objects. `live-probe-20261107/fork-refs.json` records selected fields, observation times and source/response hashes. This is an unsigned producer observation, not a transferable receipt. It establishes endpoint availability for those samples, not successful CI or an eligible protocol review. The sampled PR workflow previously had an empty association and no jobs, which remain a correct rejection.

Run `python -B test_github_fork_context.py`. The suite covers authenticated fork success and same-repository success, wrong/missing fork identity, exact head/merge pull refs, fork-specific run/PR provenance, plus inherited strict origin, policy, CI, intake and freshness regressions. Publisher check target selection remains a separate reviewed component.

## Restoring verified working stores

`restore_verified_stores.py` supplies:

```python
operator_store = restore_operator_store(location, remote_anchor, signed_entries, keys, expected_checkpoint)
audit_store = restore_audit_store(location, remote_anchor, signed_entries, keys, expected_checkpoint)
```

The anchor implements authenticated `read()` and `compare_and_swap(expected, replacement)`. Its current state is authoritative and must be provided by the trusted remote-state adapter. This helper never initializes, lowers or substitutes a remote checkpoint. It verifies the complete signed entry chain against that exact current checkpoint before creating a local file, checks the anchor again before installation, and makes a final verified store read afterward.

The local SQLite database is an ephemeral verified working copy. It is created in a new temporary file beside the intended destination, populated in a full synchronous transaction, closed, and installed using an atomic hard link that refuses an existing destination. A filesystem lacking that operation fails; there is no replacing-rename fallback. Only the exact temporary file is removed afterward. If the remote anchor advances after installation, the final read rejects the stale local copy. The stale file is retained for inspection and is never treated as authority.

The returned ordinary accepted store still uses the supplied remote anchor for every verified read and append CAS. A remote advance invalidates a stale local mirror. After a local append, the existing store's transaction/anchor-advance recovery contract applies; the controller must durably transport the signed entries and advance the authoritative remote checkpoint together according to its separately reviewed state protocol. The helper does not claim to implement that remote transport, provider authentication or cross-store atomicity.

The owner/controller and source/configuration remain trusted, and unreviewed candidate code must not execute with their credentials. Restoring both signed entries and an old matching checkpoint from candidate JSON would violate the required trusted-current-anchor contract. No database backup is claimed rollback-proof without that external authority.

Run `python -B test_restore_verified_stores.py`. Tests use fixture keys and in-memory remote anchors, with real temporary SQLite mirrors. They check valid restore/append, wrong or advanced remote checkpoints, tampered entries, no remote initialization, atomic refusal to overwrite, cleanup on install failure, correct log domain and final-read rejection after remote movement.
