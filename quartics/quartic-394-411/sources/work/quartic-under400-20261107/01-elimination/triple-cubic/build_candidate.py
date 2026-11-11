"""Rebuild the selected 488-coordinate grouped detector presentation."""
import json
from hybrid import build,OUT
candidate,construction=build({1:(3,3,3),10:(2,),40:(2,3)})
(OUT/'candidate479-ir.json').write_text(json.dumps(candidate,indent=2)+'\n')
(OUT/'candidate479-construction.json').write_text(json.dumps(construction,indent=2)+'\n')
print({'coordinates':len(candidate['coordinates']),'residuals':len(candidate['residuals'])})


