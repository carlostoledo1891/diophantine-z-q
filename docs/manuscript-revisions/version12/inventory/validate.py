"""Validate portable v12 application bindings; this is not mathematical acceptance."""
from pathlib import Path, PurePosixPath
import argparse, copy, hashlib, json, re
HERE=Path(__file__).resolve().parent
EXPECTED_IDS={'V12-EXT-FORMAL3','V12-EXT-FORMAL2','V12-EXT-LOG-MIX','V12-EXT-LOG-SCALAR','V12-EXT-LOG-DEPTH','V12-EXT-QUATERNION','V12-INT-POINTS','V12-INT-TRUNCATION','V12-INT-DETECTOR','V12-INT-PRODUCTHEIGHT','V12-INT-HALFTRACE','V12-INT-ANCHOROLD','V12-INT-SCALARCONTACT','V12-INT-SCALARHEIGHT','V12-INT-SCALARCOMPLETE','V12-INT-PRIMES','V12-INT-LUCAS','V12-ALG-POLE','V12-ALG-RECIPROCAL','V12-ALG-DCANCEL','V12-ALG-TORIC','V12-ALG-NORMSQUARE','V12-ALG-COMPILE','V12-ALG-SOS','V12-ALG-LIFT'}
OBLIGATIONS={'required_inputs','constructed_inputs','domain_and_index_coverage','transition_maps_and_scalars','identity_of_consumed_object','exceptional_cases','affected_downstream_claims','source_version_and_conventions','validation_and_acceptance_scope'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def canonical_sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def demand(ok,message):
    if not ok:raise ValueError(message)
def validate(data,repo,author=None):
    repo=repo.resolve();cache={};pins=0;labels=0;source_records=0
    demand(data.get('schema')=='portable-application-inventory-v1','schema')
    rows=data['applications'];demand(len(rows)==25,'25 records required')
    demand({r['id'] for r in rows}==EXPECTED_IDS,'application ID coverage')
    demand(len({r['id'] for r in rows})==25,'duplicate IDs')
    for r in rows:
        demand(set(r['obligations'])==OBLIGATIONS,'obligations: '+r['id'])
        demand(all(isinstance(v,str) and v.strip() for v in r['obligations'].values()),'empty obligation: '+r['id'])
        demand(bool(r['source']) and bool(r['consumers']),'missing source or consumer: '+r['id'])
        demand(all(c.get('path')=='docs/manuscript-revisions/version12/addition.tex' for c in r['consumers']),'wrong consumer file')
    def filepin(d):
        nonlocal pins,labels
        rel=d['path'];q=PurePosixPath(rel)
        demand(isinstance(rel,str) and not q.is_absolute() and '\\' not in rel and ':' not in rel and '..' not in q.parts,'nonportable path '+str(rel))
        p=(repo/rel).resolve();demand(p.is_relative_to(repo),'path escapes repository')
        demand(p.is_file(),'missing file '+rel)
        if rel not in cache:cache[rel]=(sha(p),p.read_text(encoding='utf-8'))
        h,text=cache[rel];demand(d.get('sha256')==h,'stale file pin '+rel);pins+=1
        if 'label' in d:
            n=d['line'];lines=text.splitlines();needle='\\label{'+d['label']+'}'
            demand(isinstance(n,int) and 1<=n<=len(lines) and needle in lines[n-1],'stale label/line '+d['label']);labels+=1
        if 'lineCount' in d:demand(len(text.splitlines())==d['lineCount'],'line count')
        return text
    def walk(x):
        nonlocal source_records
        if isinstance(x,list):
            for v in x:walk(v)
        elif isinstance(x,dict):
            text=filepin(x) if 'path' in x else None
            if 'recordId' in x:
                demand(text is not None,'catalog reference has no path')
                matches=[r for r in json.loads(text) if r['id']==x['recordId']]
                demand(len(matches)==1 and canonical_sha(matches[0])==x['recordSha256'],'source record pin');source_records+=1
            for v in x.values():walk(v)
    walk(data)
    catalog={r['id']:r for r in json.loads((repo/data['existingSourceCatalog']['path']).read_text())}
    def check_external(e):
        r=catalog[e['id']]
        demand(e['sourceCatalog']['recordId']==e['id'],'wrong source ID')
        for k in ['bibliography','urls','version_notes','source_status']:demand(e[k]==r.get(k,[] if k=='urls' else ''),'source metadata '+k)
        files=[{'sourceFilename':PurePosixPath(f['workspace_relative_path'].replace('\\','/')).name,'sha256':f['sha256'],'bytes':f['bytes']} for f in r['files']]
        demand(e['files']==files,'external file pins')
    demand(set(data['externalSources'])=={'silverman','voight-quaternion'},'external source coverage')
    for e in data['externalSources'].values():check_external(e)
    for r in rows:
        if r['kind']=='external':
            s=r['source'];demand(s['id']==s['pinned_source']['id'] and bool(s['location']),'external locator')
            check_external(s['pinned_source'])
    text=(repo/data['text']['path']).read_text();old=(repo/data['baselineManuscript']['path']).read_text()
    newlabels=re.findall(r'\\label\{([^}]+)\}',text);oldlabels=set(re.findall(r'\\label\{([^}]+)\}',old))
    demand(len(newlabels)==len(set(newlabels)) and not set(newlabels)&oldlabels,'new label uniqueness')
    refs=set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',text));demand(refs<=oldlabels|set(newlabels),'unresolved text reference')
    demand({r['label'] for r in data['allExplicitInheritedReferences']}==refs-set(newlabels),'inherited reference inventory')
    if author:
        demand(sha(author)==data['portability']['authorRecordSha256'],'author archive hash')
        original=json.loads(author.read_text());by={r['id']:r for r in original['applications']}
        for r in rows:
            demand(r['obligations']==by[r['id']]['obligations'],'changed obligation prose')
            demand(r['kind']==by[r['id']]['kind'],'changed application kind')
            demand([(c['label'],c['line'],c['sha256']) for c in r['consumers']]==[(c['label'],c['line'],c['sha256']) for c in by[r['id']]['consumers']],'changed consumer binding')
    return {'records':25,'obligations':225,'filePinOccurrences':pins,'labelBindings':labels,'sourceRecordPins':source_records,'newLabels':len(newlabels),'textReferences':len(refs),'checkedRepositoryFiles':sorted(cache),'scope':'Structural pins, metadata, and binding coverage only; no reviewer acceptance or mathematical proof verdict.'}
def controls(data,repo):
    cases={}
    def reject(name,mutate):
        trial=copy.deepcopy(data);mutate(trial)
        try:validate(trial,repo)
        except (ValueError,KeyError,TypeError):cases[name]='rejected';return
        raise AssertionError('Negative control was accepted: '+name)
    reject('missing_record',lambda d:d['applications'].pop())
    reject('missing_obligation',lambda d:d['applications'][0]['obligations'].pop('required_inputs'))
    reject('absolute_path',lambda d:d['text'].__setitem__('path','C:/private/addition.tex'))
    reject('stale_text_hash',lambda d:d['text'].__setitem__('sha256','0'*64))
    reject('stale_consumer_line',lambda d:d['applications'][0]['consumers'][0].__setitem__('line',1))
    reject('stale_source_record',lambda d:d['externalSources']['silverman']['sourceCatalog'].__setitem__('recordSha256','0'*64))
    reject('changed_external_pin',lambda d:d['externalSources']['silverman']['files'][0].__setitem__('sha256','0'*64))
    return cases
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--inventory',type=Path,default=HERE/'APPLICATIONS.json');ap.add_argument('--author',type=Path,default=HERE/'AUTHOR-APPLICATIONS.json');ap.add_argument('--self-test',action='store_true');ap.add_argument('--report',type=Path);a=ap.parse_args()
    d=json.loads(a.inventory.read_text());r=validate(d,a.repo,a.author if a.author.is_file() else None)
    r.update(status='passed',inventorySha256=sha(a.inventory))
    if a.self_test:r['negativeControls']=controls(d,a.repo)
    if a.report:a.report.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))
