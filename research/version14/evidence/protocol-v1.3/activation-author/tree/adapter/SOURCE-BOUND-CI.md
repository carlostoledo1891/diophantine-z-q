# Source-bound evidence for missing CI step records

The fork reader supports one explicit alternate evidence profile when GitHub returns a wholly empty `steps` array for an executed, successful job. It does not convert absent step records into successful step records. Raw job responses remain unchanged; a separate `job_evidence` entry records `evidence_mode=source-bound-job-conclusion/v1`, `steps_unavailable=true`, the workflow digest and the complete source-map digest. Jobs with step records retain `evidence_mode=api-step-conclusions` and `steps_unavailable=false`.

## Reviewed source profile

The profile covers only `.github/workflows/research-checks.yml` with SHA-256 `6488391dc379a68e855234fccc933f6d71300dba67004112376bc2c15a1d5b23`, its exact eleven expanded job names, and the expected `ubuntu-24.04` or `windows-2022` runner label for each name.

The protected reader also binds the repository identity, workflow ID and entire configured source map:

| Repository | Repository ID | Workflow ID | Source-map SHA-256 |
| --- | --- | --- | --- |
| `elliotglazer/diophantine-z-q` | 1446122118 | 407358539 | `a5f6a33320b3b266e2ebd826a2f984506538fd6c7ba9fc763c6bb9e3b6ce2fe4` |
| `elliotglazer/private-diophantine` | 1447509909 | 408660600 | `afd92925c4a26132e5d764a8a208f986488d7f50d920aee3a6b492221d8a934c` |

Source-map digests use the existing canonical JSON rule and SHA-256. They cover the public 157-input and private 181-input maps. Removing a pin, changing a source version or using an unknown repository/workflow profile cannot retain this alternate route. Updating these constants requires a new source-level review, not merely refreshing a hash after a failed check.

The audited workflow has no job condition or dependency that skips required work, no step or job `continue-on-error`, and no background or parallel step declarations. Its only explicit step conditions are `always()` on artifact uploads. Actions use exact commit pins. Under GitHub's documented default status conditions and error propagation, an executed successful job therefore supports an inference that the configured top-level checks succeeded. This is an inference from job status and reviewed source, not direct observation of every step or proof of the underlying mathematics. [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idstepscontinue-on-error), [status expressions](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions#status-check-functions).

A generic green required check is insufficient: GitHub treats skipped jobs as successful for some merge purposes. This route still rejects skipped, neutral, cancelled or failed job conclusions. [GitHub status-check meanings](https://docs.github.com/en/pull-requests/reference/status-checks).

## Source verification and observation boundaries

`ForkReadContext.sources` clears any prior internal verification stamp, verifies packet/state commit and tree agreement, then calls the existing source verifier. That verifier checks all configured input blobs against the base, head and merge trees and checks the packet's base/head pins. Only after it succeeds does the reader save a stamp covering the full observed state and protected policy, including every workflow source map.

The alternate route requires that exact stamp. Changing the state or policy invalidates it. Failed source re-verification and any new state read clear it. Calling `ci` without successful source verification cannot accept an empty step list. The stamp is internal process state, not a candidate-supplied acceptance flag or a portable authentication receipt.

All existing run and job provenance checks remain: exact repository, workflow path and ID, PR base and head association, newest run, run attempt, required job inventory, and successful run/job conclusions. The source stamp also binds the checked merge commit and tree. An empty-step job must additionally have a positive integer job ID and runner ID, a named runner and runner group, the single expected runner label, and valid UTC execution times strictly ordered inside the run's time interval.

For each empty-step job the reader fetches its individual job endpoint and requires exact equality with the attempt-list object, including unknown fields. A disagreement blocks the observation; it cannot select a more favorable representation. Missing, null or malformed `steps` fields do not enter this route. A nonempty list containing even one incomplete, skipped, failed, cancelled, neutral or malformed step is rejected.

The inherited `observe` sequence reads complete CI evidence twice and compares it exactly, along with the surrounding intake and PR state. Recovery of step data or another change between those reads requires a new observation. No sleeps or retry loops were added. The controller's immutable-object cache does not cache Actions endpoints, but GitHub may still serve cached API responses. Two equal reads establish observed consistency only; they do not establish independent freshness, atomicity or eventual recovery of missing metadata.

## Validation and deployment

`test_source_bound_ci.py` uses synthetic transport fixtures and a test-only profile. It exercises full source verification, retained raw evidence, explicit evidence modes, strict supplied-step rejection, invalidation of verification stamps, dropped or changed source pins, unknown profiles, job inventory, runner/timing requirements, direct-endpoint disagreements, and changes between the two CI reads. Existing reader and fork tests continue to exercise provenance and failure handling.

Run from the adapter directory:

```text
python -B -m unittest test_source_bound_ci test_github_fork_context test_github_read_context
```

This implementation changes neither configured reader-hash pins nor deployment state. Independent review, pin updates, fresh observations and normal protected deployment remain separate integration work.
