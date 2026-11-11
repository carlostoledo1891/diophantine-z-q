"""A manifest-bound, deduplicated research annex; never execute its contents."""
import argparse
from datetime import date
import hashlib
import io
import json
from pathlib import Path
import re
import stat
import zipfile

from release_common import safe, sha, json_bytes

ANNEX = 'research/version14/z-in-q-version14-research-annex.zip'
MAX_TOTAL = 2 * 1024**3
MAX_MEMBER = 128 * 1024**2
MAX_MANIFEST = 16 * 1024**2
DENIED = {'.git', '.env', '.ssh', '.aws', 'credentials', 'secrets',
          'conversations', 'transcripts', 'chat_history', 'node_modules', '__pycache__'}


def logical_path(name):
    path = safe(name)
    if any(part.lower() in DENIED for part in path.parts) or path.suffix.lower() in {'.pem','.key','.p12','.pfx','.zip','.pdf'}:
        raise ValueError('Excluded annex source: ' + name)
    return path


def catalogue(value):
    if set(value) != {'schema','scope','files','unavailable'} or value['schema'] != 'research-annex/v1':
        raise ValueError('Invalid annex manifest')
    if not isinstance(value['scope'], str) or not value['scope'].strip() or not isinstance(value['unavailable'], list):
        raise ValueError('Missing annex scope or unavailable-source record')
    if not isinstance(value['files'], list) or not 0 < len(value['files']) <= 20000:
        raise ValueError('Invalid annex source count')
    paths = set(); content = {}
    for row in value['files']:
        if set(row) != {'path','sha256','bytes','category','status'}:
            raise ValueError('Invalid annex source fields')
        logical_path(row['path'])
        if row['path'] in paths:
            raise ValueError('Duplicate logical source path')
        paths.add(row['path'])
        if not isinstance(row['sha256'], str) or re.fullmatch('[0-9a-f]{64}',row['sha256']) is None:
            raise ValueError('Invalid annex source digest')
        if type(row['bytes']) is not int or not 0 <= row['bytes'] <= MAX_MEMBER:
            raise ValueError('Invalid annex source size')
        if any(not isinstance(row[k],str) or not row[k].strip() for k in ('category','status')):
            raise ValueError('Missing research provenance')
        if row['sha256'] in content and content[row['sha256']] != row['bytes']:
            raise ValueError('Inconsistent deduplicated source size')
        content[row['sha256']] = row['bytes']
    if sum(content.values()) > MAX_TOTAL:
        raise ValueError('Annex expands beyond the reviewed size limit')
    return content


def validate(raw):
    def unique_fields(pairs):
        result={}
        for key,value in pairs:
            if key in result:raise ValueError('Duplicate annex JSON field')
            result[key]=value
        return result
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        infos=archive.infolist()
        names=[x.filename for x in infos]
        if len(names)!=len(set(names)) or 'MANIFEST.json' not in names:
            raise ValueError('Missing or duplicate annex members')
        item=archive.getinfo('MANIFEST.json')
        if item.file_size > MAX_MANIFEST:
            raise ValueError('Oversized annex manifest')
        manifest=json.loads(archive.read(item),object_pairs_hook=unique_fields)
        content=catalogue(manifest)
        if set(names) != {'MANIFEST.json'} | {'content/'+h for h in content}:
            raise ValueError('Unlisted or missing annex content')
        for item in infos:
            if item.flag_bits & 1 or not stat.S_ISREG(item.external_attr >> 16):
                raise ValueError('Encrypted or nonregular annex entry')
        for digest,size in content.items():
            item=archive.getinfo('content/'+digest)
            if item.file_size != size:
                raise ValueError('Annex size mismatch')
            h=hashlib.sha256(); count=0; tail=b''
            with archive.open(item) as source:
                while chunk:=source.read(1024**2):
                    count+=len(chunk)
                    if count > size:raise ValueError('Annex expansion mismatch')
                    sample=tail+chunk
                    if (b'-----BEGIN ' + b'PRIVATE KEY-----') in sample or (b'-----BEGIN ' + b'RSA PRIVATE KEY-----') in sample:
                        raise ValueError('Private key marker in annex')
                    tail=sample[-64:]
                    h.update(chunk)
            if count!=size or h.hexdigest()!=digest:
                raise ValueError('Annex content digest mismatch')
    return {'logical_files':len(manifest['files']),'unique_contents':len(content),
            'unique_bytes':sum(content.values()),'unavailable':manifest['unavailable']}


def build(manifest, sources, workspace, output, day):
    content=catalogue(manifest)
    if set(sources)!=set(content):raise ValueError('Explicit content-source map mismatch')
    workspace=workspace.resolve()
    paths={}
    for digest,name in sources.items():
        logical_path(name)
        path=(workspace/name).resolve()
        if not path.is_relative_to(workspace) or not path.is_file():
            raise ValueError('Source outside workspace or missing')
        if path.stat().st_size!=content[digest] or sha(path.read_bytes())!=digest:
            raise ValueError('Changed source; preserve its old pin and review a new snapshot')
        paths[digest]=path
    def info(name):
        entry=zipfile.ZipInfo(name,(day.year,day.month,day.day,0,0,0))
        entry.create_system=3;entry.external_attr=(stat.S_IFREG|0o644)<<16
        entry.compress_type=zipfile.ZIP_DEFLATED
        return entry
    with zipfile.ZipFile(output,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
        archive.writestr(info('MANIFEST.json'),json_bytes(manifest))
        for digest,path in sorted(paths.items()):
            with path.open('rb') as source, archive.open(info('content/'+digest),'w',force_zip64=True) as target:
                while chunk:=source.read(1024**2):target.write(chunk)
    return validate(output.read_bytes())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',required=True,type=Path)
    parser.add_argument('--manifest-sha256',required=True)
    parser.add_argument('--sources',required=True,type=Path)
    parser.add_argument('--sources-sha256',required=True)
    parser.add_argument('--workspace',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--date',required=True,type=date.fromisoformat)
    args=parser.parse_args()
    for path,digest in ((args.manifest,args.manifest_sha256),(args.sources,args.sources_sha256)):
        if sha(path.read_bytes())!=digest:raise ValueError('Unreviewed selection bytes')
    result=build(json.loads(args.manifest.read_bytes()),json.loads(args.sources.read_bytes()),args.workspace,args.output,args.date)
    print(json.dumps(dict(result,sha256=sha(args.output.read_bytes()),bytes=args.output.stat().st_size)))


if __name__=='__main__':main()
