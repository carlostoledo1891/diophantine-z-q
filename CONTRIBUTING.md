# Contributing and reviewing

Mathematical corrections, dependency checks, reproducibility reports, and improvements to the formalization are useful contributions. Please make each report specific enough that another reader can reproduce the issue.

For proposed changes, follow the [research review guide](docs/research-review/README.md) and the [complete mathematical research review protocol](docs/research-review/PROTOCOL.md). They specify PR evidence, non-author review, treatment of every audit objection, and closure on the exact final revision. For a research release, identify the project release profile and include the cumulative research handoff and synchronized release records. For a non-release change, explain which release duties do not apply and why. The guide links the live rulesets for current enforcement. Existing CI alone does not establish full protocol completion.

For proof-coverage claims, include the complete coverage index, the non-author's frozen initial source-use reconstruction, its reconciliation with the declared inventory and direct dependencies, and the separate coverage decision required by protocol v1.4. Preserve differences and their reviewed dispositions. Record prior exposure, exact proof and supplier versions, and any unreviewed passage or unresolved supplier. Changes to a supplier contract or an affected proof require renewed coverage review. Existing application acceptances alone do not establish completeness. Identify every substantive source-to-consumer transition and its derivation. After a substantive failure, include the bounded review of related uses and the check that repeated current assertions incorporate the correction. Preserve prior evidence and obtain non-author acceptance of the affected scope.

## Mathematical reports

[Open an issue](https://github.com/elliotglazer/diophantine-z-q/issues/new) with:

1. The manuscript version, exact commit or file hash, and the theorem, equation, TeX label, certificate step, or archive file under discussion. Identify the edition listed as current in the README, the October 11 manuscript, or the particular historical revision.
2. The exact step that needs justification or correction.
3. The relevant hypotheses, definitions, and external theorem statements.
4. A counterexample, calculation, proposed repair, or precise explanation of the missing implication, if available.

Distinguish a false statement from an incomplete justification or an unclear exposition. Source-application checks should identify the actual theorem and verify its hypotheses, including fields, integral structures, normalizations, and quantifier order where relevant.

Maintainers responding to a report must follow the [audit integration protocol](docs/audit-history/PROTOCOL.md). Record prior justification and current manuscript incorporation separately, with exact evidence and consuming passages. Do not describe a repair as new mathematics without inspecting the historical arguments. The [Issue 2 register](docs/audit-history/issue2/README.md) illustrates this distinction.

## Computation and formalization reports

Include the source file and hash, toolchain version, command, and relevant output. Keep a failing example small when possible. Specify whether the result concerns a historical draft, a helper lemma, an accepted production module, or the main statement.

For a proposed Lean proof, include the exact declaration and its dependencies, the compilation result, and an axiom report. Changing a definition, adding an assumption, or weakening a conclusion is a statement change and should be identified explicitly. Successful compilation of a helper module is not a proof of the main theorem.

For a computational certificate, distinguish how the certificate was found from how it was checked. Record the input and certificate hashes and the checker version.

## Proposed changes

Keep changes focused. Explain the problem, the resulting behavior or mathematical statement, and the checks performed. Preserve dated release artifacts; propose a new version rather than replacing a historical snapshot. Avoid including credentials or unrelated private files in logs.

The repository README records the collaboration credit and distinguishes the October 11 manuscript's provenance. If AI tools contributed to a proposed proof, computation, or review, describe that contribution and the verification performed. Acceptance depends on the argument and evidence supplied.
