# Independent review of the research-protocol setup documents

Decision: accepted within the documentation scope below.

Reviewer: `/root/astra_quartic_opt02_squares`, a model reviewer distinct from documentation author `/root/astra_quartic_opt10_combination`. Review date: November 7, 2026. The exact serving-model identifier is not independently attested here. The reviewer used read-only source inspection, Git comparisons, SHA-256 checks and the existing focused audit-history checker. The reviewer did not author or substantively repair these documents, edit either candidate repository, or publish a review through GitHub.

## Exact files reviewed

The acceptance covers these four file contents, identified by SHA-256 of the Git file bytes to be incorporated. The public and private copies were independently compared and match. The explicit line-ending correction below distinguishes the Windows working copy from its Git representation.

| Repository-relative path | SHA-256 |
|---|---|
| `.github/pull_request_template.md` | `bfcf19002b840001b62e0b6b7ede110aa31d0f98c75d299442b1153b2f18384d` |
| `CONTRIBUTING.md` | `f1683c2a0b1ea424da9ccc69612544d77cb067f78a0aa6807172e20a36f3dec4` |
| `docs/research-review/PROTOCOL.md` | `f2111f716457de7f45183fdeeb0a801d9c53e8378e20d7ae94bcb3f479e0b003` |
| `docs/research-review/README.md` | `2174f0d20a6bb5bedf0b8bb39e2f9e100449747fa8b7b4fd739bcd6e2655b36a` |

The previous reviewed documentation was incorporated at public commit `d8db7497a33b0439488b988a6a86574eb9dfb473` and private commit `894f8907a780367b22ddc6253d66c6330bf56cef`. The three neutral-status edits in this review were still uncommitted when inspected. Those commit IDs identify the comparison baseline, not acceptance of an unseen final packet. The four content hashes above identify this updated semantic acceptance.

Historical binding correction, November 7, 2026: the first version of this report listed `CONTRIBUTING.md` by its Windows working-copy SHA-256, `cd9b912f36b621b5fe3f7097837e89e527706382c9663907a26ac3869b518c76`. The integrator identified that Git stores the LF representation instead. I independently read both Git blobs and both working copies and verified that replacing exactly 32 CRLF line endings with LF reproduces the Git bytes exactly, with no other change. For that earlier version, I explicitly accepted Git SHA-256 `4606405b80cf1dc4eaebf078424e820865fbf68d87c0843ee0a0c5f79a7227b7`. The current table supersedes that content binding after the separately reviewed status edit. The first report is preserved separately as historical evidence. This is a reviewer-authored binding correction, not a semantic repair or an integrator refresh of an old verdict. At that earlier review the other three files used LF directly. Current line-ending verification is recorded below.

The supplied source was the owner's “Mathematical research review protocol,” version 1.1, November 7, 2026. Its SHA-256 is `f2111f716457de7f45183fdeeb0a801d9c53e8378e20d7ae94bcb3f479e0b003`. The repository's `docs/research-review/PROTOCOL.md` is byte-identical to that source. This is a review of faithful adoption and contributor guidance, not a new claim that software can decide arbitrary mathematical truth.

I also read the existing `AGENTS.md`, `docs/audit-history/PROTOCOL.md`, and the current review record's scope limitation. Their hashes are respectively `8962f442f897f69d6f001a589eeae22881bda75b77f1b77e7f30f3b7d50e0bfb`, `c0b9834a75e64bfd66183b06d1e26019f957a38468ce41b10ce290f8c5c44816`, and `b5ea322583af1100d2d73f25a7185e42e747e76c5609f227331ecd03ab869eb9`. They are unchanged from both setup bases.

## Source-to-guidance review

All five requested completion requirements are present as requirements, not optional aspirations:

1. The full protocol requires complete proof modulo identified published theorems with checked applications. The contributor guide requires publication venue and authoritative version and project proofs for needed unpublished inputs. It requires unresolved assumptions to be stated instead of claiming complete verification.
2. The guide requires every cited application and substantive uncited external input, review of the inventory for omissions, and all nine application obligations. Those obligations include connecting maps, domain coverage, conventions, exceptional cases and the exact downstream object.
3. The guide requires explicit domains, simultaneous choices, algorithms, constants, inputs, certificates, commands and reproducible outputs. It distinguishes compressed or generated representations from full expansions and finite identities from their arithmetic applications.
4. The guide requires every received human or model audit and substantive objection, including unfavorable reports and follow-ups on closed issues. It requires reviewed repairs or independently checked rebuttals and preserves unresolved findings and prior verdicts. The unchanged full protocol supplies the detailed duplicate, vague-concern and scope rules. Neither votes nor silence resolve a finding.
5. The guide requires repeated independent audit, repair and integration through final frozen closure. It requires rechecking affected premises, consumers and computations, plus independent review of the assembled proof. A collection of component acceptances is not treated as final closure.

The PR template asks for the exact revision, hashes, changes, dependency effects, source/application inventory, explicit computation evidence, non-author decisions, complete audit findings and final integration review. It directs users to explain inapplicable items and identify incomplete work. The contributor entry point links both the practical guide and full protocol. Local document links and the two named protocol heading targets were checked against the reviewed files.

The independence requirements agree with the existing guidance. An application author cannot independently accept that application; another run by the same agent is only a repeat check. A reviewer who supplies a substantive repair needs a different non-author reviewer. Human and model review are explicitly distinguished, unknown model metadata stays unknown, and new file/dependency bindings require reviewer-authored acknowledgment. These documents impose no mandatory second human or GitHub-user approval. They support independent agent review while retaining the owner's separate publication authority.

## Findings and dispositions

Finding DOCS-1: the initial PR template used `../docs/research-review/README.md` and `../docs/research-review/PROTOCOL.md`. A template's text is inserted into a PR body; it is not rendered there as a file located in `.github`. Those relative targets therefore did not reliably identify the intended guide and protocol. This issue was reported during integration before this final semantic freeze.

Disposition: resolved by the documentation author. I inspected both initial targets and the final template. The final version uses the absolute public GitHub `blob/main/docs/research-review/README.md` and `blob/main/docs/research-review/PROTOCOL.md` URLs. Both repositories carry identical guide/protocol contents. The original fix changed exactly those two targets on one line. Those absolute targets remain unchanged in the newly bound template. The URLs are navigation to the adopted main-branch documents after integration; they are not immutable review evidence. Exact review evidence remains the hashes in this report. I did not claim those new main-branch URLs were already live before the setup merge.

No other unsupported instruction, omitted completion requirement or unresolved substantive documentation finding was found in this review. That statement concerns this review's findings; it does not assert that no other audit or subsequent PR comment exists. Complete current/historical intake must still be reconciled by the final setup process.

## Mathematical scope, rollout and verification

The original setup changed the four semantic documentation paths above. The current follow-up comparison against the two commits named above changes only CONTRIBUTING, the PR template and the contributor guide. The existing setup review report remains unchanged in those working trees until the maintainer incorporates this new report. The mathematical manuscripts, polynomial artifacts, formalization, review contracts, existing guidance and focused checker sources are unchanged by this follow-up.

The guide explicitly preserves the current manuscript record's inherited qualifications and says installing the protocol neither expands its scope nor retroactively certifies the complete proof. It distinguishes structural checks, mathematical status and review coverage. The current text directs readers to the applicable live ruleset for enforcement status and expressly declines to assert that the App requirement is already active. It requires the designated App check to be required and passing for the exact revision before a merge is treated as protocol-gated. It retains the evidence bindings and recorded cutoff; the guide promises neither instantaneous later-comment detection nor an atomic comment-and-merge transaction. These are conditional requirements, not a claim that deployment tests or activation have occurred.

I ran `python -B scripts/check_audit_history.py --self-test` from each repository root using the unchanged existing checker. Both returned exit code 0 and reported:

```text
PASS: 9 historical dispositions, evidence pins and manuscript passages. Not a mathematical proof check.
PASS: 7 negative controls rejected.
PASS: 19 application-review negative controls rejected.
PASS: 3 current application contracts, revision and follow-up records. Not a proof check.
```

I did not rerun heavy mathematical builds or claim a fresh whole-proof audit. The relevant conclusion is faithful documentation adoption, correct links after the identified fix, unchanged mathematical scope, and successful existing structural checks.

## Follow-up review of neutral enforcement wording

The documentation author changed only status wording in three files. I independently read their complete new contents and compared both working trees with the prior committed versions. CONTRIBUTING replaces the fixed rollout statement with a pointer to the guide and a warning that existing CI alone does not establish protocol completion. The template and guide link the public and private rulesets and state the conditions for a protocol-gated merge. The guide changes “planned App check will bind” to the normative “App check must bind.” The complete protocol source, all five completion requirements, the nine application obligations, independence rules and mathematical scope remain unchanged.

This limited revision is accepted. It avoids a statement that would become false merely because activation occurs later. It also avoids inventing an active deployment. The named check must come from the designated App, be required by the applicable ruleset and pass for the exact revision. Neither ordinary green CI nor a contributor-written receipt satisfies that condition. The wording still imposes no mandatory human approval and does not retroactively certify the mathematical proof.

The two ruleset repository/ID pairs match the previously captured setup records in BASIC-PROTECTION-FINAL.json: public `elliotglazer/diophantine-z-q`, ID `26781429`, and private `elliotglazer/private-diophantine`, ID `26781446`. I used those records to check link identity only. I did not use an old capture to assert current live settings, and I did not assert that every reader can access the private ruleset. The links provide current navigation rather than immutable review evidence. This review does not accept any future ruleset edit or bypass setting; live activation and enforcement remain separate verification work.

The current table binds LF-normalized Git file contents. For each edited file I independently checked Git's filtered `hash-object --path` result against a direct Git-blob hash of the normalized bytes, as well as the SHA-256 shown above. Exactly 32 CRLF endings in CONTRIBUTING, 20 in the template and 43 in the guide normalize to those bytes, with no other change. Their current working-copy SHA-256 values are respectively `529cda1dbfa2d4b1cdaea368d2deac63ce7218e1cdb678e45d06be3715235b9a`, `4b38b307317af7b0bf70530849b193c8263f55eec6ffb6d72590e44738e3fcf5`, and `95961f7735d0e466ef68025a769df2f9bd1e26dc6725bf94763c36e0f73f3efe`. The protocol still uses LF directly. Git need not already store the new uncommitted blobs for this calculation; final assembly must verify the committed bytes again.

The previous accepted report is preserved as `INDEPENDENT-DOCS-REVIEW.before-neutral-status.md`, SHA-256 `b2d3b9e903bf7101bfd2e110db3b63bc2e253c93a07c4b1fa6ac8f7c1ac04e32`. `NEUTRAL-DOCS-REVIEW-CHECKS.json`, the two saved diffs and `check_neutral_docs_review.py` record the independent comparisons and fresh successful focused checks in both repositories. The original checker first attempted to read an uncommitted object by ID; because that object had not been written, I used read-only Git hash calculation and independent byte hashing instead. No candidate repository file was changed by the reviewer.

No new unresolved documentation finding was identified. This is an explicit reviewer-authored decision for the changed semantics and new hashes, not an integrator update of an earlier acceptance. The reviewer authored this report and its metadata corrections; a distinct non-author reviewer must handle their final incorporation and assembled-packet acceptance.

## Later final binding

This report accepts the four semantic file contents above. It is not its own receipt, does not contain a self-referential final-head hash, and does not accept an unseen final application or assembly packet. After the report and template are committed, the final complete manifests, changed-path coverage, application/dependency targets and exact report bytes must be inspected and explicitly adopted by an eligible non-author reviewer. Any semantic change reopens the affected review. No successful App check, merge authorization or mathematical whole-proof acceptance follows from this report alone.
