"""Stream every object in a local Git commit into a complete content manifest.

Object hashes and commit/tree links are verified. GitHub origin, current PR state,
reviewer identities and merge authorization are NOT established by this collector.
No checkout, filters, hooks, candidate programs or lazy network fetches are run.
"""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import unicodedata

CHUNK = 1024 * 1024
MAX_COMMIT = 1024 * 1024
MAX_TREE = 32 * 1024 * 1024
MAX_BLOB = 1024 * 1024 * 1024
MAX_UNIQUE_BYTES = 4 * 1024 * 1024 * 1024
MAX_FILES = 100000
MAX_TREE_DEPTH = 128
MAX_TREE_VISITS = 100000
MAX_TREE_BYTES = 128 * 1024 * 1024
MAX_PATH_BYTES = 4096

class Invalid(ValueError):
    pass

def need(value, message):
    if not value:raise Invalid(message)

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',', ':'),ensure_ascii=False,allow_nan=False).encode('utf-8')

def sha(raw):return hashlib.sha256(raw).hexdigest()

def oid_ok(oid,algorithm):
    return type(oid) is str and re.fullmatch('[0-9a-f]{%d}' % (40 if algorithm=='sha1' else 64),oid) is not None

def object_hash(kind,raw,algorithm):
    return hashlib.new(algorithm,kind.encode()+b' '+str(len(raw)).encode()+b'\0'+raw).hexdigest()

def path_ok(path):
    return (type(path) is str and bool(path) and unicodedata.normalize('NFC',path)==path
        and len(path.encode('utf-8'))<=MAX_PATH_BYTES
        and not any(ord(c)<32 or c in '\\:' for c in path)
        and all(p not in ('','.','..') and p.casefold()!='.git' for p in path.split('/')))

def fields(value,names):need(type(value) is dict and set(value)==set(names.split()),'unexpected schema fields')

def git_environment():
    env={k:v for k,v in os.environ.items() if not k.startswith('GIT_')}
    env.update(GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL=os.devnull,
        GIT_NO_REPLACE_OBJECTS='1',GIT_NO_LAZY_FETCH='1',GIT_TERMINAL_PROMPT='0')
    return env

class ObjectReader:
    def __init__(self,repo):
        resolved=Path(repo).resolve().as_posix()
        self.command=['git','--no-replace-objects','-c','safe.directory='+resolved,'-C',resolved]
        self.env=git_environment()
        result=subprocess.run(self.command+['rev-parse','--show-object-format'],env=self.env,capture_output=True,check=True)
        self.algorithm=result.stdout.decode('ascii').strip()
        need(self.algorithm in ('sha1','sha256'),'unsupported Git hash')
        self.proc=subprocess.Popen(self.command+['cat-file','--batch'],env=self.env,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
    def read(self,oid,kind,maximum,keep=False):
        need(oid_ok(oid,self.algorithm),'invalid object ID')
        self.proc.stdin.write(oid.encode()+b'\n');self.proc.stdin.flush()
        header=self.proc.stdout.readline(1024)
        parts=header.rstrip(b'\n').split(b' ')
        need(len(parts)==3 and parts[0]==oid.encode() and parts[1]==kind.encode(),'missing or wrong object')
        need(parts[2].isdigit(),'invalid object size')
        size=int(parts[2]);need(size<=maximum,'object exceeds explicit size limit')
        gh=hashlib.new(self.algorithm,kind.encode()+b' '+str(size).encode()+b'\0')
        content=hashlib.sha256();pieces=[];left=size
        while left:
            block=self.proc.stdout.read(min(CHUNK,left));need(bool(block),'truncated object')
            left-=len(block);gh.update(block);content.update(block)
            if keep:pieces.append(block)
        need(self.proc.stdout.read(1)==b'\n','bad batch terminator')
        need(gh.hexdigest()==oid,'Git object hash mismatch')
        return b''.join(pieces) if keep else None,size,content.hexdigest()
    def close(self):
        if self.proc.poll() is None:
            self.proc.stdin.close()
            try:self.proc.wait(timeout=5)
            except subprocess.TimeoutExpired:self.proc.kill();self.proc.wait()
        self.proc.stdout.close()
    def __enter__(self):return self
    def __exit__(self,*args):self.close()

def parse_tree(raw,algorithm):
    width=20 if algorithm=='sha1' else 32
    entries=[];pos=0;names=set()
    while pos<len(raw):
        space=raw.find(b' ',pos);zero=raw.find(b'\0',space+1)
        need(space>pos and zero>space and zero+1+width<=len(raw),'malformed tree')
        mode=raw[pos:space].decode('ascii');name=raw[space+1:zero].decode('utf-8')
        need('/' not in name and path_ok(name) and name not in names,'invalid tree name')
        names.add(name);oid=raw[zero+1:zero+1+width].hex();pos=zero+1+width
        need(mode in ('40000','100644','100755'),'unsupported file mode')
        entries.append((name,mode,oid))
    return entries

def commit_tree(raw,algorithm):
    first=raw.split(b'\n',1)[0]
    need(first.startswith(b'tree '),'commit missing first tree header')
    tree=first[5:].decode('ascii');need(oid_ok(tree,algorithm),'invalid commit tree ID')
    return tree

def reconstructed_tree(files,algorithm):
    nodes={};folded={};tree_count=1;tree_bytes=0
    for path,item in files.items():
        need(path_ok(path),'unsafe path')
        pieces=path.split('/')
        need(len(pieces)-1<=MAX_TREE_DEPTH,'tree depth limit')
        for n in range(1,len(pieces)+1):
            prefix='/'.join(pieces[:n]);key=prefix.casefold()
            need(key not in folded or folded[key]==prefix,'case-colliding path');folded[key]=prefix
        node=nodes
        for part in pieces[:-1]:
            if part not in node:
                tree_count+=1;need(tree_count<=MAX_TREE_VISITS,'tree work limit')
                node[part]={}
            node=node[part]
            need(type(node) is dict,'file/directory collision')
        need(pieces[-1] not in node,'duplicate file/directory path')
        node[pieces[-1]]=(item['mode'],item['blob'])
    def encode(node):
        nonlocal tree_bytes
        entries=[]
        for name,value in node.items():
            directory=type(value) is dict
            mode,oid=('40000',encode(value)) if directory else value
            name=name.encode('utf-8')
            entries.append((name+(b'/' if directory else b''),mode.encode()+b' '+name+b'\0'+bytes.fromhex(oid)))
        raw=b''.join(raw for _,raw in sorted(entries))
        tree_bytes+=len(raw)
        need(len(raw)<=MAX_TREE and tree_bytes<=MAX_TREE_BYTES,'tree byte budget')
        return object_hash('tree',raw,algorithm)
    return encode(nodes)

def verify_manifest(manifest):
    fields(manifest,'schema git_hash commit commit_raw_base64 tree files stats')
    need(manifest['schema']=='research-git-manifest/v1','wrong manifest schema')
    alg=manifest['git_hash'];need(alg in ('sha1','sha256'),'unsupported hash')
    need(oid_ok(manifest['commit'],alg) and oid_ok(manifest['tree'],alg),'invalid commit/tree ID')
    need(type(manifest['commit_raw_base64']) is str and len(manifest['commit_raw_base64'])<=4*((MAX_COMMIT+2)//3),'commit too large')
    try:raw=base64.b64decode(manifest['commit_raw_base64'],validate=True)
    except (ValueError,TypeError):raise Invalid('bad commit encoding') from None
    need(len(raw)<=MAX_COMMIT,'decoded commit too large')
    need(base64.b64encode(raw).decode()==manifest['commit_raw_base64'],'noncanonical commit encoding')
    need(object_hash('commit',raw,alg)==manifest['commit'],'commit object mismatch')
    need(commit_tree(raw,alg)==manifest['tree'],'commit/tree mismatch')
    files=manifest['files'];need(type(files) is dict and len(files)<=MAX_FILES,'file count limit')
    blobs={}
    for path,item in files.items():
        fields(item,'mode blob size sha256')
        need(item['mode'] in ('100644','100755') and oid_ok(item['blob'],alg),'unsupported blob')
        need(type(item['size']) is int and 0<=item['size']<=MAX_BLOB,'blob size limit')
        need(type(item['sha256']) is str and re.fullmatch('[0-9a-f]{64}',item['sha256']) is not None,'bad content hash')
        facts=(item['size'],item['sha256'])
        need(item['blob'] not in blobs or blobs[item['blob']]==facts,'conflicting same-blob metadata')
        blobs[item['blob']]=facts
    need(reconstructed_tree(files,alg)==manifest['tree'],'manifest tree mismatch')
    totals={'file_count':len(files),'path_bytes':sum(v['size'] for v in files.values()),
        'unique_blobs':len(blobs),'unique_blob_bytes':sum(v[0] for v in blobs.values())}
    fields(manifest['stats'],'file_count path_bytes unique_blobs unique_blob_bytes')
    need(all(type(manifest['stats'][k]) is int for k in totals) and manifest['stats']==totals,'incorrect totals')
    need(totals['unique_blob_bytes']<=MAX_UNIQUE_BYTES,'total size limit')
    return {'manifest_sha256':sha(canonical(manifest)),'commit_object_verified':True,
        'complete_tree_verified':True,'github_origin_authenticated':False,'merge_authorized':False}

def collect(repo,commit):
    with ObjectReader(repo) as reader:
        alg=reader.algorithm;need(oid_ok(commit,alg),'commit must be a full object ID')
        raw,_,_=reader.read(commit,'commit',MAX_COMMIT,keep=True)
        tree=commit_tree(raw,alg);files={};active=set();tree_visits=0;tree_bytes=0
        def walk(tree_id,prefix='',depth=0):
            nonlocal tree_visits,tree_bytes
            need(depth<=MAX_TREE_DEPTH,'tree depth limit')
            tree_visits+=1;need(tree_visits<=MAX_TREE_VISITS,'tree work limit')
            need(tree_id not in active,'cyclic tree');active.add(tree_id)
            data,size,_=reader.read(tree_id,'tree',min(MAX_TREE,MAX_TREE_BYTES-tree_bytes),keep=True)
            tree_bytes+=size;need(tree_bytes<=MAX_TREE_BYTES,'tree byte budget')
            need(data or not prefix,'unsupported empty subtree')
            for name,mode,oid in parse_tree(data,alg):
                path=prefix+name
                need(path_ok(path),'unsafe or overlong path')
                if mode=='40000':walk(oid,path+'/',depth+1)
                else:
                    need(path not in files and len(files)<MAX_FILES,'file count or duplicate path')
                    files[path]={'mode':mode,'blob':oid}
            active.remove(tree_id)
        walk(tree)
        metadata={};total=0
        for oid in sorted({x['blob'] for x in files.values()}):
            _,size,content_hash=reader.read(oid,'blob',min(MAX_BLOB,MAX_UNIQUE_BYTES-total))
            total+=size;metadata[oid]={'size':size,'sha256':content_hash}
        for item in files.values():item.update(metadata[item['blob']])
        manifest={'schema':'research-git-manifest/v1','git_hash':alg,'commit':commit,
            'commit_raw_base64':base64.b64encode(raw).decode(),'tree':tree,'files':files,
            'stats':{'file_count':len(files),'path_bytes':sum(x['size'] for x in files.values()),
                'unique_blobs':len(metadata),'unique_blob_bytes':total}}
        verify_manifest(manifest)
        return manifest

def verify_blob(stream,entry,algorithm):
    """Verify a separately transported blob without retaining its body in memory."""
    fields(entry,'mode blob size sha256')
    need(algorithm in ('sha1','sha256') and oid_ok(entry['blob'],algorithm),'bad hash algorithm/object')
    need(type(entry['size']) is int and 0<=entry['size']<=MAX_BLOB,'invalid blob size')
    gh=hashlib.new(algorithm,b'blob '+str(entry['size']).encode()+b'\0');sh=hashlib.sha256();left=entry['size']
    while left:
        block=stream.read(min(CHUNK,left));need(bool(block),'truncated blob transport')
        need(len(block)<=left,'oversized blob read');left-=len(block);gh.update(block);sh.update(block)
    need(not stream.read(1),'trailing blob bytes')
    need(gh.hexdigest()==entry['blob'] and sh.hexdigest()==entry['sha256'],'transported blob hash mismatch')
    return True

def load_json(path):
    def pairs(items):
        d={}
        for k,v in items:need(k not in d,'duplicate JSON key');d[k]=v
        return d
    def constant(_):raise Invalid('nonfinite JSON')
    with open(path,encoding='utf-8-sig') as f:return json.load(f,object_pairs_hook=pairs,parse_constant=constant)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('repository');p.add_argument('commit');p.add_argument('--output',required=True)
    a=p.parse_args();m=collect(a.repository,a.commit)
    Path(a.output).write_bytes(canonical(m)+b'\n')
    print(json.dumps(dict(verify_manifest(m),**m['stats']),indent=2))

if __name__=='__main__':main()
