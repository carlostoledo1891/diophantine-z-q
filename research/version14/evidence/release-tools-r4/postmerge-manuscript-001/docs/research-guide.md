# Research guide

The current manuscript is [*Z is Diophantine in Q*, Version 14](../manuscripts/quartic_v14.pdf), dated November 7, 2026, with [TeX source](../manuscripts/quartic_v14.tex). Start with the [299/314-variable constructions and review scopes](manuscript-revisions/version14/GUIDE.md), [application inventory](manuscript-revisions/version14/APPLICATIONS.json) and [cumulative supplement](../research/version14/README.md). The original construction and earlier proof baselines remain in the manuscript.

The [Version 13 guide](manuscript-revisions/version13/GUIDE.md) and [supplement](../research/version13/README.md) preserve the 394/411-variable edition. Continue with the [Version 12 reductions, inventory and reviews](manuscript-revisions/version12/README.md) and [supplement](../research/version12/README.md), followed by the [Version 11 repair and reviews](manuscript-revisions/version11/README.md) and [supplement](../research/version11/README.md), followed by the [Version 10 review response](manuscript-revisions/version10/README.md) and [supplement](../research/version10/README.md), followed by the [Version 9 inventory extension](quartic-523-540/README.md), then its [inherited inventory](quartic-962/README.md). It records exact source versions, hypotheses, conventions and manuscript bindings, including the new prime-pattern argument and its publication-status qualifications. The [Version 9 revision record](quartic-523-540/revision.json) binds the new section and every other edit to the exact Version 8 baseline. The finite polynomial checks and the arithmetic proof have separate scopes. The [build instructions](building.md) explain how to reproduce the artifacts.

The [research handoff guide](../handoff/README.md) identifies the Version 7 full and current-only archives. Both contain the public snapshot and selected research notes, with no conversational transcript. The full archive also embeds the unchanged Version 6 full archive, with its earlier historical baseline.

## Version 7 audits

The [Version 7 research guide](../research/version7/README.md) links the four Gaussian component audits, exact patches, source pins and integration checks. Their scope is separate from the retained arithmetic proof and formalization.

## Version 6 research

The [new research collection](../research/version6/README.md) preserves the quartic optimization, degree-four lower bound, Gaussian analytic replacement, independent reviews, and source inventories. The current manuscript reproduces the required Gaussian special case rather than invoking Frei–Tinková as a theorem. The degree obstruction is attributed to the agentic notes; the README supplies the collective contributor credit. The proof, finite certificates and incomplete formalization have distinct review scopes.

## November 6 research update

The [organized collaborator collection](../research/2026-11-06-collaborator-notes/README.md) includes the supplied equivalence and arithmetic-input notes, selected articles from the November 5 handoff, a comparison, and an exact replacement of the von Känel–Kret height input by the existing five-contact proof. Its source pins and check script distinguish a verified substitution from the still separate parity/point-existence question.

## Historical materials

The [Version 2 release](https://github.com/elliotglazer/diophantine-z-q/releases/tag/quartic-12504-version-2) and its [12,504-variable package](../quartics/quartic-12504/README.md) remain separate historical records. The remainder of this guide describes the [November 4, 2026 research handoff](https://github.com/elliotglazer/diophantine-z-q/releases/tag/research-handoff-2026-11-04-r2). It preserves earlier research history and does not contain either the Version 2 or Version 3 quartic package or all subsequent audits. Its `current/` directory means current at the archive date. The [original large construction](../construction/README.md) and [accepted Lean helpers](../lean/README.md) remain available in this checkout.

## Reading the archived manuscript

1. Read **The main theorem and proof structure** in the archived November 5 manuscript for the statement and the roles of the component arguments.
2. Read **A finite specification of the polynomial**, **A variable-shift relation for ordinary values**, and **The cutoff and polynomial size** to see what is constructed and how it defines ordinary integer values.
3. Follow the technical argument through the elliptic model, height estimate, pole predicate, multiplication, and restricted converse. The arithmetic and limit sections and source-application appendices supply the dependencies.
4. Read **Consequences of the integer definition** for the three corollaries and their scope.
5. Use the archive to inspect literal specifications, calculations, source checks, historical alternatives, or formalization work.

The archived November 5 TeX source has descriptive labels such as `thm:target`, `sec:syntax`, `sec:height`, `sec:rc`, `sec:limits`, `sec:compiler`, `sec:bridge`, and `sec:size`. Refer to those labels when page numbers differ between builds.

## Map of the argument

Revision 2 of the November 4 research handoff added the later audit campaigns and the reviewed height replacement. Start with `current/diophantine_zq.tex`, its matching PDF, and `current/height-review.md`. The old height routes do not supply extra premises for Section 4 of that archived manuscript. The archive's revision number is distinct from the current manuscript's title, Version 13.

The paths below are **original project-relative paths recorded in the archive manifest**. Search for them in `INDEX.html`, or restore them with `restore_history.py`. They are not paths in this Git checkout. Some files predate the archived November 5 manuscript; compare their scope with that revision and later audits.

| Topic | Archived November 5 manuscript section | Archive starting points |
| --- | --- | --- |
| Literal polynomial specification | A finite specification of the polynomial; Literal finite-constructor specification | `outputs/ordinary-integer-definition.json`; `outputs/ordinary-integer-polynomial.js` |
| Elliptic model and generator | The elliptic model of integer indices | `outputs/elliptic-generator-proof.txt`; `outputs/z-in-q-generator-audit.txt`; `outputs/verify-z-in-q-generator.py` |
| Height estimates | The six-contact height estimate | `work/remove-vkk-20261104/`; `work/independent-height-review-20261104/`; earlier height alternatives remain historical |
| Pole completeness and restricted converse | The pole predicate and its converse input; The restricted converse and its dependency order | `outputs/restricted-converse-and-pole-completeness-proof.txt`; `outputs/z-in-q-restricted-converse-assembly.txt` |
| Arithmetic dependencies and limits | Actual classes, local conditions and central comparison; The two limits and determinant transfer | `outputs/z-in-q-global-selmer-assembly-audit.txt`; `outputs/z-in-q-common-packet-audit.txt`; `work/sol-rc-arithmetic-graph-review-001/` |
| Computation and compilation | Exact precision computation and polynomial compilation | `outputs/integer-halting-correctness-proof.txt`; `outputs/integer-diophantine-compiler.js`; `outputs/hierarchical-integer-compiler.js` |
| Ordinary rational values | A variable-shift relation for ordinary values | `outputs/ordinary-input-bridge.txt`; `outputs/z-in-q-exact-value-bridge-audit.txt`; `outputs/z-in-q-ordinary-integer-assembly-proof.txt` |
| Variable, degree, and coefficient bounds | The cutoff and polynomial size | `outputs/ordinary-integer-polynomial-size-bounds.json`; `outputs/z-in-q-polynomial-size-bound-proof.txt` |
| Universal and ZFC-related constructions | Consequences of the integer definition | `outputs/universal-rational-equation.json`; `outputs/zfc-inconsistency-polynomial.json`; `outputs/zfc-inconsistency-polynomial-proof.txt`; `work/k215-pa/` |
| Sources and dependency graphs | Bibliography and source-application appendices | `formalization/z-in-q/ProofSources/`; `work/main-proof-graph/` |
| Earlier versions and discarded routes | Historical record | `drafts/z-in-q-candidate-preprint/`; `outputs/z-in-q-research-status.json`; archive-root `DISCARDED_APPROACHES.md` |

The archive's K215 and ZFC-related files record additional research. The archived November 5 manuscript describes the general specialization argument; it does not specify an additional explicit ZFC polynomial there. Check each historical construction's dependencies before treating it as a consequence of the manuscript.

## Verify and restore the archive

This section applies to the historical November 4 archive. For the current research archives, use the [handoff guide](../handoff/README.md). Download the historical ZIP from its release. Its SHA-256 is:

```text
827765f17087e1794c15770221a3a2d0fefed25839566a4a9bfb3b5aaa1ed42b
```

On Windows PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 .\z-in-q-research-handoff-2026-11-04-r2.zip
```

On Linux:

```sh
sha256sum z-in-q-research-handoff-2026-11-04-r2.zip
```

On macOS:

```sh
shasum -a 256 z-in-q-research-handoff-2026-11-04-r2.zip
```

The repository's [SHA256SUMS](../SHA256SUMS) identifies the files in the current release and the historical archive separately. Matching a hash establishes file identity, not mathematical correctness.

Extract the zip, then open `START_HERE.md`, `CURRENT_STATE.json`, and `INDEX.html`. The HTML index works locally without a server. Original file paths map to their stored copies through `MANIFEST.json` and `FILE_INDEX.csv`.

From the extracted archive directory, use Python 3.9 or later to restore a selected subtree:

```sh
python restore_history.py restored-outputs --prefix outputs/
python restore_history.py restored-lean --prefix formalization/
```

Or restore all indexed files:

```sh
python restore_history.py restored-project
```

Each destination must be new. The utility checks file hashes before writing and does not execute research code. A full restoration occupies about 2.8 GB before filesystem overhead; use a short destination path on Windows. Historical scripts may contain paths from the original Windows workspace that need adapting.

All archive entries and manifest references were checked for CRC and SHA-256 integrity during packaging. The original release's 54-file restore check remains historical; revision 2 also tests restoration of the new independent-review records. The 48 curated production-module source hashes still match integration 31. No clean rebuild of the full historical research project was performed as part of packaging.

## Lean formalization

The saved project uses `leanprover/lean4:v4.35.0` and Mathlib `v4.35.0`; its `lake-manifest.json` records the dependency revisions. Restored sources are under `formalization/z-in-q/`. The archive also provides a readable copy under `current/lean-project/`.

Start with these records:

- `outputs/z-in-q-integration-31.json`: the last accepted production integration and its source hashes.
- `outputs/z-in-q-progress-122.json`: later accepted helper work and the state at handoff.
- `work/astra-formal-critical-path-001/REPORT.md`: the main groups of remaining obligations. This report audits integration 29, so read it alongside the later records.
- `work/sol-post32-accepted-inventory-004/HANDOFF.json`: an inventory of further accepted components. Its directory name is not evidence that integration 32 was accepted.
- `formalization/z-in-q/Frozen/BoundedIntegerPolynomial.lean`: the exact main declaration, still unproved.

The complete elliptic model, height, restricted-converse, pole-completeness, multiplication, computation, and construction/bounds groups, and their ordinary-value composition, remain open as complete formalized interfaces. Proven helper results do not by themselves close those interfaces. Integration 32's observation was interrupted and was not accepted.

The archive omits dependency caches and compiled Lean binaries. The current repository now includes the accepted helper snapshot and [a procedure that compiles it into fresh project artifacts](building.md#lean-helpers). The saved historical compiler receipts describe their particular checked inputs, not every file in the archive.

## Archive scope

The historical archive preserves superseded approaches and unfinished work as well as accepted results. Its inventories establish file identity and provenance; they are not a complete per-source license review or a new review of every mathematical claim. See the [archival notes](archiving.md) and [third-party notices](../THIRD_PARTY_NOTICES.md). The Version 3 source and evidence are supplied separately in this repository.

Independent external mathematical review and completion of the main Lean proof are separate from these packaging checks. Record substantive findings and their resolution by version, and continue using release tags and file hashes to identify the materials under discussion.
