# Independent final review of the Version 13 quartic application

Decision: accepted within the scope stated below. No unresolved defect was found in the new application or its integration.

Reviewer: `/root/astra_bl_synthesis`. Date: 2026-11-07. I did not author any of the new quartic components, their exposition, the final arithmetic composition, or the application contract. This is a fresh review of the assembled application. The earlier component reviews were evidence to inspect, not substitutes for this decision.

## Exact objects and scope

This decision binds the following SHA-256 values.

| Object | SHA-256 |
|---|---|
| `docs/manuscript-revisions/version13/quartic-application.json` | `9369be2e7c73f62aede900c7de0782b978b115c0275e2bd2fff958f84e2786ba` |
| `manuscripts/quartic_v13.tex` | `9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd` |
| `docs/manuscript-revisions/version13/addition.tex` | `91b278b3ca1684df93e32883d8046a2accda970efc1ed9159b095183092d5a09` |
| `manuscripts/quartic_v12.tex` | `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9` |
| Final 394-coordinate residual system | `7eb02f9913b55d60a790a287616f1bb80d9f93523e9f11e12481c9ab955746a5` |
| Final 411-coordinate residual system | `b30e730bd65109a36be4f2a794222ff97dc292dcb3a4bd58de6e33f594e8c16c` |
| Installed 39-application inventory | `b7c4027a0f735906b4fdde129f08294871332e49f68b25d5e2fc32e9c42d9674` |

The review covers the new Version 13 abstract, introduction and full reduction section, their use of the retained arithmetic inputs, and the exact final polynomial artifacts. It follows the new chain from the released 498-coordinate system. It distinguishes exact private-coordinate transformations from domain enlargements and fresh completeness constructions.

The retained generator, rank, squareclass, root-height, scalar-height, Lucas, real-progression, simultaneous-prime, separation and pole-preparation results keep their existing source and review qualifications. This report does not newly certify their entire historical proofs, the unchanged minimum-degree claim, or the original huge polynomial. It does not turn the finite circuit checks into an audit of all arithmetic hypotheses. In particular, it is not a fresh whole-manuscript certification under a stricter standalone historical-proof protocol.

I checked the complete new addition and its assembly into the full TeX file. Applying the four recorded edits to Version 12 reproduces Version 13 exactly after the documented line-ending normalization. The three mathematical edit hashes agree with the contract; the remaining edit is the title. The addition occurs once. The contract's three manuscript-span hashes and every directly bound evidence-file hash agree with the files inspected. No additional historical mathematical change is hidden in the assembly.

## Primary sources and retained inputs

I inspected the pinned Silverman second-edition PDF, including Theorem IV.6.4 on printed page 132. Its logarithm isomorphism applies beyond depth `v(p)/(p-1)`. At the consumed unramified places with `p>76176`, positive integral depth meets that threshold. The new proof uses logarithm additivity only on actual formal points and uses the inherited full-tail estimate with the same parameter `z=-x/y`. Identity points use the analytic unit extension, not a quotient by zero.

The Silverman PDF has SHA-256 `72ee67bfa1e3fdf582ac7e4b032d7ca0b35a168ed6443ac39c121fbb788cab25`. The existing source inventory's qualifications remain, including the identified sign and isogeny-formula typographical errors and the fact that the full official errata file was not retrieved. This review does not claim to have checked an unavailable errata file. The source is [Silverman's second edition](https://link.springer.com/book/10.1007/978-0-387-09494-6).

I also inspected Proposition 14.6.7 and Remark 14.6.8 in the pinned corrected Voight PDF, printed pages 223-224. They give the quadratic embedding criterion in terms of splitting at ramified places, with the split etale case distinguished. Version 13 restores the existing anchor before using its arithmetic consequences; it does not introduce a new quaternion criterion. The pinned PDF has SHA-256 `a9316b834dbd500c52cd3a981c3205c9f4145b217042b213d23f696aee84b0f0`, version 1.0.7u dated August 5, 2026. The source is [Voight's corrected book](https://jvoight.github.io/quat-book.pdf). The hash, rather than the mutable URL, identifies the inspected edition.

For internal inputs I inspected the relevant Version 12 source passages, including the input and mixed-ratio sections, scalar coefficient lemma, scalar local proof, scalar preparation-zero lemma, real progression and CRT construction, and soundness/completeness passages. These are internal inherited results, not independent external publications. I checked the new applications against their stated domains and actual consumers.

## Mathematical findings

### Formal logarithms, precision and heights

The displayed rational approximation has the claimed order. Direct rational arithmetic reproduces the two remaining coefficients in `Q2*G9-N8`; the first nonzero term has degree ten in `Df^2`. Thus a formal point of depth `r` has relative error at least `40r`. The first opposite test retains its order-twelve approximation while the input and first cross test use order ten. The other cross and Lucas tests keep order forty.

The proof first obtains integrality of the full ratios, using that one of `h` and `h-1` is a local unit. Only then does it improve the primary depth. This order avoids multiplying an error term by a possibly nonintegral ratio. The resulting primary depth twenty gives the claimed order-eighty primary error. At zero numerator, the analytic unit equals one at the identity and the numerator remains zero. No step requires a nonidentity comparison point.

The scalar valuation calculation is sufficient at depth twenty-four. The two terms in each sum have opposite valuation parity because the relevant contact valuation `eta` is positive and odd. The pole bound yields

`v(Bs)>63*eta/4`, `v(q)>61*eta/4`, `v(z0)>191*eta/8`, and `v(z1)>187*eta/8`.

Both coefficient valuations are therefore at least twenty-four. Positivity of the norm only selects a place where `H` is formal. It does not imply that `R` is formal. The proof separately handles `R` near the identity and near the two-torsion point with abscissa zero. In both cases `2R` is formal with the required parameter valuation. Applying the integral group identity for `2R` gives divisibility of the integer scalar index `s`, since the half-index `h` is integral at the consumed odd prime.

The height margin was checked exactly: `(5/24)*25165823.5 > 2093966+7`. The unchanged exponent-nineteen bound therefore supplies the stated scalar-height estimates. The order-forty Lucas argument yields its original lower bound for `log B`; the order-ten input test gives the incompatible upper bound `29|a|/40` if `n-beta` is nonzero. The proof invokes the height estimate only for nonzero integers. The final input conclusion also uses that `n` is odd. Integrality of `beta` alone would not suffice.

### Enlarged point domains and exceptional cases

The odd-root norm chart preserves the intended odd-index domain. Its reverse doubling construction gives a preimage of the same root point. The norm condition forces the required squareclass, and replacing `A` by `2(x+j)-A` changes the sign class through the product `-D`. This addresses both allowed squareclass choices without assuming uniqueness of a private witness.

The reciprocal comparison charts include the identity. Their nonzero denominators follow from the real and norm arguments. The branches `r=0` and `g=0` have the stated meanings, and the equal-abscissa case corresponding to `U=-Q` uses the regular doubling value. The scaled biquadratic chart reconstructs both conics and the subtraction orientation. The retained outputs are squares of field elements, not sums of squares of their rational coefficients. Its inverse does not divide by `r`, `g`, or the retained output values.

Removing the square witnesses for `H` genuinely enlarges the soundness domain. The proof does not treat this as an old-witness bijection. It writes `H=mR0+T` and uses `h=m/2` only as a rational index. The actual group identities have integral multipliers and kill the two-torsion term. This supports both comparison ratios and the scalar identity. Completeness can still choose the original doubled points.

The enlarged-domain proof excludes the finite torsion translates before interpreting the new quotients. Their displayed abscissa norms make `f(H)` a unit at every consumed place. The order-forty detector would then make all contact radicals one. The pre-ratio root-height bound contradicts the already established scalar anchor. The later subtraction denominators are consequently nonzero. No real-positivity claim for arbitrary `H` is needed.

The global nonvanishing of the logarithm numerator and denominator is justified separately. I enumerated all residues for `N8` modulo 71 and `Q2` modulo 7 and checked the leading-unit conditions and the displayed square roots of two. A root over `K` would give a root over the corresponding split local field. The leading-unit condition makes that root integral, contradicting reduction. This repairs the domain issue that a positivity argument restricted to doubled real points would leave open.

### The anchor precedes its consumers

The new guard `g0*tau=1` first identifies a nonzero scalar difference point of even index. The case `S=P` is excluded by the guard. The case `S=-P` has the stated duplication interpretation. The inherited coefficient lemma applies to every nonzero even index, including negative indices; it does not assume anchor divisibility.

Its valuation conclusion makes `F=2g0*g1` nonzero. Only then does the proof restore the old inverse and anchor. The displayed residual identity verifies the rescaling exactly. Thus the anchor is available before the exceptional-`H` height contradiction. An isolated new anchor with an arbitrary value `g1=0` would not establish this, but that value is excluded by the full point system before the equivalence is used. Zero values of the private anchor witnesses remain allowed.

### Deterministic correction and simultaneous completeness

For integer input I checked the complete relevant residue calculations: `r=4 mod 32`, `r=3 or 6 mod 9`, and `r=15 mod 17`. These give the required local squareclasses for `c=r+4896`. At a consumed large contact prime, positivity and odd valuation of `r` precede the conclusion that `c` is a unit. The argument makes no false claim that every large prime is a unit for `c`.

The completeness construction includes all prime divisors of the actual product `cr`, as well as 2, 3 and 17, before selecting the continuity modulus and contact primes. The separate inclusion of 17 supplies its required preparation depth even when it does not divide `cr`. The square-denominator and local-square conditions are preserved at the other primes.

The choices have a valid common order. First fix the integer input and deterministic correction. Choose a preliminary deep `H0` sufficiently close to the identity over the reals, then choose the nonzero scalar point `R` sufficiently deep at the fixed finite places and sufficiently close over the reals. This gives the preliminary bound `0<b<17/4`. With `R` fixed, choose a real neighborhood preserving `0<b<17`. Choose labels and scales, remove the finitely many poles, and fix a smaller open set with compact closure and the necessary bounds. Fix the continuity modulus before selecting the contact primes.

The final congruences are compatible. The residue and modulus have the required divisibility by the number of components, so the inherited positive-progression statement applies on the correct identity component. A single final `H` satisfies the local conditions and lies in the chosen real open set. This supplies the hypotheses of the preparation-zero lemma for the same final pole input. It does not splice together unrelated real and finite witnesses.

The preparation-zero step supplies fresh witnesses for integer inputs. Its soundness restoration uses the independently proved positivity of the scalar input. It is not asserted to specialize every old private witness. The factored-pole transformation handles the zero-factor branch; its completeness direction uses semantic positivity with the stored scalar sign treated correctly. The final scalar-pole normalization divides only by an outside quantity already known to be nonzero, and preserves private zero branches.

### Circuit transformations and the final polynomial

I followed the actual residual consumers through the shared reciprocal, subtraction, grouped-product, power, affine-recentering, fixed-pivot, scalar-pole and anchor changes. The grouped detectors continue to evaluate products of `1+qY`, with the proper conjugation and order. Fixed-pivot substitutions preserve every outside use; they are not justified merely by the coordinate counts. The different physical scaling conventions are included in the comparisons.

I wrote a separate finite checker using only the Python standard library. It imports no producer or prior reviewer. It re-derives complete component differences, compares old consumers with the current accumulated system, transports the rows and coordinate changes, and compares the final systems for fourteen combined stages. Rows are compared as zero equations up to a nonzero rational scalar where normalization changes; final polynomial expansion uses the actual stored coefficients. The seven application-component records also match their full source/target differences and coordinate incidence lists.

The final sum of squares was reconstructed independently from every normalized residual. Both source-coordinate and consecutive-coordinate JSON tables match exactly, and parsing every plain-text coefficient row gives the same dictionaries. All coordinates occur. There are no monomial collisions between different symbolic powers of `C` on specialization.

| Property | Symbolic polynomial | Ordinary companion |
|---|---:|---:|
| Total rational coordinates, including the input | 394 | 411 |
| Quadratic residuals | 364 | 381 |
| Nonzero monomials | 6,338 | 6,388 |
| Total degree | 4 | 4 |
| Integer content | 1 | 1 |
| Largest absolute coefficient | `16*C^2` | 3,247 bits, below `2^3247` |
| Plain-text coefficient bytes | 212,067 | 214,957 |
| JSON coefficient bytes | 973,221 | 982,235 |

The ordinary companion is exact. Its sixteen uniquely constrained constant coordinates compute `3^(2^25)` starting with `3^1024` and fifteen squarings. Its seventeenth new coordinate is the uniquely constrained product `C*tau`. Exactly one old residual changes, substituting this product into the anchor. All other old coordinates and equations remain the same. This separate gate is necessary to keep the residual quadratic. The forward and reverse witness maps are immediate from the unique equations, with no sign or nonvanishing choice added.

I also ran the installed portable source replay. All 27 stages passed through the final symbolic and ordinary tables. I ran the installed inventory validator, which passed 39 applications, 351 obligation fields, seven components, 97 changed residuals, 47 compatibility bindings, 629 file pins, 212 spans and 155 labels. These executions are finite evidence. Their successful status is not used as a replacement for the arithmetic arguments above.

The supplemental reviewer checker has SHA-256 `38d16cd02edb689fd2ed3c6bd94c1323f95fd0f9613dadfaefb7747e256e2f61`; its result has SHA-256 `f8a939accd2d8300cf4abdf155bd5fd74fea5fff2e8b527ac6063497d9b78eb0`. They are workspace review artifacts under `work/quartic-v13-release/independent-final`, not claimed to be part of the public packet. The installed replay and its source manifest provide the distributed finite checks.

## Disposition of the nine contract obligations

| Obligation | Independent disposition |
|---|---|
| `source_hypotheses` | Accepted. The new uses preserve the model, valuations and retained hypotheses; enlarged `H` is treated separately. Source qualifications remain explicit. |
| `constructed_objects` | Accepted. The actual 394-coordinate system and its 411-coordinate companion have the stated projection under the retained arithmetic inputs. The fixed coefficient and computed-coordinate roles of `C` are distinct. |
| `index_domain_coverage` | Accepted. Identity comparison points, half-indices, torsion translates, scalar zero exclusion and negative even indices are covered before use. Completeness constructs witnesses for every integer input. |
| `transition_maps` | Accepted. Exact changes have reverse maps and justified divisors. Domain enlargement and preparation specialization have separate soundness/completeness arguments. Actual residual consumers match. |
| `limiting_object_identity` | Accepted. There is no new analytic limit. The finite residual-to-polynomial identities and coordinate maps match both complete coefficient tables. |
| `coefficient_conventions` | Accepted. Basis, conjugation, local normalization, fixed `C`, total coordinate counts, content, degree, maxima and byte counts agree with the bound artifacts. |
| `local_conditions` | Accepted. Integrality precedes improved depth; scalar depth twenty-four survives both local branches. Deterministic correction and all finite/real requirements hold for one ordered construction. |
| `exceptional_cases` | Accepted. The anchor is restored before exceptional-`H` exclusion. Zero comparison and private-pole branches remain valid, and modular certificates handle general-`H` logarithms. |
| `downstream_consumption` | Accepted. The unchanged exponent-nineteen bounds, order-forty Lucas argument, order-ten input argument and oddness bridge yield the stated input conclusion. The final abstract's new counts agree with the exact tables. |

## Corrections, build evidence and final decision

No author-file correction was required by this final review. Earlier component concerns about the half-index scalar identity and use of real positivity on an enlarged domain are resolved in the exact final text inspected here. My finite-check implementation was adjusted to compare normalized residual equations up to nonzero rational scaling; this was a checker issue, not a change to the mathematical system.

The bound build receipt records zero TeX errors and no unresolved references for the exact manuscript. The bound PDF inspection records 296 pages and inspection of the title and every new-section page. I checked those records and their manuscript/PDF bindings. I did not repeat the separate visual inspection and do not present it as my own rendering pass. The PDF identified there has SHA-256 `c72b9cc5c4f2b588b370bea80418b636cd39593fee46c991b9360103ef76bc36`.

I accept the nine obligations for the exact contract and manuscript above, within the retained-source scope stated at the start. This accepts the new mathematical application and its integration, rather than only its finite counts. It does not authorize a broader claim that every historical dependency has received a new independent proof audit.
