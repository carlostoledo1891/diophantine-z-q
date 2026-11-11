"""Bounded audit-log persistence, derived from accepted protected_ledger_store.

Same explicit isolation/external-current-checkpoint contract; distinct log codec.
No real keys or databases are created by importing this module.
"""
import copy
import audit_intake as ledger
from protected_ledger_store import ProtectedPath,SQLiteAnchor,connect,decode,Conflict,RecoveryRequired

class AuditStore:
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
        rows=[];total=0
        for item in db.execute('SELECT sequence,payload FROM entries ORDER BY sequence'):
            total+=len(item[1])
            ledger.need(len(item[1])<=ledger.MAX_EVENT and total<=ledger.MAX_LOG and len(rows)<ledger.MAX_ENTRIES,'intake database byte/count limit')
            rows.append(item)
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
        try:
            advanced=self.anchor.compare_and_swap(expected_checkpoint,new_checkpoint)
        except Exception:
            raise RecoveryRequired('intake append committed; anchor unavailable; explicit forward recovery required',new_checkpoint) from None
        if not advanced:
            raise RecoveryRequired('intake append committed; anchor CAS failed; explicit forward recovery required',new_checkpoint)
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
