# GitHub App transport

This is the real HTTP transport for `app_publisher.TrustedAppTransport`, plus the `get(path)` interface used by the existing live GitHub reader. It is an author implementation awaiting independent review. The tests make no live API calls and load no deployed key.

The isolated controller constructs it as follows, with values obtained only from protected controller configuration:

```python
from github_app_transport import GitHubAppTransport, TransportConfig, RS256Signer

transport = GitHubAppTransport(
    TransportConfig(installation_id=installation_id, repository_id=repository_id),
    RS256Signer.from_pem(trusted_pem_bytes),
)
```

There is no environment or filesystem key lookup in this module. The controller owns that boundary. `from_pem` accepts bytes, requires an RSA private key of2048 through8192 bits, and uses `cryptography` for PKCS#1 v1.5/SHA256 signatures. The tested installed dependency is `cryptography==50.0.2`; deployment dependency installation and pinning belong to the controller workflow.

App ID5663093 and slug `elliot-research-review-gate` are fixed. The only allowed repository identities are1446122118, `elliotglazer/diophantine-z-q`, and1447509909, `elliotglazer/private-diophantine`. A transport instance selects exactly one of them for all repository reads and check operations. Each installation token is explicitly limited to these two IDs. The separate controller repository1449903511 is excluded.

The requested and returned token permissions must be exactly `checks:write`, `contents:read`, `pull_requests:read`, `actions:read` and `metadata:read`. The live reader needs Actions access for its workflow/run/job checks. Token creation first authenticates the JWT through `GET /app` and verifies the configured installation's App identity and suspension state. It then checks the minted token's exact repository ID/name list, permission map and expiry. GitHub installation tokens last at most about one hour; this implementation discards its cached token after five minutes, with a further sixty-second expiry margin. Discarding a cached token does not revoke its server-side lifetime. No token is exported or logged.

The JWT uses the fixed App ID as issuer, issue time sixty seconds before the controller clock, and expiry eight minutes after it. The HTTP implementation connects directly to `api.github.com` with the default verified TLS context. It does not read proxy settings, follow redirects, retry mutations or include response bodies in exceptions. JSON responses are limited to16 MiB and reject duplicate keys and non-finite numbers. Each instance has a5000-request limit. Inventories have at most100 pages of100 rows and reject duplicate IDs, changed totals, inconsistent pagination or an exhausted bound. Pagination URLs from responses are never followed; the code constructs each fixed-origin page itself.

`get` permits GET requests only within the selected, fixed repository prefix. It rejects absolute URLs, path traversal including repeated percent encoding, fragments, backslashes and control characters. It returns the same JSON/Link-header pair expected by `github_read_context.API`. That existing reader still performs its own resource-specific identity and source-pin validation.

`open_contexts` enumerates all open PRs rather than filtering by branch name. It retains every PR sharing the requested head, including drafts and other base branches. For each it verifies the target repository, current base branch ref, current pull head/merge refs, exact commit/tree IDs and ordered merge parents `[base,head]`. Draft or unmergeable contexts are marked unready. Missing merge context blocks rather than inventing a placeholder. A second complete open-PR enumeration must match the first. The publisher independently repeats its freshness checks before publication.

The only repository mutation routes are POST to the selected repository's check-runs endpoint and PATCH to a positive check ID there. Payloads require the exact configured check name and publisher generation format. They prohibit arbitrary extra fields such as actions or details URLs. Before update, the transport reads the check and verifies the same App ID and name. Both create and update revalidate authenticated identity and verify the returned App/name/head identity. The publisher additionally checks the intended status, conclusion, external generation and durable-generation barriers. This transport cannot turn a saved success JSON into a live evaluation.

Run the offline suite from this directory:

```text
python -B -m unittest test_github_app_transport -v
```

The34 tests cover JWT signature/claims using an ephemeral synthetic RSA key, identity and permission failures, token scope and lifetime, hostile paths and routes, own-check mutations, payload restrictions, pagination, PR ambiguity, refs/merge parents, secret-safe errors and HTTPS redirect/size rejection. Passing mocks establishes these implementation checks; it does not establish deployed permissions, successful App provisioning, ruleset fallback behavior or production activation.

The API contract was checked against GitHub's official documentation for [installation access tokens](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app), [JWT authentication](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-json-web-token-jwt-for-a-github-app), [check runs](https://docs.github.com/en/rest/checks/runs?apiVersion=2022-11-28), and [pull requests](https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28). Runtime requests explicitly select REST API version2022-11-28.
