# Independent portability review

Reviewer: `/root/astra_bl_synthesis`. Date: 2026-11-07.

Decision: accepted as a bounded infrastructure change for CI submission. Actual Ubuntu success remains a required subsequent observation. This does not amend the mathematical acceptance or certify the inherited arithmetic again.

## Exact files

| File | SHA-256 |
|---|---|
| `scripts/check_quartic394_portable.py` | `0698c56d744c701901efcf418285001e7d0320b876c1edf9ed287fcfb0af0b91` |
| `scripts/quartic394_path_bootstrap.py` | `a917b8ebac5bbe0d455d6b009083962aaf393b59208d9bfbaf54dbb341230b23` |
| `docs/manuscript-revisions/version13/portability/test_portability.py` | `90a686612583e6036b42fb22e2783e67f5779079204bc155a02dedb3355826ab` |
| Unchanged `scripts/check_quartic394.py` | `faa43aab6431a9cb7ae14f92a47f649c494825ea5f3d56e798d73ad41e59ebd0` |
| Unchanged `quartics/quartic-394-411/PACKAGE-MANIFEST.json` | `b3bc37df3fcb06d622808d3a23741d602b27c0ff0b2179ad28ef313a8489fe22` |

## Failure and correction

The failed Ubuntu job completed the first nine source stages. Stage ten attempted to open the historical Windows path for `rational453-ir.json` from `certificate445.json`. On POSIX, the frozen driver's native `Path` prefix comparison did not recognize that backslash-separated path. The recorded exception is a missing-file error, not an arithmetic assertion failure. It prevented completion of the remaining checks.

The new launcher verifies the old wrapper's exact hash, imports it, and calls its unchanged `main`. Only that module's subprocess binding is replaced. The adapter accepts precisely the old child argument list, `cwd` and `check=True`; unexpected arguments or process options are rejected. It retains the interpreter, UTF-8 and no-bytecode flags, and working directory. The child bootstrap invokes the unchanged frozen driver with its original script argument. Exceptions propagate. The local subprocess binding is restored in `finally`.

Thus the original wrapper still performs its package validation before replay, checks the manifest and every file afterward, compares the download copies, and writes its original result only after success. None of those checks is copied into a weaker replacement or skipped.

## Mapping boundary

The bootstrap normalizes separators only for an exact historical-root prefix with a component boundary. An attempted historical descendant must be a listed source-manifest member. Empty components, dot components, traversal, alternate-stream syntax, NUL characters, unlisted files and missing targets fail. The resolved destination must remain within the source root and be a file. Symbolic links at the source root or on a mapped child path are rejected.

An existing absolute path inside the current packet is left unchanged. This is needed when a Windows checkout itself lies under the historical workspace. The native absolute-path test prevents a POSIX `C:\...` string from receiving that exception. Unrelated paths and file descriptors pass through unchanged, as in the old verifier. This is a narrow compatibility mapper for the frozen scripts, not a general filesystem sandbox.

Only `builtins.open`, `io.open` and the driver argument list are temporarily changed. All three are restored even when the driver fails. No global `Path` constructor is changed. The frozen driver's own report-write capture remains in effect.

## Independent checks and limits

I authored and ran the twelve tests in the pinned test file on Windows. They cover separator forms, prefix boundaries, unsafe and unlisted paths, missing members, child and root symlink rejection, current packet paths under the historical root, command and option fidelity, original-main delegation, cleanup on exceptions, and rejection of a changed original wrapper before import.

The tests also checked all 400 entries in the unchanged package manifest against their exact sizes and hashes. The historical source manifest has 382 entries within that 400-file packet. My initial test confused those two counts; correcting that test expectation required no artifact change. All twelve final tests pass.

The author separately reports a successful full Windows run through all 27 stages and the unchanged wrapper's final checks. Another review supplied 26 adverse path cases. Those are supporting reports, distinct from my own twelve-test execution. No successful Ubuntu replay is asserted here. Local WSL enumeration was unavailable, so the fixed Linux behavior must be observed in CI.

The source-root symlink check was added after my review identified that `resolve()` would otherwise follow a link at that root before inspecting children. The final code includes that correction. I found no remaining blocking defect in the pinned launcher, mapper or preservation of the original checks. Approval is limited to this infrastructure change; the existing mathematical contract and its acceptance remain unchanged.


## Addendum: canonical temporary fixture

The hosted Windows job at commit `1eb0218c75726a31c4926165779814470e01fc95` failed only `test_child_symbolic_link_rejected`. The mock compared the unresolved fixture path with the canonical path used by `make_mapper`, so an aliased temporary-directory spelling could prevent the mock from identifying its intended child. The failed job log is consistent with that mechanism; it does not establish the specific junction or alias configured on the runner.

The correction resolves the fixture packet root in `setUp` before constructing its descendants. No test assertion was removed or weakened. I independently reproduced the old failure using an existing `alias-component/..` spelling, which needs no junction privileges. The old test failed with the same `ValueError not raised` assertion. All twelve corrected tests passed both with ordinary temporary paths and under the controlled alias. The reproduction script and result are in the workspace portability directory.

The old review, acceptance and test files are preserved under `work/quartic-v13-release/portability/review-before-fixture-normalization`. The previous acceptance hash was `fa26e20372d873a5abc34f1fc3b5e70f2e03c3cd7bd169c42e878bc9bcd8f5dc`. This fresh acceptance binds the corrected test hash in the table above. Both application scripts, the original wrapper, all 400 packet entries and the mathematical acceptance remain unchanged. Fresh hosted CI confirmation is still required; the local checks do not assert that it has already occurred.
