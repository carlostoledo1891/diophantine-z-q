# Completed check reuse review

Decision accepted. Reviewer /root/sol_protocol_policy_review independently compared the root-authored changes with the deployed repository copy. Accepted app_publisher.py SHA256 is 99626b402c0378b2574385684051e4bed0f2b874fc481d427dedc6c25ee7115d. Accepted test_publisher.py SHA256 is f1db36a93b1a8898db7d723de7595a8106452854dabdf263881d8850939b1677.

The patch changes only the initial status of a reused check and whether a pending failure path can keep an existing check in progress. Reused checks receive completed/failure while the fresh evaluation runs. A newly created check still starts in progress. The allow_pending path keeps a check in progress only when it is not completed and has no conclusion. Successful publication still goes through the unchanged identity, current generation, durable before_success, full live recheck, response confirmation and post-write recheck logic. No new check is created when the matching owned check already exists.

Independently ran 35 publisher tests and 4 full live-integration tests. All passed, including the negative control that rejects reopening a completed check, late-comment and operator-append rejection, stale generations, changed identity and missing receipts.

An additional reviewer-owned exercise verified the complete sequence. A first pending evaluation leaves its new check in progress. A successful next evaluation reuses that exact check ID and exposes completed/failure throughout the validation callback before publishing success. A later pending evaluation retains completed/failure. publisher-reuse-independent.json binds these results and source hashes. No GitHub calls or source edits were made by this reviewer.

The live API diagnosis is supplied by the orchestrator. This review establishes that the proposed status handling avoids reopening a completed check while retaining the prior publication safeguards. It does not assert that a subsequent live run has succeeded.
