# Version 11 research supplement

Download [z-in-q-version11-supplement.zip](z-in-q-version11-supplement.zip), with [hash and contents receipt](SUPPLEMENT.json).

The archive contains the current TeX and PDF, Kato index/norm/interface audits, the independent final acceptance, the original-Mazur source audit, and the revised protocol and executable checks. It also includes the unchanged Version 10 supplement, which preserves the preceding source and polynomial records. It contains no conversational transcript or credentials.

Extract the archive and run `python -B restore.py restored` to verify hashes and reconstruct the review tree. Then run `python -B restored/scripts/check_audit_history.py --self-test`. The restored files are sufficient for that check. The primary PDFs are identified by URLs and hashes rather than redistributed in this supplement.

Read the [Version 11 review summary](../../docs/manuscript-revisions/version11/README.md) first. This is a supplement to the [Version 7 full research history](../../handoff/README.md), not a replacement for it. Structural checks and internal model reviews do not certify the entire informal proof.
