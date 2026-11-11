# Deployment status

This revision contains v1.4 runtime support. Activation requires the protected `PROTOCOL_APPROVED_SHA` to match the deployed controller commit. Actual activation and remote readbacks are recorded separately. Runtime support alone is no mathematical acceptance. An idle successful run does not accept a mathematical PR.

## Historical observation, November 7, 2026

The release integrator reported that remote main and protected `PROTOCOL_APPROVED_SHA` both identified `ce9c4cf5f08eb5a56eabec041fddd81f2dddcc5f`. Controller run `42452003901` succeeded with the empty active-job configuration `jobs: []`. This observation concerns the preceding v1.3 deployment; it is not a permanent claim about the current remote revision or evidence that v1.4 has been activated. The implementation author did not perform a second remote observation.

The prior status and deployment-decision bytes are preserved in `deployment-history/2026-11-07-before-v1.4/`. That directory also preserves the v1.4 preactivation proposal status as `V1.4-PREACTIVATION-STATUS.md`. Earlier pending or failed v1.2 activity and the original deployment proposal remain historical records.

Branch protection requires the eleven Actions checks and the dedicated independent-review App check. No second human approval is introduced. Runtime support does not change active jobs, signed observations, receipts, ledger keys or branch protection. The gate checks recorded evidence, not mathematical truth or honest review. Research evaluations still need exact evidence and independent review under the selected protected protocol profile.
