# Mathematical research starter kit

Download these three files together and put them at the root of a new research repository:

- [Protocol_D](https://github.com/elliotglazer/protocols/blob/main/Protocol_D.md), included as [PROTOCOL.md](PROTOCOL.md). It states the assurance requirements.
- [AGENTS.md](AGENTS.md): operating instructions for meeting those requirements with one canonical ledger, reusable evidence, and incremental review.
- [PROJECT.md](PROJECT.md): a project brief to fill in with the target, sources, deliverables, constraints, and existing authorizations.

On GitHub, open each file and use **Download raw file**. The files are Markdown and can be read without special software.

After filling in PROJECT.md, give the agent this prompt:

> Read PROTOCOL.md, AGENTS.md, and PROJECT.md. Pursue the stated mathematical objective while satisfying every applicable protocol obligation. Use the smallest adequate review implementation: one canonical ledger, reusable evidence, and incremental validation. Begin research alongside that setup; do not make infrastructure development a separate preliminary project. Preserve independent source-first reconstruction, application review, and final assembly review. Report unresolved mathematics, accepted work awaiting integration, and mechanical release work separately.

These are reusable instructions and a template, not a prebuilt automated gate. The starter-kit protocol is an exact copy of the [governing protocol](../PROTOCOL.md); update the copy when that protocol changes. The two companions provide reusable operating instructions and a project brief. They do not replace this repository's [own agent instructions](../../../AGENTS.md) or assert that its proof has completed review.

## Release workflow

The companion operating instructions include a practical release plan: immutable commit and artifact bindings, an end-to-end preflight, compatibility with existing signed evidence when used, and resumable stages that preserve successful unchanged work. PROJECT.md records the phase budgets, progress and error locations, recovery owner, and publication/readback steps.

After two unexplained infrastructure failures in a stage, diagnose and reproduce the failing step before another expensive full run while independent work continues. Publication should be a short delivery step after expensive validation. Changed relevant inputs or checkers still require the affected checks to run again. These instructions do not add mathematical assurance duties, extra human signoffs, permissions or a custom service to the selected framework.
