# Astra acceptance policy

Adopted November 9, 2026 for `elliotglazer/diophantine-z-q`.

This project uses [Protocol_D](https://github.com/elliotglazer/protocols/blob/main/Protocol_D.md). In addition, only designated Astra agents may supply the judgments that satisfy required protocol acceptance. This restriction applies to mathematical applications, repairs and finding resolutions, inventory coverage, assembled-proof acceptance, and the final protocol decision for a pull request. A non-substantive pull request still needs an eligible review of its stated scope.

## Contributions and review authority

Any authorized person or agent may propose proofs, code, computations, documentation, repairs, and preliminary reviews. Contribution credit does not depend on eligibility to accept work. Every substantive objection must be recorded and addressed regardless of who raised it. A favorable Astra review does not erase an unresolved objection.

An acceptance reviewer must be a non-author of the contribution being accepted. An Astra reviewer who supplies a substantive repair becomes an author of that repair; another eligible agent must review it. A second run by the original agent is not independent acceptance. Different Astra agents may divide the required reviews, but each must identify the exact scope and revision checked. Shared model identity does not establish independent reasoning.

## Eligible run records

The initially approved model identifier is exactly `gpt-6-astra`. Aliases, other models, fallback runs, and unknown model identities do not satisfy this policy. Adding a successor model requires a separately authorized change to the protected controller policy.

Eligibility must come from the controller's trusted run and review records, including the agent identity, model, reviewed artifacts and decision. A name, model field, approval flag, or report supplied by a pull request is insufficient on its own. The existing authenticated operator and observation process remains part of the trust base; this policy does not claim provider-signed proof of the model that served a request where no such evidence is available.

Earlier reports retain their original identities and scope. They may be used as research evidence, but an ineligible report cannot be relabeled or counted as a required Astra acceptance. Reuse of an eligible earlier review must meet Protocol_D's exact-version and dependency requirements.

## Merge enforcement

The public repository must require `Protocol / independent agent audit` from the designated GitHub App. The isolated controller must check this eligibility policy as well as the other protocol obligations before publishing a passing result for the exact reviewed pull request revision. Passing ordinary CI, a GitHub approval, or a contributor-written acceptance record cannot replace that check. The candidate pull request must not be able to change the policy used to assess itself.

Controller enforcement was activated on November 9, 2026 at revision `f1d2605e7d4b42a1e364d7c36f45a0119e4fc9fd`, after 269 independent policy and regression tests passed. The [activation record](astra-acceptance/activation-2026-11-09.json) records the exact runtime files, successful controller startup, active public App requirement and unchanged private ruleset state. That startup run had no queued PRs; it did not approve a mathematical result. Policy rejection behavior is established by the separate tests, not inferred from an idle run.

The private repository `elliotglazer/private-diophantine` has no ruleset. This policy does not add one or impose a controller requirement there. Publication and repository access remain subject to the owner's authorization.
