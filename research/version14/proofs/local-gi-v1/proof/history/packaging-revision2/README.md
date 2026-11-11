# Local GI proof supplement, packaging revision 2

The mathematical proof edition is version 1, matching the manuscript bibliography. The 16 exact modules and their scoped mathematical decisions are unchanged from packaging revision1. This successor adds the independently accepted full passage-status index/reconciliation, the Bertrand source contract, the Gaussian coverage addendum, and their independent decision.

Read `GI-SUPPLEMENT.pdf` for the assembled proof and supporting modules. Standalone TeX/PDF files, source-use and application records, and decisions are under `proof/`. `COVERAGE-INCORPORATION.json` binds the curation change. `ORIGIN-MAP.json` maps original project paths to the exact bundle copies. The original manifests and historical author-proposal wording are preserved; later independent decisions and active-source overrides govern only their explicit scopes.

Run `python verify.py` in either the full private bundle or an extracted proof-only archive. It uses only the standard library and verifies all relative file hashes. Full source-evidence references are registered, with private copies outside the proof-only archive. Historical unused inputs are identified as provenance rather than current proof suppliers.

Seven exact published sources are listed in `SOURCE-REGISTER.json`. The external PDFs and page images are excluded from `GI-PROOF-ONLY.zip`; in particular, the Tointon book is personal-use evidence and must not be redistributed. The archive contains the authored mathematical supplement, records and scoped decisions. Packaging is not an installation, registry approval, or publication.
