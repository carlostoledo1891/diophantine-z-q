# Combined source revision 003 integration review

Decision: accepted for installation of this exact combined manuscript and its exact curated payload, subject to the normal build and layout check. This is a source-integration decision, not release or whole-proof acceptance. Reviewer: `/root/astra_v14_source_review`, run `local:v14:source-first-review:20261107`. Date: 2026-11-08.

The reviewed manifest is `work/quartic-v14-prep/combined-source-revision-003/MANIFEST.json`, SHA256 `028a787e6dd717b7a98edfd1b87ec1ceb7beb1193a52159614551efa05ab6731`. The base is `80b2fd21c6e33b65d8b4cc1976d5a073ac8f6ffd156ed8e3bbb4e63ce5c75d7c`. The combined candidate is `fa53dcc19ad2d9efb43aa8e44fcbd514479ea216838dcbb64a4ab39fe12a67fd`, 1,108,177 bytes. `EDITS.json` is `48a03b3ed900fba7e8751bf3f2e2b8a0fcc7b61b0ab56d1a89f614922a9806bb`; `MANUSCRIPT.patch` is `843a186fa381b445f63068bf8519700504f7b75704f91bd8ca51c7f0f7aa2ae4`.

## Component decisions and independence

The scalar supplement incorporation was independently accepted in `PAN-CLOSED-IMAGE-INCORPORATION-DISPOSITION-001.md`, hash `19a315b821292d167a244ce06dddce5825ae4957bb43fbcf730a986c40ab7318`. It supplies only the scalar closed-image inference at Pan Lemma 3.5.9, with admissibility and universal completion retained.

The utility incorporation was independently accepted in `PAN-UTILITY-INCORPORATION-DISPOSITION-001.md`, hash `4a633c9fe08a25a88109866671c4bca8c70d44655ee2ff56d76c9245b79c0507`. It carries the four accepted local utility conclusions and their retained premises, not the full Pan theorem.

The rational parity substitution was independently accepted in `DOKCHITSER-PARITY-DISPOSITION-001.md`, hash `618124132b5a0ecb1ab588c8c728b0fbc2a83030ba1492e9a2f55980300e8621`. Its external supplier is the actual final Annals rational Selmer parity theorem, not an inferred equivalence of Crelle editions.

For the prime-five assembly, I read the two distinct independent decisions and the actual successor proof. Root's `pan-p5-incorporation-root-review/REVIEW.md`, hash `585f2ce6a68a2e573f14f7d0c54300b7a1dea82ce178c2948da1794375370081`, accepts Sections 1–5 and the unchanged Section 6 arguments, explicitly excluding the new localization paragraph and zero-rank case which root helped specify. The Gaussian decision `pan-p5-incorporation-independent-gaussian-001/REVIEW.md`, hash `40cd8b350419487580015c367b1a4561ec8e704b2b27d0d35b38ccc770ab2d83`, accepts that exact additional connection and its zero-rank case. Together they cover the selected successor `c25ce6ee7d67c6b841599e2ec8ffbd89a6e9263c6b4410f3fca75f4a2af1b4e3` at their stated bounded scope. I do not issue a new independent mathematical acceptance of the geometric construction to which I contributed. My present decision checks its incorporation against those other reviewers' decisions.

The prime-five successor also serializes the unchanged proof text with CRLF line endings. I retain the successor's exact hash and the Gaussian report's distinction between unchanged mathematical text and unchanged raw bytes. No old acceptance hash is silently transferred to new bytes.

## Actual combined passages

I read the full combined diff, the two Pan application contexts and their downstream paragraphs. At the first application, the prime-five footnote remains attached to the original Pan citation. The scalar paragraph stays intact between that citation and the no-residual-proviso sentence. The utility footnote attaches to the latter sentence. All three identify internal steps in the detailed Pan proof, and each retains its own premises. The assembled text does not identify Pan's auxiliary characteristic-five representation with the manuscript's characteristic-zero multiplicity representation.

After these insertions, the original character-twist discussion continues unchanged. The first occurrence still uses the separately supplied local-algebraicity route. The repeated occurrence still uses the weight/determinant route, expressly without that local-algebraicity theorem. The new supplements do not change those arguments or purport to derive their inputs.

At the repeated Pan application, the utility, prime-five and scalar notices follow the same original author/final-version qualification. Their order does not change a proof dependency. The scalar notice still states admissibility and universal completion. The other notices still state their inherited premises. None claims final Pan text equivalence, solves every transitive dependency, or replaces modularity with a utility lemma.

The parity edits are disjoint from these passages. Both actual applications still concern the same fixed E_l over Q at p=2 with full Selmer corank one. The combined text preserves the divisible-Sha convention and the ordering before BFH and theta choices. The summary and bibliography select the same final Annals source. This change neither assumes finite Sha nor extends that theorem to arbitrary number fields.

The bibliography contains the scalar published source and supplement, the prime-five and utility project entries, and the revised parity item. Each inserted citation resolves to a unique key in the combined candidate. The project URLs match the respective copied paths. They become usable after the exact files are installed and published; this review is not evidence that publication has occurred.

## Exact replay and payload

`check_combined_source_003.py` independently reproduced each of the four isolated candidates from the common base, then checked all thirteen combined edit steps against their before/after hashes. It matched the combined candidate exactly. The shared anchors remain unique at each step. No unlisted source changes were needed. It also checked all seventy manifest references and verified all twenty-six copied public files against their supplier files, totaling 177,171 bytes. Only Markdown and JSON occur in that payload. Results are in `COMBINED-SOURCE-CHECKS-003.json`.

The overlap order is safe. The scalar insertion leaves the original Pan citation available for the prime-five footnote. It leaves the original no-residual-proviso sentence available for the utility footnote. At the repeated occurrence, successive insertions preserve all three notices. Successive bibliography insertions preserve their original end marker and create no duplicate key. The retained line-ending rules were followed bytewise rather than normalized across the manuscript.

The unchanged scalar and utility payloads retain their prior acceptance scopes. The prime-five payload retains exact component supports and reviews, with the successor proof hash separately identified. Its historical `assembly_status` and pending-status sentences must remain historical. The new root and Gaussian assembly decisions, and this integration decision, must accompany current adoption; the old component-only `REVIEW-SCOPES.json` is not by itself evidence of assembly acceptance.

## Required downstream binding and limits

The new line-addressable project proof sources must be protected and included in the current source-use inventory. For this integration they include:

- `docs/research-review/proof-sources/pan-scalar-closed-image/proof-v1.md`.
- `research/version14/proofs/pan-utility-p5-v1/CONNECTIONS.md`.
- `research/version14/proofs/pan-p5-sw99-v1/proof.md` and its actually consumed support files `support/transfer-original.md`, `support/geometric-p5.md`, `support/sw69-uniformity.md`, and `support/eigenvalue-p5.md`.

Retain the support-file precedence stated in the prime-five proof. The geometric proof resolves the original C1 restriction only at five; the uniformity note supplies the two-entry condition; the eigenvalue proof replaces only the specified p52 route. Including these files does not reaccept every alternative historical claim they contain. Review records supply evidence of decisions and do not replace these proof sources. The earlier three protected proof paths and any other accepted additions still need their existing coverage; this list is not a complete final proof-path inventory.

I made no live changes and did not perform the PDF build or visual check. Root may install the exact accepted candidate and payload after those checks, preserving the old source and recording the new hashes. Current application locations, dependency records, source-version qualifications and audit-history bindings must then be updated explicitly. Final Pan matching, the other retained external and local premises, full GI, whole-manuscript coverage and release approval remain outside this bounded integration decision.
