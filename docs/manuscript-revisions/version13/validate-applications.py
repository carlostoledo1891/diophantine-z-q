"""Check source bytes, application coverage and consumers, not mathematics."""
from pathlib import Path, PurePosixPath
from fractions import Fraction
import argparse, copy, hashlib, json, re, shutil, tempfile

PUBLIC='docs/manuscript-revisions/version13'
OBLIGATIONS={'required_inputs','constructed_inputs','domain_and_index_coverage',
 'transition_maps_and_scalars','identity_of_consumed_object','exceptional_cases',
 'affected_downstream_claims','source_version_and_conventions','validation_and_acceptance_scope'}
COMPONENTS={'one-correction','deterministic-correction','scaled-biquadratic','H-domain',
            'preparation-zero','normalized-pole','anchor-rescaling'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def oh(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def need(ok,msg):
    if not ok:raise ValueError(msg)

def validate(data,repo,contract):
    repo=repo.resolve();cache={};count={'filePins':0,'spans':0,'labels':0}
    need(data.get('schema')=='portable-application-inventory-v2','schema')
    need(data['status'].startswith('Author-only'),'inventory must not assert acceptance')
    ids=[r['id'] for r in data['applications']]
    need(ids==contract['applicationIds']==data['applicationIds'],'application coverage')
    need(len(ids)==len(set(ids)),'duplicate application')
    def pin(d):
        rel=d['path'];p=PurePosixPath(rel)
        need(isinstance(rel,str) and not p.is_absolute() and ':' not in rel and '\\' not in rel and '..' not in p.parts,'nonportable path '+str(rel))
        full=(repo/rel).resolve();need(full.is_relative_to(repo),'path escape')
        need(full.is_file(),'missing source '+rel)
        if rel not in cache:cache[rel]=(sha(full),full.read_bytes())
        h,raw=cache[rel];need(d.get('sha256')==h,'changed source '+rel);count['filePins']+=1
        if 'start_line' in d:
            lines=raw.decode('utf-8').splitlines(keepends=True);a=d['start_line'];b=d['end_line']
            need(isinstance(a,int) and isinstance(b,int) and 1<=a<=b<=len(lines),'span range '+rel)
            span=hashlib.sha256(''.join(lines[a-1:b]).encode()).hexdigest()
            need(span==d['sha256_raw_utf8_span'],'changed span '+rel);count['spans']+=1
        if 'label' in d:
            ls=raw.decode('utf-8').splitlines();i=d['line']
            need(1<=i<=len(ls) and '\\label{'+d['label']+'}' in ls[i-1],'changed label '+d['label']);count['labels']+=1
        if 'lineCount' in d:need(len(raw.decode('utf-8').splitlines())==d['lineCount'],'line count')
        if 'recordId' in d:
            rows=json.loads(raw);matches=[r for r in rows if r['id']==d['recordId']]
            need(len(matches)==1 and oh(matches[0])==d['recordSha256'],'changed source record')
        return raw
    def walk(o):
        if isinstance(o,list):
            for x in o:walk(x)
        elif isinstance(o,dict):
            if 'path' in o:pin(o)
            for x in o.values():walk(x)
    walk(data)
    old=json.loads(pin(data['inheritedInventory']));oldrows={r['id']:r for r in old['applications']}
    catalog={r['id']:r for r in json.loads(pin(data['existingSourceCatalog']))}
    for key,e in data['externalSources'].items():
        c=catalog[key]
        for k in ('bibliography','urls','version_notes','source_status'):
            need(e[k]==c.get(k,[] if k=='urls' else ''),'external source metadata '+key+'/'+k)
        files=[{'sourceFilename':PurePosixPath(f['workspace_relative_path'].replace('\\','/')).name,'sha256':f['sha256'],'bytes':f['bytes']} for f in c['files']]
        need(e['files']==files,'external byte/version metadata')
    for r in data['applications']:
        need(set(r['obligations'])==OBLIGATIONS,'missing obligation '+r['id'])
        need(all(isinstance(x,str) and len(x.strip())>20 for x in r['obligations'].values()),'empty obligation '+r['id'])
        need(r['source']['inheritedPassages'] and r['source']['newDerivation'],'missing application source '+r['id'])
        need(r['consumers'],'missing consumers '+r['id'])
        got=[[c['start_line'],c['end_line']] for c in r['consumers']]
        need(got==contract['consumerSpans'][r['id']],'missing/changed consumer '+r['id'])
        der=r['source']['newDerivation'];need([der['start_line'],der['end_line']]==contract['derivationSpans'][r['id']],'changed derivation binding')
        need(all(c['path']==data['text']['path'] for c in r['consumers']),'wrong consumer document')
        need(r['acceptanceStatus']=='author_only_pending_separate_version13_acceptance','invented acceptance')
        for p in r['source']['priorApplications']:
            need(p['id'] in oldrows and oh(oldrows[p['id']])==p['recordSha256'],'stale prior application')
            need(p['source']==oldrows[p['id']]['source'],'altered inherited locator or qualification')
    need(data['newObligationCoverage']==contract['coverage'],'changed obligation coverage')
    imap=json.loads(pin(data['integrationMap']));rows=json.loads(pin(data['componentRows']))
    walk(imap);walk(rows)
    need(imap['component_row_bindings']==data['componentRows'],'map/component mismatch')
    need(set(data['newObligationCoverage'])=={o['id'] for o in imap['new_application_obligations']},'new substantive obligation missing')
    for v in data['newObligationCoverage'].values():need(v and set(v)<=set(ids),'obligation refers to absent application')
    need({c['id'] for c in rows['components']}==COMPONENTS,'component coverage')
    changed=0
    for c in rows['components']:
        a=json.loads(pin(c['source']));b=json.loads(pin(c['target']))
        x={r['id']:r for r in a['residuals']};y={r['id']:r for r in b['residuals']}
        dif={i for i in x.keys()|y.keys() if x.get(i)!=y.get(i)}
        need(dif=={r['id'] for r in c['changed_residuals']},'incomplete changed residuals '+c['id'])
        changed+=len(dif)
        for r in c['changed_residuals']:
            need(r['old']==x.get(r['id']) and r['new']==y.get(r['id']),'changed residual object')
            for side in ('old','new'):
                need(r[side+'_sha256']==(oh(r[side]) if r[side] is not None else None),'changed object hash')
        same=sorted(i for i in x.keys()&y.keys() if x[i]==y[i])
        need(same==c['unchanged_residual_ids'],'outside row coverage')
        need(oh([x[i] for i in same])==c['unchanged_residuals_sha256'],'outside row hash')
        ca={r['id']:r for r in a['coordinates']};cb={r['id']:r for r in b['coordinates']}
        need({i for i in ca.keys()|cb.keys() if ca.get(i)!=cb.get(i)}=={r['id'] for r in c['changed_coordinates']},'coordinate coverage')
        for r in c['changed_coordinates']:need(r['old']==ca.get(r['id']) and r['new']==cb.get(r['id']),'coordinate object')
        for inc in c['coordinate_incidence']:
            i=inc['coordinate']
            for side,obj in [('old',x),('new',y)]:
                got=[j for j,r in obj.items() if any(i in t['monomial'] for t in r['terms'])]
                need(inc[side+'_residuals']==got,'missing component consumer')
    text=pin(data['text']).decode();base=pin(data['baselineManuscript']).decode()
    newlabels=re.findall(r'\\label\{([^}]+)\}',text);oldlabels=set(re.findall(r'\\label\{([^}]+)\}',base))
    need(len(newlabels)==len(set(newlabels)) and not set(newlabels)&oldlabels,'duplicate label')
    refs=set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',text))
    need(refs<=oldlabels|set(newlabels),'unresolved reference')
    need(refs-set(newlabels)==set(data['explicitInheritedReferences']),'inherited explicit-reference coverage')
    need(refs-set(newlabels)<={x['label'] for x in data['compatibilityInventory']},'missing compatibility reference')
    # The public artifact manifest checks final coordinates/counts independently
    # from the older component indices. This does not replace SOS verification.
    ar=json.loads(pin(data['finalArtifacts']['manifest']))
    need(ar['statistics']==data['finalArtifacts']['statistics'],'artifact statistics mismatch')
    finalfiles={PurePosixPath(f['path']).name:f for f in data['finalArtifacts']['files']}
    need(set(ar['files'])==set(finalfiles),'artifact file coverage')
    for n,h in ar['files'].items():need(finalfiles[n]['sha256']==h,'artifact file hash')
    symbolic=json.loads(pin(finalfiles['candidate394-ir.json']));ordinary=json.loads(pin(finalfiles['candidate411-ir.json']))
    need(len(symbolic['coordinates'])==394 and len(symbolic['residuals'])==364,'symbolic dimensions')
    need(len(ordinary['coordinates'])==411 and len(ordinary['residuals'])==381,'ordinary dimensions')
    prod=ar['constantLift']['extraProductGate'];need(prod['sourceCoordinate']==718 and prod['factors']==[717,549],'ordinary gate factors')
    need(any(c['id']==718 and c['name']==prod['name'] for c in ordinary['coordinates']),'ordinary product coordinate')
    sy={r['id']:r for r in symbolic['residuals']};ordrows={r['id']:r for r in ordinary['residuals']}
    for i,r in sy.items():
        expected=copy.deepcopy(r)
        for t in expected['terms']:
            if t.get('sPower',0):
                need(r['name']=='anchor.translatedEquation' and t['sPower']==1 and t['monomial']==[57,549] and t['coefficient']=='-4','unexpected symbolic C consumer')
                t['sPower']=0;t['monomial']=[57,718]
        # Terms are canonically sorted after the one changed anchor monomial.
        expected['terms'].sort(key=lambda t:(t.get('sPower',0),t['monomial']))
        actual=copy.deepcopy(ordrows[i]);actual['terms'].sort(key=lambda t:(t.get('sPower',0),t['monomial']))
        need(expected==actual,'ordinary outside-row transport')
    def terms(r):return {tuple(t['monomial']):Fraction(t['coefficient']) for t in r['terms']}
    added=[r for i,r in ordrows.items() if i not in sy]
    need(len(added)==17,'ordinary extra-row coverage')
    expected_terms=[{():-3**1024,(702,):1}]+[{(i-1,i-1):-1,(i,):1} for i in range(703,718)]+[{(549,717):-1,(718,):1}]
    remaining=[terms(r) for r in added]
    for expected in expected_terms:
        need(expected in remaining,'missing/changed constant chain or product gate');remaining.remove(expected)
    need(not remaining and all(t.get('sPower',0)==0 and len(t['monomial'])<=2 for r in ordinary['residuals'] for t in r['terms']),'ordinary row degree or constant-symbol leak')
    return dict(status='passed',applications=len(ids),obligations=len(ids)*len(OBLIGATIONS),
                componentCount=len(rows['components']),changedResiduals=changed,
                compatibilityBindings=len(data['compatibilityInventory']),**count,
                checkedFiles=sorted(cache),scope='Structural source, metadata, component-object and consumer checks only. No mathematical or manuscript-acceptance verdict.')

def controls(data,repo,contract):
    outcomes={}
    def reject(name,edit):
        t=copy.deepcopy(data);edit(t)
        try:validate(t,repo,contract)
        except (ValueError,KeyError,TypeError):outcomes[name]='rejected';return
        raise AssertionError('Negative control accepted: '+name)
    reject('missing_application',lambda d:d['applications'].pop())
    reject('missing_obligation',lambda d:d['applications'][0]['obligations'].pop('required_inputs'))
    reject('missing_one_of_multiple_consumers',lambda d:d['applications'][0]['consumers'].pop())
    reject('changed_source_pin',lambda d:d['applications'][0]['source']['inheritedPassages'][0].__setitem__('sha256','0'*64))
    reject('absolute_path',lambda d:d['text'].__setitem__('path','C:/private/addition.tex'))
    reject('altered_external_version',lambda d:d['externalSources']['silverman'].__setitem__('version_notes','unreviewed source replacement'))
    reject('omitted_new_substantive_use',lambda d:d['newObligationCoverage'].pop('ordinary-C-tau'))
    reject('invented_acceptance',lambda d:d['applications'][0].__setitem__('acceptanceStatus','independently accepted'))
    # Real filesystem controls run on a temporary relocated copy, never on the
    # frozen source or the supplied installation root.
    with tempfile.TemporaryDirectory(prefix='v13-inventory-negative-') as temp:
        copyroot=Path(temp)/'repo';shutil.copytree(repo,copyroot)
        target=copyroot/data['text']['path'];old=target.read_bytes();target.unlink()
        try:validate(data,copyroot,contract)
        except ValueError:outcomes['missing_source_file']='rejected'
        else:raise AssertionError('missing source file accepted')
        target.write_bytes(old+b'\n% changed source negative control\n')
        try:validate(data,copyroot,contract)
        except ValueError:outcomes['changed_source_file']='rejected'
        else:raise AssertionError('changed source file accepted')
    return outcomes

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True,type=Path)
    ap.add_argument('--inventory',type=Path);ap.add_argument('--self-test',action='store_true');ap.add_argument('--report',type=Path)
    a=ap.parse_args();p=a.inventory or a.repo/PUBLIC/'APPLICATIONS.json'
    data=json.loads(p.read_text(encoding='utf-8'));contract=json.loads((a.repo/PUBLIC/'validation-schema.json').read_text(encoding='utf-8'))
    result=validate(data,a.repo,contract);result['inventorySha256']=sha(p)
    if a.self_test:result['negativeControls']=controls(data,a.repo,contract)
    if a.report:a.report.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
