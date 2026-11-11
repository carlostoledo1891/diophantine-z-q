# Finite reproduction

Use Python3 with its standard library. The selected checkers do not need third-party mathematical packages. Run without bytecode output.

From this repository:

`python -B quartics/quartic-299-314/verify_artifacts.py`

This verifies full299/314 sum-of-squares expansion, compact coordinate maps, decimal text, counts and coefficient bounds. The existing deeper lineage entry point is:

`python -B quartics/quartic-299-314/verify_lineage.py`

For233, make a temporary copy of the four directories reference233-sparse-015, reference233-014, reference235-sparse-012 and reference235-011, preserving their paths under work/quartic238-optimization-20261110/linear-lucas relative to a temporary root. Run:

`python -B work/quartic238-optimization-20261110/linear-lucas/reference233-sparse-015/verify.py`

The original checker writes INVERSE-MAPS.json and VERIFICATION.json, so use the temporary copy and compare its outputs against the staged originals. It checks the full reverse207-row map, affine inverses, full polynomial expansion and coefficient profile. Do not execute build.py as a substitute for verification.

Reproduction receipts describe finite algebra only. They do not prove the arithmetic input or certify an effective definingN. Full lineage replay and independent review of the final portable package remain tracked in G07.

## Original huge-polynomial expression

Use Python >=3.11 and Node.js >=22 on PATH. From this repository root run `python scripts/check_construction.py --report build/construction-checks.json`. See [scope and exclusions](construction/V15-SCOPE.md). The precision polynomial is a pinned input boundary; this command does not prove the arithmetic theorem.
