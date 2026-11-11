# Versioned PR-state projection review

Accepted the six candidate files bound by pr-state-audit/FILES.json. Reviewer /root/sol_protocol_policy_review. The exact candidate SHA256 values are

- adapter/github_read_context.py 0919a50725bf26b7b963e539ed25b12430c5d8b359279291e9474e14f5c9aab1
- adapter/github_fork_context.py 8a4a34ece004e9cd976fcaa95c166ff76c79245c835ca39fc31ba6f0e9605659
- adapter/live_protocol_context.py 8526a116b37ef5b57e332c3024fcebf0f0e5482d4d9c834015592d2efa7a629e
- adapter/live_protocol_context_forks.py 00552cfd8c15e5e37c444ba479f19873dc08a3292a64fb3f2a940092233b23cb
- adapter/GITHUB-READ-CONTEXT.md 56a7b33a5de34afdb00799345aafad2205531d0cc61051abc5cce320481bcf93
- adapter/LIVE-FORK-PROFILE.md 626fb737ed459266c770772fa42b63a4c270330db8f98074721ab01ff1bf9041

Independently compared normalized source diffs and verified all six current base hashes and candidate hashes against FILES.json. The only code changes are the explicit projections, state schema marker, their use in both readers and CI observations, and updated reader dependency pins in both live profiles.

The PR projection excludes exactly root mergeable, mergeable_state and rebaseable, plus size, open_issues and open_issues_count from base.repo and head.repo. The CI projection excludes the same three counters only from repository, head_repository and the repository slots of pull_requests associations. It does not recursively remove similarly named fields elsewhere. All unknown fields remain compared. Every projection deep-copies input before editing.

Title, body, labels, draft/open/merged status, requested reviewers, IDs, privacy, branch names, commits, trees, CI run/attempt/status/conclusion, jobs, steps and intake retain existing checks. Raw publisher transport still requires mergeable is True and repeats exact current context checks before and after publication. Excluding the derived snapshot field does not authorize a nonmergeable PR. Both live profiles retain their strict observation/reconciliation comparisons.

New observations include projection_schema github-pr-state/v2. Old raw captures lack that field and cannot compare equal, even if they happened to omit every removed field. The change therefore requires new authenticated captures. The docs explicitly forbid editing or relabeling old signed captures and preserve original history and review decisions.

Independently ran 8 projection tests and 140 existing reader, fork, runtime and live-session tests. All 148 passed. projection-tests.log records the run. A separate reviewer check confirmed exact CI repository-slot filtering, preservation of unknown nested size fields and input nonmutation. The new full-runtime tests preserve success across the App's own derived merge-state change and repository counters, while body/head/draft/CI/intake changes still fail or revoke success. This establishes tested behavior, not future live success.

## Projected capture inputs

Accepted public v3 batch 77cdf08d1d0cdb9890156d493ec9345feceb5d597dcb14d32cc8c0a390792059, private v3 batch 253350944ae389098df033b7e4ef71ba17a7d69df8b87c9e7257a10e159a146e, and projected overlay c58a8b12f77e01c5eb60f15aea8f271a8e2081592c239c164ce623520a716dc4.

Compared against the accepted v2 batches. Only the batch identities and classification-observation statements change. The new statements explicitly require fresh github-pr-state/v2 capture and retain raw history. Operator events and finding redefinitions remain empty. All original selectors, finding-ID assignments and classification reasons remain identical. Public PR8 external material is re-registered with exactly the same source identity, body and observation bytes, so it has the same immutable material ID whether the earlier raw capture committed first. Public still classifies 24 materials and private 23. The overlay preserves every v2 mapping and adds only the two v3 batch paths.

No candidate or deployed source was edited and no remote mutation was performed by this reviewer. Actual App capture, signed-ledger verification and subsequent live publication remain execution steps.
