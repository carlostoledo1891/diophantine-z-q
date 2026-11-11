# GI files in the cumulative handoff

The complete package contains the unchanged sixteen module sources and their original version 1 PDF, plus the separately identified S13 addendum in the current merged PDF. The full standalone archive is GI-PROOF-ONLY.zip. Its file manifest is PROOF-ONLY-MANIFEST.json.

The cumulative handoff retains 289 of the 297 full-manifest files and excludes 8 historical or guide PDFs under the unchanged project-PDF restriction. Every omission and its retained source or page-assembly map is enumerated in CUMULATIVE-HANDOFF.json. The historical merged PDF is assembled from the preserved original page map and original module/guide sources; its exact bytes are supplied in the complete standalone archive. Recreating those historical bytes from a reduced copy alone is not established.

Run python -B verify.py in the complete package. Run python -B verify-handoff.py only in the reduced cumulative copy; it deliberately rejects the excluded PDFs if present. File verification does not establish mathematical validity or release approval.

The standalone ZIP is not nested in the cumulative archive. Its SHA-256 is 581aa968e1c54cf78a16e47b18e981012c5b29eeb6da2e0c115b56fb7276156b. The existing main manuscript remains unchanged.
