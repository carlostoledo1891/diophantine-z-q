# Mixed toric composition gives 501 variables

This separately frozen candidate combines504 with the seven-equation mixed-depth circuit from07. It has 501 variables including input, 500 witnesses, 470 quadratic residuals, degree four, 24,724 monomials, primitive content one, and largest coefficient `16*3^(2^26)`. The fixed parameter is `C=3^(2^25)`. The user requires fewer than500 total variables before a manuscript update; this candidate does not meet that threshold.

The candidate hash is `6a31040f85e30cc6f9d076bf6c92218be110e0829e93333d7e99f93a6b2f0d9a`. The polynomial hash is `0ddbc7d10be3c9208cfcca57bbeb7d70060b226845737ad027d8175f90b2ce56`.

## Exact circuit and maps

Each detector retains E=eWeight, q=q1, Q=q^3, R=q12^2, q12, and q40. Reuse five old power-coordinate slots for a,b,u,v,t and impose:

```
E*a=1
E*b=a^2
b*u=E*q
b*v=u^2
Q*q12=v^2
q*t=E*R
v*q40=R*t
```

These force, successively, a=E^-1, b=E^-3, u=q*E^4, v=q^2*E^11, q12=q*E^22, R=q^2*E^44, t=q*E^45, and q40=q*E^78. Q=q^3 and R=q12^2 are actual retained equations, not additional premises. There is no cycle in this deduction.

Both the old and new chains have E*a=1, so E is nonzero. The unchanged q-definition, when q is zero, is exactly -E=0. Thus q is nonzero as well. Consequently b, Q, and v are nonzero whenever used as divisors. This direct argument is checked on each concrete detector and does not need the more elaborate norm-guard argument from the proposal.

The forward map computes the displayed five Laurent monomials while keeping q12,q40 and every outside coordinate. The reverse map restores the six old powers E^-1,E^-3,E^-7,E^-14,E^-29,E^-55. The original eight chain equations then hold. Both maps retain exactly the q12 and q40 values used by the mixed-depth polynomial evaluations. Their identities are verified using integer exponent pairs in E and q.

The six old internal power coordinates have no consumers outside the eight replaced equations. The five reused slots and the one deletion therefore introduce no hidden changes elsewhere. All scalar chart, scalar norm, anchor, pole-scaling, half-trace guard, and mixed-depth arguments carry over unchanged through this rational equivalence.

## Checks and acceptance scope

`build501.py` checks the old504 chain against the exact519 source and transports the07 proposal by its recorded source coordinate IDs. `verify501.py` imports no producer. It separately reconstructs all old and new chain equations, checks the retained Q and R equations and q nonzero implication, verifies incidence and all unchanged rows, computes the Laurent identities, and independently expands and compares every coefficient.

Run `python -B build501.py` and `python -B verify501.py`. These checks passed. Earlier505 and504 snapshots were not changed.

I accept07's mixed toric transformation by independent internal review as an exact rational projection equivalence. This is my composition, so this report does not independently approve the501 artifact for release. Its arithmetic scope is exactly that of504 and505. No new arithmetic hypothesis, external theorem, or prime condition is needed. The five original proposals and08 retain their previously stated qualifications. No repository manuscript or publication artifact was changed.
