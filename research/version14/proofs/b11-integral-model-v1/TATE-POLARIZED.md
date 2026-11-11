# Tate and polarized-automorphism inputs for B11

This is an author source/application proposal, not an independent decision. Let k be algebraically closed of characteristic different from 3, A/k an abelian surface, and lambda a polarization. Automorphisms mean group automorphisms preserving the identity. We include positive characteristic; no complex uniformization or lifting to characteristic zero is used.

## 1. Exact published inputs

Milne, *Abelian Varieties*, Chapter V of *Arithmetic Geometry*, Springer (1986), pp.103-150, is available as the author's scan of the published chapter. The distinct January 2, 2022 corrected version and the author's errata page were also inspected. They are not relabelled as the 1986 edition.

The needed statements in the final scan are: Theorem 8.2 and Remark 8.4, pp.115-116 (prime-to-characteristic torsion and Tate rank); Proposition 12.1 and Lemma 12.2, p.122 (isogeny decomposition and faithful Tate action); Proposition 12.4, p.123 (polynomial degree); Lemma 12.6, p.124 (divisibility of homomorphisms); the trace convention, p.125; Theorem 17.3, pp.138-139 (Rosati positivity); and Proposition 17.5(a), p.139 (finite polarized automorphism group). These are general abelian-variety statements.

## 2. The three-marking input

Apply Remark 8.4 with g=2 and l=3. Thus T_3(A)=lim A[3^n](k), with transition multiplication by 3, is free of rank 4 over Z_3, and V_3(A) has dimension 4 over Q_3. The first projection induces T_3(A)/3T_3(A)=A[3](k). Indeed, points have compatible successive 3-division lifts over k, giving surjectivity. A compatible sequence with first term zero is three times the sequence obtained by shifting its terms one place; the shifted nth term is then killed by 3^n. This proves the kernel assertion.

The given unital O action acts on this inverse system and extends continuously to O_3 on its finite free Tate module, and then to B_3 on V_3(A). Since B_3 is a division algebra, a unital action on the nonzero space V_3(A) has zero kernel: the kernel is a two-sided ideal and cannot contain 1. A left vector space over B_3 is free. Its dimension over Q_3 is its B_3-rank times dim_Q3 B_3=4. Consequently that rank is one.

General faithfulness of End(A) on T_3 is not needed for this division-algebra argument. The subsequent maximal-order lattice argument, the sheaf of markings, and descent are separate B11 inputs.

## 3. Faithfulness needed by the stabilizer argument

Use final Lemma 12.2 with B=A and l=3. If two endomorphisms agree on T_3(A), their difference is zero. In particular, an automorphism acting identically on T_3(A) is the identity on A. This is injectivity for actual endomorphisms; it does not require a Tate conjecture or surjectivity onto all Tate-module endomorphisms.

For clarity, its proof is separate from Theorem 12.5. A map with zero Tate action kills every A[3^n](k). On a nonzero simple abelian subvariety S, a nonzero map has finite kernel, whereas S[3^n](k) has unbounded cardinality 3^(2n dim S). The restriction must therefore be zero. An isogeny from a product of simple abelian varieties onto A, supplied by Proposition 12.1, proves that the original map is zero. The official imperfect-field qualification to the printed proof of Proposition 12.1 does not arise: k is algebraically closed, hence perfect.

## 4. The recorded correction in the endomorphism-lattice proof

The official errata page expressly flags the proof of Theorem 12.5 on p.124 and points to the corrected text. The printed inference that finite rational dimension and torsion-freeness alone imply finite generation is not used. The following bounded argument supplies the finite-generation step needed in the proof of Proposition 17.5(a). It follows the corrected argument's degree-polynomial and divisibility route, with the final finite-generation deduction explicit.

First let S be simple, and let M be a finitely generated subgroup of End(S), with Z-basis e_1,...,e_r. Torsion-freeness follows from Lemma 12.2. Put V=Q M and D=V intersect End(S). The degree polynomial P from Proposition 12.4 restricts to a real polynomial on V tensor R. Every nonzero element of D is an isogeny and has positive integer degree. Hence the open neighborhood P<1 of zero contains no nonzero point of D. Because D is an additive subgroup, this also gives a uniform separation between distinct elements. A compact fundamental parallelepiped for M contains only finitely many D-points, so D/M is finite. There is an integer N_M>0 with N_M D contained in M.

Suppose sum a_i T_3(e_i)=0 with a_i in Z_3, not all zero. For each m choose integers n_i congruent to a_i modulo 3^m. Then sum n_i T_3(e_i) is divisible by 3^m as a Tate-module homomorphism. Lemma 12.6 gives v_m=3^(-m) sum n_i e_i in End(S), and therefore v_m in D. It follows that every N_M n_i/3^m is an integer. Choose j with a_j nonzero and m>v_3(N_M)+v_3(a_j). Since v_3(n_j)=v_3(a_j), that integrality is impossible. Thus the Tate images of e_i are Z_3-linearly independent, and r is at most (2 dim S)^2.

Every finite independent set in End(S) has this same bound. Therefore Q End(S) is finite dimensional. Choose M spanning it over Q and repeat the preceding D/M argument. Now D=End(S), so End(S) is finitely generated. This supplies the missing inference without asserting that an arbitrary torsion-free group of finite rank is finitely generated.

For general A, choose an isogeny between A and a product of simple factors. Pre- and post-composition with suitable isogenies inject End(A) into the endomorphisms of that product. Its matrix entries are Hom(S_i,S_j). Such a group is zero for nonisogenous simple factors; otherwise composition with a fixed isogeny S_j to S_i injects it into End(S_i). Subgroups of finitely generated free abelian groups are finitely generated and free. Hence End(A) is a finite free Z-module and is a lattice in End(A) tensor R.

No claim about the cokernel of the Z_3-tensored Hom map is needed here. The prime-to-characteristic divisibility lemma and the polynomial degree and isogeny-decomposition statements remain named published inputs.

## 5. Polarized automorphisms

For a group automorphism alpha preserving lambda, the identity alpha^vee lambda alpha=lambda gives alpha^dagger alpha=1 for the Rosati involution. Theorem 17.3 says q(x)=Tr(x^dagger x) is positive definite. The trace convention gives q(alpha)=Tr(1)=2 dim A=4. The real q-sphere of radius squared 4 is compact, and its intersection with the lattice End(A) is finite. Thus Aut(A,lambda) is finite, as asserted in published Proposition 17.5(a), now with the corrected lattice step exposed.

This uses neither Proposition 17.5(b) nor its level-n argument. It concerns pointed polarized automorphisms, not arbitrary translations of the underlying variety. No bound on the order of this finite group is asserted.

## 6. Actual B11 consumption and limits

At THREE-MARKING, use Section 2 for rank 4 and rank one over B_3. At FIVE-ACTION-FREE, use Sections 3 and 5: a stabilizer gives a polarized group automorphism of finite order; its full three-marking puts its Tate matrix in 1+3M_4(Z_3). The manuscript's separate odd-prime binomial argument then makes that matrix the identity, and Tate faithfulness makes the automorphism the identity. The last full-five marking step is unchanged.

The exact historical consumers are manuscript925967 lines708-721 and723-731, already transported to candidate040646 by the independent six-phase review. This packet does not refresh their pins to a later manuscript. Finite-etale Isom representability, scheme-level torsion, local division-order lattices, free quotients, descent, and the normalizer degree calculation remain separate. All source corrections above are bounded to the inputs actually used here; no whole-chapter or whole-B11 acceptance is claimed.
