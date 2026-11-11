# Independent coverage assembler review

Reviewer: /root/sol_protocol_final_review. Author: /root/astra_v14_baseline_compiler. Candidate manifest SHA-256 3a683211de92399c2f9dffdc7af279e2e311bf8c2ebb8bbfc9cd97ece39fbfec.

**Decision: changes required before assembling production evidence.**

All six manifest members matched their frozen byte counts and SHA-256 hashes. The 23-test suite passed independently under the pinned Python 3.12 interpreter. The default validator's two modules and contract matched the exact Git blobs at local controller commit df1c825c6094facd3cec383d0b5040429525820e. The record command passes the caller's packet, evidence and profile through unchanged to check_records, which remains a structural check. The alternate validator directory is caller-selected, so use the verified default for this release.

The assembler checks referenced bytes before parsing and records consumed file hashes. It copies supplied assertions and finding dispositions and derives structural relationships from input tables. Its output separates unresolved diagnostics from the proposed dossier. It reports direct-edge omissions, dependency cycles, source gaps, unknown applications and unresolved findings. No signature, observation or approval is generated.

1. A terminal historical disposition can be relabeled as a current resolution. In assemble_coverage.py, the supplied current row carries only an ID and history. Copy a preserved resolved history verbatim into the current table for an edited use or edge. The prefix and terminal-status checks pass and the assembler assigns fresh before/after digests to the historical resolution. Require supplied current dispositions to bind the exact computed target. Preserve the old target binding and require a new explicit disposition when the target changes. Test the unchanged historical row against a changed target, as well as legitimate continued history.
2. The validate-records output can overwrite its evidence. It writes args.out after reading the packet, evidence, profile, blob map and blob files. Passing any of those input paths as args.out overwrites that input even on validator rejection. Guard all input paths and mapped blobs against output aliases before writing, or require exclusive creation of a fresh output. Test a direct alias and verify original bytes survive.

This review covers tooling only. Production dossier contents, mathematical completeness, authentication and live gate behavior require their own evidence.
