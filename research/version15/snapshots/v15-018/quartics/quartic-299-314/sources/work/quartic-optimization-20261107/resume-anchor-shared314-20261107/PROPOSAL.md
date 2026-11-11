# Reuse an anchor witness as the inverse common parameter

Exploratory proposal by `/root/astra_quartic_opt05_anchor`, November 7, 2026. No reduced IR or acceptance is claimed. Source is accepted shared314 IR `7805ee1ebd5fec7ac20b2b5590afe9b5891c85aff8eee5f58b104a888bb9e6f5`. Frozen earlier candidates remain unchanged.

The earlier root-chart and direct-elimination searches on 315 found no saving. Those results do not address the new common parameter introduced by shared314. This proposal couples that parameter to a private anchor witness, leaving all root and point coordinates unchanged.

## Exact circuit target

The existing anchor is

    u²+6v²-2(w+C)² = 3T²-2C²,
    T=2g0g1+Cq,
    q=48v83²+48v87²+432v89².

Try gamma=1/u. Keep the anchor coordinate u. Replace the nine common coordinates gamma,gamma²,gamma⁴,gamma⁸,gamma¹⁶,J,gamma⁴⁰,gamma⁸⁰,gamma¹⁶⁰ by eight coordinates

    a2=u², a4=a2², a8=a4², a16=a8²,
    a16*J=1, gamma40*a8=J²,
    gamma80=gamma40², gamma160=gamma80².

They uniquely give J=gamma¹⁶ and the required high powers. The guard term uses J*E8. All equations are quadratic. The explicit inverse excludes u=0 and gives the required nonzero gamma. This would save one rational coordinate. It is not a bijection with all old witness fibers: it restricts the formerly independent gamma, so completeness needs a new witness-selection argument.

## Proposed completeness argument, requiring independent audit

Let t=T/C and N=3T²-2C². Since t is rational, N is nonzero. The existing quaternion criterion supplies a rational point on the smooth affine quadric

    Q(u,v,z)=u²+6v²-2z²=N, z=w+C.

The point/scalar/root data and t are fixed before contact primes. The anchor witnesses themselves can be postponed because they occur nowhere in the original point, scalar or detector inputs.

The desired gamma conditions become

    1/(2lambda) < u < 1/lambda,
    v_p(u)=-1 at each selected contact prime,
    v_p(u)=nu_p at p=2,3,17.

The small-prime condition is exact, not just an arbitrary lower bound. It suffices to have a smooth local solution at u=0 and then perturb u to a value of exactly that valuation while solving for v or z. The required nu values are fixed arbitrarily large before prime selection.

At 3, t is integral by the existing anchor preparation. Set v=0 and z=C sqrt(1-3t²/2). The radicand is 1 modulo3 and therefore a square in Q3. The z derivative is nonzero.

At 17, 2 is a square. Set v=T/sqrt(2), z=C. This solves the equation at u=0 for every rational T, including nonintegral T. The z derivative is nonzero.

At 2, arrange the existing freely adjustable scalar depth so Fs=2g0g1 is divisible by8. Each odd root has v2(X_i)=-1. Hence

    q=3(2X_A)²+3(2X_T)²+27(2X_Z)² = 1 modulo8.

Since C is odd, t=Fs/C+q is odd. Set v=T/2 and z=(C/2)sqrt(4-3t²). The radicand is1 modulo8 and is a Q2 square. This gives a smooth local solution at u=0. The proposed extra scalar depth is of the same finite kind already allowed before roots and contact primes; its compatibility must be checked against the actual existing preparation order.

At each selected contact p>3, require that the fixed T has no denominator at p. The existing prime selection can exclude finitely many prime divisors of these already fixed data. Choose u=p^-1. After multiplying the binary equation for v,z by p², its right side is -1 modulo p. The binary norm form 6v²-2z² represents every nonzero residue modulo p: if 3 is nonsquare this is the surjective norm of Fp², and if 3 is square it factors into two independent linear factors. A nonzero solution is nonsingular and lifts. Thus a local quadric point with v_p(u)=-1 exists, independent of overlap between detector contacts.

Over the reals, for any small positive u one can choose v large enough that z²=(u²+6v²-N)/2>0. Thus the required real interval is nonempty on the quadric.

Finally, a smooth quadric Q=N with a rational point has an explicit rational parametrization on a dense open set. For a rational point P and direction d=(1,s,t), the second line intersection is

    P - 2 B(P,d)/Q(d) * d,

where B is the polar bilinear form. This is rational in two parameters. Avoid its finitely many exceptional algebraic loci at each real or p-adic target. Ordinary weak approximation for two rational parameters then approximates all prescribed local points at once, giving exact open valuation conditions and the real interval. This should be proved directly by CRT and a real interval, rather than added as an unexamined external theorem.

If these steps hold in the full source order, choose this anchor point after lambda and the contact primes, before the final H. It determines gamma=1/u with exactly the shared314 conditions. All detector estimates are uniform in gamma/lambda in(1,2), so the same final H progression and compact real neighborhood remain valid.

## Remaining work

Check the exact scalar finite-depth ordering and the local perturbation argument at2, including rational-coordinate conventions; formalize the elementary parametrization/approximation proof; bind every common-power consumer to the proposed eight-coordinate chain; emit and independently review the candidate and its full SOS. No saving is accepted until those steps are complete. Sparse and ordinary transports of the already accepted314 remain separate work.
