# Version 14 artifact index

These are the current manuscript and research artifact identities. The cumulative archive preserves the source revision recorded in its manifest; subsequent delivery documentation and its release checks have their own revision.

| Artifact | Repository path | Scope |
| --- | --- | --- |
| Main TeX | `manuscripts/quartic_v14.tex` | November 9, 2026 source |
| Main PDF | `manuscripts/quartic_v14.pdf` | 323 pages |
| Merged GI PDF | `research/version14/proofs/local-gi-v1/GI-SUPPLEMENT.pdf` | 106 pages: original 103, delivery guide and Section 13 addendum |
| GI PDF alias | `manuscripts/quartic-local-gi-supplement.pdf` | Same bytes as the merged GI PDF |
| Standalone GI archive | `research/version14/proofs/GI-PROOF-ONLY.zip` | Separate proof-only delivery, not nested in the cumulative archive |
| Research annex | `research/version14/z-in-q-version14-research-annex.zip` | 1,939 logical records, 1,643 distinct content objects; 10,265,610 bytes |

SHA-256 identities:

```text
main TeX       5882a77003b9772b5b572a5ab2c2b2f8ce9fc53e1e368a3b69851c8a9b3bfcac
main PDF       7107f98b3f003aac9d307c9f88c5813aff184f131fde8a0d7536b71817789650
GI PDF/alias   c971bcad7a269f8bd4cd18102d62cd8d61b801d9c4439d729457f37721e7228a
GI archive     581aa968e1c54cf78a16e47b18e981012c5b29eeb6da2e0c115b56fb7276156b
GI manifest    4b5e400758f6fc3e9ad1a07f06e2ac0a222f70a067e7726922b5857914083eb0
research annex 54e7aec54df9c1bd9bed0b02cd22a9a41ae3fb7717d12107ff72dd0700a2cd51
```

The main PDF is 1,835,219 bytes. The [complete proof-source index](PROOF-SOURCE-INDEX.md) identifies all 136 selected proof-source files; its SHA-256 is `0b0930de27e7c460bb98a63359d6e971cbbb607c7f07f44dfef68b6d1e256dac`. The [supporting-notes guide](SUPPORTING-NOTES.md) has SHA-256 `4e85619afbf17a48f872c4a441204a73928160bf565fc56c6568b3253f0a80b1`.

The accepted final source-collection snapshot has manifest SHA-256 `e3bac2e4887f5fda951468cd1994fffafe420a6dc5c1aeaad60ff2a99c2126d5`. Its seven-root mathematical review is `351f75cf54f3607150069e16c1e716f77cb5f7fbcdde23cb33e02ffef27162fd`; the separate cumulative-transport and source-representation review is `0dcb2c2eabe7a17fed695633f23a4654b55e08752f5e19da5037616fb349547c`. These are scoped source-review identities, not authenticated release-gate or publication receipts.

The GI manifest is `PROOF-ONLY-MANIFEST.json` inside the standalone package. Its membership describes that package, not a smaller cumulative selection.

The coefficient tables below are in `quartics/quartic-299-314/`.

| Table | Variables | Monomials | Bytes | Input coordinate |
| --- | ---: | ---: | ---: | --- |
| `quartic-299-symbolic-coefficients.txt` | 299 | 6,630 | 228,028 | `x1` |
| `quartic-314-ordinary-coefficients.txt` | 314 | 6,672 | 264,430 | `x1` |
| `quartic-314-source-id-coefficients.txt` | 314 | 6,672 | 222,890 | `x0`, preserved source IDs |

```text
299 text       e7f00ae1c0643cb31b93c28ea88e30c3b1790ace718625bb5e223b91e2b101ba
314 text       57d44e10a92cda1ffac29f46a54282f855882bcf21760c3419df62dc8c673822
314 source IDs efb34a9664a3a2c5b0abe548463e646ba18d6f7e5ab5d9eff9e80bb8b461291e
package        5369f80f69742958ea31f3a32b62b43e6b23b284063e6870af2dc2f0073977fb
```

The package identity is its `PACKAGE-MANIFEST.json`. See `ARTIFACTS.json`, `ACCEPTANCE.json` and the coordinate maps for the JSON tables, exact maxima, and distinctions between accepted and rejected history. Finite checks verify these constructions and serializations; they do not replace the retained arithmetic premises.

The [cumulative archive](https://github.com/elliotglazer/diophantine-z-q/releases/download/quartic-299-version-14/z-in-q-version14-supplement.zip) is 221,978,813 bytes, with SHA-256 `6025a0af2835a239c5dcd03f4aa4f8987f16c0fb5a7deae7f49089aefaf7ec9d`. It was built from `ceb028b95dd5d485586baa824badf0eb856567cb`. See [RELEASE-RECEIPT.json](RELEASE-RECEIPT.json) and [CUMULATIVE-HANDOFF.md](CUMULATIVE-HANDOFF.md) for the archive and source-gate bindings.
