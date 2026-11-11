# Version 14 release tools, revision 4

This isolated successor fixes the renderer invocation produced by revision 3.
That invocation selected `--edition v14`, but the repository renderer accepted
only editions through v13. `prepare_ci.py` now emits the updated
`scripts/render_quartic_review.py` alongside the paper builder and two workflows.
Its CI preparation manifest binds all four emitted files.

The renderer accepts `--edition v14`. With that edition and no explicit PDF, it
uses `manuscripts/quartic_v14.pdf`. Its automatic selection finds the unique body
heading `A quartic presentation with 299 variables` and selects through the
following References page, plus the first four pages. Missing or repeated
headings and missing reference boundaries fail. The default edition remains
v13, and every v5-v13 route and default path is unchanged.

The original `paper()` and `workflow()` functions are unchanged. All other R3
Python tools and tests are byte-identical copies. The complete R3 top-level
files, including its manifest, README, test result and original CI preparer,
are preserved under `history/r3/`. R3 preview files and repositories remain
untouched. The predecessor manifest SHA256 is
`b23f11f00cbb8a549a12d845e0ab396dd392ba16585167a3267d4263a46ba989`.

`ci-preview-001/` contains the actual generated four-file delta from public base
`2125274b93314c9a9e51c7b47559025489565632`, with date November 7, 2026 and render
selection `1,289-301`, expected page count 309. This is local preparation, not a
deployed workflow or a new source-policy approval. The renderer's changed hash
must be included in the reviewed CI source transition.

The new regression invokes the real generated parser and `main()` against the
final 309-page PDF at
`work/quartic-v14-release/preview-repository/build/paper/quartic_v14.pdf`, SHA256
`bebcfc92b11ee45c3302716859214b9feefab86480d941995b37eaa05d7a0ca5`.
It runs explicit `--edition v14 --pages 1,289-301 --select-only` and verifies
exactly those pages, then tests the default v14 PDF path and automatic heading
selection. It also checks historical automatic routes, missing/ambiguous
headings, missing reference boundary, source markers and unchanged R3 functions.

The test uses the renderer's existing `--pypdf` option. Its subprocess wrapper
suppresses pypdf's optional-font warnings only inside the test. No logging or
extraction behavior is changed in the renderer. The first local attempt used
PATH's uninitialized MiKTeX `pdftotext` and failed before extraction; that was an
environment error. The supported pypdf route succeeds. Page selection is not
visual inspection; the emitted reports retain `visual_inspection=PENDING`.

Run the complete suite with the reviewed Python interpreter:

```powershell
<reviewed-python> -B -m unittest discover -s work/quartic-v14-release-r4 -p test_*.py -v
```

Independent review must bind this R4 tool set and the emitted renderer before
root integrates it. This preparation makes no repository, preview or remote
change and creates no mathematical acceptance.
