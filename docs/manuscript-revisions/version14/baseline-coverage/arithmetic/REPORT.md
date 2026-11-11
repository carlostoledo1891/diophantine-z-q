# Arithmetic source-first coverage review

Reviewer: `/root/astra_v14_baseline_arithmetic`, a separate model agent from the author/integrator. Date: November 7, 2026. The tool interface did not report the exact inherited model identifier. Available tools included local shell, Python and file reads. No web search, remote change, manuscript edit or optimization was performed.

The frozen target is `manuscripts/quartic_v13.tex` in `work/quartic-version6-release/repository`, repository HEAD `2125274b93314c9a9e51c7b47559025489565632`, SHA-256 `9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd`. This review covers lines 1 through 5930 inclusive. It covers the stated main theorem and its composition, syntax, elliptic model, height, pole, multiplication, restricted-converse assembly, actual classes and both limits. Later supplier sections remain explicit joins to the other assigned reviews.

## Decision

Accepted within the scope of source-first reconstruction: the coverage index covers every line in this assigned slice, and the initial table identifies its substantive imported assertions and the inline arguments consuming them. There are 117 consecutive passage records, including 115 dependency groups, one front-matter exclusion and one historical-context passage with no proof import. Paragraphs mixing proof with comments keep the proof classification. No passage in the assigned slice is marked unreviewed.

The separate decision on complete supplier reconciliation is **incomplete pending the assembled joins**. The table has 39 explicit references to 27 distinct labels outside this slice. Some are announced downstream conclusions; others are required suppliers such as the coefficient rules, simultaneous-address construction, odd stabilization, de Rham descent and literal compiler. Their exact current label locations are in `RECONCILIATION.json`. This report does not accept their proofs on the basis of their summaries here. The parent must join supplying and consuming contracts, including the implicit dependence on visibility implication O.8 in the odd-source appendix.

No specific false arithmetic inference or counterexample was found in this slice. That is a scoped observation, not a claim to have re-proved all inherited mathematics. The retained application decisions concern their published-source interfaces and named internal premises. They must not be promoted to whole-proof acceptance by counting them or by passing a schema check.

## How the reconstruction was frozen

I first read the actual source in bounded consecutive chunks. A truncated tool result required a separate reread of lines 218 through 277. I completed all 5930 lines before writing the initial rows. I had not opened the declared application inventory, dependency records or favorable reports at that point. Before the source read I did read the user protocol, repository `AGENTS.md`, the required `docs/audit-history/PROTOCOL.md` and the unslop skill. The repository protocol mentions previous Issue 2 failure categories. Thus this was source-first, but not a claim of ignorance of all prior project history.

`INITIAL-FREEZE.json` was written before inventory access. It pins:

- `INITIAL-SOURCE-USES.json`: `c2aca1c006a6d160db3ba60fce551eabf0858d71f71419709bf58b06701eb503`.
- `COVERAGE-INDEX.json`: `7ade73cf73d1fb089296a1611e7ec07bdf55c16e30e2e6200d2aff025956d421`.

Every passage hash is SHA-256 of its actual source byte lines, preserving the original mixed LF/CRLF endings. Generated JSON and this report use UTF-8 and LF. The frozen initial files were not rewritten during reconciliation.

## Reconciliation and retained acceptance

I read the relevant application contracts after the freeze, including their required objects, hypotheses, convention differences and translation justifications. `RECONCILIATION.json` maps 100 of the 115 groups to named historical application families. The remaining groups include definitions, announced claims, finite algebra and arguments given directly in this slice. Eighty-five groups also intersect exact historical anchor text. An anchor match is recorded as a textual match, not an independent proof of every assertion in a broad passage.

The old `coverage.json` already says semantic exhaustiveness and application correctness are not certified. The historical inventory is bound to its own `audited-baseline.tex`, not directly to V13. The new table preserves that distinction. The historical anchor matcher normalizes line endings only to locate identical text and then hashes the actual V13 byte spans. It does not refresh an old review hash. Changed or unlocated historical contexts cannot gain acceptance merely from overlapping a new passage.

`DEPENDENCIES.md` and `DEPENDENCY_PHASES.json` give important restrictions that agree with the source-first reconstruction. A075's finite-model construction precedes duality and its later arithmetic budgets. A080's derivative local-data argument supplies actual maps and homotopies; A044 still needs exact global annihilators and the nonzero localization of the actual class. A041 additionally needs the actual norm relation and determinant-basis comparison. These direct premises remain visible in the new source-use rows, even when the old inventory groups them under one application number.

A023 alone is not the current prime-two Kato justification. V13 carries the `KATO-1999-INDEX-AND-CLASS` contract with the full 1999 index domain, both norm cases and identification of its supplied class with the retained cyclotomic class. I read the V11 `norms.md` and `interface.md` derivations and the exact V13 carryforward contract/report. Those arguments preserve the same character conductor, smoothers and fixed lattice multiplier. Equal support gives no extra Euler factor; transitivity is applied to the actual upper class, not to a restriction followed by corestriction. The direct consumer in this slice is the common even scalar at lines 1970 through 2095. The primary Kato application passage itself is beyond this slice, so the appendix reviewer still supplies the current-source join. The V13 carryforward acceptance is retained within its stated scope and is not replaced by a new whole-proof verdict.

Other application families lying beyond this slice, such as the quantitative prime bound, MRDP compiler and degree/corollary arguments, are not extra unused premises merely because their detailed uses occur later. The initial table retains their announced and composition-level consumers, and the parent must join those consumers to the later coverage records.

## Two historical arguments checked directly

The pole matrix construction at lines 1104 through 1156 is compressed and refers to S11–S12. I read the actual derivation in `docs/theorem-application-audit/evidence/pole.md`, not just its opening verdict. It proves both cross-row sums while allowing nonzero individual cross-symbols, the rank-one correction and deleted-block criterion, the full-product coefficient argument for the second support, and the simultaneous CRT realization. It handles a one-prime beta and theta equal to one. It checks the extra class locally at every place before using the dimension upper bound. The subsequent Kummer argument proves full Selmer corank one before applying RC, and uses finite Sha only after the forward rank theorem.

That report also gives explicit witnesses with the same m, A and H. If x1=Aq1² and x2=Aq2², H=theta c², then e=n/q1² and z=cq2/q1 produce the required second ordinate z*r2. This matches lines 1196 through 1206. The report's comparison with the saved root Q_pole² explains why its saved root can have degree 150 while the displayed Q_pole has degree 75. There is no degree-75 assertion for the squared root here. I found prior justification incorporated by summary and source reference, not a new mathematical gap. Publication of the complete source packet remains a release-evidence question for the parent.

For multiplication soundness I read the historical valuation excerpt in `docs/audit-history/issue2/evidence/valuation.md` and compared its actual common-group/common-place argument with lines 1287 through 1331. The current proof uses a different direct contradiction estimate: alpha is odd and at most delta, a failed threshold gives inverse-group valuation at least 2delta−alpha, and failure everywhere gives an odd pole valuation at most −delta. The integrality of the two log ratios is established before using absolute truncation congruences. This does not require all factors in the selected group to be units. The earlier derivation is prior justification; the new coverage row identifies the current written argument rather than substituting the historical verdict.

## Finite computation replay

I copied the existing exact generator checker into this output directory without changing its bytes and ran it with the pinned Python executable. This is a replay of an existing certificate check, not a new search. It verified the 20/24 reduction counts, 7004 primitive quadratics, 14008 quadratic roots, 111 rational candidates, the exact seven survivors, the integer height comparison, torsion translates and coordinate change from 2R to P0. Its output is `generator-arithmetic.json`; checker SHA-256 is `f10d5636264f0c1b1ce23fd288532ac509e167aba3dab89a5655d7bb4e9de0fb`.

This computation does not prove the duplication-height inequalities, two-isogeny local image calculations, or any restricted-converse theorem. Those are explicit separate inputs in the coverage table.

## Limits and outstanding joins

The review checks dependency coverage and compares the current contracts. It is not a fresh page-by-page inspection of every published source, and no such claim is made. Historical accepted source applications can remain accepted where the exact assertion and its dependencies match. The external statements, versions and locators copied into `RECONCILIATION.json` are inherited source records; their presence is not a claim that this agent opened every primary file again.

The parent still needs to join at least these supplier interfaces before an assembled completeness decision:

- The two numerical height applications and the fixed M0/catalogue/guard constructors to the size and literal-expression proof.
- The compiler/bridge's natural witness domain and one-shared-shift value relation to the ordinary integer projection.
- Kato's current full index-domain and retained-class construction to the even common scalar, including the positive real complex and central calibration.
- Actual coefficient omission, contraction and primary-isolation rules to the two address lemmas, with the same source/depth and all finite operator budgets.
- Odd visibility, attained minimum and stabilization to the final family. The stage must be selected before its actual primes, and the final companion K and determinant precision must already be fixed.
- De Rham descent to the representation consumed by Berger and Pan, retaining the Tate/cohomology dual and weights 0,−1.
- Later quartic and consequence claims announced in lines 44 through 158 to their own independent coverage.

No source file outside this output directory was changed. No old acceptance was regenerated. The review may be reopened by a later omitted input or failed supplier join.
