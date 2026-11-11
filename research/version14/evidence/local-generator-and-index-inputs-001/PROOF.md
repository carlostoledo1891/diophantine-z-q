# Local generator and fixed-index connections

Author: /root. Proposed for independent review. This records the local arguments already used by the current manuscript; it does not certify the whole proof.

Source: J. H. Silverman, The Arithmetic of Elliptic Curves, second edition, Springer, 2009. The exact local PDF has SHA256 72ee67bfa1e3fdf582ac7e4b032d7ca0b35a168ed6443ac39c121fbb788cab25. Locators below are printed pages. The extracted local text was read together with the current consuming arguments. No unseen erratum is imported.

## S1. Integral formal chart and logarithm

Chapter IV Proposition1.1 and the discussion on pp.116–120 construct the integral series w(z)=z^3(1+...), the point (z/w(z),-1/w(z)), and its formal addition law from a Weierstrass equation with integral coefficients. Example2.2.3 names this formal group. Over a complete local field the series converge for z in the maximal ideal. This construction does not require a minimal equation.

Chapter IV Proposition5.5, p.129, gives log_F(T)=sum a_n T^n/n with integral a_n and a_1=1. Lemmas6.2–6.3 and Theorem6.4, pp.130–132, apply over a complete characteristic-zero discretely valued field, with v(K*)=Z and residue characteristic p. The logarithm is a homomorphism on F(m), and is an isomorphism from F(m^r) to the additive m^r for integral r>v(p)/(p-1). These are statements for the indicated formal group, not for all elliptic-curve points.

## S2. Nonsingular reduction and its formal kernel

Chapter VII Proposition2.1, p.188, gives the exact sequence 0 -> E_1(K) -> E_0(K) -> E_ns(k) -> 0 for a minimal integral Weierstrass equation over a complete discretely valued field. Proposition2.2, p.191, identifies the formal group on m with E_1(K), using exactly z=-x/y and the series in S1. E_0 means nonsingular reduction; E_1 means reduction to the identity. An arbitrary integral point is not automatically in E_0.

## S3. Finite-field order bound

Chapter V Theorem1.1, p.138, gives |#E(F_q)-(q+1)| <= 2 sqrt(q) for an elliptic curve over a finite field. This is used only at good reduction places. It is not applied to the singular cubic at the bad prime.

## D1. Actual formal logarithm calculation

The current model is E:y^2=x^3-d^2 x over K_0=Q(s), s^2=2, d=75-53s, with the exact P_0 in currentmain328–332. Its coefficients are integral. Write v for the integer-normalized valuation of a completion and e=v(p). For t=v(z)>e/(p-1), the n-th higher logarithm term has valuation at least nt-v(n)>t because v(n)<=e(n-1)/(p-1). Hence v(log_F(z))=v(z). The homomorphism property and the inverse on this subgroup give v(z([a]P))=v(z(P))+v(a) for nonzero integers a, unless the point is the identity, which is handled separately. Multiplication stays in this subgroup. In the chart, w(z)=z^3 times a unit, so v(1/x)=v(w/z)=2v(z).

At every odd place of K_0, e=1. A nonidentity point in the formal kernel has v(z)>=1>1/(p-1). At the dyadic place v_s(s)=1 and v_s(2)=2. The exact coordinates give v_s(x(P_0))=-6 and v_s(y(P_0))=-9, so v_s(z(P_0))=3>2. The integral chart from S1 applies directly at this place; no assertion that this dyadic equation is minimal is needed. Its positive multiples therefore remain in the same deep formal subgroup.

## D2. Actual odd reduction kernels

Norm(d)=7, and the discriminant of the displayed equation is 64d^6. All odd places away from d have good reduction. At the prime over7 with s=3, v(d)=1 and v(a_4)=2<4; since the residue characteristic is greater than3 the short integral equation is minimal. The exact coordinates reduce to (2,6) on y^2=x^3. This point is nonsingular since 2y=12 is nonzero modulo7. At the other prime over7, s=4, d is a unit and reduction is good. Thus P_0 belongs to the required E_0 at every odd place in the fixed support.

For each odd place above a prime dividing N_s, take the actual positive order of this reduced point, and let m_0 be the product of those orders. Exactness in S2 sends [m_0]P_0 into every indicated formal kernel. Upper bounds on orders are not substituted for actual multiples.

## D3. Bounding that actual product

The residue degree at an odd place is at most2. S3 gives an order bound (p+1)^2<p^3 for each good place. The nonsingular points on the one bad cubic over F_7 are O and (1,1),(1,6),(2,1),(2,6),(4,1),(4,6), so its group has order7, also below7^3. There are at most two places above each rational prime. Consequently m_0 <= product_(p|N_s, p odd) p^6 <= N_s^6. This finite calculation is independent of the catalogue-size estimate.

## D4. The least successful index and denominator guard

Set n=N_s^4 m_0>0. If [n]P_0=O, the convention 1/x(O)=0 already gives a successful search value. Otherwise D1 and D2 give v(1/x([n]P_0))>=2+8v_p(N_s) at each odd supported place, and v_s(1/x([n]P_0))>=6+16v_2(N_s) at the dyadic place.

Write u=1/x([n]P_0)=a+bs. Extraction uses a=(u+conj(u))/2 and b=(u-conj(u))/(2s). At odd places these denominators are units, with both conjugate places included. At2 their valuations are2 and3, so at most3 is lost. Since the extracted coefficients are rational, both coefficients have rational p-valuation at least4v_p(N_s) for every p dividing N_s. Thus a,b belong to N_s^4 Z_(N_s).

Clear their denominators with a positive integer c coprime to N_s and reduce the triple of integer numerator coefficients and c to gcd1. The denominator remains coprime to N_s and both integer numerators remain divisible by N_s^4. This is the exact guard in currentmain310–315. Every earlier positive search step also has defined reciprocal coordinate, because the dyadic subgroup gives either O or negative abscissa valuation. Therefore the least positive successful index exists and M_0<=n<=N_s^10. No nontorsion premise is used to make this search total. Nontorsion for the separate finite false-triple guard remains a separate generator input.

## D5. Actual duplication-form bound

Use C:y^2=x^3-delta^2 x, delta=3-s, and the PID O_(K_0)=Z[s], the latter supplied by the separate quadratic-field/descent argument. For a primitive homogeneous pair (a,b), the duplication forms are F=(a^2+delta^2 b^2)^2 and G=4ab(a^2-delta^2 b^2). Both real embeddings have 1<delta^2<25. If M=max(|a|,|b|), then M^4<=max(|F|,|G|)<=676M^4; indeed |F|<=26^2 M^4 and |G|<=104M^4.

No prime away from2delta divides both F and G: modulo such a prime, F=0 and G=0 would imply either a=b=0 or 2delta^2 b^2=0, contradicting primitivity. At(delta), if a is a unit F is a unit. Otherwise b is a unit and v_delta(F)<=4; when v_delta(a)=1 this uses that -1 is not a square in F_7. At(s), if just one of a,b is a unit then F is a unit. If both are units put u=a/(delta b)=A+Bs, A odd. For B even, v_s(u^2+1)=2; for B odd it is3, from the separate valuations of A^2+2B^2+1 and2ABs. Therefore v_s(F)<=6.

The common ideal has norm at most2^6 7^4=392^2. Divide the logarithmic finite contribution by [K_0:Q]=2 and combine the two real estimates. With the manuscript's absolute logarithmic projective height, 4h_x(P)-log392 <= h_x(2P) <=4h_x(P)+log676. Homogeneous coordinates include the identity and doubling into the identity; a zero affine denominator is not discarded. The limit normalization 2 hhat(P)=lim 4^(-j)h_x(2^j P), supplied separately by the canonical-height theorem, yields h_x(P)<=2 hhat(P)+log392/3 and 2 hhat(P)<=h_x(P)+log676/3. These are the input inequalities to the independently recorded generator-saturation argument.

## Scope

This packet supplies only the displayed formal, reduction-order, least-index and local duplication connections. The fixed catalogue's prime existence and quantitative size, the quadratic-field PID and descent, canonical-height properties, finite generator replay, actual template semantics, and final polynomial theorem retain their separate dependencies. Published statements S1–S3 and local derivations D1–D5 must not be interchanged in the dependency graph.
