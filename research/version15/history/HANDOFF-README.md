# Version 15 local handoff candidate

This directory is a concrete local overlay, not a published release. The immutable selected snapshot is [snapshots/v15-017](snapshots/v15-017/README.md), whose manifest SHA256 is a29b94fb4f1083b42ee297d4590965b5b629d201752559d35b8472f75b08010b. It preserves the accepted016 manuscript and PDF, adds six scoped receipts, and corrects the stale construction companion-name note. Exact changes and prior bytes are retained in its staging017 records.

[Author checks](CHECKS.json) cover bytes, copy origins and current navigation. [The late source-first adoption/Gaussian decision](evidence/GAUSSIAN-CURRENT-AND-ADOPTION-DECISION.json) arrived after017 froze and is included alongside it without altering that snapshot. Degree addendum and final assembly are still pending. The full proof is not marked globally approved.

The proposed manual-only workflow and scripts/v15 tools are separate from the snapshot. They need independent tooling review before any deployment. No remote action, release creation, ZIP or PDF rebuild was performed. Version14 and original016 remain outside this candidate and unchanged.

Local verification:

    python -B scripts/v15/check_snapshot.py --repository snapshots/v15-017 --manifest-sha256 a29b94fb4f1083b42ee297d4590965b5b629d201752559d35b8472f75b08010b

Existing finite checks can be run through scripts/v15/run_finite.py with the same repository/hash and a fresh nonoverlapping scratch directory. Use --kind 233,314 or huge. Python3.11+ is required; huge also needs Node22+. These are bounded finite checks, not global mathematical approval.
