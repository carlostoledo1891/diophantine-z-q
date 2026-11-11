# Application-review protocol audit

Date: 2026-11-07. This is a structural code review, not acceptance of a mathematical proof or of a not-yet-created release record.

I read `scripts/check_application_reviews.py`, `scripts/check_audit_history.py`, `docs/audit-history/PROTOCOL.md`, and `AGENTS.md` in `work/quartic-version6-release/repository`. The final application-checker revision tested here has SHA256 `8f42eba870fc3f364b637478b0116d240a8f031f80284f205a81a408a687da47`. No shared repository file was edited by this reviewer.

## Two coverage gaps found and repaired

The initial displayed implementation allowed a nonadministrative edit to cite any existing contract, without binding that edit's actual old/new text to the contract. Binding the whole manuscript did not establish that a scope-limited contract reviewed the extra edit. I requested either positional span coverage or a separate explicit exact-edit binding. The updated implementation requires each contract's `reviewed_edits` dictionary to equal the IDs and hashes of all edits assigned to it. Changing that dictionary changes the contract hash and invalidates the approval. This is an adequate explicit binding; it does not require each change to lie within one of the three representative spans.

The initial follow-up check only required a nonempty list. Omitting the latest finding while keeping an older one would pass. I requested a pinned authoritative snapshot and exact required-finding comparison. The updated implementation reads a pinned snapshot, requires the latest comment in its required list, and compares the ledger's URL set with that list. It now rejects deletion of one required finding while an older finding remains.

`protocol_counterchecks.py` is an in-memory test of these two interfaces. It does not alter repository files. Against the hash above it produced:

```text
Positive fixture accepted with exact reviewed-edit binding.
Unbound edit rejected: Contract does not explicitly review these exact edits: c
Dropped follow-up rejected: Follow-up ledger omits or changes a required source finding
```

The first negative test supplies a freshly rehashed approval but removes the per-edit binding. It therefore checks the new coverage condition rather than merely relying on a stale hash rejection. The second test keeps the pinned snapshot and deletes only the newest required ledger entry. The test fixture is synthetic; no current-release JSON existed when this review began, so these results are not represented as a successful release validation.

## Properties checked by inspection

* The nine obligation names are mandatory and exact. Each has required/constructed/justification text plus known evidence and source references. `not_applicable` still needs a justification and an independently accepted contract.
* Bound evidence files and manuscript spans are hashed. The contract itself and the separate approval are hashed. Approval names the exact contract and manuscript hashes, a report, a scope, and a reviewer distinct from all listed authors.
* Revision edits reconstruct the complete current manuscript from the pinned baseline. Unlisted text changes fail. Administrative changes are restricted to the exact version/date syntaxes. All other changes require exact per-edit contract bindings.
* The old checker still validates the nine historical entries against the v10 source. Carry-forward is explicitly historical, and unchanged passages must retain their exact bytes. Fresh acceptance is separately required for the changed route.
* The existing entry point invokes the current checker after the legacy checker, so a historical PASS does not skip current-application validation. Missing `current.json` fails rather than silently accepting the old record.
* The checker only reads approvals; it contains no path that generates an accepted decision or automatically refreshes a reviewer fingerprint. The self-tests intentionally manufacture altered in-memory fixtures, not release approvals.

## Limits to retain in reporting

Primary-source URL/version/locator/hash fields are bound metadata. The checker validates their format and their membership in the contract, but it does not download the primary source and compare its bytes. Locally pinned evidence is checked byte-for-byte. Thus "source fingerprint binding" must not be reported as a new remote-source download/verification.

A pinned issue snapshot cannot establish that GitHub has acquired no later comment. Refreshing the snapshot before a public response remains a human/tool workflow requirement. The new exact-set test prevents dropping required findings from that snapshot; it is not a live issue monitor. The required-finding selection and the claim that an older comment needs no separate treatment remain reviewer judgments.

The script cannot authenticate author/reviewer identities, prove that a reviewer actually read the sources, or detect an intentionally misleading accepted justification. These are already acknowledged in the protocol. Changing reviewer-authored approval files simply to refresh hashes remains forbidden by the workflow; the script is not a cryptographic signing service.

Unchanged text can acquire different dependencies after another edit. The carry-forward impact assessment is required but its mathematical truth is not computable here. The protocol correctly requires a reviewer to assess that effect and does not turn byte identity into fresh whole-proof acceptance.

## Disposition

The two concrete structural gaps found in the initial displayed code are repaired in the tested revision. Within its stated scope, the implementation is suitable for checking binding completeness and stale records. Final release validation must still run against the completed real record and the final file hashes. This review supplies no automatic mathematical acceptance and no blanket approval of future revisions.

## Final frozen-record execution

After the root agent announced the freeze and supplied `current.json`, I independently ran the actual entry point with `--self-test`. It exited zero and reported all nine historical dispositions checked, seven historical negative controls rejected, nineteen application-review negative controls rejected, and one current application contract checked. The script and manuscript hashes remained those stated above.

I also read the final real `kato-application.json`, `acceptance.json`, and the relevant current-record entries. The application contract explicitly binds the five nonadministrative edits. Its authors include the drafting agents, while the acceptance names `/root/astra_bl5_models`, who is not among those authors. The acceptance scope is limited to index coverage, norm transitions, factors, lattice scalar and retained-class identity. Unchanged nonvanishing and local-complex arguments are explicitly dependencies, not newly accepted whole-proof conclusions. The source-byte and historical-carry-forward limitations are printed in the real record.

These final runs supersede the earlier statement that no release record was available at the start. They establish structural validation of this frozen record, not correctness of all manuscript mathematics.
