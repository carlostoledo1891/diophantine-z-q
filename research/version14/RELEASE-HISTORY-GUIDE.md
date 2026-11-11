# Version 14 research history and evidence

This is a proposed guide for the cumulative Version 14 handoff. The selected constructions are the corrected 299-variable symbolic quartic and its 314-variable ordinary companion. Their finite artifacts and component reviews exist. Final assembled-proof, coverage, release and deployment decisions remain separate records. Inclusion in this archive does not turn a candidate, historical review or successful script into a current proof acceptance.

## Start with the current artifacts

The proposed public coefficient files are `quartics/quartic-299-symbolic-coefficients.json`, `quartics/quartic-299-symbolic-coefficients.txt` and `quartics/quartic-314-fully-expanded.txt`. They must be exact copies of the corresponding files in `quartics/quartic-299-314/`.

The package README explains the coordinate conventions. The symbolic polynomial has 299 total variables, 298 witnesses, 6630 monomials and fixed integer C=3^(2^25). Its maximum coefficient magnitude is 186624*3^(2^26). The ordinary polynomial has 314 total variables, 313 witnesses and 6672 monomials. Its largest coefficient has 6496 bits and is strictly below 2^6496. The ordinary compact text contains 264430 bytes. The preserved source-ID text contains 222890 bytes; those are different serializations.

`PACKAGE-MANIFEST.json`, `SOURCE-MANIFEST.json`, `ACCEPTANCE.json` and `VERIFICATION-PLAN.json` bind the package. `verify_lineage.py` replays its finite construction history and exact tables. Its scope is finite reproduction, with the separately stated inherited arithmetic inputs. Follow the actual component reviews in `reviews/`; do not infer their scope from a single package status field.

## Follow the selected construction and its alternatives

The package preserves the selected branch beginning at the 394-variable baseline, its subsequent eliminations and compositions, the alternate-ordinate 301 step, the corrected oriented 299 construction and the ordinary lift. `sources/work/` keeps the exact producer and review paths for that branch. `REPRESENTED-BY-FROZEN-PACKAGE.json` in the selection evidence maps original local research files to their already packaged copy.

The proposed `research/version14/evidence/research/` directories retain the rest of the dated optimization, under-400 and under-300 research. This includes proof drafts, finite searches, candidate systems, verifiers, reviews, rejected routes and coefficient tradeoffs. These directories are history. Their presence does not select every construction they contain.

The first 299 attempt is rejected because it used alternate-cache coordinates 202/203. The accepted component review concerns the corrected `reciprocal299-r2` branch using 196/197. The 315- and 316-variable ordinary alternatives remain useful history. The 316 alternative retains the earlier 2^3247 coefficient bound; the selected 314 companion uses the explicitly larger 2^6496 bound. Preserve all three without substituting one artifact's bound for another's.

The earlier Version 13 archive is the exact nested base, SHA256 `10787487f46ebfefe931e2e7db163a2e8bd0605b3c0325534a47cd93dd43b01b`. It preserves earlier manuscript editions and research. The Version 14 layer should add or supersede paths explicitly rather than rewrite the historical archive.

## Read the proof coverage in two stages

The proposed `docs/manuscript-revisions/version14/baseline-coverage/` preserves the arithmetic, compiler, Gaussian and theta partitions. Read their initial source-use reconstructions and freezes before their reconciliation and decision records. The exact line coverage is evidence of the audit's scope; it is not a machine proof of the mathematics.

`docs/manuscript-revisions/version14/source-review/` preserves the 394/411 and new 299/314 review, including its initial reconstructions, frozen drafts and later layout comparisons. Earlier decisions may bind earlier assembled hashes. A later layout or source version needs its own exact comparison and decision. The final cross-partition coverage join and reconciliation against the final application inventory were still pending when this proposal was prepared.

`docs/manuscript-revisions/version14/APPLICATIONS.json` and the adjacent final-records-002 files are proposed current author records. Historical component reviews and the older final-records-001 attempt remain under `research/version14/evidence/inventory-history/`. Neither an author's inventory nor a structural validator creates an independent mathematical acceptance.

The interpreter/precision report and original source pins belong under `docs/research-review/proof-sources/`. `INTERPRETER-SOURCE-MAP.json` maps the original source paths to exact existing repository files or proposed additions, prioritizing the report's first 14 code and machine inputs. The original report and pins stay byte-identical. The existing pole supplier remains `docs/theorem-application-audit/evidence/pole.md`. A relocated source is the same source only when its hash agrees.

## Keep supplier-version qualifications visible

The Gaussian supplier supplement records a successful comparison of the final published Browning-Loughran Theorem 4.1. The Dodos-Kanellopoulos author-linked theorem was compared directly, but access to the final typeset article remained unavailable. The Browning-Heath-Brown final-text comparison likewise remained qualified. These are precise version/access limitations. They are not findings of false mathematics.

The new archive layer excludes downloaded full papers, full-text extractions and paper-page images. It retains hashes, URLs, page and theorem locators, comparison notes and the access outcome. Some original manifests therefore describe locally inspected papers that are deliberately absent from the public selection. Do not rewrite those historical manifests to pretend the files were never inspected; use the explicit exclusion record to explain the public subset.

## Protocol and release history

The governing protocol is the exact supplied version 1.3 text at `docs/research-review/PROTOCOL.md`, SHA256 `d3eb878bb3fb12d3b27d157e33f417f6f81bf2a873370f2758e8ccb1e5314d0a`. Version 1.2 remains historical. The proposed evidence directory keeps the documentation, gate, runtime, activation and independent reviews as dated records. Earlier pending rollout snapshots are not the final deployment state.

The release profile states requirements. Eleven required Actions checks and the dedicated App-bound independent-agent gate remain distinct from ordinary manuscript validation. No additional mandatory second-human rule is introduced here. Final source transitions, actual gate decisions, both repositories' immutable readbacks and fresh archive restore/replay evidence must be added as they actually occur. Optimization is paused; this release work continues.

The R4 release-tool history and its separate independent review explain the renderer repair. Page selection tests do not supply visual review. The final current PDF, build report and actual visual-review record must bind the selected source and edition.

## Reconstruct the handoff

The release builder takes a flat JSON object mapping repository-relative paths to SHA256 values and a second JSON object containing nonempty `coverage`, `profiles` and `evidence` path lists. Every listed path must be included in the first object. The current `INCLUSION-PROPOSAL.json` is an author proposal with source paths, hashes and pending items, not that final executable selection.

Before building, install only the independently reviewed exact files, complete the pending records, bind the final committed bytes and produce the actual two selection inputs. The cumulative builder adds the pinned Version 13 base and runs restoration and finite checks. Preserve those observed receipts. No ZIP or repository installation was performed by this selection task.
