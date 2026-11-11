# Audit integration and historical claims

This protocol addresses two failures exposed by Issue 2. Earlier arguments were compressed or omitted from the manuscript, then some omissions were incorrectly described as new mathematical gaps. In the revised Kato application, the review checked several hypotheses but failed to compare the required index set with the constructed system or identify the limiting class used downstream. It cannot guarantee mathematical correctness. It makes those comparisons explicit and prevents stale approval from passing the release checks.

## Before responding to an objection

1. Freeze the reviewed manuscript and the proposed revision by commit or SHA-256. Identify the exact claim, its inputs, and the passage that uses it.
2. Search the source inventory, earlier proof packets, corrections, and reviews. Read the actual relevant arguments. A PASS label or a source filename is not evidence that the implication was checked.
3. Classify the historical result separately from the manuscript result. The historical result is one of: prior justification found, prior inputs found but their connecting argument needs work, genuinely new argument required, attribution/history only, or unresolved. The manuscript result is: incorporated, partly incorporated, or pending. Do not call an objection a new gap merely because the printed explanation is incomplete.
4. Record what was searched, the exact evidence that supports the classification, and what was not established. Finding one prior justification does not show that every previous audit checked it independently. Failing to find a proof is not proof that none existed.

## Before marking a repair incorporated

Trace the source statement, hypotheses and conventions through the actual application to its consumer. Check the carrier, field, prime, integral versus rational coefficients, local conditions, maps, normalizations, quantifiers and relevant exceptional cases. Include the connecting argument at the application site or an explicit reference to the exact lemma that supplies it. Check both locations after editing.

For a substantive repair, obtain review by someone other than its author before describing it as independently accepted. If such review has not happened, record that limitation. Repeated reviews by the same agent are not independent reviews. For this Issue 2 historical follow-up the assessment is internal source comparison, not new independent whole-proof validation.

Update the evidence register and run its structural checker. A changed manuscript hash or excerpt must invalidate the old binding until the change is reviewed. Do not relabel all historical sites as current without comparing them. Link the exact release in any public reply, state the scope of the checks, and distinguish a document repair from a change to the polynomial or theorem.

## Release and reporting rules

- Every tracked finding needs its historical disposition, manuscript disposition, supporting evidence, and consuming passage.
- Keep unresolved items open and describe them explicitly. Do not infer global completeness from the number of completed reviews.
- A green CI result verifies only what the named checker implements. It does not certify an informal proof, establish priority, or check the truth of an external theorem.
- Preserve dated source packets and correction notes. Do not rewrite old verdicts to make the history look consistent.
- Before claiming an objection newly discovered a gap, read the historical evidence again. If earlier reporting was inaccurate, correct it explicitly.

## Mandatory comparison for a changed application

Create an application contract before accepting a new or revised route. Use the source theorem itself and its definitions. A summary of its conclusion is insufficient. Record all of the following, with exact source versions, locators and evidence:

1. What the source requires, including every quantified index and exceptional case.
2. What the manuscript actually constructs, including its domain, coefficient ring, lattice and local conditions.
3. Why the constructed domain covers the required domain. When it does not, supply the extension and check its hypotheses.
4. The transition, norm or comparison maps, their directions, and their compatibility. Compute any scalar or Euler factor; do not silently drop it.
5. The identity of the resulting object with the object used by the next argument. A theorem about a related class, ideal or normalization is insufficient.
6. The downstream statements affected by the change and why other historical dispositions can be retained.

The machine-readable contract has nine required obligations. Each must contain the required input, the constructed input, a justification, source references and evidence. If an obligation does not apply, explain why and have the reviewer accept that judgment. Marking a box without an argument does not satisfy the protocol.

Bind the contract to the whole manuscript and to the exact construction, application and consumer passages. An independent reviewer must read those passages and the primary sources, then author an acceptance record identifying the exact contract hash, manuscript hash and review report. The reviewer must differ from every author of that application. Internal model review must be described as such. Do not manufacture approval by copying a previous verdict or editing its hash.

Any change to a bound source, definition, argument, consumer, obligation or manuscript invalidates this acceptance. Compare the change and obtain fresh acceptance before release. Even an editorial change requires the reviewer to acknowledge the new binding; it need not trigger a full mathematical re-audit if the reviewer verifies that the mathematical text is unchanged.

## Follow-ups and release checks

Keep new comments in the follow-up ledger even if GitHub already shows the issue as closed. A closed issue is not evidence that a subsequent objection has been resolved. Each addressed follow-up must point to accepted contracts; unresolved obligations block a release described as incorporating that repair. An interim draft may remain unaccepted, but must say so and must not bypass the release check.

The [Version 10 register](issue2/register.json) is immutable historical evidence. [current.json](current.json) binds the current edition, its exact edits, new application contracts, independent approvals and follow-ups. Its carry-forward entries preserve unchanged historical dispositions, not fresh whole-proof acceptance. Reviewers must check dependency effects even when an old passage is byte-for-byte unchanged.

Run:

```sh
python -B scripts/check_audit_history.py --self-test
```

The checker verifies historical evidence, reconstructs the current manuscript from the reviewed edits, requires a contract for every non-administrative edit, compares fingerprints, checks construction/application/consumer coverage, and rejects missing obligations, missing follow-ups, self-approval and stale approval. The negative controls include the missing index-domain and limiting-class checks that exposed the Kato error. The checker is part of the existing CI workflow.

These checks cannot decide whether a purported argument is correct, whether a reviewer actually read a source, whether all dependencies were identified, or whether two named agents are epistemically independent. They make omissions inspectable; mathematical acceptance still requires the source-level review above. Do not report a structural PASS as proof acceptance.
