# Version 14 maintenance revision 5

This proposal adds one explicitly named research annex to the reviewed R4
cumulative handoff. R4's manuscript, CI, rendering, mirror and restoration code
is unchanged. The modified packager requires and validates
`research/version14/z-in-q-version14-research-annex.zip`; arbitrary ZIP files
remain rejected.

The annex stores each distinct content hash once and keeps a logical path,
size, category and historical status for every source occurrence. It never
executes or automatically extracts the annex. The ordinary cumulative handoff
restores the current repository files, including the annex as an opaque file;
the annex's own manifest identifies the additional research history.

The builder takes two separately hash-pinned inputs: a reviewed manifest and
an explicit content-hash to workspace-relative source map. It rejects changed
source bytes, paths escaping the workspace, nested archives, PDFs and known
credential/transcript locations. Its validator checks exact membership,
regular-file types, sizes, all content digests, duplicate JSON fields, and
private-key markers. These structural checks do not prove that a source is
appropriate for publication or that all research history was selected. The
actual selection still requires independent scope and privacy review.

The annex is intended to preserve additional history without adding thousands
of individual files to the live repository and its protocol-check inputs.
Current mathematical proof sources, coverage records, contracts, reviews and
reproducibility artifacts remain separately addressable and reviewed.

Root authored this revision. All 29 inherited/new tests passed using the pinned
Python 3.12 runtime, including the actual 309-page PDF selection regression.
The first run exposed a missing copied R3 test fixture; the fixture was restored
byte for byte before the successful run. No actual annex has been created and
no publication or independent acceptance is claimed.


## R7 historical scanner literals

The default credential-marker rejection remains. Five historical utility files
are accepted only at the exact destination paths, SHA-256 values and sizes in
the separately reviewed, digest-pinned `reviewed-literal-files.json`. Their two
marker strings are scanner tests, not credentials. A changed byte, appended key,
unlisted path, or changed allowlist still fails. No source byte is rewritten.
This exception does not apply to arbitrary Python or patch files.
