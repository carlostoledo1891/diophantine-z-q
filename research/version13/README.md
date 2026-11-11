# Version 13 research supplement

The supplement is packaged as [z-in-q-version13-supplement.zip](z-in-q-version13-supplement.zip) after the final manuscript, contracts and release checks are complete. Its packaging receipt records the exact hash and size. The archive target is not itself an approval of an unfinished snapshot.

The handoff preserves the November 7, 2026 manuscript, the portable 394/411-variable construction, complete coefficient tables, application inventory, independent review records and the selected research evidence. The [Version 12 supplement](../version12/README.md) remains the preceding historical reference. The archive contains no conversational transcript or credentials.

Start with the [Version 13 guide](../../docs/manuscript-revisions/version13/GUIDE.md). The package's source and file manifests identify the exact inputs. After restoration, run from the restored repository root:

```sh
python -B scripts/check_quartic394_portable.py
python -B docs/manuscript-revisions/version13/validate-applications.py --repo . --self-test
python -B scripts/check_audit_history.py --self-test
```

The Version 13 finite replay and inventory validator use Python's standard library. These checks establish their stated algebraic, coefficient and record-integrity properties. They do not prove all inherited arithmetic inputs or complete the Lean formalization. Primary source versions and redistribution limits remain recorded in the inventories and [third-party notices](../../THIRD_PARTY_NOTICES.md).
