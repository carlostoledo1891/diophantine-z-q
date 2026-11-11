# Issue 2: historical justification and manuscript incorporation

The [review](https://github.com/elliotglazer/diophantine-z-q/issues/2) identified real omissions and unclear connections in the printed manuscript. [Version 10](../../../manuscripts/quartic_v10.tex) addresses its nine points. A subsequent comparison with the earlier research record found that the technical edits mostly restored or connected existing arguments. Describing all of them as newly filled mathematical gaps would be inaccurate.

| Point | Earlier evidence and what Version 10 changes | Historical classification |
| --- | --- | --- |
| 1. Mazur | The [earlier corollary audit](evidence/corollaries.md) checked the projection argument and the 1995 formulation. The revision adds the 1992 priority credit and the Conjecture 2 consequence. | Attribution and an additional consequence. |
| 2. Determinant coordinate | The [earlier determinant review](evidence/determinants.md) checked generic rank at a known simple zero, the regularity of the actual functional, and base change without nonunit t-disks. The revision invokes these at the central calibration. | Prior justification; missing connection at the application. |
| 3. Turing versus many-one | The [earlier audit](evidence/corollaries.md) constructed both many-one reductions. The revision separates that claim from OpenAI's prior Turing-completeness result. | Novelty and attribution correction. |
| 4. Kato at two | The [earlier applicability audit](evidence/kato.md) explicitly recorded the stronger abelian-kernel condition and the open commutator image, the away-two statement, and local cohomology comparisons. Version 10 assembles and expands the direct 1999 route in the precise convention used. | Prior inputs; fuller connecting argument and explicit application. Not a claim that every earlier review repeated the entire argument independently. |
| 5. Saved polynomial | The [original multiplication proof](evidence/valuation.md) wrote the conjugated ratios. The [earlier template audit](evidence/templates.md) identified the saved pole square and shared witnesses. The revision consolidates the dispersed mapping into a printed dictionary. | Prior justification; missing manuscript traceability. |
| 6. Valuations | The [November 3 proof](evidence/valuation.md) uses a maximum-valuation argument, not an assertion that every factor in some group is a unit. Its hash matches the [earlier audit's source pin](evidence/valuation-pin.md). The revision prints a shorter contradiction argument. | Prior proof and audit; omitted derivation. |
| 7. OpenAI credit | The [earlier RC audit](evidence/rc-provenance.md) names the frozen upstream sources. The revision supplies local credit and the public preprint/section mapping. | Attribution correction, not a new assumed theorem. |
| 8. History | The revision adds the Robinson, Poonen and Koenigsmann background. These historical assertions are not additional premises of the construction. | Historical context. |
| 9. Off-filter primes | The [earlier audit](evidence/off-filter.md) explicitly distinguished filtering the total label from filtering each prime. The revision states the appendix's scope at the consuming lemma. | Prior justification; scope clarification. |

The historical review found no new mathematical ingredient required by points 1, 2, 3, 5, 6, 7, 8 or 9. For point 4 it found earlier checks of the stronger hypotheses and related local comparisons; Version 10 gives the direct route a fuller, connected treatment. This is a statement about these findings, not certification of the whole theorem. Internal model reviews are not external peer review, and the copied excerpts retain their original scope limitations.

The failure was to conflate an argument present in research notes with an argument adequately incorporated into the manuscript, and then to describe some documentation repairs as mathematical discoveries without first checking that history. Earlier unpublished research is not a reason to dismiss a reader's request for a complete printed argument.

[register.json](register.json) binds each disposition to the exact Version 10 source, application passages, and evidence excerpts. The excerpts record their full original file hashes and original line ranges. A hash establishes identity, not truth, independent review or priority.

```sh
python -B scripts/check_audit_history.py --self-test
```

The checker rejects missing dispositions, missing evidence for claims of prior justification, changed evidence or manuscript bytes, changed application spans and unresolved incorporation. Its negative controls exercise these failure cases. It cannot decide whether the arguments are valid. The [integration protocol](../PROTOCOL.md) specifies the source-level review that still has to be done.

## Subsequent Kato correction

The November 7 follow-up found a missing connection in the Version 10 Kato route: its constructed index set did not cover the 1999 theorem, and the supplied limiting class was not identified. The historical register above is preserved; it is not complete acceptance of that revised route. [Version 11](../../manuscript-revisions/version11/README.md) supplies and independently checks the extension, norm relations and class identity. The current checker now reads a separate application contract and follow-up ledger.
