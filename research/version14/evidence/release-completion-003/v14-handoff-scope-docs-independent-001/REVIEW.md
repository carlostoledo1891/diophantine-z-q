# Independent reduced-GI handoff and documentation review

Reviewer: /root/v14_integration_review. Decision: ACCEPT the exact reduced-GI controls and three handoff documents below for integration. This is bounded packaging/documentation acceptance, not final archive, mathematical, or authenticated-gate approval.

## Reduced GI controls

Accepted proposal MANIFEST.json: e426ea4698e01ca607e833d0f9a0a44954ef4cd24d8943974dd5b73bb716db3d in ../v14-gi-handoff-scope-001. Its CUMULATIVE-HANDOFF.json is ff99cb9a8c1e1b12506e0c82195c4a522851e01f892958fe66d187339801fea1; verify-handoff.py is 62e73cbc5df9fe52ce7ea4d93f2a440076ce75212ba223aa7f42bc91cf1dc1b2; explanatory note is 87664d96d331338cc79edc23d6e8b84d6ba9fcd2bf8de9234305d01c24593e96.

I read the full generator, wrapper, note, outer manifest, and CHECKS.json. I independently compared the partition with the original full manifest: exactly 279 retained and seven omitted members, disjoint and exhaustive over all 286 original files. All 286 source-file hashes matched, and each omitted PDF's exact retained TeX counterpart matched. I ran the actual fixture verifier with the bundled Python; it passed the exact-file-set check with 279 retained members and seven exclusions. I reviewed the author's negative controls and results for missing/changed retained content, extra files and a reintroduced excluded PDF; they reject those cases, restore the fixture, and show that the unchanged full verifier fails exactly on the seven deliberate omissions. Those negative runs are author evidence, not represented as my own runs.

The omitted members are the guide PDF and six historical PDFs, with the standalone proof ZIP recorded separately outside the GI directory. Seventeen approved current GI PDFs remain here; the eighteenth approved project PDF is the merged alias under manuscripts. The main PDF remains separately governed. Existing release guards are unchanged. The wrapper pins the handoff manifest, which pins the original full manifest and retained content; its own identity is supplied by the outer proposal/selected-file pin, not by a self-hash claim. Its scope is this reduced GI directory. It does not validate the external ZIP or authenticate a gate.

The explanatory note correctly distinguishes full and reduced verification, preserves original full-manifest bytes, and does not claim turnkey or byte-identical reconstruction from the reduced copy. These controls must travel with the reduced selection. The original verify.py remains a full-package verifier and is expected to report the seven missing PDFs here.

## Three handoff documents

Accepted files in ../v14-handoff-docs-003:
- README.md: e2e976e4719459768127ec38d26a6e5f5e04b19162e38dbf29e99f98e6542fc1.
- ARTIFACT-INDEX.md: 8b6852c8646a7527bc9fcd1d599816b32c627158471b8e972fabc5407335ad1d.
- CUMULATIVE-HANDOFF.md: 451338efd5849d5726100544ea308285818bb6e438ffdb7d21f29b6ea6dd69e8, including the added explanation that restore preserves rather than expands the research annex.

I read all three documents and the exact added paragraph supplied by root. All Markdown links resolve from the proposed research/version14 location, using the candidate files for new sibling documents. The intentionally excluded standalone ZIP is described as a separate delivery without a dangling cumulative hyperlink. Main/GI identities match the previously accepted exact artifacts. I verified the three coefficient text hashes and sizes against actual repository files and PACKAGE-MANIFEST.json hash 5369f80f69742958ea31f3a32b62b43e6b23b284063e6870af2dc2f0073977fb. ARTIFACTS.json agrees with the stated variable/monomial counts, input-coordinate distinction and coefficient bound; ACCEPTANCE.json records the separate construction/serialization acceptances. This reuses those mathematical decisions rather than independently re-proving them.

Actual CUMULATIVE-INTAKE.json hashes to e554a9051acbf8716c8a3d328a58254ef4d8e9edcd4ed0c7a862e8c8fde6cefe and contains 1,939 file rows. The document correctly labels this a proposed logical intake, not a finished ZIP count or theorem-acceptance count. O4-COMPANION-INDEX.json agrees with the damaged-draft and three-companion hashes and the warning that the readable successor also narrows the mathematics.

I read restore.py: it accepts exactly one output-directory argument, refuses an existing directory, materializes selected current files, and does not expand the research-annex ZIP. The documented command python -B restore.py NEW_DIRECTORY is correct; no unsupported --help invocation remains. Post-freeze source-commit, archive, final-input and authenticated-gate identifiers stay pending in committed prose and are assigned to external final records, avoiding a self-reference cycle. The final archive remains explicitly unassembled. No missing final gate or source binding is represented as already complete.

## Remaining integration obligations

Include the exact reviewed controls in the reduced GI selection, preserve the independent full package, and verify the selected/restored file set after final assembly. Preserve the exact PDF allowance and existing source/provenance requirements. Final cumulative membership, archive digest, selected source commit, external final-input/source-map records and actual authenticated gate remain root's separate work. There are no required changes to the reviewed candidate text.
