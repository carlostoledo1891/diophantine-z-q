# Version 15 — local preparation

This repository stages the full Version 15 draft: the original 292,890,231,905-variable polynomial, the fully decimal 314-variable quartic, and the 233-variable family. It is not a Protocol D completion or publication.

- [Manuscript PDF](manuscript/quartic_v15.pdf): 525 pages, November 9, 2026.
- [TeX](manuscript/quartic_v15.tex): SHA256 dbc35d8c7f746401b102e0c40e62f906f54fd407ce95229488434ebf0d711e1b.
- [Artifact index](ARTIFACT-INDEX.md) and [cumulative handoff](CUMULATIVE-HANDOFF.md).
- [Bounded remaining work](review/tasks/BOUNDED-TASKS.json).
- [Governing document navigation and scope](docs/governing/README.md).

The 314-variable polynomial has 6,672 monomials and a 264,430-byte decimal table. Its proven coefficient bound 2^6496 implies the abstract's 2^6500 bound. The 233-variable family has 207 quadratic residuals and 2,514 monomials; A_N=149^(2N+1), with coefficient height A_N²+1 for N>=53. The sufficient defining N0 remains ineffective. No specific defining N or numerical coefficient bound for a certified member is supplied.

The 2,408-term candidate is not included. Prior proof sources and reviews keep their historical scope. Protocol D coverage, source-use, findings and assembly obligations remain open.

The [original huge-polynomial specification](construction/V15-SCOPE.md) and its supported finite reproduction package are also included. Their arithmetic premises and current Protocol D acceptance remain separate.

The latest evidence update is the [consolidated adoption record](review/staging-016/ADOPTION.json). See the [current open items](review/staging-016/OPEN-ITEMS.json) for the remaining ProtocolD work. Bounded row and artifact checks do not constitute approval of the complete manuscript.

The adopted source includes the reviewed published surface-height route and four wording clarifications. The [build record](review/staging-016/BUILD.json) binds the matching PDF; the [visual inspection](review/staging-016/VISUAL-REVIEW.json) is author-side layout verification. Source-first and inherited-routing acceptances retain their exact scopes. No 232-variable optimization is adopted.

The separate local staging017 metadata update preserves the staging016 manuscript and PDF. See [the exact change record](review/staging-017/CHANGE-RECORD.json), [new scoped evidence](review/staging-017/EVIDENCE.json), and [remaining work](review/staging-017/OPEN-ITEMS.json). The construction companion-name note now reflects the adopted manuscript. This is a local review candidate, not a published or globally approved release.

Staging018 adds the [final source coverage and separate mathematical assembly receipts](review/staging-018/STATUS.json). These decisions bind the unchanged adopted manuscript. Earlier open-item records are historical; remaining release/tooling/provenance tasks are stated in the current status. This is still a local candidate, not a published or authenticated release.
