"""Canonical serialization for the original numeric degree-eight polynomial."""
from pathlib import Path
import gzip
import hashlib
import io
import json

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode('ascii')

def sha(data):
    return hashlib.sha256(data).hexdigest()

def compress(data):
    output=io.BytesIO()
    with gzip.GzipFile(filename='',fileobj=output,mode='wb',mtime=0,compresslevel=9) as stream:
        stream.write(data)
    return output.getvalue()

def write_json(path,value):
    Path(path).write_bytes(canonical(value)+b'\n')

def read_rows(path):
    data=Path(path).read_bytes()
    if str(path).endswith('.gz'):data=gzip.decompress(data)
    values=[json.loads(line) for line in data.splitlines()]
    return values[0],values[1:]

def row_bytes(rows):
    return b''.join(canonical(row)+b'\n' for row in rows)

def write_rows(path,header,rows):
    Path(path).write_bytes(compress(canonical(header)+b'\n'+row_bytes(rows)))

def expansion_bytes(poly):
    return (b'# Exact expanded integer polynomial. Variable0 is free X; other indices are rational witnesses.\n'+
            ''.join(str(c)+(' '+' '.join(map(str,m)) if m else '')+'\n' for m,c in sorted(poly.items())).encode('ascii'))

def read_expansion(path):
    data=gzip.decompress(Path(path).read_bytes());out={}
    for line in data.splitlines():
        if not line or line.startswith(b'#'):continue
        c,*m=map(int,line.split());m=tuple(m)
        assert c and m==tuple(sorted(m)) and m not in out
        out[m]=c
    return out
