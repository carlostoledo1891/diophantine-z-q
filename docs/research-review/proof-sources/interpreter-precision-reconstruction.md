# Reconstructing the original interpreter evidence layout

The source map preserves all 34 entries from the original source-pin document. The licensed Silverman PDF is metadata only and is not selected for redistribution. Two source inputs have exact existing repository matches; other required bytes have proposed destinations. Repeated identical inputs may share one destination while keeping every original pin.

The destination paths are evidence-storage locations. These loose relocated files are not claimed to run directly: their code imports and data lookups use the original relative layout.

To prepare a separate reproduction directory after the selection is reviewed, iterate the source map and copy each included destination's bytes to its original `path` under that new directory. Verify the SHA256 and byte count from the original source pin before and after each copy. Reject absolute original paths, `..` components or targets outside the reproduction root. Where two original paths map to the same bytes, create both original relative paths. Preserve the original report and original source-pin document unchanged beside the map.

For the licensed paper, use the source hash and the report's printed/PDF-page locators to identify an independently obtained legitimate copy. Its absence from the public handoff does not authorize substituting a different edition or claiming its source-version comparison was repeated.

Run any reconstruction checks only from the restored original layout with the original report's stated dependencies and scope. This proposal contains no new successful execution claim for those programs. Source identity, natural-number semantics, historical mathematical imports and finite execution remain distinct audit questions.
