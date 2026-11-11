"""Bounded, exact retained-ideal elimination search. No theorem oracle.

For each constant pivot x=q, substitute in affected rows and seek quadratic
remainders by linear elimination of high-degree monomials using multiples of
unaffected rows. Closure is bounded, so failure is not an impossibility result.
"""
from search import *
from collections import defaultdict, deque
import itertools, time

LIMIT = int(sys.argv[1]) if len(sys.argv)>1 else 1200
MAX_STEPS = 10000

def divmon(a,b):
    s,m=a;t,n=b
    if s<t:return None
    z=list(m)
    for v in n:
        if v not in z:return None
        z.remove(v)
    return s-t,tuple(z)

def high(p):return {k:v for k,v in p.items() if len(k[1])>2}

def multiples(targets,excluded):
    index=defaultdict(list)
    for r,p in c.rows.items():
        if r in excluded:continue
        for k in p:
            if len(k[1])==2:index[k].append(r)
    seen=set();generated={};todo=deque(k for p in targets for k in high(p))
    while todo:
        k=todo.popleft()
        if k in seen:continue
        seen.add(k)
        s,m=k
        for pair in set(itertools.combinations(m,2)):
            for sp in range(s+1):
                d=sp,pair
                if d not in index:continue
                quotient=divmon(k,d)
                for r in index[d]:
                    key=r,quotient
                    if key in generated:continue
                    p=C.multiply(c.rows[r],{quotient:F(1)})
                    generated[key]=p
                    todo.extend(high(p))
                    if len(generated)>=LIMIT:return generated,False
    return generated,True

def solve(targets,excluded):
    gens,complete=multiples(targets,excluded)
    # Only high-degree vectors enter the linear algebra; combination records
    # allow reconstruction and exact checking of every lower-degree term.
    basis={}
    for key,poly in gens.items():
        p=high(poly);trace={key:F(1)};steps=0
        while p:
            k=max(p,key=lambda k:(len(k[1]),k))
            if k not in basis:
                a=p[k];basis[k]=({j:v/a for j,v in p.items()}, {j:v/a for j,v in trace.items()});break
            q,tr=basis[k];a=-p[k]
            for dst,src in [(p,q),(trace,tr)]:
                for j,v in src.items():
                    dst[j]=dst.get(j,F(0))+a*v
                    if not dst[j]:del dst[j]
            steps+=1
            if len(p)+len(trace)>MAX_STEPS or steps>MAX_STEPS:return None,complete,len(gens)
    results=[]
    for target in targets:
        p=high(target);trace={}
        while p:
            k=max(p,key=lambda k:(len(k[1]),k))
            if k not in basis:return None,complete,len(gens)
            q,tr=basis[k];a=-p[k]
            for dst,src in [(p,q),(trace,tr)]:
                for j,v in src.items():
                    dst[j]=dst.get(j,F(0))+a*v
                    if not dst[j]:del dst[j]
        result=target.copy();factors={}
        for (r,k),v in trace.items():
            result=C.add(result,gens[r,k],v)
            factors[r]=C.add(factors.get(r,{}),{k:v})
        assert C.degree(result)<=2
        results.append((result,factors))
    return results,complete,len(gens)

def run():
    start=time.time();attempts=[];operations=[]
    for v in sorted(c.coordinates,reverse=True):
        if v in c.protected:continue
        excluded=c.incidence[v]
        for rid in sorted(excluded):
            pivot=c.pivot_replacement(v,rid)
            if not pivot:continue
            a,q=pivot
            others=sorted(excluded-{rid})
            targets=[C.substitute(c.rows[r],v,q) for r in others]
            result,complete,n=solve(targets,excluded)
            attempts.append({'coordinate':v,'pivot':rid,'multiples':n,'closureComplete':complete,'success':result is not None})
            if result is not None:
                op={'coordinate':v,'name':c.coordinates[v]['name'],'pivot':rid,'replacement':C.terms(q),'changes':[]}
                for r,(p,tr) in zip(others,result):
                    op['changes'].append({'row':r,'result':C.terms(p),'multiples':[{'row':s,'factor':C.terms(t)} for s,t in tr.items() if t]})
                    c.replace_row(r,p)
                c.replace_row(rid,{})
                del c.rows[rid];del c.coordinates[v];c.incidence.pop(v,None)
                operations.append(op)
                print('ELIMINATED',v,op['name'],len(c.coordinates),flush=True)
                break
        if v%20==0: print('coordinate',v,'attempts',len(attempts),'elapsed',round(time.time()-start,1),flush=True)
    cert={'baselineSha256':C.digest(BASE/'baseline498.json'),'operations':operations,'counts':{'coordinates':len(c.coordinates),'residuals':len(c.rows),'degree':max(map(C.degree,c.rows.values()))}}
    (OUT/'macaulay-certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    (OUT/'macaulay-candidate-ir.json').write_text(json.dumps(c.output(),indent=2)+'\n')
    (OUT/'macaulay-search-report.json').write_text(json.dumps({'limit':LIMIT,'attempts':attempts,'seconds':time.time()-start},indent=2)+'\n')
    print(cert['counts'],flush=True)

if __name__=='__main__':run()

