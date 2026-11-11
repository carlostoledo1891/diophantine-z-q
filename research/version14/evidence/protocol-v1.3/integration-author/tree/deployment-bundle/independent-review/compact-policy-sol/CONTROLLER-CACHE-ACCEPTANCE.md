# Controller immutable blob cache acceptance

Reviewer /root/sol_protocol_policy_review accepts the narrow candidate runtime.py SHA256 3a58b29457eefa4fc02226db07c3589db82e381fad680516cb6500882175ca4c and test_controller_blob_cache.py SHA256 6909b6d6f046273452f2cebd428dec821ab3dd68f98b892e340cf5d84660e06b. Files reviewed under work/protocol-ruleset-20261107/state-cache-candidate/files/controller. No candidate source was edited by this reviewer.

Read the complete source delta and the tests. Independently ran the 7 cache tests and 14 existing runtime integration tests. All 21 passed. controller-cache-tests.log records the run. The mutable-ref race and late-comment rejection tests remain in the passing runtime suite.

The one ControllerHTTPS instance is shared across the configured jobs. Cache admission follows the unchanged fixed-origin endpoint allowlist and an authenticated successful response. Only exact GET git/blobs/SHA paths qualify. Admission checks the requested SHA, integer size, base64 decoding, decoded length and Git blob hash. Cached values are immutable bytes. Every hit returns a newly constructed response dictionary and base64 string. Mutable responses, writes, repository identity, refs, commits and recursive trees remain live. Each GitState load still verifies the selected index, membership, size, SHA256, ancestry and final tip. Caching bytes of an index blob by immutable SHA does not cache which index is current.

The cache bounds retained payload bytes at 64 MiB and entry count at 4096. These are payload and entry bounds, not a total process RSS guarantee. Normal serial request execution admits each SHA once until eviction. No persistent or candidate-supplied preseed path was added.

Diagnostics disclose only request/hit counts and numeric limit/remaining/reset response headers. They run in main's finally block after transport construction, including failure paths. Cache hits do not consume the network request counter. Headers reflect the latest actual response, not an independent quota reservation. Tokens, URLs, response bodies and request bodies are not logged.

## Measured two-evaluation check

Independently constructed a fixture with 100 state files and the real candidate ControllerHTTPS over the test HTTP backend. Ran two successful sequential evaluations with the same transport and fresh RemoteState instances. The first used 416 requests including initial remote load, and the second used 321 additional requests. Total was 737 requests with 1340 cache hits. Both succeeded and the state inventory grew to 106 files. controller-cache-count.json records this result.

The two evaluations reuse the fixture's context. Live public/private contexts and observations may require different fixed checks, and this test cannot establish the live remaining quota. Compared with the earlier 2073-request projection without caching, it verifies the intended shared blob savings. It does not establish that two such runs per hour fit a 1000-request budget.

Hourly initial polling is reasonable pending actual quota diagnostics. At this fixture count it leaves about 263 requests for other controller activity within an otherwise unused hour. Manual dispatches and ingress share the repository token budget and require checking remaining/reset headers first. The next deployed run must establish actual counts and remaining quota. No current live quota failure is asserted.

Authenticated Git fetch could provide verified blob bytes in a separate future design, but this accepted candidate has no Git seeding. Such a design would need a fixed trusted controller remote, fresh bare temporary repository, bounded depth/no tags, no checkout or hooks, exact Git object validation plus current index size/SHA256 verification, and unchanged live ref/CAS checks. It is deferred until evidence requires it.
## Read-only quota probe addendum

Accepted quota_probe.py SHA256 972a1b7faae6e1ce6a6e17abd46ad0f9c6075641243857acab73e78c2efe5793 and protocol-quota-probe.yml SHA256 8dcb0de11562c72b3a6dffd92bc2316bbbd404296f805f24983c6802ec450cd5. Runtime remains the accepted 3a58b29457eefa4fc02226db07c3589db82e381fad680516cb6500882175ca4c. The revised targeted test file has SHA256 c0b215073dd92a8f7355c0657e7b25e8beedfbc2c28f1d23b464a35f3aea1174. Independently reran all 9 targeted tests, which passed.

Read both added files. The workflow is manual-only, uses contents read permission, checks out the approved main SHA, and supplies only GITHUB_TOKEN plus the approved SHA. The probe reads protected configuration, validates its controller identity, and runs the existing RevisionGuard. That makes exactly two fresh GET requests for repository identity and main ref, then prints the same numeric diagnostics even on failure. It loads no ledger keys or App private key and performs no writes. The existing approved dependency lock and binary-only installation remain in use. It can measure remaining quota before a full evaluation, with a small cost from checkout and its own two GETs.
