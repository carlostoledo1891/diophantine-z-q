# Unsigned substantive packet inputs

This builder uses the accepted schema-2 packet and v1.3 coverage formats. It does
not introduce a new gate policy. It prepares exact target requests without
signing a receipt, generating an acceptance or authenticating an author.

The command is:

```powershell
<reviewed-python> -B work/protocol-v13-20261107/substantive-packet-author/build_packet.py `
  --repository <local-Git-repository> --context <actual-context.json> `
  --contract <reviewed-release-contract.json> --reports <actual-reports.json> `
  --findings <findings.json> --finding-bodies <original-bodies.json> `
  --profile <reviewed-protected-profile.json> --output <new-directory-under-substantive-packet-author>
```

Every input file is explicit. The output directory must stay under this author
directory. Repeating identical outputs is allowed; replacing different frozen
bytes is rejected. No checkout, candidate program, network request or credential
lookup is performed. The repository must already contain the complete objects.

## Actual context and release contract

Context has exactly `repository`, `repository_id`, `pr`, `base`, and `head`.
Use the actual repository name, positive numeric repository/PR IDs, and complete
commit IDs. The collector verifies the full commit/tree/blob manifests. It does
not authenticate that GitHub currently associates the commits with that PR;
protected ingress must establish that later.

The release contract has exactly these fields:

| Field | Value |
| --- | --- |
| `schema` | `unsigned-research-release/v1` |
| `policy_sha256` | Existing protected runtime audit-policy digest |
| `policy_paths` | Explicit protected policy path/prefix list |
| `changes` | Complete reviewed change records described below |
| `applications` | Actual authored ordinary schema-2 applications |
| `coverage_record` | Head pin to the committed substantive dossier |
| `coverage_author_runs` | Actual authors of the coverage proposal/assembly |
| `assembly_author_runs` | Complete actual assembly authors, including every application, coverage, report and finding author |

Each change has exactly `path`, `kind`, `applications`, `base`, and `head`.
`base` and `head` are the complete file entries from the collected manifests, or
null when absent. The set must equal the complete Git change set, including
reports, coverage files, workflow changes, documentation, binaries and modes.
`kind` is `argument`, `source`, `computation`, `editorial`, or `policy`.
`applications` lists ordinary applications of that same kind which bind every
present base/head version of the file. Policy paths must use kind `policy`.

Each ordinary application uses exactly the existing fields `id`, `kind`,
`authors`, `dependencies`, `files`, and `obligations`. Supply the nine authored
obligations from the accepted core schema; the builder never writes mathematical
justifications or changes an unresolved status to checked. File pins contain
exactly `side`, `path`, and `sha256`. Dependencies must name ordinary supplied
applications and be acyclic. Do not supply a coverage application or an ordinary
dependency on the reserved coverage ID.

The builder adds `protocol-v1.3-coverage` with kind `coverage`, the supplied
coverage authors, and dependencies on every ordinary application. It binds the
dossier, governing protocol, initial reconstruction and proof sources. The
ordinary change classification must still cover all changed coverage files.

## Report and finding inputs

The report manifest is a nonempty list of objects with exactly `path`, `sha256`,
`bytes`, `author_runs`, and `scope`. Reports must already exist in the head tree
as regular mode-100644 files and match the exact bytes. Existing report paths
may be retained unchanged; replacing a historical report is rejected. A report
is evidence, not an automatic decision on the new target.

Findings use exactly the existing fields `id`, `body_sha256`, `status`, `reason`,
`authors`, `applications`, and `duplicate_of`. `finding-bodies.json` maps every
finding ID to its original UTF-8 text. Their digest and set must match. The
builder preserves open or unresolved dispositions; the real gate will still
reject closure until they are resolved and independently accepted. No known
finding may be omitted from the actual protected intake merely because it is
absent from these author inputs.

## Coverage inputs for the joiner

Use the existing complete specification in
`../gate-author/adapter/COVERAGE-V1.3.md`. Its schema is unchanged.

The protected profile has exactly `schema`, `protocol_version`,
`governing_protocol`, `runtime_policy_sha256`, `mode`, `claim_ids`, `proof_paths`,
and `allowed_nonmath_paths`. Here `schema=protocol-coverage-policy/v1`,
`protocol_version=1.3`, `mode=substantive`, and `allowed_nonmath_paths=[]`.
`claim_ids` is the nonempty announced-claim application inventory. `proof_paths`
is the complete independently reviewed source inventory. The governing path is
`docs/research-review/PROTOCOL.md` with exact user-supplied SHA256
`d3eb878bb3fb12d3b27d157e33f417f6f81bf2a873370f2758e8ccb1e5314d0a`.
The runtime audit-policy digest is a separate identity and must equal the
contract's `policy_sha256`.

The substantive dossier has exactly:

```text
schema = protocol-coverage/v1
profile_sha256 = SHA256 of canonical protected profile JSON
mode = substantive
sources = exact head pins for proof_paths
scope = actual scope and limitations
coverage_index = complete passage records
initial = head pin to the preserved initial reconstruction JSON
reconstruction = actual source-first process attestation
reconciled_uses = complete final source-use table
declared_edges_before = preserved pre-comparison edge inventory
declared_edges = final ordinary-application direct edge inventory
reconciliation = preserved discrepancy/disposition records
```

The initial JSON has exactly `schema=protocol-source-first/v1`, `sources` equal
to the dossier's source list, and `uses`. It must already be committed and
preserved. Reconstruction has exactly `run_id`, `method`, `prior_exposure`,
`limitations`, `frozen_at`, and `compared_at`. The accepted gate requires that
run ID to be the eventual coverage reviewer and the recorded freeze time to
precede comparison. That reviewer must be independent of the proposal and
ordinary application authors by actual agent identity. Run labels alone do not
establish independence.

The existing supported route requires the coverage reviewer to attest their own
reconstruction. Separate source-first slice reviews may be preserved as
evidence. Their author identities and chronology must not be relabeled as one
reviewer's work. A different multi-reviewer protocol would require separately
reviewed gate changes; this builder does not implement one.

Coverage index rows, source uses, assertions, suppliers, locations, edges and
reconciliation histories retain all fields specified in `COVERAGE-V1.3.md`.
Locations use one-based inclusive line ranges and SHA256 of the exact raw
excerpt, including line endings. Reconciliation IDs are `use:ID` or
`edge:CONSUMER->SUPPLIER`, with before/after canonical digests and preserved
disputed/rejected/resolved histories. Initial omissions, added/deleted uses,
changed edges and extra edges must be handled by the existing full gate rules.

The builder checks source inventories, all nested pin/excerpt bindings, complete
source-line and announced-claim coverage, declared graph equality, and missing or
stale reconciliation for changed rows. It does not call the gate with fabricated
receipts to claim complete coverage acceptance. The complete supplier, use,
reconciliation, author-independence and final decision checks remain in the
accepted gate after actual authenticated evidence is available.

## Outputs and next boundary

Outputs are `packet.json`, `coverage-profile.json`, `targets.json`,
`report-manifest.json`, `finding-bodies.json`, both complete manifests, and
`PREPARATION.json`. Every target is explicitly awaiting actual independent
final-target review. No previous receipt is copied onto the new base/head
binding. A real reviewer may expressly adopt earlier content where appropriate,
but coverage and assembly still need actual current decisions.

The output profile remains an author proposal until independently reviewed and
installed inline in the protected controller job. The candidate repository may
not select its own runtime profile. Root must perform the existing owner-event,
signed intake, selected-report and live evaluation workflow after reviews.

The synthetic tests exercise real local Git objects and explicitly synthetic
reports. They do not create production observations or claim mathematical review.
