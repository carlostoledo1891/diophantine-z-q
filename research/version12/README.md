# Version 12 research supplement

Download [z-in-q-version12-supplement.zip](z-in-q-version12-supplement.zip), with [hash and size receipt](SUPPLEMENT.json).

The archive includes the exact current manuscript, the portable 498/514-variable construction, application inventory, independent reviews, protocol records and selected reports from all ten optimization approaches. It embeds the unchanged Version 11 supplement, preserving earlier research records. It contains no conversational transcript or credentials.

Extract and run `python -B restore.py restored` to verify hashes and restore the current files and historical base. From the restored directory, run `python -B scripts/check_quartic498.py`, `python -B scripts/check_audit_history.py --self-test`, and `python -B docs/manuscript-revisions/version12/inventory/validate.py --repo . --self-test`. Node is required for polynomial reconstruction.

Read the [Version 12 review summary](../../docs/manuscript-revisions/version12/README.md) first. This supplements the [Version 7 full research history](../../handoff/README.md). Primary source PDFs are identified by URLs and hashes rather than redistributed. The checks certify the stated finite and record-integrity properties, not every arithmetic inference in the manuscript.
