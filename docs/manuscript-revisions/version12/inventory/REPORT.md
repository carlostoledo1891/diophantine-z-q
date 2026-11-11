# Portable Version 12 application inventory

`APPLICATIONS.json` contains the 25 application and consumer records for the frozen Version 12 addition. Its SHA-256 is `9e63180a33da914e5179ebf5296a287cbb8bbd7007f5e5cc3aaac5d0844be863`.

All active file bindings use repository-relative paths. The addition binds to `docs/manuscript-revisions/version12/addition.tex`; the baseline binds to `manuscripts/quartic_v11.tex`; the final residual and coefficient files bind under `quartics/quartic-498-514/`. Their content hashes are unchanged.

`AUTHOR-APPLICATIONS.json` is a byte-for-byte archive of the original author inventory, including its historical absolute paths. Its SHA-256 is `3e89a24d3027749c9f22c5dcda640747de473bb4d499e19d4181bff43b81cda4`. Neither that original file nor the frozen TeX was modified.

The portable record preserves all 25 IDs, all 225 obligation texts, all source labels and line numbers, and all consumer labels and line numbers. External publications retain their bibliography, exact file hashes, byte counts, filenames, and version qualifications. Their private workspace locators are replaced by references to exact records in the repository's existing `docs/theorem-application-audit/sources.json`. The inventory does not claim that those external PDF bytes are distributed in the repository.

`transform.py` reproduces the portable record from the unchanged original inventory one directory above this packet. `validate.py` is a standalone structural validator; it imports no transformer. Run it from any directory:

```text
python -B validate.py --repo /path/to/repository --self-test --report VALIDATION.json
```

The validator passed against the public repository. It checked 25 records, 225 nonempty obligation fields, 117 file-pin occurrences, 100 exact label/line bindings, eight source-catalog record pins, 35 unique new labels, and all 40 references in the addition. With the archived author record present, it also checks that all obligation prose, kinds, and consumer bindings are unchanged. Seven negative controls rejected a missing record, missing obligation, absolute path, stale addition hash, stale consumer line, stale source-record hash, and changed external file pin.

`VALIDATION.json` records those results. These are structural checks, not an independent mathematical review or acceptance record. No reviewer approval, contract, `current.json` entry, or manuscript edit was created.
