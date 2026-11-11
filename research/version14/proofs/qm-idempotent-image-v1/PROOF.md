# Abelian images of rational idempotents

Let A be an abelian variety over a characteristic-zero field k. The image of a rational idempotent e of A is represented by an abelian subvariety over k. Complementary idempotents give the corresponding isogeny decomposition. Matrix units identify the factors up to isogeny, and their rational endomorphism rings are the corresponding corners. Differentiation of rational endomorphisms is faithful.

## The image of an integral homomorphism

For a homomorphism f from A to another abelian variety D, the image is closed because f is proper. Give its image X the reduced closed subscheme structure in D. The morphism factors through X because A is reduced, and the map A to X is surjective. It is schematically dominant because a function on an open of the reduced scheme X whose pullback is zero vanishes at every point of that open.

The product of two copies of this surjection is schematically dominant as well. On an affine open U of X, cover its inverse image by finitely many affines. The coordinate ring of U injects into the finite product of their coordinate rings. Tensoring two such injections over k preserves injectivity, and finite products commute with this tensor product. This tests schematic dominance on products of affine opens of X.

Multiplication on D restricted to X times X factors through X. Indeed, the equations of X vanish after pulling back by A times A because f is a homomorphism, so schematic dominance makes them vanish on X times X. The same argument with one copy of A gives inversion. The identity belongs to X. Thus X is a closed group scheme of finite type over k. Cartier's theorem makes X smooth in characteristic zero. The surjection remains surjective over an algebraic closure, so X is geometrically connected. It is projective as a closed subscheme of D and commutative as a subgroup. These are the required abelian-variety properties. [Stacks Project, Lemma 39.8.2, tag 047N](https://stacks.math.columbia.edu/tag/047N)

## Clearing denominators and recovering the factors

For any positive integer m, multiplication by m on an abelian variety has invertible differential at the identity in characteristic zero. Its image is an abelian subvariety by the preceding argument. The differential factors through the Lie algebra of that image, so the image has full dimension and is the entire variety. Its kernel has zero tangent space at the identity, and translations give zero tangent spaces at all its geometric points. The finite-type kernel is therefore zero-dimensional and finite. In particular an integral homomorphism killed by m is zero, since its geometrically connected image lies in that finite kernel.

Choose a common positive integer m clearing the denominators of a finite family of pairwise orthogonal rational idempotents e_i with sum 1. Write f_i=m e_i as an integral endomorphism and X_i for its image. The identities f_i f_j=0 for i different from j and f_i^2=m f_i hold integrally by torsion-freeness just proved. Because f_i surjects onto X_i and the source X_i is reduced, these identities imply that f_i restricts to multiplication by m on X_i and to zero on each other X_j. The addition map p from the product of the X_i to A and the tuple q of the f_i in the other direction therefore satisfy p q=[m] and q p=[m]. Thus p is an isogeny and q/m is its inverse in the rational category. The image is independent of the chosen denominator because passing to a common multiple composes with surjective multiplication on each X_i.

Write j_i for the inclusion of X_i and r_i for the rational projection f_i/m with codomain X_i. Then r_i j_i=1 and j_i r_i=e_i. The maps h to j_i h r_i and H to r_i H j_i identify End^0(X_i) with e_i End^0(A) e_i. If the e_i are diagonal matrix units, the off-diagonal units yield rational isomorphisms between the factors using the corresponding inclusions and projections. This construction also works for a single idempotent by adjoining its complement.

## Faithfulness of differentiation

A nonzero homomorphism f has a positive-dimensional image X, since a smooth geometrically connected zero-dimensional group with an identity is trivial. The induced dominant map from A to X has differential of rank dim(X) at the generic point in characteristic zero. Indeed, after extending to an algebraic closure, a transcendence basis of the function field of X extends to one of the function field of A. Their differentials are bases in the respective fields, since the algebraic extensions of the resulting rational function fields are separable. Thus the pullback of differentials has full rank on a nonempty open. Translation by a geometric point identifies the differential there with the differential at the identity, since f is a homomorphism. The differential at the identity is therefore nonzero. Clearing denominators proves the claimed faithfulness for rational endomorphisms as well.

## Uses in the scalar-descent lemma

First apply the single-idempotent case to e=jp on the Weil restriction W. The image is the X in the descent proof. The already proved identity pj=1 identifies this same image with the original power of A after base change to the comparison field.

Next apply the matrix-unit case to the faithful M_2(C) action on X. The two factors are isogenous over Q and have equal dimensions. Since their dimensions sum to 2[C:Q], either corner is the Y of dimension [C:Q] in the proof.

Finally apply the matrix-unit case to the computed End_Q^0(Y)=M_s(E). One factor Y0 has endomorphism ring up to isogeny equal to the E corner, and Y is isogenous over Q to Y0^s. The algebra calculation and the separate Poincare argument establish the field and simplicity conditions in the scalar-descent proof.

The Lie-module calculation uses the faithful differential on the actual Y over Q. This geometric argument supplies faithfulness. The scalar centralizer computation and the primitive factor's later modularity use separate arguments.
