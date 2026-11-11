# Original huge-polynomial machine specification

This directory now includes the exact portable original expression ordinary-integer-definition.json (SHA256 4d639d4c44e69ea360d36d4591b8fdc82269d68b9363af0157d1e5c1174c7af6, 23,179,783 bytes), its pinned precision input and the existing supported reproduction package. It has 292,890,231,904 rational witnesses and one free input. It is a finite expression specification, not an expanded monomial table.

The [historical README](README.md) and [source manifest](SOURCE_MANIFEST.json) retain their exact original bytes and status language. Their old release links and claims describe that historical package, not Version 15 approval. [Copy origins](../review/huge-spec-integration-014/COPY-ORIGINS.json) bind all 28 copied files.

Use Python 3.11 or later and Node.js 22 or later, with Node on PATH. From the repository root, run `python scripts/check_construction.py --report build/construction-checks.json`. The unchanged checker verifies all 25 source-manifest members, works in a temporary directory, regenerates the expression, compares the exact hash, recomputes syntactic bounds and runs four finite suites. This does not regenerate the precision input from its earlier machine or prove the arithmetic premises.

No construction/SOURCE_MAP.json was found in the historical source tree. The adopted Version 15 manuscript now names the available SOURCE_MANIFEST.json, which records historical source paths and hashes. This resolves the current companion-name discrepancy; it does not manufacture a historical map or claim that optional historical-original normalization was replayed. The historical README is preserved unchanged. The exact wording correction was reviewed in the source-first proposal decision and adopted in staging016.
