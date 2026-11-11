# Independent protected-store and evidence-bridge review

Agent02 accepts the frozen local persistence and schema 2 evidence-derivation components within their documented protected-configuration and trusted-context contracts. No implementation defect was found in this review. All 24 component tests, 32 accepted-ledger tests, 44 accepted-schema-2 tests and 21 independent tests pass.

This is not acceptance of a production capture service, real OS isolation, live context verifier, GitHub publisher or activated ruleset. No production state, real keys or remote settings were created or changed.

## Exact source scope

| Source | SHA256 |
| --- | --- |
| `adapter/protected_ledger_store.py` | `8bd48c4439079a75976afd61aa8a7acaf319daf01b6d34df589883a0e2c292d2` |
| `adapter/ledger_evidence_bridge.py` | `72b37bd78377f94131d7bf338a83becee197a65fb00d495836369df22d3f358f` |
| `adapter/STORE-BRIDGE.md` | `8de2c6b463d92914d1ec31b823d29cffb918a32dbf45a11a53c4f7312ec54bb5` |
| Independent tests | `3db69de6f948008710e4b104f985e11290d3c6ee3a4054f7d7a369721bffdb03` |

The accepted ledger, schema 2 core and manifest collector hashes are recorded unchanged in `STORE-BRIDGE-CHECKS.json`. `run_store_bridge_audit.py` reproduces the four suites and checks source hashes before and after. All test databases live in temporary directories and all context/observation/key inputs are synthetic. The independent bridge fixtures use the reviewer's earlier independently constructed schema 2 records, not the producer's fixture builder.

## Persistence findings

The store uses an immediate SQLite transaction to check the expected database checkpoint, verify the authenticated history, and commit the next signed row with its database checkpoint. A subsequent compare-and-swap advances the separate anchor. Independent concurrent tests start three writers from one expected checkpoint and obtain exactly one committed append. Failed event validation leaves both stores unchanged, and reopening verifies the same rows and checkpoint as the independent HMAC-chain implementation.

An interruption after database commit but before anchor advancement leaves a signed tail and a checkpoint disagreement. Normal reads block. The independent test injects an anchor-write exception after the database commit, confirms that reads and stale appends fail, and then recovers explicitly forward. The recovery checks the exact expected database state, the current external anchor, the old authenticated prefix and the complete signed tail. It does not lower an anchor. Tests reject altered tail bytes, stale expected database state and attempted backward recovery after a database-only rollback.

This protocol is deliberately not a distributed atomic transaction. Two files with different paths are not proof of independently protected history. Restoring both database and anchor to an earlier valid state remains undetectable; the independent test demonstrates this limitation. Actual backup/restore policy must keep a trusted current anchor outside a ledger rollback. SQLite synchronous commits were exercised through ordinary temporary-file operations, not power-loss or hardware fault testing.

Stored JSON must be canonical, entries must have consecutive database sequence numbers, and the authenticated chain must verify. Tests reject duplicate JSON keys, sequence gaps and tampered payloads. Missing state is not recreated by a read. Bootstrap is explicit and refuses existing files; interrupted bootstrap still requires an operator procedure rather than automatic trust reconstruction.

`ProtectedPath` rejects declared candidate-write descendants, relative or unresolved paths, and a symlink at the selected state path. These checks validate supplied configuration. They do not set permissions, enumerate all aliases or discover undeclared write access. The trusted operator must actually protect the code, keys, database, journal files and anchor against candidate execution. A separate path string alone is insufficient isolation.

## Evidence derivation findings

The bridge derives receipts from the authenticated ledger each time, using the accepted export checks. It does not trust standalone exported receipt JSON. Application, finding and assembly target/dependency digests are recomputed. Independent tests compare all target tuples with separately calculated receipt values, including an application dependency and a duplicate finding linked to another disposition.

Selected report identities must cover exactly the expected targets, bind the current candidate and match the current freeze and reviewer decision. The bridge obtains run identities and author sets from verified ledger events. A fresh context does not rescue an acceptance superseded by a later rejection. The schema 2 core still performs its own complete changed-file, authorship, obligation, findings, receipt and assembly checks.

Report matching uses the observed raw report digest and the complete head manifest; the resulting pin is then passed to schema 2's actual blob verification. Independent tests confirm that a missing blob reader or corrupt report body fails. A successful synthetic evaluation performs the expected three unique evidence-blob reads. The caller's packet remains unchanged because evaluation uses a private copy.

The separate context verifier must authenticate origin, old policy, complete findings and report selection for the current checkpoint. The bridge binds its context to the digest of all recorded reports, including negative and superseded ones. Tests confirm that an objection reaches the supplied inventory, an altered inventory digest fails, and even a new non-report ledger event invalidates an old checkpoint-bound context. A dictionary with a `verified` flag is not accepted as context.

The inventory digest proves which report inventory the context references; it does not itself prove that the context classified every objection correctly. The independent synthetic context can deliberately claim a complete findings list while ignoring an objection, and the bridge relies on that trusted claim. This is the declared external-context contract, not an implemented objection resolver. A real context verifier must reconcile the entire inventory and registered external audits.

The store is rechecked before and after core evaluation. Independent tests append during blob reading and leave a database-ahead/anchor-behind state during reading; both prevent a successful result. A final check cannot make a later GitHub publication atomic with future ledger events. The publisher still needs generation/freshness handling at its own boundary.

## Remaining deployment scope

Accepted successful evaluations retain `merge_authorized: false`, `deployment_eligible: false`, unimplemented live GitHub state and no provider cryptographic attestation. The authentication label describes operator-ledger verification plus an externally trusted context, not independent provider authentication.

Actual collaboration capture, correctly protected host configuration, live repository/PR/policy/intake verification, operational backup/recovery and an isolated App publisher remain unimplemented or unreviewed. The live gate remains not ready. These local components preserve authenticated records and derive offline evidence; they do not establish mathematical truth or current merge eligibility.
