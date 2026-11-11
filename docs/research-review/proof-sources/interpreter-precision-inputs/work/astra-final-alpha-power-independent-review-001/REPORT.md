# Independent alpha / power / polynomial-value review

4 November 2026. Scope: the exact natural alpha and power macros, their literal polynomialization, and the saved power VALUE consumer. No global theorem or Lean acceptance is inferred.

## 1. Result and exact source scope

I found no missing mathematical premise in the alpha/power junction of the reviewed producer report. I reconstructed both directions from the actual fifteen clauses, checked the two reflection signs independently, and checked that CRT is used only for deliberately chosen witnesses. The power result holds for every natural input, including zero and one. The saved hierarchy evaluates the entire power polynomial at its private natural witnesses; it does not assert that every power subcall vanishes.

There is one source wording clarification: V4b/V4d/V4e `04-computation-value.tex:150-152` uses two successive plus/minus signs. They must not be read as synchronized. For n=2*l*m+epsilon*j the exact value sign is (-1)^l*epsilon. The subsequent proof at 172-180 uses the two signs separately and remains valid. A same-sign interpretation is false; see section 4. This is a local notation ambiguity, not an additional hypothesis or a failure of the literal macro.

The reviewed producer is `work/astra-final-alpha-power-junction-001/REPORT.txt`, SHA256 `40b3afe50003ffbc2511ef859fcd9e1d003d9cff8813a596597e3658da19e92a`. I read it fully and verified all eighteen entries of its SOURCE_PINS. Its verdict is not a premise of this review.

Direct implementation locators:

- `outputs/integer-diophantine-compiler.js:13-45`: allocation and expression sharing; 50-61: helper equations; 63-78: alpha; 80-94: power; 124-140: exact formula polynomialization.
- `outputs/hierarchical-integer-compiler.js:3-27,33-53`: the sole power template, fresh private blocks, and evaluation by substitution.
- `outputs/rational-circuit-translator.js:26-73,94-109`: private natural guards, operation arguments, value root, and actual recipe semantics.
- `outputs/ordinary-integer-polynomial.js:24-45`: saved source selection and `power_value` / `precision` modes.
- The actual saved JSON objects, checked structurally below, not just their metadata.
- V4b, V4d and the now-present V4e `04-computation-value.tex` have identical SHA256 `1d99adec80afa2a6a59759996240150c775ef874957b665a25d3e9de15d8b788`. Relevant ranges are 111-208 and 300-322. This binds the conclusion to the current text as well as the producer's V4b target.

The original cached AFP sources were read directly: `Exponentiation.thy:67-85,214-290,631-684,1038-1217,1228-1314,1345-1533,1540-1605,1610-1692`; all of `Alpha_Sequence.thy` and `Exponential_Relation.thy`. These confirm the literal domains and clauses. I independently give the elementary derivation below; this is not a claim to have built Isabelle or inspected a Lean proof. The cached Git blob identifiers are checked in SOURCE_PINS against `work/afp-diophantine-tree.json`.

## 2. Exact natural formula and helper semantics

All input and witness variables of the macros range over N={0,1,...}. Polynomial values and algebraic manipulations range over Z. No subtraction below means truncated natural subtraction.

Write U_b(0)=0, U_b(1)=1, U_b(n+2)=b*U_b(n+1)-U_b(n). For inputs (X,b,N), the literal alpha formula has witnesses (r,s,t,u,v,w,x,y) and requires:

1. b>3;
2. u^2+t^2=1+b*u*t;
3. s^2+r^2=1+b*s*r;
4. r<s;
5. u^2 divides s;
6. v+2*r=b*s;
7. w congruent b modulo v;
8. w congruent 2 modulo u;
9. w>2;
10. x^2+y^2=1+w*x*y;
11. 2*X<u;
12. 2*X<v;
13. x congruent X modulo v;
14. 2*N<u;
15. x congruent N modulo u.

These are precisely compiler 63-78, current04:155-170, and AFP `alpha_equations` at 1038-1055. There is no hidden ordering on (u,t) or (x,y).

The helper equations are exact over their intended natural arguments. For a<b, the new variable d=b-a-1 is natural, and conversely b=a+1+d implies strict inequality. For a divides b, b=a*d with d natural is equivalent when a,b are natural, including a=0. For congruence the equation a+m*h=b+m*k, h,k natural, represents any signed quotient: if m>0 and q=(b-a)/m is an integer, take h=max(q,0), k=max(-q,0). At m=0 this equation means a=b, as does equality of remainders modulo zero. We never invert a zero modulus: clauses 11-12 already force u,v>0 in soundness.

Fresh emission into this review directory gives alpha: 26 variables, 139 arithmetic nodes, 15 equality leaves and one conjunction; power: 82 variables, 474 nodes, 55 distinct equality leaves and 62 formula nodes. The independent checker normalizes each equality residual to a sparse integer polynomial and compares the complete expected formula tree, including the helper-variable indices. Thus every strict inequality, both squared occurrences of u, and all four congruences are checked against actual output.

## 3. Sequence facts and squared divisibility, reconstructed

For b>=3 induction gives U_n>=n and 0<=U_n<U_(n+1). The base terms are 0,1. The recurrence gives U_(n+2)-U_(n+1)=(b-1)U_(n+1)-U_n>0; integral strict growth then gives the lower bound.

Put M=[[b,-1],[1,0]]. Direct induction gives, for n>=1,

    M^n = [[U_(n+1),-U_n],[U_n,-U_(n-1)]],   det(M)=1.

The determinant identity implies the Pell equation and gcd(U_n,U_(n-1))=1. Parameter congruence is a separate induction on the recurrence: congruent b,b' modulo any positive d give congruent U_b(n),U_b'(n). At b'=2 the recurrence is exactly U_2(n)=n. No period assertion for the index is substituted for parameter congruence.

Unordered Pell solutions: let a,c be natural with a^2+c^2=1+b*a*c and b>2. Equality a=c would imply (2-b)a^2=1, which is impossible. Order the pair A>C. If C=0 then A=1. If C>0, put Z=b*C-A in Z. The equation says A*Z=C^2-1>=0. Since A>0, Z>=0. Also Z=(C^2-1)/A<C, because A>C. Direct substitution shows C^2+Z^2=1+b*C*Z. Descent on the smaller coordinate reaches (1,0). Reversing each step, (C,Z) goes to (b*C-Z,C), precisely the recurrence. Thus the unordered pair consists of adjacent sequence terms, while a specified larger coordinate is U_m and its smaller companion U_(m-1), m>0. This justifies both uses of unordered Pell and the one ordered use in the actual formula.

For k>0 put h=U_k and a=-U_(k-1). The matrix identity is

    M^k = a*I + h*M,       h>0,       gcd(a,h)=1.

For m=q*k+r with 0<=r<k, reduce modulo h. The lower-left entry gives U_m congruent a^q*U_r. If h>1 the scalar a is a unit modulo h, and 0<=U_r<h, so h divides U_m exactly when r=0. If h=1 then k=1 and the same divisibility equivalence is immediate. This proves U_k|U_m iff k|m without an unproved strong-divisibility theorem.

For m>0, I then obtain

    U_k^2 | U_m    iff    k*U_k | m.                         (D)

For k=0 both sides are false: U_m>0 and m>0. For k>0, either side first forces k|m, so write m=k*q with q>0. Expand the commuting matrices (a*I+h*M)^q modulo h^2. Its lower-left entry is q*h*a^(q-1) modulo h^2. If h>1, cancel the positive h and then the unit a^(q-1) modulo h, giving h|q. If h=1 both divisibilities are automatic. Conversely the same expansion gives h^2|U_(k*q) when h|q. This handles k=1 and the possible a=0 without calling 0 an invertible integer. It also explains why the condition is squared divisibility, not merely u|s.

This is the actual scope of current04:137-146 and AFP `divisibility_alpha2:631-684`, whose hypotheses are b>2 and m>0. All actual uses have b>=4 and m>0.

## 4. Reflection and the two separate bounded-residue steps

Let m>0 and v=U_(m+1)-U_(m-1)=trace(M^m). Cayley-Hamilton for the determinant-one matrix M^m gives M^(2m)-v*M^m+I=0. Hence M^(2m) is -I modulo v. M is invertible over Z; its negative powers have lower-left entry U_(-j)=-U_j.

Every n>=0 can be written

    n=2*l*m+epsilon*j,  l>=0, epsilon in {+1,-1}, 0<=j<=m.

Take the remainder modulo 2m. If it exceeds m, increase l by one and use the negative representative. Consequently the exact formula is

    U_n congruent sigma*U_j modulo v,
    sigma=(-1)^l*epsilon.                                   (R)

The value sign sigma and index sign epsilon are not identical in general. With b=4,m=2,n=3,j=1,l=1,epsilon=-1, we have v=14 and U_3=15 congruent +1, not -1. Current04:150-152 is correct only when its two plus/minus signs denote separately possible signs. An unambiguous replacement is:

    Every n>=0 has n=2*l*m+epsilon*j with 0<=j<=m and
    epsilon in {+1,-1}; then U_n is congruent
    (-1)^l*epsilon*U_j modulo v.

`REFLECTION_SIGN_CLARIFICATION.patch` contains this additive proposal against immutable V4e04 (the relevant V4b/V4d source is identical). No manuscript file was changed. No equation in the saved artifact changes. Current04:176-180 and the producer report's 60-80 do not rely on synchronized signs.

For b>=4, since U_m>U_(m-1),

    v=b*U_m-2*U_(m-1)>(b-2)*U_m>=2*U_m>0.

This strict inequality also holds at m=1, where v=b and U_m=1.

Now take an arbitrary full alpha solution. The bounds force u,v>0. The Pell analysis gives u=U_b(k) with k>0, s=U_b(m), r=U_b(m-1) with m>0, and x=U_w(n) with n>=0. The last use is valid because w>2; y can be the preceding or following term. By (D), u|m. Parameter congruence gives x congruent U_b(n) modulo v and x congruent n modulo u.

Reflect n using (R). Clause 13 gives X congruent sigma*U_b(j) modulo v. Both 2X<v and 2U_b(j)<=2U_b(m)<v. If sigma=+1, the difference is a multiple of v with absolute value <v, so X=U_b(j). If sigma=-1, the nonnegative sum X+U_b(j) is a multiple of v smaller than v, hence both terms are zero. Again X=U_b(j).

It follows that j<=U_b(j)=X, and therefore 2j<u. Independently, u|m and clause 15 give N congruent n congruent epsilon*j modulo u. Both 2N<u and 2j<u. The same difference/sum argument, now with epsilon, forces N=j; in the negative case both are zero. Therefore X=U_b(N).

This proves soundness for every natural assignment satisfying the actual formula. It uses neither oddness of u nor gcd(u,v)=1. Those are unavailable as universal consequences and are not needed. The example in section 8 verifies a full solution with gcd(u,v)=2.

## 5. Completeness and CRT with chosen witnesses

Assume b>=4 and X=U_b(N). Among k=2X+1 and k=2X+2 at least one U_b(k) is odd, because adjacent terms are coprime and cannot both be even. Choose that k. Then u=U_b(k)>=k>2X and k>0. Define

    t=U_b(k+1), m=k*u, s=U_b(m), r=U_b(m-1), v=b*s-2*r.

The Pell equations and r<s hold. Formula (D) gives u^2|s. Since N<=X, 2N<u. Also m>=u and s>=m, so v>2s>=2u>2X; in particular v>0.

Only for these chosen witnesses do we prove gcd(u,v)=1. If d>0 divides both, then d|s since u^2|s. The equation v=b*s-2*r gives d|2r. But d is odd, because u was chosen odd, so d|r. Consecutive s,r are coprime, giving d=1. This reasoning does not apply to arbitrary satisfying assignments with even u, and the proof never attempts to apply it there.

Positive coprime moduli u,v admit the requested CRT class w congruent 2 modulo u and b modulo v. Choose a nonnegative representative z and put w=z+u*v. Here u>=1 and v>=4: from s>r>=0 and b>=4 one has v>=4s-2r>=2s+2>=4. Thus w>2. If u=1 its congruence is automatic; there is no invalid inverse modulo zero. Taking x=U_w(N), y=U_w(N+1), parameter congruence gives x congruent X modulo v and N modulo u. All main witnesses are natural; section 2 constructs all helper witnesses.

This proves completeness with quantifiers

    for every X,b,N in N:
    [b>3 and X=U_b(N)] iff there exist 23 natural witnesses
    making the standalone alpha polynomial zero.

The witnesses depend on the given inputs. No uniform finite bound is claimed or required. The choice k=2X+1 or 2X+2 is an existence proof, not a restriction imposed in the formula.

For N=X=0 one can choose r=0,s=1,t=b,u=1,v=b,w=b,x=0,y=1 directly. For b<=3 the first strict inequality excludes every solution. If X=0, soundness forces N=0; if X=1, strict growth forces N=1. These cover the potentially delicate zero and one inputs.

## 6. Power: all natural inputs and signed intermediate algebra

Compiler 80-94 and current04:193-208 have exactly three branches. The first requires Q=R=0,P=1. The second requires Q=0,R>0,P=0. The third requires Q>0, with five main witnesses b,m,a0,a1,a2, and the full alpha clauses expressing

    a0=U_(Q+4)(R+1),  b=a0+Q^2+2,
    m+Q^2+1=b*Q,  P<m,
    a1=U_b(R),  a2=U_b(R+1),
    P+b*a1 congruent Q*a1+a2 modulo m.

All three alpha groups have distinct private variables. Since Q>=1 in the third branch, induction on the recurrence gives a0>=(Q+3)^R. Indeed for c=Q+4>=5 and n>=1, U_c(n+1)=c*U_c(n)-U_c(n-1)>=(c-1)*U_c(n), starting with U_c(1)=1. Hence b>=4 and

    m=Q*a0+Q^2*(Q-1)+2Q-1 >= Q*a0+1 > Q^R.

Thus m>0, and its defining equation has a natural solution. No potentially negative integer is silently converted to a natural witness.

Put E_r=(Q-b)*U_b(r)+U_b(r+1) in Z. Direct expansion, using the recurrence, gives

    E_0=1,
    E_(r+1)-Q*E_r=(b*Q-Q^2-1)*U_b(r)=m*U_b(r).

The last congruence in the macro is therefore P congruent E_R congruent Q^R modulo m. Both P and Q^R lie in [0,m), so P=Q^R. Conversely, for P=Q^R choose the displayed a0,b,m,a1,a2, apply alpha completeness separately to the three calls, and split the signed quotient in the final congruence into its two nonnegative parts. All variables can be supplied simultaneously because the private blocks are disjoint.

For Q=0, precisely the first two branches implement 0^0=1 and 0^R=0 when R>0. For Q=1, m=a0+1>=2 and the argument gives P=1 for every R. For R=0 with Q>0, a0=1,a1=0,a2=1 and m>1; the bounded congruence forces P=1. Inactive branches need not satisfy their own equations. Their private variables may be any naturals; the zero factor of the chosen disjunction branch suffices.

The resulting statement is for every P,Q,R in N, with no positivity convention omitted:

    P=Q^R iff there exist 79 natural witnesses
    making the emitted power polynomial zero.

## 7. Exact VALUE, private witnesses, and the saved rational consumer

Let F(P,Q,R,w) denote the actual 474-node integer power polynomial, where w has 79 natural entries. The preceding theorem concerns the existence of w for which F=0. The VALUE interface is the different, pointwise statement that a call node returns the integer F at its supplied inputs and chosen w, whether or not it is zero.

`Builder.polynomial:124-134` sends equality to a signed difference, conjunction to a sum of squares and disjunction to a product. Over Z these have exactly the required zero sets. Its `polynomial` formula-node case passes the given expression through unchanged. The independent checker compares the exact expression hashes obtained from these operations, preserving operand order, with both emitted arithmetic roots. The direct source establishes the rule for all assignments; this finite structural check binds that rule to the artifacts.

`HierarchicalBuilder:13-26` allocates a distinct interval of 79 variables for each power call and sets its node to the template call. Evaluation at 33-53 takes the three actual integer argument values, appends that interval's 79 assigned values, and evaluates the template. By induction over the finite arithmetic DAG this is identical, for each assignment, to complete literal substitution. This proof includes nonzero calls and signed intermediate arguments. It does not interpret a call as a Boolean or as Q^R itself.

The saved sole template in `precision-natural-polynomial.json` equals the freshly emitted power nodes and root as parsed arrays; its parameter/witness/variable counts are (3,79,82). All 15,845 private intervals are disjoint from one another and from the 54,056 explicit variable indices, and together they cover exactly the 1,305,811 source variables. Each interval is used by precisely one call. Every explicit variable node addresses an explicit variable. These are checked from the saved data, not only the allocator's source.

The actual rational recipe `power_value` has 20 parameters: three five-coordinate signed integer codes and one output code. It has `naturalInputs:false`, `outputMode:value`, and root equality `[17751579,15]`. The three inputs receive no naturalness guard; all 79 source witness variables do. This is the appropriate scope: the polynomial F has a value at signed input integers too, whereas the exponentiation equivalence above is asserted only on N^3.

The exact signed index model, its natural predicate, its scalar constants, and its arithmetic operation contracts remain external to this bounded review. Given canonical signed input codes and these contracts, topological induction gives the canonical code of every integer node value; all private source variables are natural by their guards. Intermediate sums/products are not incorrectly forced natural. Raw addition is used only on codes already supplied by this induction. No claim about arbitrary malformed rational five-tuples is made here.

I checked every edge and allocation of the saved VALUE recipe: 82 source-variable rows, 196 addition operations, 190 multiplication operations, constants 0/1/-1 through their distinguished references and 4/2/3 through their actual fixed scalar bindings. Its allocated variable count is 17,786,718, and its output is equated to parameter code 15 rather than the identity reference -1. The allocation intervals, including all natural guards and operation witnesses, are consecutive and nonoverlapping.

The saved precision parent has five natural code inputs, `naturalInputs:true`, `outputMode:zero`. I checked all its 125,327 addition, 98,382 multiplication and 15,845 power-value operation mappings. Every power call preserves its three source argument-node references, has its own output code, and allocates a disjoint copy of the whole VALUE recipe. Its root equality is `[292889492850,-1]`; its total allocated variable count is 292,889,492,861. This last identity condition is on the final parent polynomial root. It is not imposed independently on the root of every substituted power polynomial.

In the existence direction, restrict a full source assignment to each disjoint 79-entry block and choose the finite local arithmetic witnesses evaluating it. In the converse direction, read the 79 natural values from each VALUE instance and combine them with the explicit parent values; disjointness prevents conflicting assignments. The operation induction identifies the resulting parent polynomial value exactly. Thus the existential assignment correspondence preserves the required shared source variables and private witnesses without an illicit change of quantifier order.

This review does not establish the packed-history predicates or that every downstream use of the exponentiation equivalence supplies natural P,Q,R. That is a separate consumer obligation. It does establish the signed pointwise polynomial-value interface used to preserve literal substitution.

## 8. Independent finite checks and refutation attempts

`check_independent.py` is newly written for this review. It does not import or run the producer's checker or `outputs/verify-alpha-power.js`. Its fresh macro emissions use the actual Builder solely to obtain the implementation being tested. The checker independently constructs the expected sparse residuals and formula topology, evaluates the arithmetic nodes, computes the recurrence by matrix powers, and reads saved JSON mappings.

The completed check records:

- exact agreement of all 15 alpha and 55 power equality leaves and full formula topology;
- exact expression-hash agreement for both formula polynomializations;
- sixteen fully constructed natural witness assignments, including b=4 and N=0, Q=0/R=0, Q=0/R>0, Q=1, and R=0;
- sixteen negative controls changing only the claimed result by +1 (these test those fixed assignments, not all alternative witnesses);
- 5,280 squared-divisibility instances, including k=0 and k=1;
- 5,856 reflection instances with the actual (-1)^l factor;
- 156 power bound / exact E-recurrence instances;
- 206 full alpha solutions generated without requiring u odd, allowing both orders for the x,y pair; 42 have noncoprime u,v;
- the complete saved-template, variable-block, operation-edge, natural-guard and allocation checks described in section 7.

Three targeted countermodels were independently evaluated.

(a) Omitting the square in clause 5 is unsound. Take b=4,X=0,N=6,r=4,s=15,t=56,u=15,v=52,w=212,x=U_212(6),y=U_212(7). Exactly clause 5 of the original fifteen fails, while u|s holds and U_4(6)=780 is not X.

(b) Omitting clause 14 is unsound. Take b=4,X=0,N=1,r=0,s=1,t=4,u=1,v=4,w=4,x=0,y=1. Exactly 2N<u fails; X is not U_4(1).

(c) Universal coprimality is false even for the unmodified formula. Take b=4,X=N=0,r=2911,s=10864,t=15,u=4,v=37634,w=37638,x=0,y=1. All fifteen clauses hold and gcd(u,v)=2. This directly tests the logical distinction between arbitrary soundness witnesses and chosen CRT witnesses.

For the VALUE issue, with all 79 witnesses zero the actual polynomial values are F(2,0,0)=26825, F(-1,2,3)=7722216, F(0,-1,-1)=53745, and F(1,0,0)=0. A translator that replaced each call by an independently asserted power relation would lose these pointwise values. The saved translator does not do that.

These finite checks corroborate and bind the all-input proof; no finite enumeration is represented as proving the universal arithmetic theorem. During development the checker had an eager-default dictionary lookup that accessed an absent `variableCount` in a freshly emitted flat artifact. That local checker bug was corrected to choose the existing `variables` field first. The final completed run exited zero. No production source was modified.

## 9. Remaining boundaries and disposition

No counterexample or unproved implication was found in the exact natural alpha/power formulas, squared-divisibility use, separate-sign reflection, chosen-witness CRT, or the saved polynomial VALUE substitution. The only proposed text clarification is the explicit sign formula in section 4. It is already compatible with the actual downstream soundness proof and requires no polynomial change.

The following remain outside this receipt: the signed elliptic index model and its arithmetic/naturalness producer proofs; all later binomial, packed-history, interpreter and precision-machine correctness; the ordinary-value Test/Close bridge; arithmetic RC and the geometric pole/height producers; final theorem acceptance; Isabelle/Lean build or formal proof status. Their separate reports are not imported as blanket evidence here.

All reviewed originals were preserved. SOURCE_PINS records exact bytes, source roles and directly read ranges; RECEIPT records this report and the new checker/emission/result files. The conclusion is only this bounded informal alpha/power/value review.
