# Modular genus and Belyi input review

Reviewer: /root/v14_arithmetic_review. Accepted at the two stated current source-application scopes.

Author manifest v14-middle-modular-genus-inputs-001/MANIFEST.json: 54d4c1ef73cf25f133ff3aca785407cd6be77e42236fe2fdfe17d9ce97842457. SOURCE-ROLES.json: 829c5577f46c66bd7a845a90aef6b616e47174934762d219db95b450c518f7ce. Manuscript: 1f7bf748843d67c6a67d9863931ff0a15ca2548ae171ec1c1ce34b9002eb70a8.

I directly read the final von Känel publisher PDF, SHA256 5749ce3a371c571655b44174e2a0d65c2e53dc179f518f0e52d585ff73da46f9, printed pages8-9 and13 (PDF indices7,8,12). Equations4.1-4.2 and the proof of Lemma4.1 supply the stated projection, degree and cusp facts. Equation5.9 explicitly gives the genus/dimension bound. The text also explains that X1(N) has genus zero for N<=10.

MIDDLE-J1-MODULAR-GENUS: current8492-8494 uses the actual J1(N), with g>=2 supplied by the preceding same-field subvariety/isogeny construction. Thus N>=11. For Gamma1(N), the degree is at most N^2/2 and there are at least two cusps; g<=1+d/12-cusps/2 therefore gives g<=N^2/24, exactly the stated current bound. The dimension is the genus of this exact modular curve, not an arbitrary curve or the later J_H.

MIDDLE-J1-MODULAR-BELYI: current8495-8499 uses the same X1(N). The standard projection to X(1)=P1 has at most the cusp and two elliptic branch values. A target coordinate change sends these to 0,1,infinity, so it supplies a geometric Belyi map of degree at most N^2/2, hence at most N^2. No descent of that coordinate change to the manuscript's ground field is needed for geometric Belyi degree and the stable-height application. With the separate Javanpeykar inequality, the deliberately weaker displayed height bound follows from deg_B<=N^2 and g<=N^2 (indeed g<=N^2/24). This review does not reapprove that independent height theorem or its metric conventions.

The same-field map, absolute simplicity, g>=2, Javanpeykar and later conductor/isogeny arguments remain separate inputs. No new source ancestry or whole J1/height closure is asserted. Five exact manifest/source/consumer checks pass in CHECKS.json. An initial text extraction encountered only a console encoding error; rerunning with Python UTF-8 read the cited pages successfully. No canonical files changed.
