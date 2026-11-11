"""Create a portable inventory without changing the frozen author record or TeX."""
from pathlib import Path, PurePosixPath
import argparse, copy, hashlib, json
HERE=Path(__file__).resolve().parent
AUTHOR=HERE.parent/'APPLICATIONS.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def canonical_sha(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def external_record(record,catalog_pin):
    return {'id':record['id'],'bibliography':record['bibliography'],'urls':record.get('urls',[]),
      'version_notes':record.get('version_notes',''),'source_status':record.get('source_status',''),
      'sourceCatalog':dict(catalog_pin,recordId=record['id'],recordSha256=canonical_sha(record)),
      'files':[{'sourceFilename':PurePosixPath(f['workspace_relative_path'].replace('\\','/')).name,'sha256':f['sha256'],'bytes':f['bytes']} for f in record['files']],
      'availability':'External source bytes are not asserted to be distributed in this repository. These exact pins and qualifications are verified against its frozen public source catalog.'}
def transform(author):
    out=copy.deepcopy(author)
    catalog_pin={'path':'docs/theorem-application-audit/sources.json','sha256':author['existingSourceCatalog']['sha256']}
    ex={k:external_record(v,catalog_pin) for k,v in author['externalSources'].items()}
    def walk(x):
        if isinstance(x,list):return [walk(v) for v in x]
        if not isinstance(x,dict):return x
        if 'bibliography' in x and x.get('id') in ex and 'files' in x:return copy.deepcopy(ex[x['id']])
        d={k:walk(v) for k,v in x.items()}
        if 'path' in d:
            p=d['path'].replace('\\','/')
            if p.endswith('/06-product/manuscript-v12/addition.tex'):p='docs/manuscript-revisions/version12/addition.tex'
            elif '/quartic-version6-release/repository/' in p:p=p.split('/quartic-version6-release/repository/',1)[1]
            elif '/10-combination/' in p:p='quartics/quartic-498-514/'+p.rsplit('/',1)[1]
            else:raise ValueError('Unmapped path: '+p)
            d['path']=p
        return d
    out=walk(out)
    out['schema']='portable-application-inventory-v1'
    out['status']='Author application inventory; independent acceptance is recorded separately.'
    out['portability']={'authorRecordSha256':sha(AUTHOR),'mappingVersion':1,
       'authorArchive':'AUTHOR-APPLICATIONS.json',
       'changes':'Only path bindings, external-source metadata representation, schema/status metadata and this provenance object changed. Application IDs, obligations, consumer labels/lines, source labels/lines and mathematical prose are preserved.',
       'sourceAvailability':'All active path bindings refer to repository files. External publications are identified by exact existing catalog pins, not claimed as included files.'}
    return out
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);a=ap.parse_args()
    author=json.loads(AUTHOR.read_text());(HERE/'AUTHOR-APPLICATIONS.json').write_bytes(AUTHOR.read_bytes())
    portable=transform(author)
    (HERE/'APPLICATIONS.json').write_text(json.dumps(portable,indent=2)+'\n')
    print(json.dumps({'records':len(portable['applications']),'authorSha256':sha(AUTHOR),'portableSha256':sha(HERE/'APPLICATIONS.json')},indent=2))
