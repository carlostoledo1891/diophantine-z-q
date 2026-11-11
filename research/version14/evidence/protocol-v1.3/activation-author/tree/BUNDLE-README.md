# Curated controller deployment staging

No commit or push is performed by this staging tool. Runtime and ingress
use only the files marked production and workflow in BUNDLE-MANIFEST.json.
Test-only files contain synthetic observations and fake HTTP transports.
They are never production observations, receipts, configuration or packets.

Protected config and packet overlays must be supplied by the owner. This
tree does not contain credentials or a copy of remote protocol-state.
The bootstrap record documents an earlier observation, not a live read.

Runtime smoke test: from controller/, run python -B -m unittest
test_runtime test_ingress test_git_state -v. Full transport tests run
separately from publisher/ and require the locked cryptography dependency.
