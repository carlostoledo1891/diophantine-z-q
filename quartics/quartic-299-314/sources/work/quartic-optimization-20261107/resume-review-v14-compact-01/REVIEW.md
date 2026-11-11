# Independent compact-coordinate artifact review

I accept the frozen compact-coordinate renaming and coefficient serialization identified below. Both compact systems and both canonical tables are exact transports of their separately accepted source artifacts. No correction was needed in this frozen artifact subset.

Reviewer: agent01. I authored the underlying299 construction and earlier constant-chain work, but did not author this compact renaming or serialization. This review covers only the new bijections, literal equations, coefficient transport, table encodings and associated counts, bounds and bytes. It does not renew mathematical acceptance of my source construction, review the assembled Version14 exposition, or authorize publication.

## Reviewed bytes and source decisions

The frozen subset is in `work/quartic-v14-prep/quartic-299-314`. Its `ARTIFACTS.json` SHA256 is `4ad263949b42d7bc5c306f68a168f4375275271e4bf649225b9479340cbe67af`. The producer `work/quartic-v14-prep/package_v14.py` is pinned at `d638a7251a6540aeacf31b2cb66d457589f1d5dd3e010c9c94b3fc6d5b1b5af6`. I read the producer but did not execute or import it. My checker verifies every artifact listed in this manifest and rechecks the same bytes afterward. Later packaging additions outside this frozen subset are not approved here.

The symbolic source IR is `8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815`, with polynomial `e208b503cad67bb53eb42fd78e64b3ebe9e99223692af91dd6c6b5b5b405ca3c`. Its independent source review is `f51b3e1f571820f2d3b5bf6fb7b60e8b3a7506457bca0a72cbd3a3cfd8feb699`.

The ordinary314 source IR is `02b8b6a8b13a566ef520c7a65ec58fd6e63bafa9d7d447e323864b1bae29a5f7`, with polynomial `2ea9fb17223a2e2a4fbf98f113d9e0e1da7019a74f4d2c7cefdb31e5b4637028`. Its independent transport/table review is `13ed2acad2b751abfdb8000a931e6f93bd41b038a965f38c4c2d4902c17318db`. Those exact reviews remain the mathematical and ordinary-lift inputs. The source-ID IRs, polynomials, ordinary text and ordinary certificate copied into the reviewed subset are byte-identical to their source files.

## Bijection and literal equation checks

For each system, sort its distinct source coordinate IDs increasingly and map the j-th ID to j+1. My checker derives this map independently from the actual source IR. It verifies both serialized map directions, their exact inverses, the complete range1..299 or1..314, and source input0 mapping to compact input1. Every coordinate is declared and occurs. The compact coordinate records retain the source metadata and add the actual source ID.

Every residual is compared term by term with the coordinate permutation of its source residual. All row IDs, names and other row metadata remain unchanged. Applying the inverse map restores every source residual exactly. Every other top-level datum is unchanged apart from the explicit coordinate convention and the ordinary fixed-constant coordinate reference. The latter correctly maps source coordinate1014 to compact coordinate304; the fixed value remains C=3^(2^25). The symbolic parameter remains a fixed coefficient, not an added variable.

These maps give inverse rational assignments and preserve the distinguished input. They have no exceptional branch, denominator or square-root choice. This is a coordinate bijection of the accepted source systems, not a new application of their arithmetic proof.

My independently written checker also expands every primitive integral residual square of each compact IR and compares every coefficient with both the compact JSON table and the permuted source polynomial. Primitive normalization and degree are preserved. No source or producer implementation is imported.

## Serialization, counts and coefficient bounds

The JSON reader rejects duplicate keys. The term decoder rejects duplicate or zero terms and unsorted monomials. The independent text parser reads each coefficient, C exponent and coordinate list; it checks exact equality with the JSON polynomial. I separately reconstruct the complete ASCII serialization, including every coordinate legend line, and compare its bytes. The retained ordinary source-ID text is independently parsed in its original syntax and also matches the source polynomial.

| Artifact | Total variables | Witnesses | Quadrics | Monomials | Canonical text bytes |
|---|---:|---:|---:|---:|---:|
| Symbolic299 |299|298|279|6630|228028|
| Ordinary314 |314|313|294|6672|264430|

Both polynomials have degree4 and content1. The symbolic maximum remains exactly186624*C^2, or186624*3^(2^26). The lower C-power coefficients are bounded by small integer comparisons; the enormous fixed C is not expanded. The ordinary maximum is checked against every actual decimal coefficient. It equals3^4098+K, where K is the constant coefficient of the exact symbolic source table, and satisfies2^6495<=maximum<2^6496. It has6496 bits and1956 decimal digits. The ordinary constant-chain metadata has fourteen constant gates and one root-sum gate, and its recorded exponent recurrence ends at2^25.

The canonical ordinary text has264430 bytes. The retained source-ID text has222890 bytes and remains separately named. The byte counts describe different encodings of the same polynomial and must not be interchanged in release metadata.

The compact IR hashes are `5c789e9b664463733793d4242a2fbec4f7512ec706fefd1276de8eeab2a27ad3` for299 and `8dae9a4c1b5840004e145e52eb4d2c7fb4eb024606b8d1a42e8b2a7ae024e25b` for314. The canonical text hashes are `e7f00ae1c0643cb31b93c28ea88e30c3b1790ace718625bb5e223b91e2b101ba` and `57d44e10a92cda1ffac29f46a54282f855882bcf21760c3419df62dc8c673822`, respectively. The retained ordinary source-ID text hash is `efb34a9664a3a2c5b0abe548463e646ba18d6f7e5ab5d9eff9e80bb8b461291e`.

`check.py` reproduces the review using only the standard library and writes only `CHECKS.json` in this review directory. All frozen author and source artifacts were unchanged. The accepted subset is ready for the remaining packaging and assembled-exposition checks under their separate scopes.
