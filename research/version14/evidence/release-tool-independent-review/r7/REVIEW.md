# Independent R7 literal-file exception review

Reviewer `/root/sol_protocol_final_review`. Author `/root`. November 7, 2026.

Accepted the narrow packaging repair at MANIFEST.json SHA-256 `f92a6b5adda0cace9f68c2564e0279a79800b5f3f8d12eeb8f56999bf6408af3`. I verified all manifest hashes and byte lengths and confirmed all inherited R6 executable files other than package_v14.py remain exact.

The copied exception map is byte-identical to my independently reviewed five-file map at SHA-256 `709881ac53aaf6b1013d06e00f668dff1664753e1d4dc708767058010ff5a15a`. The packager binds that digest before interpreting the map. It accepts a marker-bearing file only when its exact destination, whole-file SHA-256 and byte length all match an entry. The ordinary marker-free path and default marker rejection are unchanged. No file-type-wide, quote-based or caller-selected bypass is introduced. The selected Git blob still passes the ordinary reviewed selection pin before the marker check. The annex validator and all other packaging restrictions remain unchanged.

All37 tests passed independently under pinned CPython3.12.14 in26.855 seconds. The eight added tests check the five exact originals, changed bytes, appended key-like blocks, an unlisted destination, arbitrary Python marker literals, key-like bytes at an allowed destination, changed exception-map bytes and ordinary marker-free data. The key fixtures are synthetic. The code rejects them on exact byte mismatch without requiring a key parser.

This acceptance covers the R7 tool and its fixed exception map, together with the already reviewed exact historical scanner files. It does not accept the remaining direct-history selection, actual final archive, current registry, coverage dossier or public/private release. No repository, frozen source or remote was changed during this review.
