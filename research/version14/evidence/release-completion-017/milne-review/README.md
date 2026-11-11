# Bounded independent Milne review

`REVIEW.md` contains the mathematical decision and its limits. `SOURCE-PINS.json` identifies the author targets and independently retrieved primary sources. `OCCURRENCES.json` binds current source uses and repeated assertions. `ERRATA-APPLICABILITY.json` records the ten-page addendum check. `CHECKS.json` records reproducible mechanical checks, which are not a proof of duality.

Run from the workspace root:

```powershell
& 'C:/Users/glaze/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' work/source-risk-review-20261107/milne-review/review_checks.py
```

The checker requires the exact local primary-source PDFs identified in `SOURCE-PINS.json`. It reads but never executes author code. Its writes stay within this review directory. The source PDF copies and their complete extractions and page images remain in `local-only/`; they are not part of the proposed review handoff. The unredacted working folder is not a public release package.

No private conversation or personal assessment is used as mathematical evidence. No production manuscript, current registry, successor004 artifact or remote setting is changed by this packet.
