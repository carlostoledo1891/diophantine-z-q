from pathlib import Path
import hashlib,json
R=Path('work/source-risk-review-20261107');O=R/'v14-local-twist-factors-002'
s=(R/'v14-local-twist-factors-001/PROOF.md').read_text(encoding='utf-8')
s=s.replace('These are separate inputs from any global nonvanishing theorem.','We also use the minimal-model reduction criteria in VII.5.1, p196, which have no residue-characteristic restriction. These are separate inputs from any global nonvanishing theorem.')
s=s.replace('With the usual local Euler convention det(1-Frob_q q^(-s) | V^I), this means the local factor is1. This argument does not use q-adic coefficients and applies also at q=3.','In particular the twist has bad reduction by VII.7.1. Its j-invariant equals that of E and is integral, since E has good reduction. If the twist had multiplicative reduction, VII.5.1(b) would give v_q(c4)=0 and v_q(Delta)>0 in a minimal model, hence v_q(j)=3v_q(c4)-v_q(Delta)<0, a contradiction. It therefore has additive reduction by the exhaustive criteria VII.5.1, and C.16 gives its local factor as1. This uses only prime-to-q Tate coefficients and the published minimal-model criteria, including at q=3; it does not require identifying two definitions of Euler factors.')
(O/'PROOF.md').write_text(s,encoding='utf-8')
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
(O/'SOURCE-PINS.json').write_text(json.dumps(dict(path='work/astra-final-size-independent-review-001/silverman-2009.pdf',sha256='72ee67bfa1e3fdf582ac7e4b032d7ca0b35a168ed6443ac39c121fbb788cab25',printed_pages=[45,186,187,196,201,449],scope='Table3.1; VII.1.3; VII.5.1; VII.7.1; C.16 definitions. No BSD conjecture or conductor formula is imported.'),indent=2)+'\n')
(O/'MANIFEST.json').write_text(json.dumps(dict(files={p.name:dict(sha256=sh(p),bytes=p.stat().st_size) for p in sorted(O.iterdir()) if p.is_file() and p.name!='MANIFEST.json'},predecessor_proof_sha256=sh(R/'v14-local-twist-factors-001/PROOF.md')),indent=2)+'\n')
print(sh(O/'PROOF.md'));print(sh(O/'MANIFEST.json'))
