# Independent review of the classical modular representation connector

Disposition: accept the bounded mathematical connector in classical-local-connector-root-001/PROOF.md, SHA256 d990c04c59fbf78ea085e018a6da82f269bb7735379b82255f2ffd4fac110c5e, under author manifest483553ea83403d850304e4d0ede65ced31e7b06c5e23d9fd339fdb0942d2aa06. No substantive repair was requested. The accepted content is the primitive selection, weight-one exclusion, all-level classical de Rham input, exact dual/Frobenius normalization, and the resulting weight-two/finite-twist deduction, under its stated incoming hypotheses.

The exact consumer is pan-calegari-direct-author-001/PUBLIC-PROOF.md25–32, SHA256995d60ad7b793c17096bbb55476f52104af45a84d634713e3c490fe9bbd6ffda, excerpt86a53ed78e2ef0ed09ed988807f5bebd8d481dcd5fcaec7c34bca01a435c9dd9. The same representation r5 and character delta are retained. This review does not reprove Calegari/Pan modularity, reconstruct r5, or approve manuscript incorporation or an ordinary-record adoption.

## Independence and reading order

I am not an author of this connector or of SourceReview's Kato dual-match derivation. I first read the current consumer and final primary sources, then froze SOURCE-FIRST.md7997d8943df779abb05acfa378bf8f66b478df2995a4eea5fd2a2ecb489fe91d. Root subsequently added primitive normalization to the review scope and named the intended oldform-decomposition/Hecke-equivariance route. That guidance is disclosed prior exposure. I directly read the relevant Deligne–Serre statements and froze SOURCE-FIRST-PRIMITIVE.md f73b1449d2bff12bae00f29e78553a48b34f8f6bf3a115da4e981df567e585e3 before reading the author packet. I received source locators, not SourceReview's argument or a favorable verdict. My earlier Pan record-adoption review is prior exposure, not authorship of this mathematical bridge. The serving model is unknown/not exposed in retained launch metadata.

The author correctly discloses root authorship, SourceReview's source/dual-match contribution, and Sol's early-Li scope finding. Those contributions are not counted as independent acceptance.

## Source and proof checks

The primary sources were independently hashed and read directly, with the decisive formulas visually inspected on locally rendered pages. Kato's final PDF is3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d. Deligne–Serre's final PDF is65b390f6d33e827e30c6c66bbc15421eca51db3180bdf5996dcee19047be97fc. All extracts and renders remain local-only.

The preliminary selection at author lines11–18 is valid for positive classical weight before k=2 is known. Deligne–Serre1.9 supplies the primitive/oldform decomposition and its uniqueness. Its1.6 coefficient formula gives commutation with h(z) to h(dz) at primes coprime to the ambient level. Therefore any nonzero constituent in the decomposition of the given cuspidal simultaneous eigenform has the same good-prime eigenvalues. Section1.7 supplies a_1=1 for the primitive constituent. This does not divide by a possibly zero first coefficient of the original oldform and does not use Li's weight-two theorem prematurely. The source statement and the local equivariance derivation are correctly distinguished.

The weight-one argument at lines19–28 uses Deligne–Serre3.1 and4.1, not Kato's k>=2 formula. The parity hypothesis follows from the nonzero form's action under -I. Sections8.2,8.5,8.6 give the claimed number-field realization; Remark6.5 and its footnote provide additional direct confirmation of the finite-image p-adic realization. The arithmetic-Frobenius convention agrees. Matching the semisimple representation by3.2 is legitimate because the modular representation is irreducible, being a character twist of r. After killing the finite local image, r is two copies of the same character. Finite-extension compatibility and subobject closure then contradict its distinct weights. Ramification at5 is harmless here.

At lines29–42, Kato5.4 and8.3 include the low-level realizations;6.3 gives dimensions2 and1;9.2 and9.4 give de Rhamness and filtration dimensions2 for i<=0,1 for1<=i<=k-1, and0 for i>=k. There is no condition5 not dividing N, no non-CM condition, and no inference of crystallinity. I read14.10 through its continuation at241; the crystalline-module formula is not used as a replacement for the all-level de Rham statement.

The normalization is exact. Kato's V has determinant kappa^(1-k)epsilon_f^(-1), and14.10.3 puts the Hecke polynomial on inverse arithmetic Frobenius. The dual therefore has arithmetic-Frobenius polynomial X^2-a_ell X+epsilon_f(ell)ell^(k-1), determinant epsilon_f kappa^(k-1), and weights{0,1-k}. The author does not silently assume that a whole cohomology group is semisimple: its semisimplification matches irreducible U_f; hence the two-dimensional V^vee itself is irreducible and isomorphic to U_f. No conjugate-form change or extra Tate twist is introduced.

At lines43–54 the stable Hom line supplies delta as a de Rham character. Its single integral weight m gives{m,m+1-k}={0,-1}; after the separate weight-one exclusion, k>=2 forces m=0 and k=2. The retained finite character alpha=det(r)/kappa then gives delta^2=alpha/epsilon_f. The finite-image conclusion follows from finite fibers of squaring in characteristic zero. It is not inferred from weight0 alone.

## Nine comparisons

| Comparison | Result |
|---|---|
| Source hypotheses | Nonzero classical cuspidal eigenform, positive integral weight, correct parity, and incoming irreducible de Rham r are preserved. |
| Constructed objects | Primitive f is selected without replacing r or delta; Kato's precise coefficient-field realization is used. |
| Index and domain coverage | k=1 is separate; all k>=2, N>=1 and primes dividing N are covered. |
| Transition maps | Degeneracy/Hecke commutation, compatible coefficient extension, finite local restriction, duality and the Hom line are explicit. |
| Consumed-object identity | Good-prime matching plus semisimplification/irreducibility identifies the actual U_f with V^vee. |
| Coefficients | The fixed eigenvalue-field embedding is retained through finite extensions; the weight-one number-field realization is sourced. |
| Local conditions | De Rhamness, finite-extension compatibility and the sign HT(kappa)=-1 are used; good reduction/crystallinity is not assumed. |
| Exceptional cases | Low levels, k=1, CM forms, ramification at5 and a zero initial oldform coefficient do not create omitted cases. |
| Downstream consumption | The exact parent section receives k=2, a_1=1, finite delta and the correct determinant; conductor and finite-twist extraction remain separate. |

## Verification and limits

CHECKS.json records54/54 integrity checks passed, including the author manifest/member, source inputs, both source-first freezes and local evidence, and the exact parent-consumer excerpt. TARGET.json records all six author section ranges and raw excerpt hashes. INPUTS.json contains50 unique pinned inputs. These integrity counts supplement the mathematical reading; they are not a substitute for it.

Accepted standard foundations remain the published modularity input, the already supplied r5 properties and finite-alpha argument, de Rham tensor/dual/subquotient theory and its Hodge–Tate weight rules, and characteristic-zero semisimple uniqueness from good-prime polynomials. No recursive proof audit of those foundations is claimed.

No manuscript or historical review was changed. Exact incorporation into both current callers, ordinary-inventory adoption, controlled-field/conductor conclusions, full source ancestry, builds, and publication/release require their separate checks. This decision supplies no broader acceptance.
