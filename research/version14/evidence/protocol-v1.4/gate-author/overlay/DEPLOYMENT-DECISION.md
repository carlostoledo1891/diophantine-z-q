> Historical proposal, preserved November 7, 2026. This document is not a current deployment receipt. The exact original bytes are retained in `deployment-history/2026-11-07-before-v1.4/DEPLOYMENT-DECISION.md`. See `DEPLOYMENT-STATUS.md` for the current bounded readback.

# Live deployment decision

The user requested completion and activation on November 7, 2026. Basic
pull-request and CI rules are already active. They are not the protocol gate.

The proposed deployment uses a separate private control repository owned by
elliotglazer. Project collaborators receive no access to it. Its trusted
controller runs on a separate GitHub Actions runner, with the GitHub App key
and ledger-signing secrets available only there. The App is installed only
on the two mathematical repositories with the permissions in
`adapter/APP-SETTINGS.json`. The control repository's own GITHUB_TOKEN, not
the App token, maintains controller state.

The owner and local orchestrator remain trusted administrative and
observation authorities. This does not protect against compromise of their
GitHub credentials. Unreviewed candidate programs must run only in separate
ordinary Actions jobs with no control-repository or App credentials. The
controller reads candidate Git objects and evidence as data. It never runs
candidate scripts, actions, imports, hooks, build commands, or workflow code.

Operator observations record actual agent identities, original reports,
authorship and frozen target bindings. They are operator attestations, not
cryptographic attestations from a model provider. Unknown serving-model
metadata must remain unknown. A candidate cannot certify its own receipts
by writing reviewer names or acceptance flags in repository files.

Trusted controller code, policy promotions and observation intake are
separate from mathematical PRs. Dispatches must use the approved controller
ref. Untrusted strings are data, never shell command fragments. Controller
state updates use an expected remote commit with compare-and-swap; the
remote state ref is the authority. Two files in one state commit do not
constitute independent rollback protection. Administrative rollback is a
trusted-operator action and must be explicitly recorded.

The required check is `Protocol / independent agent audit`, restricted to
the new App's numeric identity. It records the exact reviewed repository,
PR, base/head/merge commits, complete manifests, policy, audit history and
receipt set. The test-merge commit is the preferred publication target,
subject to live validation of its interaction with the eleven existing CI
contexts. No success is published from candidate-supplied booleans.

Polling provides a recorded evaluation cutoff, not instantaneous detection
of future comments. Each publication repeats live state and checkpoint
checks. New evidence invalidates the applicable approval when observed.
The documentation must not promise an atomic GitHub comment/merge transaction.

No App, control repository, credential or new protocol rule has been
provisioned by this decision document. Deployment follows independent review
of the working integration and a concrete final App-setup approval if the
UI requires it.
