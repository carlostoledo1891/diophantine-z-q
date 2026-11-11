# Original huge-polynomial distribution proposal

Copy exactly the source/destination pairs in SELECTION.json into a fresh V15 assembly. This proposal does not copy them or change any repository. It preserves the original ordinary-integer expression and its existing supported reproduction package, distinct from the 233-variable family.

The original expression has 292,890,231,904 rational witnesses and one free rational input t. Its portable SHA256 is 4d639d4c44e69ea360d36d4591b8fdc82269d68b9363af0157d1e5c1174c7af6. It is a finite machine specification, not its expanded monomial list. Its own conditional arithmetic status and limitations remain intact.

## Reproduction

Use Python 3.11 or newer and Node.js 22 or newer on PATH. No third-party Python or npm packages are required. From the assembled repository root run:

    python scripts/check_construction.py --report build/construction-checks.json

The unchanged checker verifies every SOURCE_MANIFEST member, works in a temporary directory, regenerates the expression, compares its exact hash, computes syntactic bounds and runs four finite verification suites. It invokes Node with a 2048 MB old-space limit. Keep all manifest members: pruning them would break this supported checker. The smaller thirteen-JavaScript generator closure is recorded separately in SELECTION.json for explanation, not as a replacement for the checked distribution.

The precision-natural-polynomial.json is an exact pinned input boundary. This package reproduces the ordinary-integer expression from that input; it does not regenerate the precision input from earlier machines or prove all arithmetic dependencies. No enormous historical archives are selected.

## Provenance and integration notes

SOURCE_MANIFEST.json records original paths/hashes and the portable release hashes. Historical expression SHA a86790bbf1095d6b1cea9c66067ad8432dd35adc320254eecde21f9f98574714 differs only in three provenance path locations as documented by the existing checker. Do not claim raw historical-byte equality with the portable artifact.

The exact construction/README.md is retained because the checker refers to its scope limitations. It is historical documentation and contains older-version links; it must not be presented as a current V15 completion statement. GI should update current V15 packaging prose after installation/checking rather than rewriting this preserved source document silently.

No construction/SOURCE_MAP.json exists in this selected tree. The manuscript claim naming that companion remains a concrete integration issue: locate an authentic historical map or correct the companion filename/claim through the author. SOURCE_MANIFEST does retain historical references, but this proposal does not invent or rename a map.

Static verification here checked all selected bytes and manifest hashes and traced local CommonJS dependencies. The reproduction command has not been run by this selection task. No new mathematical acceptance, final packaging acceptance, or publication is claimed.
