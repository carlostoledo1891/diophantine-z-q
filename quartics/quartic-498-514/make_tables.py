"""Render complete consecutive-coordinate JSON and text tables from frozen IRs."""
from pathlib import Path
import json
H=Path(__file__).resolve().parent
def main():
 for n in [498,514]:
  ir=json.loads((H/f'candidate{n}-ir.json').read_text());p=json.loads((H/f'polynomial{n}.json').read_text())
  cs=sorted(ir['coordinates'],key=lambda c:c['id']);mp={c['id']:i for i,c in enumerate(cs)}
  table={'format':'integer-quartic-consecutive-coordinates-v1','variables':n,'witnesses':n-1,'degree':4,
    'coordinates':[{'id':i,'sourceId':c['id'],'name':c['name']} for i,c in enumerate(cs)],
    'terms':[dict(t,monomial=[mp[v] for v in t['monomial']]) for t in p['terms']]}
  if n==498:table['fixedParameter']={'name':'C','value':'3^(2^25)','coordinate':False}
  name=f'quartic-{n}-'+('symbolic-coefficients' if n==498 else 'ordinary-coefficients')
  (H/(name+'.json')).write_text(json.dumps(table,indent=2)+'\n', encoding='utf-8', newline='\r\n')
  lines=[f'# Integer quartic in {n} rational variables; x0 is the input.',
    '# Every following non-comment row is coefficient | C exponent | variable indices.',
    '# C = 3^(2^25), a fixed integer, not a variable.' if n==498 else '# C exponent is zero in every row.']
  lines += [f'# x{i} = source coordinate {c["id"]}: {c["name"]}' for i,c in enumerate(cs)]
  lines += [str(t['coefficient'])+' | '+str(t.get('sPower',0))+' | '+','.join(map(str,t['monomial'])) for t in table['terms']]
  (H/(name+'.txt')).write_text('\n'.join(lines)+'\n', encoding='utf-8', newline='\r\n')
if __name__=='__main__':main()
