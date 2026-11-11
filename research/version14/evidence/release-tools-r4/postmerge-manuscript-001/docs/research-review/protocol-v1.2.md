# Mathematical research review protocol

Version 1.2 | November 7, 2026

## Purpose and scope

Use this protocol to review mathematical research maintained in a Git repository, including informal manuscripts, computational constructions, and partial or complete formalizations. It connects each claimed result to its actual inputs, the argument applying them, and the later arguments that use its conclusion.

The governing rule is simple: review the inference actually written, using the objects actually constructed. An accepted conclusion, a familiar theorem name, a successful computation, or an earlier favorable report does not establish that a changed argument works.

This protocol specifies a review process and the requirements for supporting software. It does not include an executable checker. Automated record checks establish only the properties they implement. They cannot decide the correctness of arbitrary mathematics or guarantee that the dependency inventory is complete.

## Required completion standard

The default goal is to verify the complete proof modulo published theorems, inventory and check every cited theorem application, make every construction and computation explicit, resolve every recorded audit objection, and repeat review and repair until the final revision is stable under the checks below. These are completion requirements, not optional aspirations.

1. **Complete proof modulo published theorems.** Trace every claimed conclusion to proved internal steps and identified published external theorems. Check each external theorem's actual hypotheses, conclusion, conventions, and application. A public preprint does not qualify as a published theorem merely because it is accessible. Record the publication venue and authoritative version. An unpublished result may motivate the argument or receive attribution, but its needed content must be proved within the reviewed manuscript or a precisely linked, versioned project proof before declaring this standard met. Any unresolved conjecture, unsupported internal lemma, unverified computational assertion, or additional axiom prevents full completion under this standard. A conditional result may still be reported, with its remaining assumptions explicit.
2. **Complete inventory and source checks.** Inventory every cited theorem and every substantive uncited external input. Record the exact source version and theorem location. Compare the final published statement, applicable corrections, and the definitions needed for each use. Perform the nine application checks below, including the connecting maps and actual downstream object. Review the inventory itself for missing applications.
3. **Explicit constructions and computations.** Supply unambiguous definitions, domains, parameter choices, algorithms, constants, and output representations for every construction. State and prove existence or termination where the construction requires it. For each finite computation, provide its exact inputs, procedure or certificate, checker, and reproducible result. If an object is too large to print, a finite, unambiguous specification and a justified method for recovering its entries may suffice; label that representation accurately. Do not claim a full expansion when only a generator or compressed representation is supplied. No assertion that a calculation is routine substitutes for the calculation or a complete derivation.
4. **Every audit objection addressed.** Enter every substantive doubt raised in every received human or model audit into the findings ledger, regardless of the auditor's identity or reputation. Resolve it by a reviewed repair or an independently checked, evidence-based rebuttal. Duplicate objections may link to an existing resolution. A vague concern must be made precise enough to assess, or retained with an explicit explanation of what information is missing. Votes, repeated assurances, silence, and the absence of further replies do not resolve an objection. A concern outside the claimed scope may be closed only with a recorded scope explanation; an unsupported step needed by a claimed result cannot be moved out of scope to obtain completion.
5. **Iterate until stable.** After every substantive repair, recheck its premises, affected consumers, and relevant computations. Repeat independent audit, repair, integration, and review until the final frozen revision meets the closure test below. A lack of new comments or agreement among several models is not, by itself, stability.

If a project intentionally adopts a broader trust base or leaves work unfinished, state that departure explicitly. It must not describe the result as fully verified modulo published theorems under this protocol.

## Roles and independence

An **author** proposes a statement, proof, construction, or repair. A **reviewer** assesses a specified version against its sources. An **integrator** incorporates accepted changes, checks their effects elsewhere, and prepares the release. One person may fill different roles for different applications, but an author must not supply the independent acceptance of their own application.

Record whether each reviewer is human or a model. For model reviews, record the model, task identity, reviewed files, available tools, and scope. A second run by the same agent is a repeat check, not an independent review. A distinct agent can supply a non-author review, but distinct identities do not establish independent reasoning or eliminate correlated errors.

Reviewers should derive the relevant inference from the primary sources and manuscript before relying on earlier verdicts. They may use earlier reports to locate evidence, then compare the actual arguments. If a reviewer supplies a substantive repair, obtain another non-author review of that repair before calling it independently accepted.

These are review requirements, not permission to publish, message other people, disclose private files, or change repository access. Those actions remain subject to the project owner's authorization.

## The working sequence

1. Freeze the manuscript, source files, and computational artifacts being reviewed.
2. Inventory the target claims, external inputs, internal dependencies, and exact application sites.
3. Write an application record for each substantive inference or change of proof route.
4. Review the required inputs against the constructed objects, including all connecting maps and exceptional cases.
5. Obtain a separately authored decision tied to the exact reviewed files and edits.
6. Integrate the argument into the manuscript and review its downstream effects.
7. Reproduce the relevant checks from the release files, preserve unresolved findings, and publish only the status justified by the evidence.
8. Repeat the audit-and-repair cycle and perform the final closure review below. Any new substantive finding or change reopens the affected obligations.

Parallel work is encouraged when applications have stable interfaces. Give workers bounded tasks, explicit source versions, permitted output files, and a named consumer for their result. A separate integration review must check that independently accepted pieces use the same objects and conventions.

## Freeze the evidence

Identify each review target by an immutable Git commit and by hashes of the files actually examined. Include uncommitted files explicitly. Record paths relative to the repository so another researcher can reconstruct the same packet.

Use a declared hash algorithm, such as SHA-256. Specify text encoding and line endings for generated files. If a check compares canonical JSON or another normalized representation, version the canonicalization rule and preserve the original bytes as well. Do not silently normalize mathematical content to make a hash match.

For a manuscript passage, record its theorem or section label, line or page range, and excerpt hash. Bind the application record to the whole manuscript as well as the construction, application, and consumer passages. Whole-file hashes detect changes; passage references explain what was reviewed.

A PDF build record should identify the source tree, main file, engine and dependency versions, build command, diagnostics, and output hash. A successfully rendered PDF establishes neither reference accuracy nor mathematical correctness.

## Inventory claims and dependencies

Start from the results announced in the title, abstract, main theorems, and claimed corollaries. Trace their dependencies through the manuscript. Include computational facts, existence statements, uniformity claims, effectivity claims, parameter bounds, and translations between representations.

For every external input, record:

- The exact statement used, including quantifiers and hypotheses.
- The work's title, authors, edition or revision, publication status, stable locator, and an accessible source location where available.
- The hash of the source file actually read, with access date when useful.
- Relevant definitions, proof passages, corrections, and errata.
- Whether the final published version, an author manuscript, or another version was checked.
- Every consuming application, or a precise reusable lemma that supplies those applications.

For internal results, record the exact statement, its proof location, its dependencies, and its consumers. A source with a similar conclusion is not a substitute for the required statement. A diagram or citation does not supply an omitted connecting argument.

Check that the abstract and corollaries use no stronger conclusion than the proved statement. In particular, pointwise existence does not automatically supply a uniform construction, and existence does not automatically supply an effective bound.

The inventory is itself subject to review. A schema can require fields in an entered record; it cannot establish that every necessary record was entered.

## The nine application obligations

Each application record must address the following obligations. For every obligation, write **what is required**, **what is constructed**, **why they match**, and **where the evidence is located**. Include the derivation rather than a bare checked box.

| Obligation | Required comparison |
| --- | --- |
| Source hypotheses | Match every source hypothesis and quantified parameter to the application. Read the relevant definitions and resolve material ambiguity from the proof. |
| Constructed objects | Identify the actual fields, rings, spaces, modules, schemes, functions, classes, witnesses, or algorithms supplied by the manuscript. |
| Domain and index coverage | Show that the construction covers the source's entire required domain, family, or index set. Prove any extension, restriction, or cofinality argument. |
| Transition and comparison maps | State the maps, their directions, and their compatibility. Account explicitly for signs, scalars, normalizations, degree factors, and Euler factors. |
| Identity of the consumed object | Show that the conclusion concerns the object used in the next step. Identify limits, specializations, images, ideals, or normalizations precisely. |
| Coefficient and normalization conventions | Match coefficient rings, integral versus rational structures, embeddings, bases, valuations, Frobenius conventions, duals, and twists wherever relevant. |
| Local conditions | Check localizations, completions, supports, ramification, boundary conditions, and local or global compatibility requirements. |
| Exceptional cases | Treat excluded characteristics, small primes, zero denominators, degenerate parameters, torsion, singular loci, and endpoint cases that can occur. |
| Downstream consumption | Identify every affected consumer and show that the output has the precise strength and form needed there. |

An obligation may be marked **not applicable** only with a reason specific to the application. The reviewer must assess that reason. For example, a finite polynomial substitution may introduce no limiting process, but its output must still be identified with the polynomial consumed downstream.

### Common failures to test explicitly

- A theorem requires a family indexed by all admissible integers, while the construction supplies only a smaller subfamily.
- A source proves an exact sequence, but the application uses an isomorphism of one of its maps.
- Two constructions produce proportional classes, but a later step needs equality or equality of integral ideals.
- A relation holds after tensoring with a field, while the conclusion requires an integral statement.
- A generic formula divides by a quantity that may vanish on an allowed solution.
- A cited rank, nonvanishing, or existence statement has a different prime, twist, local condition, or quantifier.
- Separately valid choices of witnesses, auxiliary primes, or parameters cannot be made simultaneously in the order the proof requires.

These are diagnostic patterns, not an exhaustive list.

## Review objections without rewriting the history

Freeze the objection and the version it concerns. Search earlier manuscripts, source inventories, proof packets, correction notes, and reviews. Read the relevant earlier arguments rather than relying on their titles or verdicts.

Register every received audit and reconcile its individual findings with ledger entries. Do not select only favorable reports or omit a finding because another model declared the same section correct. Track the disposition of each finding separately. A repair must address the stated inference; a rebuttal must explain why that inference is justified or why the objection does not apply to the frozen claim.

Record historical justification separately from incorporation into the current manuscript.

| Historical finding | Meaning |
| --- | --- |
| Prior justification located | An earlier argument supplies the inference, with its stated hypotheses. |
| Prior components located | Relevant inputs exist, but their connecting argument still requires work. |
| New argument required | The available route does not establish the needed inference; a substantive repair is required. |
| Attribution or presentation issue | The finding concerns credit or exposition rather than an identified invalid inference. |
| Unresolved | The search or analysis is insufficient to classify the issue. |

Separately mark manuscript incorporation as **incorporated**, **partly incorporated**, or **pending**, with exact locations. Record the search scope and its limits. Failure to locate an argument is not proof that no argument existed. Finding one earlier justification is not evidence that every prior reviewer checked it.

Also separate mathematical status from review coverage. “I have not checked this cited theorem” differs from “this theorem is an unproved premise” and from “this application is invalid.” A claim is conditional on an unproved mathematical input, not merely on the fact that a particular reviewer has yet to read part of its proof. State which situation applies.

Preserve prior verdicts and append corrections with dates and reasons. If earlier reporting was inaccurate, correct the reporting explicitly.

## Changes invalidate old acceptance

An acceptance applies only to its named manuscript, application record, source versions, evidence, and exact edits. A change to any bound item makes that acceptance stale for the changed version.

Classify the change and assess its effects before refreshing any binding:

- **Substantive argument or statement change:** review the changed inference and affected consumers anew, even if its conclusion was accepted previously.
- **Source or convention change:** compare the exact versions and recheck every application affected by the difference.
- **Computational change:** recheck the specification, implementation or certificate affected, plus the connection to the mathematics.
- **Editorial or unrelated change:** verify that the relevant mathematics and dependencies are unchanged, then obtain an explicit reviewer acknowledgment of the new binding. A full mathematical re-audit is unnecessary when this comparison establishes that it is unaffected.

The new decision must be authored by the reviewer. An integrator must not copy an old favorable verdict and replace its hashes to manufacture fresh acceptance. Record the exact edit fingerprints that the reviewer accepted, not just the final file hash.

Changed dependencies can invalidate an unchanged passage. A dependency review must therefore accompany textual comparison. Do not infer safety solely from a byte-identical theorem application.

## Computations and certificates

Distinguish **finding** an object from **checking** it. A search program may use heuristics or substantial resources. Its output becomes evidence only through a check that addresses the required mathematical specification.

For a computational claim, record the input specification, source and executable versions, dependencies, invocation, resource limits, outputs, exit status, and artifact hashes. Preserve enough information for a fresh checkout to reproduce the relevant check. Use deterministic serialization for files whose exact bytes are part of the certificate.

State exactly what the checker establishes. For a polynomial construction, relevant questions include:

- Does the checked source system express the intended arithmetic predicate?
- Does every transformation preserve the required projection over the stated field, in both directions?
- Are divisions, exceptional branches, signs, and simultaneous witness choices justified?
- Are fixed constants distinguished from quantified variables and free parameters?
- Are coordinate maps, full expansions, cancellations, coefficient bounds, degrees, and variable counts checked in the representation actually published?

An algebraic identity check does not establish a separate arithmetic existence theorem. A tested sample does not establish a universal assertion. A successful program exit does not establish that the program checks the intended property.

Where practical, separate the certificate producer from the checker and test rejection of deliberately corrupted certificates. Document the checker's own mathematical justification and trusted software dependencies. Report a platform-specific replay as such until portability has been tested.

For formalization, bind the exact formal statement to the mathematical claim and list admitted assumptions and axioms. An externally attested computation recorded as an axiom remains an additional assumption of the formal proof. It is discharged only by an appropriate verified argument or explicitly included in the stated trust base. Distinguish kernel-checked certificate verification from unverified external checking.

## Independent decisions and integration

The reviewer must inspect the application, its sources, and its consumers. The decision must identify the exact reviewed versions, remaining dependencies, and one of these outcomes:

- **Accepted within stated scope:** the specified inference passes review relative to the listed inputs.
- **Changes required:** identify the unsupported step and the needed correction or evidence.
- **Incomplete review:** identify what was and was not checked without implying a mathematical counterexample.
- **Rejected:** give the precise contradiction, counterexample, or invalid inference found.

The integrator must check the final manuscript after incorporation. A correct proof left in a private note is not an incorporated repair. Include the argument at its application site or link to an exact lemma that supplies it. Review both the supplying and consuming passages after editing.

For parallel work, check that common notation denotes the same objects across packets. Reconcile hypotheses, coefficient conventions, parameter choices, and exceptional cases before assembling the conclusions. A collection of favorable component reports is not an integration proof.

## Repository records and automated checks

The project may choose its own paths and file formats. A small installation can keep these records as Markdown plus JSON or YAML; a larger project can generate them from a database. Keep the source records portable and version controlled.

| Record | Minimum contents |
| --- | --- |
| Claim inventory | Target statements, dependency edges, proof locations, consumers, and status. |
| Source inventory | Exact versions, statements used, locators, file hashes, corrections, and access limitations. |
| Application records | The nine obligations, author identities, bound files and passages, exact edits, and dependency impact. |
| Reviewer decisions | Reviewer identity and type, decision, scope, application hash, manuscript hash, and report hash. |
| Findings ledger | Objection identity, reviewed version, history classification, manuscript incorporation, response, and remaining work. |
| Release manifest | Manuscript and artifact hashes, accepted record set, unresolved findings, reproduction instructions, and check results. |

An automated implementation should reject missing required fields, unsafe paths, changed bound files, unresolved required obligations, missing consumers, self-approval, stale decisions, unexplained edits, and omitted tracked findings. It should verify that the files selected by the build are the files selected by the current review record.

Tests should deliberately introduce a missing domain argument, a missing consumed-object identity, a changed source, an unreviewed edit, a stale approval, a mismatched build target, a missing follow-up, and a corrupted certificate. Each should fail the relevant check for the intended reason. Keep these negative controls alongside the checker.

Do not imply that these structural checks establish complete source coverage, honest review, mathematical truth, or independence of thought. Name CI jobs according to what they check, and keep mathematical review status separate from execution status.

## Release and issue closure

### Final closure review

After the last substantive repair, an independent reviewer must review the assembled proof from its stated results through its dependency chain. Accepted component reports may supply evidence, but they do not replace this check of the complete composition. Freeze the revision being assessed and verify all of the following:

- Every announced result has a complete reviewed argument whose external assumptions are published theorems with checked applications.
- Every construction and computational claim meets the explicitness and reproducibility requirement above.
- Every received audit is registered, and each substantive finding has a reviewed resolution applicable to this revision.
- All required application records and affected downstream reviews are current; no change or dependency update remains unreviewed.
- The complete manuscript incorporates the accepted arguments, including repairs previously present only in notes or packets.
- The relevant computations and release checks pass on the exact frozen artifacts, and the inventories and manifests describe those same artifacts.
- The final assembly review introduces no unresolved substantive finding.

If any condition fails, continue the cycle. If the final review produces a repair, integrate it and repeat the affected reviews and closure assessment. Record the reviewers, review scope, findings, resolutions, and frozen revision for every round. Stability means these explicit obligations are closed on the final revision; it does not guarantee that no future reviewer will discover an error. A later substantive objection reopens the relevant finding and completion claim.

### Release and issue decisions

Before describing a revision as resolving a finding, confirm that:

- The exact revised argument is present in the released manuscript.
- Its application and affected consumers have current review decisions.
- Relevant computations have been reproduced from the release files.
- The source inventory and findings ledger match the release.
- Unresolved inputs and review limits are stated where they affect the claim.
- Public links identify the actual release, rather than a moving or obsolete draft.

A GitHub issue's closed state does not establish that a later comment has been addressed. Keep new substantive follow-ups in the ledger. If an issue is closed for administrative reasons while a mathematical question remains open, say so. A release may contain an explicitly marked open argument, but must not describe that argument as resolved or bypass its incomplete review status.

Preserve historical releases and review evidence. Do not silently overwrite an earlier verdict, change a bound source, or present an old review as acceptance of a new proof route.

## Release maintenance and research handoff

Maintain a reviewed project profile that identifies the required release artifacts, their names and locations, edition and date conventions, publication destinations, reproducibility entry points, and any size or inclusion thresholds. Make these requirements specific enough to check against the actual release. A profile may require additional evidence for the project's constructions or publication process. It must preserve this protocol's proof, source-application, objection and independence requirements. Changes to the profile require an explicit review of their effect on release coverage.

### Cumulative research handoff

Update a cumulative research handoff for every research release. Include the current research and the relevant prior research, derivations, computational evidence and reviews needed to understand or reproduce the released work. Retain relevant negative results, rejected approaches and superseded reviews with their status and the reason for supersession. Link a corrected claim to the earlier claim and the correction. Preserve the originals so a later reader can reconstruct the reasoning and review history.

The handoff must contain the actual research evidence or identify its exact versioned location. A summary cannot replace a needed derivation, certificate or review. Record known missing evidence and open work explicitly. Include the provenance of contributed research and computational artifacts, including authors, reviewers, source versions, generating tools and any stated limitations. Attribute earlier work and later repairs accurately.

Keep conversational transcripts, credentials and unrelated private files out of release handoffs. Extract the relevant mathematical arguments, decisions and objections into reviewable records while preserving their meaning and attribution. Preserve any original conversation evidence needed for an audit in the appropriate restricted record, with an access limitation recorded where it affects review. A publication access restriction does not resolve a mathematical objection or excuse omission from the findings ledger.

### Archive index and release manifest

Maintain an archive index and a manifest for the handoff and release artifacts. Identify each release's source commit, version, date, authorship and provenance, review status, remaining assumptions and open work, reproduction entry points, and the required files with their declared hash algorithm and hashes. Identify which entries are current, historical, superseded or incomplete. Record the relationship between generated artifacts and their source inputs, commands and tool versions. State the coverage of the archive and any unavailable material.

Preserve old editions and their manifests at stable versioned locations. A new release may update a current-version pointer, but it must retain the earlier edition and its review status. Avoid a manifest self-reference by recording its own digest in a separate release record or other external versioned binding. Bind final review to the completed release manifest and actual artifact bytes.

### Synchronize the release

Before final acceptance of each research release, compare the assembled files and verify all applicable items below.

- Update the repository README and current-paper links, the current TeX or other manuscript source, the built PDF, the artifact catalog, the cumulative handoff, the source and application inventories, and the findings ledger together. Their statements about the current result, proof status, assumptions and unresolved work must agree.
- Verify that the PDF was built from the identified source revision and declared build inputs. Compare the source edition, selected build target, output identity and release manifest. Check title, version and date agreement across the manuscript, README, archive index and release metadata. Preserve prior editions in the archive rather than relabeling them as current.
- Describe each construction artifact by the representation actually supplied. Distinguish a full explicit expansion from a symbolic expression, compressed encoding, generator, certificate or sampled output. Ensure the artifact catalog and manuscript make the same claims about recoverability, verification and reproduction. Check the project's required artifact names and inclusion thresholds against the actual files.
- Review citation and credit changes, including the provenance of reused research, independent reviews, computational discoveries and substantive repairs. Keep source-version references and application records synchronized with changes to citations or mathematical inputs.
- Validate release links and their intended targets, including README links, archive entries, source locations, evidence and reproduction entry points. Check immutable identifiers where a link is used as review evidence. Distinguish a current-version navigation link from an immutable release binding, and record access restrictions or unavailable targets.
- If the project maintains public and private mirrors, identify the intended contents and permitted differences for each. Review the selected files for publication scope, publish only with the owner's authorization, and read back each configured destination. Compare the published revision and artifact hashes with the reviewed release manifest. Record the readback results and any outstanding difference. A successful local build, push command or acceptance of one mirror does not establish the contents of the other.

Record who performed these comparisons, the exact files and destinations checked, the results, and any remaining discrepancy. A discrepancy in a required artifact or its stated status prevents declaring the release-maintenance requirements complete. After a correction, recheck the affected files and obtain the corresponding reviewer-authored updated binding under the existing change rules.

### Scope and automated coverage

For a small non-release PR, state explicitly which release-maintenance duties do not apply and why. Identify the artifacts and claims left unaffected, and have the reviewer assess that scope. A documentation, infrastructure or metadata label does not itself establish nonapplicability. A later research release must still perform the complete applicable maintenance and handoff review.

Automated checks must report their actual coverage. A path check, hash comparison, successful build or link check establishes only the property tested. It cannot establish that an archive contains all relevant prior research, that citations and credit are complete, that a representation supports its mathematical claim, or that all objections received review. Record the human or model review of these coverage questions separately from machine-check results.

## Reusable application form

Copy this form for each substantive application. Replace every placeholder; do not interpret an empty field as acceptance.

```text
Application ID:
Claim being justified:
Authors:
Manuscript commit and file hash:
Construction location and excerpt hash:
Application location and excerpt hash:
Consumer locations and excerpt hashes:
Exact source versions and statements:
Dependencies and their mathematical status:
Exact proposed edits and fingerprints:

For EACH of the nine obligations:
  Obligation name:
  Status: addressed / unresolved / not applicable
  Required input:
  Constructed input:
  Derivation or reason not applicable:
  Source locator:
  Evidence file and hash:

Effects on downstream statements:
Exceptional cases checked:
Computational checks and their precise scope:
Remaining questions:

Independent reviewer:
Reviewer type and review conditions:
Decision and exact scope:
Application record hash:
Manuscript hash:
Review report and hash:
Date:
```

## Reusable response form

```text
Finding and version reviewed:
Exact inference questioned:
Earlier evidence searched and historical finding:
Mathematical diagnosis:
Repair or explanation, with source and manuscript locations:
Affected downstream claims:
Independent review decision and scope:
Reproduction results and limitations:
Released commit or version:
What remains open:
```

Use these records to make the reasoning inspectable. The standard for a mathematical conclusion remains a valid argument from its stated inputs; the standard for a review claim is evidence that the specified argument was actually reviewed.

Version 1.1 makes the five completion requirements explicit and adds the final closure review. Version 1.0 remains a separate historical document.

Version 1.2 adds release maintenance, cumulative research handoffs, archive and artifact synchronization, publication readback, and explicit scope and coverage records. Version 1.1 remains a separate historical document.
