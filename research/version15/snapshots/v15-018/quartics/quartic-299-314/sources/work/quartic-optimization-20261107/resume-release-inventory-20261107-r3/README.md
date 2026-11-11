# Preparatory inventory revision 3

This revision corrects the two findings in the independent review of r2. It preserves r2, its manifest, its review and the original adverse results unchanged. It is an author-prepared correction awaiting independent inventory review. It grants no mathematical or publication approval.

The candidate cutoff is unchanged from r2: 22 canonical IRs, with combined315 selected, three accepted ordinary lifts on exact319, and the separately accepted sparseLucas320. Later sparse315 and ordinary-sparse315 packets are outside this inventory cutoff. This exclusion is not a claim that they remain unreviewed. The selected 315-variable construction remains above the strict publication threshold.

## One relation and all its projections

`relation_spec.py` is the explicit, manually reconciled specification. `CANONICAL-RELATION.json` is its frozen data form. Each edge names a baseline application, an internal entry, its mathematical reason, its source proof and its selected or alternative component scope. An edge means a direct changed application, exact transport or explicitly restored hypothesis. It does not claim that every edge is new arithmetic or that all transitive consumers are listed.

The r2 application and entry lists disagreed on 38 edges affecting 23 applications. `EDGE-DECISIONS.json` records every disputed edge, its two old states, the decision and the reason. This is not an automatic union. In particular:

* N02 and N03 do not modify the unchanged Ui/Vi identity-inclusive chart extension. Their H/V0 reconstruction branches are different objects.
* N03 does not change the primary biquadratic identities. N09 and N13 explicitly consume those identities for their valuation arguments.
* N13 restores local comparison depths; it does not change the separate beta-to-input parity lemma.
* N07 restores S parity and the old anchor. The scalar torsion/log step still uses its existing integral group identity and local formal cases.

These five disputed edges are excluded. Two additional edges present on both r2 sides are also excluded: the N12 Laurent chain is not a constant-pivot elimination, and the N22 Lucas recentering does not alter the input parity lemma. The remaining disputed edges are included for the specific restoration or consumer role recorded in the specification. For example, N16 restores the old anchor bound explicitly consumed by the scalar-height inequality, and N18's forward private map belongs in the final completeness construction.

The resulting relation has 117 edges. `APPLICATION-DELTA.json` generates both `application.newEntryIds` and `entry.baselineApplications` from that relation. `INTEGRATION-MAP.json` generates its consumer links from the same relation. The original baseline source and consumer records remain unchanged. Each old r2 list is retained in a field named with the `revision2` prefix.

## Source-specific ordinary status

The current machine classification of `V13-ORDINARY-GATE` is now `accepted_exact319_ordinary_lifts_only_no_selected315_lift_in_scope`. Its separate scope object identifies the accepted source exact319 and the three 334/335/336 artifacts. It says explicitly that a selected315 lift is not included at this cutoff. The obsolete r2 classification is retained only as historical data.

This classification distinguishes the two equal-count 319 constructions and does not promote an ordinary lift across a source change. Full candidate hashes and review records remain in `CANDIDATES.json` and `CANONICAL-INDEX.md`.

## Validation and retained outline

`validate_relation.py` requires equality of the canonical edge set, all application lists, all entry lists and the entire integration map. It rejects duplicate or unknown endpoints, scope drift and changed consumer spans. It also checks the exact ordinary-lift classification and source scope.

`check_revision.py` verifies the frozen source pins and unchanged r2 packet, baseline source/consumer records, outline hash and labels. Ten negative fixtures cover an omitted application edge, extra application edge, omitted entry edge, omitted map edge, duplicate canonical edge, unknown endpoint, scope drift, changed consumer span, obsolete ordinary classification and an unauthorized selected315-lift claim. All ten are rejected. `CHECKS.json` records the result.

`PROOF-INTEGRATION-OUTLINE.tex` is byte-identical to r2. Only its consumer map changes. Its local labels remain proposed exposition, not production theorem labels. The recorded MiKTeX setup limitation remains; no compiled PDF is claimed. Full manuscript statements, application contracts and independent review of any future exposition remain separate work.

Reproduce from the workspace root with the recorded Python interpreter:

```text
python -B work/quartic-optimization-20261107/resume-release-inventory-20261107-r3/build_revision.py
python -B work/quartic-optimization-20261107/resume-release-inventory-20261107-r3/check_revision.py
```

The builder reads the immutable r2 packet and source specification. It does not import or execute candidate code. No production inventory, manuscript, controller, candidate or author proof file has been modified.
