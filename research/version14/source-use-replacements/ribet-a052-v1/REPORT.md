# Published Ribet supplier for the A052 geometric interface

This is an authored source-to-consumer proposal, not its own independent acceptance. It replaces the required A052 interface by exact statements in the final published Ribet article and a short coarse-point argument below. It does not assert equivalence of the unavailable final Jetchev–Kane text with its author version. The separate root good-reduction draft remains unfinished and is not an accepted premise of this packet.

## Source and domain

The local final scan is SHA256 `08f8ebfda40855d0f6d9e90e1dc352eb6576ecc44cc7c6e6ca3d448d724503b4`, 4,955,997 bytes, 47 PDF pages including an archive cover. The author-hosted URL is https://math.berkeley.edu/~ribet/Articles/invent_100.pdf. The printed title page identifies K. A. Ribet, *On modular representations of Gal(Qbar/Q) arising from modular forms*, Inventiones Mathematicae 100 (1990), 431–476, Springer-Verlag 1990. DOI: `10.1007/BF01231195`.

I visually read printed pages 438–443, physical PDF pages 9–14, including the complete statements and the convention passages used below. This is a reading of the published scan, not a comparison based only on title metadata. I also checked the author's publication archive and bounded searches combining the title/DOI with correction and erratum. No separate correction affecting these passages was found; that bounded search is not a proof of universal absence.

Section 3 begins on page 438 with distinct primes p,q and an arbitrary positive integer M prime to pq. Set q=ell_0 and M=N. Choose the auxiliary p outside the finite set of primes dividing Nq. No auxiliary modularity hypothesis involving p enters Proposition 3.3 or Remarks 3.5. There is no squarefreeness assumption on M. The local proof of Proposition 3.6 on page 442 explicitly allows any positive exponent n=v_l(M), so this application includes powers of two.

## Available published assertions

Page 439 defines an enhanced curve as a supersingular elliptic curve over the algebraic closure of F_q with a cyclic subgroup of order M. Its endomorphism ring is the intersection of the two indicated maximal orders and is an Eichler order of level M; its automorphisms are the units of that endomorphism ring. These are geometric objects.

Proposition 3.3, page 440, gives the bijection from their isomorphism classes to the quaternion double class set. The preceding construction retains the level subgroup as an enhancement of the Tate lattice. At primes different from q it uses ordinary Tate modules. At q it expressly uses the transpose of the contravariant Dieudonne module, to obtain the matching variance. It is not a rank-two etale q-adic Tate module in characteristic q.

Remark 3.5(a), page 441, identifies the same objects with locally free rank-one right R-modules Hom(E_0,E). It separately discusses Hom(E,E_0) and left modules. We use the former convention throughout. Proposition 3.6, pages 441–443, supplies a geometric enhanced reference curve for an arbitrary Eichler order expressed as the intersection of two maximal orders. Its proof on page 442 gives the endomorphism order by conjugating the reference completed order. This is enough to choose the manuscript's initially specified R as the reference order; it is not necessary to assume all Eichler orders are globally conjugate.

Remark 3.5(b), page 441, explicitly says that Frobenius is the involution obtained by right multiplication by an idele which is 1 away from q and a division uniformizer at q. It also gives the right-ideal formulation using the subideal of index q². The closing paragraph of Proposition 3.6 on page 443 repeats the Frobenius interpretation of the odd-valuation operation. This is the exact extra statement missing from the short JK Section 2.5 paragraph.

## Right-module and Tate-lattice connection

Fix an enhanced reference E_0 with R=End(E_0), and identify its rational endomorphism algebra with B. For an enhanced E choose a rational quasi-isogeny lambda:E→E_0. The right R-module Hom(E_0,E), embedded into B by phi↦lambda phi, is a locally free rank-one lattice I. Write its completion as I_hat=z R_hat. Changing a generator changes z on the right by R_hat*, and changing lambda multiplies it on the left by B*. This gives exactly B*\Bhat*/Rhat*.

An endomorphism u of E acts on I by left multiplication by lambda u lambda^{-1}. With the geometric endomorphism identification in Ribet's construction, its order is the left order of I, namely B intersect z R_hat z^{-1}; the units give the automorphism group. This is the manuscript's R_z. No inversion of z is introduced while retaining that formula. The alternative left-module convention in Remark 3.5(a) must not be mixed with this one.

At l different from q, the same quasi-isogeny realizes the enhanced Tate lattice of E inside the rational Tate space of E_0. Taking z to transport the reference enhanced lattice to this lattice is consistent with I_hat=z R_hat. If one instead writes a transporter sending the lattice of E back to that of E_0, that transporter is the inverse and is not the variable z in R_z. This fixes the direction without relying on an ambiguous transporter name.

For an O-ideal a prime to Nq, the quotient E→E/E[a] replaces the O_l lattice by a_l^{-1} times that lattice. Thus the adelic coordinate is a^{-1}z with the same global inverse convention already recorded in the conductor-one proof. At q the quotient is an isomorphism on the q-divisible group; at primes of N it preserves the labelled level eigensummand. The existence and specialization of the quotient are retained good-reduction inputs, not new conclusions of Ribet Proposition 3.3. Ribet supplies the geometric/Tate interpretation needed to compare that already constructed quotient with the class-set action.

## Coarse rationality without a scalar model

Let S be the supersingular geometric points of the coarse modular curve X_0(N) over F_q. Ribet identifies S with the geometric enhanced-curve isomorphism classes and states that q-Frobenius acts as an involution. Hence every x in S satisfies Frob_q²(x)=x.

For a scheme of finite type over F_q, a geometric point with algebraic coordinates lies over a closed point with finite residue field F_(q^d). Its Frobenius orbit has length d. If the square of Frobenius fixes the geometric point, then d divides 2, so its residue field embeds in F_(q²). The geometric point therefore comes from an F_(q²)-valued point of the coarse scheme. This applies to X_0(N), and proves precisely the rationality needed by P_M and the character sum. It does not assert descent of a chosen elliptic curve, subgroup, embedding or isogeny with all its labels.

The modular parametrization after good reduction is defined over F_q by the separately retained extension input. It sends such a coarse F_(q²)-point to E(F_(q²)). Therefore every term is in the domain of the same lambda_M. Frobenius and inverse Frobenius coincide on these points and their parametrization values. The two inert embedding orientations are still distinct: this argument concerns the underlying coarse point, not an identification of the labelled embeddings.

Thus the needed interface does not require the stronger assertion that each underlying elliptic curve has a chosen F_(q²)-model with scalar Frobenius. This packet does not source or prove that stronger assertion. The proposed candidate replaces it by the coarse-point proof above, after the consumer checks below.

## Affected and repeated consumers

The current fa53 manuscript uses the geometric model at lines 14158–14168, then P_M at 14170–14186. The latter only needs coarse rationality, the rational parametrization and the Frobenius operation. Lines 14982–14989 use rationality for the finite sum; lines 15037–15056 use the uniformizer/Frobenius sign and equality of arithmetic and geometric operations on F_(q²)-points. None uses a chosen scalar model. Lines 14246–14249 concern conjugation in the local quaternion residue field, a separate algebra statement; no scalar elliptic model is used there.

I searched the whole frozen manuscript for scalar/Frobenius combinations, supersingular objects, division uniformizers and coarse-point assertions. The other Frobenius scalars at lines 4483, 4630 and 5797–5798 concern one-dimensional Galois-character values in deformation/cohomology constructions, not supersingular elliptic models. Lines 3238–3252 use the CM raising-isogeny congruence and a unique subgroup of order ell; lines 3392–3399 and 3463–3469 obtain residue fields from the class-field splitting calculation. They do not cite or require the scalar model sentence being removed. The finite-field norm count near line 16795 is unrelated.

The accepted conductor-one proof is unchanged. Its input 4, ideal/Tate comparison in Section 3, opposite-q anchor in Section 4 and finite-sum domain in Section 5 need the geometry and coarse rationality just supplied. Its full text contains no scalar-Frobenius-model requirement. The earlier conditional review's discussion of the scalar-model route remains a historical description of the old manuscript; this candidate supplies a different, explicit route to the same required coarse rationality. No old review bytes are rewritten.

## Remaining boundaries

The proposal imports the exact published geometric statements; it does not reprove their Deuring/Dieudonne foundations. It retains the modular curve/coarse moduli interpretation, ordinary Tate/Dieudonne variance, CM reciprocity, the good-reduction functor facts, the modular parametrization and the project's weight formulas. The root draft `cj-good-reduction-root/PROOF-DRAFT.md`, SHA256 `a13f646503e35dc24670c72637905e3c4cff4067c144340e634f3df94ef4c2c6`, is explicitly not treated as accepted.

The evidence supports a proposed published alternate supplier for A052. It does not qualify the final JK text. The short right-module and coarse-point connections, the exact candidate, and the source replacement need independent review. No live manuscript, previously frozen CJ packet or review was modified.
