# Research review and reporting

Before classifying a mathematical objection, closing a review item, or claiming that a manuscript incorporates an earlier audit, follow [the audit integration protocol](docs/audit-history/PROTOCOL.md).

Read the actual earlier argument, not only its verdict. Keep historical justification and incorporation into the current manuscript separate. Record exact sources, conventions, hypothesis checks, and the consuming passage. If the history has not been checked, say that it is unresolved rather than calling a repair new. A passing structural or computational check is not proof of the arithmetic theorem.

For every changed theorem application, compare the source's required inputs with the objects actually constructed. Explicitly check index-set coverage, transition maps and the identity of the object consumed downstream. Review a changed route anew even when its conclusion was accepted earlier. Follow the contract and independent-acceptance requirements in the protocol; do not let a historical approval authorize a revised argument.

Run `python -B scripts/check_audit_history.py --self-test` after changing the register, current manuscript, application contracts or their bound sources. This checks both immutable history and current acceptance. Do not refresh hashes merely to silence a failed check; review the changed application first. Never generate an independent approval on behalf of a reviewer. User instructions take precedence. This protocol introduces no additional permission requirement.
