# Continuation after accepted392t

The H-Kummer square-output elimination direction has been passed to agent01 to avoid duplicate work. In392t, fH and fV0 appear outside the Kummer block through their squared outputs; whether their unsquared coordinates can be removed while retaining signs and quadratic degree remains a concrete open direction. This note does not claim a saving from it.

## A simple root merge loses completeness

One tempting large reduction is to identify the independent scalar anchor root S with the input root A, removing a root chart and comparison branch. This cannot retain the current scalar certificate unchanged.

In the present construction A=[n]P, S=[a]P, beta=51(2X+1)^2+2504, and the input proof forces n=beta. The scalar certificate proves that every p>76176 with odd v_p(r(beta)) divides s=a-1 to power24, where

    r(beta)=beta(beta-1)(beta-2401)(32beta+343)(2beta-1).

Take the integer input X=23. Then beta=115163 is prime. Trial division up to339 verifies primality. Its valuation in r(beta) is one, because all other factors are nonzero modulo115163. If S=A, then s=115162, which is not even divisible by115163. The scalar certificate is impossible. The same argument rules out S=-A on this input, since s=-115164 is also a unit modulo115163.

This is a completeness obstruction to that exact root merge with the retained scalar certificate, not a claim that all root-sharing constructions are impossible. The current freedom to choose a highly divisible scalar index after beta is fixed is substantive.

## Direct logarithm fusion still has a degree cost

The low-order G2 factor can be replaced locally by its [1/1] Padé approximation (1-11w/15)/(1-w/3), retaining order12. Weighting LP by its denominator would then remove the explicit approximation-factor pair from the log equation. However, the cross test becomes L*(1-w/3)-LPweighted, a quadratic field expression. Its squared test output requires a new field pair unless an additional relation eliminates that product. In the current circuit this merely trades the two approximation coordinates for two cross-test coordinates. No saving is claimed.

Likewise direct elimination of a high-order R factor into the log quotient produces products of the common denominator logarithm, LP, and the quadratic Padé denominator. The resulting residual is cubic in stored coordinates. The existing two-gate obstruction concerns only explicit rational evaluation from w and does not establish impossibility of a future shared or curve-based fusion.

All frozen392t artifacts and their independent acceptance remain unchanged. These findings introduce no new assumptions or proposed release edits.
