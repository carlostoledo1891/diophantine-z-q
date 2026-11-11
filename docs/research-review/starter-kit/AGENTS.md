# Operating instructions for mathematical research

Read PROTOCOL.md and PROJECT.md before starting. PROTOCOL.md defines the assurance obligations. This file defines how to meet them efficiently; it does not relax them. If these instructions conflict with the protocol, preserve the protocol's assurance requirement and report the specific conflict.

## Start with a small working system

Use one authoritative, version-controlled review ledger. Reuse an existing adequate implementation. Otherwise begin with one structured file or a small database and a minimal validator. Generate human-readable inventories and status reports from it. Do not maintain independently edited copies of the same facts.

Identify the target statements, source versions, required artifacts and authorization already supplied by the owner. Initialize the ledger alongside the first proof draft. Do not defer this work until publication. Research and review preparation may proceed in parallel.

Do not build a custom GitHub App, service, elaborate dashboard or separate review framework unless the owner requests it or a concrete requirement cannot be met by the simpler system. Never substitute infrastructure work for mathematical progress.

## Record meaningful mathematical units

A review unit is a coherent lemma, theorem application, construction or connecting argument with a definite input/output contract. Do not automatically create a new application record for each sentence, line, citation or checklist field.

Every substantive input must still be accounted for. Group repeated uses only when the same reviewed contract actually covers them, and list every consuming location. Split a unit when its hypotheses, objects, conclusions or consumers require different justifications.

Store each mathematical assertion and proof once and reference it from related records. Populate the protocol's nine obligations by linking to the relevant argument and explaining the match. Do not manufacture nine versions of the same proof or use generic nonempty prose as evidence.

Maintain stable identifiers for claims, uses, sources, findings and review decisions. Preserve historical versions through immutable Git references or another declared versioned archive. Do not create a new packet merely to repeat unchanged evidence.

## Preserve the independent reviews the protocol requires

Assign source-first dependency reconstruction to a non-author reviewer. That reviewer must derive the initial source-use table from the proof before using the declared inventory or earlier verdicts as a checklist. Preserve that initial table, then reconcile it with the canonical ledger. Record prior exposure honestly.

Retain separate decisions for application correctness, inventory coverage and final assembled-proof acceptance. These may be fields in shared records and may be supplied by the same eligible reviewer where the protocol permits. They do not require separate file trees or independent administrative pipelines.

An author cannot independently accept their own argument. If a reviewer supplies a substantive repair, obtain non-author acceptance of that repair. This does not require another mathematical review of unchanged arguments or an endless sequence of reviews of review prose.

## Make review incremental

Before assigning work, check the ledger for an applicable accepted result and an active owner. Reuse accepted evidence at its exact scope and version.

Bind a review to the assertion, proof, relevant definitions and assumptions, source versions, dependencies and consuming context. A matching paragraph hash alone is insufficient if any of that context changed. An unchanged whole file alone is insufficient if a dependency changed.

For each change, identify the affected units and consumers, including textually unchanged consumers. Reopen those obligations and the necessary coverage and assembly judgments. Preserve acceptance of genuinely unaffected units.

Handle moved passages, line-number changes and editorial changes through an explicit scoped comparison. Automate exact-byte passage relocation where possible; obtain the acknowledgment the protocol requires. Do not label a change editorial merely to avoid review.

Maintain whole-file and passage bindings without copying the entire evidence set into every record. Cache mechanical results by the complete relevant input and checker versions. Invalidate the cache when those inputs change.

## Keep parallel work compatible

Use one integration owner and one selected integration candidate at a time. Give workers stable input contracts, disjoint output ownership and explicit acceptance criteria. Reviewers assess the exact submitted candidate.

Workers return a focused proof/edit and its review evidence. They do not rebuild the entire project inventory or release archive. Reuse shared source checks when applicable; each actual application still needs its own justified match.

Do not run competing integration scripts or replay a possibly live job. Check actual process identity and terminal state first. Preserve drafts and failed attempts when they matter to the audit.

## Keep the trust boundary explicit

Under the default protocol, published theorems are external inputs after the required source-version, correction, hypothesis and convention checks. Do not silently expand the task into reproving the entire published literature.

Inspect relevant proof passages when needed to resolve ambiguity, establish applicability, or investigate a concrete concern. A known substantive objection cannot be ignored because the theorem was published. Record the concern, its effect on the project and its reviewed resolution or unresolved status.

Check all substantive uncited inputs too. Calling an input standard does not exempt it from the inventory.

## Separate mathematical progress from administration

Report separately:
- unresolved mathematical or source-applicability questions;
- accepted arguments awaiting incorporation or current-use review;
- mechanical checks and release work.

Count accepted obligations at a defined scope, not files, tokens, agent activity or repeated checks. Label planning percentages as estimates. A component review is not whole-proof acceptance.

When tools fail, use one recovery owner, bounded retries and backoff. Preserve exact errors and distinguish an unstarted request from a live job. Continue independent work where possible. Do not create duplicate workers or new paperwork to keep the system looking busy. Report a persistent external blocker without weakening the verification standard.

## Plan and rehearse the release

These operational checks preserve the selected protocol's assurance level. They add no mathematical review role, mandatory extra human, permission, or service.

Bind the primary release to an immutable commit and exact artifact hashes. Keep incidental hosting metadata, such as a workflow URL or displayed status, outside the identity of the material being reviewed. If a build or check consumes a generated merge commit, tree or other derived artifact, pin its exact identity as a stage input and invalidate affected checks when it changes. Check delivery state, freshness and authorization separately; do not omit security-relevant inputs from those checks. Do not redefine the primary candidate merely because a hosting service refreshed its metadata.

Before an expensive run, preflight the complete path from the selected inputs through validation, evidence assembly, publication and readback. Exercise the actual commands, schemas and consumers in a safe local rehearsal or supported dry run; identify any live-only checks still pending. Include missing, stale or malformed evidence, an interrupted stage, a failed publication and a retry after partial success. Where signed evidence already exists, check that the selected verifier accepts its exact historical formats, identities and trust configuration. Do not relabel, re-sign or rewrite old evidence to make a compatibility check pass. A mock transport does not establish live authentication or freshness.

Split expensive validation, evidence assembly and publication into independently resumable stages. Record each stage's complete relevant inputs, checker and configuration versions, output hashes and observed terminal result. Preserve successful stages when those bindings remain unchanged. If a relevant input or checker changes, invalidate and rerun the affected stage and its dependent checks; never reuse a success merely because filenames match. Before retrying a writer, check its actual process or remote job identity, terminal state and any completed side effects. Resume safely from that state instead of duplicating an action.

Assign one recovery owner. After two unexplained infrastructure failures in the same stage, diagnose the captured errors and reproduce the failing step at the smallest useful scope before another expensive full run. Continue independent proof, review or packaging work meanwhile. A retry must address the diagnosed cause or be justified by evidence that the external condition changed. Do not weaken a failed check or discard its evidence.

Give each phase an elapsed-time, compute and storage budget based on a measured sample or prior comparable run; label initial estimates. Report the current phase, job identity, elapsed time, last observed progress and exact error location without exposing secrets. Record actual phase costs and revise estimates as evidence arrives. Exceeding a budget calls for inspection and a recovery decision, not an arbitrary timeout that kills a possibly healthy job.

Prepare publication commands and destinations during preflight. After expensive validation passes, keep final publication short: check current bindings and authorization, transfer the exact validated artifacts, and read back the destination identity and required files. A delivery failure alone should not repeat unchanged expensive validation. Stop once the selected protocol's closure and release checks pass.

## Finish once the specified checks pass

Agree on each task's acceptance criteria before execution. After they pass, close the task. Reopen it only for a relevant change, a concrete finding or a demonstrated coverage omission.

After the final substantive repair, complete the protocol's independent assembled-proof and coverage review. Reproduce the required computations from the selected release artifacts. A clean ledger or passing CI cannot replace these mathematical judgments.

Build the cumulative handoff and synchronize the manuscript, README, inventories, findings and artifact index for each research release as the protocol requires. Do not repeat the whole release pipeline after each internal proof edit.

Use ordinary CI or local scripts to validate records and detect stale evidence, with the protocol's required negative tests. Do not claim that these scripts prove mathematical truth or completeness. Publish, send messages or change access only within the owner's existing authorization.

Once all actual closure and release obligations are satisfied, stop the cycle and report the evidence. Do not invent further rounds merely because another round is possible.
