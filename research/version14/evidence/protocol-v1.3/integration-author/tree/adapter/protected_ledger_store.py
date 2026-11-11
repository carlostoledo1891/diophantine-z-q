"""Protected local SQLite persistence for the accepted operator ledger.

The caller supplies protected paths, keys and a separately trusted anchor.
The database transaction and anchor CAS are NOT one distributed transaction.
Any interrupted mismatch blocks reads until explicit forward recovery.
"""
from dataclasses import dataclass
from pathlib import Path
import copy
import contextlib
import json
import sqlite3
import operator_ledger as ledger

class Conflict(ledger.Invalid):pass
class RecoveryRequired(ledger.Invalid):
    def __init__(self,message,pending_checkpoint=None):
        super().__init__(message)
        self.pending_checkpoint=copy.deepcopy(pending_checkpoint)

@dataclass(frozen=True)
class ProtectedPath:
    path: Path
    candidate_roots: tuple[Path,...]
    def checked(self):
        ledger.need(type(self.candidate_roots) is tuple and self.candidate_roots,'explicit candidate write roots required')
        p=Path(self.path)
        ledger.need(p.is_absolute(),'protected path must be absolute')
        ledger.need(not p.is_symlink(),'protected path cannot be a symlink')
        resolved=p.resolve()
        ledger.need(resolved==p,'protected path must be resolved')
        for root in self.candidate_roots:
            root=Path(root)
            ledger.need(root.is_absolute() and root.resolve()==root,'candidate write root must be absolute and resolved')
            ledger.need(resolved!=root and root not in resolved.parents,'protected state is inside candidate writes')
        ledger.need(p.parent.is_dir(),'protected state parent must already exist')
        return p

def decode(raw):
    raw=bytes(raw)
    def pairs(items):
        result={}
        for k,v in items:
            ledger.need(k not in result,'duplicate stored JSON key');result[k]=v
        return result
    value=json.loads(raw,object_pairs_hook=pairs)
    ledger.need(ledger.canonical(value)==raw,'noncanonical stored record')
    return value

@contextlib.contextmanager
def connect(location):
    p=location.checked()
    ledger.need(p.is_file(),'protected state not initialized')
    db=sqlite3.connect(p.as_uri()+'?mode=rw',uri=True,timeout=5,isolation_level=None)
    db.execute('PRAGMA trusted_schema=OFF');db.execute('PRAGMA synchronous=FULL')
    try:
        yield db
    finally:
        if db.in_transaction:db.rollback()
        db.close()

class SQLiteAnchor:
    """Separate trusted checkpoint store. Do not roll this back with the ledger."""
    def __init__(self,location):self.location=location
    def initialize(self,checkpoint):
        ledger.check_checkpoint(checkpoint);p=self.location.checked()
        with p.open('xb'):pass
        with connect(self.location) as db:
            db.execute('BEGIN IMMEDIATE')
            db.execute('CREATE TABLE anchor (id INTEGER PRIMARY KEY CHECK(id=1), checkpoint BLOB NOT NULL)')
            db.execute('INSERT INTO anchor VALUES (1,?)',(ledger.canonical(checkpoint),));db.commit()
    def read(self):
        with connect(self.location) as db:
            rows=db.execute('SELECT checkpoint FROM anchor').fetchall()
        ledger.need(len(rows)==1,'invalid anchor row count')
        value=decode(rows[0][0]);ledger.check_checkpoint(value);return value
    def compare_and_swap(self,expected,replacement):
        ledger.check_checkpoint(expected);ledger.check_checkpoint(replacement)
        ledger.need(expected['ledger_id']==replacement['ledger_id'] and replacement['sequence']>expected['sequence'],'anchor may only advance')
        with connect(self.location) as db:
            db.execute('BEGIN IMMEDIATE')
            changed=db.execute('UPDATE anchor SET checkpoint=? WHERE id=1 AND checkpoint=?',
                (ledger.canonical(replacement),ledger.canonical(expected))).rowcount
            db.commit();return changed==1

class LedgerStore:
    def __init__(self,location,anchor,ledger_id,trusted_keys):
        if trusted_keys is None:raise ledger.IntegrationMissing('protected key registry required')
        location.checked();self.location=location;self.anchor=anchor;self.ledger_id=ledger_id
        self.keys=copy.deepcopy(trusted_keys)
        if isinstance(anchor,SQLiteAnchor):
            ledger.need(location.checked()!=anchor.location.checked(),'anchor and ledger must be separate stores')
    def initialize(self):
        genesis=ledger.genesis(self.ledger_id)
        # Bootstrap is explicit and refuses existing state; reads never recreate it.
        self.anchor.initialize(genesis)
        p=self.location.checked()
        with p.open('xb'):pass
        with connect(self.location) as db:
            db.execute('BEGIN IMMEDIATE')
            db.execute('CREATE TABLE metadata (id INTEGER PRIMARY KEY CHECK(id=1), checkpoint BLOB NOT NULL)')
            db.execute('CREATE TABLE entries (sequence INTEGER PRIMARY KEY, payload BLOB NOT NULL)')
            db.execute('INSERT INTO metadata VALUES (1,?)',(ledger.canonical(genesis),));db.commit()
    def _load(self,db):
        meta=db.execute('SELECT checkpoint FROM metadata').fetchall()
        ledger.need(len(meta)==1,'invalid ledger metadata')
        checkpoint=decode(meta[0][0]);ledger.check_checkpoint(checkpoint)
        ledger.need(checkpoint['ledger_id']==self.ledger_id,'wrong protected ledger identity')
        rows=db.execute('SELECT sequence,payload FROM entries ORDER BY sequence').fetchall()
        ledger.need([r[0] for r in rows]==list(range(1,len(rows)+1)),'database sequence gap')
        return [decode(r[1]) for r in rows],checkpoint
    def read_verified(self):
        expected=self.anchor.read()
        ledger.need(expected['ledger_id']==self.ledger_id,'wrong anchor ledger identity')
        with connect(self.location) as db:
            db.execute('BEGIN')
            entries,stored=self._load(db);db.commit()
        if ledger.canonical(stored)!=ledger.canonical(expected):
            raise RecoveryRequired('database and external checkpoint disagree; no automatic rollback or repair',stored)
        state=ledger.verify(entries,self.keys,expected)
        if ledger.canonical(self.anchor.read())!=ledger.canonical(expected):raise Conflict('anchor changed during read')
        return entries,expected,state
    def assert_current(self,expected):
        _,current,_=self.read_verified()
        if ledger.canonical(current)!=ledger.canonical(expected):raise Conflict('ledger changed during evaluation')
    def append(self,event,key_id,expected_checkpoint):
        ledger.check_checkpoint(expected_checkpoint)
        if ledger.canonical(self.anchor.read())!=ledger.canonical(expected_checkpoint):raise Conflict('stale external checkpoint')
        with connect(self.location) as db:
            db.execute('BEGIN IMMEDIATE')
            entries,stored=self._load(db)
            if ledger.canonical(stored)!=ledger.canonical(expected_checkpoint):raise Conflict('stale database checkpoint')
            new_entries,new_checkpoint=ledger.append(entries,event,key_id,self.keys,expected_checkpoint)
            db.execute('INSERT INTO entries VALUES (?,?)',(new_checkpoint['sequence'],ledger.canonical(new_entries[-1])))
            db.execute('UPDATE metadata SET checkpoint=? WHERE id=1',(ledger.canonical(new_checkpoint),));db.commit()
        if not self.anchor.compare_and_swap(expected_checkpoint,new_checkpoint):
            raise RecoveryRequired('signed database append committed, but anchor CAS failed; explicit forward recovery required',new_checkpoint)
        return new_checkpoint
    def recover_forward(self,expected_anchor,expected_database_checkpoint):
        """Explicit trusted-operator action. Never lower or reconstruct an anchor."""
        with connect(self.location) as db:
            db.execute('BEGIN IMMEDIATE')
            entries,stored=self._load(db)
            if ledger.canonical(stored)!=ledger.canonical(expected_database_checkpoint):raise Conflict('database changed before recovery')
            if ledger.canonical(self.anchor.read())!=ledger.canonical(expected_anchor):raise Conflict('anchor changed before recovery')
            ledger.need(stored['sequence']>expected_anchor['sequence'],'recovery only advances to a signed tail')
            ledger.verify(entries[:expected_anchor['sequence']],self.keys,expected_anchor)
            ledger.verify(entries,self.keys,stored)
            if not self.anchor.compare_and_swap(expected_anchor,stored):raise Conflict('recovery anchor CAS failed')
            db.commit();return stored
