# Independent schema 2 core review

Agent02 accepts the corrected manifest-input offline core at SHA256 `4d57a1b1300dab80957d39857e12a9a5c0926c8dddf5874c5ba1c0d80ff0e5a0`, subject to its explicit external-authenticator contract. One independently found Git-reader failure was corrected and retested. This accepts an offline component, not a live protocol gate, authentic agent-session bridge, GitHub publisher or ruleset deployment.

No shared implementation or published files were edited by this reviewer. Schema 1 remains unchanged. All reviewer files are in `independent-review/adapter/`.

## Source binding

| Source | SHA256 |
| --- | --- |
| `adapter/offline_manifest_gate.py` | `4d57a1b1300dab80957d39857e12a9a5c0926c8dddf5874c5ba1c0d80ff0e5a0` |
| `adapter/git_manifest.py` | `8ca4d7b1ffb49d1a329f5ab8f423b1e415b3c5616f8e6d03a052348f75f9fcef` |
| `adapter/manifest_transport.py` | `e30a0da1349807b370a533bf5f41062013a6b6fee989631cbfc6f499c3f4dc9c` |
| `adapter/MANIFEST-CORE.md` | `a86383bd512fbb1f74f58fd59b849be4af5288cd72114fddb741249844d5018a` |
| Accepted `gate/offline_gate.py` | `2fa1678f4533bfd1067e8b73e8d9ab8a1e85c1716ba9b72dfb4bc9fcd626c5ad` |

The initial schema 2 core, SHA256 `b2374f6eab1e617268c998ffdfac0878a658c6c25cce196f79fbc518da689fcc`, is preserved in `schema2-initial/`. The corrected core differs from that version only in Git subprocess completion/error handling.

## Finding resolved

The initial `GitBlobReader` ignored `git cat-file` exit status. In a freshly initialized bare repository containing no objects, asking it for the empty-blob object produced an empty stdout stream and a Git failure. The empty stream matched the expected empty-blob length and both hashes, so a synthetic schema 2 packet using empty evidence/report blobs incorrectly passed despite the missing source. No nonempty incorrect bytes were accepted, but this contradicted the documented missing-source failure behavior.

The corrected stream closes stdout, waits for process completion, and raises on every nonzero exit. A timeout kills the process and raises rather than accepting its output. The core converts these I/O failures into an invalid evidence-blob result. Independent tests cover a missing empty object, a present empty object, nonzero exit after otherwise correct output, and timeout/termination. The full-core counterexample still fails against the preserved original implementation, as recorded in `schema2-original-reproduction.log`, and passes as a rejection test against the corrected implementation.

## What was checked

`run_schema2_audit.py` independently compares the actual Python syntax trees. Sixteen common top-level definitions are unchanged. The entire block from application processing through changed-path coverage, recursive dependency digests, findings and duplicate disposition digests, authorship inventory, receipt validation and final decisions is identical to the accepted schema 1 block. The binding function adds only `record_schema`. This comparison supplements the manual review of the changed snapshot, pin, reader and CLI paths; it is not a substitute for those checks.

The new snapshot path verifies the complete collector manifest, including raw commit hash/link, reconstructed tree, all paths/modes/object IDs, resource bounds and consistent metadata. It projects exactly `{mode, blob, sha256}` per path, preserving schema 1 content-manifest digests for identical supported content. Independent fixtures check byte-identical maps and digests for both SHA-1 and SHA-256 Git repositories. The full transport, including sizes, totals and raw commit bytes, remains inside the packet digest accepted by the assembly receipt.

Changed-path coverage is still derived from both complete maps. Tests rebuild valid commits/trees before trying to omit a deletion, addition or mode change; fresh synthetic receipts do not rescue omitted coverage. A rename passes only when both the old and new paths are covered. A sparse replacement tree cannot reuse the old binding. Inline schema 1 snapshots do not satisfy schema 2, and receipts with missing, wrong or numeric-alias schema identifiers are rejected.

Every application file pin and every obligation/report pin reaches the byte-verification path. It checks the declared length, Git blob hash and raw SHA-256, and closes the stream on success or failure. Independent tests replace, append or remove base evidence, head evidence and reviewer-report bytes. All are rejected. Cache entries use the full algorithm/object-ID/size/SHA-256 tuple; a claimed same raw digest with a different object ID is read and rejected rather than incorrectly reused. Repeated identical objects can safely reuse one verification because the cache represents content identity, not path provenance.

An unconsumed blob's claimed raw digest is still an external collector assertion. A deliberately dishonest manifest with fresh synthetic receipts can pass the unverified preview. That is an explicit trust boundary: the collector has to authenticate the complete manifest and its computed metadata. The core cannot infer raw SHA-256 values from Git object IDs. An unconsumed size-only change leaves the compatibility map unchanged, but the independent test confirms that it invalidates the old assembly receipt through the complete packet digest. Neither compatibility hashing nor per-object caching permits legacy sparse proxies.

The tests retain independently constructed checks for finding inventory, authorship, parent-policy path protection and duplicate-finding dependency invalidation. A changed target disposition invalidates its duplicate's receipt. The copied non-author and assembly logic remains identical to schema 1, whose complete test suite was also rerun.

## Executed verification

| Suite | Passed |
| --- | ---: |
| Unchanged schema 1 author suite | 53/53 |
| Schema 2 author suite | 44/44 |
| Independently constructed schema 2 suite | 20/20 |

The independent fixture builder reuses this reviewer's earlier synthetic tree/record builder, not the producer's schema 2 fixture or receipt helpers. All its receipts are test data, never authentic review evidence. `SCHEMA2-CHECKS.json` pins the sources and records results; `schema2-audit-*.log` contains the executed suite logs.

The complete real public and private manifests, with 2,254 and 2,816 paths respectively, passed snapshot verification and exact projection comparison. Through the corrected `GitBlobReader`, this review independently selected and checked each repository's largest blob plus a source file, totaling 25,619,557 bytes per repository. It created no review receipts for these repositories. The prior accepted transport review separately recomputed every unique blob's Git hash and raw SHA-256 in both manifests. These local checks do not assert current GitHub head status or repository origin.

## Remaining boundaries

`check_records` remains an unauthenticated structural preview. `validate_offline` requires a caller-supplied authenticator; no authenticator ships here. Missing authenticators or blob readers fail. A synthetic authenticator does not create merge authority: all tested successful results retain `merge_authorized: false`, `deployment_eligible: false` and unimplemented live GitHub state. The CLI's tested success-preview and missing-integration paths exit with code 2, never a deployable success.

`DirectoryBlobReader` and `GitBlobReader` supply bytes only. They do not establish who reviewed them or which live repository/PR selected them. HMAC transport authenticates its key holder only. The operator-attested session bridge, complete registered audit intake, live GitHub acquisition, current CI provenance, final PR/base/freeze reconciliation and isolated publisher remain separate work. No live checks, merges, App setup or ruleset mutations were performed in this review.

The accepted result is an offline schema 2 composition that preserves the reviewed record constraints while permitting complete large-tree manifests. It is not a determination of mathematical truth, semantic completeness or live merge eligibility.
