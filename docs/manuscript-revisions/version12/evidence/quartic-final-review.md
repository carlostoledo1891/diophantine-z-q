# Independent re-review after the serialization repair

Reviewer: `/root/astra_bl5_models`. Decision: accepted. Date: 2026-11-07.

This fresh acceptance binds `docs/manuscript-revisions/version12/quartic-application.json`, SHA-256 `3bb26b28713cbcea81061e6d2e4cbfab371164ed630fd510d5020d7646d0d15c`, to the unchanged `manuscripts/quartic_v12.tex`, SHA-256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`.

## Change reviewed

Linux CI exposed a byte-serialization difference: the builders used the platform default line ending, while the frozen intermediate-file hashes require CRLF. The repair explicitly sets `encoding='utf-8', newline='\r\n'` on the JSON writer in six builders and on the JSON/text writers in the download-table renderer. The manifest changes because those seven source files change. Its own line-ending change is also immaterial to its parsed entries but correctly changes its file hash.

I read the Git diff and `portability/serialization-repair.json`. I independently checked all seven before/after source hashes against Git and the working tree. Comparing parsed Python ASTs gives exact equality after removing only the added encoding and newline keyword arguments from `write_text` calls. The numerical operations, residual construction, assertions, pin checks and verification conditions are unchanged.

The writer arguments serialize strings constructed with LF separators. Explicit CRLF translation therefore reproduces the frozen Windows bytes on either platform; it does not change JSON values. JSON string content is escaped by `json.dumps`, so the newline option does not alter embedded mathematical data. The table renderer likewise joins its rows with LF before writing.

I validated all 82 entries of the revised manifest against actual file sizes and SHA-256 hashes. Exactly seven parsed manifest entries differ from the prior manifest, corresponding to the seven reviewed source files. Both final candidates and both polynomial files retain their previously accepted hashes. I separately regenerated all four download tables in an isolated directory using the repaired renderer. Each is byte-for-byte identical to its frozen counterpart, including the 690,922-byte ordinary text table.

## Retained mathematical acceptance

The original full final review is preserved at `portability/initial-quartic-final-review.md`, SHA-256 `a62b33ae131cfb54a1ecc64d780af3ebbb8716e0c5dfdeab1d8249f9c7a539cd`. It accepts all nine obligations of the selected 498-variable construction and 514-variable coefficient lift within the stated inherited arithmetic scope. The detailed `evidence/composition-review.md` and `evidence/integration-review.md` also remain unchanged. Their mathematical reasoning is retained here; it is not being inferred anew from a serialization test.

The revised contract differs only in evidence and the dependency-impact paragraph. Its source records, author list, nine obligations, three reviewed-edit fingerprints, manuscript binding and construction/application/consumer spans are unchanged. I rechecked all revised evidence pins and raw manuscript span hashes. The new diagnostic accurately describes the source changes and unchanged mathematical data. The previous acceptance was invalidated by the changed bound manifest, and this is a newly authored acceptance of that new binding.

This review accepts the serialization repair and carries forward the prior mathematical decision without enlarging it. It does not claim a new Linux CI pass. The author reports that a local full replay is being run; no completion of that run is assumed here. The previously recorded portable verification describes its original package and must not be presented as a Linux verification of this repaired package. A fresh Linux CI result remains a separate execution check.

Kato's contract and acceptance are unchanged. The inherited restricted converse, point-group input, height theorem, prime-pattern argument and other unchanged arithmetic dependencies retain the exact qualifications in the original review. No whole-manuscript proof certification is implied. No further correction is requested for the revised contract and serialization-only source changes.
