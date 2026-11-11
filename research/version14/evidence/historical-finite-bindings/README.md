# Historical finite checks

This package contains author-side finite checks for the historical F8, 4973 and962 constructions. The reports are not independent approvals and do not establish the arithmetic input-projection theorems.

Run from the repository root with Python3 and Node:

```text
python -B research/version14/evidence/historical-finite-bindings/recheck_f8.py --package research/version14/evidence/historical-finite-bindings/f8 --repo .
python -B research/version14/evidence/historical-finite-bindings/recheck_4973.py --repo .
node research/version14/evidence/historical-finite-bindings/recheck_962.js .
```

These commands write no report by default. The Python commands accept `--report PATH`; the Node command accepts a report path after the repository argument. Use an external writable path to preserve this package. Run Python without `-O`; assertions are part of the check. No nonstandard libraries or network access are needed.

The14-file F8 closure contains the independent recursive instantiator, canonical serialization module, six literal construction modules, descriptors,15107-row archive, construction certificate and complete coefficient table. It checks15672 variables, degree8,129497 monomials and maximum coefficient685783949153203534233601. The six module bytes are also compared with `degree8-original/modules` in this repository. The archived producer and broader historical `check.py --rebuild --code-audits` command are not included or claimed to be rerun. The older manuscript path `degree8-original/build.py` names that historical producer; this package supplies the narrower exact finite replay at the path above.

The4973 wrapper calls the packaged independent checker with report writing disabled. It checks the selected source,551 transformations,4552 residuals and72925 monomials in4973 coordinates.4552 is an equation count, not another polynomial's variable count.

The962 wrapper checks904 actual gate identities,894 certificate operations,919 residuals and55409 monomials. The fixed coefficient S=3^(2^27) is not a coordinate. The checker retains127 quotient-domain obligations for the source proof. Exact gate identities do not prove those denominator domains. The wrapper records artifact paths relative to the repository without altering their hashes or mathematical results.

`PROVENANCE.json` identifies the exact original file locations and hashes used for the F8 closure and preserves the broader historical verification report and receipt hashes as provenance only. `INSTALLATION-MANIFEST.json` lists every installed input, wrapper and result. The current manuscript separately supplies arithmetic interpretation and rational witness-map arguments; their inherited qualifications remain.
