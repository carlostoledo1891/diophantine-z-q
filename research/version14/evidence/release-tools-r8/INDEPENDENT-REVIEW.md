# Independent R8 maintenance tooling review

Accepted for the exact lexical-only successor at MANIFEST SHA-256 0787681b0124f2d138e985461cc7a2b62b66b04f0ac531189e17065af4906f68.

Reviewer /root/sol_protocol_final_review. Author /root/astra_v14_assertions_arithmetic.

All 43 manifest members matched recorded bytes and hashes. Compared with R7, the only changed inherited implementation/test files are research_annex.py and test_research_annex.py. Three byte literals are split into constant-folded concatenations. Recursive compiled code fields match under pinned CPython 3.12, including bytecode, constants, names, variables, closures, argument counts, flags, stack size and exception tables. Source positions change.

The actual private-key marker values, scanning behavior and rejection tests are retained. package_v14.py and reviewed-literal-files.json match R7 byte for byte. The exact five historical exceptions remain unchanged.

All 37 tests passed independently in 26.183 seconds, including the actual 309-page PDF selection regression. The PDF test validates page selection and does not claim visual inspection. Prior R7 review and all source artifacts remain unchanged. No production or candidate files were edited.
