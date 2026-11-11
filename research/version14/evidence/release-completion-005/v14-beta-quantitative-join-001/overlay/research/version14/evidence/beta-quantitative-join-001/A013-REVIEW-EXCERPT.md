## A013: semistability after adjoining torsion

Consumer: lines 780-787, with the resulting conductor use through line 810. Exact source: Silverberg-Zarhin 1995, Theorem 3.5, printed p. 406. The scanned page explicitly reads n >= 3, despite the text extractor's n > 3. It assumes n prime to the residue characteristic and that n-torsion is defined over an unramified extension of the base. Apply it with base F(A[n]); all n-torsion is then rational, so the identity extension supplies the unramified premise. Choose n=3 unless p=3, and n=5 at p=3.

For an abelian surface in characteristic zero, A[n] has rank four over F_n for these primes. Its field of definition is finite Galois of degree at most |GL_4(F_n)|. Together with [F:Q_p]<=D, this is at most DG_0. The source's Theorem 3.3, printed p. 405, gives the semistable inertia criterion: inertia acts trivially on its invariant subspace and quotient, hence unipotently on the Tate module when l differs from p. The image of wild pro-p inertia in GL_4(Z_l) is finite, since the congruence kernel is pro-l. A finite-order unipotent matrix in characteristic zero is the identity. Thus wild inertia is trivial, exactly the conclusion consumed by A012. Good reduction is not asserted after the torsion extension.

Accept conditional on A061's degree bound and A012's separately checked change of ramification numbering. The local semistability assertion itself does not depend on A012.

