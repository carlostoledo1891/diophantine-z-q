# Independent source-bound CI review

Reviewer `/root/sol_protocol_final_review`, November 7, 2026. Implementation author `/root/protocol_v12_acceptance`; integration pins and fixture update by `/root`.

## Decision and exact scope

Accepted implementation for the complete combined v3 fork reader, including its source-bound empty-step route and the refreshed dependency pins. No material defect found in this scope. This is implementation acceptance. Live source checks, authenticated observations and protected deployment must still run for their actual targets.

Reviewed SHA-256 values

- adapter/github_fork_context.py `0de8fbbb6bd9a0de03a30645ca72ed981e3347da8599e37ce1828f1a0b245345`
- adapter/github_read_context.py `52504ba81c8072e63477bfa9af35eadf2bc94db635efa10021d6ada9f4c81f6a`
- adapter/test_source_bound_ci.py `36790117f5e020f7f000fd862bb07d6f8790bd0bf119be68a889d15ed9a507ed`
- adapter/SOURCE-BOUND-CI.md `f673945ef35aa796aae99a07e166d9dafdf19e8c107ab00689d0b991bbb48641`
- adapter/live_protocol_context.py `6e6111e32cac20a84ee200a0fa887a76086ee4e4a124efeda01c89566c2b0148`
- adapter/live_protocol_context_forks.py `ed98f8543e7a6518d8946a6e045f200828ae7487fe69d7e70db999510eaf6525`
- adapter/test_live_protocol_context_forks.py `dd3120722b7a5fbfc66a512fc32373849467b8209c39fcdb16f352075d66f320`

## Evidence semantics

I read the whole reader and inherited source, observation and live-session methods. Empty steps remain empty in raw evidence. The separate evidence_mode expressly records an inference from successful executed jobs and reviewed source. Nonempty step lists retain strict success checking; missing, malformed, null, skipped, neutral, cancelled and failed evidence cannot select the alternate route.

The source profile fixes repository identity, workflow ID/path, the workflow SHA, complete source-map SHA and all eleven expanded job names. Both actual protected maps match the encoded digests, with 157 public and 181 private inputs. I independently hashed every listed input from the corresponding local Git HEAD blob, with zero mismatches. This verifies available pinned Git bytes, without asserting current remote branch state. The workflow bytes hash to `6488391dc379a68e855234fccc933f6d71300dba67004112376bc2c15a1d5b23`. Its steps have no continue-on-error or work-skipping condition; only uploads use always(). There are no job dependencies, job conditions or background/parallel step declarations. Required commands and actions are explicit. The inference concerns their reported execution success, not mathematical truth.

GitHub documents default success conditions, shell error propagation and the effect of continue-on-error. GitHub also warns that skipped jobs can satisfy required-check status. The implementation therefore requires actual successful Actions job/run objects, assigned runner metadata, the expected exact runner label and strictly ordered execution times, in addition to the reviewed workflow shape. These checks support the narrower documented inference. [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [status expressions](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions#status-check-functions), [status checks](https://docs.github.com/en/pull-requests/reference/status-checks).

## Authority and consistency

Successful sources() verifies all policy/workflow blobs at base, head and merge, and the packet manifests. Only then does it stamp the full state and policy. Failed re-verification, new state reads and changed state/policy invalidate the stamp. It is process-local evidence within the existing trusted-process boundary. Candidate code cannot establish authority by supplying a stamp field.

The reader retains newest-run selection, exact PR/base/head/fork/workflow/run-attempt association, complete job inventory and strict successful conclusions. The individual job endpoint must agree with the attempt listing on every field. Two complete CI reads must agree, followed by the state comparison. Cached matching responses establish observed consistency; they do not establish atomicity or independent freshness. The controller cache is confined to immutable Git blobs.

The v3 projection retains author-controlled and unknown fields, exact commits/trees/refs, intake and CI. Only its enumerated derived PR fields and repository activity fields are omitted at specific slots. Raw publisher merge readiness remains independently required. The live session reobserves after core checks, binds protected policy snapshots, verifies current ledger checkpoints and permanently invalidates a failed recheck. The refreshed dependency pin and test expectation select the exact fork-reader bytes above.

## Tests and scope limits

I independently ran all 120 source-bound/fork/base-reader tests successfully. They include full observe() with actual source verification in synthetic transport, explicit evidence modes, failed source checks, source-map removal/drift, missing/failed steps, runner/timestamp errors, direct-endpoint disagreements and changes between reads. Root separately reports 98 controller tests passed and 149 adapter tests with one stale expected hash corrected and its targeted rerun passed. These are separate recorded executions.

This review supplies no new observation that any missing step metadata has recovered. Historical captures retain their original semantics. Fresh authenticated captures under the new reader are required. The larger stage manifest also contains ingress batches and prior v3 diagnostic reports; this decision does not independently approve those unrelated bytes or authorize deployment. No production or author file was edited during this review.
