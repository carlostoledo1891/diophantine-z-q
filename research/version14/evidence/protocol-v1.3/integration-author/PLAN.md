# v1.3 integration preparation

This local candidate starts from exact Git blobs of protected controller `18793299c641e653e32c9648c37c7a50ecd51928`. It overlays the ten independently accepted gate/runtime files and their runtime integration note. `INTEGRATION.json` records every baseline blob, overlay digest, production import edge and test import edge. Both live evaluator dependency maps match the resulting bytes. The original supplied protocol is preserved verbatim at `adapter/PROTOCOL-V1.3.md`.

The `tree` directory is an isolated review candidate. Its inherited protected configuration and packets still describe the historical v1.2 rollout. Their presence establishes baseline preservation only. They are not v1.3 inputs. This candidate has no fabricated PR identity, author event, decision, receipt or acceptance. Existing active rollout directories remain unchanged.

## Reproduction

Run `prepare.py` with the reviewed Python interpreter. It uses read-only Git object commands, verifies all accepted source hashes, and creates only this local candidate. Repeating preparation verifies baseline copies and regenerates identical accepted overlays. `run_tests.py` discovers every `test_*.py` module separately in controller, adapter, publisher, gate and immutable-cache, retains complete output and exits nonzero if any suite fails. `INTEGRATION.json` also lists the twelve existing-and-new explicit staging test roots. No coverage test is omitted or replaced with a fallback.

## Production staging requirements

Root must review this combined source closure and test results before creating a deployment commit. Preserve all baseline workflow bytes and source-bound CI routing. Stage the ten accepted files together, plus the coverage schema, exact normative protocol, runtime integration note, independent gate/runtime reviews and this combined review evidence. The production closure grows from twenty-two to twenty-three modules through `coverage_gate.py`. The candidate includes the original baseline source/test/documentation inventory, rather than regenerating historical evidence.

When using the existing curated staging tool, add `adapter/test_coverage_gate.py` and `controller/test_runtime_coverage.py` to its explicit TESTS tuple. Add `adapter/COVERAGE-V1.3.md`, `adapter/PROTOCOL-V1.3.md`, `RUNTIME-INTEGRATION.md` and independently accepted integration evidence to DOCUMENTS. Resolve staging against this integrated source tree. Recompute the closure and require it to equal this manifest before deployment. Do not retain a source pin that names different bytes or replace missing dependencies with an older module.

## Actual configuration sequence

1. Finish the frozen v1.2 rollout under its existing configuration. Preserve its evidence and historical standards.
2. Prepare actual v1.3 documentation commits using the six-file r3 manifest `2d5d9f5eb02ca11ac145d53b02f3c722ffb2e3e375464dd040b923227fa45a8d`. Pass that manifest explicitly to the accepted packet builder because its default remains r2. The user protocol SHA must remain `d3eb878bb3fb12d3b27d157e33f417f6f81bf2a873370f2758e8ccb1e5314d0a`; preserve historical v1.2 bytes.
3. Obtain actual PR base/head/test-merge identities, actual author runs and independently authored reports. Select a reviewed, nonempty protected proof/source inventory whose full Git entries are unchanged by the documentation PR. Include the exact changed six documents, actual review evidence and dossier paths in `allowed_nonmath_paths`, disjoint from proof paths.
4. Independently review each real inline `coverage_profile`. Bind its governing protocol path/hash, existing runtime audit-policy hash, exact proof paths and exact allowed paths. A non-substantive profile has no claim IDs. Build its actual committed dossier and packets using the accepted builder, then obtain the separate authenticated coverage decision alongside every other required decision. Coverage depends on all ordinary applications. Ordinary applications do not depend on coverage.
5. Put the reviewed profile directly on each protected controller job as `coverage_profile`. Bind packet path/hash, actual context and selected receipts through the existing owner-input process. A candidate-controlled profile is insufficient. Missing or invalid v1.3 profiles must fail before publication. Preserve all inherited operator/material/finding history and classify new actual evidence through the existing authenticated ingress.
6. Recheck live operator checkpoint and exact target contexts before ingress. Stage only the reviewed actual configuration/packet overlay with the combined source. Review the final Git blob manifest and deployed source SHA, then let root authorize the protected revision. Run actual ingress and final evaluation, read back App success and all required checks, and use the separately reviewed normal merge path only after every live prerequisite succeeds.

A successful non-substantive coverage decision concerns the bounded adoption diff. It does not recertify the existing manuscript under v1.3. Structural checks bind submitted coverage and reconciliation evidence. Source-first chronology and mathematical completeness still require independent reviewer attestation and substantive mathematical review.

## Prepared local staging

`stage.py` wraps the existing curator at SHA-256 `191cd76f17740153c958fb41d87a05a1a670a6d67dbfa8a383b72bc0d3e01a9b`. It implements the test/document additions above and verifies all accepted overlays and import edges after staging. The baseline stores its quota workflow only at `.github/workflows/protocol-quota-probe.yml`; the wrapper copies those exact bytes to the curator's expected template name inside the isolated tree. No workflow behavior changes. The resulting 129-file bundle manifest is `a7a880139ca8b146d7d64f6dea64da73f940638fb92fdd3afff9c3fcc954de4a`. It intentionally has no protected configuration. Root must prepare and review an actual-input overlay separately before deployment.

## Local test record

The initial Python 3.14 discovery exercised 642 tests. Controller 113, adapter 380, gate 53 and immutable-cache 22 passed. Publisher exercised 74 with one environment error because that installation lacked `cryptography`. The historical error is retained in `publisher-tests-PY314.log` and `TEST-RESULTS-PY314.json`; the synthetic real-RSA test was not skipped. A complete rerun with the required dependency was necessary and was completed successfully as recorded below. Deployment retains the unchanged hash-locked CPython 3.12/Linux dependency workflow.

The complete rerun used `C:/Users/glaze/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`, CPython 3.12.14 with cryptography 50.0.2. All 642 discovered tests passed, including the 74 publisher tests and the real synthetic RSA test. The current `TEST-RESULTS.json` records this successful run and exact executable commands. `TEST-RESULTS-PY314.json` and `publisher-tests-PY314.log` preserve the earlier environment error. No test was skipped. The earlier production-count statement was corrected to the actual baseline count of 22, growing to 23.
