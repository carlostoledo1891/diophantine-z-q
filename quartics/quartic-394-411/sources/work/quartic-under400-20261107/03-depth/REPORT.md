# Eight variables saved by a rational logarithm approximant

Replace the four retained G9 logarithms by the rational function specified below. Their local precision remains 40, and their global nonvanishing follows from an explicit positivity certificate. The source compiler saves two rational coordinates per replacement, eight total.

The rebuilt mixed-depth source has 511 coordinates rather than 519, before composing the other improvements already present in the published 498-variable construction. Its 480 quadratic residuals give a degree-four sum of squares with 24,499 monomials. This is a component candidate, not a replacement final count for the combined construction. It is compatible in scope with the later pole, anchor, scalar and toric changes because it changes only the four G9 evaluation blocks and their resulting comparison values. The integration agent must check their actual composition.

Exact polynomial identities, positivity certificates, source gates, all nine final eliminations and the complete component sum of squares have passed the available checks. The new arithmetic application below is my own derivation and needs fresh independent acceptance before use. No released manuscript or previous proposal was edited.

## The rational function

Use the existing formal-logarithm coefficients a0=1, a1=-2/5 and a_j=(4j-5)a_(j-1)/(4j+1). Write G9(w)=sum_{j=0}^9 a_j w^j. Define

    Q(w)=1-(1526/1073)w+(513/1073)w^2

and

    N(w)=1-(9776/5365)w+(2941/3219)w^2
         -(1024/13949)w^3-(1920/237133)w^4
         -(1024/711399)w^5-(1408/5928325)w^6
         +(2432/103152855)w^8.

There are no w7 or w9 terms. Exact rational arithmetic gives

    Q(w)G9(w)-N(w)
      =(2970726/254443709)w^10
       -(41697666/6361092725)w^11.

Thus R(w)=N(w)/Q(w) agrees with the formal logarithm factor G(w) through degree nine. The missing w7 term permits a shorter circuit. The two denominator parameters were chosen to make the coefficients of w7 and w9 in QG9 vanish.

Replace ell40(V_i)=z(V_i)G9(D f(V_i)^2) by

    ellR(V_i)=z(V_i)R(D f(V_i)^2), i=0,2,3,4.

The numerator for i=1 remains the existing ell12=zG2. All primary parameters, test orders, point charts, scalar conditions, height scales and anchor stay unchanged. In particular the two input-comparison tests still have order 12. The previous order-10/11 alternatives are separate proposals and are not needed here.

## Global domain and nonvanishing

Each consumed V_i is a nonidentity point of 2E(K), where K=Q(sqrt(2)), E:y^2=x^3-Dx and D=(3-sqrt(2))^2. This follows from the same retained chart and difference-point domains as before. For a nonzero double, its abscissa is a nonzero square under each real embedding. Its ordinate is nonzero by the retained point domain. Consequently

    x>sqrt(D)>0,
    0<w=D/x^2<1

under both real embeddings. This does not assert a property of arbitrary elliptic points; it uses the actual doubled points in the source.

On [0,1], Q'(w)=(-1526+1026w)/1073 is negative. Hence

    Q(w)>=Q(1)=60/1073>0.

Write N in the degree-eight Bernstein basis:

    N(w)=sum_{k=0}^8 b_k binom(8,k) w^k(1-w)^(8-k).

Its exact coefficients b_k, in order, are

    1,
    4143/5365,
    260069/450660,
    27829/67340,
    4636683/16599310,
    82391/474266,
    2245591/23713300,
    955437/23713300,
    83904/10113025.

All are positive and the last is the minimum. Since the Bernstein basis sums to one,

    N(w)>=83904/10113025>0 on [0,1].

Therefore Q(w), N(w), and R(w) are nonzero at every alternate point admitted by the source. The existing nonzero z(V0) then implies ellR(V0) is nonzero. Every new rational evaluation and every alternate ratio has a proved global denominator. No new witness restriction, sign predicate or inverse coordinate is needed.

## Local precision, including inert places

Let p>76176 and let v be either unramified completion of K above p, with v(p)=1. At a nonidentity formal point let r=v(z)>=1. The inherited identity gives v(f)=2r and v(w)=4r. Every denominator appearing in Q, N, G9 and the displayed error identity has prime factors at most 37. Thus those coefficients are integral at v. Both Q(w) and N(w) are 1 modulo the maximal ideal, so R(w) is a unit.

The exact identity implies

    v(R(w)-G9(w))>=40r.

The existing entire-tail estimate gives v(G(w)-G9(w))>=40r. Combining the two bounds proves

    v(log_E(V)-ellR(V))>=41r,
    ellR(V)/log_E(V) in 1+p^40 O_v,
    v(ellR(V))=v(log_E(V))=r.

The argument uses only coefficient integrality and the unramified normalization, not residue degree one. It therefore covers inert and split places exactly as the prior mixed-depth proof requires.

## Soundness and completeness

In the mixed-depth soundness proof, the full alternate ratios remain (u_i-n_i)/(h-1). Replacing their numerators and common denominator by ellR changes them by relative errors of order at least 40. For i=1 the numerator stays ell12 and the common denominator now has precision 40, so that ratio still has precision 12. All approximate ratios still have the valuations of the exact ratios. The integrality-transfer step therefore precedes and justifies the same conversion from relative errors to absolute errors.

The primary points retain depth at least twenty after that transfer, so their uncorrected z ratios still have precision 80. The unchanged cross-tests yield L1=n modulo p^12 and L2,L3,L4 equal their integer labels modulo p^40. The scalar bound, product-height inequality, Lucas contradiction, beta contradiction and their constants are unchanged.

For completeness, keep the exact prior order of choices: integer input, scalar preparation and roots, height scales and continuity modulus, separated contact primes, then the shared-index CRT. The chosen primary points have depth twenty, and the alternate points are formal. The new estimates meet the same test orders. The new rational functions are defined at every source point by the global positivity proof, so continuity gives the required fixed local neighborhoods. Any finite coefficient denominators are absorbed by the existing finite preparation and cutoff; their prime factors are already at most 37. The real-parameter pole estimates use fixed continuous test values and the same orders, so they remain valid.

This proves both directions of the integer-input projection under the same inherited arithmetic inputs. It does not claim that the two systems have identical comparison values or identical exterior witness spaces.

## Circuit and counts

For each replacement, w already exists as the unchanged affine expression D f^2. Introduce

    s=w^2,
    t=s^2=w^4.

The numerator is then the quadratic expression

    1+p1*w+p2*s+p3*w*s+p4*t+p5*w*t+p6*s*t+p8*t^2.

The denominator 1+q1*w+q2*s is affine in available coordinates. Introduce the two rational components of R by the field equation

    Q(w) R=N(w).

All its component residuals are quadratic. This needs three field outputs: s, t and R. The old G9 block used four field outputs: w2, w3, its middle block and its final polynomial block. Multiplication by z, or the existing ordinate-denominator equation for V0, is unchanged. Four blocks therefore save 4*2=8 rational coordinates.

The actual source replay gives 520 compiled coordinates versus 528 before the final reductions. The same five inherited elimination identities and four shared-coefficient shears reduce this to 511 versus 519. The complete new component polynomial has 24,499 monomials and SHA-256 `294bb5a52de989f51063ac8490262372599cdc8eb967547bedc252a03555234c`.

Reproduce, using the working Python executable, with

    python -B build_source.py
    python -B finish_source.py
    python -B verify_rational.py

The verifier first checks the approximation and positivity certificates independently of the builder. It then uses the existing separately authored source, elimination and sum-of-squares checkers, with only paths and the expected component count changed. The checks are evidence for the finite algebra; they do not independently establish the inherited arithmetic theorem or approve this new application.

## Application contract and limitations

The required source inputs are the exact doubled-point domain, the normalized logarithm log_E with parameter z=-x/y, the full-tail estimate at order 40, the mixed-ratio integrality argument, and the existing completeness continuity procedure. The constructed points and field are unchanged. All five alternate points are covered: four receive the new precision-40 function and V1 retains G2. The common denominator is the new ellR(V0), whose nonvanishing is proved above. Conjugation acts on the same coefficient basis and commutes with the rational function, whose coefficients are rational.

The downstream consumer is the actual ratio used in each test, with precision 12 or 40 as appropriate. No local estimate is applied to a merely related point, no branch is silently discarded, and no stronger divisibility of an alternate point is assumed. The first-stage source is rebuilt from the previously frozen mixed-depth source; integration into a later combined candidate must still compare all affected row and coordinate bindings.

I also investigated reducing G9 to G8 without changing its representation. That would give only precision 36 at a general depth-one point, below the current Lucas inequality's threshold greater than 38. Removing primary formality tests using only positivity of the local valuation of z fails because z also vanishes near a nonidentity two-torsion point. Those alternatives are not used in this proposal.
