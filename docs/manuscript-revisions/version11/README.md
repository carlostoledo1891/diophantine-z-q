# Version 11: Kato application and review protocol

The [November 7 follow-up on Issue 2](https://github.com/elliotglazer/diophantine-z-q/issues/2#issuecomment-6714388221) found a missing connection in Version 10. K8 defined classes on Kato 2004's restricted index set, but the later application of Kato 1999 required every multiple of a fixed integer coprime to the smoothing parameters. The manuscript also failed to identify the latter theorem's supplied limiting class with the class whose coordinate ideal it used.

## Mathematical repair

[Version 11](../../../manuscripts/quartic_v11.tex) defines K8 on the larger domain permitted by the original construction. It sets `N_K=2Nd` and `N'_K=c d_s`, verifies both norm cases in Kato 1999 (0.1.1), and proves that norm from the `N_K 2^n` levels gives the original dyadic class. Equal construction supports give no Euler factor; transitivity gives no field-degree multiplier. The optional fixed lattice factor is explicit and is a unit at the away-from-two localizations actually used.

The construction support is distinguished from the primes inverted in the cohomology scheme. The source's divisor parameter `d=1` and its class `xi_K` are distinguished from the manuscript's conductor part and modular symbol. The abstract, polynomial tables and numerical bounds are unchanged.

Reviews and bindings:

- [Primary index-domain audit](evidence/arithmetic.md) and [source pins](evidence/arithmetic-source-pins.json).
- [Primary norm and character-convention audit](evidence/norms.md).
- [Consumer, lattice and notation audit](evidence/interface.md).
- [Independent review of the exact final TeX](evidence/independent-review.md), [acceptance record](acceptance.json) and [application contract](kato-application.json).
- [Six exact edits](edits.json), [current review ledger](../../audit-history/current.json), and [pinned build receipt](build-report.json).

These are internal model reviews of the stated repair. They do not freshly validate the unchanged nonvanishing, local-complex, restricted-converse or height arguments, and do not establish independent human peer review or a completed Lean proof. Earlier approvals of related formulations did not check this missing connection adequately.

## Original Mazur source

The original 1992 publisher PDF was obtained and pages 35–37 were read directly. They confirm the variety convention, Conjectures 2 and 3, and the projection argument. In 1992 the finite-homotopy-type assertion follows the displayed Conjecture 2; it is part of the displayed formulation in the 1995 update. The current proof works with either formulation. See the [dated audit](evidence/mazur1992.md) and [source record](mazur1992-source.json).

The earlier Version 10 record correctly reported that this scan had not yet been read. That historical record is preserved rather than rewritten. No change to the Mazur argument is needed.

## Protocol repair

The [revised protocol](../../audit-history/PROTOCOL.md) requires comparison of required and constructed domains, transition maps, the exact limiting object and downstream consumption. Every changed mathematical passage is bound to a contract. An independent reviewer supplies approval for that exact contract and manuscript. A changed definition or manuscript invalidates the binding. The follow-up ledger is compared with a pinned issue snapshot, including its latest comment.

Run from the repository root:

```sh
python -B scripts/check_audit_history.py --self-test
```

The checker rejects missing obligations, stale approval, self-approval, unreviewed edits and omitted findings. It preserves the nine historical dispositions separately. Source-PDF hashes are identity metadata; the script does not download or prove the contents of those sources. A passing result verifies records and bindings, not mathematical truth.

The [independent protocol review](evidence/protocol-review.md) found two omissions in the first implementation. Both were repaired and retested before release. The final run rejects 19 application-review mutations and seven historical-register mutations.
