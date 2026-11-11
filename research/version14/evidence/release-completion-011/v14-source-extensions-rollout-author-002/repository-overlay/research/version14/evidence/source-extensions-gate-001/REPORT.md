# Additive source reconstruction: isolated proposal

Author: /root/v14_h6_coverage. This is an implementation proposal, not independent acceptance or deployment.

The existing substantive coverage validator requires the initial source list to equal the final proof list. This preserves the existing path and adds an explicit version 1.4-only extension path. The original initial file is neither rewritten nor replaced. Its continuation still binds its original source list. Ordered disjoint supplements account for added proof files, and the concatenation must equal the complete final source list exactly.

## Record schema

An optional nonempty source_extensions array belongs to the substantive protocol-coverage/v1 dossier, only under a version 1.4 protected profile. Each member has exactly: schema (protocol-source-extension/v1), original_initial (the original dossier.initial pin), sources (nonempty ordered added head pins), initial (head pin to protocol-source-first/v1 with exactly schema/sources/uses), initial_passages (head pin to an array), and reconstruction. Each passage has exactly id, location, use_ids, reason. Locations retain the existing exact raw-byte line/hash schema. The initial source snapshot's use fields are unchanged.

reconstruction retains run_id, method, prior_exposure, limitations, frozen_at, compared_at and optional existing protocol-review-continuation/v1 continuation. The supplemental initial and its passage table are both frozen evidence named by the signed final dossier; the actual freeze receipt and operator review must establish that these are the real frozen bytes. The validator does not read a wall clock or prove historic freezing. Supplements must freeze no earlier than the original freeze and strictly before their own fresh comparison. Prior familiarity is permitted and must be disclosed; no blind-review claim is imposed.

## Preserved controls

Each supplement uses the authenticated final reviewer or an explicit authenticated same-agent continuation. All ordinary and coverage authors remain excluded. No new model eligibility mechanism is introduced: authenticated run admission and protected runtime policy remain the existing boundary. Unknown or different-agent continuation identities are rejected.

Original sources cannot be replaced through a supplement, source paths cannot overlap, and original or supplemental use IDs cannot collide. Supplemental passages cover every raw line of every added source. Each initial use is linked bidirectionally to its own supplemental passages. All supplemental uses join the original before-set: removals, migrations and changed assertions require the existing exact before/after hash and resolved-history reconciliation. Final proof_paths, full-line coverage, claims, source and supplier hashes, application dependencies, connection checks and signed receipt checks are unchanged.

A favorable review alone is insufficient. This implementation does not accept existing author mappings as a replacement for a genuinely source-derived supplemental initial snapshot. It also cannot prove source completeness, truthful exposure or mathematical correctness: those remain explicit reviewer attestations. The source index and original 92-source freeze are not edited here.

## Validation

164 tests pass across test_source_extensions, test_coverage_gate, test_connections_gate and test_review_continuity. Tests include the unchanged 1.3/1.4 routes, additive success, preserved original continuation hash, exact union order, missing/duplicate/changed source rejection, stale initial pin, original-source substitution, duplicate/missing/displaced uses, both initial and final line omissions, explicit removal reconciliation, missing exposure, false chronology, v1.3/nonmath rejection, and authenticated unknown-run/different-agent/author-agent rejection. Ephemeral fixture keys are synthetic and are not real review evidence.

Run from an isolated copy of deployment-repository with the two overlay files applied: python -B -m unittest test_source_extensions test_coverage_gate test_connections_gate test_review_continuity (working directory adapter). The local-only test runtime copies adapter and gate so existing relative fixture imports work. It is not part of the proposed deployment. TEST-OUTPUT.txt records the actual run.

Only overlay/adapter/coverage_gate.py and overlay/adapter/test_source_extensions.py are proposed changes. No active controller, canonical proof, protected profile or deployed test file was modified. Independent code review and any deployment remain separate.
