# Independent interpreter / precision / specialization review

4 November 2026. Informal source audit. No global theorem or Lean acceptance is claimed.

## 1. Finding and scope

I found no mismatch in the reviewed interpreter/precision junction. The actual interpreter implements the stated natural-number program encoding; the actual precision IR computes the totalized five-integer predicate; lowering turns false results into an absorbing nonhalting state and true results into a final zero-register halt; and the actual Cantor wrapper and polynomial specialization preserve the five input codes in their specified order.

This is an independent reconstruction from the literal source and saved objects. The reviewed producer is `work/astra-final-interpreter-precision-junction-001/REPORT.txt`, final SHA256 `396376ff238078e1c25113ca489fe45fbfeb7b5bd781ff607513802dcc41e91f`. I read its final 239 lines and checked all 26 source pins. Its success statements were not used as proofs.

One existing import is retained precisely: the natural packed-history compiler contract for a finite valid increment/decrement machine with a unique final halt is that the emitted polynomial has natural witnesses exactly when the machine reaches that halt with all registers zero. Its locator is `work/astra-final-packed-history-junction-001/REPORT.txt`, SHA256 `55ce89be757e9da1b43b364e8ed8ffed921efabf13c089613c40a35c5863610b`. This review checks the interpreter's exact convention and the saved polynomial's binding to that actual machine; it does not redo the binomial/bitwise/history proof. The alpha/power VALUE interface has the separate independent review `work/astra-final-alpha-power-independent-review-001/REPORT.md`, SHA256 `fec52995bce844c6893150a0c666e815f020ae0d74765e2aa585dd06372e0ba8`.

I also checked the small fixed-point definedness input directly, using the original good-reduction torsion proposition and two exact point counts. Thus this report does not need the full generator/rank/height argument merely to identify the manuscript's ratios with the totalized computational predicate. No arithmetic converse or finiteness of Sha enters any argument here.

Direct source locators:

- `outputs/universal-interpreter.js`, read in full: Assembler 6-93, actual interpreter 94-123, encoding 124-137, finite-budget simulators 144-168.
- `outputs/variable-shift-precision.py`, read in full: literal curve and point 15-21; affine group law 63-94; z/epsilon/center 97-111; capped arithmetic 114-193; strict precision and full predicate 196-231; signed coding 234-248.
- `work/precision-register/precision-register.js`, read in full: IR and signed/field operations 18-69; group operations 70-110; fractions 111-132; capped arithmetic and height 136-162; predicate 164-191; lowering 193-219; budgeted evaluator 221-239.
- `work/precision-polynomial/specialize-precision.js`, read in full: actual unpair 16-26; wrapper 27-37; specialization 40-71.
- Current V4e04:1-61 and 290-322, and V4e02:1-23. The V4e mathematical files used here remain byte-identical to the corresponding pinned V4b text.
- The saved interpreter, universal polynomial, precision IR/machine, wrapper, wrapper code and precision polynomial were checked directly by the new independent scripts.

## 2. Exact predicate, domains and fixed point

The five natural input codes decode to (n,kappa,a,ell,j) by dec(2q)=q and dec(2q+1)=-q-1. The inverse is enc(n)=2n for n>=0 and -2n-1 otherwise. Thus code 0 denotes 0 and code 1 denotes -1. All intermediate natural-register values are unbounded mathematical naturals. Physical resource limits and simulator budgets are not rejection rules.

Put K=Q(s), s^2=2, d=75-53s and A=-d^2=-11243+7950s. The exact point used in Python is

    P=((1641-1160s)/8,(-123720+87483s)/32).

The IR's Jacobian representation is

    X=13128-9280s, Y=-1979520+1399728s, Z=8,
    x=X/Z^2, y=Y/Z^3.

Division by 64 and 512 gives precisely the Python point, with no scaling or sign change. Direct rational field arithmetic verifies y(P)^2=x(P)^3+A*x(P). Since Norm(d)=7, A is nonzero and the discriminant 64*d^6 is nonzero. Both programs therefore use the same nonsingular curve and same point, not merely isomorphic curves with unspecified coordinates.

Let C={0,-15,-20,-24,-30,-60}, F(n)=product_(c in C)(n-c), and H=H6(primes<=324), defined by the exact expression in section 6. The total predicate rejects unless n is outside C, kappa is nonzero, a,ell>=1 and j=n*a. It then computes z=-x/y on finite points, z(O)=0, epsilon=the sum of absolute values of the two rational coefficients of z([ell]P), and r=the first coefficient of z([j]P)/z([a]P). It rejects undefined divisions and epsilon<=0, and otherwise accepts exactly when

    |r-n|<epsilon,       4*epsilon < 4^(-H*|kappa*F(n)|^24).      (P)

The first coefficient equals half the K/Q trace. No additional factor two belongs in the distance test. The algorithms implement this total predicate even without assuming P nontorsion.

For its relation to the manuscript, I checked nontorsion independently. At the degree-one primes (17,s-6) and (23,s-5), d reduces to 12 and 17 respectively. The discriminant is a unit at both primes, so reduction is good. The new exact enumeration finds 20 and 24 points including O. The rational two-torsion is O,(0,0),(d,0),(-d,0), all distinct.

The primary input is Silverman, *The Arithmetic of Elliptic Curves*, second edition, VII.3.1 and Application 3.2, printed page 192 / PDF page 208. I read the statement and proof and visually inspected a new render. The local-field setup on printed 185 / PDF 201 was read as well: a complete discretely valued field with perfect field and residue field. The completions of K at these primes satisfy that setup. The proposition gives injectivity of m-torsion under good reduction when m is prime to the residue characteristic. Applying it at both primes kills every odd primary torsion group; the 17-primary part is killed at 23 and the 23-primary part at 17. Each finite 2-primary subgroup has order dividing both 20 and 24, hence at most four. Since the displayed E[2] already has four points, all torsion is E[2]. The literal ordinate of P is nonzero, so P is not in E[2] and has infinite order.

Consequently for every nonzero integer k, [k]P is neither O nor a point with y=0. Its x-coordinate cannot be zero, since x=0 would force y=0. Therefore z([k]P) is defined and nonzero. On the guarded input domain a,ell,j are nonzero (n is outside C, which contains 0), so all manuscript ratios are defined and epsilon>0. This closes the definedness junction to V4e04:9-20 using only the small torsion argument, not a rank computation, generator saturation, or the height theorem.

## 3. Assembler and exact universal interpretation

The primitive language consists of increment, decrement/zero-branch, and halt. Assembler allocates its reserved zero register immediately after the input registers; every temp() returns a fresh larger index. Labels are resolved to actual instruction positions. An unconditional jump has identical positive and zero successors, so it always takes that successor; in the actual computation its register also stays zero.

For every natural initial value, clear consumes the register to zero. take consumes one before each body execution and terminates in every actual use because its body does not increase that same counter. ifNZ and whileNZ restore the unit consumed by their test before entering a positive body. Thus branch bodies see the original tested value. The actual whileNZ callers either decrease a counter or traverse a strictly decreasing list tail.

For distinct source and target, copy clears its target and fresh temporary, transfers all units from the source to both, then restores the source from the temporary. If source and target coincide it does nothing, which is the correct copy. addInto uses the same restore invariant without clearing the target; its self-alias case first snapshots the source, so it doubles rather than feeding back indefinitely. All temporaries used by these macros are cleared or overwritten on every invocation, including loop reentry.

ifLt consumes copies in pairs, testing the second copy first. It selects the less branch precisely when the first copy is exhausted while another unit of the second existed; otherwise the second expires first and the greater/equal branch is selected. It preserves the originals. divmod2 copies its input before writing its distinct outputs, then consumes pairs and records the final parity. Thus either output may alias the old input safely. General divmod, used with positive divisor y, starts with rem=x,quot=0 and repeatedly subtracts y when rem>=y. The invariant x=quot*y+rem and strictly decreasing rem prove termination and exact quotient/remainder. It assigns its outputs only after the loop; any actual output/input aliases are therefore harmless.

The lowering's add case snapshots y when its output is y, before copying x. Its subtraction snapshots y and performs saturating decrements of a copy of x. Its multiplication uses a fresh accumulator and copied x counter while addInto preserves y; only after completion is the output assigned. This covers output=x, output=y and x=y. The independent primitive executor checked 225 such cases. assignMany in the IR detects any overlap between destination and source lists and snapshots every source before assigning any destination. Actual destination tuples have distinct entries. This makes point updates and sign swaps simultaneous as intended.

The universal numbering is literal: e+1=2^w(2D+1). If w=0, the virtual program halts immediately. Otherwise B=2^w>=2, and state p reads four base-B digits at positions 4p,...,4p+3. They are opcode, register, positive/add target and zero target. Opcode 1 increments; 2 decrements if possible and branches; every other opcode halts. Missing high digits are zero. This is a definition of the numbering, not a validation convention borrowed from another language.

The tape representation has nil=0 and cons(h,t)=2^h(2t+1). For a positive code, repeated halving determines h and the remaining odd factor determines t. The new tail is strictly smaller than its positive code. uncons(nil)=(0,0); its initial copy makes output/input aliases safe. getList follows exactly the prescribed number of links and returns zero beyond the end. setList saves the traversed prefix in a reversed encoded list, replaces the next head, and prepends that prefix in reverse. Missing links contribute zero entries. Its traversal counter and reversed-list tail terminate. The output is written after all source values needed for reconstruction have been used.

At the interpreter loop, D and B remain fixed, pc is the virtual state and tape holds the virtual register values, initially register 0=n and all others zero. The code computes 4pc using a preserved copy of pc, divides D by B that many times, extracts the next four digits by positive-divisor division, and implements exactly the decoded instruction. Its opcode tests preserve the original opcode and exclude precisely 0 and values>=3. Each virtual step requires finitely many primitive steps, with no uniform time bound asserted. Induction proves exact simulation of every finite prefix. A virtual halt enters cleanup; an infinite virtual run cannot reach cleanup. Cleanup clears every physical register and ends at the unique halt. This is the all-zero convention required by the imported packed-history theorem.

The encoder chooses a width large enough for all fields, packs the first instruction least significantly and returns 2^w(2D+1)-1. A trailing zero halt digit may disappear from the written number but still decodes as a missing zero opcode. The actual precision wrapper has valid in-range targets and opcodes, so none of its rejecting branches can become an invalid-opcode virtual halt.

## 4. Signed field and projective arithmetic on all reached values

A signed value is (p,n) with p,n natural, p*n=0 and value p-n. snormal maps arbitrary natural p,n to (p dotminus n,n dotminus p), preserving that value and making at least one coordinate zero. Every signed add/subtract/multiply normalizes; negation swaps; nonnegative scaling preserves normalization. Thus p+n is the actual absolute value wherever sabs is used. The decoding branches produce exactly (q,0) or (0,q+1).

A field pair represents a+b*s. Multiplication is (ac+2bd,ad+bc), conjugation is (a,-b), and norm is a^2-2b^2. For rational a,b, zero norm forces a=b=0; otherwise sqrt(2) would be rational. Thus fnz's sum of the four nonnegative signed coordinates detects precisely a zero field element. This test is safe because signed coordinates are normalized.

The point invariant is: origin=1 represents O; origin=0 has integral field X,Y,Z with Z nonzero and Y^2=X^3+A*X*Z^4, representing (X/Z^2,Y/Z^3). The literal base point satisfies it. Infinity branches assign the origin flag and coordinates explicitly. All outputs of the nonexceptional formulas are fresh points, so pointSet does not overwrite an input field needed by a later coordinate calculation.

For doubling with finite Y nonzero, put E=3X^2+A Z^4 and D=4XY^2. The emitted coordinates are

    X'=E^2-2D, Y'=E(D-X')-8Y^4, Z'=2YZ.

Z' is nonzero. Dividing by its powers gives x'=lambda^2-2x and y'=lambda(x-x')-y with lambda=(3x^2+A)/(2y). The formula therefore gives the tangent-law double and preserves the curve equation. For O or Y=0 the code returns O, exactly the missing group-law cases.

For finite addition, write U1=X1 Z2^2,U2=X2 Z1^2,S1=Y1 Z2^3,S2=Y2 Z1^3, H=U2-U1,R=S2-S1. If H is nonzero, the output is

    X'=R^2-H^3-2U1 H^2,
    Y'=R(U1 H^2-X')-S1 H^3,
    Z'=H Z1 Z2.

Its affine slope is lambda=R/(H Z1 Z2). Dividing the displayed formulas gives x'=lambda^2-x1-x2 and y'=lambda(x1-x')-y1. These are the chord-law coordinates, so the result is on the curve and Z' is nonzero. If H=R=0, the two affine points are equal and the code doubles. If H=0,R!=0, equal x on the curve gives y2=-y1, and the code returns O. If either input is O, it copies the other. These cases exhaust all valid inputs. The reference's exceptional ValueError for invalid equal-x data is unreachable from P.

Scalar multiplication begins at O, uses -P for a negative index and applies binary halving to its natural absolute value. At each iteration, an odd low bit adds the current base before the count is halved; the base doubles only if another bit remains. The usual invariant accumulated_point+[remaining_count]base=[original_index]P proves correctness. The count halves and terminates even at zero. No nontorsion premise is needed for this computation.

The new exact field checker compares all IR multiples from -7 through 7 with an independently written affine repeated-addition calculation. These fixtures supplement the general identities above; they do not replace the all-input induction.

## 5. Fractions and totalized rejection

An IR fraction is N/D with integral field numerator and positive natural denominator; it need not be reduced. fractionFromSignedDen first rejects a zero signed denominator, then moves its sign into N and stores its positive absolute value. Since its signed input is normalized, the sign and magnitude tests are exact.

For a finite Jacobian point, -x/y=-XZ/Y. The code writes this as -XZ*conjugate(Y)/Norm(Y), with the preceding sign normalization. It rejects exactly Y=0. At O it returns 0/1. Dividing N1/D1 by N2/D2 is N1*conjugate(N2)*D2 divided by D1*Norm(N2), so the same guard rejects exactly a zero divisor. The reference Python uses these same field identities with rational coefficients and catches ZeroDivisionError. Its invalid-point exception never occurs by the point invariant.

Let epsilon=U/D, where U is the sum of absolute coefficients of the IR numerator and D>0. The code rejects U=0. If the center's first coefficient is C0/Dc, Dc>0, its comparison is

    |C0-n*Dc|*D < U*Dc.

This is precisely |r-n|<epsilon, with strictness unchanged. Negative n or C0 is handled by normalized signed arithmetic. No magnitude test uses a potentially negative natural denominator.

All reached general natural divisions have positive divisors. The generic IR.divmod adds an explicit nonzero test, the precision division is by 4U with U already positive, and the later logarithm division is by 4. The three new synthetic zero cases (finite point with Y=0, division by z(O), and division by a zero fraction) all reject before any unguarded division. These test totalization separately from the fixed-P nontorsion argument in section 2.

## 6. Strict precision, saturation, and the exact height expression

For integers U,D>0 and E>=0,

    4(U/D)<4^(-E)
    iff 4U*4^E<D
    iff 4^E <= floor((D-1)/(4U)).                            (S)

The D-1 is essential. Replacing it by D would accept equality at U=1,D=16,E=1. If L=floor((D-1)/(4U)) is positive, the maximum E is floor(log_4 L). The reference computes it from integer bit_length; the IR counts repeated divisions by four while the current value exceeds three. Both compute the same integer. L=0 yields rejection. A maximum exponent of zero also yields rejection because, on the guarded domain, H*|kappa F(n)|^24 is a positive integer.

Reduction of fractions is irrelevant. For every positive integer c, floor((cD-1)/(4cU)) equals floor((D-1)/(4U)): both are the greatest integer t for which 4Ut<D. Any two integral numerator/denominator descriptions of the same positive rational have a common positive integral scaling. Thus the unreduced IR and Python Fraction produce the same precision threshold. The new checker verifies 780 small strict-bound cases and 3,120 nontrivial scalings as finite controls.

Fix cap B>=1 and sigma(x)=min(x,B+1). On nonnegative integers, sigma commutes with addition, multiplication and maximum when its arguments are already saturated and the result is saturated. Zero factors must be retained: the reference checks them before overflow division, while the IR forms the exact product then caps it. For powers, saturation of a base or exponent also preserves the final saturated value. At exponent zero the answer is 1, including base zero; at base zero or one and positive exponent it is that base. At base>=2, any exponent greater than B already gives a value greater than B, and capping it at B+1 does not change that conclusion. A base greater than B likewise gives an overflow for every positive exponent. These cases prove the identity without assuming monotonicity across 0^0.

The IR power loop begins with one and decrements the exponent counter. It stops early only when the product has exceeded the cap; for a base>=2 it cannot return below the cap afterward, and bases zero/one never overflow. The reference binary loop has the same invariant and safe early exits. Both terminate for every finite input. The fixed factorial loop uses factors 2 through 324; after overflow all remaining factors are positive, so its early stop is sound.

The literal expression computed in both programs is

    f=324!, D0=f*3^(256*f^4), G0=116064000000,
    E0=10*(D0*G0)^2, R0=max(D0,317,10^12), Q0=R0^(R0*E0),
    Bcm=D0^2*3^(21000*D0^2)+1,
    Ccm=2*Bcm+4096*(1028+5*D0+84000*D0^2),
    H=2*10^13*max(1,Ccm,Q0^17).

This is V4e02:15-23 at S_ht and its default R; 317 is the largest prime <=324. In particular H is a positive integer without invoking any height theorem. The new scripts execute the actual JS height method over a symbolic expression algebra and parse the actual Python function into the same expression algebra. They compare the entire operand-ordered expression tree, including every literal. This avoids treating universal saturation at small numerical caps as evidence that two different astronomical expressions agree.

After the initial guards, kappa*F(n) is a nonzero integer. Saturating its absolute value to the 24th power, H, and their product therefore gives the exact sigma(H*|kappa F(n)|^24). Comparison with the positive maximum exponent B accepts precisely when the unsaturated required exponent is <=B, which is (S). The public Python cap=0 case returns 1; the internal path does not call positive-cap arithmetic at B=0.

## 7. From total IR to a recognizing machine

The IR first decodes all inputs, checks all elementary guards, computes epsilon and the precision threshold, evaluates the exact capped height requirement, then computes the center and distance if still eligible. Rejecting before a later undefined or failed test does not change the truth value of the conjunction. All loops have explicit finite variants: binary scalar count, repeated division by four, natural power counter, or the fixed factorial index. Thus ideal IR evaluation ends in accept or reject for every five-natural tuple.

The production runIR limit is expressly a simulation budget; exhaustion throws an error instead of reporting false. My new evaluator has the same separation and is not used as a proof of termination. The termination proof is by the preceding variants and the finite operation graph.

The lowerer maps logical input registers 0-4 identically, reserves physical 5 as zero, and maps every other logical register injectively above it. All assembler temporaries are allocated afterward. It emits the initializations before the body. By induction over the IR statement tree, the primitive helper invariants in section 3 implement every arithmetic operation and control branch with the same live values, including loop reentry and aliases.

A true branch jumps to cleanup. A false branch jumps to an absorbing reject instruction, not a return that could fall through. In the exact saved machine reject is PC 122828, a decrement/branch on physical 5 with both targets 122828. The accepting cleanup begins at 122829, clears each of 23,582 physical registers exactly once via its own terminating loop, then reaches the unique halt at 146411. The new replay checks every one of these instructions and verifies that no increment ever changes physical 5.

Therefore accept gives a finite all-zero-register halt, whereas reject gives a finite prefix followed by infinite residence in the rejecting state. This is compatible with a total deciding IR and a partially halting primitive recognizer. A false IR result cannot have a finite accepting history under the packed-history convention.

## 8. Cantor wrapper and exact saved polynomial

Define pair(h,t)=(h+t)(h+t+1)/2+t. The emitted unpair starts sum=0,rem=code. Its loop condition sum<rem permits subtracting sum+1 exactly, then increments sum. The invariant is code=sum(sum+1)/2+rem with rem>=0. Rem decreases on every loop iteration; at exit 0<=rem<=sum. Hence head=sum-rem,tail=rem are natural and pair(head,tail)=code. The disjoint triangular intervals prove uniqueness. This also proves unpair(0)=(0,0).

The helper copies the input code to a private rem before writing its outputs. In the actual first call head aliases code register 0, and in later calls the tail aliases the previous remainder-code register; neither destroys the saved rem. Four calls recover the first four natural input codes and the remaining tail becomes the fifth. They do not decode signed integers or reverse their order.

The wrapper starts its scratch registers above the entire main-machine register range. It modifies only the intended five input registers and these private scratch registers, preserving zeros in the remaining main registers. It clears its scratch range [23582,23633) before transferring to the main entry. The saved prefix has 368 instructions. Every main jump is relocated by 368 while all register numbers are retained. The main program never uses those cleared wrapper-only registers. Thus main cleanup also leaves all wrapper registers zero. A relocated rejection remains an absorbing loop, and the wrapper's only halt is the main halt.

The actual wrapper code has field width 18. My independent decoder reads the saved hexadecimal number and compares all 146,780 decoded instructions, including missing/trailing halt fields and every relocated target. Separately, fresh source generation reproduces the full saved number exactly; no finite modular fingerprint is substituted for equality of its large decimal constant in the polynomial.

For the polynomial junction, fresh generation first reproduces the actual 1399-state, 204-register universal interpreter. The universal H metadata's program, register count and input order are compared against that interpreter, then the actual generic hierarchical compiler reproduces the whole H object exactly. This binds the imported packed-history contract to the machine proved in section 3, rather than to an unrelated saved polynomial with the same descriptive label.

The specializer replaces H's code variable e by the fixed wrapper number, maps its old input n to tuple variable 5, maps every old witness index i>=2 to i+7 and shifts each private power block by 7. The five new input indices are 0-4; the four tuple witnesses are 5-8. This is injective and disjoint. Private blocks retain their actual polynomial VALUE semantics.

The four new equations are, for i=0,1,2,

    2t_i=(c_i+t_(i+1))(c_i+t_(i+1)+1)+2t_(i+1),

and 2t_3=(c_3+c_4)(c_3+c_4+1)+2c_4. They uniquely prescribe the nested Cantor tuple for every c in N^5; existence uses only the even product of two consecutive integers. I checked these residuals as exact sparse integer polynomials, not just sample evaluations.

The final arithmetic root is H_specialized^2 plus the squares of those four residuals. Over N/Z it vanishes exactly when all five terms vanish. Forward: any zero determines the unique tuple code, gives a valid finite accepting interpreter history by the imported compiler theorem, hence the wrapper halts, hence the precision predicate is true. Reverse: a true predicate gives finite main and wrapper zero halt, then finite interpreter zero halt, and the imported theorem supplies natural H witnesses; the unique tuple witnesses give a zero of the final polynomial. Existential witnesses are selected only after the five inputs are fixed. There is no bounded search assumption, no common runtime bound and no reuse of conflicting private witness positions.

The new data checker verifies every one of 293,568 original source-node mappings, including 54,049 variable nodes and 15,845 call offsets, the unchanged power template and all block shifts, and the exact final sum-of-five-squares graph. Full generation also reproduces the saved final object. Its variable count is 1,305,811, of which five are inputs. These checks bind the all-input argument to `precision-natural-polynomial.json`, SHA256 `f3e163f5c60b972c98b48647274f956dd7d78428e27ddc0543574a5f18120b8c`.

## 9. Evidence, limits and disposition

New files in this review directory provide independent checks. `check_independent.cjs` uses a new primitive executor and ideal IR evaluator; it does not call the producer's checker or production simulators. It checks 225 lowered arithmetic alias cases, three explicit zero-denominator rejections, 560 capped-power cases, 780 strict-bound cases, 15 point fixtures, and all 1024 input-code tuples in {0,1,2,3}^5. It also regenerates every saved artifact in memory, including the universal H binding, and checks the exact cleanup/reject structure. It writes only this review's result and fixture files.

`check_independent.py` implements separate quadratic-field Fraction arithmetic and affine repeated addition, checks the exact point fixtures and finite-field reductions, compares all 1024 full results with the actual Python predicate, checks 3,120 unreduced-fraction scalings, derives and compares the complete height expression tree, independently decodes the entire wrapper number, and checks all specialization mappings and residuals. Both final runs exited zero. All 1024 complete predicate examples reject. No feasible positive sample meeting the enormous height threshold is claimed; the positive direction is the mathematical operation/termination/specialization proof above.

The new primary render `silverman-208.png` and extracts bind the torsion argument; this classical theorem is distinct from a computation certificate. The reviewed book PDF is pinned. The zero-denominator program equivalence does not depend on that theorem; only identifying all guarded manuscript ratios as defined uses it.

No source correction was found necessary in this interpreter/precision review. The separate alpha report's sign clarification remains additive and unchanged. Original sources, reports, manuscript and live jobs were preserved.

Remaining external obligations are exactly the generic packed-history/compiler theorem, the later rational model interpretation and ordinary-value Test/Close bridge, and all independent arithmetic/geometric producers used to prove existence of suitable witnesses. This report neither proves those by implication nor treats them as established merely because this computational junction is consistent. It grants no global theorem status and no Lean or Isabelle credit.
