# Deployment status

As reported by the release integrator on November 7, 2026, the controller remote main and protected `PROTOCOL_APPROVED_SHA` both identify `ce9c4cf5f08eb5a56eabec041fddd81f2dddcc5f`. Controller run `42452003901` succeeded with the empty active-job configuration `jobs: []`. This is the deployed v1.3 runtime. The present v1.4 extension is an isolated proposal pending independent review, installation, deployment and new remote readback. It is not live v1.4 acceptance.

This status records the integrator's reported readback, not a second remote observation by the implementation author. The deployment integrator must bind the actual readback evidence and update this status after any later deployment. An idle successful run does not accept a mathematical PR.

The previous status and deployment-decision bytes are preserved in `deployment-history/2026-11-07-before-v1.4/`. They describe earlier pending/failed v1.2 activity and the original deployment proposal. They must not be read as the current deployment state.

Branch protection continues to require the eleven Actions checks and the dedicated independent-review App check. No second human approval is introduced by this proposal. The extension does not change active jobs, signed observations, receipts, ledger keys or branch protection. It checks recorded evidence, not mathematical truth or honest review.
