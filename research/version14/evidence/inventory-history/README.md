# Version 14 inventory preparation component

This bounded authoring component prepares the selected299-symbolic/314-ordinary
inventory. It preserves the frozen R6 research inventory and distinguishes the
24-IR assembly history from the current proof-use map. There are39 baseline
application identities,351 obligations and263 R6 edges to reconcile.

`BASELINE-ADAPTATION.json` gives a comparison note for each baseline application.
The notes identify retained inputs and changed constructions, including all-E
auxiliaries, zero-safe log identities, global N/Q use, same-place denominator
recovery, oriented root reconstruction and the constructive anchor choice.
They are author notes, not completed current application records or approvals.

`route.py` produced `ROUTE-SELECTION.json` from the immutable R6 graph. It records
32 candidate current entries and185 candidate current edges,31 supporting
edges, and47 archived edges. Final source/consumer mappings must justify which
candidate edges are actually consumed. No claim is made that all263 edges
appear in the final manuscript. Rejected299 and unused ordinary/root-weighted
branches remain in the artifact archive and retain their statuses.

`install_inventory.py` is a working staging installer with a portable validator
in `inventory_core.py`. It requires the final authored records and contract;
there is no permissive fallback. `INPUT-CONTRACT.md` specifies the required
files and every record field. The final addition and all351 current obligation
statements/spans are not fabricated by this packet. Therefore this directory
contains no final APPLICATIONS.json, current registry or acceptance record.

Run the checks from this directory:

```text
python -B verify_preparation.py
python -B -m unittest -v test_inventory.py
```

The first checks actual frozen sources and selected artifacts. The second uses
explicitly synthetic current prose and artifact bodies to test validation and
installation failures. Its success is not evidence that the final mathematical
claims are correct. `CHECKS.json` records the replay. Once final inputs exist,
run the installer, then obtain independent structural and mathematical review
of the exact final records and source spans before registry integration.

The supplied schema keeps the prior source catalog unchanged and pins the
current selected artifacts. Any actual change to those inputs or to the route
classification needs a preserved successor packet and review. The interpreter
is Python with only the standard library. No network, GitHub or production
repository mutation is performed by this component.
