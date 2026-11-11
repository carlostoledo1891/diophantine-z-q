# Research review for contributors

Follow the [mathematical research review protocol](PROTOCOL.md), version 1.4, for mathematical claims, constructions, computations and repairs. This directory contains the complete standalone protocol. [Version 1.3](protocol-v1.3.md), [Version 1.2](protocol-v1.2.md) and [Version 1.1](protocol-v1.1.md) are retained as historical policy. The [audit-history protocol](../audit-history/PROTOCOL.md) explains the repository's existing contracts, findings records and checks.

Version 1.4 governs research-review completion. The repository's [AGENTS.md](../../AGENTS.md) and [audit-history procedures](../audit-history/PROTOCOL.md) still apply to local checks, contracts and historical findings.

## Enforcement status

The live [public repository ruleset](https://github.com/elliotglazer/diophantine-z-q/rules/26781429) and [private repository ruleset](https://github.com/elliotglazer/private-diophantine/rules/26781446) are authoritative for current enforcement. Before treating a merge as protocol-gated, confirm that the applicable ruleset requires `Protocol / independent agent audit` from the designated GitHub App and that it passes for the exact revision. Existing CI alone is insufficient. This document does not assert that the App requirement is already active.

The App check must bind its decision to the reviewed repository, PR, base, head and merge revisions, evidence manifests and audit history. Contributor-written reviewer names, acceptance flags or receipts cannot authorize that check. Trusted observations and policy are managed separately. A check records an evaluation cutoff; it does not promise instantaneous detection of later comments or an atomic comment-and-merge transaction.

The [current review record](../audit-history/current.json) states the manuscript's existing scope and inherited qualifications. Installing this protocol does not expand that scope or retroactively certify the complete proof.

Historical research releases and reviews retain their original standard and scope. Adopting v1.4 does not recertify them. Full closure requires the source-first coverage and reconciliation retained from v1.3, plus reviewed connecting arguments, related-use checks after substantive failures, and consistency of corrected current assertions.

The controller now includes independently reviewed v1.4 support at commit `582200ce3f46e8c0682eaa38a4f519f887c6a515`. Its approved-revision readback and empty-queue smoke check passed; see the [activation record](../../research/version14/evidence/protocol-v1.4/runtime/ACTIVATION.json) and [run result](../../research/version14/evidence/protocol-v1.4/runtime/DEPLOYMENT-READBACK.json). This confirms runtime deployment, not acceptance of a mathematical PR. Each candidate still needs the protected v1.4 profile and exact reviewed evidence. Historical v1.3 checks do not establish v1.4 acceptance. The [adoption record](ADOPTION-V1.4.md) distinguishes policy, runtime and release status.

The protected controller must bind the governing protocol, runtime policy, permitted mode and proof-source inventory. The existing substantive mode checks linked coverage records, direct dependencies, reconciliation and authenticated non-author decisions. A narrowly reviewed non-substantive mode covers only its declared policy or editorial change; it cannot certify the complete proof. V1.4 also requires review of the available and needed conclusions at each substantive transition, related occurrences after failures, and current repeated assertions. Automated checks establish only the recorded relationships and bindings they implement. Source completeness and mathematical adequacy require the specified review.

## Evidence to include in a PR

Link repository-relative evidence files and identify the exact commit and SHA-256 hashes reviewed. Include uncommitted evidence explicitly while preparing the packet, then bind the final committed revision. Keep secrets, local absolute paths and unrelated private material out of the packet.

1. Trace each claimed result to internal proofs and identified published theorems. Record the publication venue, authoritative version, statement, definitions and corrections actually used. Supply project proofs for needed unpublished inputs. State unresolved assumptions instead of claiming complete verification.
2. Inventory every cited application and substantive uncited external input. For each, address all [nine application obligations](PROTOCOL.md#the-nine-application-obligations), including conventions, connecting maps, exceptional cases and the precise downstream object. Have a non-author reviewer reconstruct the substantive uses from the frozen proof sources, freeze that initial reconstruction, then reconcile it with the declared inventory and dependency graph.
3. Supply explicit constructions and computations. Record domains, simultaneous parameter choices, algorithms, constants, exact inputs, certificates, checker commands and reproducible outputs. Distinguish a generator or compressed representation from a full expansion, and a finite identity check from its arithmetic application.
4. Register every received human or model audit and every substantive objection in the findings ledger, including unfavorable reports and comments on closed issues. Link each finding to a reviewed repair or an independently checked rebuttal. Preserve unresolved findings and earlier verdicts; a majority vote or silence does not resolve an objection.
5. Repeat independent review, repair and integration until the final frozen revision meets the protocol's [closure test](PROTOCOL.md#final-closure-review). Recheck changed premises, affected consumers and computations after each substantive repair. Obtain an independent review of the assembled proof, rather than inferring completion from component approvals.

For a documentation-only or infrastructure PR, identify the unaffected mathematical claims and explain which obligations do not apply. A PR can report incomplete work honestly; it must not mark an unreviewed argument as accepted or a finding as resolved.

## Source-first coverage and reconciliation

Follow the protocol's [independent dependency reconstruction requirements](PROTOCOL.md#independently-reconstruct-and-reconcile-dependencies) before claiming full closure.

- Assign a non-author reviewer to reconstruct inputs from the frozen statements and proofs, including appendices and linked proofs. Record prior exposure to inventories or verdicts. The declared graph and earlier favorable reviews must not become the initial checklist. Freeze the initial source-use table before reconciliation.
- Supply a coverage index for the complete argument. Identify each statement and proof passage, including unnumbered passages, with its version, location, review status and associated source-use entries. Explain passages outside the claimed proof and reviewed passages with no substantive imported input.
- For each substantive use, state the actual required assertion, objects, hypotheses, quantifiers, parameter range, uniformity, constants, normalizations, exceptional cases and limit order. Name the exact supplier or inline derivation and the application record. Include section-only internal uses and unnamed estimates.
- Reconcile every genuine use with its actual direct supplier and application. Preserve the initial table, both inventory versions, differences, reviewed dispositions and disputed findings. A transitive path or matching theorem name does not establish a reviewed direct use. Check extra graph entries too.
- Obtain a distinct coverage decision bound to the coverage index, initial and reconciled source-use tables, reconciliation and frozen proof sources. The eligible reviewer may also assess applications or assembly, but must record those scopes separately. An unreviewed required passage, missing checked supplier or unresolved reconciliation difference prevents full closure.
- Recheck affected source-use entries, contracts, consumers and coverage decisions after substantive changes. Keep earlier records and decisions. An omitted edge is a review finding to assess, not by itself a proof that the mathematical inference is false.

The required implementation checks are linked-record consistency, stale coverage and supplier-contract detection, and rejection of unresolved required reconciliation. Omission tests must cover a named theorem use, a section-only internal use and an unnamed estimate, deletion of a referenced source-use entry, and a changed supplier contract without renewed affected review. Record actual automated results separately from the non-author mathematical coverage decision. These tests cannot establish that every input was found.

## Connecting arguments and corrections

For every substantive transition, identify the exact supplying conclusion, the assertion consumed next, and the derivation or reviewed lemma connecting them. Distinguish a source statement from a proof passage, construction, application or reviewer's assertion. Check relevant adverse cases and avoid circular justification. Reviewers must say whether they reconstructed a derivation, reused an identified exact prior derivation, or only checked consistency; consistency alone cannot accept a required connection.

After finding an invalid inference or an unestablished connection, define a bounded search for other plausible occurrences in the actual proof and its consumers. Preserve candidate locations, scope limits, dispositions and a non-author coverage decision. A narrow repair does not establish a broader proposition or renew its other uses.

Compare every current repetition of a corrected assertion, including manuscript text, linked proofs, supplier contracts, inventory fields and summaries. Correct or explicitly retire incompatible current statements while preserving historical originals. Keep proposal, scoped acceptance, incorporation, affected-use review and final release acceptance distinct.

Apply the protocol's probability and stopping checks only where those features occur. For other arguments, inspect the corresponding changes of domain, normalization, quantifier, approximation or limit order; give specific reasons for nonapplicability.

## Research release maintenance

For every research release, follow the protocol's [release maintenance and research handoff requirements](PROTOCOL.md#release-maintenance-and-research-handoff). Identify the reviewed project profile that defines required artifacts, names, locations, thresholds, publication destinations and reproduction entry points.

- Update the cumulative handoff with current and relevant prior research and reviews. Retain negative results and superseded evidence with their status, correction links and provenance. Exclude conversational transcripts, credentials and unrelated private files from the release handoff.
- Update the archive index and release manifest with the source commit, version, date, authorship, review status, open work, reproduction entry points and artifact hashes. Preserve prior editions and their manifests.
- Synchronize the README, current manuscript source and built PDF, artifact catalog, handoff, source/application inventories and findings ledger. Check version and date agreement, source-to-PDF build identity, citation and credit changes, and the precise representation supplied for each construction artifact.
- Validate links and required artifact coverage. For configured public/private mirrors, review the intended contents and permitted differences, then compare the authorized published readbacks with the reviewed release manifest.
- Record the reviewer, exact evidence and results. For a non-release PR, explain which duties do not apply and which artifacts remain unaffected. Report machine-check coverage separately from review of completeness.

## Independent review and exact versions

An application author cannot independently accept that application. Record reviewer identity, whether the reviewer is human or a model, the model and task identity when known, tools, reviewed files and scope. Unknown model metadata must remain unknown. Another run by the same agent is a repeat check. If a reviewer supplies a substantive repair, obtain a different non-author review of that repair.

Review the primary statements and actual manuscript argument, including their consumers. Compare publication versions, errata, coefficient rings, bases, signs, valuations and all other relevant conventions. Check that the manuscript edition, build target, PDF, artifacts, inventory and release manifest name the same revision. Preserve historical editions. Version 13 and later manuscript subtitles have no trailing period.

An acceptance covers only its exact bound files, sources, edits and dependencies. Further changes require a reviewer-authored decision for the new binding. Even an editorial change needs an explicit acknowledgment after comparison; it need not trigger a full mathematical audit when the comparison establishes that the mathematics is unaffected. Do not refresh accepted hashes merely to make a checker pass.

## Checks and final handoff

Run the focused checks relevant to the change. The existing audit-history check and its rejection tests are:

```sh
python -B scripts/check_audit_history.py --self-test
```

Run this command from the repository root. Include its result and limitations in the PR. The [research-checks workflow](../../.github/workflows/research-checks.yml) lists the existing computational and build checks; a small documentation change does not require running every heavy job locally.

Before final acceptance, freeze the assembled revision and record its exact changes, review decisions, findings dispositions and reproduction results. New changes or substantive objections reopen affected obligations. Keep the proof's mathematical status separate from coverage and execution status: structural checks cannot establish complete source coverage, honest independent reasoning or mathematical truth. Publication remains a separate maintainer decision.
