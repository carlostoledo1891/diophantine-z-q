# The retained detector equations force q nonzero without the trace

Use exact raw224/198 IR6b961988414509ff6619fb674b696c745b098d00ad2af326df43e4db5aa5d39f. Here q=x102 is detector1.q1, R=x126 and T=x125. Only the ten rows in REQUIRED-ROWS.json are used. In particular no root equation, aggregate trace, paired-factor definition, or proposed inverse guard is used.

## R and T cannot vanish

Row9 gives x55=x1²>=0. Substitution of row56 into57 gives x114=P(x55), where all five coefficients of the quartic P recorded in CHECKS.json are strictly positive. Thus x114>0. Row71 gives R(1+22201*x114)=A*x114. For the admitted A=149^(2N+1)>0 this gives R>0 (nonzero A alone suffices for R!=0). Row68 gives T=R²!=0. This proof is independent of every root and trace modification in the proposed chart.

## Normalize the retained detector

Put t=x98/T and r=x99/T. Row43 gives r=(t-1)². Rows44 and73 give x100/T=r² and x128/T=r³. Row45 gives x101/T²=P5(r), with exact rational coefficients recorded by the checker. Finally row46 gives

    (1+q)P5(r)=r⁵.

All coefficients of P5 are5-adically integral; the leading coefficient is1. Its reduction is

    P5(r)=(r-1)²(r-4)³ mod5.

Assume q=0. If t is5-adically integral, r is0,1 or4 mod5. For r0 the equation reads1=0 mod5, while for r1 or4 it reads0=r mod5. If t is not integral, v5(r)=2v5(t)<0. The leading terms cancel in P5(r)-r⁵, and the coefficient of r⁴ is a5-adic unit (it is1 mod5). All lower coefficients are integral, so the degree4 term uniquely has the smallest valuation. The difference cannot vanish. Thus q=0 is impossible for every rational solution of the ten retained rows.

This includes t=1 and does not imply q>0, q+1!=0, or any particular component nonvanishing. In fact t=1,r=0,q=-1 satisfies the local contact equation with P5(0)!=0. No full-system existence assertion is made for that local example.

## Guard deletion and witness maps

If a proposed full chart retains these ten rows with the indicated coordinate meanings, an added guard q*h=1 is redundant. The forward map from its guarded system deletes h. The reverse map assigns h=1/q, uniquely and rationally. All other coordinates remain unchanged; both maps include q=-1 and every other nonzero rational q. The reverse map uses the retained-equation proof above, not equivalence to an old trace equation valid only on q!=0.

This can save the one proposed guard coordinate and its one equation, but does not establish the complete root chart or its total variable count. If any of the ten required rows or meanings changes, their preservation must be checked again. No additional arithmetic premise or effective defining threshold is introduced. The accepted full-system threshold remains ineffective.
