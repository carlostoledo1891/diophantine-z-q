"""Create an isolated A007/A011 projection. Never edit source packets or live files."""
import argparse, copy, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
P = 'work/source-risk-review-20261107/'
A = ROOT / (P+'a007-a011-current-anchor-001')
B = ROOT / (P+'a007-a011-current-anchor-002')
OLD = ROOT/'work/quartic-v14-combined-20261108-004/candidate/manuscripts/quartic_v14.tex'
MID = ROOT/'work/quartic-v14-combined-20261108-005/candidate/manuscripts/quartic_v14.tex'
EXPECTED = '1f748130c21db66a3eacc679ace1d13c22f86a6add2a383581077c00c7ef499f'
PROOF_PATH = 'research/version14/proofs/character-jacobian-current-v1/CONNECTION.md'
STATEMENTS_PATH = 'research/version14/proofs/character-jacobian-current-v1/CURRENT-SOURCE-STATEMENTS.md'
FIELDS = ['statement','objects','hypotheses','quantifiers','parameter_range','uniformity','constants','normalizations','exceptional_cases','limit_order']
sha = lambda b: hashlib.sha256(b).hexdigest()
enc = lambda x: (json.dumps(x,ensure_ascii=False,indent=2,allow_nan=False)+'\n').encode('utf-8')
canon = lambda x: sha(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode())
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def pin(path, data): return {'side':'head','path':path,'sha256':sha(data)}
def walk(x):
    yield x
    if isinstance(x,dict):
        for v in x.values(): yield from walk(v)
    elif isinstance(x,list):
        for v in x: yield from walk(v)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--target',default='work/quartic-v14-combined-20261108-007/candidate/manuscripts/quartic_v14.tex'); ap.add_argument('--sha256',default=EXPECTED); ap.add_argument('--output',default=str(HERE)); args=ap.parse_args()
    out=Path(args.output).resolve(); target=(ROOT/args.target).resolve(); raw=target.read_bytes(); assert sha(raw)==args.sha256
    old=OLD.read_bytes(); mid=MID.read_bytes(); oldlines=old.splitlines(keepends=True); lines=raw.splitlines(keepends=True)
    assert sha(old)=='ed992fd5876ad89383dc58848bab378045820cf411535dbd6045e3bea0b3a68f'
    assert sha(mid)=='7a848c441ebd7a03c249db66b555f2c0439da79efe10eadedff118247229b551'
    inputs=[]
    def add_input(p,expected=None):
        p=p.resolve(); data=p.read_bytes(); h=sha(data); assert expected is None or h==expected,(p,h,expected)
        row={'path':p.relative_to(ROOT).as_posix(),'sha256':h,'bytes':len(data)}
        if row not in inputs: inputs.append(row)
        return data
    for f in ['APPLICATIONS.json','BOUNDARY-INPUTS.json','RELATED-USES.json','EDGES.json','SOURCE-PINS.json','CONNECTION.md','MANIFEST.json']: add_input(A/f)
    for f in ['ASSERTIONS.json','INDEX.json','SOURCE-TO-APPLICATIONS.json','DELTA.json']: add_input(B/f)
    add_input(B/'MANIFEST.json','26cee5b5ef88478dfae6215e746cb79b75974dffb913e0ed5af60bb39ed4bd92')
    review=ROOT/'work/quartic-v14-prep/independent-source-review/a007-a011-current-review-001'
    add_input(review/'MANIFEST.json','b24ff96dcc7a0acd9b884a6531278e1aa26f9ff8272ba4d540d03760ee74b5a5'); add_input(review/'REVIEW.md')
    for f in [OLD,MID,target]: add_input(f)
    sources=read(A/'SOURCE-PINS.json')
    for s in sources: add_input(ROOT/s['primary']['path'],s['primary']['sha256'])
    pan=ROOT/(P+'pan-calegari-direct-author-001')
    add_input(pan/'MANIFEST.json','2917deeccedb30b6e49a764efbaa51393a95a51f4343c26efe4ce6330a5f2f5f')
    for name in ['SOURCE-APPLICATIONS.json','PAYLOAD-MAP.json','SOURCE-STATUS.md','SOURCES.md']: add_input(pan/name)
    panproof=add_input(pan/'PUBLIC-PROOF.md','995d60ad7b793c17096bbb55476f52104af45a84d634713e3c490fe9bbd6ffda')
    panpath='research/version14/proofs/direct-p5-modularity-v1/PROOF.md'
    assert (target.parents[1]/panpath).read_bytes()==panproof
    add_input(target.parents[1]/panpath)
    panreviews=[]
    for dirname,manifest_hash,review_hash in [
      ('work/quartic-v14-prep/independent-source-review/pan-calegari-direct-review-001','6bb2a75363d2ae010bceb5e76362c12bfd954e4419116240aa9953ab1d3eee93','a16eba4e1f75d190122963134a102491ce6a68885754dd83a64f6137edfac584'),
      (P+'pan-calegari-incorporation-review-compiler-001','3b1afd562e355880a846a45b5a3be44bec2092a4cdcff33ff9d33626e41cf0aa','1ca001b4f5be8e2f74f1f8c77dff729cd18b235fc7f4b7554029754bfab5966b')]:
        add_input(ROOT/dirname/'MANIFEST.json',manifest_hash); add_input(ROOT/dirname/'REVIEW.md',review_hash)
        panreviews.append({'manifest':dirname+'/MANIFEST.json','manifest_sha256':manifest_hash,'review':dirname+'/REVIEW.md','review_sha256':review_hash})
    pancards={x['id']:x for x in walk(read(pan/'SOURCE-APPLICATIONS.json')) if isinstance(x,dict) and x.get('id') in ['DIRECT-FIRST-CALLER','DIRECT-SECOND-CALLER']}
    assert len(pancards)==2
    oldapps=read(A/'APPLICATIONS.json'); apps=copy.deepcopy(oldapps); appmap={a['id']:a for a in apps}
    oldindex=read(B/'INDEX.json'); sourcecalls=read(B/'SOURCE-TO-APPLICATIONS.json'); assertions_raw=read(B/'ASSERTIONS.json')
    proof=add_input(A/'CONNECTION.md','4fd5cbac764d12ce16d943bac23854bd78a42c824473209966e34b6af9280889'); prooflines=proof.splitlines(keepends=True)
    proof_locations={a['id']:next(r['location'] for r in oldindex if r['id']==a['id']+'-PROOF') for a in apps}
    assertions={r['consumer']:r['application_output'] for r in sourcecalls}
    for aid in appmap:
        if aid in assertions: continue
        candidates=[]
        for node in walk(assertions_raw):
            if isinstance(node,dict) and aid in node.values():
                candidates.extend(z for z in walk(node) if isinstance(z,dict) and all(k in z for k in FIELDS))
            if isinstance(node,dict) and aid in node:
                candidates.extend(z for z in walk(node[aid]) if isinstance(z,dict) and all(k in z for k in FIELDS))
        assert candidates,('Missing assertion',aid); assertions[aid]={k:candidates[0][k] for k in FIELDS}
    transport=[]
    def locate(fragment,data):
        assert fragment and data.count(fragment)==1,('nonunique fragment',sha(fragment),data.count(fragment))
        at=data.index(fragment); start=len(data[:at].splitlines())+1; end=start+len(fragment.splitlines())-1
        assert b''.join(data.splitlines(keepends=True)[start-1:end])==fragment
        return start,end
    def move(loc):
        if loc['pin']['path']!='manuscripts/quartic_v14.tex':
            assert loc['pin']['path']==PROOF_PATH and loc['pin']['sha256']==sha(proof)
            assert sha(b''.join(prooflines[loc['start_line']-1:loc['end_line']]))==loc['excerpt_sha256']; return copy.deepcopy(loc)
        assert loc['pin']['sha256']==sha(old)
        fragment=b''.join(oldlines[loc['start_line']-1:loc['end_line']]); assert sha(fragment)==loc['excerpt_sha256']
        m=locate(fragment,mid); n=locate(fragment,raw)
        result={'pin':pin('manuscripts/quartic_v14.tex',raw),'start_line':n[0],'end_line':n[1],'excerpt_sha256':sha(fragment)}
        record={'original':loc,'combined005_lines':list(m),'current':result,'comparison':'exact raw bytes, including line endings'}
        if record not in transport: transport.append(record)
        return result
    occurrences=[]
    for r in oldindex:
        if r['location']['pin']['path']=='manuscripts/quartic_v14.tex':
            occurrences.append({'id':r['id'],'application_ids':r['claim_ids'],'location':move(r['location']),'root_attachment_status':'pending; this is an application occurrence, not a source invocation or a self-edge'})
    # Project only the selected published statements, with their original source pins.
    selected={s['id']:s for s in sources if 'available_statement' in s}
    text=['# Selected published inputs\n','\n','These are project-authored summaries of the pinned published inputs. They are not new proofs or a claim of full-source comparison. The separate application proof derives its outputs from these inputs and its other stated premises.\n','\n']
    source_ranges={}
    for sid,s in selected.items():
        start=len(text)+1
        text.extend(['## '+sid+'\n',s['available_statement']+'\n','Source: '+s['primary']['sha256']+'; '+s['locator']+'.\n','Version and scope: '+s['version']+' '+s['scope']+'\n'])
        if sid=='SHIMURA': text.append('The unconditional clause selected for C4 gives the coefficient-conjugate normalized eigenforms at the same level. C4 does not apply the conditional Euler-product clause.\n')
        source_ranges[sid]=(start,len(text)); text.append('\n')
    sourcebytes=''.join(text).encode('utf-8'); slines=sourcebytes.splitlines(keepends=True)
    source_locations={sid:{'pin':pin(STATEMENTS_PATH,sourcebytes),'start_line':v[0],'end_line':v[1],'excerpt_sha256':sha(b''.join(slines[v[0]-1:v[1]]))} for sid,v in source_ranges.items()}
    contexts={
      'MILNE-LOCAL':('A nonarchimedean local field K and its finite characters and Brauer group.','Continuous finite-order characters; the application specializes to Q_p.','All finite rational primes, including 2.','Local reciprocity convention is retained; inversion does not affect the order-two test.','The character square-root criterion is a derived project result, not the published statement.'),
      'MILNE-BRAUER':('A global field and all its completions.','The local classes satisfy the global invariant-sum compatibility.','The application is K=Q and includes the real place.','Local invariant maps and their sum.','Finite-place equality alone uses the invariant-sum step before global injectivity.'),
      'LI':('A normalized primitive cuspidal eigenform and its coefficient conjugates.','The form has the stated level, weight and nebentypus.','The application uses weight 2 and arbitrary character.','The determinant-normalized slash and the weight-two factor relating the two Fricke conventions.','No individual Fricke eigenvector or algebraicity of its scalar is asserted.'),
      'SHIMURA':('A normalized weight-two eigenform for Gamma1(N) contained in Gamma contained in Gamma0(N).','The stated eigenform hypotheses; the Euler clause additionally requires its separate Fricke or Gamma0 hypothesis.','The same level N and all coefficient embeddings.','The rational quotient, coefficient action and conjugate differential span of Theorem 1.','The unconditional conjugate-form clause must not be confused with the conditional Euler clause.'),
      'EMERTON-CLASSICAL':('The classical Galois representations attached to cuspidal newforms.','The stated cuspidal newform and good-prime hypotheses.','Each coefficient conjugate at coefficient prime 5, weight 2.','Cohomological geometric Frobenius; the Tate arithmetic representation is its dual.','Only section 2.3 classical attachment is imported, not a p-adic local-global conjecture.'),
      'FALTINGS':('The rational Tate module of an abelian variety over a number field.','An abelian variety over a number field; the published correction is retained.','A_f and J1(N) over Q, coefficient prime 5.','Rational Tate module; finite coefficient extension is handled separately in the project proof.','This source call is semisimplicity, not a new full faithfulness or conductor assertion.'),
      'SERRE-TRACE':('Continuous Galois representations and finite-dimensional semisimple representations of an algebra over a characteristic-zero field.','Finite exclusions for density and semisimplicity for trace determination.','The actual finite 5-adic coefficient field and its group algebra.','Use density to compare continuous traces, then the standalone algebra lemma.','Do not import the stronger surrounding Q-rational compatible-system theorem.'),
      'MILNE-H1':('An abelian variety over a field and its Tate module and first etale cohomology.','The coefficient prime differs from the characteristic of the base field.','A_f over Q with coefficient prime 5.','The canonical Galois-equivariant linear dual; no Tate twist.','Conductor equality and level equals conductor remain separate arguments.')}
    source_assertions={}
    for sid,s in selected.items():
        obj,hyp,ran,norm,exc=contexts[sid]
        source_assertions[sid]=dict(zip(FIELDS,[s['available_statement'],obj,hyp,'For every object satisfying the selected published hypotheses.',ran,'Only the stated source scope is imported.','No new effective numerical bound is supplied.',norm,exc,'Establish the published input before applying the separate project derivation.']))
    pubs={
      'MILNE-LOCAL':('Arithmetic Duality Theorems','J. S. Milne','Second edition, 2006'),
      'MILNE-BRAUER':('Arithmetic Duality Theorems','J. S. Milne','Second edition, 2006'),
      'LI':('Newforms and functional equations','W.-C. W. Li','Mathematische Annalen 212 (1975), 285-315'),
      'SHIMURA':('On the factors of the jacobian variety of a modular function field','G. Shimura','Journal of the Mathematical Society of Japan 25 (1973), 523-544'),
      'EMERTON-CLASSICAL':('A local-global compatibility conjecture in the p-adic Langlands programme for GL2/Q','M. Emerton','Pure and Applied Mathematics Quarterly 2 (2006), 279-393'),
      'FALTINGS':('Endlichkeitssatze fur abelsche Varietaten uber Zahlkorpern','G. Faltings','Inventiones Mathematicae 73 (1983), 349-366; correction 75 (1984), 381'),
      'SERRE-TRACE':('Abelian l-adic representations and elliptic curves','J.-P. Serre','Published book, exact pinned edition retained'),
      'MILNE-H1':('Abelian varieties','J. S. Milne','Arithmetic Geometry (1986), original chapter')}
    uses=[]; index=[]; connections=[]
    def make_use(uid,consumer,supplier,assertion,location,role):
        pid=uid+'-P'
        u={'id':uid,'consumer':consumer,'passages':[pid],'assertion':copy.deepcopy(assertion),'classification':'dependency','reason':'Import the selected input at the actual project-proof invocation. The application output and other premises remain separate.','shared_contract_justification':None,'supplier':supplier,'application_id':consumer,'inline_argument':None}
        uses.append(u); index.append({'id':pid,'claim_ids':[consumer],'location':location,'status':'reviewed','reason':'Author-checked exact invocation; new current projection awaits independent adoption review.','use_ids':[uid],'no_imports_reason':None})
        capability='selected-input:'+uid
        connections.append({'use_id':uid,'use_sha256':canon(u),'supplier_passage_role':role,'available_assertion':copy.deepcopy(assertion),'needed_assertion':copy.deepcopy(assertion),'required_capabilities':[capability],'available_capabilities':[capability],'derived_capabilities':[],'connecting_derivation':{'kind':'identification','location':location,'application_id':consumer,'output_assertion':copy.deepcopy(assertion)},'adverse_cases':{'status':'checked','reason':assertion['exceptional_cases'],'evidence':[location]},'consumer_locations':[location]})
    for call in sourcecalls:
        sid=call['source']['id']; s=selected[sid]; title,authors,venue=pubs[sid]
        publication={'title':title,'authors':authors,'venue':venue,'authoritative_version':s['version']+' Original SHA256 '+s['primary']['sha256'],'locator':s['locator'],'corrections':'All original source qualifications and separately pinned correction files are retained in SOURCE-PINS.json.'}
        imported=copy.deepcopy(source_assertions[sid])
        if call['id']=='CURRENT-A011-FRICKE-SPAN-FROM-SHIMURA':
            imported['statement']='Every coefficient conjugate of the normalized weight-two eigenform is a normalized eigenform at the same level, with the corresponding coefficient embedding.'
            imported['hypotheses']='The normalized weight-two eigenform and group hypotheses of the unconditional clause of Theorem 1.'
            imported['exceptional_cases']='No conditional Euler-product clause is invoked in C4, so no Fricke premise is assumed while proving Fricke stability.'
        supplier={'kind':'published_external','application_id':None,'location':source_locations[sid],'statement':imported['statement'],'publication':publication}
        make_use(call['id'],call['consumer'],supplier,imported,move(call['connecting_derivation']),'statement')
    for a in apps:
        for dep in a['dependencies']:
            if dep not in appmap: continue
            supplier={'kind':'internal','application_id':dep,'location':move(proof_locations[dep]),'statement':assertions[dep]['statement'],'publication':None}
            make_use(a['id']+'-FROM-'+dep,a['id'],supplier,assertions[dep],move(proof_locations[a['id']]),'proof')
    # Keep the original comparisons, distinguish their old decision from this new projection.
    for a in apps:
        a['authors']=list(dict.fromkeys(a['authors']+['/root/astra_v14_baseline_theta']))
        a['files']=[pin('manuscripts/quartic_v14.tex',raw),pin(PROOF_PATH,proof),pin(STATEMENTS_PATH,sourcebytes)]
        for name,o in a['obligations'].items():
            o['evidence']=[pin('manuscripts/quartic_v14.tex',raw),pin(PROOF_PATH,proof)]
            o['justification']=o['justification'].replace('Author comparison only; independent acceptance pending.','The original ed992 comparison has separate independent acceptance b24ff96d. Its required and constructed fields are unchanged here; this current projection awaits a new independent adoption decision.')
            if any(d not in appmap for d in a['dependencies']) and name in ['source_hypotheses','consumed_object_identity','downstream_consumption']:
                o['justification']+=' The current FIRST/SECOND caller inferences have separate Pan mathematical and incorporation decisions. Their exact current owner replacement is proposed in OWNER-REPLACEMENTS.json and still requires independent mapping review and merge.'
    boundary_raw=read(A/'BOUNDARY-INPUTS.json'); boundary_changes=[]
    for node in walk(boundary_raw):
        if isinstance(node,dict) and 'pin' in node and 'start_line' in node:
            try: current=move(node); state='exact unchanged bytes'
            except AssertionError:
                fragment=b''.join(oldlines[node['start_line']-1:node['end_line']]); assert sha(fragment)==node['excerpt_sha256']; locate(fragment,mid)
                current=None; state='old premise paragraph changed; accepted direct-caller replacement is proposed separately in OWNER-REPLACEMENTS.json'
            boundary_changes.append({'original':node,'current':current,'status':state})
    # Locate the two actual new premise paragraphs, without treating them as their own proof.
    owner_candidates=[]
    for i,line in enumerate(lines):
        if b't_\\sigma=a_\\sigma/\\beta(\\sigma)' in line or b't_\\sigma=a_\\sigma/b(\\sigma)' in line:
            j=i
            while j<len(lines) and lines[j].strip() and not lines[j].startswith(b'For this final newform') and not lines[j].startswith(b'For the conductor'): j+=1
            lo=max(0,i-1); hi=j; fragment=b''.join(lines[lo:hi])
            owner='QM-FIRST-MODULARITY-APPLICATION' if b'\\beta' in line else 'QM-SECOND-MODULARITY-APPLICATION'
            owner_candidates.append({'owner':owner,'location':{'pin':pin('manuscripts/quartic_v14.tex',raw),'start_line':lo+1,'end_line':hi,'excerpt_sha256':sha(fragment)},'status':'actual current assertion occurrence only; not supplied as its own proof'})
    assert {x['owner'] for x in owner_candidates}=={'QM-FIRST-MODULARITY-APPLICATION','QM-SECOND-MODULARITY-APPLICATION'}
    panlines=panproof.splitlines(keepends=True)
    panloc={'pin':pin(panpath,panproof),'start_line':33,'end_line':37,'excerpt_sha256':sha(b''.join(panlines[32:37]))}
    assert b'## 6.' in panlines[32] and b't_sigma=a_sigma/beta' in panlines[36] and b't_sigma=a_sigma/b(sigma)' in panlines[36]
    owner_replacements=[]
    for row in owner_candidates:
        first=row['owner']=='QM-FIRST-MODULARITY-APPLICATION'; card=pancards['DIRECT-FIRST-CALLER' if first else 'DIRECT-SECOND-CALLER']
        owner_replacements.append({'owner':row['owner'],'accepted_source_card':card,'source_card_origin':str((pan/'SOURCE-APPLICATIONS.json').relative_to(ROOT)).replace('\\','/'),'current_assertion_occurrence':row['location'],'current_immediate_proof':panloc,'reviews':panreviews,'mapping':{'cochain':'t=a/beta' if first else 't=a/b','representation':'The same original r5; finite coefficient enlargement does not replace the representation.','controlled_data':'Keep A, L_prime, beta and the original r_l.' if first else 'Keep A, L_prime, b, chi=b^2 and the original r_l; absorbed delta is distinct from chi.','conductor':'No new conductor bound. The final primitive level and the original 5-to-3 argument retain their separate inputs.'},'status':'Proposed current owner replacement. Mathematical caller inference is separately accepted; this exact graph association and merge are not self-approved.','retained_boundary':'The shared scalar-lemma output and all preceding geometry/full-endomorphism hypotheses remain required. No whole-root attachment is inferred.'})
    related=[]
    for node in walk(read(A/'RELATED-USES.json')):
        if isinstance(node,dict) and 'pin' in node and 'start_line' in node:
            try: current=move(node); state='unchanged; original scope exclusions retained'
            except AssertionError: current=None; state='changed/removed; no automatic adoption or retirement'
            related.append({'original':node,'current':current,'status':state})
    for u,c,idx in zip(uses,connections,index):
        assert c['use_sha256']==canon(u) and c['consumer_locations']==[idx['location']]
        assert set(c['required_capabilities'])<=set(c['available_capabilities']) and c['needed_assertion']==c['available_assertion']==u['assertion']
        assert u['supplier']['statement']==u['assertion']['statement']
        assert set(u['assertion'])==set(FIELDS)
        if u['supplier']['kind']=='internal': assert u['supplier']['application_id'] in appmap[u['consumer']]['dependencies']
    assert len(apps)==6 and len(uses)==14 and len(connections)==14
    assert sum(len(a['obligations']) for a in apps)==54
    for a,old_a in zip(apps,oldapps):
        for k,o in a['obligations'].items(): assert o['required']==old_a['obligations'][k]['required'] and o['constructed']==old_a['obligations'][k]['constructed']

    # The successor changes only the target binding; independently replay its one TeX spelling change.
    import re
    predecessor=ROOT/(P+'a007-a011-current-projection-theta-001')
    add_input(predecessor/'MANIFEST.json','c857f8276d6c56f67ba1a88f635f46542135b1593199c31be73035bbdc1aca3e')
    previous=add_input(ROOT/'work/quartic-v14-combined-20261108-006/candidate/manuscripts/quartic_v14.tex','c6c7abca5e97bb295d775b9fd642bc4444b6650280fe5e0db5ff3ba52fad4b48')
    old_token=bytes([92])+b'C'; new_token=bytes([92])+b'mathbb{C}'
    positions=[m.start() for m in re.finditer(re.escape(old_token)+rb'(?![A-Za-z])',previous)]
    positions=[i for i in positions if previous[:i]+new_token+previous[i+len(old_token):]==raw]
    assert len(positions)==1, '007 is not exactly the authorized one-token spelling change'
    changed_at=positions[0]
    delta={'predecessor_manifest':'c857f8276d6c56f67ba1a88f635f46542135b1593199c31be73035bbdc1aca3e','previous_target_sha256':sha(previous),'current_target_sha256':sha(raw),'byte_offset':changed_at,'line':previous[:changed_at].count(b'\n')+1,'before':old_token.decode(),'after':new_token.decode(),'inverse_replay':raw[:changed_at]+old_token+raw[changed_at+len(new_token):]==previous,'scope':'TeX spelling only; no new Pan mathematical approval or owner merger.'}

    files={
      'INPUTS.json':enc(inputs),'APPLICATIONS.json':enc(apps),'USES.json':enc(uses),'INDEX.json':enc(index),'CONNECTIONS.json':enc(connections),
      'INHERITED-APPLICATIONS.json':(A/'APPLICATIONS.json').read_bytes(),'INHERITED-ASSERTIONS.json':(B/'ASSERTIONS.json').read_bytes(),
      'INHERITED-SOURCE-COMPARISONS.json':(B/'SOURCE-TO-APPLICATIONS.json').read_bytes(),'SOURCE-PINS.json':(A/'SOURCE-PINS.json').read_bytes(),
      'APPLICATION-OCCURRENCES.json':enc(occurrences),'TRANSPORT.json':enc(transport),
      'BOUNDARIES.json':enc({'original':boundary_raw,'transport':boundary_changes,'actual_current_assertions':owner_candidates,'required_owners':['QM-FIRST-MODULARITY-APPLICATION','QM-SECOND-MODULARITY-APPLICATION'],'status':'Current caller mathematics is supplied by the two separately accepted Pan cards. Exact owner replacement and final merge remain proposed, not inferred from the manuscript assertions.'}),
      'OWNER-REPLACEMENTS.json':enc(owner_replacements),
      'ASSERTION-SCOPE.json':enc({'C5':'The accepted C5 assertion stops at the rational quotient, differential span and Euler product. Its broad heading does not enlarge the adopted assertion to the Tate constituent.','C6':'The actual Tate constituent and dual conductor assertion is owned by C6; its accepted corrected span begins at line39 and binds the Emerton/Faltings/Serre imports. Thus no missing C5 source edges are manufactured from its heading.','C4_SHIMURA':'Only the unconditional coefficient-conjugate eigenform clause is imported; the conditional Euler clause is applied later in C5 after C4.'}),
      'RELATED-USES.json':enc({'original':read(A/'RELATED-USES.json'),'transport':related}),
      'ROOT-ATTACHMENTS.json':enc({'status':'pending whole-root association','first_historical_candidate':'ORIGINAL-SIX-CONTACT-HEIGHT','second_historical_candidate':'COMPILER-B108','occurrences':occurrences,'rule':'No self-edges or historical whole-root acceptance are manufactured.'}),
      'SOURCE-MAP.json':enc([{'source':str((A/'CONNECTION.md').relative_to(ROOT)).replace('\\','/'),'path':PROOF_PATH,'sha256':sha(proof),'role':'exact project proof, with original historical status prose retained'},{'source':'CURRENT-SOURCE-STATEMENTS.md','path':STATEMENTS_PATH,'sha256':sha(sourcebytes),'role':'new selected-source summaries, not independent proofs'}]),
      'CURRENT-SOURCE-STATEMENTS.md':sourcebytes,
      'CHECKS.json':enc({'status':'author structural and byte checks passed; no full gate or independent adoption decision','target_sha256':sha(raw),'apps':6,'obligations':54,'external_uses':10,'internal_uses':4,'connections':14,'application_occurrences':len(occurrences),'raw_transport_records':len(transport),'unchanged_required_constructed_pairs':54,'unresolved_incoming_owner_obligations':sum(o['status']=='unresolved' for a in apps for o in a['obligations'].values())}),
      'STATUS.json':enc({'target':str(target.relative_to(ROOT)).replace('\\','/'),'sha256':sha(raw),'status':'author proposal; independent current projection review pending','inherited_scope':'Six conditional arguments, 54 comparisons accepted only at the separately pinned ed992 checkpoint.','current_owner_adoption':'FIRST and SECOND retain separate accepted Pan caller inferences; exact replacement mapping and merge remain proposed.','whole_root_adoption':'pending','global_gate':'not run; external owner replacement and root attachments are explicit merge boundaries','release':'not approved'}),
      'README.md':('''# A007/A011 current projection\n\nThis author proposal preserves six conditional application claims and their 54 required/constructed comparisons. The independent b24ff96d review applies to the original ed992 checkpoint. This new current projection needs a separate adoption review.\n\nThe ten published imports occur at actual calls in the unchanged project proof. Their eight source summaries retain the original PDF/image hashes, printed locators, correction files and scope limits. Four internal imports preserve C1 to C2 to C3 and C4 to C5 to C6. Published input statements are not asserted to prove the whole application output individually. The inherited source comparisons retain the actual derivations and other premises.\n\nAPPLICATION-OCCURRENCES records manuscript conclusions separately from the proof's source calls. ROOT-ATTACHMENTS remains pending because no current whole-root owner is supplied for either first or repeated construction. BOUNDARIES preserves the distinct FIRST and SECOND owners. Their actual current paragraphs are not their own proof. OWNER-REPLACEMENTS binds the separately accepted Pan caller inferences to the two existing owners; that exact mapping still needs independent review and merge. All 54 conditional comparisons retain their original required and constructed fields.\n\nEmerton section 2.3 classical attachment remains active. The argument also retains Faltings semisimplicity, Serre density/trace comparison, Milne duality, and the separate level/conductor premise. Main-text bibliography removal does not retire these sources. The two different cochains, controlled fields and degree bounds remain distinct. RELATED-USES does not absorb the separate diamond-action, Gamma0, or exact-level arguments.\n\nThe generator accepts a target path/hash and writes only a fresh output packet. Every unchanged location is found by a unique raw-byte match through combined005. A new target is not accepted merely because its hash was predicted. Source PDFs/images are local-only and are not copied to proposed-repository. No live registry, manuscript or profile is changed.\n''').encode(),
      'proposed-repository/'+PROOF_PATH:proof,'proposed-repository/'+STATEMENTS_PATH:sourcebytes}

    stable=['USES.json','INDEX.json','CONNECTIONS.json','INHERITED-APPLICATIONS.json','INHERITED-ASSERTIONS.json','INHERITED-SOURCE-COMPARISONS.json','SOURCE-PINS.json','CURRENT-SOURCE-STATEMENTS.md','SOURCE-MAP.json','ASSERTION-SCOPE.json','README.md','proposed-repository/'+PROOF_PATH,'proposed-repository/'+STATEMENTS_PATH]
    rebound=['APPLICATIONS.json','APPLICATION-OCCURRENCES.json','TRANSPORT.json','BOUNDARIES.json','RELATED-USES.json','ROOT-ATTACHMENTS.json','OWNER-REPLACEMENTS.json','STATUS.json','CHECKS.json']
    for name in stable:
        data=add_input(predecessor/name); assert files[name]==data,('Unexpected source or proof change',name)
    for name in rebound:
        data=add_input(predecessor/name)
        expected=data.replace(sha(previous).encode(),sha(raw).encode()).replace(b'quartic-v14-combined-20261108-006/candidate/manuscripts/quartic_v14.tex',b'quartic-v14-combined-20261108-007/candidate/manuscripts/quartic_v14.tex')
        assert files[name]==expected,('Change exceeds exact target binding',name)
    delta['byte_identical_files']=stable; delta['target_binding_only_files']=rebound
    files['TRANSPORT-DELTA.json']=enc(delta)
    files['INPUTS.json']=enc(inputs)

    out.mkdir(parents=True,exist_ok=True)
    assert not any(p.name!='prepare.py' for p in out.iterdir()),'Output is not fresh; choose a new --output'
    if out!=HERE: files['prepare.py']=Path(__file__).read_bytes()
    for name,data in files.items():
        p=out/name; p.parent.mkdir(parents=True,exist_ok=True)
        with p.open('xb') as f: f.write(data)
    members=[{'path':p.relative_to(out).as_posix(),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(out.rglob('*')) if p.is_file()]
    manifest={'schema':'bounded-source-projection/v1','status':'author proposal; independent adoption pending','target_sha256':sha(raw),'files':members}
    with (out/'MANIFEST.json').open('xb') as f: f.write(enc(manifest))
    print(json.dumps({'manifest':sha((out/'MANIFEST.json').read_bytes()),'members':len(members),'checks':json.loads(files['CHECKS.json'])}))
if __name__=='__main__': main()
