# Bounded attribute review

Reviewer: `/root/astra_v14_baseline_compiler`, operator-local identifier. Attribute author: `/root`. I did not author the reviewed five-rule addition. I do author the surrounding R5 installation proposal, so this review does not independently accept that proposal or its catalog.

Accepted within the byte-preservation scope below. The exact target `.gitattributes` SHA-256 is `bf7529b55e1c929df6633f13f706674a5ee7419e22e9c89dea399a418417db8b`. Removing the exact comment and five added rules reproduces the R4 target SHA-256 `1267a27daab7298e2f962f3947b534725b3c757180d015b345eeb47523155bff`.

The five rules unset Git's text conversion for `AGENTS.md`, `README.md`, `CONTRIBUTING.md`, `.github/pull_request_template.md` and `docs/research-review/**`. Existing source/evidence rules remain unchanged. These rules preserve bytes; they do not alter the protected controller's policy paths or reviewer requirements.

The previously observed `AGENTS.md` raw blob was `f8c28ed337bb73603526c152d3d09c0cbd7e6778`, while Git's clean conversion produced `884b18e158b2e5f9e3eccc4e346b148793b09bda`. After the addition both are the former value. I ran `git check-attr text` and `git hash-object --path ... --stdin` for all eight adoption targets and compared each result with the independently calculated raw Git blob hash. All eight have text conversion unset and identical raw/clean hashes. Their SHA-256 values still match the accepted initial or successor documentation targets. The whole current snapshot was also rechecked and has no raw/clean mismatch.

`ATTRIBUTE-CHECKS.json` records the exact added text, source/target hashes and every checked path/result. This review accepts that exact addition for preserving those reviewed bytes. It does not accept a future commit, file mode, archive restore, controller deployment or mathematical assertion. Changed attributes or documentation bytes require a new check.
