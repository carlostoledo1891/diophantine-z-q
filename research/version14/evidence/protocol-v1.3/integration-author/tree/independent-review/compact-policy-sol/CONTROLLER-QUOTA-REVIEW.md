# Controller token request scaling

Read-only review on 2026-11-07. No deployed or source files were edited. This report does not diagnose a current live quota failure.

GitState.load performs n+6 requests for n state files excluding index.json. It reads identity, tip, commit, recursive tree, index blob, n content blobs, and tip again. append reloads authoritatively before writing. RemoteState.advance then reloads again after the write. A successful evaluation saves generation state at begin, before_success, and finish. This repeats the complete state inventory six times. Ref and generation checks add further requests.

I instrumented the existing successful runtime fixture by wrapping its fake controller API. With 23 state files, evaluate used 453 requests, including 153 blob GETs. With 100 state files, evaluate used 915 requests, including 615 blob GETs. Both successfully published. Padding used additional immutable snapshot files and changed no signed ledger contents or production code. The difference is exactly six requests per additional state file. In this fixture the total is 6n+315.

runtime.main constructs another RemoteState per configured job. Its initial load and guard add n+8 requests, and the per-job guard adds 2. With two successful jobs starting at n=100, the fixture-derived projection is about 2073 controller requests, allowing three added publisher snapshots between jobs. This is a projection, since the live ledger/context can change the number of fixed checks. It excludes checkout and unrelated workflows.

GitHub documents the usual GITHUB_TOKEN limit as 1000 requests per hour per repository. New jobs share that repository quota. The source's internal 100000-request limit is a separate bound. The mathematical repositories' App installation token has a different budget. https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api

The public ingress log 42439545480 shows successful finalization and an empty unclassified-material list. It exposes no request counter or rate-limit headers, so its elapsed time cannot establish remaining quota. The earlier evaluate log exposes a generic blocked result and cannot establish its cause.

If a real quota failure occurs, retain the failure receipt, avoid immediate retry loops, and wait for the observed reset. The smallest source mitigation is an instance-scoped bounded cache of independently verified immutable blob bytes in GitState.blob. Key it by exact blob SHA within the fixed repository, preserve size validation on hits, and keep load's SHA256 and manifest membership checks. Continue reading identity, refs, index selection and CAS authority fresh. This reduces repeated ledger reads without trusting a caller-supplied mutable Snapshot. It requires its own tests and independent review before deployment.

Blob caching alone does not prove that two polls per hour fit. The successful fixture still has substantial repeated mutable guard traffic. After any change, measure the actual controller transport count and response quota headers, and choose a polling interval that includes ingress and manual dispatches. No current schedule guarantee follows from the App-side immutable-source estimate.
