# Independent combined v1.3 source integration review

Reviewer `/root/sol_protocol_final_review`. Integration author `/root/sol_protocol_policy_review`. November 7, 2026.

## Decision

Accepted combined code and staging readiness against controller baseline `18793299c641e653e32c9648c37c7a50ecd51928`. Final integration-author/MANIFEST.json SHA-256 is `50c322d6a88ab0ae800bf4b9a39fd371cfac72c153514a8bcd4249b49d2ea796`. PLAN.md is `fd25119c116bd17b0db59fab79d47daefee473c6cb4596d083a8d6c7ffb6b746`. Staged BUNDLE-MANIFEST.json remains `a7a880139ca8b146d7d64f6dea64da73f940638fb92fdd3afff9c3fcc954de4a`.

This acceptance covers the combined source and staging machinery. The bundle intentionally lacks an actual protected configuration. Actual v1.3 PR contexts, proof inventories, profiles, dossiers, author observations, reviewer decisions and receipt selections remain separate review targets. This report authorizes no deployment.

## Independent checks

I inspected prepare.py, stage.py, the pinned curator, the actual integration manifest and staged files. My check_integration.py verifies every manifest hash, all eleven declared overlays against their accepted source files, all remaining baseline copies and every staged file hash. The baseline contains 143 files. The eleven overlays are the ten accepted source/test/documentation files plus the runtime note.

I independently reconstructed static imports, including imports inside functions and the explicit dynamic legacy fixture edge. The actual closure contains 23 production modules and 47 test modules. It matches both integration and staged manifests. All 20 previously staged test modules remain. The added coverage tests and runtime-profile tests are explicit roots. The baseline had 22 production modules, with coverage_gate.py adding the twenty-third. The initial plan count was corrected.

The staging wrapper binds the original curator hash, stages against the isolated tree, retains both live dependency maps and verifies their exact bytes. The quota template is a byte-identical copy of the baseline workflow. No source-bound CI map, live workflow behavior, credential permission or existing packet is changed by this preparation. The final staged bundle has 129 files and no protected configuration. Its two embedded independent component reports retain their reviewed bytes.

## Test evidence

The final pinned CPython 3.12.14 run reports 642 passing tests with no skips, comprising controller 113, adapter 380, publisher 74, legacy gate 53 and immutable cache 22. I parsed each complete recorded result and its exit status. I independently reran all 74 publisher tests with that interpreter, including the real synthetic RSA case, and obtained 74 passes in 4.107 seconds. Earlier component reviews separately record my independent core, runtime and coverage executions on the exact inherited components.

The earlier Python 3.14 missing-cryptography error is preserved in TEST-RESULTS-PY314.json and publisher-tests-PY314.log. The final plan correctly distinguishes that historical environment failure from the completed pinned-runtime rerun. No skipped or substituted test is used to turn that earlier error into success.

## Final boundaries

The plan orders completion of the frozen v1.2 rollout before actual v1.3 input preparation. It explicitly selects the reviewed R3 documentation manifest, requires final committed report/dossier bytes, reviewed inline profiles and separate non-author coverage decisions, then requires exact source/configuration review and authenticated live readback. Historical evidence is preserved. The non-substantive adoption result cannot establish full manuscript coverage under v1.3.

No material code or staging issue remains in this reviewed scope. All production and author artifacts were left unchanged by this reviewer.
