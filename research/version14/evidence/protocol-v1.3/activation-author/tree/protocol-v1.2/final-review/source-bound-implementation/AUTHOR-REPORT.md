# Source-bound CI implementation report

Author: `/root/protocol_v12_acceptance`. I authored this implementation after the earlier independent diagnosis. I am not its independent acceptance reviewer.

The frozen candidate files and SHA-256 values are in `CANDIDATE.json`. Production changes are confined to `adapter/github_fork_context.py`. The existing version 3 state projection is preserved. The new test and documentation files are `adapter/test_source_bound_ci.py` and `adapter/SOURCE-BOUND-CI.md`.

The alternate route accepts only wholly empty step arrays, after successful full source verification for the same state and protected policy. It requires the exact reviewed workflow digest, repository/workflow identity, complete source-map digest, full job inventory, assigned runner, expected label, ordered execution times and an identical individual-job response. All supplied incomplete or non-successful steps still reject. The original response remains intact, with an explicit separate evidence-mode record.

The source verification stamp clears before a new source check or state read and is recorded only after the inherited source verifier succeeds. It covers the entire policy and state. The inherited two complete observation reads remain in place; no sleep, unbounded retry or claim of independent cache freshness was added.

Validation completed:

- The 120 tests in `test_source_bound_ci`, `test_github_fork_context` and `test_github_read_context` passed.
- Both production repository/workflow identities, source-map digests and expected job inventories match `deployment-v1/config.json`.
- Broader live tests and runtime/projection tests were attempted. They stopped at the intentionally unchanged `github_fork_context.py` dependency pins, including the corresponding exact-profile comparison. The integrator owns those pin updates and the subsequent combined run. These attempts do not establish passing combined integration.

Two test-authoring issues were corrected before the passing focused run: a test property accidentally shadowed `unittest.TestCase.run`, and one assertion expected a later runner-validation error even though the existing API layer correctly rejected a Boolean job ID first. No production guard was relaxed for either test.

No reader hash pins, stage-bundle code, candidate research repository, credential, CI run or deployment was modified by this author. `/root/sol_protocol_final_review` received the exact candidate hashes for independent review.
