# Independent review of the 330-variable strong-H detector

I accept this exact construction as a reduction from accepted366 on its explicitly retained arithmetic premises. The four-group construction and the stronger H slot were checked together directly against366. I do not assume acceptance of the intermediate332 candidate.

Reviewer `/root/sol_protocol_final_review`, November 7, 2026. Author `/root/astra_quartic_opt03_depth`. I did not author or substantively repair these candidate equations or proofs. Exact serving-model metadata is not independently attested.

## Bound artifacts and independent finite checks

The candidate report has SHA-256 `a90fe9b838dba89e77ee54672c42fbc60b669924032ccfc780bc2e531fef90b8`. The IR has SHA-256 `41602bf9d25d52ae6e461f958eb21e1d752190ef71a72c1cc7c444f4e0a9fff6`. The polynomial has SHA-256 `c4fcd50ed0322c4e7b0ce6bf48bed6e2321e5d8610c061bb4dd1ac4e56981f81`. Accepted366's IR remains `0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56`.

I read both the330 and332 reports, the actual330 and366 equations, and the verifier. The inherited domain correction, source366 parity proof, guard-free369 proof, Kummer and biquadratic proofs, and manuscript CRT/real-density passages were also inspected during my immediately preceding340 review. Their applications here were checked anew for the changed groupings. That340 review remains unchanged and supplies no acceptance of332.

The independent checker in this directory reuses my sparse-rational arithmetic from the340 audit and reconstructs all55 new rows directly from366. It verifies every removed-coordinate consumer, all retained coordinate objects and outside rows, field normalization of every high/middle square, cached alternate powers, all old and new required weight exponents, the full source366 sign involution, and the generic-H polynomial identity. It independently expands every primitive residual square and compares all5792 coefficients. It also checks the secondary332 delta as a separate factual comparison. The latter removes only coordinates824/825 and rows737/738 and changes twelve component rows for groups0/2.

CHECKS.json records330 active coordinates,329 witnesses,300 quadratic residuals,5792 quartic monomials, degree four and content one. C-independent coefficients have at most1520 bits and C-linear coefficients have magnitude at most96. The unique C² coefficient remains16 on its unchanged monomial, so the maximum is16C² for C=3^(2^25). I replayed the author verifier with its only output redirected into this directory. All author files remained byte-identical, as recorded in AUTHOR-UNMODIFIED.json.

## Four groups and their actual meanings

The exact groups are

```text
G0 = 1 + E^79 H4² + E^158 H2^4 + E^4 P1² + E^8 T0
G1 = 1 + E^79 H1² + E^158 H3^4 + E^4 P2² + E^8 T2
G2 = 1 + E^19 M0² + E^158 H0² + E^4 P3² + E^8 T3
G3 = 1 + E^19 M1² + E² P4 + E^4 Z1 + E^8 T4.
```

Here P_i=f(U_i)², Z1=conjugate(f(V1)^4), T_j=conjugate(f(V_j)^8), H0=f(H), H1,H2,H3 are the retained cross-log differences, H4 is the retained Lucas polynomial and M0,M1 are the two middle comparisons. All sixteen old tests occur. The stored affine H4² and translated M1², including beta and15321, match their literal source square equations.

The V1 cache is normalized. Its actual w² is193v192-132ρv193. Dividing by D² and conjugating gives exactly Z1. The other four caches are w⁴ with ordinary field components; dividing by D⁴ and conjugating gives T0,T2,T3,T4. No new alternate root or inverse is assumed. The two high fourth powers and three primary square powers cost ten rational components; three E4 gates cost three more. Against366,49 old coordinates disappear and13 new ones appear, giving330. The norm and B consumers retain their old W coordinate pairs and exact equations.

## H valuation and exceptional domains

The new H0² slot requires valuation in4Z. This holds before interpreting the H-P difference. On the generic squared-H branch, the retained equations recover nonzero f, F with fF=v² and the Kummer relation. With c=a² and S=(b+ct+Dft)/a, the denominator-cleared identity checked independently gives S²=1/f-Df without dividing by c+Df. Consequently (1/f,S/f) is a genuine curve point.

At each consumed unramified prime p>76176, D is a unit. The equation y²=x(x²-D) gives even v(x), separately for positive, zero and negative v(x). Thus v(f) is even and v(U)=2v(f) lies in4Z. If F is nonzero, fF=v² gives even v(F), hence v(T0) lies in16Z. If F=0, that term vanishes.

On U=0, the H0² term is zero and T0 is a fixed unit. On Q=0, U=V=-v² for one of the two explicit fixed unit values, so v(U)=0 and T0 is again a unit. Their placewise unit property follows from the same fixed denominators and norms used in the inherited354 correction. No fourth root of an arbitrary nonsquare is asserted.

The other primary and difference outputs are fourth powers from the unchanged biquadratic identities, including their zero branches. Therefore P_i has4-divisible valuation, P_i² and Z1 have8-divisible valuation, and T_j has16-divisible valuation. H2^4 and H3^4 are actual fourth powers of retained field expressions. H4² and both middle squares are actual squares. These facts give every slot its required multiplicity without a premature logarithm or height conclusion.

## Same-place soundness

At a required contact prime, α=v_p(R)>0 is odd and1+R is a unit. In each group the nonconstant valuations occupy the disjoint classes odd,2 modulo4,4 modulo8 and8 modulo16, beside constant class zero. For G2, H0² uses its proved4Z valuation with weight158. For G3, P4 uses4Z with weight2. I checked all odd residue representatives modulo16 independently. Zero summands can be omitted and the unique minimum persists. Thus every G is nonzero with nonpositive valuation.

Set W to their product. Its nonzero value and retained norm equation force Re(W) and z nonzero, so T=Tr(W^-1)=1/z. Trace integrality gives v_p(T)≥-Λ for Λ=max v_w(W). The retained B equation gives v_p(B)≤α+2Λ. Since v_p(B) is odd and the pole obstruction excludes negative odd valuation, Λ>-α/2.

At one place attaining Λ, each G has valuation at leastΛ because the other factors have nonpositive valuation. Every nonzero summand is therefore greater than-α/2 at this same place. The weight79 square forces H1,H4 to order40, and weight158 fourth powers force H2,H3 to order40. The weight158 H0² term forces v(U)≥160, hence v(f)≥80 in the generic branch. The middle squares force order10. The8-divisible slots force valuation at least8, P4 at least4, and the T slots at least16, giving all low reciprocal tests order at least2. All original orders hold simultaneously; no per-test choice of place is combined.

A unit T0 on either exceptional pre-H branch contradicts its forced positive valuation at every required prime. All three radicals would be one, which the retained pre-H anchor/parity and root-height argument excludes. The later H/V0 exceptional-point exclusions and logarithm, Lucas, scalar24 and input-integrality consumers receive their original hypotheses. Radical-free detectors still require no trace interpretation. In particular, no removed global W inverse is reinstated, and zero or infinite-valued test cases are covered by omitting zero summands and retaining the constant term.

## Completeness with primary depth40

The source depth20 is insufficient for the new H0² term, and I do not use it as if it were40. Replace Π^19 byΠ^39 only in the primary h congruence. The actual manuscript coprimalities give gcd(Π,M+)=gcd(Π,L)=1, gcd(M-,M+)=1, gcd(M-,L)=16 and gcd(M+,L)=1. The h0 compatibility condition is unchanged. No extra divisibility is imposed on h-1.

The original reduction-order multiple is formal with depth at least1. Multiplication by p^39 then gives depth at least40 under the inherited unramified formal-logarithm isometry. Thus v(f(H))≥80 and v(H0²)≥160. Integral multiplication by each integer root label preserves this subgroup; negative labels are allowed and zero labels give zero reciprocal tests. Opposite-place congruences and their alternate truncation precision remain unchanged.

At a selected successful place α=1, the nonconstant margins in every group are at least1,2,4,8. All G have residue one there. At the other place, uniqueness gives inverse residue zero or one; the trace is a unit of residue one or two. The inert case has residue trace two. Hence B has positive odd valuation one at selected primes. Away from those primes the inherited even v(R) and denominator squares give square reduced denominator, including any new prime divisors of the sums.

The strengthened congruence is chosen in the existing order. Scalar data, roots, scales, initial H, finite neighborhoods, L and a compact real neighborhood avoiding comparison poles are fixed before the contact primes. The new powers are uniformly bounded on these same neighborhoods. Π^39 changes the final progression but preserves the required residue and modulus divisibility by m0. Its dense positive tail therefore still meets the chosen real neighborhood while preserving h modulo L.

At2,3,17 all positive E exponents make the new nonconstant terms tend to zero as the prescribed denominator divisibility grows. W tends to one and T to two with the required local precision, preserving the squareclasses and attaining the preparation-zero thresholds. At both real embeddings the complete-witness terms are nonnegative. Large positiveλ gives W,T positive and B tending to zero positively. Oneλ bound handles all three scales. The retained pole-realization theorem then supplies fresh pole witnesses for the same final H.

## Scope of acceptance

No unresolved defect was found in the366-to330 reduction. Its integer-input projection is accepted relative to the same inherited arithmetic inputs as366 and my340 review. These include the elliptic label/domain theorems, contact-height bound, restricted-converse-dependent pole theorem, preparation-zero realization, scalar/anchor bounds, formal-logarithm result, simultaneous-prime/separation and real-density results, and final Lucas implications. Their full proofs and underlying published-source versions were not independently re-audited here. The existing qualifications remain in force.

This review certifies neither the entire manuscript under the full research protocol nor publication readiness. The below300 threshold remains unmet. All previous340 review artifacts, author artifacts and released files remain unchanged. Run `python -B work/quartic-optimization-20261107/resume-sol-review330-20261107/check.py` from the workspace root with a recorded compatible Python interpreter to reproduce the finite audit.
