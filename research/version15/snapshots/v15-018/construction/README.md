# Original large construction and checks

This directory preserves the original large polynomial construction from the earlier November 5 manuscript. Its saved expression has one free rational input and 292,890,231,904 rational witness variables. The current [Version 2 manuscript](../quartic_12504.pdf) also gives an [explicit quartic in 12,504 total variables](../quartics/quartic-12504/README.md). The commands below check this original construction, not the quartic package. The large constants and finite products are represented by explicit finite constructors; their monomial expansions are not materialized.

## Run the checks

Use Python 3.11 or later and Node.js 22 or later. No Python or npm packages are required. From the repository root:

```sh
python scripts/check_construction.py --report build/construction-checks.json
```

The command verifies source hashes, copies the inputs into a temporary directory, regenerates the ordinary-integer polynomial, compares its exact bytes with the saved polynomial hash, reruns the syntactic bound calculation, and runs four finite arithmetic suites. Generated working files stay in the temporary directory; the optional report is written to the requested path. The Node processes use a 2 GB heap limit.

The first local run took 8.5 seconds with Node.js 24.22.1 and Python 3.12.14 on Windows. Runtime depends on the machine. The graph-generation step took 1.5 seconds; the division-polynomial cases took 6.1 seconds. Peak process memory was not measured.

## Files to read

| File | Role |
| --- | --- |
| [ordinary-integer-definition.json](ordinary-integer-definition.json) | The complete finite expression specification, about 23 MB. Start with `definitions`, `library.fixedConstants`, and the seven entries in `recipes`. |
| [ordinary-integer-polynomial.js](ordinary-integer-polynomial.js) | Builds the ordinary-value and integer-definition composition and audits its witness blocks. |
| [precision-natural-polynomial.json](precision-natural-polynomial.json) | The pinned five-input natural-number polynomial used as the translation input, about 18 MB. |
| [rational-circuit-translator.js](rational-circuit-translator.js) and [audit-rational-expression.js](audit-rational-expression.js) | Translation into rational point-code constraints and separate checks of source-node evaluation wiring. |
| [finite-polynomial-expressions.js](finite-polynomial-expressions.js) and [variable-shift-polynomial-library.js](variable-shift-polynomial-library.js) | Finite constructors, fixed constants, and ordinary-value coordinate templates. |
| [ordinary-integer-polynomial-size-bounds.json](ordinary-integer-polynomial-size-bounds.json) | Recomputed expression heights, variable count, and symbolic size bounds. |
| [bound-ordinary-integer-polynomial.py](bound-ordinary-integer-polynomial.py) | Computes those syntactic bounds without expanding the large constants. |
| [integer-compiler-spec.txt](integer-compiler-spec.txt), [integer-halting-correctness-proof.txt](integer-halting-correctness-proof.txt), and [z-in-q-polynomial-size-bound-proof.txt](z-in-q-polynomial-size-bound-proof.txt) | Preserved explanatory notes. Read their historical scope statements and the corresponding original-construction sections of the [Version 2 manuscript](../quartic_12504.pdf). |
| [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) | Original archive paths, original and release hashes, and the exact changes made for portability. |

Other JavaScript files are the local module dependencies of these entry points or the finite checkers listed below. Some reusable modules also export functions for older universal-equation workflows. Only the command documented above is supported by this curated input set; the full historical archive contains those other inputs.

## What each check establishes

The [Issue 3 reproducibility note](../docs/audit-history/issue3/README.md) gives every finite case range, the division-polynomial evaluation points, and the exact expression-hash serialization. It also documents the Version 4 quartic's terminal-row digest.

| Check | Checked scope |
| --- | --- |
| Regeneration and structural audit | The saved expression is reproduced exactly from the pinned natural-polynomial input; source-node wiring, rational input conventions, recipe order, private witness blocks, and variable coverage are checked. |
| Syntactic size calculation | The root has expression-height bound 256. It records degree bound `B^2048` and coefficient bound `2^(B^2048)`, using the meanings and estimates in the companion proof. |
| `verify-integer-compiler.js` | Finite binomial-digit, bit, packed-trace, and backend examples: 285 digit cases, 4,096 bit cases, 30,120 packed cases, and 49 backend cases. |
| `verify-division-polynomials.js` | 44 exact examples compared with independent affine arithmetic over Q(sqrt(2)), plus 44 changed-x and 30 changed-y rejection cases. |
| `verify-finite-polynomial-expressions.js` | Expansion identities at small fixture constants and rejection of four malformed constructor bindings. |
| `verify-six-contact.js` | The finite algebraic identities and inequalities listed by that checker. |

These computations do **not** establish that the rational zero projection equals the integers. They do not prove the global height or restricted-converse inputs, the natural precision polynomial's complete machine semantics, or the general equivalence of the alpha/power representation. Small fixtures do not evaluate or replace the actual large fixed constants. The numerical tower bounds in the 11/5 manuscript also use the companion mathematical estimates; the script does not compute the astronomical constants numerically.

The natural precision polynomial is an explicitly pinned input boundary. This check suite regenerates the rational expression from it, not the earlier compilation of that natural polynomial from the precision machine. The earlier machine, compiler stages, and their reviews remain available in the [research handoff](../docs/research-guide.md).

## Portability and provenance

The original ordinary-integer expression in the research archive has SHA-256:

```text
a86790bbf1095d6b1cea9c66067ad8432dd35adc320254eecde21f9f98574714
```

The portable expression in this directory has SHA-256:

```text
4d639d4c44e69ea360d36d4591b8fdc82269d68b9363af0157d1e5c1174c7af6
```

Only three provenance locations differ: the `sourceFile` strings in the `power_value` and `precision` recipes and the key in `sourceHashes`. They now name `precision-natural-polynomial.json` instead of a workstation's absolute path. A full parsed-JSON equality comparison after this normalization passed. No polynomial node, constant, witness address, formula, or mathematical status field changed.

The generator uses the same stable source label. The bound checker pins the portable artifact hash. The generated check report and bound report carry the corresponding new hash. The manifest records these changes and any line-ending normalization; all other selected files preserve their original bytes.

To repeat the historical equality check, first restore `outputs/ordinary-integer-definition.json` from the handoff, then supply that original file:

```sh
python scripts/check_construction.py --historical-polynomial /path/to/restored/outputs/ordinary-integer-definition.json
```

The checker verifies the historical file's original hash, changes only the three documented metadata locations in memory, and compares every parsed field with the portable artifact.

The alpha/power formulas in `integer-diophantine-compiler.js` are attributed there to the AFP `DPRM_Theorem` development, specifically `Alpha_Sequence.alpha_dioph` and `Exponential_Relation.exp_repr`. No AFP source files or other third-party text are bundled in this curated directory. The historical notes and source references remain in the separate archive.
