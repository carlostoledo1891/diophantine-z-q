# Unsigned version 1.3 packet preparation

This builder prepares a non-substantive documentation-adoption packet from actual future Git commits. It does not check out files, execute repository programs, create a PR, sign records, publish reviews, or invent observations. The original v1.2 rollout remains separate.

## Inputs and trust

Use the reviewed six-document manifest at `../docs-author/r2/MANIFEST.json`. The original accepted five-document revision remains preserved at `../docs-author/MANIFEST.json`. The six-document revision adds the main README's current-protocol link and clarifies that AGENTS.md and the audit-history procedures remain applicable. AGENTS.md itself stays unchanged because it is an existing workflow source pin.

Supply the real repository path and exact future PR context with `repository`, numeric `repository_id`, numeric `pr`, full `base` and `head` commit IDs. The Git collector verifies complete commit/tree/blob manifests without checkout or lazy fetching. It does not authenticate the current GitHub PR or the operator's asserted repository identity. Protected ingress must do that later.

Supply one or more actual report descriptors with `path`, `source` and `author_run`. `source` is the local file containing the exact report bytes. Each repository report path must be new under `docs/research-review/`. Reports must already exist in the head commit and match those bytes. Reports are preserved evidence, not automatic acceptance. A final eligible reviewer must explicitly decide the exact packet targets later.

Supply the actual committed coverage dossier path and local source file, its actual author run labels, and the separately reviewed protected coverage profile. The builder supports `non_substantive` mode only. The profile fields are

```text
schema = protocol-coverage-policy/v1
protocol_version = 1.3
governing_protocol = {path, sha256}
runtime_policy_sha256
mode = non_substantive
claim_ids = []
proof_paths = [explicit reviewed unchanged proof/source artifacts]
allowed_nonmath_paths = [exact six documents plus actual reports and dossier]
```

The governing protocol must name `docs/research-review/PROTOCOL.md` with the owner's exact v1.3 SHA256. The runtime policy digest is the existing protected gate policy identity. The two hashes have different roles. The dossier fields are `schema`, `profile_sha256`, `mode`, `sources` and `scope`. Its schema is `protocol-coverage/v1`. Every source is a head pin containing `side`, `path` and `sha256`. The source set must equal the nonempty protected proof-path set, and every corresponding base/head Git file entry must be identical.

The builder checks these bindings but does not establish that the operator chose the complete proof-path set. Independent review must assess the protected profile and the non-substantive scope. A policy-only adoption does not recertify historical mathematical work or satisfy the substantive v1.3 coverage requirements for a new full proof-closure claim.

## Packet structure

The exact changed-path set is the six reviewed documentation paths plus the supplied new report paths and dossier. All document, report and dossier files must be regular mode-100644 files. Every other Git file entry must remain identical. The supplied v1.3 bytes and historical v1.2 bytes are fixed by SHA256 even if an operator supplies a different document manifest.

The policy application covers the complete documentation/evidence change set. Its conservative author list includes the text author, integrator and dossier authors. The reserved `protocol-v1.3-coverage` application has kind `coverage`, binds the head dossier and governing protocol and all protected proof-source pins, and depends on every ordinary application. Ordinary applications do not depend on the coverage application. This direction avoids a dependency cycle and makes the coverage target change when a covered application changes.

The coverage target requires its own non-author decision and authenticated receipt in the gate. The builder emits only target requests marked as awaiting independent review. Assembly authors additionally include all supplied report authors and finding authors. Caller-supplied run labels are not authenticated by this tool. Findings preserve their supplied bodies, hashes, dispositions and author labels. Unresolved findings remain unresolved.

## Invocation

Use a reviewed Python interpreter and record its version and executable identity.

```powershell
& <reviewed-python-interpreter> -B work/protocol-v13-20261107/packet-author/build_packets.py `
  --repository <actual-local-repository> `
  --context <actual-pr-context.json> `
  --policy-sha256 <protected-runtime-policy-sha256> `
  --reports <actual-report-descriptors.json> `
  --dossier-path <committed-dossier-path> `
  --dossier-source <actual-dossier-file> `
  --coverage-profile <reviewed-protected-profile.json> `
  --text-author-run <actual-text-author-run> `
  --integrator-run <actual-integrator-run> `
  --coverage-author-runs <actual-dossier-author-runs.json> `
  --findings <actual-findings.json> `
  --finding-bodies <original-finding-bodies.json> `
  --output <directory-inside-packet-author>
```

Outputs are `packet.json`, complete base/head manifests, `coverage-profile.json`, `targets.json` and `PREPARATION.json`. Existing different output bytes are rejected. The output profile is a proposal to install through the protected configuration workflow, not authority conferred by a candidate repository file.

Fourteen synthetic tests use temporary Git repositories. They check actual committed source and report bytes, the new coverage schema, full unchanged-file coverage, dependency direction, immutable output behavior, fixed v1.3/v1.2 hashes, unchanged proof artifacts, required reports, profile binding, missing dossier sources, preserved unresolved findings and executable-mode rejection. The coverage schema test uses explicit synthetic in-memory test data for the post-authentication validation routine. It emits no receipt and proves no real review happened.
