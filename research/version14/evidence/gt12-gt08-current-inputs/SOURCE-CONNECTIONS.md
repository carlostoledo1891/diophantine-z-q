# Current GT12, GT14 and GT08 source connections

This author packet binds only the twelve source uses below. Existing proof text and historical decisions remain unchanged. Published source conclusions are separated from local repairs. LIN has no identified GT12 dependency and is excluded. GTZ, Hall, selection and cube imports belong to the other author.

## BASE-FORWARD
Source: Green and Tao, An inverse theorem for the Gowers U^3(G) norm; Proceedings of the Edinburgh Mathematical Society51 (2008),73–153; Forward Theorem10.11 pp124–125, equations10.7 and10.9; Theorem2.7, Corollary10.6 and Proposition10.10 in its proof. December2023 author notice identifies the false general quadratic-extension proposition. BASE uses its independently reviewed H={0} finite-box replacement; no backward theorem or skew-iterate result is imported.

Available statement: The forward prime-cyclic bracket theorem supplies a bounded-frequency bracket quadratic on a proper progression containing a Bohr set, with a positive shifted correlation for each nonempty subset of that progression. Hypotheses: P>2 prime and a fixed sufficiently small positive U3 lower bound eta. Range: Prime cyclic groups and the forward implication only. Conventions: Centered fractional-part representatives and cyclic averages. Exceptions: The proof chain uses the affected quadratic-extension assertion; only its H={0} proper-progression use is repaired locally here. No unmodified general extension theorem is accepted.

Current connection (GI-01-BASE2, 01-gi-base2 lines42–111): BASE42–65 imports only the forward cyclic bracket conclusion. BASE76–111 proves the H={0} specialization needed in Proposition10.10 by constant finite-box second differences, including side lengths1 and2, and converts its coordinate polynomial with the independent frequency lifts. This replaces the failed general extension step in the forward proof. It does not import the converse, Theorem12.9, or the erroneous skew iterate.

Separate inputs: Local finite-box specialization BASE76–111; Remaining GTZ polynomial closure and interval normalization are the other worker's slice..

## BASE-BOHR
Source: Green and Tao, An inverse theorem for the Gowers U^3(G) norm; Proceedings of the Edinburgh Mathematical Society51 (2008),73–153; Definition2.6 printed p84; Lemmas8.1–8.2 printed pp105–106; regular Bohr sets. December2023 author notice identifies the false general quadratic-extension proposition. BASE uses its independently reviewed H={0} finite-box replacement; no backward theorem or skew-iterate result is imported.

Available statement: A Bohr set has a radius-dependent positive density bound and a regular radius can be selected in a fixed comparable interval; at a regular radius, small relative radius changes change cardinality by O(d epsilon). Hypotheses: Fixed finite frequency set and admissible positive radius; regularity perturbation epsilon within its d-dependent range. Range: Finite abelian groups; radii and frequency count held fixed for the application. Conventions: Group cardinality normalization and the source Bohr distance to integers. Exceptions: Empty frequency set is the full group and is handled separately without division by d.

Current connection (GI-01-BASE2, 01-gi-base2 lines114–149): Choose a regular radius below the already supplied progression inclusion radius. Apply the forward correlation to that same Bohr subset. The displayed cutoff differs from its indicator only in the two-sided shell; choosing epsilon after b_star and d loses at most half the correlation. Density gives the positive cyclic lower bound. P alpha_j integral makes the product periodic. These smoothing/periodicity deductions are local, not extra claims of the Bohr lemma.

Separate inputs: BASE-FORWARD phase and subset correlation; Local cutoff construction; no universal cutoff derivative constant.

## DF-WEAK
Source: Green and Tao, The quantitative behaviour of polynomial orbits on nilmanifolds; Annals of Mathematics 175 (2012),465–540; One-variable Proposition9.2 pp522–523 with Theorem2.9 and Lemma6.7 pp501–502; GT14 pp1175–1176 preserves one-variable scope. Read with final2014 erratum: one-variable results retained, multiparameter application restricted to corrected equal-side theorem. Local right-period and affine repairs are kept distinct.

Available statement: In one parameter, failed quantitative total equidistribution admits the bounded horizontal-character obstruction and weak factorization construction of Proposition9.2; Lemma6.7 characterizes adapted polynomial maps by supported binomial coordinate coefficients. Hypotheses: Fixed dimension/degree, adapted rational Malcev basis, positive quantitative failure parameter with the basis rationality bound absorbed. Range: One variable only; the published2014 correction preserves this scope. Conventions: Binomial coefficients supported in G_r at degree r; real horizontal lift is used in the construction. Exceptions: No multi-parameter unequal-side theorem or single-scale equidistribution equivalence is imported; stronger local coefficient/real-kernel claims require the displayed argument.

Current connection (GI-05-DF, 05-gi-df lines104–180): DF113–131 extracts a standard discrepancy and normalizes g(0)=c lambda. The source obstruction is transferred from the witnessing dense progression by the independently accepted MF91–138 inverse-affine estimate, rather than an invalid bounded-height claim for O(N) offsets. DF133–178 splits supported coefficients into nearest-integer and small parts. Exact real horizontal zero, not merely circle zero, puts p in a connected proper kernel. Rational numerators may be unbounded. Local closure and right-period arguments are separately exposed.

Separate inputs: MF-AFFINE current MF91–138, accepted also for DF132–145; GTZ polynomial group closure; DF rational coordinate/period deductions.

## DF-COORDINATES
Source: Green and Tao, The quantitative behaviour of polynomial orbits on nilmanifolds; Annals of Mathematics 175 (2012),465–540; Lemmas A.2–A.3 pp526–528, Lemma6.7 pp501–502. Read with final2014 erratum: one-variable results retained, multiparameter application restricted to corrected equal-side theorem. Local right-period and affine repairs are kept distinct.

Available statement: For a fixed rational Malcev basis, first/second-kind coordinate changes, multiplication and inversion are fixed rational polynomial maps. Hypotheses: A rational Malcev basis for the fixed nilpotent group and its lattice. Range: Fixed finite dimension and nilpotency step. Conventions: GT12 Lemmas A.2–A.3 coordinate conventions; right lattice quotient. Exceptions: These polynomial laws alone do not assert small Taylor bounds, a period, or all-cover equidistribution.

Current connection (GI-05-DF, 05-gi-df lines181–260): DF192–216 scales n=Nt and applies the fixed coordinate polynomials. Triangular monomial/binomial conversion preserves O(N^-r); the formal-weight Taylor extraction, using the separately supplied group-Taylor convention, rules out lower-weight contributions. Bounded derivatives on the fixed compact scaled range give O(1/N). DF218–259 also uses these same rational laws to construct the weighted denominator lattice and the right-difference polynomial. The latter is a local replacement for the flawed left-coset inference in A.12, not an unmodified application of its proof.

Separate inputs: GTZ B9 group Taylor convention; DF218–259 local overgroup and right-period proof, separately accepted root orientation002.

## DF-BSG-PLUNNECKE
Source: Green and Tao, An inverse theorem for the Gowers U^3(G) norm; Proceedings of the Edinburgh Mathematical Society51 (2008),73–153; Theorems5.2–5.3, printed p95. December2023 author notice identifies the false general quadratic-extension proposition. BASE uses its independently reviewed H={0} finite-box replacement; no backward theorem or skew-iterate result is imported.

Available statement: A finite nonempty set with additive energy at least |A|^3/K has a large subset of bounded difference doubling; a finite set with difference doubling at most K has |kA-lA|<=K^(k+l)|A| for k,l>=1. Hypotheses: K>=1; high energy for Theorem5.2, bounded difference doubling for Theorem5.3. Range: Arbitrary additive groups as stated; applied here to a finite abelian product. Conventions: Energy counts ordered additive quadruples. Exceptions: No correlation premise or identification of the group with its dual is needed; Proposition5.4 is not used.

Current connection (GI-05-DF, 05-gi-df lines319–363): DF319–351 rounds into the actual product B x A with Q=100N+1 and M=ceil(1/e). The signed first coordinates and fixed target sum give a Fourier/Holder bound for the energy of any selected graph. Its size is at most3N and energy is bounded below by c2 N^3, so BSG applies with K depending only on c,C; Plunnecke with k=9,l=8 yields F2. Neither equal cyclic orders nor the specialized correlation premise of Proposition5.4 is assumed.

Separate inputs: Local rounding and Fourier/Holder energy calculation DF319–351; Later target-character separation DF364–396 is local, not a blind Lemma9.2 import.

## DF-BOHR-PROGRESSION
Source: Green and Tao, An inverse theorem for the Gowers U^3(G) norm; Proceedings of the Edinburgh Mathematical Society51 (2008),73–153; Lemma6.4 pp97–98; Lemma10.4 and its lattice-lift proof p121 (using10.3). December2023 author notice identifies the false general quadratic-extension proposition. BASE uses its independently reviewed H={0} finite-box replacement; no backward theorem or skew-iterate result is imported.

Available statement: A positive-density subset of a finite additive group has a Bohr set B(S,1/4) in2A-2A with bounded |S|; a Bohr set contains a large proper coset progression whose real frequency generators are independent and add exactly in its lattice lift. Hypotheses: Positive density for Bogolyubov; finite frequency set and admissible positive radius for the progression construction. Range: Finite groups including composite cyclic groups. Conventions: The progression has exact lifted coordinates in the real frequency cube; the subgroup is the common annihilator. Exceptions: The subgroup need not vanish in general; that is obtained only after adding a faithful character in the current cyclic application.

Current connection (GI-05-DF, 05-gi-df lines364–433): The local separation argument DF364–396 constructs an exact Freiman map on2H_doubleprime-2H_doubleprime into the actual cyclic target, without identifying that target with the dual of B. Apply Bogolyubov to H_doubleprime in B=Z/Q. Add x/Q, making the annihilator zero, and take radius1/16. The source progression has independent real lifts. Delete inactive generators; centered coordinate paths stay in P, so local additivity integrates. Dual real vectors give F4. No quadratic extension or classification is imported.

Separate inputs: DF364–396 actual-target graph refinement; No GT08 Proposition3.2/10.7 use here.

## MF-EQUAL-CUBE
Source: Green and Tao, On the quantitative distribution of polynomial nilsequences—erratum; Annals of Mathematics 179 (2014),1175–1183; Corrected equal-side theorem, printed pp1176–1177; smoothness norm p1177; minor errata pp1182–1183. Final published erratum only; no unpublished arbitrary-side extension.

Available statement: On an equal cube [N]^t, a polynomial orbit in an m-dimensional rational filtered nilmanifold is delta-equidistributed or has a nonzero bounded horizontal character whose product-binomial C-infinity norm is bounded. Hypotheses: 0<delta<1/2; a 1/delta-rational adapted basis; integers m,t,N,d>=1. Range: Equal side lengths only; integer parameters >=1 visually verified on printed1176. Conventions: C-infinity norm is sup over alpha!=0 of N^|alpha| times the circle norm of the product-binomial coefficient. Exceptions: The original arbitrary-side theorem is not imported; zero-dimensional trivial groups are handled outside the failure case.

Current connection (GI-06-MF, 06-gi-multifactor lines139–173): MF147–161 subtracts the Haar mean, rotates to positive real discrepancy and tiles the dense progression index rectangle by equal cubes. Choose eta after discrepancy so discarded remainder is harmless. On the chosen cube apply exactly the published equal-side theorem, with error below both discrepancy and the reciprocal rationality bound. Finitely many bounded integer vectors make the character standard. MF-AFFINE, not the published unequal-side claim, transfers it to the original variables afterwards.

Separate inputs: MF91–138 inverse-affine transfer; Polynomial precomposition and support via GT12 Lemma6.7; Later factor construction not supplied by the obstruction theorem alone.

## MF-SUPPORTED-COEFFICIENTS
Source: Green and Tao, The quantitative behaviour of polynomial orbits on nilmanifolds; Annals of Mathematics 175 (2012),465–540; Lemma6.7 and Corollary6.8, pp501–502. Read with final2014 erratum: one-variable results retained, multiparameter application restricted to corrected equal-side theorem. Local right-period and affine repairs are kept distinct.

Available statement: Adapted polynomial maps have Malcev-coordinate binomial expansions whose coefficient at multiindex alpha is supported in the coordinates for filtration layer G_|alpha|, and the converse holds. Hypotheses: Fixed rational Malcev basis adapted to the finite-degree filtration. Range: Finite positive parameter count; total multiindex size, not the maximum coordinate index. Conventions: Product-binomial coefficients; the support is G_|alpha|. Exceptions: The characterization does not itself supply a horizontal obstruction or delete rational Taylor terms.

Current connection (GI-06-MF, 06-gi-multifactor lines175–198): MF175–190 normalizes the constant and uses the source support characterization to place t_alpha in G_|alpha|. The selected w_alpha,z_alpha remain in that coordinate subspace, so the converse characterization makes their maps polynomial. The real lift cancels exactly in the ordered middle factor, giving a connected real kernel. Closure under products is a separately registered GTZ input; the coordinate theorem alone is not asked to prove it.

Separate inputs: MF-EQUAL-CUBE obstruction; MF-AFFINE; GTZ polynomial group closure.

## MF-COORDINATES
Source: Green and Tao, The quantitative behaviour of polynomial orbits on nilmanifolds; Annals of Mathematics 175 (2012),465–540; Lemmas A.2–A.3 pp526–528, with Lemma6.7 coordinate degree. Read with final2014 erratum: one-variable results retained, multiparameter application restricted to corrected equal-side theorem. Local right-period and affine repairs are kept distinct.

Available statement: For a fixed rational Malcev basis, first/second-kind coordinate changes, multiplication and inversion are fixed rational polynomial maps. Hypotheses: A rational Malcev basis for the fixed nilpotent group and its lattice. Range: Fixed finite dimension and nilpotency step. Conventions: GT12 Lemmas A.2–A.3 coordinate conventions; right lattice quotient. Exceptions: These polynomial laws alone do not assert small Taylor bounds, a period, or all-cover equidistribution.

Current connection (GI-06-MF, 06-gi-multifactor lines201–250): MF202–225 applies rational polynomial laws to scaled variables and the separately supplied Taylor extraction. MF227–234 constructs the BCH-closed weighted denominator lattice. MF236–250 interpolates gamma on a fixed integer grid and forms the correctly ordered R_i. Since R_i(n,0)=0, every monomial contains r; a common denominator q makes each R_i(n,q) integral. This proves the right-coset period without the flawed orientation in the source A.12 proof. Least-dimension descent and common-core conclusions remain later local steps.

Separate inputs: GTZ B9 Taylor convention; MF weak factor construction; Local weighted denominator and right-period arguments.

## MF-LATTICE-LOGARITHMS
Source: Green and Tao, The quantitative behaviour of polynomial orbits on nilmanifolds; Annals of Mathematics 175 (2012),465–540; Definition2.1 and remarks p478; Lemma A.2 pp526–527. Read with final2014 erratum: one-variable results retained, multiparameter application restricted to corrected equal-side theorem. Local right-period and affine repairs are kept distinct.

Available statement: The ambient lattice has integer second-kind coordinates, and the change between first-kind logarithm coordinates and second-kind Malcev coordinates is a fixed rational polynomial map. Hypotheses: A connected simply connected nilpotent group with a rational Malcev basis relative to Gamma. Range: Fixed finite dimension and nilpotency step. Conventions: Definition2.1 integer second-kind lattice convention and Lemma A.2 coordinate conversion. Exceptions: The source only gives rational logarithm coordinates; Lie rationality from subgroup compactness remains the separate local argument.

Current connection (GI-06-MF, 06-gi-multifactor lines369–386): Definition2.1 makes lattice second-kind coordinates integers; A.2 therefore makes their logarithms rational. MF373–382 proves that their Lie span is the entire subgroup Lie algebra: a proper maximal nilpotent subalgebra would be a codimension-one ideal, yielding a surjection H->R that kills the lattice, contrary to compactness. Rational linear algebra identifies the intersection Lie algebra. The independent integration review checked this exact reverse direction; it is not a backward use of A.10.

Separate inputs: Given compact lattice quotients for P and G_d; Local maximal-subalgebra/compactness proof MF373–382.

## MF-INTERSECTION-LATTICE
Source: Green and Tao, The quantitative behaviour of polynomial orbits on nilmanifolds; Annals of Mathematics 175 (2012),465–540; Definitions2.1,2.3,2.5 pp478–480 and Proposition A.10 p534. Read with final2014 erratum: one-variable results retained, multiparameter application restricted to corrected equal-side theorem. Local right-period and affine repairs are kept distinct.

Available statement: A closed connected Lie-rational subgroup with a rational filtration admits a Malcev basis relative to its actual intersection with the ambient lattice. Hypotheses: GT12 Definition2.5 rational Lie basis with bounded rational height; ambient adapted rational basis; rational subgroup filtration. Range: Fixed finite dimension and step; a suitable finite rationality bound Q is chosen for the actual data. Conventions: Proposition A.10 supplies a basis for H/(H intersect Gamma); Definition2.1 identifies the associated integer coordinate lattice. Exceptions: Lie rationality is a premise and must be proved without assuming the desired compact quotient. Trivial subgroup is immediate.

Current connection (GI-06-MF, 06-gi-multifactor lines383–399): MF383–390 uses rational linear algebra and global exponential/BCH to obtain the exact closed connected K and rational lower-central filtration. Choose a finite standard Q for that actual data, apply A.10 and Definition2.1 to K intersect Gamma. MF392–394 injects its coset set into (P intersect Gamma)/Delta, proving finite index without normality. The later quotient uses this same K and the separately retained central-quotient lemma.

Separate inputs: MF-LATTICE-LOGARITHMS reverse rationality argument; LP13 central-quotient lemma; All-limit vertical identity for the actual vector.

## RANK-SUBGROUP-LATTICES
Source: Green and Tao, The quantitative behaviour of polynomial orbits on nilmanifolds; Annals of Mathematics 175 (2012),465–540; Definitions2.1,2.3,2.5 pp478–480 and Proposition A.10 p534. Read with final2014 erratum: one-variable results retained, multiparameter application restricted to corrected equal-side theorem. Local right-period and affine repairs are kept distinct.

Available statement: A closed connected Lie-rational subgroup with a rational filtration admits a Malcev basis relative to its actual intersection with the ambient lattice. Hypotheses: GT12 Definition2.5 rational Lie basis with bounded rational height; ambient adapted rational basis; rational subgroup filtration. Range: Fixed finite dimension and step; a suitable finite rationality bound Q is chosen for the actual data. Conventions: Proposition A.10 supplies a basis for H/(H intersect Gamma); Definition2.1 identifies the associated integer coordinate lattice. Exceptions: Lie rationality is a premise and must be proved without assuming the desired compact quotient. Trivial subgroup is immediate.

Current connection (GI-10-RANK, 10-gi-rank lines59–73): RANK59–68 verifies rationality by rational brackets, the ideal property by weights, and closed connectedness by the exponential homeomorphism. Its rational lower-central layers and finite Q meet A.10. The supplied basis is relative to the actual lattice intersection, which is therefore discrete and cocompact. The later refinement retains the original orbit and top character; this source use does not certify the rank-decrement analytic input.

Separate inputs: Rational ordinary-degree input geometry; Local bracket-weight and exponential argument; Later rank iteration remains separate.
