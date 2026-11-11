# Isolated V15 controller integration

This candidate applies the independently reviewed routing003 files to the exact deployed a7016ba2 controller tree. It is not deployed and is not authorization to switch ownership or initialize a state branch.

The six-file delta retains the legacy configuration, existing key identifiers, App/installation identities and publisher code. The 200 other base files are unchanged. CODE-DELTA.json and CODE-DELTA.diff identify the exact changes; BASE-FILES.json records every original blob.

NAMESPACE-INPUTS.pending.json contains proposed new ledger names, observed existing identities, and null fields for all unobserved final state, packet, Git, review and routing-pin inputs. OPERATIONS.md gives the owner-only sequence. No new key or App is proposed. Historical publisher mappings must be checked against the authenticated final state export before use.

Tests

The initial 187-test run had three legacy fixture incompatibilities with existing deployed behavior. The two REST-only cache fixtures failed when an unmocked protected acquisition attempted a fake repository read; the diagnostic expectation omitted two already-deployed sanitized fields. The initial failure logs and the earlier launcher timeout are preserved. BASE-TEST-INTERFACE-COMPARISON.json proves the implicated methods are unchanged. The separate test adapter mocks acquisition only for that old REST fixture and updates its exact diagnostic expectation; production code is unchanged. TEST-COMPAT-RESULT.json records the resulting run.

Review limits

This is implementation readiness only. Final authenticated export, no-writer observation, old-state preservation, complete ownership reservation, actual V15 head/job/packet and a reviewed create-only bootstrap remain required. The protected routing digest is intentionally not computed from invented inputs. No current state snapshot, secret, workflow variable, repository ref or remote object was changed.
