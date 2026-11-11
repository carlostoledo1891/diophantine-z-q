"""Restore exclusive ephemeral SQLite mirrors under remote-authoritative anchors.

Remote anchors implement read() and compare_and_swap(expected,replacement).
Their authentication, durability and freshness are trusted external dependencies.
No remote anchor is initialized, replaced or lowered by this module.
"""
import copy
import os
from pathlib import Path
import tempfile
import operator_ledger
import audit_intake
from protected_ledger_store import ProtectedPath,LedgerStore,connect,Conflict
from audit_intake_store import AuditStore

def _restore(location,anchor,entries,keys,expected_checkpoint,codec,store_type):
    entries=copy.deepcopy(entries);expected_checkpoint=copy.deepcopy(expected_checkpoint)
    codec.verify(entries,keys,expected_checkpoint)
    target=location.checked()
    codec.need(not target.exists(),'restore target already exists')
    if codec.canonical(anchor.read())!=codec.canonical(expected_checkpoint):
        raise Conflict('remote authoritative checkpoint differs before restore')
    descriptor,name=tempfile.mkstemp(prefix='verified-ledger-',suffix='.sqlite',dir=target.parent)
    os.close(descriptor);temporary=Path(name).resolve()
    temporary_location=ProtectedPath(temporary,location.candidate_roots)
    try:
        with connect(temporary_location) as db:
            db.execute('BEGIN IMMEDIATE')
            db.execute('CREATE TABLE metadata (id INTEGER PRIMARY KEY CHECK(id=1), checkpoint BLOB NOT NULL)')
            db.execute('CREATE TABLE entries (sequence INTEGER PRIMARY KEY, payload BLOB NOT NULL)')
            db.execute('INSERT INTO metadata VALUES (1,?)',(codec.canonical(expected_checkpoint),))
            db.executemany('INSERT INTO entries VALUES (?,?)',[(e['sequence'],codec.canonical(e)) for e in entries])
            db.commit()
        if codec.canonical(anchor.read())!=codec.canonical(expected_checkpoint):
            raise Conflict('remote authoritative checkpoint changed during restore')
        # Same-directory hard link gives atomic no-overwrite installation. A
        # filesystem lacking hard links fails rather than using replacing rename.
        os.link(temporary,target)
        store=store_type(location,anchor,expected_checkpoint['ledger_id'],keys)
        store.read_verified()  # Includes another remote current-checkpoint check.
        return store
    finally:
        # Exact temporary file only, never recursive deletion or remote mutation.
        temporary.unlink(missing_ok=True)

def restore_operator_store(location,anchor,entries,keys,expected_checkpoint):
    return _restore(location,anchor,entries,keys,expected_checkpoint,operator_ledger,LedgerStore)

def restore_audit_store(location,anchor,entries,keys,expected_checkpoint):
    return _restore(location,anchor,entries,keys,expected_checkpoint,audit_intake,AuditStore)
