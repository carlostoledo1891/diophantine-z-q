# Version 12 integration review

Reviewer: `/root/astra_bl5_models`, 2026-11-07.

I checked the assembled `manuscripts/quartic_v12.tex`, SHA-256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`, against the reviewed Version 11 manuscript and the four edits in `docs/manuscript-revisions/version12/new-edits.json`.

The edits reconstruct the complete manuscript exactly after normalizing line endings. They change the version number, the current quartic summary in the abstract, the version-history introduction, and insert the reviewed proof section before the bibliography. The inserted section equals the independently reviewed addition, SHA-256 `d229ea5c501fd2b61a281172dc8b038b49c2a8838abe6ae7afc92b766cdee800`, up to surrounding whitespace. The mathematical review of that section is `COMPOSITION_REVIEW.md`, SHA-256 `3e67873e47eb463444dcb8844d5d03ae6c4cd45f71728223c695983a6a625d90`.

I read the changed abstract and introduction in the assembled manuscript. The counts distinguish total variables from quantified witnesses, the fixed coefficient parameter from a variable, and the current constructions from the retained historical baselines. The abstract agrees with the new theorem and tables. Direct inspection of `quartics/quartic-514-fully-expanded.txt` gives 690,922 bytes, 24,716 coefficient rows, content one, and largest absolute coefficient `3^2048+1005072314676622`, of bit length 3247. The frozen 498 table and its full expansion were already checked in the composition review. The addition states the 514 table's hash and the unique 16-variable coefficient lift explicitly.

Every reference introduced by the added section resolves to a label in the assembled manuscript. None of its labels is duplicated. Its citations to Silverman and Voight resolve to the existing bibliography entries, and the bibliography is unchanged from Version 11. The addition does not redefine global macros or change an earlier theorem. The version-history sentence that the earlier specifications were unchanged remains within the paragraph about Version 10, while the new paragraph explicitly describes the Version 12 reduction.

The new proof retains the earlier Kato-dependent point-group input rather than replacing it. Each of the five reviewed Kato mathematical/source edits is present exactly once and unchanged in both versions: the construction domain, construction subfamilies, specified Euler subfamilies, index/norm/limiting-class argument, and bibliographic locators. Thus this integration introduces no altered Kato index domain, lattice, scalar, Euler factor, or downstream class identification. Fresh contract metadata still needs its own hash-bound acceptance; the earlier approval must not be copied with a new manuscript hash.

The machine-readable integration observations are saved in `integration-checks.json`. Those checks establish text and table consistency, not the truth of retained external theorems. This review does not enlarge the scoped mathematical acceptance in the composition review or the previous Kato review.

No integration correction is requested for the manuscript hash above. Final application-contract acceptance is separate from this report.
