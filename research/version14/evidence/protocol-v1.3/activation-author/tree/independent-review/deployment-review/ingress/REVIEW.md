# Independent ingress review

Decision: accept the corrected ingress component within the stated protected-controller trust boundary. This is not approval of a deployed gate, live credentials, a particular observation packet, mathematical conclusions, or a future unreviewed composition.

Reviewer: `/root/astra_quartic_opt02_squares`, distinct from ingress author `/root/astra_quartic_opt05_anchor`. The reviewer did not edit the producer. All writes for this review are in this independent-review directory. No live API requests, real keys, repository settings changes, pushes or deployments were performed.

## Exact scope

SHA-256 pins, relative to `work/protocol-ruleset-20261107/`:

| File | SHA-256 |
|---|---|
| `controller/ingress.py` | `24d4ebad365d30986d1f6abd18851acaa0e83dae64c90458ec0b2996407668fd` |
| `controller/INGRESS.md` | `f2dc3b5756b99abcb9ec654057f114e705ca135ec324b23b834c893d07aee9b8` |
| `controller/ingress.workflow.template.yml` | `cb31cf34ebeb6b8fb3d3b0d480b38db48f511cc63b8e1ce85ca4d8867c459b54` |
| `controller/test_ingress.py` | `bcdca9c3d1a558315a514f19400aba3aeead67003033084c46eb280fe0cc897b` |

The inspected runtime dependency is `39ec395c8d21227bd3709b1a909dd976fcb6cd2177837f5526c1290801c7c912`; GitState is `76269c5918bdf81d40e58685a9c207faa85f342cf0cd79e4d8a9203e7ea87815`; full collector is `8ca4d7b1ffb49d1a329f5ab8f423b1e415b3c5616f8e6d03a052348f75f9fcef`. This review checks ingress's use of those interfaces and carries forward their separate review scope. It is not a fresh independent audit of every runtime or App-transport operation.

## Finding ING-1: collector inherited controller secrets — resolved

Original ingress SHA-256: `b672b91e655438e85166b6408c5e38eeab419719acdeb855e53f0eed9a2deb0a`, preserved as `ingress_original.py`. The initial bare-fetch subprocesses received a scrubbed environment. However, the subsequent in-process full collector created its own Git subprocess environment from the parent process. Its environment filtering removed Git variables, not the parent's App private key, HMAC registries or controller token. Clearing the earlier local dictionary did not change that parent environment. This contradicted the component's stated credential separation.

`probe_environment.py` intercepted the actual full collector's ObjectReader launch using synthetic variables only. `original-environment.log` records the failure and the inherited names `PROTOCOL_APP_PRIVATE_KEY`, `PROTOCOL_OPERATOR_KEYS`, and `GITHUB_TOKEN`. No real credential values were inspected or printed.

The author moved full collection into a separate `sys.executable -I -B` invocation of the hash-pinned collector file, with `PROTOCOL_*`, `GITHUB_TOKEN`, `GH_TOKEN` and Python import-environment variables removed. Each worker's nested Git children now inherit that scrubbed environment. The parent environment remains intact; the code does not temporarily mutate global environment state. The installation token is confined to the earlier authenticated Git environment and absent from worker argv/environment. Worker outputs must exist, fit the 40 MiB input bound and parse as strict JSON; the full exact manifest comparison remains before envelope signing. The accepted collector itself was not modified.

An independent test uses a real local bare Git repository and actual isolated Python collector workers for both manifests. It verifies exact manifest equality, two worker invocations, environment filtering, isolation flags and unchanged parent synthetic variables. A missing actual Git blob makes collection fail; a pre-existing output file is preserved and rejected. These checks supplement the author's mocked argv/environment regression. The original probe is preserved, not rewritten to pretend it tests the new architecture.

No further ingress correctness defect was found in the inspected source or independent negative controls.

## State and evidence checks

Ingress reloads both complete verified signed logs and stages copies. Explicit events use the existing authenticated codecs. It cannot use a candidate `verified` flag or reviewer label in place of those records. Source selectors require an existing material ID or one exact report-ID/body-digest pair. It neither silently classifies new materials nor infers favorable semantic findings.

The full collector checks every local tree and blob, including files not subsequently consumed as proof evidence. Before sealing, ingress compares the complete canonical collected manifest against the protected packet, including raw content digests. The later intake reader independently binds current repository/PR/commit provenance. Bare acquisition is limited to the configured base repository and branch plus the base repository's PR head ref; there is no checkout, hooks, submodule execution or candidate dependency installation. Ref mismatch fails before signing. These claims assume the approved controller code, Python/Git installation and system environment are trusted.

`finalize` requires complete current intake reconciliation and the exact set of selected application/finding/assembly receipts, including their target and dependency hashes and current binding. `capture` can preserve objections before they are classified, but returns pending material IDs and no merge authorization. Every observed historical material remains subject to the existing ledger rules. Operator classification of a source as containing no findings remains a trusted semantic act, not an algorithmic proof.

All new operator and intake entries, both replacement checkpoints and a content-addressed receipt are supplied in one authoritative state advance. Old immutable entries and unrelated publisher state survive. The existing GitState interface rejects competing updates. Independent tests verify a single successor generation, all signed tails and checkpoint sequences, retained deleted-comment history, no authoritative update on failed validation, and preservation of the competing winner in a race.

Exact batch replay returns its already-committed receipt without resigning or rereading GitHub. A changed batch using the same ID is rejected. The replay result deliberately is not a current freshness assertion; a later evaluator still must run the live checks. No arbitrary historical receipt is a substitute for a current evaluation.

## Workflow and limits

The template dispatch selects a committed path under the protected ingress directory; the runtime applies its protected path and revision checks. The workflow uses approved-main identity checks, a pinned checkout action with persisted credentials disabled, a hashed dependency lock, fixed command text, and the shared serialized state concurrency group. It grants the controller token contents write for protected state; the separate App installation supplies target-repository read access. It does not put controller/App secrets into candidate jobs.

The trusted owner must keep unreviewed candidate execution away from owner/controller credentials, approve actual controller code and configuration, and supply authentic observations. This mechanism cannot establish provider-level cryptographic agent identity or defend against a malicious trusted owner. It does not protect against owner rollback of the complete authoritative remote state. Remote fetch can consume disk/time before the collector's object limits apply; the per-command/workflow timeouts and collection limits are not a strict network/disk quota. Current-state checks have a recorded cutoff, not atomicity with future comments or merges.

Actual deployment still requires separately reviewed controller composition, protected configuration and dependencies, App installation and permissions, authentic owner ingress data, a live evaluator/publisher and ruleset verification. No live enforcement readiness follows from this component acceptance.

## Reproduction

Run `python -B check_review.py` from this directory with the environment's configured Python. It pins source before and after execution, runs both author suites plus the reviewer-authored state and real-worker tests, and writes `CHECKS.json` and individual logs here only. The expected total is 45 tests: 18 ingress, 12 GitState, 12 independent state/evidence controls, and 3 independent real-worker tests. No test uses the network or real secrets.

The initial combined-discovery harness errors and their correction are disclosed in `INITIAL-FIXTURE-NOTE.md`; they were reviewer fixture issues, not producer findings. The original failing credential probe remains separate evidence of ING-1.
