# Repaired policy and memory-cache integration acceptance

Reviewer /root/sol_protocol_policy_review independently reviewed this repair on 2026-11-07. The earlier REVIEW.md remains the record of the rejected candidate.

## Repaired compact policy

Accepted for public HEAD 8cc69491fb252375e7fd77601fad19e90846d86d and private HEAD 637919efb60bdfd350ef1ec2a6c8ebc4432a9f4d, with compact config SHA256 31a2467eccdfca979bbdc5acc00f236c9817c7e866b0e27c078c25eb949a2409. This acceptance covers the exact documentation-only setup changes and the eleven CI execution routes recorded in REVIEW.md. It requires renewed review for future files that change import resolution, executable input selection or validation authority.

The generator now includes all five omitted files. Independently read every direct pin from HEAD using git show and verified all 157 public and 181 private SHA256 values. The five additions fix the concrete root-authority omissions. The package pre-execution ordering review from REVIEW.md remains applicable. repaired-verification.json binds the current policy and exact heads.

## Memory-cache integration

Accepted for the narrow runtime, ingress and stage_bundle wiring described by controller/MEMORY-CACHE-INTEGRATION.json. The five integration source hashes, delta hash, immutable module hash and bundle manifest hash match the current files. The module remains the exact independently accepted 6a349dfad429765bc3e938179ae1243edfb047c2b1a14eea22ee6a420cabd57b implementation. The staged bundle manifest includes the module, its tests and its existing independent acceptance.

runtime.evaluate constructs the normal ForkReadContext and assigns CachingAPI before constructing the AuditObservationSource or EvaluationInputs. Both receive the same reader. The publisher's evaluation route therefore shares that cache with the intake observations and final rechecks. ingress.main likewise replaces only the reader API before apply_batch. The App transport and publication/state transports retain their existing roles. The cache matches only exact selected-repository immutable Git object paths. Mutable comments, refs, PR information and CI calls continue through fresh transport requests.

Independently ran the current runtime suite, 14 tests, and ingress suite, 18 tests. All 32 passed. Logs are runtime-tests.log and ingress-tests.log. These include real evaluator publication with cache hits and the negative control adding a comment at before_success after the cache warmed. That control prevents success. Source review of the complete delta found no candidate-selectable cache construction, persistence or preseed path. The existing module acceptance governs its authenticated commit-response assumptions.

## Polling choice

A 30-minute scheduled poll with deliberate manual dispatch after intake/review actions is a reasonable small operational change for this exact setup. At the supplied estimate of 755 immutable requests per two-repository run, two scheduled runs use about 1510 immutable requests per hour. Mutable observations, authentication, state calls, retries, workflow duplication and manual dispatches add to that estimate. This is an estimate rather than a measured total or quota guarantee. Observe actual App transport counters and avoid overlapping duplicate dispatches before shortening the interval.

The cache lasts for one evaluation. It reduces repeated reads inside a run and does not preserve objects across scheduled runs. A slower poll retains the already-disclosed observation race and increases time to notice a newly changed state. It supplies no atomic merge guarantee. No persistent cache is needed to accept the narrow integration reviewed here.

Backend model metadata remains unknown. This acceptance does not assert live GitHub deployment, completion of remote CI, or mathematical validity of the manuscript.
## Final staging and rule activation supplement

Reviewed final bundle manifest 9069f75f52834c4dd9421732d8f3b7aec90e8b1f83d13abcb015bc0e02b0a7a1. All staged file hashes match that manifest. All 21 production modules match their current accepted source bytes. The deployed config policy objects are exactly equal to the accepted compact policy objects. Only the packet and selected-report paths differ, selecting the exact public and private heads stated above.

Read the complete controller workflow. It uses the 30-minute schedule and workflow_dispatch, fixed writer concurrency with cancellation disabled, approved main revision checkout, locked dependencies, and the same runtime entry point. Staged workflow bytes equal the current source template. There is no previous deployed workflow in the local repository's initial parent commit, so this review confirms the complete current workflow rather than independently proving a schedule-only diff against that parent.

Independently rehashed all 709 manifest-covered members in each repository against the eight supplying manifests. Every hash matched. There are 189 guarded code paths per repository. barrier-verification.json records these checks.

Read activate_protocol_rule.py and its imported GitHub request helper. Its target repositories, ruleset IDs, PR numbers, App ID and check name are fixed in source. It requires a single completed successful check from that App on the freshly observed PR head, checks its external-ID prefix, keeps active enforcement and empty bypass actors, requires strict status-check policy, and appends only the expected App-specific check. It preserves all other current rules and conditions in the update payload. It rechecks PR head and base before the PUT and verifies the complete payload on readback. A successful earlier repository update can remain if the second repository fails, and its receipt is written after each successful update.

The narrow activation is accepted for the trusted operator's ordinary Python execution with assertions enabled, after actual successful App evaluation. The script implements its guards with assert, so do not invoke it with -O or PYTHONOPTIMIZE. Concurrent administrator changes to these rulesets must be excluded during its read/update interval, since the API update is a full ruleset replacement without a compare-and-swap guard. This review performed no activation and makes no live success claim. A source-level improvement would replace assert with explicit failing checks, but no source was changed by this reviewer.
