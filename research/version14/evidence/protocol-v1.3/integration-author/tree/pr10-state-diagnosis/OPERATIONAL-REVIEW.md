# Operational integration review

Accepted the requested staging-selection, status and idle-preparation changes within their stated scope. Reviewer /root/sol_protocol_policy_review. No deployment or stage operation was run.

stage_bundle.py SHA256 6ed6d008c80fa0e2f99871a0de4d813d5feaf5ceabed8789690fc46346b00bff includes adapter/test_source_bound_ci.py in TESTS and adapter/SOURCE-BOUND-CI.md in DOCUMENTS. Both files exist. Invoking only the static closure function confirms that the new test is included with its imported local dependencies. This accepts inclusion in the staging selection, not the separately reviewed CI semantics or a later complete bundle hash.

DEPLOYMENT-STATUS.md SHA256 494dd22d89f3a0970f82bbca020f88e98466c4337af64b71cd659a87e15f0ea4 distinguishes the active App gate and merged setup from pending v1.2 PRs. It preserves the failed evaluation status and need for repairs, fresh captures, successful evaluation and protected merges. It makes no new proof claim. Live status is based on the recorded execution evidence supplied for this review.

prepare_idle.py SHA256 dd9814578831c05658afb433c2b613f46ddfef19982242a1000a50d1e95ca8ee retains the accepted active configuration pin and changes only its output jobs list to empty. It now sources overlay history from deployment-v3. Ran this local preparer as requested after preserving the previous idle files under idle-prior/.

The regenerated idle config is byte-identical to the accepted original, SHA256 00c3118bc4bd74dd0871e297c9ab2d733f2185aeb24d44f0abe6ef397d5b2c97. The idle overlay SHA256 is 21d6de0c546ee3d81955f6a779d81b564dbbc9c555c5550b70ebfe3ff5aa6a05. No prior mapping changes. Two projected-v3 batch mappings are added, and all eighteen non-config history mappings are retained. The sole current config pointer names the idle config. OPERATIONAL-CHECKS.json records the exact comparisons.

The idle preparation remains a future transition after both PRs have actually merged and remote readback is verified. This review does not authorize prematurely dropping their active evaluations. No App, ledger, branch-protection, publisher, CI or mathematical source file was changed by this reviewer.
