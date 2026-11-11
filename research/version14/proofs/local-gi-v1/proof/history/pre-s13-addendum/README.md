# Local GI proof supplement, current source revision

GI-SUPPLEMENT.pdf contains the current 103-page supplement: one guide page and sixteen proof modules. PDF-PAGE-MAP.json locates each module. MODULES.json binds the current TeX and standalone PDFs while preserving original source and manifest identities.

The current sources include the reviewed LP13 wording, increment-linearization proof, rational-subgroup bridge, E5 strong-test selection, rank wording and strong-family/full-matrix assembly join. The target remains the normalized finite-family same-step inverse conclusion. The retained mathematical hypotheses and scoped exclusions still apply.

proof/current-source-applications/INDEX.json identifies the current source/application records. CURRENT-PASSAGE-INDEX.json transports historical classifications only across unchanged text and binds changed passages to their own reviews. Historical owners, status fields and independent receipts are preserved. ORIGIN-MAP.json resolves historical source and PDF references to their preserved copies.

LP13 uses the project strong all-limit convention on the actual reviewed constructor outputs, not an inference from the literal published Definition 6.19 alone. RANK and MF use the GT12/local rational-intersection bridge; LP13 retains its central-quotient role.

Run python verify.py after extracting the proof-only archive. It verifies the selected file sizes and SHA-256 hashes using the standard library. The archive excludes external published PDFs, page images and private-evidence assets, including the restricted Tointon source.
