"""Protected local generations. A SQLite lock serializes our remote mutations.

This is not a distributed transaction with GitHub. Committed mutation_intent
marks an interrupted operation as needing reconciliation on the next run.
"""
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
import json
import sqlite3
import uuid

class StaleGeneration(Exception):pass

@dataclass(frozen=True)
class Lease:
    key: str
    generation: int
    token: str

class SQLiteGenerationState:
    def __init__(self,path,candidate_roots):
        self.path=Path(path)
        if not self.path.is_absolute() or self.path.resolve()!=self.path or self.path.is_symlink():
            raise ValueError('state path must be absolute, resolved and not a symlink')
        if not candidate_roots:raise ValueError('explicit candidate write roots required')
        for value in candidate_roots:
            root=Path(value)
            if not root.is_absolute() or root.resolve()!=root:raise ValueError('invalid candidate root')
            if self.path==root or root in self.path.parents:raise ValueError('state is candidate writable')
        if not self.path.parent.is_dir():raise ValueError('state parent does not exist')
    def initialize(self):
        # Never reset a pre-existing state file or silently recreate a lost one.
        with self.path.open('xb'):pass
        db=sqlite3.connect(self.path)
        try:
            db.execute('PRAGMA synchronous=FULL')
            db.execute('CREATE TABLE generations (key TEXT PRIMARY KEY, generation INTEGER NOT NULL, token TEXT NOT NULL, phase TEXT NOT NULL, detail TEXT NOT NULL)')
            db.execute('CREATE TABLE targets (key TEXT NOT NULL, target TEXT NOT NULL, PRIMARY KEY (key,target))')
            db.commit()
        finally:db.close()
    @contextmanager
    def _db(self):
        if not self.path.is_file() or self.path.is_symlink():raise ValueError('protected state unavailable')
        db=sqlite3.connect(self.path.as_uri()+'?mode=rw',uri=True,isolation_level=None,timeout=5)
        db.execute('PRAGMA trusted_schema=OFF');db.execute('PRAGMA synchronous=FULL')
        try:yield db
        finally:
            if db.in_transaction:db.rollback()
            db.close()
    def read(self,key):
        with self._db() as db:r=db.execute('SELECT generation,token,phase,detail FROM generations WHERE key=?',(key,)).fetchone()
        return {'generation':r[0],'token':r[1],'phase':r[2],'detail':json.loads(r[3])} if r else {'generation':0,'token':'','phase':'new','detail':{}}
    def begin(self,key,expected_generation):
        if type(expected_generation) is not int or expected_generation<0:raise ValueError('exact generation required')
        with self._db() as db:
            db.execute('BEGIN IMMEDIATE')
            r=db.execute('SELECT generation FROM generations WHERE key=?',(key,)).fetchone()
            if (r[0] if r else 0)!=expected_generation:raise StaleGeneration('generation changed')
            token=uuid.uuid4().hex;generation=expected_generation+1
            if r:db.execute('UPDATE generations SET generation=?,token=?,phase=?,detail=? WHERE key=?',(generation,token,'pending','{}',key))
            else:db.execute('INSERT INTO generations VALUES (?,?,?,?,?)',(key,generation,token,'pending','{}'))
            db.commit();return Lease(key,generation,token)
    def _require(self,db,lease):
        r=db.execute('SELECT generation,token FROM generations WHERE key=?',(lease.key,)).fetchone()
        if r!=(lease.generation,lease.token):raise StaleGeneration('superseded generation')
    def assert_current(self,lease):
        with self._db() as db:self._require(db,lease)
    def known_targets(self,key):
        with self._db() as db:return tuple(r[0] for r in db.execute('SELECT target FROM targets WHERE key=? ORDER BY target',(key,)))
    def remember_target(self,lease,target):
        with self._db() as db:
            db.execute('BEGIN IMMEDIATE');self._require(db,lease)
            db.execute('INSERT OR IGNORE INTO targets VALUES (?,?)',(lease.key,target));db.commit()
    def snapshot(self):
        """Trusted controller can durably commit this before permitting success."""
        with self._db() as db:
            db.execute('BEGIN')
            generations=[{'key':k,'generation':g,'token':t,'phase':p,'detail':json.loads(d)} for k,g,t,p,d in db.execute('SELECT key,generation,token,phase,detail FROM generations ORDER BY key')]
            targets=[{'key':k,'target':t} for k,t in db.execute('SELECT key,target FROM targets ORDER BY key,target')]
        return {'schema':'protocol-publisher-state/v1','generations':generations,'targets':targets}
    def restore_trusted(self,snapshot):
        """Only into empty initialized state, from authenticated remote authority.

        This method does not authenticate a supplied snapshot. The controller
        must verify its protected state-ref/CAS chain before calling it.
        """
        if type(snapshot) is not dict or set(snapshot)!={'schema','generations','targets'} or snapshot['schema']!='protocol-publisher-state/v1':raise ValueError('invalid state snapshot')
        with self._db() as db:
            db.execute('BEGIN IMMEDIATE')
            if db.execute('SELECT count(*) FROM generations').fetchone()[0] or db.execute('SELECT count(*) FROM targets').fetchone()[0]:raise ValueError('restore requires empty state')
            for r in snapshot['generations']:
                if type(r) is not dict or set(r)!={'key','generation','token','phase','detail'} or type(r['generation']) is not int or r['generation']<1 or not all(type(r[k]) is str and r[k] for k in ('key','token','phase')) or type(r['detail']) is not dict:raise ValueError('invalid generation snapshot')
                db.execute('INSERT INTO generations VALUES (?,?,?,?,?)',(r['key'],r['generation'],r['token'],r['phase'],json.dumps(r['detail'],sort_keys=True)))
            for r in snapshot['targets']:
                if type(r) is not dict or set(r)!={'key','target'} or type(r['target']) is not str or len(r['target'])!=40:raise ValueError('invalid target snapshot')
                if not db.execute('SELECT 1 FROM generations WHERE key=?',(r['key'],)).fetchone():raise ValueError('orphan target snapshot')
                db.execute('INSERT INTO targets VALUES (?,?)',(r['key'],r['target']))
            db.commit()
    def intent(self,lease):
        with self._db() as db:
            db.execute('BEGIN IMMEDIATE');self._require(db,lease)
            db.execute('UPDATE generations SET phase=?,detail=? WHERE key=?',('mutation_intent','{}',lease.key));db.commit()
    def perform(self,lease,operation,phase,detail=None):
        """The operation includes its final reads and remote write under one lock."""
        with self._db() as db:
            db.execute('BEGIN IMMEDIATE');self._require(db,lease)
            try:result=operation()
            except Exception:
                db.execute('UPDATE generations SET phase=?,detail=? WHERE key=?',('uncertain','{}',lease.key));db.commit();raise
            db.execute('UPDATE generations SET phase=?,detail=? WHERE key=?',(phase,json.dumps(detail or {},sort_keys=True),lease.key));db.commit()
            return result

class LocalSQLiteAuthority:
    """Explicit long-lived local deployment only, NEVER an ephemeral runner.

    A controller deployment must inject its remote-CAS authority instead.
    """
    def __init__(self,state):self.state=state
    def begin(self,lease,snapshot):self.state.assert_current(lease)
    def assert_current(self,lease):self.state.assert_current(lease)
    def before_success(self,lease,snapshot,identity):self.state.assert_current(lease)
