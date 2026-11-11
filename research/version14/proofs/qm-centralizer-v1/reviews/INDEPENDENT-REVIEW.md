# Independent review of the centralizer calculation

Decision: accept the exact algebra lemma and its conditional application at ed992 lines575-583. The wider consumer span575-588 also includes geometric consequences; acceptance of this algebra does not supply those consequences.

## Independence and scope

I did not author qm-centralizer-author-sol-001 or contribute a repair to it. I authored the earlier B11 Tate-module and endomorphism-lattice packet. That packet concerns a different interface, including positive-characteristic Tate faithfulness, and is not invoked here. This decision does not independently reapprove my B11 work.

I read all27 lines of the frozen proof, the one use/connection, all nine obligations, the index and merge records, and the actual manuscript context556-588. I checked the deductions below rather than treating file verification as proof review.

## Algebraic proof checks

1. Scalar-extension simplicity. Choose minimal tensor length among nonzero elements of the nonzero two-sided ideal. After choosing independent scalar coefficients, simplicity over E makes a finite sum b_j a_1 c_j equal1. The replacement remains nonzero because its coefficient at the first independent scalar is1. A commutator has at most one fewer terms, so minimality makes it zero. Linear independence then places every coefficient in the center E. The resulting nonzero scalar in K is invertible. Thus the ideal is the entire scalar extension. This proves the needed simplicity without assuming the centralizer formula.

2. Splitting over the algebraic closure. Each nonzero right translate of a minimal left ideal is a simple isomorphic left module. A translate not contained in the accumulated sum has zero intersection with it. The sum of all translates is a nonzero two-sided ideal and hence the full algebra; finite dimension makes the direct-sum selection terminate. A module endomorphism of the minimal ideal is either zero or invertible. An eigenvalue over K makes its difference from a scalar noninvertible, proving that the endomorphism algebra is K. Endomorphisms of the regular left module give the opposite algebra. Transposition removes the opposite, so Delta_K is a full matrix algebra of an integer size d, and dim_E Delta=d^2.

3. Field-idempotent ranks. Characteristic zero makes C/E separable. After extension, its m primitive idempotents are nonzero because tensoring the inclusion is injective. They split K^n. Automorphisms of an algebraic closure over E act transitively on the embeddings of C; their semilinear action preserves the dimensions of A_K e. In M_n(K) that left ideal has dimension n times the rank of e. All ranks are therefore the same positive integer r, and n=mr.

4. Centralizers and dimensions. Commuting with an E-basis of C is a finite system of linear equations. Field extension preserves its kernel. Hence the centralizer after extension is precisely C_K. In the idempotent decomposition, commuting matrices preserve each summand, with arbitrary endomorphisms within it. Their dimension is m r^2. Comparison with dim_K C_K=m gives r=1 and m=sd. This argument neither assumes that C is Galois nor assumes that Delta is split beforehand.

5. The same module. The matrix units split the unital module V into s isomorphic summands. None is zero because V has C-dimension one and is nonzero. A summand is a finite left Delta-vector space of positive integer dimension h. Thus dim_E V=s h d^2. The identical V also has dimension [C:E]=sd. Cancellation yields h d=1, so h=d=1. The central inclusion E into the one-dimensional E-algebra Delta is then an isomorphism.

## Actual consumer and retained inputs

The manuscript first constructs the same unital field C action on Y, with [C:Q]=dim Y. The preceding characteristic-zero differentiation argument embeds A=End_Q^0(Y) into End_Q(Lie Y). The resulting Lie module V has C-dimension one. Its C-linear endomorphisms are C itself, so the centralizer inside A is exactly C. This is the actual Lie representation, not a Tate representation or a selected submodule.

Poincare reducibility is a retained prior geometric input giving finite-dimensional semisimplicity of A. Its center embeds into C, because central elements commute with C. A finite-dimensional commutative semisimple algebra has a product decomposition into fields; the absence of nontrivial idempotents inside C leaves one field E. The usual simple-algebra decomposition therefore supplies the stated A=M_s(Delta). These are the input interfaces already stated in the proof and manuscript; this decision does not reprove Poincare reducibility or the preceding construction of Y.

The algebra conclusion matches lines578-583: [C:E]=sd, dim_Q V=h s d^2[E:Q], and Delta=E. Lines583-588 additionally realize rational matrix idempotents as abelian factors and identify their endomorphism algebra. Those geometric steps remain separate. The source-use statement correctly stops at A=M_s(E), even though its recorded consumer span extends through588.

## Adverse cases and records

A self-centralizing field alone does not imply Delta=E: a maximal subfield of a nonsplit quaternion division algebra is a counterexample. The nonzero rank-one C-module is essential and is explicitly retained. A higher C-rank module would give a different integer identity, so no such generalization is accepted. Inseparable extensions are excluded by characteristic zero. Matrix size and field degree must be positive; no zero-module division occurs.

The nine obligation entries retain their input hypotheses and left-module conventions. The canonical proof path is a proposed alias of the exact author proof, not an assertion that it is already installed. The single use digest, supplier and consumer locations, available/needed assertions, and edge agree. Index status is author metadata; this decision accepts the named algebra use and does not certify that every mathematical assertion within the broad consumer span is covered.

No correction is requested. Full QM descent, abelian images, cohomology comparison, modularity, other source qualifications, current integration, and release remain outside this decision.
