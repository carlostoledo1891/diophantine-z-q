from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import hashlib,json,sys

OUT=Path(__file__).resolve().parent
URLS=[
('bl-publisher','https://www.ams.org/journals/tran/2019-371-08/S0002-9947-2018-07514-6/home.html'),
('bl-final','https://www.ams.org/journals/tran/2019-371-08/S0002-9947-2018-07514-6/S0002-9947-2018-07514-6.pdf'),
('bhb-publisher','https://www.degruyterbrill.com/document/doi/10.1515/forum-2020-0074/html'),
('bhb-final','https://www.degruyterbrill.com/document/doi/10.1515/forum-2020-0074/pdf'),
('browning-publications','https://tdbrowning.github.io/pubs.html'),
('bhb-oxford-record','https://ora.ox.ac.uk/objects/uuid:029537a5-f3a1-4ec7-a96f-07533accd494'),
]
def retrieve(item):
 name,url=item
 row=dict(id=name,requested_url=url,time_utc=datetime.now(timezone.utc).isoformat(),method='Unauthenticated ordinary HTTPS GET, no bypass or modified access credentials')
 try:
  response=urlopen(Request(url,headers={'User-Agent':'Codex source-audit research'}),timeout=25)
 except HTTPError as error:response=error
 except Exception as error:
  row['error']=repr(error);return row
 body=response.read();row.update(status=response.status,resolved_url=response.url,content_type=response.headers.get('Content-Type'),bytes=len(body),sha256=hashlib.sha256(body).hexdigest())
 pdf=body.startswith(b'%PDF-')
 suffix='.pdf' if pdf else '.html'
 path=OUT/(name+suffix);path.write_bytes(body);row['saved_as']=path.name;row['pdf_signature']=pdf
 return row
rows=list(ThreadPoolExecutor(max_workers=4).map(retrieve,URLS))
(OUT/('RETRIEVAL'+('-'+sys.argv[1] if len(sys.argv)>1 else '')+'.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
print(json.dumps(rows,indent=2))
