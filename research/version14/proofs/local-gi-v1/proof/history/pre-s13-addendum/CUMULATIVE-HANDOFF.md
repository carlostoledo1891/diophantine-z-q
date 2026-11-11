# GI files in the cumulative handoff

These controls are stored in the complete canonical local GI package and also included in its reduced cumulative-handoff copy. They describe and verify the reduced copy only; their presence does not make the canonical directory reduced. The cumulative builder keeps its existing restriction to the main manuscript and 18 approved project PDFs, and rejects nested ZIP files other than the research annex. This is a packaging scope distinction; no mathematical acceptance is enlarged.

Of the 286 files listed in the original full-package PROOF-ONLY-MANIFEST.json, the reduced copy retains 279 and omits seven PDFs: the standalone guide and six historical module PDFs. CUMULATIVE-HANDOFF.json lists every retained and excluded file with its exact hash and byte count. Each omitted PDF has a retained TeX counterpart. The 17 current approved GI PDFs in this directory remain; the eighteenth project PDF is the identical merged-supplement alias under manuscripts. The main manuscript is checked separately.

The complete canonical package and the separately distributed GI-PROOF-ONLY.zip remain complete. The ZIP is not nested in the cumulative archive. Its SHA-256 is d4aa92224ff373410a8e63073d0f829f80f55ad81be5dda357872a88822c0ae0.

In the complete canonical directory, run `python -B verify.py` to check the original full-package manifest. The added handoff controls are outside that unchanged manifest and outside the unchanged standalone ZIP.

After extracting the guard-filtered cumulative handoff, enter its local-gi-v1 directory and run:

    python -B verify-handoff.py

Running verify-handoff.py in the complete canonical directory intentionally fails because the seven excluded PDFs are present. It is not the full-package verifier. In the reduced copy, the handoff verifier checks the exact retained files, original full manifest, and handoff controls; missing, changed, excluded, extra or symlinked files fail. It does not verify mathematical claims or an authenticated release gate.

The unchanged verify.py belongs to the complete package. Running it on this reduced copy reports the seven omitted PDFs as missing. That is expected; do not interpret this reduced copy as passing the full-package check, delete entries from the original manifest, or silently substitute the handoff result for it.

## Reconstruction scope

The excluded-file records identify the retained TeX sources. Historical BUILD-REPORT.json files record the Tectonic engine, bundle and commands used for their builds. The guide source is proof/guide/cover.tex. These sources permit rebuilding with suitable TeX tooling, but the compiler/cache environment is not supplied here and byte-identical PDF reconstruction has not been established.

The existing workspace guide build script depends on its workspace layout and cached Tectonic bundle. The merge script consumes existing pinned PDFs; it does not rebuild omitted PDFs. The archive script verifies the full manifest before zipping, so it cannot recreate the complete ZIP from this reduced copy alone. These scripts are provenance pointers, not a turnkey reduced-handoff rebuild command. Obtain the complete separately distributed package for the original exact PDF/ZIP bytes; regenerated artifacts need their own hashes and must not be presented as the old ones.
