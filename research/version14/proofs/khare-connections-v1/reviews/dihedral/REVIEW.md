# Independent review of the selected Khare 5.1 replacement

Reviewer: /root/astra_v14_baseline_compiler, model agent, operator-local identity. Date: 2026-11-08. Author: /root/astra_quartic_opt05_anchor. Target manifest: 353f130bacf8516b86d9f5374884c4902478c27c8ce6ac8d793a651fd338c158. Target proof: ed37c6855905d91344b41fdf56c6482fdee899bee71d4a524a396d7ac81efb40.

Decision: accept the two stated residual-representation connections and their conditional fourteen-caller partition. This is not acceptance of Khare 5.3, 5.4, a modularity lifting theorem, the class-number existence assertion, or the final Khare edition.

## Independence and source reading

I have previously reviewed related SW, exceptional-p3, and modularity-source material. I did not author this replacement, supply a mathematical repair to it, or use an earlier acceptance as a substitute for its proof. I first read the exact caller records and actual Serre pages, then the Khare author statements and the new proof. This was not a blind or whole-source completeness audit. My independent derivations below concern the new finite-group, inertia and weight connections only.

I visually read final Serre1987 pp.183–184, including Proposition1, (2.2.1)–(2.2.5) and (2.3.1)–(2.3.2). The final PDF is pinned at 8048919db24dcb972435aaaa2a74d1168d0fe533af3aa26c6c809b12ddaee038. These are definitions and tame-inertia calculations, not an invocation of the then-conjectural modularity statement. The niveau-two weight is 1+pa+b with 0<=a<b<=p-1; the split niveau-one rule gives 1+pa+b apart from the specified (0,0) case.

I read Khare's author text pp.20–28 for the statements, local hypotheses, six pairs of FIRST/RETURN uses and the link-back; I also visually checked pp.20,21,26,27. Its PDF is pinned at 3012a51759ad10695792bc8a2d1af75890f38d6ebacd37fb61e01bfdb89c9c2f. This is explicitly an author version. No final-edition equivalence is asserted. The replacement retains the named elementary quadratic-discriminant and local-inertia background; this review is not a new source-edition audit of every such background fact.

## Independent mathematical checks

**Prime-to-p image.** A finite-order projective 2-by-2 matrix in characteristic p is either diagonalizable with prime-to-p eigenvalue ratio, or has one nontrivial Jordan block and projective order p. Thus a cyclic rotation subgroup with p-divisible order has order p and a unique invariant projective point. Its dihedral normalizer preserves this point, contradicting absolute irreducibility. The scalar kernel also has prime-to-p order, since a finite subgroup of the multiplicative group in characteristic p has no p-torsion. Therefore the full image is prime to p. Wild inertia vanishes, tame inertia is cyclic, and the restrictions used below are semisimple. Away from p, unipotent residual inertia must then be trivial. This last implication uses precisely Khare's residual meaning of semistable, not characteristic-zero semistability.

**Strict level one.** If t were even, the dihedral quotient C2 x C2 would give more than one quadratic field unramified outside the odd prime p, contradicting the discriminant formula. Hence t is odd. The rotation quotient is the unique quadratic character unramified outside p; it must ramify at p. Odd complex conjugation is a nontrivial projective involution, therefore a reflection, so this quadratic field is imaginary and p is 3 modulo4. Tame projective inertia is cyclic and surjects onto the rotation quotient: its generator outside the rotations has order2, so its image is exactly a reflection subgroup. Decomposition normalizes that subgroup, and the reflection centralizer for odd t is itself. Thus projective decomposition equals projective inertia of order2.

The linear preimage of this cyclic subgroup consists of scalars and scalar multiples of one matrix, so it is abelian. Its finite prime-to-p subgroup diagonalizes over a finite coefficient extension. The two characters have distinct inertia and quadratic ratio. The Frobenius relation for each local character makes its inertia a power of the mod-p cyclotomic character chi. A global chi twist removes one inertia character, leaving ratio chi^((p-1)/2). Serre's split digits are then (0,(p-1)/2), not (0,0); the weight is (p+1)/2. No conclusion about a characteristic-zero ordinary line follows from this argument alone.

**Cyclotomic-induced small weight.** The induced basis gives a cyclic projective diagonal subgroup and an off-diagonal reflection, with quotient the inducing quadratic character. Absolute irreducibility excludes the cyclic case. The preceding prime-to-p argument applies, including t=2. Since the inducing quadratic field is ramified at p, cyclic projective inertia contains a reflection and hence has order2. This does not use strict level one or odd t. The two distinct inertia eigenspaces cannot both have niveau one if the local representation is irreducible: Frobenius would preserve each. Thus Serre's niveau-two rule applies. Their ratio has order (p+1)/gcd(p+1,b-a). The actual inequality 1+pa+b<=p+1 forces a=0, since a>=1 implies b>=2 and weight>=p+3. Ratio order2 and 1<=b<=p-1 then force b=(p+1)/2, giving k=(p+3)/2. In particular the actual weight2 case is locally reducible. No silent cyclotomic twist or reduction of a larger weight is used here.

## All fourteen callers

| Caller | Actual local input supplied here | Retained boundary |
| --- | --- | --- |
| LEVEL1-WEIGHT-TRANSFER | Strict-level-one residual splitting and distinct inertia | Crystalline classification, weight2 exclusion, and lifting remain separate. |
| W8-FIRST | Weight2 excludes local irreducibility in the cyclotomic-induced branch, at ell=3 | A second ramified prime7 is allowed; no strict-level-one assertion. |
| W8-RETURN | Strict conclusion at P=7 once the recorded unramified-outside7 hypothesis holds | The finite twist and ordinary characteristic-zero line still require5.3. |
| W10-W12-FIRST | The same small-weight assertion at ell=5 | The original finite type at11 is not removed. |
| W10-W12-RETURN | Strict conclusion at P=11 | Same separate5.3 and lifting premises. |
| W14-W20-FIRST | The same small-weight assertion at ell=3 | Finite type at19 remains allowed. |
| W14-W20-RETURN | Strict conclusion at P=19 | Same separate5.3 and lifting premises. |
| W22-W30-FIRST | The same small-weight assertion at ell=7 | Finite type at29 remains allowed. |
| W22-W30-RETURN | Strict conclusion at P=29 | Same separate5.3 and lifting premises. |
| W32-FIRST | The same small-weight assertion at ell=5 | Finite type at31 remains allowed. |
| W32-RETURN | Strict conclusion at P=31 | Same separate5.3 and lifting premises. |
| GENERAL-FIRST | The same small-weight assertion for the chosen odd ell | No global unramified-outside-ell claim. |
| GENERAL-RETURN | Strict conclusion at P once the return system has the stated level | Same separate5.3 and lifting premises. |
| GENERAL-LINK-BACK | Reuses its actual FIRST partition at the fixed coefficient place | Shared residual objects do not identify characteristic-zero lifts; lifting and compatible-system transfer remain required. |

Each row applies only on the globally absolutely irreducible dihedral/cyclotomic-induced branch specified in the proof. Globally reducible and nondegenerate residual branches are not converted into this branch. The claim that cyclotomic restriction degeneracy yields the relevant inducing character remains the caller's stated input; this packet explicitly assumes induction where it is needed.

The original author p.26 calls its FIRST weight argument “Lemma5.1(i)” while using the numerical conclusion of5.1(ii). The new partition correctly supplies only the small-weight result there; it does not inherit the stronger strict-level-one hypothesis. This is a bounded citation/consumer correction, not a declaration that the original global theorem fails. All fourteen historical row bindings remain unchanged. No actual application to a second-prime FIRST member of the strict-level-one result was found in the new packet.

## Application obligations and limits

Source hypotheses and constructed objects match at the level explicitly claimed: odd p, finite residual image, absolute rather than coefficient-relative irreducibility, and the named ramification or induction hypotheses. The two domains are kept separate. The maps are the projectivization, rotation quotient, inertia/decomposition images and explicitly recorded chi twist. The consumed object is the same residual representation after only the declared coefficient extension or twist. Serre's digits, cyclotomic convention, and inertial ratio are read from the final source. Local splitting means splitting after a finite coefficient extension; no nonsplitting-field claim is made. The p=2, cyclic image, scalar inertia and larger-weight cases are excluded or treated explicitly, while t=2 remains available in the small-weight argument. Downstream only residual splitting/distinguishedness and the weight2 obstruction are accepted.

The checker verifies frozen source bytes, five proof spans and all fourteen canonical historical row hashes. These checks establish binding, not mathematical correctness or complete source coverage. There is no live manuscript edit or automatic adoption into the canonical register. The Khare final-version,5.3 BM/Savitt, full5.4/Cor5.5, solvable-image modularity, ordinary ordering and compatible-system qualifications remain exactly separate.
