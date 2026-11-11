"""Exclude external page extracts; preserve original candidate and all old pins."""
from pathlib import Path
from collections import deque
import hashlib,json,re
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2];OLD=OUT.parent/'handoff-annex-author'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(n,o):(OUT/n).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n',encoding='utf-8')
manifest=json.loads((OLD/'SELECTION.json').read_bytes());sources=json.loads((OLD/'CONTENT-SOURCES.json').read_bytes());mapping=json.loads((OLD/'SOURCE-MAP.json').read_bytes())
assert sha(OLD/'SELECTION.json')=='327746832af51572672d1fc6b62fab8ec2a5ee1f100c9088e0680690862b3522'
assert sha(OLD/'z-in-q-version14-research-annex.zip')=='da7f16019591a37c22c38e5c7567e4f7cbf3f900a0f34f638a5c247196f35d3e'
extracts={
 'work/quartic-under300-20261107/01-elimination/review-positive365/VOIGHT-EXTRACT.txt':('224','243'),
 'work/quartic-under300-20261107/11-anchor-next/voight-223-225.txt':('223-225','242-244'),
}
excluded_hashes={h for h,n in sources.items() if n in extracts};assert len(excluded_hashes)==2
source_tokens=set()
for h in excluded_hashes:
    tokens=re.findall(r'\w+', (ROOT/sources[h]).read_text(encoding='utf-8').lower())
    source_tokens.update(tuple(tokens[i:i+16]) for i in range(max(0,len(tokens)-15)))
screen=[];new_exclusions=[];unavailable_hashes=set()
for h,n in sorted(sources.items()):
    p=ROOT/n
    if not p.is_file() or sha(p)!=h:
        unavailable_hashes.add(h);screen.append({'sha256':h,'source':n,'status':'original pin now unavailable; excluded without refresh'});continue
    b=p.read_bytes();t=b.decode('utf-8',errors='replace');markers=[]
    if re.search(r'(?im)^\s*(PDF (?:index|page)|\d+\s+CHAPTER\s+\d|CHAPTER\s+\d\.)',t):markers.append('external-PDF-page/header shape')
    if re.search(r'(?im)^.{0,25}(?:verbatim|extracted (?:text|pages?)|source (?:excerpt|extract)|copyright|all rights reserved).{0,60}$',t):markers.append('source-extraction/provenance phrase')
    if re.search(r'(?im)^\s*(?:©|Copyright|Springer-Verlag|Annals of Mathematics|Acta Arithmetica).{0,100}$',t):markers.append('publication-imprint phrase')
    overlap=0;longest=0;streak=0
    if any(x in t.lower() for x in ['voight','quaternion','global field','quadratic form','isotropic']):
        q=deque(maxlen=16)
        for word in re.finditer(r'\w+',t.lower()):
            q.append(word[0])
            if len(q)==16 and tuple(q) in source_tokens:overlap+=1;streak+=1;longest=max(longest,streak+15)
            else:streak=0
    screen.append({'sha256':h,'source':n,'status':'external extract excluded' if h in excluded_hashes else 'retained exact prior bytes','markers':markers,'matching_16_word_windows':overlap,'longest_contiguous_matching_words':longest})
for r in manifest['files']:
    if r['sha256'] in excluded_hashes:
        n=sources[r['sha256']];pages,pdf_indices=extracts[n]
        new_exclusions.append({'path':r['path'],'original_sha256':r['sha256'],'original_bytes':r['bytes'],'source_workspace_path':n,'category':r['category'],'disposition':'external_source_page_extract','reason':'Excluded from redistribution: extracted external book pages, not original project research. Original candidate remains preserved for audit; no extracted text is reproduced in this record.',
         'source_identification':{'title':'Quaternion algebras','author':'John Voight','version':'corrected published online edition v1.0.7u, as identified in the original author/reviewer records','url':'https://jvoight.github.io/quat-book.pdf','pdf_sha256':'a9316b834dbd500c52cd3a981c3205c9f4145b217042b213d23f696aee84b0f0','printed_pages':pages,'zero_based_pdf_page_indices':pdf_indices,'consumed_theorem':'Theorem14.6.9, Hasse-Minkowski, printed page224'}})
    elif r['sha256'] in unavailable_hashes:
        new_exclusions.append({'path':r['path'],'original_sha256':r['sha256'],'original_bytes':r['bytes'],'source_workspace_path':sources[r['sha256']],'category':r['category'],'disposition':'unavailable_original_pin_since_r1','reason':'Original pin unavailable during successor preparation; no changed content substituted.'})
remove=excluded_hashes|unavailable_hashes
manifest['files']=[r for r in manifest['files'] if r['sha256'] not in remove]
manifest['unavailable']+=new_exclusions
manifest['scope']+=' Successor R2 excludes the two external Voight page extracts found by independent selection review. It preserves their hashes and source locators as metadata only; all other selected content is byte-identical to the first candidate.'
sources={h:n for h,n in sources.items() if h not in remove};mapping=[r for r in mapping if r['sha256'] not in remove]
dump('SELECTION.json',manifest);dump('CONTENT-SOURCES.json',sources);dump('SOURCE-MAP.json',mapping);dump('EXCLUSIONS.json',manifest['unavailable'])
dump('SOURCE-EXTRACTION-SCREEN.json',{'method':'Sequential exact-content identity check; all selected distinct contents scanned for PDF page headers, extraction/provenance phrases and publication imprints;16-word overlap with both excluded Voight page extracts checks for renamed or embedded copies. Only metadata/results retained here, no page text. Marker hits require manual interpretation.','contents':screen,'new_exclusions':new_exclusions})
dump('INPUT-PINS.json',{'predecessor_selection_sha256':sha(OLD/'SELECTION.json'),'predecessor_archive_sha256':sha(OLD/'z-in-q-version14-research-annex.zip'),'predecessor_source_map_sha256':sha(OLD/'SOURCE-MAP.json'),'selection_sha256':sha(OUT/'SELECTION.json'),'content_sources_sha256':sha(OUT/'CONTENT-SOURCES.json'),'r5_manifest_sha256':'e06b81223c6e2cedbcff78cc65cbddf07d1930e75342ecbb147f8abc402d7028'})
print(json.dumps({'logical_files':len(manifest['files']),'unique_contents':len(sources),'new_exclusions':len(new_exclusions),'retained_marker_or_overlap_hits':[r for r in screen if r['sha256'] not in remove and (r.get('markers') or r.get('matching_16_word_windows'))]}))
