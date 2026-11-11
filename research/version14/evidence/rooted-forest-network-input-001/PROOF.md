# Rooted-forest coefficients for a primary auxiliary network

Work over F_2, or first over the polynomial ring in independent edge weights and then reduce modulo two. Let U be the finite auxiliary vertex set and T the terminal set. Network edges join two auxiliary vertices or an auxiliary vertex to a terminal; the original terminal edges are not network edges. Let B be an arbitrarily oriented incidence matrix and W the diagonal matrix of edge weights. Write L=BWB^t. Put Q=L[U,U], and let c_a be the column of weights joining U to terminal a, so L[U,a]=-c_a. There are no network terminal-to-terminal edges.

The symbol rules used below are incoming hypotheses: edge differences contract that edge; a cycle difference vanishes; and an isolated primary component without a terminal vanishes. After contracting a forest component with k terminals, its contribution has terminal difference degree k-1. No contraction removes the final terminal. These are precisely the retained contraction/isolation rules invoked in main17172–17187, not new consequences of the determinant calculation.

For completeness, the needed incidence-minor fact is elementary. For a square submatrix B[V minus R,F] with |F|=|V|-|R|, its determinant is zero unless F is a spanning forest with exactly one vertex of R in each component. A cycle gives dependent columns. If the edge set is acyclic, a component with no removed vertex leaves a row dependence, and the row/column counts then force one removed vertex per component. In that case deleting leaves successively gives determinant plus or minus one. This proves the assertion also for isolated vertices.

Cauchy–Binet applied to L[V minus R,V minus C] expands its determinant as a sum over edge sets F of the product of the two incidence minors and the edge weights. By the preceding fact, the surviving sets are precisely forests with one R-vertex and one C-vertex in each component. Over F_2 all signs disappear. This is the only all-minors forest identity needed here; it holds as a polynomial identity without an invertibility hypothesis.

Take R=C=T. The minor is Q. Its determinant is therefore the sum of weights of forests in which every component has exactly one terminal. Under the incoming symbol rules, these are precisely the degree-zero network terms. Their coefficient is det(Q).

For distinct terminals a,b, take R=T minus {a} and C=T minus {b}. Every terminal other than a,b belongs to both root sets. Its component can contain no other terminal. The one remaining component contains a and b and no other terminal. Hence the surviving forests have one two-terminal component joining a,b, and all other components have one terminal. Order the remaining rows as U,a and columns as U,b. The Laplacian minor is the block matrix [[Q,-c_b],[-c_a^t,0]], whose determinant is -c_a^t adj(Q)c_b by direct determinant expansion, whether or not Q is invertible. Modulo two this is c_a^t adj(Q)c_b. It is exactly the coefficient of the single terminal difference partial_ab.

Any surviving forest with a component containing at least three terminals, or at least two components each containing two terminals, has terminal difference degree at least two. Thus the network operator, under the retained symbol rules, has degree-zero and degree-one part

det(Q) times 1 + sum_(a<b) c_a^t adj(Q)c_b partial_ab.

This proves the displayed coefficients in main17188–17197, including singular Q. For disjoint auxiliary sets with no cross-network edge, choosing edge subsets independently gives the product of their difference operators. A union that creates a terminal cycle vanishes by the retained cycle rule. Consequently the same operator acts on either projected symbol whenever both satisfy the stated contraction and isolation rules. This is the precise conditional scope of main17198–17202.

The note does not establish the arithmetic symbol rules, the later prescribed Laplacian/activation construction, or the simultaneous coefficient selection argument. Those remain separate inputs and subsequent arguments.
