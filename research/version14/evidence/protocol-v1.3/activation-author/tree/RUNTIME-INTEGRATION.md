# Protected profile runtime integration

Author `/root/protocol_v12_acceptance`. This is a separately frozen candidate
following the accepted eight-file gate candidate. The original candidate files
are unchanged. No existing live source, configuration or remote was modified.

Baseline `controller/runtime.py` has SHA-256
`be8dd9c490f1e8f0c03ff8ece6ed95a3b4b9b1f49f2496a3ae8f17b644753759`,
identical in the current source and deployed checkout when inspected.

A protected controller job may include one optional inline `coverage_profile`
object using the schema in `adapter/COVERAGE-V1.3.md`. The profile is not a path
to candidate content and is not read from the packet. Present null/string/list
values are rejected. `load_job` validates the profile against the packet with
`coverage_gate.select_profile` and keeps its existing four-item return value for
ingress callers. The main loop passes a copy of the configured profile into
`evaluate`.

`evaluate` copies the packet and profile, validates selection before restoring
state or constructing the publisher, and supplies the profile to
`ForkProtocolRunner`. The runner keeps a private copy and passes a further copy
to the live evaluation API. The accepted coverage validator then checks the
dossier's profile digest and all receipts. Existing authenticated source, intake,
ledger, publisher-generation and remote-state checks are unchanged.

Legacy jobs may omit the optional field and retain the existing path, subject to
the accepted gate's explicit legacy version checks. A v1.3 packet without a valid
profile fails. Empty job lists still check the approved controller revision and
return without loading App or ledger credentials.

`controller/test_runtime_coverage.py` exercises the actual protected JSON reader,
job parser, main loop, evaluation composition and runner. It replaces network,
state restoration and publisher I/O with marked test doubles. The final live
API double invokes the real coverage validator on synthetic records. These tests
establish configuration propagation and rejection behavior; they do not claim
cryptographic validation for their synthetic inputs. Existing `test_runtime.py`
separately exercises signed fixture ledgers, the live evaluator, publisher and
remote compare-and-swap path.

Run from `controller`:

```text
python -B -m unittest -q test_runtime_coverage test_runtime_idle test_runtime test_ingress test_git_state test_controller_blob_cache test_pr_state_projection
```

`RUNTIME-TEST-RESULTS.log` records the combined result. `CANDIDATE.json` lists the
two source/test hashes and the inherited gate hashes. These are candidate
fingerprints, not an independent acceptance or deployment authorization. Root
integration still must stage the reviewed sources and configure exact profiles
for the actual target packets before deployment.
