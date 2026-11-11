# PR-state freshness audit

Reviewer and candidate author `/root/sol_protocol_final_review`, November 7, 2026.

## Finding

The existing reader can invalidate its own successful App check. This is a reproducible controller liveness issue. The local reproduction changes only the PR's server-derived `mergeable_state` from `blocked` to `clean` after the App success write. The full runtime then reports failure, confirms revocation and leaves the check at `failure`. `REPRODUCTION.json` records the result. No remote mutation was needed for the reproduction.

`ForkReadContext.state` returns the complete raw PR object. `AuditObservationSource.observe` captures that state. `TrustedContextVerifier.verify_context` compares its current state to the registered capture. `_reobserve` compares the complete fresh observation to the previously accepted observation. `Publisher.run` calls `_fresh` immediately before and after the success write. A changed `mergeable_state` therefore fails the post-write comparison and enters the revocation path. An unrelated nested repository size or open-issue counter change has the same effect.

GitHub's REST PR example contains nested repository size/open-issue counters and the mergeability fields. GitHub's GraphQL merge-state documentation distinguishes passing and nonpassing commit-status cases. This supports treating these values as derived service output. The exact timing of a REST `mergeable_state` transition after an App write is a live-service question. The reproduction establishes the controller failure whenever that transition becomes visible during its post-write checks. [REST PR documentation](https://docs.github.com/en/rest/pulls/pulls), [merge-state documentation](https://docs.github.com/en/graphql/reference/pulls), [required-status troubleshooting](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks)

## Candidate remedy

The candidate changes only the state representation and pinned dependencies. Both readers emit `projection_schema` equal to `github-pr-state/v2`, copy the raw PR, then exclude exactly its root `mergeable`, `mergeable_state` and `rebaseable` fields. Within its `base.repo` and `head.repo`, they exclude exactly `size`, `open_issues` and `open_issues_count`.

CI run records and the collected run inventory can embed the same repository metadata. Their `repository`, `head_repository` and `pull_requests[*].base.repo` or `head.repo` receive the same three-counter projection. The implementation does not recursively strip generic names from unknown objects. Unknown fields and all other fields remain byte-for-byte significant under canonical comparison. Raw input objects are not mutated.

Author-controlled PR fields, title/body, state/draft/merged flags, labels, review requests, repository IDs/names/privacy/default branches, commits, trees, pull refs, base refs, source pins, CI identity/status/attempts/jobs/steps and complete intake remain subject to the existing checks. The separate publisher transport still requires `mergeable is True` in its ready-PR check and repeats its live context checks around publication. No change to that transport or the publisher is proposed.

This is a narrow liveness correction. Timestamp changes and other server metadata remain conservative failure triggers. Removing them would need a separately justified change.

## Evidence and deployment conditions

`FILES.json` pins six candidate files. `files/adapter/` contains the two changed readers, two updated live-profile dependency maps and two updated reader-profile documents. `pr-state-projection.patch` records the complete delta. Both live profiles pin the new shared reader. The fork profile also pins the new fork reader.

Eight new regressions passed using real fixture stores, the live evaluator and publisher. They cover a successful post-write derived-state change, repository/CI counter changes, body changes, draft changes, head changes, failing CI, new intake and exact retention of all other fields. Another 140 existing reader, fork, runtime and live-evaluator tests passed. Tests ran against an isolated temporary copy with candidate files overlaid and the actual updated dependency pins. `run_tests.py` records this procedure and `TEST-RESULTS.log` preserves its results. The initial harness lacked the test-only gate dependency directory; adding that unchanged directory fixed the harness before the successful runs.

Independent review must approve the exact candidate and source-pin changes before deployment. Retain all original raw signed captures as historical evidence. After deployment, make new authenticated captures using the projected reader. The explicit projection schema guarantees a different state representation; editing old capture bytes or replacing their digests would fabricate an observation. Existing packet content and review acceptance are unchanged by the projection, but captures and fresh evaluation must match the newly deployed reader. Source bindings and approved controller revision must also identify that deployment.
