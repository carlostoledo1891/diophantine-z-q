# Version 13 replay portability correction

The initial Ubuntu CI run stopped at a historical certificate containing a
Windows path with backslashes. The frozen launcher used the host platform's
path rules, so Linux did not redirect that path into the supplied source packet.
The Windows replay had passed. This was a replay portability defect, not a
change to the polynomial, manuscript, or arithmetic argument.

Use the current entry point from the repository root:

```sh
python -B docs/manuscript-revisions/version13/portability/test_portability.py
python -B scripts/check_quartic394_portable.py
```

The new entry point checks the original wrapper's hash and calls its unchanged
`main` function. It substitutes a bootstrap only for the wrapper's one exact
verifier subprocess call. The bootstrap redirects historical paths beneath the
recorded original root to files listed in the source manifest. It rejects
traversal, unlisted destinations and symbolic links in redirected paths, while
preserving real paths already inside the current packet. It restores the open
functions when execution ends, including on failure.

The original wrapper still checks all 400 packet files before and after replay,
requires identical manifest bytes, and compares the three public coefficient
downloads with their packet originals. The frozen verifier still executes all
27 stages. The original wrapper, packet, coefficient tables, TeX, PDF and three
mathematical application contracts remain byte-for-byte unchanged.

The [independent infrastructure review](REVIEW.md) and
[acceptance record](acceptance.json) cover this correction. The mathematical
reviews retain their original scope. CI runs the path tests and full replay on
both Ubuntu and Windows; a local Windows success alone is not evidence that
the Ubuntu run passed.
