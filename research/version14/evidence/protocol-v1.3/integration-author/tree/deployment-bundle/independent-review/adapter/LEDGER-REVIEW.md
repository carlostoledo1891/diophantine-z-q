# Independent operator-ledger review

Agent02 accepts the frozen pure append/verify/export component at the hashes below. No implementation defect was found within its stated trust model. All 32 author tests and 20 independently constructed tests pass. This acceptance does not cover actual observation capture, protected persistence, a schema 2 evidence adapter, GitHub publication or live enforcement.

| Source | SHA256 |
| --- | --- |
| `adapter/operator_ledger.py` | `5e2cec65c3b516f62ec4bbd9ae071c431c11ab7456edd4d7000c986782c072d7` |
| `adapter/OPERATOR-LEDGER.md` | `2936b1ba0ff032ee85e883b18916d7aee7f57b72f18f28bb47b8515f3c8aec23` |
| `adapter/test_operator_ledger.py` | `4b4471ebb44f40591da3ad72b27efc8e0a3a3ae16af9e5680679b932e37ce0ef` |
| `independent-review/adapter/test_ledger_review.py` | `939f2fbb6fea1f12be2e8ddb0e4298d9fd77036dec54d305f23a428499736675` |

The reviewer made no changes to the producer files. `run_ledger_audit.py`, `LEDGER-CHECKS.json` and the `ledger-*-tests.log` files reproduce the review's executed checks. All identities, keys, observations and reports used in these tests are synthetic.

## Integrity and rollback

The independent fixture builder signs rows without importing the producer's signing, hashing, canonicalization or fixture functions. Those rows verify under the implementation, and rows produced by `append` exactly equal the independent reference rows and checkpoints. The MAC covers the complete event and the schema, ledger identity, sequence, previous hash, key identity and operator identity under a fixed domain. The next head hashes the authenticated row. Tests reject field tampering, a MAC without the required domain, wrong keys/operators and malformed event histories even when a test key signs them correctly.

An externally supplied current checkpoint is mandatory. It fixes the ledger identity, exact sequence and head hash; an authentic shorter prefix cannot verify against it, and an unexpected extension cannot verify against an older checkpoint. The independent test also intentionally supplies an authentic old prefix together with its old checkpoint and confirms that it still verifies. That is the expected boundary: the module cannot tell that a caller has rolled back both its inputs. The external checkpoint must be protected and current, not read from candidate files or selected by the candidate.

Genesis is checked against the ledger identity even for an empty list. Sequence, schema and candidate identity fields reject boolean/float aliases where integers are required. Missing checkpoint or key registry fails rather than falling back to an unauthenticated result.

## Review state and export

Only observed run IDs can be authors or reviewers, and a run cannot be redefined. Stable agent identity determines independence, so another run of the authoring agent cannot supply an independent acceptance. The trusted operator must provide the real stable identity and complete contributor list; the module does not derive these from the observation text.

Each target freeze binds candidate, target, dependency digest and author runs. A new freeze for the same candidate/target invalidates older reports, including when only authorship changed. Independent tests add the former reviewer to a refreshed author list and verify that neither the old acceptance nor a new self-acceptance exports. A new dependency freeze requires a new matching report.

For a given freeze and stable reviewing agent, a later decision supersedes the old one, including when recorded under a different run. All three nonaccepting decisions invalidate the earlier acceptance. Original reports remain in verified state. Export compares every expected target/binding field, including schema, commits, trees, policy and content-manifest hashes. Both SHA-1 and SHA-256 candidate bindings were exercised.

The original report bytes survive canonical base64 encoding, including CRLF, NUL and non-UTF-8 byte values. Export recomputes their SHA-256. Empty, oversized and noncanonical report/observation encodings are rejected. Export remains labelled operator-attested, with provider cryptographic attestation false and merge authorization false.

Another reviewing agent's objection does not automatically suppress export of this agent's positive receipt. The independent test confirms that the objection remains in verified state. This matches the documented component boundary: the full findings intake and eventual gate must process every received report. Selecting one positive receipt is not proof closure and must never replace that complete inventory.

## Required integration contracts

- The operator/capture bridge is trusted to record actual observations accurately, preserve original bytes, supply stable identities, record all substantive authorship, and order superseding decisions correctly. Arbitrary text labelled as an observation is not provider attestation. Every holder of an authorized HMAC key can create operator-authenticated records.
- Persistence must serialize appends and atomically update the independently protected checkpoint. Tests create two individually valid appends from one prior checkpoint; either fork rejects the other's checkpoint. The pure module does not choose which branch should commit or merge both events. A transaction or compare-and-set is still required, including crash recovery without silently discarding a received event.
- Python return values are mutable. Mutating an appended event through a retained reference causes later authentication to fail; the function does not provide immutable data structures. Persist the returned authenticated bytes and checkpoint as one protected operation.
- The exported receipt dictionary is not itself a portable, self-verifying signature. Consume it within the protected process, authenticate its transport, or rederive/verify it against the trusted ledger and checkpoint at the receiving boundary. Loading candidate-supplied export JSON would bypass this component's verification.
- A future schema 2 adapter must compare the exported target, dependency, authorship and report digest with the actual packet and consumed report blob. It must preserve complete findings intake, policy authority and current candidate bindings. Those comparisons are not implemented by this ledger alone.
- Key rotation/revocation and checkpoint retention are supplied policy. This module authenticates using the caller's registry; it does not decide which historical keys should remain trusted. Replay of an unchanged authentic history is not live freshness.

The implementation replays the supplied log when verifying or appending. It does not implement a bounded persistent database or guarantee a particular scaling profile. No real secret, provider credential, collaboration capture or GitHub action was used in this review.

The accepted component provides integrity and consistent receipt selection for accurately recorded operator observations under protected keys and checkpoints. The live gate remains not ready. This review makes no claim about mathematical truth, actual reviewer reasoning, complete semantic discovery or current merge eligibility.
