# Deployment status

The independent-review App gate is active in both research repositories. The setup PRs merged under the required App check. Protocol v1.2 is pending in public PR10 and private PR2; it has not merged.

The most recent v1.2 evaluation, 42444615303, failed. The public PR had a registered-state mismatch. A subsequent comparison found only nested repository activity-field differences. The private PR's successful CI run returned empty step arrays for five jobs. A failed check remains required and blocks merging. Reviewed repairs and fresh authenticated captures are required before another evaluation.

## Protection currently active

Both main branches require pull requests, resolved review threads, all eleven existing Actions checks, and `Protocol / independent agent audit` from App 5663093. Rulesets 26781429 and 26781446 use strict up-to-date checks and no bypass actors. No second GitHub user's approval is mandatory.

The gate validates recorded review evidence, source bindings, author-distinct reviews, resolved findings and repository context. It does not independently prove the mathematics asserted in an accepted review. Owner credentials, truthful observation capture and GitHub API semantics remain trusted. Normal merges remain subject to branch protection.

## Isolation and retained history

`Elliot Research Review Gate` is installed as 179741595 only on the two math repositories. The controller is the owner-only private `elliotglazer/research-review-controller`, repository ID 1449903511. App and ledger credentials are Actions secrets. Candidate files are read as data and are not executed with these credentials.

The controller's `protocol-state` branch retains signed observations, findings, decisions and prior rejected or superseded records. New captures must use fresh identities. Historical records are not overwritten to simulate a current review.

The evaluator is enabled for hourly scheduled checks and manual dispatch. Once both v1.2 PRs merge and their remote contents are verified, a separately reviewed empty active-job configuration can stop repeated evaluation of completed PRs. Future PRs still require their own accepted packet and a passing required check.

## Evidence and next step

Local evidence includes `PROTOCOL-RULE-ACTIVATION.json`, `SETUP-MERGES.json`, actual controller logs, and the v1.2 independent review records. The remaining sequence is reviewed controller repair, fresh captures, successful actual evaluation, normal protected merges and remote readback. This policy-only update changes no mathematical manuscript, polynomial or theorem status.
