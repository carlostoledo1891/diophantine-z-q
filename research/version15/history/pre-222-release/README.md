# Version 15 research candidate

The [prospective protocol inputs](protocol/README.md) contain the joined current applications, coverage and connections. Authentication and publication remain pending.

This directory contains the current Version 15 manuscript, finite artifacts, review evidence and preserved preparation history. Prospective contributor and application records have scoped independent reviews. Authenticated protocol capture and publication remain pending.

- [Manuscript PDF](snapshots/v15-018/manuscript/quartic_v15.pdf) and [TeX source](snapshots/v15-018/manuscript/quartic_v15.tex)
- [Current artifact index](ARTIFACT-INDEX.md)
- [Current cumulative handoff](CUMULATIVE-HANDOFF.md) and [active review resolver](ACTIVE-REVIEW-RESOLUTION.json)
- [Current finding dispositions](evidence/current-dispositions/FINDING-JOINS.json) and [their review](evidence/current-dispositions/FINDING-JOINS-REVIEW.json)
- [Source-first chronology](evidence/sourcefirst-chronology/INITIAL-FREEZE.json) and [assembly reasoning](evidence/final-assembly/REVIEW.md)
- [Consolidated readiness evidence](evidence/readiness-002/README.md) and [remaining protocol/deployment work](evidence/readiness-002/STATUS.json)
- [CI connections](CI-CONTRACT.json)
- [Version 14 history](../version14/CUMULATIVE-HANDOFF.md) and [repository overview](../../README.md)

The selected manuscript retains the original huge polynomial, the 314-variable decimal quartic and the 233-variable family with 2,514 monomials. Its defining threshold remains ineffective. No 232-variable optimization is included. The prior snapshots and qualified review records remain intact.

From the repository root, verify the selected snapshot with:

```text
python -B scripts/v15/check_snapshot.py --repository research/version15/snapshots/v15-018 --manifest-sha256 8a10b6a6405adabf25ad8359900c7681251cf710a24bb4926feec261a411df6c
```

Run each existing finite check using `scripts/v15/run_finite.py` with the same repository and manifest arguments, a fresh `--scratch` directory outside the repository, and `--kind 314`, `--kind 233`, or `--kind huge`. The [manual workflow](../../.github/workflows/version15-checks.yml) uses these exact paths. These checks do not constitute protocol or publication approval.
