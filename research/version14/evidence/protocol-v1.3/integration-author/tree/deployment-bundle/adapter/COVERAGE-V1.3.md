# Protocol 1.3 coverage adapter

This adapter checks coverage records against immutable Git blobs and existing
authenticated operator receipts. It does not prove a mathematical argument,
discover every omitted input, establish how a reviewer reasoned, or authorize a
merge. The supplied protocol is preserved verbatim in `PROTOCOL-V1.3.md`, SHA-256
`d3eb878bb3fb12d3b27d157e33f417f6f81bf2a873370f2758e8ccb1e5314d0a`.

## Selecting the governing protocol

Pass a protected operator `coverage_profile` to `evaluate_session`, `evaluate`,
`LedgerEvidenceBridge`, `validate_offline`, or `check_records`. Do not obtain it
from candidate repository code or an unreviewed packet field. The controller
must load it from its reviewed configuration and pass it explicitly to the
live evaluator. The current live reader's `policy_path` is
`docs/audit-history/PROTOCOL.md`; its policy hash does not identify the human
research protocol. The profile binds both identities.

The profile has exactly these fields:

```json
{
  "schema": "protocol-coverage-policy/v1",
  "protocol_version": "1.3",
  "governing_protocol": {
    "path": "docs/research-review/PROTOCOL.md",
    "sha256": "d3eb878bb3fb12d3b27d157e33f417f6f81bf2a873370f2758e8ccb1e5314d0a"
  },
  "runtime_policy_sha256": "EXACT EXISTING PACKET POLICY HASH",
  "mode": "substantive",
  "claim_ids": ["APPLICATION ID FOR EACH ANNOUNCED CLAIM"],
  "proof_paths": ["COMPLETE REVIEWED PROOF SOURCE PATH INVENTORY"],
  "allowed_nonmath_paths": []
}
```

Only the canonical governing path and supplied protocol hash are supported.
An explicit unknown version/hash/path fails. Without a profile, known v1.1 and
v1.2 packets retain the existing schema-2 record checks and receive the status
`legacy-records-only`. Unknown bytes at the canonical protocol path fail. Exact
v1.3 bytes anywhere in either tree, or a reserved coverage application, require a
profile. A legacy result is never a v1.3 coverage acceptance. Removing, moving or
changing the governing document under a v1.3 profile fails.

The profile digest is SHA-256 of the existing sorted, compact, UTF-8 canonical
JSON representation. The dossier binds this digest. The signed receipt binds the
dossier through its blob hash, together with the complete schema-2 Git binding.
Historical packet, manifest and target digest algorithms have not changed.

## Separate coverage target

Add one application with exactly these fields:

```json
{
  "id": "protocol-v1.3-coverage",
  "kind": "coverage",
  "authors": ["ACTUALLY OBSERVED PROPOSAL AUTHOR RUN"],
  "dependencies": ["EVERY OTHER APPLICATION ID"],
  "files": [{"side":"head", "path":"coverage/dossier.json", "sha256":"EXACT BLOB HASH"}],
  "coverage_record": {"side":"head", "path":"coverage/dossier.json", "sha256":"EXACT BLOB HASH"}
}
```

The coverage application cannot classify changed files. An ordinary policy,
editorial or mathematical application must still cover every actual change.
Ordinary applications must not depend on the coverage application, which would
introduce a cycle. The operator must record actual proposal authors, never
fabricated or copied author identities.

An ordinary authenticated application-target receipt is required for this exact
coverage target, separately from each application and the assembled packet.
The coverage reviewer must differ from every ordinary application's authors and
the coverage proposal's authors, by immutable agent identity. The same eligible
reviewer may write other decisions; a second run by an author is insufficient.
The coverage decision must state its scope and adopt the complete bound records.
Signed ledger intake, retained reports, author observations, exact target and
dependency digests, report blobs, and live source bindings continue to apply.

## Substantive dossier

The JSON dossier has exactly `schema` (`protocol-coverage/v1`),
`profile_sha256`, `mode` (`substantive`), `sources`, `scope`, `coverage_index`,
`initial`, `reconstruction`, `reconciled_uses`, `declared_edges_before`,
`declared_edges`, and `reconciliation`.

`sources` is the exact list of head pins for `proof_paths`. A pin has `side`,
`path`, and `sha256`. `scope` is a nonempty description of the reviewed argument
and limitations. Every consumed blob is checked against its Git object, size
and SHA-256. Coverage reads support line-addressable blobs up to 16 MiB each.
Convert larger or non-line-addressable evidence into a separately reviewed
source representation before using this route; do not silently truncate it.

`coverage_index` rows have `id`, `claim_ids`, `location`, `status`, `reason`,
`use_ids`, and `no_imports_reason`. A location has `pin`, `start_line`,
`end_line`, `excerpt_sha256`. Lines are one-based, inclusive, preserving raw line
endings in the excerpt hash. The index must cover every line of every protected
proof source and every announced claim. Status is `reviewed` or
`outside_claimed_proof`; an awaiting-review passage blocks closure. Outside rows
must have no claimed results or uses and must state a reason. Reviewed rows
without genuine imported dependencies must have an explicit
`no_imports_reason`; otherwise that field is null. A reviewer must assess the
source inventory, index completeness and outside-scope reasons. Covering every
listed line cannot establish that an unlisted source or dependency does not exist.

`initial` pins a separate preserved JSON blob with `schema`
(`protocol-source-first/v1`), the exact same `sources`, and initial `uses`.
Initial use rows preserve the same fields as reconciled rows, including any
unresolved initial supplier. `reconstruction` has `run_id`, `method`,
`prior_exposure`, `limitations`, `frozen_at`, and `compared_at`. The supported
route uses the same reviewer run for reconstruction and coverage acceptance.
Timezone-qualified timestamps must put freezing before comparison. The reviewer
attests their own source-first work, prior exposure and sequence. These text and
time fields do not authenticate an independent clock or prove mental independence.

Each reconciled use has `id`, `consumer` (an ordinary application ID),
`passages` (index row IDs), `assertion`, `classification`, `reason`,
`shared_contract_justification`, `supplier`, `application_id`, `inline_argument`.
`assertion` has nonempty `statement`, `objects`, `hypotheses`, `quantifiers`,
`parameter_range`, `uniformity`, `constants`, `normalizations`,
`exceptional_cases`, and `limit_order`. Inapplicable details need an explicit
reason. All repeated consuming locations must appear in both the use and index;
multiple locations require a shared-contract justification.

Classification is `dependency`, `notation`, `background` or `unused_reference`.
Nondependencies require a passage-specific reason and null supplier/application/
inline argument. A dependency has a supplier with `kind`, `application_id`,
`location`, `statement`, `publication`. Kinds are `internal`,
`published_external`, `computation`, `inline`. An internal supplier names its
ordinary application ID and requires a direct edge in the consumer application's
dependencies. A transitive route is insufficient. The supplier location must be
bound by that supplier application. Other supplier kinds have null application ID.
A published supplier's publication object has nonempty `title`, `authors`,
`venue`, `authoritative_version`, `locator`, `corrections`; other kinds use null.
This records publication evidence; a reviewer must check its truth.

For each dependency, `application_id` names the ordinary application checking
the match, whose files must bind the supplier and all consuming passages.
Alternatively, that field is null and `inline_argument` is an exact checked
location. The separate coverage reviewer accepts that inline argument.

Both edge lists have rows `consumer`, `supplier`, `use_ids`, `reason`. The final
list must exactly equal all ordinary application dependency edges. Each final
edge must list all and only its direct source uses. Extra edges without an actual
use require a preserved reconciliation disposition. The before list records the
inventory found when comparison began, after freezing the initial source table.

Reconciliation rows have `id` (`use:ID` or `edge:CONSUMER->SUPPLIER`),
`before_sha256`, `after_sha256`, `history`. Hashes bind canonical before and after
rows; an absent row uses null. Every changed/added/deleted initial use and every
changed edge requires a row. History entries have `status` (`disputed`,
`rejected`, `resolved`), `reason`, `finding_ids`. Disputed or rejected entries
must reference actual findings in the fully reconciled packet. The last entry
must resolve the difference. Earlier disputed/rejected dispositions remain;
old decisions and packet history are also retained by the existing ledger/Git
workflow. The gate cannot discover an undisclosed audit or deleted author-side
history outside its authenticated intake.

This route requires current source-bound reconstruction records and a fresh
coverage receipt even for editorial changes to those source blobs. The protocol
permits a scoped editorial acknowledgment; an optimized reuse route is not
implemented here. Do not rewrite old reviewer hashes or imply that reuse occurred.

## Policy or documentation change with no mathematical claim

Use a separately reviewed protected profile with `mode: non_substantive`,
empty `claim_ids`, nonempty `proof_paths`, and exact `allowed_nonmath_paths`.
The allowed paths must not overlap the proof inventory. Every changed path must
be allowed and every ordinary application must be policy/editorial. Every
protected proof artifact must be byte-, mode- and object-identical in base/head.
The dossier then has only `schema`, `profile_sha256`, `mode`, `sources`, `scope`.
Its scope must explain the bounded documentation change and the unchanged proof
inventory. The separate non-author coverage receipt remains mandatory.

This outcome is `1.3-non-substantive-scope-only`. It does not certify a complete
proof. The operator and reviewer must assess the allowed paths and the claim that
the change contains no mathematics. Calling an argument file “documentation”
does not justify such a profile.

## Validation and deployment boundary

`test_coverage_gate.py` includes synthetic keyed-ledger tests and negative tests
for missing coverage decisions, omitted uses and passages, direct-edge removal
for named, section-only and unnamed inputs, stale source/supplier/receipt
bindings, cycles, unresolved differences and out-of-scope nonmath changes.
Run `python -B -m unittest -q test_coverage_gate test_manifest_gate
test_store_bridge` from the adapter directory.

All candidate code is isolated. Integration must add `coverage_gate.py` to the
reviewed controller bundle/dependency pins, wire its protected profile through
the job configuration to the live evaluator, and obtain independent acceptance
of exact source/configuration/packet targets before deployment. No tests or
author report in this directory supply that independent acceptance.
