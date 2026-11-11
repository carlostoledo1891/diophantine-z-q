# Independent protected runtime integration review

Reviewer `/root/sol_protocol_final_review`. Author `/root/protocol_v12_acceptance`. November 7, 2026.

Accepted runtime integration at runtime-r2/CANDIDATE.json SHA-256 `0b6b4e963caa608090140734658f316ab28ced90c735423180129c7349fbf96c`. Runtime SHA-256 is `fd1f167f983dcb0ef262af95126dadf1d42a6c3b6b9c22707c974fbf0286a410`; test module is `a89f9216e91c232fad630b10ac265621cdb12e1ec013b73b1e02c5b350496dbc`.

I independently checked every candidate manifest file and all eight inherited gate hashes, including the separately accepted coverage validator. The recorded baseline runtime matches actual current source bytes at `be8dd9c490f1e8f0c03ff8ece6ed95a3b4b9b1f49f2496a3ae8f17b644753759`. I inspected the full delta and relevant surrounding protected loader, evaluator, runner and main loop.

The optional coverage_profile is an inline object in protected job configuration. It is not loaded from a candidate-controlled path or field. load_job rejects invalid selection and retains its established four-value interface. main passes a deep copy into evaluate; evaluate independently validates and copies it before restoring state or constructing the publisher. ForkProtocolRunner retains a copy and supplies another copy to the accepted live evaluator and ledger bridge. The dossier subsequently binds the exact profile digest and receives its own authenticated coverage decision.

Missing v1.3 profiles, changed governing/runtime identity and unsupported versions fail. Candidate packet fields cannot override protected configuration. Legacy selection remains explicitly legacy-scoped. The empty-job branch still verifies the controller revision before success and needs no App or ledger key. Existing source, ledger, generation, current-intake and publisher checks remain in place.

The 22 focused runtime/profile/idle tests passed independently. They exercise actual protected JSON reading, main, load_job, evaluate and runner propagation through explicit test doubles into the real structural validator. Their mock publication result is synthetic, not a live success. Full combined independent test results are recorded in RUNTIME-TESTS.json. Root deployment and an actual job profile/packet/selection remain separate integration targets requiring review.

This decision covers the reusable runtime change. It approves no actual future profile scope or packet evidence and authorizes no deployment. Earlier component, documentation and builder decisions remain separate. No implementation or production file was edited during this review.
