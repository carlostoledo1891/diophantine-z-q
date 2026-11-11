# Version 13: 394 and 411 variables

The [November 7, 2026 manuscript](../../../manuscripts/quartic_v13.pdf) and its [TeX source](../../../manuscripts/quartic_v13.tex) retain the earlier constructions and add the reductions from the Version 12 baseline. The subtitle is `Version 13`, without a trailing period.

| Construction | Total variables | Witnesses | Quadratic residuals | Quartic monomials | Coefficient magnitude |
| --- | ---: | ---: | ---: | ---: | --- |
| Symbolic coefficients | 394 | 393 | 364 | 6,338 | Maximum $16\cdot3^{2^{26}}$ |
| Decimal coefficients | 411 | 410 | 381 | 6,388 | Less than $2^{3247}$ |

Both polynomials have integer content one. The symbolic table uses the fixed integer $C=3^{2^{25}}$, which is not another variable. The ordinary text table contains every coefficient in decimal and occupies 214,957 bytes. The [artifact manifest](../../../quartics/quartic-394-411/ARTIFACTS.json) records the exact maximum coefficient without requiring its digits to be reproduced here.

## Tables and finite verification

- [394-variable JSON table](../../../quartics/quartic-394-symbolic-coefficients.json) and [text table](../../../quartics/quartic-394-symbolic-coefficients.txt)
- [411-variable decimal table](../../../quartics/quartic-411-fully-expanded.txt)
- [Portable package and reproduction instructions](../../../quartics/quartic-394-411/README.md)
- [Complete package manifest](../../../quartics/quartic-394-411/PACKAGE-MANIFEST.json) and [source manifest](../../../quartics/quartic-394-411/SOURCE-MANIFEST.json)

All compact coordinates run from 1 through the total variable count, with `x1` as the input. The ordinary companion adds sixteen repeated-squaring coordinates and the product coordinate `t=C*tau`. That last coordinate keeps the rescaled anchor quadratic; replacing the fixed constant by a variable without it would not preserve the quartic construction.

Run from the repository root:

```sh
python -B scripts/check_quartic394_portable.py
python -B docs/manuscript-revisions/version13/validate-applications.py --repo . --self-test
python -B scripts/check_audit_history.py --self-test
```

The finite replay uses Python's standard library. It verifies the frozen packet before and after 27 source and certificate stages, expands both complete sums of squares, checks the compact coordinate maps, and compares the three public downloads. Its receipt is written to `build/quartic-394/verification.json`. It does not change the frozen package.

## Mathematical review and inherited scope

The new argument includes rational logarithm evaluation, mixed detector orders, shared polynomial circuits, reciprocal and identity-inclusive charts, the enlarged auxiliary H domain, deterministic scalar correction, simultaneous real and finite-place preparation, pole normalization and anchor rescaling. The [final mathematical composition review](../../../quartics/quartic-394-411/reviews/mathematical-review.md) and [separate artifact review](../../../quartics/quartic-394-411/reviews/artifact-review.md) bind the exact results. [ACCEPTANCE.json](../../../quartics/quartic-394-411/ACCEPTANCE.json) identifies their files and scopes. These are internal model reviews, not independent human peer review or a completed formal proof.

The composition review checks the new implications and the objects they consume, including zero branches, local places, nonzero denominators and the order of the completeness choices. Its acceptance retains the earlier arithmetic inputs. It does not re-prove every restricted-converse, height or prime-pattern theorem, and it does not remove the literature-version and errata qualifications in the inherited inventories. The [Version 12 guide](../version12/README.md), [Version 11 Kato repair](../version11/README.md) and [audit protocol](../../audit-history/PROTOCOL.md) retain those records.

The [39-application inventory](APPLICATIONS.json) records 351 explicit obligations and the relevant source, construction and consumer passages. Its [own README](README.md) explains the provenance and structural checks. The inventory is an author record; its successful validation does not create independent approval. The [current audit register](../../audit-history/current.json) and [new quartic application contract](quartic-application.json) bind the assembled manuscript and its required independent acceptances. Historical component approvals alone do not approve a changed exposition.

## Manuscript and research handoff

See the [build instructions](../../building.md) for the pinned compiler and manual PDF review. The manual workflow renders pages 1 and 276–288 and checks a total of 296 pages. The [Version 13 supplement guide](../../../research/version13/README.md) identifies the research archive assembled from the final checked state. The Version 12 tables, earlier manuscripts and previous supplements remain available under their existing paths.
