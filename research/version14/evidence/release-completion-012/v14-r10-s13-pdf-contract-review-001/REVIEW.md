# R10 S13 PDF contract review

Accepted within the narrow allowlist/provenance scope: author manifest ef911a44ee0da6e471f50c18d1362cc58d46883c389d002758f52d8f33ec5b46. Reviewer /root/v14_arithmetic_review is independent of author /root/v14_h6_coverage.

I compared the actual assembled001 predecessor and candidate. The same eighteen ordered PDF paths remain. The sixteen module PDF/source pairs are unchanged. Only the two merged PDF hashes and sizes change to c971bcad7a269f8bd4cd18102d62cd8d61b801d9c4439d729457f37721e7228a / 1591093 bytes. Both source lists add the exact e245e0eb S13 Markdown. Existing proof manifest, packaging check and page-map pins update; MODULES and ORIGIN-MAP remain unchanged. Four additional provenance records bind the scoped S13 review and accepted delivery review, manifest and build script. I read the delivery review and retain its artifact-only limitations; this review does not independently re-render or re-prove the supplement.

The actual artifact_contracts.py diff is exactly the PROJECT_PDFS_SHA literal, from f19a979e60d444dfcebd196d78b59812699b26be4a3a487b421ab72648443e63 to 40b2fd8d9a082c32205e5bacc71c483789f2107e06a2669fd5835e7f2f884941. No validator logic or admissibility rule changes. I independently checked all five candidate manifest members and all forty-four distinct current PDF/source/provenance files. All hashes and sizes match.

I executed the candidate check.py with the bundled Python interpreter: exit0, nine checks pass. These include rejection of the old merged PDF, missing or changed S13 source, missing or changed scoped review, and historical PDF admission. The same-path update therefore does not weaken the historical-PDF exclusion or source/provenance requirements.

This accepts the isolated two-file candidate for installation. It is not a report of installation, a final archive validation, a mathematical coverage approval, or release authorization. Final packaging must contain every pinned provenance file and must be validated against its actual selected source tree.
