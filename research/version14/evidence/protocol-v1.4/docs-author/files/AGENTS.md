# Research review and reporting

Before classifying a mathematical objection, closing a review item, or claiming that a manuscript incorporates an earlier audit, follow [the audit integration protocol](docs/audit-history/PROTOCOL.md).

Read the actual earlier argument, not only its verdict. Keep historical justification and incorporation into the current manuscript separate. Record exact sources, conventions, hypothesis checks, and the consuming passage. If the history has not been checked, say that it is unresolved rather than calling a repair new. A passing structural or computational check is not proof of the arithmetic theorem.

For every changed theorem application, compare the source's required inputs with the objects actually constructed. Explicitly check index-set coverage, transition maps and the identity of the object consumed downstream. Review a changed route anew even when its conclusion was accepted earlier. Follow the contract and independent-acceptance requirements in the protocol; do not let a historical approval authorize a revised argument.

Run `python -B scripts/check_audit_history.py --self-test` after changing the register, current manuscript, application contracts or their bound sources. This checks both immutable history and current acceptance. Do not refresh hashes merely to silence a failed check; review the changed application first. Never generate an independent approval on behalf of a reviewer. User instructions take precedence. This protocol introduces no additional permission requirement.

The governing [mathematical research review protocol](docs/research-review/PROTOCOL.md) is version 1.4. For substantive source-to-consumer transitions, record the available result, the needed assertion and the exact derivation connecting them. After a substantive failure, review plausible related uses within a justified scope and compare all current repetitions of the corrected assertion. Preserve historical evidence. A scoped component acceptance is not final assembled-proof or release acceptance. The local audit-history checker implements only its documented subset of these requirements.
