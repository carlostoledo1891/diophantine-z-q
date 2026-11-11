# Independent review of the assembled v11 Kato repair

Reviewer: `/root/astra_bl5_models`.

Reviewed artifact: `work/quartic-version6-release/repository/manuscripts/quartic_v11.tex`.

SHA256: `1210d2e6f409e502fc9c95afc248fac16a9df48c760a396143780c20ec80b662`.

Verdict: the exact assembled changes close the Issue 2 Kato indexing and retained-class-identification gap. No mathematical correction to these changes is requested. This review is limited to that repair; it is not a certification of the whole manuscript.

## Exact changes checked

I read all six entries of `docs/manuscript-revisions/version11/edits.json` and the actual corresponding passages in the assembled TeX. Applying the six replacements to the pinned v10 file reconstructs v11 exactly, with each old passage occurring once. This was checked independently by literal string replacement, not inferred from the edit manifest.

The new K8 domain at lines 12398–12414 includes every positive m prime to c d_s. The source hypotheses for these classes hold by K5 and d|F. The text correctly retains the original 2004 index set as a subfamily and does not call the whole enlarged family a section-13.1 Euler system.

Lines 12689–12710 correctly choose N_K=2Nd and N′_K=c d_s, distinguish construction support from inverted arithmetic support, and carry the fixed lattice map into the full cohomology groups. The two cases cover every prime allowed by Kato 1999 (0.1.1). A newly introduced prime cannot divide 2Nd; consequently the good-prime polynomial displayed there is valid. Its substitution gives K9 exactly, with the inverse deck action, trace a_l χ(l), determinant l, and unchanged quadratic coefficient after twisting.

Lines 12712–12743 correctly distinguish Kato's divisor parameter d=1 from the odd conductor part d and distinguish ξ_K from the modular-symbol combination ξ. Both supports are prime(2Nd). Proposition 8.12 therefore has an empty Euler product in the displayed inner norm. The fields in that norm and in K8 lie in Q(ζ_{DN_K2^n}); transitivity through its two intermediate fields gives precisely the displayed y-class identity. Tensoring commutes with the inner norm because χ is trivial over Q(ζ_{D2^n}). No restriction–corestriction identity, trace normalization, projector division, degree scalar, or hidden factor of two is used. The equalities hold for n≥1, independently of the later optional simplification of the dyadic conductor; this is a cofinal tail for the inverse limit.

The last paragraph explicitly handles the sole permitted fixed scalar: if the lattice map is needed, ξ_K is the full-cohomology image of 2^{c_E}y_{2∞}. At the stated height-one primes this multiplier is a unit. Thus its coordinate ideal is the same localized J, without asserting an unscaled integral equality when the lattices differ. The retained smoothing factors are never divided out.

## Primary evidence

The independent source checks and full norm computation are recorded in `SOURCE_AUDIT.md` in this directory. Kato 1999 §§0.1, 0.4–0.7 and Theorem 0.8 were read in the local primary extraction, with printed p.318 also visually inspected. Kato 2004 printed pp.180, 186 and 224 were visually inspected. The hashes of the primary PDFs are:

- Kato 1999: `483dc18c56b2fe9cfac4e37f2e6594399625c3f0ea98a05bb69116377c67fc06`.
- Kato 2004: `3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d`.

The subsequent interface and norms reports were read as cross-checks after the independent source computation. Their conclusions were not substituted for primary verification.

## Acceptance boundary

This decision applies only to the hash above. It does not authorize manuscript or GitHub edits by this reviewer.

I also read and accept the scoped application contract `docs/manuscript-revisions/version11/kato-application.json`, SHA256 `bb725ef321d28b2cdfeac64fa86deb864c09590d49e5fe05b9bdb95f73986e0b`. Its nine obligations accurately state this repair and its unchanged dependencies. I independently verified the manuscript hash, all three line-span hashes, both cited evidence-file hashes, and all five mathematical/source-edit hashes. The last use sorted-key compact JSON for each complete edit object, as specified by the review protocol. The administrative version-title edit is outside the mathematical contract.

The construction, application and K15 consumer spans were all read in the exact assembled artifact. The existing nonvanishing proof, representation-theoretic inputs, and full/j_* local-complex comparison are unchanged dependencies; acceptance here checks the repaired class and indexing interface they consume, and does not claim a fresh independent proof of those unchanged arguments. No additional mathematical assumption is introduced by the repair.
