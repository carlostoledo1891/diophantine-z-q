# Version 12: 498 and 514 variables

The [manuscript](../../../manuscripts/quartic_v12.pdf) and [TeX](../../../manuscripts/quartic_v12.tex) retain the original large polynomial and add a complete section proving the new quartic reductions from the 523-variable baseline.

| Construction | Total variables | Witnesses | Quadratic residuals | Quartic monomials | Largest absolute coefficient |
| --- | ---: | ---: | ---: | ---: | --- |
| Symbolic coefficients | 498 | 497 | 467 | 24,669 | $16\cdot3^{2^{26}}$ |
| Decimal coefficients | 514 | 513 | 483 | 24,716 | $3^{2048}+1005072314676622<2^{3247}$ |

Both sparse polynomials have content one. The fixed constant in the symbolic table is $C=3^{2^{25}}$. It is not an extra variable. The decimal table occupies 690,922 bytes.

## Reproduce the finite construction

- [498-variable JSON table](../../../quartics/quartic-498-symbolic-coefficients.json) and [text table](../../../quartics/quartic-498-symbolic-coefficients.txt)
- [514-variable decimal table](../../../quartics/quartic-514-fully-expanded.txt)
- [Portable source and certificate package](../../../quartics/quartic-498-514/), with its [manifest](../../../quartics/quartic-498-514/MANIFEST.json)

Run from the repository root:

```sh
python -B scripts/check_quartic498.py
python -B scripts/check_audit_history.py --self-test
python -B docs/manuscript-revisions/version12/inventory/validate.py --repo . --self-test
```

The first command requires Node as well as standard-library Python. It reconstructs the mixed source, replays each selected transformation, expands the sum of squares and compares both published tables. Generated work remains under the package's ignored `build/` and `work/` locations. The manifest lists the immutable inputs; the package also contains a few pinned files under `work/`.

## Mathematical review

The selected chain uses mixed orders 12/40, normalized detector poles, five half-trace guards, a one-coefficient anchor, a shorter scalar norm tree, a scalar reciprocal chart, mixed toric circuits, scalar denominator cancellation and norm-coordinate reuse. The separate order-10 and factored-pole candidates were not used.

The [complete composition review](evidence/composition-review.md) checks soundness and simultaneous completeness, including the exceptional scalar points and the actual formal place. The [integration review](evidence/integration-review.md) checks the full revised manuscript. The [application inventory](inventory/APPLICATIONS.json) identifies 25 uses of published results, inherited lemmas and elementary algebra; its author record remains distinct from independent acceptance.

The exact [quartic application contract](quartic-application.json) and [independent acceptance](quartic-acceptance.json) bind the new mathematical edits to the entire manuscript. The [Kato contract](kato-application.json) and [fresh acceptance](kato-acceptance.json) bind the unchanged Version 11 Kato repair to this edition. The [current register](../../audit-history/current.json) preserves historical dispositions and checks the cumulative revision from Version 10.

These reviews cover the new reductions relative to the retained arithmetic inputs. They do not re-prove the restricted converse, height theorem or prime-pattern theorem, and they do not remove the source-version qualifications recorded in earlier inventories. Finite verification, structural validation, internal model review and a completed formal proof are different claims. No new completed formal proof is claimed.

The [research supplement](../../../research/version12/README.md) preserves these records and the preceding supplements without a conversational transcript.

## Serialization correction

The initial Linux replay exposed platform-dependent line endings in generated intermediate JSON files. The frozen hashes were computed on Windows. The builders and table renderer now explicitly write UTF-8 with CRLF line endings on every platform. The [diagnostic and exact changes](portability/serialization-repair.json) preserve the initial review records. The mathematical data, hash assertions and manuscript are unchanged; the revised package binding received fresh independent review.
