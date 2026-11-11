# Crystalline Hecke-map source and connection review

Reviewer: `/root/astra_quartic_opt05_anchor`, 2026-11-08. This review accepts the bounded eta-map source audit002 and its application at CEGGPS6.17, relative to the retained source inputs specified below. It does not certify the whole CEG+16, CEGGPS or BM proof, and does not compare unavailable final editions. Exact targets and decision are recorded in DECISION.json.

I read the original audit001, its source and map records, CEG+16's actual author text pp5–6 and30–38, and CEGGPS's actual type/Hecke definitions and Proposition2.9 on pp8–11 together with6.14–6.18 on pp32–35. I visually checked the framed Theorem4.1 statement on p31 and the explicit Hecke formulas on CEGGPS p11. These are the exact author versions in the target, not relabelled final publications.

## Normalization and the source statement

CEG+16 defines geometric Frobenius, cyclotomic Hodge–Tate weight minus one, and `r_p(pi)=rec_p(pi tensor |det|^((1-n)/2))`. If the two increasing weights are u<v, the pre-dual highest weight is `(v-1,u)`. Taking the stated algebraic dual gives highest weight `(-u,1-v)`, or `Sym^(v-u-1) tensor det^(1-v)`. This agrees with the body of CEGGPS: sigma_(a,b) has weights `(-a-b,1-a)`. It does not use the previously excluded introductory convention or apply a second cyclotomic twist to the Paškūnas label.

Theorem4.1 interpolates the *classical* locally algebraic type-space character at potentially crystalline points of a framed fixed-type deformation ring. It says nothing by itself about the locally algebraic vectors of an arbitrary Banach representation. Its proof constructs the Hecke map using the Bernstein center and then the map on Hecke functions multiplying by the algebraic representation. The intervening Bernstein twist is exactly `|det|^((1-n)/2)`. Thus the natural action on Hom_K is the one compared by CEGGPS6.17, with no unrecorded inverse of the Hecke eigencharacter.

## Proof-path audit

I checked the actual local proof before its return to the global patched module. Proposition4.2 uses the varying Weil–Deligne representation and the Bernstein pseudotrace. Lemma4.5 proves generation through power sums and negative power sums after separating inertial constituents. These are classical Weil/smooth representation statements, not Banach locally algebraic identifications.

Lemma4.8 invokes Hu2009's weak-admissibility/Jacquet conditions, with the extra unitary twist explicitly cancelled, and Emerton2006a Proposition4.3.6 for the Jacquet functor on an algebraic tensor a smooth representation. The bibliography identifies that input as the 2006 ENS Jacquet-module article. The old file separately lists the local-global manuscript as `[Eme]`; that is not the input cited here. Corollaries4.9–4.11 and Proposition4.12 propagate the eigenvalue bounds through the type Hecke algebra. Kisin generic-fiber regularity and de Jong's bounded-function result then put the map in the algebraic generic-fiber ring.

This confirms the audit's bounded claim: the displayed local proof path does not invoke the disputed Emerton2011 supercuspidal Banach identification. The appearance of classical supercuspidal supports is not that assertion. The conclusion is limited to these inspected proof steps and named incoming edges. It is not a proof that all ancestors of Hu, Chenevier, Kisin, de Jong or the classical type theory are independent of every other source concern.

## The actual consumer

At CEGGPS6.17, the auxiliary absolutely irreducible residual domain ensures irreducibility of all characteristic-zero lifts. The selected nonexceptional crystalline fibers have the actual Banach identification supplied by the earlier restricted review, and Berger–Breuil supplies their locally algebraic principal-series embedding. Their type space is one-dimensional. Consequently the Hecke action on this line is the classical character interpolated by eta. The unramified character variable preserves the eigenvalue ratio, so the chosen dense set remains dense after adjoining it. The reduced ring and its faithful rank-one module permit the passage from pointwise equality to equality of ring maps. The reducible-Galois Breuil–Emerton branch is unused.

The original audit identified the framed source and the unframed consumer without explicitly writing their descent. I requested a separate successor connection rather than treating the two target rings as identical. The author supplied audit002, whose manifest is `c9a6ba3fe403c89d593c347672bba68ef27ea34f0d03d8915b43d16f77c87ecd` and report is `86fd9e8449185b59019796d8b91f9a1013c9c54a89062799a844f21e2a978d9e`. The original001 remains unchanged. The omission was a missing explicit connection in the source-audit record, not a counterexample to CEGGPS. My feedback identified the missing connection; I did not author the successor proof.

## Descent and generator check

The residual representation is absolutely irreducible. Its endomorphisms are scalar, the unframed deformation functor is represented, and a representative of its universal class can be chosen in a basis lifting the specified residual basis. Framing this representative adds the three formal coordinates of the identity neighborhood of PGL2. The resulting description of the framed ring as `R[[x1,x2,x3]]` restricts to the crystalline quotient because the crystalline condition is invariant under conjugation. Setting the frame coordinates to zero is an actual ring retraction onto R. This does not identify framed points with unframed points.

Compose the framed Hecke map with this retraction. At any closed framed characteristic-zero point, the original frame and the frame chosen after restriction to R give isomorphic Galois representations. Theorem4.1 assigns them the same classical type character. For each Hecke element the difference between the framed map and the base change of the retracted map therefore vanishes at every closed point. The reduced Jacobson property of this crystalline generic-fiber ring makes that difference zero. Repeating the same argument for any two sections proves independence of the chosen universal frame. This is a valid descent argument in the stated absolutely irreducible domain. It neither uses an unproved invariant-ring equality nor infers a ring identity from an unspecified sample of points.

I checked the generators against CEGGPS Proposition2.5 and the proof of Proposition2.9, including the actual PDF p11. For `sigma=det^a Sym^b`, the weights are `r=-a-b`, `s=1-a`. Unnormalized induction of `|.|chi1 tensor chi2` becomes normalized induction of `chi1 tensor chi2` after the prescribed half-determinant twist. The unweighted double cosets act by `t` and `5^-1 d`. The algebraic factors give exactly `eta(T)=5^(a+b)t` and `eta(S)=5^(2a+b-1)d`, since `-r=a+b` and `-r-s=2a+b-1`. These are identities in `R[1/5]`. The argument asserts no integrality of t or d in R. Nonzero Frobenius determinant also respects the invertibility of S.

The indecomposable hypothesis in the explicit filtered-module calculation is satisfied here: a characteristic-zero reducible representation preserving a lattice would give an invariant line after saturation and reduction, contradicting residual absolute irreducibility. Thus the actual interpolation, filtered-module and consumer domains agree. The descent and formulas are accepted for this domain; there is no extension to arbitrary residual reducible deformation problems.

## Verification and independence

The accompanying checker independently hashes both frozen audit manifests and their members, the two source PDFs and text extractions, and verifies that the successor preserves the old source pins and old map fields while adding the declared descent. Its integer exponent checks are only convention checks. These finite checks do not prove the mathematical statements; the source reading and the arguments above provide the bounded mathematical assessment. Local PDF renders are excluded from this review's distributable manifest.

I authored neither audit001 nor audit002. My earlier conditional consumer review and the request for an explicit framed-to-unframed connection are disclosed here. This acceptance supplies the source-to-consumer connection missing from that conditional review; it does not silently discharge its other retained inputs.

## Limits

The final editions of CEG+16, CEGGPS and BM remain separate qualifications. The inspected proof still retains its family comparison, classical type theory, Hu/Jacquet, crystalline-regularity and bounded-function inputs. A source audit of their uses does not recertify their entire proofs. The separate Ext/BP application reviews do not alter those source-version limitations. There is no whole-manuscript, patching or release approval here.
