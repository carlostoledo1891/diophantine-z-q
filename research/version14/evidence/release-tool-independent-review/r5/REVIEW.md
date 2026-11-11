# Independent R5 research-annex tooling review

Reviewer `/root/sol_protocol_final_review`. Author `/root`. November 7, 2026.

Accepted as preparation tooling at `quartic-v14-release-r5/MANIFEST.json` SHA-256 `e06b81223c6e2cedbcff78cc65cbddf07d1930e75342ecbb147f8abc402d7028`. I verified every listed file hash and length, read the full annex builder and package delta, and confirmed that the other accepted R4 core executable files are unchanged.

The annex keeps a manifest row for each logical path, with content digest, size, category and status, and a separate unavailable-items record. Contents are stored once per digest. A hash reused with a conflicting size is rejected. The archive must contain exactly its manifest and the expected content-addressed members. Validation requires regular unencrypted files, bounded manifest size, at most20000 logical rows, at most128MiB per unique content and at most2GiB total unique content. Every content is streamed, length-checked and SHA-256-checked. Cross-chunk private-key markers are checked. Paths reject unsafe traversal and designated credential/transcript/runtime locations. Source files must resolve within the selected workspace and match their exact pins.

The cumulative packager adds only the exact `research/version14/z-in-q-version14-research-annex.zip` exception, requires that path in the selection, and calls the annex validator before packaging. Arbitrary other ZIP files remain rejected. Restoration treats this annex as opaque data; it neither executes nor automatically expands its research content. The existing layered archive and replay logic remains unchanged.

All29 inherited/new tests passed independently under pinned CPython3.12.14 in23.869 seconds, including the actual PDF selection regression. Five additional reviewer-written negative controls passed for member size, total size, inconsistent deduplication size, content-hash mismatch and symlink archive entries. No actual annex selection or publication was created or accepted by these tests.

The structural filters cannot establish privacy suitability or complete historical research coverage. In particular the logical path labels, categories, status text and unavailable records require actual selection review; their inclusion in a manifest does not make them true. The intended space savings have not been measured on an accepted actual selection in this review. An actual frozen source map, manifest, built archive and its inclusion in the final cumulative handoff require separate exact-byte review.

No defect requiring a tooling change was found within this scope. No frozen author file, repository or remote was changed during the review.
