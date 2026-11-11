# Review of direct-history scanner-literal flags

Reviewer `/root/sol_protocol_final_review`. November 7, 2026.

## Finding and disposition

The five flagged paths in direct-history-install/INSTALLATION.json contain reviewed scanner literals, not private-key blocks. I checked their exact hashes and byte counts, read the containing source/patch statements and searched for standalone PEM headers and closing private-key delimiters. Each contains exactly two BEGIN marker strings inside byte-string membership tests. No standalone header, closing delimiter or encoded key body was found in these files.

The exact five destination/hash/length pairs are recorded in REVIEWED-LITERAL-FILES.json. They have three distinct content hashes.

- Historical stage_bundle.py `191cd76f17740153c958fb41d87a05a1a670a6d67dbfa8a383b72bc0d3e01a9b`
- Two copies of R1-TO-R2.patch `c1a96b8711f149ebc219bd98c4805cad880b58fa3fb686cb19e9e75c30092a61`
- Two copies of package_v14.py `cfe43081de32a5036a0c929be0c2981831fc4751df7ab448f2ab80fa5758cc1b`

I approve preserving these exact historical bytes as data within the direct release evidence, subject to a separately reviewed packager repair. No current rule is bypassed by this report and no source bytes were changed.

## Narrow repair recommendation

Use a versioned exact destination-path plus whole-file SHA-256 exception map for these five reviewed files, with byte lengths as an additional check. Keep the blanket marker rejection for every other path and for any changed bytes. The exception map itself must be fixed in the reviewed tool or bound to an independently reviewed fixed digest. An arbitrary caller-supplied allowlist must not grant itself an exemption.

Do not exempt Python files, patch files or quoted marker strings generally. Do not remove the marker checks or attempt to infer safety merely because a marker appears in quotes. The exact known bytes contain no key, so a real key inserted into one changes its digest and loses the exception. All other path, source-hash, archive, transcript and credential restrictions remain required.

Required negative tests should cover an appended real key block at an allowed path, another one-byte change at an allowed path, an allowed hash at an unlisted destination, and an ordinary real-key file. All must fail. Positive tests should preserve all five exact files, including duplicate-content copies, without changing their hashes.

## Overall selection limits

INSTALLATION.json records1107 already-exact items and476 newly installed exact items. Five additional files are awaiting this literal-content handling. Two title metadata destinations and one changed deployment-status source remain explicitly pending. This focused review does not accept the complete direct-history selection, final Version14 coverage, current registry or deployment records. The title metadata has a separate narrow review, and its final reconciliation must remain explicit. The direct packet's privacy/completeness and current final bindings still require their dedicated final review.

No packager, source file, exclusion record, repository or remote was changed in this task.
