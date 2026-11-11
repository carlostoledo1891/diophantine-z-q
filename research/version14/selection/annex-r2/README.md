# Research annex successor R2

R2 removes the two external Voight page extracts identified during independent selection review. The first candidate, its manifest and archive remain unchanged. Every retained logical row and content hash is identical to the first candidate, and the original exclusion records remain intact.

The removed files are `review-positive365/VOIGHT-EXTRACT.txt`, 3210 bytes, and `11-anchor-next/voight-223-225.txt`, 8411 bytes. The new exclusions retain their exact hashes, the source PDF hash, source URL, edition and printed-page/theorem locators. They contain no extracted page text. Original research reports and source-application records remain unchanged, including their historical references to the locally inspected extracts.

The candidate archive has 2422 logical files, 1539 unique contents and 318517790 unique uncompressed bytes. Its actual size is 19271803 bytes. SHA256 is `e61d92c3373bb92f6fbb8e8f2d6a3730be665885f98c98374d7f8c838bf96d3d`.

The exact selection SHA256 is `7c6fe7eb7730d424c6d4ad1f81e0a5e895e17da708465d34adb4d6badd5c0c6c`. The content-source map SHA256 is `6f0971d20f75edd8d6ca97924c47e589b7efeba531f5db29bffdd840322fbde0`.

R5 validated the built archive's manifest, exact content set, regular-file status, sizes and hashes. The successor check also confirmed that no retained row changed and every prior exclusion record was preserved. No content was executed, installed or pushed. Independent successor review remains required.

## Additional source-extraction screen

The screen inspected all 1541 distinct contents in the predecessor selection, one file at a time, for page headers, publication imprints and extraction/provenance markers. It also compared 16-word sequences against the two excluded extracts to detect renamed or embedded copies. No retained file matched a 16-word sequence from either extract.

Three retained files triggered marker checks: the project's Version 11 and Version 12 manuscripts, and its optimization manuscript. Manual inspection located ordinary bibliography entries in the first two. The optimization manuscript's marker hits were bibliography entries and `verbatim` blocks containing the project's own Python reproduction commands at lines 9436–9438, 9503–9505, 9580–9587 and 9596–9602. These are not external-source page extracts. The positive-anchor author report and independent review paraphrase the mathematical source and state their application; they do not reproduce the excluded pages.

`SOURCE-EXTRACTION-SCREEN.json` records only paths, hashes, marker categories and overlap counts. No extracted source text is copied into it. This targeted screen found no additional source extract requiring removal; it is not a blanket copyright or privacy guarantee. The prior current-proof/direct-packet exclusions and credential/transcript restrictions continue to apply.

The predecessor independent review is `work/quartic-v14-release-review-sol/annex/REVIEW.md`, SHA256 `644f1d85f1af06899f2012bb22b0781ddb3d9221ce5f47b2d40480d50543c504`. Its two required selection corrections are addressed here without changing the accepted R5 tooling.
