# Versioned supporting notes

These notes expand specific arguments in the [manuscript source](../../manuscripts/quartic_v14.tex). They retain their stated hypotheses and review qualifications; inclusion here is a navigation aid, not an additional mathematical approval or a claim that all incoming premises have been discharged. Locations refer to the current manuscript source unless a supporting note is named.

The [complete proof-source index](PROOF-SOURCE-INDEX.md) lists every selected source file and its exact SHA-256. This page highlights selected notes.

| Supporting argument | Application location | Scope |
| --- | --- | --- |
| [Generic-field Kummer exact sequence](evidence/generic-kummer-current/PROOF.md) | Lines 3908–3912 and 3968–3972 | Explicit Galois-cohomology argument in characteristic zero and its naturality. Ring-class, norm and local component estimates remain separate inputs. |
| [Compatible CM points](evidence/heegner-cm-construction-current/SOURCE-CONNECTION.md) | Lines 3746–3766; norm application at 3824–3846 | Compatible all-split CM points and the raised-conductor construction under the stated coprimality and orientation assumptions. This is not a Néron-model or eigenvalue argument. |
| [Heegner descent source connections](evidence/heegner-descent-current/SOURCE-CONNECTIONS.md) | Heegner descent argument | Eight conditional source interfaces, including conductor norms, CM congruence, derivative descent and local conditions. Read with the two separate construction and Kummer notes above. |
| [Néron models for the fixed local argument](evidence/heegner-neron-current/SOURCE-CONNECTION.md) | Heegner descent note, lines 69–75, 81–87 and 93–97 | Finite unramified base change, smooth lifting and a fixed geometric component-group annihilator. Lang, formal-group cohomology, limiting arguments and the resulting H¹ bound remain separate inputs. |
| [Additive finite-field input](evidence/heegner-finite-field-current/PROOF.md) | Heegner descent note, formal-quotient argument (lines 79–87) | Normal basis and vanishing of positive cohomology for the additive residue module, including when the residue characteristic divides the extension degree. The formal-filtration identification, successive lifting and completeness remain separate. |
| [Based Atkin–Lehner formula](evidence/heegner-atkin-current/SOURCE-CONNECTION.md) | Lines 3853–3856; fixed eigenquotient at 2588–2657 | Formula for the based map, conditional on the stipulated involution action on the differential line and cusp permutation. The fixed cuspidal exponent is a separate input; no general eigenvalue or root-number theorem is asserted. |
| [Generic-conductor inert CM reduction](evidence/heegner-cm-reduction-current/SOURCE-CONNECTION.md) | Lines 3866–3868; Heegner descent note, lines 33–37 | Supersingularity for the actual CM order and permitted inert prime, including ideal-class translates. Good-model realization, raising-kernel specialization, level structure and extension of the parametrization remain separate. |
| [Good-prime modular model and fixed map](evidence/heegner-integral-map-current/SOURCE-CONNECTIONS.md) | Lines 3869–3874; Heegner descent note, lines 33–37 | Smooth proper coarse model and extension of the fixed map at the stipulated good prime. Equality of reduced CM points, raising kernels and level specialization remain separate. |
| [LP03 bounded lower-test selection](source-adoption-ordinary-v1/local-derivations/GI-LP03-BOUNDED-LOWER-TEST-SELECTION.md) | Local GI module 04, lines 166–189 | Conditional selection for the actual strong represented families and pointwise correlation premise. Neither arbitrary weak nilcharacters nor the later shift arguments are supplied. |
| [Bertrand interval theorem](source-adoption-ordinary-v1/source-statements/ERDOS-BERTRAND.md) | Local GI BASE prime selection | Prime between m and 2m for every integer m>1; no arithmetic-progression assertion. |
| [Convex boundary estimate](source-adoption-ordinary-v1/source-statements/GT-CONVEX-BOUNDARY.md) | Local GI MF boundary argument | Boundary-neighborhood volume in fixed dimension. Lattice counts and the empty-interior case are separate local deductions. |
| [Ultralimit equality and evaluation](source-adoption-ordinary-v1/source-statements/GTZ-LIMIT-EVALUATION.md) | Local GI LP13 evaluation argument | Exact equality and evaluation of represented functions on the full ultraproduct domains; not a standard-point-only identity or a bounded-complexity construction. |
| [Raising-isogeny specialization](evidence/heegner-kernel-specialization-current/PROOF.md) | Lines 3868–3872; Heegner descent note, lines 33–37 | Degree-preserving specialization for the actual finite raising diagram, with transported prime-to-residue-characteristic level subgroup. Generic CM data, supersingularity and the fixed-map extension remain separate inputs. |
| [Henselian finite-étale lifting](evidence/heegner-kernel-specialization-current/source-statements/STACKS-04GK.md) | Kernel specialization note, line 25 | Pinned digital source for equivalence under residue-field reduction. The finite-residue-field splitting and actual level-subgroup application are proved in the linked kernel note. |
| [Local algebra for the fixed-type CJ comparison](evidence/cj-local-structure-001/SOURCE-CONNECTION.md) | CJ conductor-one proof, lines 33–44 | Rational embedding, specified conjugacy, pointwise centralizer and two local residue orientations. Geometric realization, analytic transformations and caller support remain separate. |
| [Atkin–Lehner cusp permutation](evidence/atkin-cusp-input-001/PROOF.md) | Lines 3853–3856 and the based-map supporting note | Matrix normalization and permutation of the actual cusp classes. Cuspidal finiteness, the chosen annihilator and differential eigen-action remain separate inputs. |
| [Actual newform Atkin–Lehner action](evidence/atkin-newform-input-001/SOURCE-CONNECTION.md) | Lines 15111–15116 and 15911–15914 | Primitive weight-two eigen-action in the determinant-normalized convention, including exact powers of two. The same-quotient differential identity is explicit; root-number and local orientation identities remain separate. |
| [Codimension-one intersection criterion](source-adoption-ordinary-v1/source-statements/STACKS-0AVB.md) | Cubic/Yuan codimension-two extension | Pinned reflexive-module statement over a Noetherian normal domain. The regular-chart, invertible-sheaf and descent applications remain separate arguments. |
| [Cyclic-level local normalizer](evidence/cj-level-normalizer-001/PROOF.md) | CJ conductor-one proof, lines 37, 83 and 87; main lines 15119–15185 and 15906–15920 | Matrix conjugation and exchange of the two integral idempotents, including at two, under the stated split cyclic-level hypotheses. Global correspondence, actual support and character conditions remain separate caller obligations. |
| [Finite forgetful maps and Picard pushforward](evidence/forgetful-picard-current/NOTE.md) | Lines 1831–1855 | Finite locally free forgetful maps, determinant norm and descent to the relative Picard functor. Actual modular-curve hypotheses and the stated source inputs remain part of the argument. |
| [Finite Weil and Tate pairings](source-statements/rc-finite-weil-pairing.md) | Lines 3708–3718 | Perfect integral elliptic Tate pairing, including at two, with the stated Galois action. Scalar-twist compatibility and Selmer duality remain separate arguments. |
| [Integral Shapiro transfer](source-statements/rc-integral-shapiro.md) | Lines 4129–4159 | Integral cochain transfer, section homotopy and tower compatibility. Local conditions, inverse limits and later homotopy constructions remain separate. |
| [Quadratic Gauss-sum normalization](evidence/quadratic-gauss-local-001/PROOF.md) | Lines 13653–13659 and 13686–13691 | Finite primitive-character calculation and the four possible basis factors. Actual character/discriminant identification, reciprocity and period comparisons remain separate inputs. |
| [Dual exponential and finite trace](evidence/dual-exponential-trace-001/PROOF.md) | Lines 13617–13622 | Finite-extension trace compatibility and the explicit character-twisted endpoint. No averaging factor is introduced; smoothing, infinite towers, reciprocity and periods remain separate. |
| [Global geometric Atkin–Lehner identification](evidence/cj-global-atkin-identification-current/PROOF.md) | CJ conductor-one proof, line 66; main lines 15906–15916 | Quotient by the cyclic subgroup, dual kernel, matrix action and prime-to-residue-characteristic specialization. Newform action, character/support conditions and opposite Frobenius orientation remain separate. |

## Exact file identities

SHA-256 values identify the linked note versions; a changed file requires a new identity and its own applicable review.

- `research/version14/evidence/generic-kummer-current/PROOF.md`: `523a28c1c3bdb5f23db40adb362d2f7ca3cb51851f598d2df496f4f1568945a3`
- `research/version14/evidence/heegner-cm-construction-current/SOURCE-CONNECTION.md`: `78d42dee9a7b335cef8de11310bb091a10c127e87f691eae911aa270ebc7ad6b`
- `research/version14/evidence/heegner-descent-current/SOURCE-CONNECTIONS.md`: `d16b5cbc134812a4ecf1a6c4c008a0a076b79fdce7d3b5f6b9f8d94c9276268f`
- `research/version14/evidence/heegner-neron-current/SOURCE-CONNECTION.md`: `ac5c73e55a0580b0f11166969f6a2c6109833fe9de3e9ba3fef42ebc1f570ba9`
- `research/version14/evidence/heegner-finite-field-current/PROOF.md`: `7cf2deac2376b3866f091ce4fce6469d4feedb6544193e1607daac2e5bc77f8f`
- `research/version14/evidence/heegner-atkin-current/SOURCE-CONNECTION.md`: `6e1d3c56b11e6303d42f3efc095f2fea6e37759f9757f9c1a78ae1405eafaf18`
- `research/version14/evidence/heegner-cm-reduction-current/SOURCE-CONNECTION.md`: `5a8f69fef00fc38d9bf01e5c0edb722e99e8810e74f027f6ea31841873e2ee8f`
- `research/version14/evidence/heegner-integral-map-current/SOURCE-CONNECTIONS.md`: `c220b352d3be0ef26a3b0475b141e2b43c239095e8a0430156670f2de4adc1f6`
- `research/version14/source-adoption-ordinary-v1/local-derivations/GI-LP03-BOUNDED-LOWER-TEST-SELECTION.md`: `4f3252d25bceb9011ca0db677ab9be2200472f5f9201ae729a8118412f6411f0`
- `research/version14/source-adoption-ordinary-v1/source-statements/ERDOS-BERTRAND.md`: `cd7f32ca7c929290d94f0b5913c604a395ff45f9c28e9f946cf0968105d22746`
- `research/version14/source-adoption-ordinary-v1/source-statements/GT-CONVEX-BOUNDARY.md`: `410779025e5123ff8838c6a864539494696635d302069c7397b2dc0732101c55`
- `research/version14/source-adoption-ordinary-v1/source-statements/GTZ-LIMIT-EVALUATION.md`: `add3aeaa2357c623c9d9f9f6324c5750d78b81ad4aa47f627857ec46edcec2a7`
- `research/version14/evidence/heegner-kernel-specialization-current/PROOF.md`: `9ecec72ad6682c91c8ce182e3f9e3e9c57a960b0daf96bb8e519f553ca4209ef`
- `research/version14/evidence/heegner-kernel-specialization-current/source-statements/STACKS-04GK.md`: `b3da49274324f40e5ad3e3207ca330e0c4b972e5926ba0e5f8f65fb88d60be56`
- `research/version14/evidence/cj-local-structure-001/SOURCE-CONNECTION.md`: `f40e1015c5d651a998856ba90dd74a15d6e01a705da7f70301b1d6ad0c149293`
- `research/version14/evidence/atkin-cusp-input-001/PROOF.md`: `f52c5697ecb22b43035bf4abd79114157917db0e07a1774889200acb3d291629`
- `research/version14/evidence/atkin-newform-input-001/SOURCE-CONNECTION.md`: `d80e8c4e1b8df11af13a3eb3dd6b9d27326334c8e79ac8edfd0820f12a183a1f`
- `research/version14/source-adoption-ordinary-v1/source-statements/STACKS-0AVB.md`: `57049123c6f253a19b618319e61399853c292b6794b878ce570d05b4690a1b2e`
- `research/version14/evidence/cj-level-normalizer-001/PROOF.md`: `af0522be35419ac63aa18e08c3752e8a491db72f5ff1a1659992c79448cade78`
- `research/version14/evidence/forgetful-picard-current/NOTE.md`: `afd3b60929199666e657f6d9cc1482631843f7e9e5401bd294604664d05904e5`
- `research/version14/source-statements/rc-finite-weil-pairing.md`: `f9eb4109c3632fe823ac99169494c03209d193d34b588f4c46e26d1badd0d0b8`
- `research/version14/source-statements/rc-integral-shapiro.md`: `28f8afd89cb315762c03d84e3a7b6d36d93e8a6d682b9607251a20c7976039c7`
- `research/version14/evidence/quadratic-gauss-local-001/PROOF.md`: `0ea59481f2f6bed3ddd4bf19362fee92a110ab88d3f2ee63788ebd8edb7e1f06`
- `research/version14/evidence/dual-exponential-trace-001/PROOF.md`: `41b8b280384292d6ff17a0be43c63821eeb3bd5ebaed7d5d5942046637dcc086`
- `research/version14/evidence/cj-global-atkin-identification-current/PROOF.md`: `14272b5fa771ac76aa3279234ecceeeef01e7c9855613b6abbec58bd159f9057`
