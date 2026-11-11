# Finite Heegner and Kummer producers at two

Date: 4 November 2026. Scope: A1, A2 and A3 of the V4b producer-consumer checklist, for the actual non-CM pole curves. This is an independent mathematical reconstruction from the pinned raw constructions and the primary statements identified below. It is not an endorsement inferred from earlier review verdicts.

## 1. Conclusion and exact boundary

No missing finite arithmetic implication or strengthened finite-Sha assumption was found in these three producers. One fixed integer L suffices before the companion field, conductors, derivative set, coefficient precision and binary dimension vary. The finite classes and their local boundary witnesses exist at the required retained precision. The proof includes the extra bit at two and does not use residual irreducibility.

This conclusion consumes ordinary class field theory, the CM moduli description, the basic good-reduction and Neron-model facts stated below, and the checked primary open-image, norm and Lang theorems. It does not prove the moving-character existence theorem A4, the bounded-model and two-limit theorems A9, a determinant inequality, the full restricted converse, the polynomial semantics, or the Lean target. When the finite construction is applied, its finite character and compatible Frobenius choices must be supplied by those separate producers. No new manuscript correction is requested.

The original raw prose also discusses CM curves. This review uses the non-CM open-image theorem only for the pole curve E_l: y^2=x(x-l)(x+3l). Its j-invariant is 35152/9, not an algebraic integer, so it has no CM. Nothing here applies that open-image assertion to the separate CM generator curve.

## 2. Objects and quantifier order

Fix E/Q and its Tate lattice T=T_2E, one modular parametrization pi:X_0(N)->E with pi(infinity)=0, and the finite set of local quadratic types allowed at primes dividing 2N. The actual pole family is handled one fixed E_l at a time. Uniformity as l varies is not asserted.

Choose L using only these data. Subsequently choose an imaginary quadratic K, split at 2N and different from Q(i),Q(sqrt(-3)); an old conductor f prime to 2ND_K; and a finite product n of distinct new inert good primes, each outside 6fND_K. In the application f contains the active conductor and the moving scalar prime. Old split prime factors are allowed. The quadratic/scalar coefficient character must factor through H_f/K; this is part of the actual ring data, not a conclusion for an arbitrary signed integer h. In the binary case use the actual universal character whose restrictions at 2N are trivial before reducing modulo two.

For every retained exponent m choose a working exponent a>=m+e and Frobenius precision at least a+1. Each new derivative prime is chosen with rational Frobenius congruent to the fixed complex-conjugation action J modulo 2^(a+1). Thus a_l=0 and l=-1 modulo 2^(a+1). The original finite character and any additional local/Galois prescriptions must be compatible with this choice. The current proof is conditional on that compatibility, which is the separately assigned prime/evaluation producer; it does not invoke Chebotarev for arbitrary independent prescriptions.

After the finite point calculation, project E[2^a] to E[2^m], extend coefficients to the actual finite Artin ring, and perform its weighted transfer. This order avoids assuming that a given Artin character lifts to an arbitrary larger Artin ring. At no stage is t inverted in a finite ring.

## 3. A single scalar bounds invariant torsion

Serre's primary article, printed pp259-260, states openness of the l-adic image for a non-CM elliptic curve over a number field. In our case choose d>=2 such that 1+2^d M_2(Z_2) is in rho(G_Q). Let u=1+2^d and choose g with rho(g)=uI. Fix complex conjugation tau and set

    z=g^2 tau g^2 tau^(-1),       e=v_2(u^4-1)=d+2.

The square g^2 fixes every quadratic field. Each H_c/K is abelian and H_c/Q is generalized dihedral; tau acts by inversion on Gal(H_c/K). If the image of g^2 in that quotient is a, the image of z is a a^(-1)=1. This uses no class-number bound and works for every permitted K and c with this same z. Its action on T is u^4 I. Consequently every point in E(H_c)[2^infinity] is killed by 2^e.

This is an exponent bound, not the false assertion E(H_c)[2]=0. Full rational two-torsion causes no problem. The same element fixes rational quadratic characters, so the torsion argument is also compatible with the twists used after transfer.

Primary match: Serre, Proprietes galoisiennes des points d'ordre fini des courbes elliptiques, Invent. Math.15 (1972), pp259-331; local PDF work/serre-1972-open-image.pdf. I read the rendered pp259-260. The result is used only in this fixed non-CM setting.

## 4. Descent from the whole conductor, once

The ring-class exact sequence and Chinese remainder theorem identify

    Gal(H_fn/H_f) = product_(l|n) (F_(l^2)^*/F_l^*).

Every factor is cyclic of order l+1. The only global units of K are +/-1, which have trivial images in these quotients. Thus the derivative operators commute. For an oriented generator sigma_l put

    D_l=sum_(j=1)^l j sigma_l^j,       D_n=product_(l|n) D_l.

Telescoping gives (sigma_l-1)D_l=(l+1)-Norm_l. Applying the norm relation in section5 shows that the Kummer class c of D_n y_fn is invariant modulo 2^a when 2^a divides all l+1 and a_l.

Let H=G_(H_fn), G0=G_(H_f), Q=G0/H and M=E[2^a]. The exact inflation-restriction segment is

    H^1(Q,M^H) -> H^1(G0,M) -> H^1(H,M)^Q -> H^2(Q,M^H).

Because 2^e M^H=0, both outside groups are killed by 2^e. Lift 2^e c to b in H^1(G0,M), then define D(c)=2^e b. Its independence of b follows because any two lifts differ by an element of the left image. Additivity and naturality under coefficient maps follow by the same argument. Its restriction is 2^(2e)c.

This operation is applied to the complete n, never successively once per prime. For n=1 use the same convention D(c)=2^(2e)c; this matters when comparing the empty derivative set to the first derivative. For I and I union {l}, restriction to the intermediate old field therefore gives the Kummer classes of the same fixed multiples L D_I y and L D_(I union {l}) y. A new switch does not pay the descent factor again. Changing cocycle representatives introduces a coboundary, not an additional multiplier.

Neither inflation-restriction nor the torsion exponent uses rank one, nonzero L-values, or finite Sha.

## 5. Arbitrary-old-conductor point relations

The primary norm input is Cai--Chen--Liu, Heegner points on modular curves, Trans. AMS370 (2018), Theorem2.15, printed p3730. I downloaded the original, read the theorem and surrounding hypotheses, and rendered its page. It permits arbitrary old conductor c prime to N and a new prime outside 6cND_K. With the extra-unit fields excluded, its unit factor is one. In the split-Heegner specialization X_K(N)=X_0(N), pushing the divisor relations through the fixed normalized modular quotient gives

    Tr y_(f l)=a_l y_f                     (l inert),
    Tr y_(f q)=(a_q-sigma_q-sigma_q^-1)y_f (q split).

This is an unaveraged trace. There is no inverse class-group order. The modulus f may contain earlier split or derivative primes. One can apply the theorem with that entire f as its base conductor and m=1; there is no requirement that the old conductor be an inert squarefree product. The two split Frobenii are inverse because their product is the rational principal ideal (q).

The normalized map factors through [P-infinity] in J_0(N), and its elliptic quotient is Hecke-equivariant. Since T_q(infinity)=(q+1)infinity, these point norm identities have no varying cuspidal correction. If other chosen orientation conventions introduce cusp differences, a single fixed multiple kills their images: there are only finitely many cusps on the fixed X_0(N), and Manin--Drinfeld makes their differences torsion. Such a fixed factor C_cusp can be included in L. No class-number or conductor factor arises here.

## 6. The reduction relation does not restrict the old conductor

At a new inert l outside fN, the CM order O_f tensor Z_l is the maximal unramified quadratic order. The CM elliptic curve has potentially good reduction, and after a finite extension we can use its smooth integral model. Its reduction is supersingular. Indeed an ordinary elliptic p-divisible group has rational endomorphism algebra Q_l x Q_l, which cannot contain the unramified quadratic field acting here.

Over the algebraic residue field a supersingular elliptic curve has a unique subgroup scheme of order l: the kernel of Frobenius. Its l-torsion has p-rank zero and a-number one; every order-l subgroup is alpha_l and its image is therefore that kernel. The closure of each characteristic-zero cyclic l-isogeny kernel is finite flat of order l, so every one of the l+1 conductor-raising quotients reduces to the Frobenius quotient. The prime-to-l cyclic N-level structure is carried along by that same quotient. Hence the upper and Frobenius-lower points coincide in the special fiber of X_0(N). Applying pi, which is defined over Q and extends at this good prime, gives

    red(y_(f l))=F_l red(y_f).

The argument only uses maximality at the new l and invertibility of N there, so earlier split primes in f make no difference. Transporting the place with every class-group translate gives the translated identity too. The K-prime (l) is generated by a rational integer prime to f, hence has trivial ring-class Artin symbol. Thus the lower residue field is F_(l^2) and F_l^2 red(y_f)=red(y_f).

The good-reduction moduli facts and the ordinary/supersingular p-divisible-group classification in this paragraph are classical foundations, stated explicitly rather than supplied by an audit label. The resulting congruence agrees with Howard, The Heegner point Kolyvagin system, Section1.7, equation(13), printed p19. Howard's global theorem and unique descent require hypotheses not valid here, so neither is used. The preceding local proof is what extends his displayed congruence to arbitrary old f.

## 7. Fixed bad-place Kummer conditions

Let F be a completion at a prime dividing 2N and F'/F a finite unramified extension arising in descent. For any allowed local twist B, write B_1(F') for the formal subgroup and B_0(F') for the Neron identity-component points. The residue group is the group of points of a smooth connected algebraic group over a finite field.

Lang's primary Theorem1 and corollary, printed p557, give surjectivity of Frobenius-minus-one for that connected group. For a cyclic residue extension k'/k of degree r, a cocycle value x with (1+F+...+F^(r-1))x=0 can be written x=(F-1)y over the algebraic closure. Then (F^r-1)y=0, so y lies in k'. This proves H^1(Gal(k'/k),Bbar_0(k'))=0 without dividing by r.

Every successive formal quotient is an additive residue-field module. The normal-basis theorem makes its cyclic Tate cohomology zero, including when r is even or the residue characteristic is two. Finite induction gives H^1=0 on finite formal quotients. For an actual cocycle, the solution sets to its coboundary equations modulo successive powers are nonempty closed subsets of the compact formal group and are nested. Compactness gives a solution in B_1(F'). Smooth reduction is surjective, so the exact sequence with the connected residue group gives H^1(Gal(F'/F),B_0(F'))=0.

The quotient B(F')/B_0(F') embeds in the finite geometric component group. Its order therefore kills H^1(Gal(F'/F),B(F')). If a class in H^1(F,B[2^a]) becomes Kummer over F', its image in H^1(F,B)[2^a] restricts to zero; inflation-restriction and this component bound show that multiplying by the geometric component order makes it Kummer already over F.

Here K is split at 2N, so the base completions are the fixed Q_p. Unramified extension does not change the geometric component group. There are finitely many local quadratic twisting types at each of the finitely many p|2N. Let C_bad be the product of all their geometric component orders. This one integer works before K,f,n,a vary. The argument uses B=E^(h) when that is the local twist, not an unqualified replacement by E.

Thus take L=C_cusp C_bad 2^(2e). At good primes outside the conductor and two, the upper Kummer class is unramified and the extension is unramified, so the same inertia group shows the descended class is unramified. At active and moving primes the imposed condition is full. No semistability, ordinarity, class-number bound or finite-Sha hypothesis has been inserted.

## 8. The local calculation at two

Fix l|n. Apply all derivative operators other than D_l and call the resulting lower and upper points X,Y. Work with the actual fixed multiples L X and L D_lY. Put F=F_l on the reduced curve; then

    F^2-a_l F+l=0,   Tr Y=a_l X,   red(Y)=F red(X),
    F^2 red(X)=red(X).

Choose 2^a Q=L X. The lower finite Kummer coordinate is

    f_old=(F^2-1)red(Q)=(a_l F-(l+1))red(Q).

Choose 2^a Z=L D_lY. Represent the descended upper class by a cocycle b whose restriction to the upper-field group is (g-1)Z. This representative exists because its restriction is precisely that Kummer class; subtract the corresponding global coboundary if needed. Set

    U=(sigma_l-1)Z-b(sigma_l).

Comparing b(g sigma_l) with b(sigma_l(sigma_l^-1 g sigma_l)) for upper-field g gives gU=U. Thus U is an actual upper-field point, not an arbitrary division point. Moreover

    2^a U=L((l+1)Y-a_l X).

Since both coefficients are divisible by 2^a, the upper-field point

    U0=L((l+1)/2^a)Y-L(a_l/2^a)X

has the same 2^a-multiple. Hence U-U0 is upper-field two-primary torsion killed by 2^e. Inertia acts trivially on geometric reduction, so reduction of b(sigma_l) is -red(U). Substituting the actual U0 gives

    s_new=(a_l-(l+1)F)red(Q)+epsilon,    2^e epsilon=0.

The polynomial identity

    (F-a_l)(a_l F-(l+1))=a_l-(l+1)F

follows on substituting F^2=a_lF-l. Therefore s_new=(F-a_l)f_old+epsilon. Under E[2^a]->E[2^m], which is multiplication by 2^(a-m), epsilon vanishes for a-m>=e. The Frobenius congruence then gives s_new=J f_old at retained level m. This proof never splits integral J-eigenspaces and never treats a skew-symmetric form as alternating in characteristic two.

For the upper finite coordinate, all inertia translates have the same reduction. Thus

    red(L D_lY)=l(l+1)/2 * F red(LX).

If v_2(l+1)>=a+1, this is 2^a times an F^2-fixed point. The local conductor extension is totally ramified, so its Frobenius lift may be chosen in the upper-field group. At the odd good prime l, the formal group is uniquely 2-divisible. The displayed reduction is zero in E(F_(l^2))/2^a, which makes the upper finite Kummer coordinate zero. This is exactly the extra bit needed to absorb the division by two.

Consequently at the retained precision

    f(P_(I union {l}))=0,     s(P_(I union {l}))=J f(P_I).

The same calculation at every old derivative prime preserves the old singular conditions. Commutativity of the D_l and the translated point relations justify that assertion; no new L factor is paid per old condition.

## 9. Transfer and actual finite boundary witnesses

For Delta=Gal(H_f/K) and the actual finite character theta, the induced-module map

    T_A tensor A[Delta] -> T_A(theta),
    v tensor [delta] |-> theta(delta)v

is equivariant with the diagonal action. Indeed g maps the displayed output to theta(g) rho(g) theta(delta)v, equal to the image of rho(g)v tensor [g delta]. With inverse-action conventions invert both character conventions consistently. Composing with Shapiro gives a finite weighted sum, without 1/|Delta|. The same proof applies to values in A[G] for the universal binary character.

The local Mackey formula transports the place and its Frobenius with each coset. The lower and upper weight coincide because theta factors through the old conductor. The point norm, finite coordinate and singular coordinate identities therefore hold term by term before summing. At 2N the scalar deformation is trivial; in the universal family the quadratic character is also trivial there before mod2. In a scalar twist use the actual B=E^(h) local Kummer map. Restriction and corestriction commute with these maps, so weighted transfer retains the local condition.

An equality of finite local cohomology classes means the difference of their cocycle representatives equals db for an actual local degree-zero cochain b. Kummer membership likewise supplies a local Kummer representative and a boundary comparing its image with the global restriction. These choices make an actual cycle of the finite Selmer cone. No dimensions or ranks are used to invent a class.

If a target contraction has projection p with pd=dp, then z-z'=db implies pz-pz'=d(pb). If i,p,h is a normalized contraction, the comparison of p'fz with p'fi pz has the explicit boundary p'fhz. Retain these vectors and homotopies in the same finite diagram. The large ring-class source complexes need not be retained after the finite sum. Bounded ranks, compatible limit selection and preservation of all later evaluation/duality data remain separate obligations; this paragraph supplies their finite inputs only.

## 10. Assumption tests and source precedence

A1 passes with L fixed before every varying arithmetic datum. C_bad depends only on the fixed local types, and the scalar exponent e only on fixed E. Higher precision changes neither. A2 passes at arbitrary old conductor with both inert and split norms; it is not reduced to Howard's inert squarefree special case. A3 passes with an actual cochain construction and a loss a-m>=e plus one Frobenius bit. It is not an application of Howard's odd-p unique-descent or Selmer-rank theorem.

None of sections2-9 uses finite Sha, either at the base or at derivative conductors. No L-value nonvanishing is required to construct the classes. Finite Sha enters later central length formulas only on their separately specified known simple-zero domain; that later use is outside this audit.

The raw RD assertion mentioning a CM scalar input is not the source for our non-CM proof; section3 above is the precise replacement used by V4b. Historical review paragraphs about determinant rank reduction are not evidence for A1-A3. The current V4b passage agrees with the finite construction, so no manuscript change follows from this audit.

## 11. Source locators and primary access

Raw RD is formalization/z-in-q/ProofSources/work/ring-determinants-frozen-4eaee875.tex:182-409, with the finite diagram interface at411-437. Raw RL is formalization/z-in-q/ProofSources/work/ring-limits-frozen-4eaee875.tex:12-35, the finite local data, and407-540 for the separately consumed character specification. The dedicated raw supplement is ProofSources/outputs/finite-heegner-descent-audit.txt. The immutable consumer is review-v4b/03a-arithmetic.tex:18-111 and its derived local-condition continuation.

Primary originals downloaded and pinned here: Cai--Chen--Liu Theorem2.15 p3730; Howard Section1.7 pp19-21 for comparison only; Lang Theorem1 and corollary p557. Their exact URLs and hashes are in primary/DOWNLOADS.json. The original Serre PDF and rendered pp259-260 are pinned from the existing workspace. I visually read CCL p3730, Howard p19, Lang pp555-557 and Serre pp259-260; Howard pp20-21 were also read as extracted text. The local CM reduction argument in section6 is supplied explicitly rather than attributed to a theorem whose old-conductor scope was not checked.

SOURCE_PINS.json records raw, primary and consumer bytes. RECEIPT.json checks those bytes and the written report. These files record provenance; the mathematical evidence is the derivation above. All V4b artifacts and all earlier sealed reports remain unchanged.
