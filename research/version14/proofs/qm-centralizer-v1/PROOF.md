# Centralizer calculation in the primitive-factor reduction

This proof supplies the finite-dimensional algebra step used after the rational Poincare decomposition in the scalar-descent lemma. It assumes that decomposition and the stated centralizer and Lie-module identities. It does not construct the abelian images of rational idempotents or supply the subsequent modular cohomology comparison.

## Statement

Let E be a characteristic-zero field. Let A=M_s(Delta), where Delta is a finite-dimensional central division algebra over E. Let C/E be a finite field extension embedded unitally in A and suppose that the centralizer of C in A is C. Put m=[C:E]. Then dim_E(Delta)=d^2 for a positive integer d and m=sd. If a unital left A-module V is one-dimensional over C, then d=1 and A=M_s(E).

## Scalar extension and matrix size

Let K be an algebraic closure of E. For any finite-dimensional central simple E-algebra S, the algebra S_K=S tensor_E K is simple. To see this, take a nonzero element x of a nonzero two-sided ideal J of S_K with the fewest terms in an expression x=sum_i a_i tensor lambda_i. The coefficients lambda_i can be taken E-linearly independent. Choose a_1 nonzero. Simplicity of S gives b_j,c_j in S with sum_j b_j a_1 c_j=1. Replacing x by y=sum_j b_j x c_j puts coefficient 1 at lambda_1, so y is nonzero. For every a in S, the commutator [a,y] belongs to J and has an expression with at most one fewer term. Minimality forces it to vanish. Independence of the lambda_i makes every coefficient of y central in S. Thus y is a nonzero scalar in K and J is the whole algebra.

A finite-dimensional simple algebra T over the algebraically closed field K is a matrix algebra. Choose a minimal nonzero left ideal L. The sum of its right translates L t is a nonzero two-sided ideal, hence equals T. Each nonzero translate is a simple left module isomorphic to L. Choose successively translates outside their current sum. A new translate has zero intersection with the sum by simplicity, so this gives T as a finite direct sum of copies of L. Every nonzero T-endomorphism of L is invertible. Such an endomorphism has a K-eigenvalue because L is finite-dimensional over K. Subtracting that eigenvalue times the identity gives a noninvertible endomorphism and therefore zero. Thus End_T(L)=K. Computing End_T(T) from the direct sum and from right multiplication identifies T^op with a matrix algebra over K. Transposition gives the same conclusion for T.

Apply this to Delta_K. It is M_d(K) for a positive integer d, so dim_E(Delta)=d^2 and A_K=M_{sd}(K). Write n=sd.

## Ranks of the field idempotents

The extension C/E is separable, so C tensor_E K is a product of m copies of K indexed by the embeddings of C in K. Its primitive idempotents are nonzero pairwise orthogonal projections on K^n, with sum 1. The automorphisms of K over E permute the embeddings transitively. Their semilinear action on A_K permutes the idempotents and preserves the dimensions of the left ideals A_K e. For an idempotent of rank r, that left ideal has dimension nr over K. Hence every primitive idempotent has the same rank r, and n=mr.

Taking the centralizer of C commutes with extending scalars, because it is the kernel of the finite system of linear commutator equations for a basis of C over E. Thus the centralizer of C_K is C_K and has dimension m over K. In matrices this centralizer consists of the endomorphisms preserving the m idempotent summands, each of dimension r. Its dimension is therefore mr^2. Comparing gives r=1, so m=n=sd.

## The actual Lie module

The diagonal matrix units of M_s(Delta) split V into s mutually isomorphic summands. One summand is a nonzero left Delta-vector space of some dimension h. Consequently dim_E(V)=s h d^2. The one-dimensional C-action also gives dim_E(V)=m=sd. Thus hd=1, which forces h=d=1. This proves Delta=E and A=M_s(E).

In the printed application, A=End_Q^0(Y), E is its center and V=Lie(Y/Q). The preceding rational Poincare argument supplies the semisimple decomposition. The preceding faithful rank-one C-action identifies its centralizer with C. Apply this calculation before cutting out Y0. The abelian-variety realization of the resulting rational matrix idempotents remains a separate geometric step.
