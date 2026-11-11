# Independent structural review of final-records-002

Reviewer: `/root/astra_v14_baseline_theta`. Date: 2026-11-07.

**Result: no structural defect found in the frozen packet.** This is a byte-binding, inventory-completeness and evidence-reference review. It is not mathematical acceptance of the 351 assertions, a proof of exhaustiveness of the inherited 263-edge relation, approval of the current contract, a gate receipt, or publication authorization.

The reviewed packet is `work/quartic-v14-prep/inventory/final-records-002`, with exact pins:

| Object | SHA-256 |
|---|---|
| FROZEN-MANIFEST.json | `45b012aaf2fc75698c8c62d4a9ac24fe2593116d1a75a838072365a938aa75f5` |
| APPLICATIONS.json | `a3c7f119e53f59ed81f4f9a3ac6b57f069c1d24da191aef5e150b38a50933abf` |
| quartic-application.json | `92dac763a44921556152bd0cbdf050eed7fb26ea12fb935b6060345c138f6ad1` |
| Current manuscript | `b8421edc569a832c9c4271e3592b10df58e75d25f4dc5619c2b4a6766157044d` |
| Current addition | `b5840b3598c655fc7f3db3475b089b65800b98f136a601c4360c72d22d6f95a0` |

## Independent checks

I read the packet schema, installer contract checks, supplied checker, export logic and representative records, then wrote `independent_check.py` without importing the author's validator or builder. It uses strict JSON parsing, raw bytes for hashes and line slices, and a read-only resolution of staged files over the preview repository. It reports its complete resolved file set. The separate supplied-checker replay is corroboration, not the basis of the independent result.

All 24 manifest-bound files match their hashes and byte lengths; the frozen file enumeration is complete. Local and staged copies of the applications, contract and selected maps agree. The current addition occurs byte-for-byte exactly once in the b842 manuscript, beginning at line 21633. All required labels resolve uniquely. Each of the 84 pre-layout/current passage pairs is checked by its own raw span hash, by replay of the three exact pinned formatting substitutions, by unique content occurrence, and by mapping the current addition passage into the current manuscript. The entire transformed pre-layout addition equals b584. No fixed-line-shift assumption substitutes for this content check.

All 39 application IDs are unique and exactly match the frozen schema and baseline records. Each has all nine obligation statements and all nine dependency dispositions: 351 total. All 61 `preserved` statements are byte-equal as decoded strings to the identified baseline obligation; the remaining 290 have explicit replacement dispositions. Prior record hashes and inherited source/convention records match. Every obligation has nonempty source and consumer span lists, and every consumer is bound to the current manuscript, not the old manuscript or pre-layout addition. `OBLIGATION-COVERAGE.json` enumerates all 351 checked slots, their text hashes and evidence counts.

All 263 application/entry edge pairs are unique and equal the complete frozen R6 pair set. Each role matches the route selection exactly, rather than merely belonging to an allowed vocabulary: 185 `current_consumer`, 31 `supporting_derivation`, and 47 `archived`. The duplicated selected-application map is identical. Current/supporting edges have source and current-manuscript consumer evidence; archived edges have no such asserted evidence. All endpoints resolve. `EDGE-COVERAGE.json` enumerates the 263 exact record hashes and dispositions.

All 48 entry IDs are unique and equal the route's entry set. Their roles, historical proofs, historical reviews, recorded components and selected components match that source. The precise breakdown is 32 `current_application`, five `supporting_source`, one `artifact_repair_history`, four `superseded_intermediate_circuit`, and six `unused_alternative`. Thus the summary phrase "six supporting/provenance entries" must not be read as six supporting mathematical applications. Current and supporting entries have their historical proof spans and current derivation spans; archive/repair-history entries retain their historical locators and review pins without being promoted into current proof steps. All 48 portable historical review pins resolve. Historical headings and ranges were checked, including the three explicit `Whole report` locators. `ENTRY-COVERAGE.json` enumerates all 48 entries.

The assembly list has 24 unique IR identifiers, agrees with the route and selected map, and obeys every declared assembly dependency. The selected final pair is the corrected `reciprocal299r2` and `ordinaryReciprocal299_314`. This structural result does not assert that each intermediate assembly component is a current theorem application.

The contract targets b842, has nine obligation records, resolves every listed source/evidence ID, and binds its three reviewed edits to their canonical hashes in the exact current new-edits list. Its 11 construction/application/consumer spans match the manuscript bytes. All staged installation-manifest files, all read-only dependencies, and all SOURCE-PINS entries checked against actual files. The independent traversal checked 146 distinct resolved files and 234 distinct raw line spans. Repeated use of the same evidence is not counted as a new independent source.

The 39 gate text fragments have the same application IDs, source metadata, required/constructed strings and proposed evidence references as the application records. They expressly remain incomplete caller-authored fragments. Their `checked` text statuses do not establish authenticated reviewer identity or mathematical acceptance. The packet correctly leaves actual identities, ordinary application dependency edges, and complete base/head file and commit coverage to the parent gate integration.

## Corroboration and limits

The author's read-only `check_final.py` was replayed with output directed into this review directory. It passed its eight in-memory negative controls: missing obligation, missing disposition, self-acceptance flag, wrong ordinary artifact, old manuscript, missing edge, wrong coefficient bound and stale current span. It reports 118 entry proof/current span occurrences and 48 historical review pins. `PROVIDED-CHECKER.json` contains the complete replay output.

No approval file, current registry entry, packet file, repository file or remote state was edited. Python was invoked with `-B`; all new review artifacts are confined to this directory.

The fresh proof reviewer must still decide whether the actual current arguments discharge the obligations and whether the bound source passages justify each claimed map, condition and downstream use. I have not replaced that decision with counts, hashes, historical favorable reviews, or nonempty prose. Likewise, this review preserves the packet's published-source qualifications and does not re-prove inherited external theorem applications. There are no structural defects to refer back to the author from these checks.
