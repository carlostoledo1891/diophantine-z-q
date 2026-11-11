# Version 1.3 independent review checklist

Reviewer `/root/sol_protocol_final_review`. Source-first checklist prepared from the user-supplied protocol, before reading the proposed implementation. Source SHA-256 `d3eb878bb3fb12d3b27d157e33f417f6f81bf2a873370f2758e8ccb1e5314d0a`. Implementation review is pending. This checklist records expected evidence and tests, without asserting that the gate can discover omitted mathematics.

| Requirement | Evidence to inspect | Required structural test or explicit limitation |
| --- | --- | --- |
| Preserve exact source | Supplied bytes, current protocol, separately preserved v1.2 | Hash equality and version/history agreement; reject unsupported version |
| Initial independent reconstruction | Separately authored source-use table, initial hash/version, review conditions and prior exposure | Reject author self-approval, absent initial version or absent exposure record; cannot prove independent reasoning from identity |
| Source-first order | Initial table frozen before reconciliation; declared inventory/graph separately identified | Initial binding must remain immutable through reconciliation; changing initial bytes invalidates decision; timestamps alone do not prove reading order |
| Announced claims and proof scope | Complete proof-source set, claimed results, appendices, linked proofs and unnumbered passages | Reject missing declared source/claim links and stale source bytes; source coverage completeness requires reviewer judgment |
| Passage coverage | Exact file/version, locations/excerpts, reviewed/awaiting/outside status; explicit reason for exclusion or no substantive imported input | Awaiting required passage blocks closure; missing excerpt, missing reason, deleted referenced passage or use fails |
| Substantive source use | Consuming claim/passage, required assertion, objects/hypotheses/quantifiers/ranges, uniformity/constants/normalization/limit order | Required fields and declared links validated; mathematical adequacy separately reviewed |
| Supplier | Exact internal/external/computational/inline supplier, version/location, application or checked derivation | Missing supplier remains unresolved and blocks closure; reject stale source/supplier binding; familiar name supplies no acceptance |
| Classification | Genuine use versus notation/background/unused with passage-specific reason | Reject unexplained exclusion; reviewer assesses whether classification is correct |
| Repeated uses | Every consuming location and one contract covering all | Reject dangling location and missing application links; review whether shared contract suffices |
| Direct dependency | Actual invoked internal result connected directly to consumer, intermediate lemma's own dependencies separately represented | Removing required edge fails even if transitive path or common ancestor remains; include named theorem, section-only internal use and unnamed estimate fixtures |
| Reconciliation | Initial and reconciled tables, graph/inventory hashes, differences, preserved disputed/rejected dispositions | Unresolved required difference blocks closure; deleting difference or altering bound graph invalidates decision; extra graph edges classified with reasons |
| Disposition review | Correction/addition/existing derivation/nondependency evidence, separately authored decision | Reject disposition self-approval, stale evidence or absent decision; substantive new doubts enter findings ledger |
| Separate coverage decision | Explicit acceptance of exact coverage index, initial/reconciled uses, graph, inventory and proof set | Application acceptance or assembly acceptance alone cannot satisfy coverage; separate decision can share an eligible reviewer |
| Dependency changes | Supplier contracts, changed proof/statements and affected consumers | Changed supplier with unchanged consumer paragraph invalidates affected coverage/review; renewed relevant review restores eligibility |
| Editorial change | Scoped reviewer acknowledgment that uses/contracts stay unchanged | Bare editorial label or refreshed hash cannot bypass review |
| Migration | Preserve old records/decisions and v1.2 evidence; explicit incomplete v1.3 coverage until required review exists | Legacy acceptance cannot silently become v1.3 coverage acceptance; old parser route remains honestly version-scoped or blocks unsupported full closure |
| Negative controls | Exact fixtures and observed rejection reasons | Missing domain, consumed-object identity, source change, unreviewed edit, stale acceptance, wrong build target, missing follow-up, corrupt certificate remain tested; add all v1.3 omission controls |
| Reported scope | Gate output, CI name, docs, protocol examples | Describe recorded consistency and change detection; make no claim of finding every omitted inference or proving honest review, independence, mathematical truth or full source coverage |

## Review procedure

Read actual implementation and tests after this checklist is frozen. Trace normal gate entry points and schema/version dispatch, including legacy records. Inspect every closure path for a bypass of new required coverage. Compare actual fixtures with the supplied protocol's omission cases. Run positive and negative tests, record exact file hashes, and issue a separate decision. Preserve this initial checklist when recording later findings or repairs.
