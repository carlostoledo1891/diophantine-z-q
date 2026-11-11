# Isolated V15 routing integration

The candidate is deployed controller a7016ba2c686dcd6a49be5654eda19fff31a2c51 plus six accepted prototype003 file changes. Its config remains byte-identical legacy v1. It is not an activated V15 deployment. No ledger, key, App identity or sole-publisher implementation was changed.

## Offline checks

Run Python -B run_tests_compat.py from this directory using the bundled Python runtime. TEST-COMPAT-RESULT.json records this run. The first local attempt hit its 20-second launcher timeout and is preserved as ATTEMPT1. The original completed run is TEST-RESULT.json: it had three legacy fixture failures, not a clean pass. TEST-COMPATIBILITY.json and BASE-TEST-INTERFACE-COMPARISON.json disclose the test-only adapter and the initial fake-repository read attempts; no production credential or state was used. Production code and original test files in candidate/ remain unchanged.

## Owner sequence after actual inputs exist

1. Finish V14 and hold evaluator and ingress writers using the existing owner procedure. Read actual terminal status and protected state. Keep protocol-state unchanged.
2. Use the existing guarded RemoteState and trusted current keys to call namespace_lifecycle.export_namespace. Independently seal the complete descriptor and bytes. Recheck old ledger IDs against this actual export; STATE-BOOTSTRAPPED is only historical identity evidence.
3. Run inspect_export on those bytes with its separately reviewed descriptor digest, then ownership(states, old_branch, publishers). Compare all publisher identities with HISTORICAL-PUBLISHERS.json. Missing identities block preparation. Retain every authenticated freeze, capture, generation and target owner.
4. Build exact old/new route objects. Preserve old namespace IDs and all old owners. Add only the actual reviewed V15 head under the same App and installation. Populate the actual V15 job, packet and reports. Proposed new ledger IDs are names only; they are not new keys.
5. Independently review old/new config, export digest, old route, publishers and cutover observation. Call prepare_transition with that receipt. Only its fully bound routing object yields the protected variable digest.
6. Obtain a fresh reviewed controller/ref observation with the actual candidate controller commit, unchanged retired state and absent protocol-state-v15 ref. Call prepare_bootstrap with this observation and receipt. It returns proposed bytes only.
7. The owner installs the reviewed code/config and digest while writers are held, rechecks identity/ref absence and uses create-only initialization. A concurrent creator must cause failure; never force or overwrite a state ref. Independently verify the complete new genesis and a real-input transaction rehearsal.
8. Enable only the reviewed V15 job. Preserve protocol-state and all historical evidence. Keep existing keys, App and sole publisher. Never clear the routing guard to bypass ownership checks.

The exact lifecycle functions are the accepted prototype. Final V14 export, V15 source/packet, fresh no-writer/ref observations and their independent decisions remain required. This folder performs no production operation.
