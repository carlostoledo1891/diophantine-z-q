# Compact policy independent review

Decision: changes required. Reviewer independently read the current generator, configuration, coverage account, repository AGENTS.md, workflow and relevant validator/replay sources on 2026-11-07. This review does not accept the compact policy.

## Scope and snapshot

Public HEAD is 8cc69491fb252375e7fd77601fad19e90846d86d. Private HEAD is 637919efb60bdfd350ef1ec2a6c8ebc4432a9f4d. Configuration SHA256 is df70effc527282a805414ee540e9bdced14a7c810c9535eb4ab1a8d3b4c9d96c. Findings apply to this snapshot. Future added shadow modules require renewed source-closure review. Backend model metadata is unknown.

All 152 public and 176 private direct hashes matched HEAD Git blobs. Some Windows checkout bytes have CRLF conversion. The raw-worktree discrepancies in verification.json were individually checked against Git blobs and all matched the policy, so those discrepancies are not policy defects.

## Blocking omissions

Both policies omit these five control files. The generator still omits them too.

- docs/manuscript-revisions/version13/validation-schema.json. The main function reads this file without an independently pinned hash at validate-applications.py line 177. Line 23 trusts its applicationIds to define required coverage. This is a validation selector.
- docs/audit-history/current.json. check_application_reviews.py sets CURRENT to this path and check_current loads it directly. The record selects manuscript, baseline, contracts, approvals and issue snapshot. Its internal hashes cannot freeze the selector itself.
- docs/manuscript-revisions/version8/revision.json. check_manuscript_revision.py loads MANIFEST and trusts its baseline, candidate and abstract records. Internal record hashing leaves the containing authority mutable.
- docs/manuscript-revisions/version10/revision.json. version10/check.py loads this file in build and takes baseline/candidate bindings from it. Later consistency checks do not independently freeze that root authority.
- .gitattributes. Checkout consumes these rules before Python starts. They determine the bytes against which replay manifests operate on Windows. The file belongs in the exact checkout control closure.

Add direct base hashes for all five in both policies and regenerate COVERAGE.json. Pinning only executable suffixes misses validation and checkout controls. The README claim about all source selection being fixed must account for these files.

## Eleven CI executions checked

The workflow expands eight YAML jobs into eleven executions. The matrix pairs run the same ordered commands on Ubuntu and Windows.

| Executions | Ordered local route and result |
| --- | --- |
| Version 13 Ubuntu and Windows | portability test, portable wrapper, application validator, audit-history validator. The portable wrapper checks original wrapper bytes before import. The original wrapper checks package entries before replay execution. Direct wrapper/bootstrap and package manifest protect the replay route. Application-schema and current-review selectors remain omitted. |
| Version 12 Ubuntu and Windows | audit-history validator, quartic498 wrapper, inventory validator. verify_portable imports standard-library modules before verifying package and repository pins. It checks generated builder text before Node execution and later invokes checked package scripts. Current-review selector remains omitted. |
| Version 9 Ubuntu and Windows | odd-product wrapper, inventory validation, version10 checker, valuation checker, audit validator, inventory tests. Source replay verifies its manifest before dynamic patch imports and generated builder execution. Final verify_all imports verify_elimination before verification, and both are direct. Revision10 and current-review selectors remain omitted. |
| Version 6 | quartic962 wrapper, inventory validator, inventory tests. package_integrity verifies literal expected manifest hash and full file inventory before local replay programs execute. Its additional JavaScript helper is direct. |
| Version 5 | quartic1272 wrapper, historical inventory validation, historical inventory tests. reproduce imports integrity before verification, and both files are direct. verify(HERE) precedes package copying and pipeline execution. |
| Construction | construction checker, row-hash replay, Lean structural checker, theorem application validator. Construction checks release_sha256 for every listed input before copying and running local programs. Row-hash and application validator programs are direct. |
| Paper | revision8 checker, odd-product inventory, version10 checker, valuation checker, paper builder. The builder fixes the copied TeX source. Revision8 and revision10 selectors remain omitted. |
| Lean | pinned elan installation, lake dependency-cache command, Lean checker/build. Local Lean declarations, Lake configuration, toolchain, dependency lock and checker are direct. External toolchain/dependency execution remains an explicit trust input. |

These source-order observations support the listed package barriers, but they do not close the validation-control omissions. No live GitHub gate acceptance, CI completion, deployment, or theorem acceptance is asserted.

## Evidence limits

The existing package-coverage count is supporting inventory only. This review does not infer authority from that count. The five concrete omissions suffice to withhold acceptance. Repair and re-review must use the current exact configuration digest and HEAD pair. No policy, repository source or GitHub state was edited by this reviewer.
