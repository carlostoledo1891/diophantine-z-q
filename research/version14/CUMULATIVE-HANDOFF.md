# Cumulative Version 14 handoff

Download the [cumulative research ZIP](https://github.com/elliotglazer/diophantine-z-q/releases/download/quartic-299-version-14/z-in-q-version14-supplement.zip). The November 9, 2026 manuscript and standalone GI artifacts are identified in [ARTIFACT-INDEX.md](ARTIFACT-INDEX.md).

| Binding | Value |
| --- | --- |
| Archive size | 221,978,813 bytes |
| Archive SHA-256 | `6025a0af2835a239c5dcd03f4aa4f8987f16c0fb5a7deae7f49089aefaf7ec9d` |
| Archive source commit | `ceb028b95dd5d485586baa824badf0eb856567cb` |
| Build and restoration receipt | [RELEASE-RECEIPT.json](RELEASE-RECEIPT.json) |
| Source protocol check | [Successful App check](https://github.com/elliotglazer/diophantine-z-q/runs/129408252578) |
| Source map and final inputs | `cumulative-source-map.json` and `release-inputs.json` inside the ZIP |
| Gate evidence | `post-gate/` and `post-gate-manifest.json` inside the ZIP |

The ZIP preserves source commit `ceb028b95dd5d485586baa824badf0eb856567cb` and the protocol check for that source. This guide is subsequent delivery documentation. The delivery commit requires its own release check on GitHub; the source check does not approve a later commit. The archived source documents retain the pending-delivery wording they had when frozen. The ZIP's separate final-input and post-gate records resolve those source-time placeholders.

## What is preserved

The cumulative design preserves the exact Version 13 archive, whose SHA-256 is `10787487f46ebfefe931e2e7db163a2e8bd0605b3c0325534a47cd93dd43b01b`, and adds a selected Version 14 layer. The retained research-annex intake contains 1,939 logical rows. It is bound by intake SHA-256 `e554a9051acbf8716c8a3d328a58254ef4d8e9edcd4ed0c7a862e8c8fde6cefe`. This is the retained intake identity, not the digest of the final cumulative ZIP. The separately verified research annex preserves those 1,939 logical rows in 1,643 distinct content objects. Its collection review checked the exact membership, byte hashes, original statuses and required O4 companions. This collection acceptance does not turn historical research into accepted mathematics. Duplicate historical destinations and content objects have different counting rules. Use the generated archive manifest for membership.

The history includes proof proposals, rejected attempts, corrections, source/application records, independent scoped reviews, and computational and build evidence. Original scientific statuses remain unchanged. Inclusion means the material belongs in the research record; it does not mean every claim was accepted or that an old review applies to a later version. Current mathematical decisions retain their exact source and application bindings.

Conversations, private correspondence, credentials, purchased source PDFs, external-paper page images and full external-source extracts are excluded. References to their source hashes and bibliographic locators may remain. The final cumulative PDF and nested-archive rules are narrower than the standalone GI package. Its proof-only ZIP, guide PDF and historical PDFs must not be assumed present in the cumulative selection. Preserve the standalone package separately; use the final selection and omission records to determine which cumulative files are delivered.

## O4 encoding history

The two damaged O4 drafts are encoding-failure history, not active proof suppliers. Their SHA-256 identities are `bdb5b23d0b654c40c867b938351e4c0bb71cc4fc0cc5491e104a0a75eee080dd` and `4221666760319755413521826b1b7c08fc196ca6b917c48b609898d38d5e8ab2`. Selecting either requires all three companions:

```text
O4-ENCODING-HISTORY.md 77eed581cd186f706936679eab70ec20a994eb258bf87fe2de9d1ff77ba1fed8
readable PROOF.md     ee499c7392ad089ec36b90d116223a693ab7949331d390a8e0de6217801a26ae
PROPOSED-RESOLUTION   e4e0728fbc1ea6e393dc192878d6fb61839141371bcb3b2baa6c4c45dc687ad0
```

The readable successor narrows the mathematics as well as repairing text; it is not merely a character-encoding conversion. Original holds remain historical decisions. The proposed relationship record is `research/version14/evidence/release-completion-003/v14-handoff-content-successor-root-004/O4-COMPANION-INDEX.json`. Resolve it through the final history manifest and check the companion bytes.

## Verification and historical runners

Verify the archive against the SHA-256 above, extract it and run `python -B restore.py NEW_DIRECTORY`, choosing a directory that does not exist. Do not restore over a working research tree. Restoration materializes the selected repository and retains the research-annex ZIP. It does not automatically expand the annex. The 1,939 rows name logical destinations in the annex manifest, whose contents use content-addressed storage. From the restored repository, the selected package's finite replay command is:

```sh
python -B quartics/quartic-299-314/verify_lineage.py
```

It checks 28 stages, coefficient tables and coordinate maps. It does not prove the inherited analytic, geometric or arithmetic inputs. Source-binding checks are separate:

```sh
python -B scripts/check_audit_history.py --self-test
python -B docs/manuscript-revisions/version14/validate-applications.py --repo . --self-test
```

The standalone GI archive has its own `verify.py`. Do not apply its full membership manifest to a cumulative subset that deliberately omits files. Final selection-specific checks must account for those omissions explicitly.

Historical scripts are evidence, not instructions to overwrite their old outputs. Several expect the original workspace layout. In particular, `apply-dispositions.mjs` expects `fs` from `node:fs/promises`, `path` from `node:path`, and `crypto` from `node:crypto`; `base` is the workspace root, `risk` is `base + '/work/source-risk-review-20261107'`, and `shas` computes the SHA-256 hexadecimal digest of bytes. Its final `nodeRepl.write` may be replaced by `console.log` in a standalone runner. Output files use exclusive creation. Replay only in an isolated workspace or with new output paths. The accompanying provenance records identify which results were executed by the reviewer and which used a separately credited executor.
