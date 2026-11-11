# Controller operation

This is the owner-only controller for the two research repositories. The owner
requested and approved the App, installation and secret storage. App 5663093 is
installed as 179741595 only on those two repositories. Its key and signing
registries are Actions secrets here; no credentials belong in this tree.

The controller publishes `Protocol / independent agent audit` on the exact PR
head. Keep the strict up-to-date branch rule and all eleven existing Actions
checks. A new PR with no configured, accepted packet has no passing App check
and cannot meet the required-check rule. This service does not invent reviews
or run candidate programs.

For each new PR, prepare complete base/head manifests, the application inventory,
all received findings and independent author-distinct reviews. Preserve original
observations and rejected or superseded reports. Commit the protected packet,
explicit report selections and actual observation batches to this private
controller after review. Set `PROTOCOL_APPROVED_SHA` to that reviewed main SHA.
Run protected ingress, then evaluation. Changed source/dependencies, intake or
base/head identity require appropriate renewed review and reconciliation.

The initial schedule polls hourly to bound cold GitHub API reads.
Dispatch evaluation immediately after owner review or intake work. It repeats
live checks at publication boundaries, but cannot atomically exclude a comment
or a second PR created after its final observation. It does not guarantee a
one-hour maximum delay from GitHub's scheduler. Review the recorded cutoff
before merging. Owner credentials and truthful observation capture remain
trusted.

The in-memory cache stores only verified immutable Git objects. Mutable PR,
comment, CI and ref observations remain live. The optional disk-cache research
component is not deployed. The initial source policy independently pins CI
entrypoints and control data and uses reviewed pre-execution manifest checks for
packaged code. Source policy changes require a separate controller review.

Historical design notes preserve earlier plans and implementation-stage status.
This operation note states the deployed design; actual successful publication
and ruleset activation must be verified from GitHub, not inferred from notes.

After a configured PR is merged or closed, remove it from the active job list
and keep its evidence/state history. Until then a subsequent closed-PR
evaluation fails closed. Do not weaken the required-check rule, use a bypass,
or relabel a failed evaluation as acceptance.

An empty job list is an idle controller. It verifies the owner and approved revision, loads no App or ledger credentials, and publishes no PR check. Retain all prior packet and state history.
