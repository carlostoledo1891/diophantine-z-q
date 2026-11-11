# Coverage dossier assembly

This helper assembles an unsigned protocol 1.3 dossier from the root's supplied records. It does not author mathematical assertions, create review decisions, authenticate identities, sign observations, or change finding dispositions. The root remains the actual dossier assembly author. The source reconstruction and final coverage review remain with the independent reviewer.

The implementation reads the existing gate modules from `work/protocol-v13-20261107/gate-author/adapter`. It uses their canonical serialization, schema helpers, profile selector and timestamp parser. Its multi-error diagnostics are preparation checks, not a replacement gate. The separate `validate-records` command calls the unmodified `offline_manifest_gate.check_records` on supplied packet, evidence and blob bytes.

Run with the pinned Python:

```powershell
& 'C:/Users/glaze/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B work/quartic-v14-prep/coverage-assembly-tools/assemble_coverage.py assemble --input ROOT-SUPPLIED-INPUT.json --out work/quartic-v14-prep/coverage-assembly-output
```

The input must have exactly these keys:

| Key | Value |
| --- | --- |
| `schema` | `coverage-assembly-input/v1` |
| `author_run` | The actual root assembly author's operator-local run ID |
| `profile` | Complete standard `protocol-coverage-policy/v1` profile |
| `scope` | Actual authored dossier scope text |
| `initial` | `{file, sha256, pin}`, preserving the original initial JSON bytes |
| `blobs` | List of `{pin, file}` for every consumed source, including the governing protocol and external supplier locations |
| `applications` | Hash-pinned JSON file containing the full ordinary application list, or exactly `{applications: [...]}` |
| `uses` | Hash-pinned JSON file containing the final standard use list |
| `coverage_index` | Hash-pinned JSON file containing the complete standard index list |
| `declared_edges_before` | Hash-pinned JSON file containing the actual pre-reconciliation edge list |
| `edge_reasons` | Hash-pinned JSON object mapping each final `CONSUMER->SUPPLIER` to its actual authored reason |
| `reconciliation_histories` | Hash-pinned JSON list of `{id, before_sha256, after_sha256, history}` with actual complete histories bound to the current targets |
| `preserved_reconciliation` | Hash-pinned JSON list of prior reconciliation rows; use an explicit empty list only if none existed |
| `findings` | Hash-pinned JSON list of all preserved actual packet findings, including open findings |
| `reconstruction` | Hash-pinned JSON object with the independent reviewer's actual reconstruction metadata |
| `proof_inventory` | Hash-pinned independent inventory review JSON containing the accepted `sources`; if it includes `initial_sha256`, that binding is checked |

A hash-pinned JSON reference is exactly `{"file": "...", "sha256": "..."}`. All file paths resolve relative to the assembly input file. A source pin is exactly `{side, path, sha256}`. Source paths in pins are repository paths. Local file paths are never substituted into those pins.

The current independently accepted inventory is `work/quartic-v14-prep/independent-source-review/PROOF-INVENTORY-REVIEW.json`. It lists the manuscript, pole proof and interpreter-precision proof. Its sources must match the preserved initial source list exactly, including order. The profile must list exactly those proof paths. The helper does not add sources to that accepted inventory.

The catalog must contain final ordinary applications, with their actual files, authors, obligations and direct dependencies. Do not include the reserved coverage application. The helper does not create that application or its reviewer receipt. It also does not convert family catalogs, placeholder consumers or author proposal locations into final standard records.

Histories use the existing schema:

```json
{
  "id": "use:ACTUAL_USE_ID",
  "before_sha256": "CANONICAL_SHA256_OF_THE_ACTUAL_BEFORE_RECORD_OR_NULL",
  "after_sha256": "CANONICAL_SHA256_OF_THE_ACTUAL_AFTER_RECORD_OR_NULL",
  "history": [
    {
      "status": "disputed",
      "reason": "Actual recorded explanation.",
      "finding_ids": ["ACTUAL_FINDING_ID"]
    }
  ]
}
```

The example illustrates shape only. Replace the placeholders with actual canonical record hashes, or JSON null when that side is absent. Supply actual text, IDs and dispositions. The helper computes the expected bindings and checks both supplied hashes; it never supplies the explanation or a terminal `resolved` entry. Every changed, added or deleted use/edge receives a reconciliation row. An edge without source uses also requires an explicit reconciliation history, as the deployed schema requires. Missing current history yields an empty history and an unresolved report. Earlier history stays in the preserved input/output and must be included as an exact prefix when the root supplies the complete current history. If either target hash differs from the preserved row, the current history must append a new explicit disposition. Copying the old terminal resolution is insufficient even when the caller updates the hashes. An unchanged, explicitly bound target can retain the same history. A binding mismatch, erased prefix, malformed preserved row or missing new disposition produces an empty dossier history so the deployed validator also rejects it.

Outputs are deterministic canonical JSON without timestamps:

- `profile.json` and `dossier.json`.
- `unresolved.json`, including exact missing line ranges, uncovered claims, unknown IDs, missing direct edges, cycles, source/record schema errors, missing explanations and open findings.
- `preserved-findings.json` and `preserved-reconciliation.json`, canonical semantic copies without changing any supplied fields.
- `manifest.json`, recording the actual author string, every consumed file hash, relevant validator file hashes and output hashes.

The command returns 2 for unresolved inputs and 0 only for a clean local preflight. It still writes the incomplete dossier and diagnostics when the input container can be read. Hash mismatches or malformed input containers fail before writing. A clean preflight is not a review acceptance. The output does not silently fill uncovered lines, change classifications, add catalog dependencies, drop duplicate rows, or close findings. Both commands refuse to overwrite any supplied input or mapped blob, including resolved path aliases and existing hard links.

For final record validation, supply the actual packet and operator evidence:

```powershell
& 'C:/Users/glaze/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B work/quartic-v14-prep/coverage-assembly-tools/assemble_coverage.py validate-records --packet PACKET.json --evidence ACTUAL-EVIDENCE.json --profile PROFILE.json --blob-map BLOB-MAP.json --out VALIDATION.json
```

The blob map is a JSON list of `{pin, file}`. It must provide every base/head blob needed by the packet, including the assembled dossier and exact initial JSON. The deployed validator checks those bytes against the packet's Git object metadata. This command does not authenticate the evidence; the protected operator intake must do that separately. It creates no observations or receipts.

Tests use the existing validator's explicitly synthetic fixture. No synthetic result is production evidence. From this directory:

```powershell
& 'C:/Users/glaze/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B -m unittest -q test_assemble_coverage
```

The tests cover deterministic CLI output, all required input hashes, retained history, unresolved findings, missing lines, claims and direct edges, unknown suppliers, cycles, stale excerpts and inventory pins. Two assembled synthetic dossiers also pass through the unmodified deployed validator.
