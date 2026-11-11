# Idle activation of the accepted v1.3 runtime

This isolated preparation applies the independently accepted v1.3 source bundle
to controller `bc56dd5efa51eaefc3007044c59ba1d063ec8aa8`, with the separately
reviewed idle configuration. It preserves every baseline path and all 20 input
mappings. The 19 historical files remain byte-identical. No source code differs
from the accepted integration bundle, whose manifest is
`a7a880139ca8b146d7d64f6dea64da73f940638fb92fdd3afff9c3fcc954de4a`.

`tree/` contains the complete 153-file candidate. `ACTIVATION.json` binds every
file and lists the 16 changed or added paths relative to the deployed refresh
controller. The owner README and `.gitattributes` are retained, although the
curated integration bundle did not include them. The bundle manifest now records
the actual protected inputs and all preserved files. The actual combined
integration review is included alongside its component reviews.

The only configuration change is `jobs=[]`, using the already reviewed SHA256
`00c3118bc4bd74dd0871e297c9ab2d733f2185aeb24d44f0abe6ef397d5b2c97`.
An actual intervening idle-controller commit does not exist in this preparation;
if root creates one, verify its complete delta from `bc56dd5` is exactly those
idle config bytes before applying this candidate. The future activation commit
is also unknown. Neither value is fabricated.

Deploy only after both exact v1.2 normal merges and their immutable readbacks
succeed, and after independent review of this complete candidate. Root then
reviews the staged diff, commits and pushes through the normal process, reads
back remote main, and approves that exact revision. An actual dispatched idle
evaluation must return `[]` under the revision guard. No closed v1.2 job should
be activated again.

The 22 existing idle and protected-profile tests pass on this prepared tree
with the pinned CPython 3.12 interpreter. The earlier 642-test accepted integration
run remains applicable to identical code bytes; it was not repeated or relabeled
as a new run here.

This activation installs capability. It does not itself adopt repository
documentation or certify a mathematical release. The user's current direction
is a combined Version 14 and v1.3 documentation update. No standalone six-doc PR
is prepared. The following combined release still needs actual base/head/PR
identities, the full substantive source-use and reconciliation dossier, its
reviewed inline profile, independently authored final decisions, authenticated
ingress and actual successful checks. The existing non-substantive documentation
builder cannot be used to bypass those substantive requirements.

`prepare.py` reads immutable Git objects and the accepted local artifacts. It
writes only this directory, accesses no credentials, and performs no deployment.
