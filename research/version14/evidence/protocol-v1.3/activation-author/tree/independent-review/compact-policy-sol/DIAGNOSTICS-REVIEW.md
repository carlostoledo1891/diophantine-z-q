# Private diagnostics review

Accepted app_publisher.py SHA256 a13b02558ad3ad769a2c10f8889519990dc89274736b8bed937face776fa0c97 and test_publisher.py SHA256 7bd1368e64a94ff36dd2b4dd305fd814b0779b45d3356062a1b693e5cdbb671c. Reviewer /root/sol_protocol_policy_review. Compared current source with the deployed repository copy and read the full added helper and return-field change.

The delta adds a failure_location helper and a diagnostic field to the private controller result. It records only the exception class name and last twelve traceback code locations as basename, function and line number. It does not inspect exception messages, arguments, locals or source lines. Both slash conventions are stripped from filenames. The code executes only protected controller/library modules under the existing no-candidate-execution boundary.

All prior success barriers, revocation attempts, status choices and public App summaries remain unchanged. Diagnostic generation follows the existing revocation attempt and cannot authorize success. The pre-existing reason handling is unchanged.

Independently ran 36 publisher tests and 4 live integration tests. All passed, including the secret-sentinel test. An additional reviewer-owned depth-30 exception exercise confirmed exactly twelve retained frames, expected field names, absent directory separators and no exception-value sentinel. Logs are diagnostics-tests.log. No live calls or source edits were performed.

This acceptance covers private code-location diagnostics. It does not establish the cause of the current live blocked result before that result is observed with the new instrumentation.
