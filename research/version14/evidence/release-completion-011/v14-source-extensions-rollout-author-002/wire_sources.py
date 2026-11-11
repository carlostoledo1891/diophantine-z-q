"""Wire frozen source snapshots; never create or select a review receipt."""
import argparse, copy, datetime, hashlib, json, pathlib
HERE=pathlib.Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def time(s):
    t=datetime.datetime.fromisoformat(s.replace('Z','+00:00'))
    if t.tzinfo is None:raise ValueError('timezone required')
    return t
def wire(dossier, entries, repository):
    def read(pin):
        path=(repository/pin['path']).resolve()
        if not path.is_relative_to(repository.resolve()):raise ValueError('path escape')
        raw=path.read_bytes()
        if sha(raw)!=pin['sha256']:raise ValueError('changed frozen source')
        return json.loads(raw)
    if not entries:raise ValueError('at least one independently frozen supplement required')
    if 'source_extensions' in dossier:raise ValueError('refuse replacement of existing extension')
    original_pin=entries[0][0]['original_initial']
    if dossier['initial']!=original_pin:raise ValueError('original initial pin differs from installation mapping')
    original=read(original_pin);sources=list(original['sources']);ids={u['id'] for u in original['uses']};extensions=[]
    for spec,comparison in entries:
        if spec['original_initial']!=original_pin:raise ValueError('supplements bind different original initials')
        sub=read(spec['supplemental_initial']);read(spec['supplemental_passages']);freeze=read(spec['freeze'])
        if sub['sources']!=spec['sources']:raise ValueError('supplement source scope changed')
        if {p['path'] for p in sources}&{p['path'] for p in sub['sources']}:raise ValueError('overlapping source extension')
        newids=[u['id'] for u in sub['uses']]
        if len(set(newids))!=len(newids) or ids&set(newids):raise ValueError('duplicate supplemental use')
        if comparison['initial_sha256']!=spec['supplemental_initial']['sha256'] or comparison['initial_passages_sha256']!=spec['supplemental_passages']['sha256']:raise ValueError('comparison targets wrong supplement')
        recon=copy.deepcopy(comparison['reconstruction'])
        for key in ('frozen_at','method','prior_exposure','limitations'):
            if recon[key]!=freeze[key]:raise ValueError('frozen reconstruction attestation changed')
        if time(recon['frozen_at'])>=time(recon['compared_at']):raise ValueError('comparison not after freeze')
        if not isinstance(recon['run_id'],str) or not recon['run_id']:raise ValueError('actual reviewer run required')
        extensions.append(dict(schema='protocol-source-extension/v1',original_initial=original_pin,sources=sub['sources'],initial=spec['supplemental_initial'],initial_passages=spec['supplemental_passages'],reconstruction=recon))
        sources.extend(sub['sources']);ids.update(newids)
    if sources!=dossier['sources']:raise ValueError('not exact original plus supplemental source union')
    result=copy.deepcopy(dossier);result['source_extensions']=extensions
    return result
def main():
    p=argparse.ArgumentParser();p.add_argument('repository',type=pathlib.Path);p.add_argument('dossier',type=pathlib.Path);p.add_argument('output',type=pathlib.Path)
    p.add_argument('--extension',nargs=2,action='append',required=True,metavar=('SPEC','COMPARISON'));a=p.parse_args()
    entries=[(json.loads(pathlib.Path(s).read_bytes()),json.loads(pathlib.Path(c).read_bytes())) for s,c in a.extension]
    result=wire(json.loads(a.dossier.read_bytes()),entries,a.repository)
    with a.output.open('x',encoding='utf8',newline='\n') as f:json.dump(result,f,indent=2);f.write('\n')
if __name__=='__main__':main()
