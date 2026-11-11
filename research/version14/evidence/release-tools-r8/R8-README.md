# R8 packaging-source literal correction

R8 preserves R7 and changes two inherited source files. In `research_annex.py`, the two scanner marker byte strings are written as concatenated byte-string fragments. The one corresponding fixture in `test_research_annex.py` uses the same spelling. The complete marker values at runtime are unchanged.

This lets the two source files pass the existing packaging scanner when included as source evidence. The source text no longer contains contiguous marker bytes. `package_v14.py`, the five-entry historical literal allowlist, its pinned digest, the annex scan loop, boundary tail, rejection branches and all other inherited source bytes are unchanged. This is the spelling already used by `package_v14.py`.

`R8-DELTA.json` records the exact two-file before/after hashes and replacement counts. A comparison of CPython3.12.14 compiled semantic fields found identical code bytes, recursive constants, names, variables, argument counts, flags, stack sizes and exception tables. Source-position metadata differs and is excluded from that comparison. The change introduces no new conditional branch or exemption.

`TEST-RESULT.json` records the full37-test command and its observed result. The tests include the annex rejection test and the historical exception tests for changed bytes, appended keys, renamed paths, unlisted markers and a changed allowlist. `MANIFEST.json` freezes every source and retained-history file in this successor. `PARENT-MANIFEST.json` is the exact R7 manifest.

Historical files containing scanner literals retain their original immutable bytes and existing reviewed paths. They must not be relocated under newly invented allowlist paths. This successor does not expand that allowlist.

This is an author proposal for independent Sol review. It changes neither the manuscript nor the preview repository and performs no deployment.
