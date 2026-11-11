# Version 14 maintenance revision 3

This preserves revision 2 and adds one mirror guard: an existing path may not change its Git mode or object type. A new independent regression constructs a 100755-to-100644 transition and requires rejection. All other executable bytes are unchanged from revision 2. The source/archive linear-commit support and mandatory protocol/coverage selection remain.

Author of this correction: /root. Independent acceptance is pending. The original revision 2 README and 13-test output are preserved with R2 prefixes. The new test run executed all 14 tests successfully; TEST-RESULT.json records the actual operator-observed run, not a copied compiler transcript. No repository or remote was changed.
