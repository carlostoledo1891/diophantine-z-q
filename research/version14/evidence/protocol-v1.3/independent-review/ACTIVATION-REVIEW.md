# Independent v1.3 idle activation preparation review

Reviewer `/root/sol_protocol_final_review`. Author `/root/protocol_v12_acceptance`. November 7, 2026.

Accepted for postmerge activation preparation at CANDIDATE.json SHA-256 `cb11bfc90e06a4099ca81720a0c083a2f95c3438343c25a93c780ae9f3690e9e`, binding ACTIVATION.json `ece0148e3f0c4e378d183c5cfcca4c79f5feecf418caeede6673e9c5dda6dfac`.

I read the preparer and plan, verified every candidate and tree hash, and compared the full tree against actual Git blobs of bc56dd5efa51eaefc3007044c59ba1d063ec8aa8. All baseline paths remain. There are exactly 153 files and 16 changed/added paths. Every file from the separately accepted 129-file integration bundle is byte-identical. All twenty input mappings match the accepted idle overlay, including nineteen unchanged history blobs. The sole configuration change is jobs=[], with the previously accepted configuration hash. Owner README and .gitattributes are retained. The bundle manifest describes actual protected inputs; no v1.3 packet, dossier, profile or receipt is invented.

The seven idle tests passed independently under pinned CPython 3.12.14. The author records 22 idle/profile tests passed. Earlier independent core/runtime reviews and the accepted 642-test integration run apply to identical code bytes, rather than being relabeled as a new execution.

The plan correctly requires both exact v1.2 normal merges and immutable readbacks before deployment. An actual intervening idle commit and final activation commit require exact delta/readback review. An actual guarded idle evaluation must return []. This is readiness acceptance, not evidence that those prerequisites have happened or authorization to deploy early. The subsequent combined Version14/v1.3 release requires substantive coverage and separate actual-target acceptance. No remote mutation or source edit was made during this review.
