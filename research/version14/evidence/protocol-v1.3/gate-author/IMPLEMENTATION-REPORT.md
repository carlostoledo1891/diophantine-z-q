# Version 1.3 coverage implementation candidate

Author `/root/protocol_v12_acceptance`. This is an implementation report, not an
independent acceptance. All work is confined to this isolated directory. No live
controller, v1.2 packet, deployed configuration, credential or remote was changed.

The candidate adds structural source coverage validation and a reserved coverage
application through the existing schema-2 receipt mechanism. It preserves the
operator ledger event types and all existing target/binding digest algorithms.
The separate coverage receipt binds the dossier, initial reconstruction, proof
sources, required assertions, supplier contracts, graph and reconciliation through
verified blobs and dependency hashes. Coverage acceptance excludes every ordinary
application author as well as the coverage proposal author.

The live `policy_path` points to `docs/audit-history/PROTOCOL.md`. The new protected
profile explicitly binds that runtime policy hash and the supplied human protocol
at `docs/research-review/PROTOCOL.md`. Unknown explicit versions/hashes/paths fail.
Absent profiles cannot silently reuse the legacy route when exact v1.3 bytes or
coverage applications occur, or when an unknown canonical protocol hash appears.
Known v1.1 and v1.2 records retain legacy validation and cannot receive a v1.3 label.

Policy/editorial changes can use a narrowly scoped profile with a reviewed exact
changed-path allowance and a nonempty inventory of unchanged proof artifacts.
This route still requires a separate non-author receipt and reports no mathematical
completion. Substantive coverage requires a full line index of the protected proof
sources, all announced claim links, current use/supplier records, direct internal
edges, preserved initial/final differences and resolved dispositions. Dependency
cycles remain blocked by the existing core.

The supported process route has the same eligible reviewer reconstruct and decide
coverage. Frozen/comparison timestamps, source-first method, prior exposure and
limitations are attestations adopted by that reviewer's receipt. They do not prove
reading order or independent reasoning. Current source-bound records and a new
receipt are required after source changes, including editorial changes. The
protocol's optimized scoped-acknowledgment route is not implemented.

`adapter/COVERAGE-V1.3.md` documents exact schemas, limits and the protected-profile
integration requirement. `adapter/PROTOCOL-V1.3.md` preserves supplied bytes with
SHA-256 `d3eb878bb3fb12d3b27d157e33f417f6f81bf2a873370f2758e8ccb1e5314d0a`.

Validation includes synthetic keyed-ledger integration, direct-edge omission for
named theorem/section-only/unnamed estimate uses, deleted uses/passages, missing
coverage receipts, stale suppliers/dependencies/profiles, cycles, preserved disputes,
and nonmath scope boundaries. The final core/ledger/live/CI/intake/restore regression
run passed 391 tests in 39.459 seconds, recorded in `TEST-RESULTS.log`. The unchanged
transport suite passed 25 tests in 11.385 seconds and the legacy schema-1 suite
passed 53 tests in 1.032 seconds. Exact candidate hashes are in `CANDIDATE.json`.
All test receipts and observations are explicitly synthetic.

The candidate changes four existing adapter modules, adds one validator and
one test module, and supplies two documentation files. The existing modules
are the manifest core, ledger bridge, and the two live evaluators. Only the isolated live-evaluator
pin tables were refreshed. Root integration must stage the new module/test/docs,
pass the protected job profile to the live evaluator, and obtain independent
exact-target acceptance before deployment. No source hashes in this report are
an approval or authorization to deploy.
