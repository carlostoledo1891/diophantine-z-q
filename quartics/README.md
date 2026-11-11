# Quartic polynomial tables

The filenames identify how the coefficients are written:

- **`fully-expanded.txt`** lists every nonzero monomial with its coefficient written out as a decimal integer.
- **`symbolic-coefficients.json`** also lists every nonzero monomial, but expresses some coefficients using a specified fixed integer `S` or `C` (the exponent depends on the construction). Those coefficients are exact; their full decimal digits are not written out. Neither constant is an additional variable.

All variable counts include the input. Each download below is a byte-identical copy of the table in its linked verification package.

| Variables | Polynomial table | Coefficient format | Verification package |
| ---: | --- | --- | --- |
| 299 | [quartic-299-symbolic-coefficients.json](quartic-299-symbolic-coefficients.json), [text](quartic-299-symbolic-coefficients.txt) | Exact coefficients, `C=3^(2^25)` | [Version 14 guide](../docs/manuscript-revisions/version14/GUIDE.md) |
| 314 | [quartic-314-fully-expanded.txt](quartic-314-fully-expanded.txt) | Fully written decimal integers | [Version 14 guide](../docs/manuscript-revisions/version14/GUIDE.md) |
| 394 | [quartic-394-symbolic-coefficients.json](quartic-394-symbolic-coefficients.json), [text](quartic-394-symbolic-coefficients.txt) | Exact coefficients, `C=3^(2^25)` | [Version 13 guide](../docs/manuscript-revisions/version13/GUIDE.md) |
| 411 | [quartic-411-fully-expanded.txt](quartic-411-fully-expanded.txt) | Fully written decimal integers | [Version 13 guide](../docs/manuscript-revisions/version13/GUIDE.md) |
| 498 | [quartic-498-symbolic-coefficients.json](quartic-498-symbolic-coefficients.json), [text](quartic-498-symbolic-coefficients.txt) | Exact coefficients, `C=3^(2^25)` | [Version 12 guide](../docs/manuscript-revisions/version12/README.md) |
| 514 | [quartic-514-fully-expanded.txt](quartic-514-fully-expanded.txt) | Fully written decimal integers | [Version 12 guide](../docs/manuscript-revisions/version12/README.md) |
| 523 | [quartic-523-symbolic-coefficients.json](quartic-523-symbolic-coefficients.json), [text](quartic-523-symbolic-coefficients.txt) | Exact coefficients, `S=3^(2^26)` | [Version 9 guide](../docs/quartic-523-540/README.md) |
| 540 | [quartic-540-fully-expanded.txt](quartic-540-fully-expanded.txt) | Fully written decimal integers | [Version 9 guide](../docs/quartic-523-540/README.md) |
| 962 | [quartic-962-symbolic-coefficients.json](quartic-962-symbolic-coefficients.json) | Exact symbolic coefficients | [Version 6 guide](../docs/quartic-962/README.md), [package](quartic-962/) |
| 1,272 | [quartic-1272-symbolic-coefficients.json](quartic-1272-symbolic-coefficients.json) | Exact symbolic coefficients | [Version 5 package](quartic-1272/) |
| 4,973 | [quartic-4973-fully-expanded.txt](quartic-4973-fully-expanded.txt) | Fully written decimal integers | [Version 4 package](quartic-4973/) |
| 9,625 | [quartic-9625-fully-expanded.txt](quartic-9625-fully-expanded.txt) | Fully written decimal integers | [Version 3 package](quartic-9625/) |
| 12,504 | [quartic-12504-fully-expanded.txt](quartic-12504-fully-expanded.txt) | Fully written decimal integers | [Version 2 package](quartic-12504/) |

The 314-variable decimal table has 6,672 monomials, occupies 264,430 bytes and has coefficient magnitudes below `2^6496`. The 299-variable symbolic table has 6,630 monomials.

The 411-variable quartic is the Version 13 decimal companion. Its text table occupies 214,957 bytes and has 6,388 monomials, with coefficient magnitudes below `2^3247`. The 394-variable symbolic table has 6,338 monomials. The current manuscript gives both defining properties while retaining the original construction and earlier proof baselines. The new text downloads are lossless reformattings of their package JSON tables; the reproduction command compares every coefficient.

The Version 13 tables number all coordinates consecutively from 1, with `x1` the input. Their rows use `coefficient | C exponent | variable indices`: `-6 | 0 | 1,3,3` denotes `-6 x1 x3^2`. The middle field is zero throughout the 411-variable decimal table. The [package](quartic-394-411/README.md) includes exact maps from the source coordinate IDs.

The historical 498/514-variable text tables use `coefficient | C exponent | variable indices`. Thus `-6 | 0 | 0,2,2` denotes `-6 X_0 X_2^2`; the middle field is zero throughout the fully expanded decimal table. A row with no variable indices is a constant term. Older packages may use whitespace-separated coefficients and repeated indices. Each table's header and package guide state its format.

The package directories retain their existing names because the source inventories, certificates and reproduction commands refer to those paths.
