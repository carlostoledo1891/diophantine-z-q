"""Check that Version 8 changes only the approved abstract and version number."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT/'docs/manuscript-revisions/version8/revision.json'

def checked(record):
    path=(ROOT/record['path']).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError('Revision path escapes the repository')
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=record['sha256']:
        raise ValueError('Revision hash mismatch: '+record['path'])
    return raw

def main():
    manifest=json.loads(MANIFEST.read_bytes())
    if manifest['version']!=8 or manifest['base_version']!=7:
        raise ValueError('Unexpected manuscript revision')
    before=checked(manifest['baseline'])
    after=checked(manifest['candidate'])
    abstract=checked(manifest['abstract']).rstrip(b'\r\n')
    old_title=b'\\large Version 7.'
    if before.count(old_title)!=1:
        raise ValueError('Expected exactly one Version 7 title')
    begin=b'\\begin{abstract}'
    end=b'\\end{abstract}'
    if before.count(begin)!=1 or before.count(end)!=1:
        raise ValueError('Expected one abstract')
    start=before.index(begin)+len(begin)
    stop=before.index(end,start)
    newline=b'\r\n' if before[start:start+2]==b'\r\n' else b'\n'
    abstract=abstract.replace(b'\r\n',b'\n').replace(b'\n',newline)
    expected=(before[:start]+newline+abstract+newline+before[stop:]).replace(old_title,b'\\large Version 8.')
    if after!=expected:
        raise ValueError('The revision changes text outside the abstract and version number')
    print(json.dumps({'status':'PASS','version':8,'changes':['abstract','version number'],
                      'body_unchanged':True,'manuscript_sha256':manifest['candidate']['sha256'],
                      'baseline_sha256':manifest['baseline']['sha256']},indent=2))

if __name__=='__main__':main()
