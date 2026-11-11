# Inputs required to finish the Version 14 records

This packet is an authoring and installation component. It is not the final
application inventory. `install_inventory.py` cannot run successfully without
the complete records described here. No default empty records or fallback
acceptance files are provided.

## Read-only assembled repository

The `--repo` directory must contain the exact final
`manuscripts/quartic_v14.tex`, the author's final
`docs/manuscript-revisions/version14/addition.tex`, and the exact new-edit list
at `docs/manuscript-revisions/version14/new-edits.json`. The addition must occur
byte-for-byte exactly once in the manuscript. The installer does not normalize
line endings. Both the complete file and each span use SHA256 over raw bytes.
Line numbers are one-based and inclusive. Spans use `splitlines(keepends=True)`.

The same directory must contain the retained Version 13 sources and the frozen
`quartics/quartic-299-314` artifact package. Its source archive supplies the R6
relation, manifest and repair history. The schema pins the selected source IRs,
expanded polynomials, compact tables and coordinate maps. The independent
artifact verifier remains responsible for recomputing the full sums of squares.
The inventory validator binds those exact reviewed files; it does not claim to
perform a second polynomial expansion.

The artifact package manifest has SHA256
`5369f80f69742958ea31f3a32b62b43e6b23b284063e6870af2dc2f0073977fb`.
The symbolic299 and ordinary314 counts and coefficient qualifications are fixed
in `validation-schema.json`. Other accepted ordinary companions are archival
alternatives, not substitutions for selected314.

## Final APPLICATIONS input

The JSON passed as `--records` has these fields:

- `schema`: `portable-application-inventory-v3`.
- `status`: `author_records_pending_independent_review`.
- `selected`, `baselineInventory`, `baselineManuscript`, `routeSelection`,
  `r6Relation`, `r6Manifest`, `repairHistory`, `finalArtifacts`: exact copies of
  the fields in the pinned validation schema.
- `manuscript`, `addition`, `edits`: portable `{path,sha256}` file pins for the
  final files named above.
- `externalSources` and `existingSourceCatalog`: exact Version 13 values,
  retaining the existing source qualifications. A newly justified revision of
  these values requires a new schema/component review, not a silent installer
  override.
- `assemblyOrder`: the exact 24-element `assemblyTopologicalOrder` in the route
  selection. This is a finite derivation graph, not a list of current theorem
  applications.
- `mathematicalAcceptanceClaim`: the literal JSON boolean `false`.
- `applications`: 39 records in the schema's baseline order.
- `edgeBindings`: one record for each of the 263 canonical R6 edges.

Each application has its baseline `id`, the SHA256 of the canonical prior
record in `priorRecordSha256`, an exact copy of the prior `source` object in
`sourceVersionAndConventions`, and nine nonempty current obligation strings in
`obligations`. The nine keys are listed in `inventory_core.OBLIGATIONS`.
`BASELINE-ADAPTATION.json` supplies the 39 prior hashes and author comparison
notes. It does not supply or approve the final obligation strings.

For each of those nine keys, `dependencyDisposition` contains:

```json
{
  "mode": "preserved or replaced",
  "justification": "The actual reason the old or new statement applies to the current objects and consumers.",
  "sourceSpans": ["one or more exact raw-byte span objects"],
  "consumerSpans": ["one or more spans of the current assembled manuscript"]
}
```

A preserved obligation must retain its prior string exactly. Preserving a
string still requires an explanation and source/current-consumer spans. Changed
object domains, scalar factors, exceptional cases or construction order require
an explicit current statement and semantic review. Merely saying that the old
paragraph is unchanged does not establish unchanged applicability.

A span object is `{path,sha256,start_line,end_line,sha256_raw_utf8_span}`.
An optional `label` must occur once in the entire file and within the span.
`inventory_core.bind_span` constructs and checks a span after the final file
hash and line interval have been selected. It does not decide whether the
interval proves an obligation.

Each edge binding has `applicationId`, `entryId`, `role`, `justification`,
`sourceSpans` and `consumerSpans`. The roles are `current_consumer`,
`supporting_derivation` or `archived`. Archived edges have empty span lists;
they must not claim current consumption. All other edges need exact source and
current manuscript spans. A current entry in the route selection needs at
least one actual current consumer. A candidate edge may be archived with an
explicit reason. Supporting entries cannot be relabeled as direct current
applications; unused and superseded entries cannot become current by assertion.
This reconciles every research edge without declaring every edge consumed.

The route dispositions themselves are author work awaiting independent review.
If the final mathematical review changes them, preserve this frozen component
and prepare a reviewed successor rather than editing its pin.

## Contract and evidence

`--contract` is an already authored `QUARTIC-299-COMPOSITION` application
contract in the repository's existing contract format. It must bind the final
manuscript, all its new mathematical/source edits, actual authors, all nine
contract obligations, source versions, evidence and construction/application/
consumer spans. Evidence must include the exact generated APPLICATIONS bytes.
Use `install_inventory.encoded(records)` to compute that future file pin.
This serialization is indented UTF-8 JSON with a final LF; canonical record and
edit hashes separately use sorted compact UTF-8 JSON.

Evidence files can already exist in the read-only assembled repository, or be
supplied through `--evidence-plan`. A plan is a JSON list of
`{source,target,sha256}`. Source names are relative to the plan file's directory;
targets are portable paths below `docs/manuscript-revisions/version14/evidence/`.
Every copied evidence file must actually be referenced. The unchanged
`ROUTE-SELECTION.json` is copied to `evidence/route-selection.json` by this plan.
The final contract or inventory must reference any additional copied report.

No reviewer identity or acceptance decision is generated. Final non-author
proof review, structural review, source-first coverage under protocol v1.3,
and current-registry incorporation are separate inputs/stages. A local name in
JSON is not independent authentication of a reviewer. The parent orchestrator
must retain the actual observed authorship/review provenance.

## Installation and ownership

Run the following on one line, with actual paths replacing the examples:

```text
python -B install_inventory.py --repo ASSEMBLED_READ_ONLY_REPO --records FINAL_RECORDS.json --contract FINAL_CONTRACT.json --evidence-plan EVIDENCE_PLAN.json --output NEW_STAGE_DIRECTORY
```

The output directory must not exist and must be outside the read-only
repository. The tool writes a new staging directory only. It emits
`APPLICATIONS.json`, `validation-schema.json`, `validate-applications.py`,
`quartic-application.json`, `GUIDE.md`, copied referenced evidence, and
`inventory-install-manifest.json`. The manifest records exact output hashes
and every read-only dependency used by validation.

The installer deliberately does not create `current.json`, acceptance records,
carry-forward approvals, or merge authorization. The policy release builder
should integrate the reviewed staging files only after receiving the actual
independent records. Existing historical files remain untouched. The installed
validator supports `--repo . --self-test`; it reports structural consistency
only. Its five built-in mutation tests do not replace the larger author and
independent test suites.
