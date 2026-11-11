# Isolated controller runtime

`runtime.py` composes the accepted signed-ledger restoration, fork-capable live evaluator and
App publisher with the remote `GitState` authority. It imports no candidate code.
The App transport is `publisher/github_app_transport.py`, maintained separately.
No live API calls have been made by this runtime implementation or its tests.

The private control repository contains the trusted `adapter/`, `publisher/` and
`controller/` code, protected packet data and explicit receipt selections. Only
the owner may write or dispatch it. Repository administrators and observation
operators remain trusted. No artifact upload, candidate workflow checkout,
candidate script, plugin, Python import or subprocess is used by the runtime.

## Configuration and credentials

`controller/config.json` is protected configuration with exactly these fields:

```json
{
  "schema": "protocol-controller/v1",
  "controller_repository": "elliotglazer/research-review-controller",
  "controller_repository_id": 123,
  "jobs": [{
    "id": "public-pr-example",
    "publisher": {
      "repository": "elliotglazer/diophantine-z-q",
      "repository_id": 1446122118,
      "app_id": 5663093,
      "installation_id": 123,
      "base_ref": "main",
      "target_mode": "merge",
      "required_merge_ci": [{"name": "ACTUAL REQUIRED CONTEXT", "app_id": 123}]
    },
    "policy": {
      "repository": "elliotglazer/diophantine-z-q",
      "repository_id": 1446122118,
      "base_ref": "main",
      "policy_path": "ACTUAL_POLICY_PATH",
      "policy_sha256": "ACTUAL_APPROVED_64_HEX_SHA256",
      "policy_paths": ["ACTUAL_PROTECTED_PATH"],
      "workflows": [{
        "workflow_id": 123,
        "path": ".github/workflows/ACTUAL_WORKFLOW.yml",
        "jobs": ["ACTUAL_JOB_NAME"],
        "source_sha256": {".github/workflows/ACTUAL_WORKFLOW.yml": "ACTUAL_APPROVED_64_HEX_SHA256"}
      }]
    },
    "packet": "packets/1446122118/1/ACTUAL_HEAD_SHA/packet.json",
    "selected_reports": "packets/1446122118/1/ACTUAL_HEAD_SHA/selected-reports.json",
    "collector_sha256": "ACTUAL_APPROVED_64_HEX_SHA256"
  }]
}
```

This is a schema illustration, not deployable policy. Replace every placeholder
with reviewed live identities and exact source pins. The separate private math
repository ID is1447509909. The App transport independently restricts the two
math repositories. `selected-reports.json` is the explicit target-name to observed
report-ID map required by the accepted live evaluator. It is not generated from
candidate acceptance flags. A packet is data; it cannot supply key registries,
policy, transport configuration or controller state.

The Actions variable `PROTOCOL_APPROVED_SHA` must be the reviewed40-hex current
main commit. It is separate from the checked-out config. The runtime requires
GITHUB_SHA to equal it, GITHUB_REF to be refs/heads/main, and the event to be
workflow_dispatch or schedule. Authenticated reads recheck current remote main
and exact private controller repository identity before every state barrier.

Only the final evaluation step receives these secrets:

- `GITHUB_TOKEN`, the control repository's own token, writes only the control
  repository Git API endpoints. It never accesses math repositories or checks.
- `PROTOCOL_APP_PRIVATE_KEY`, a PEM private key, goes only to the separate App
  signer/transport. Its installation can read the math repositories and write
  their checks. It cannot write controller state or math contents.
- `PROTOCOL_OPERATOR_KEYS` and `PROTOCOL_INTAKE_KEYS` are JSON objects mapping
  approved key IDs to `{"operator_id":"trusted-operator-identity","secret_hex":"<hex>"}`.
  The runtime preserves this attribution and converts `secret_hex` to the exact
  `{operator_id,secret:bytes}` record required by both accepted signed-log codecs.
  An old bare-hex entry is rejected. Each secret is32-128 bytes encoded as lowercase hex.
- `PROTOCOL_COLLECTOR_KEYS` maps approved key IDs directly to lowercase hex
  encodings of32-128 byte keys, as required by the manifest transport codec.
  Separate registries remain separate trust roles even if a trusted deployment
  deliberately supplies overlapping key IDs.

The workflow template uses one global concurrency group with cancellation
disabled. It checks out only the reviewed private controller commit, without
persisting Git credentials or loading submodules/LFS. It requires a reviewed
hash-locked `controller/requirements.lock` supplying cryptography50.0.2,
cffi2.0.0 and pycparser2.23. The supplied lock targets CPython3.12 on the
Ubuntu24.04 x86-64 runner; the workflow rejects a different Python minor version.
It installs binary wheels into a fresh runner-temporary virtual environment.
The lock is part of reviewed controller code, not any mathematical packet.

## Authoritative state and bootstrap

The root operator must explicitly bootstrap `protocol-state`. Runtime loading
never creates a missing ref, recreates lost state or silently resets checkpoints.
Use the existing `GitState` index schema. Its checkpoint map must contain exactly
`operator`, `intake`, and `publisher`. The first two are the signed codecs' current
checkpoints. Every sequence1..N has one canonical JSON entry at
`state/entries/operator/0000000001.json` or the corresponding intake path.
Missing, surplus, noncanonical or incorrectly signed entries fail restoration.

The publisher checkpoint is `{"snapshot_sha256":"<SHA256>"}`. Its content is
canonical JSON at `state/snapshots/<SHA256>.json`. The initial content is:

```json
{
  "schema": "protocol-controller-generation/v1",
  "controller_sha": null,
  "state": {"schema": "protocol-publisher-state/v1", "generations": [], "targets": []},
  "publication": null
}
```

Hash the canonical serialization, not the whitespace in this document. The
ordinary GitState index binds the content's blob ID, SHA256 and size. Subsequent
snapshots record the approved controller revision. A success barrier additionally
records the exact publication identity before sending the check update. Final
state records the resulting local phase. All earlier snapshots remain immutable.

The remote ref is the authority. The signed entries plus checkpoint in one commit
are not independent rollback protection. Administrative rollback remains a
trusted, explicitly recorded operator action. Any unexpected ref advance during
an evaluation invalidates that run. All commits use the old remote tip as their
single parent and update without force. A competing writer cannot silently
overwrite the run's state.

Ephemeral SQLite mirrors are restored only after complete authentication and
bounded inventory checks. Evaluation reads both ledgers. Observation append and
classification belong to separate trusted ingress tooling; the evaluation
anchors reject append requests. Every new run restores the durable publisher
snapshot before selecting its next generation. It does not infer a generation
from a previous check result.

## Tests and present boundary

Production always constructs `github_fork_context.ForkReadContext` and calls
`live_protocol_context_forks.evaluate_session` through a runtime-owned
`ForkProtocolRunner`. The runner validates that exact profile's in-process
`LiveEvaluation` type. Neither profile selection nor module names come from
packets. The accepted core publisher is unchanged. Base-repository pull refs,
the authenticated fork repository identity and fork CI provenance are checked
again on the final live recheck.

Each production reader immediately receives the accepted bounded
`immutable_git_cache.CachingAPI` wrapper. Its fixed transport and reader are
reused through the live session and final checks. Only exact immutable Git
object endpoints are cached; PRs, refs, comments, CI and other mutable endpoints
still reach authenticated transport every time. The cache does not supply
receipts or alter the signed-ledger checks. Ingress uses the same wrapper.

From this directory, run `python -B -m unittest test_runtime -v`. The tests use
real signed fixture histories, both restored SQLite stores, the actual live
evaluator, actual publisher, actual remote generation authority and actual
GitState CAS implementation. Only GitHub I/O is synthetic. Success is never
returned by a replacement evaluator, copied from fixture result JSON or inferred
from candidate booleans. A second evaluation starts from a fresh directory and
continues at generation2.

Negative cases cover altered signed entries, stale remote main, an unapproved
dispatch ref, a remote-state race, new unregistered comments, missing selected
receipts and credential endpoint separation. These are offline integration
tests, not proof of live GitHub API compatibility. Deployment additionally needs
the reviewed App transport, actual protected packets and
observations, controller bootstrap, approved SHA variable and independent review.
The publisher's polling cutoff limitation still applies: this is not an atomic
transaction between future GitHub comments, branch changes and merge.

The initial runtime had a real environment-boundary defect: its loader returned
bare bytes for operator/intake keys, while tests supplied the already structured
fixture registries directly. The corrected suite exercises the production
environment loader through both signed codecs, collector verification and a
complete fork publication. It also rejects lost/changed operator attribution and
the previous bare-hex secret schema. The prior runtime and verdict are preserved
in `revisions/pre-secret-fork-fix`; their20-test result did not establish this
production boundary. The subsequent cache integration suite has26 tests including
GitState tests. It includes a full successful publication with observed cache
hits and a new comment injected after warming the cache at the success barrier;
that comment blocks publication.
