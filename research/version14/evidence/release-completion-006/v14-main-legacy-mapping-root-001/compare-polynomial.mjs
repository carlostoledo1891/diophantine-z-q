import fs from 'node:fs';
import crypto from 'node:crypto';
import {isDeepStrictEqual} from 'node:util';
const [originalPath, portablePath] = process.argv.slice(2);
if (!originalPath || !portablePath) throw new Error('Usage: node compare-polynomial.mjs ORIGINAL PORTABLE');
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const ob=fs.readFileSync(originalPath), pb=fs.readFileSync(portablePath);
if (sha(ob)!=='a86790bbf1095d6b1cea9c66067ad8432dd35adc320254eecde21f9f98574714' || sha(pb)!=='4d639d4c44e69ea360d36d4591b8fdc82269d68b9363af0157d1e5c1174c7af6') throw new Error('Unexpected input version');
const o=JSON.parse(ob), p=JSON.parse(pb);
for (const k of ['precision','power_value']) {
  if (o.recipes[k].sourceFile===p.recipes[k].sourceFile) throw new Error('Expected changed provenance string');
  o.recipes[k].sourceFile=p.recipes[k].sourceFile;
}
const ok=Object.keys(o.sourceHashes), pk=Object.keys(p.sourceHashes);
if (ok.length!==1 || pk.length!==1 || ok[0]===pk[0] || o.sourceHashes[ok[0]]!==p.sourceHashes[pk[0]]) throw new Error('Expected key-only sourceHashes change');
o.sourceHashes={[pk[0]]:o.sourceHashes[ok[0]]};
if (!isDeepStrictEqual(o,p)) throw new Error('Additional JSON difference');
console.log(JSON.stringify({status:'pass',original:{bytes:ob.length,sha256:sha(ob)},portable:{bytes:pb.length,sha256:sha(pb)},library_template_count:Object.keys(p.library.templates).length,named_recipe_count:Object.keys(p.recipes).length,root_recipe:p.rootRecipe,parameterNames:p.parameterNames,parameterDomain:p.parameterDomain,witnessDomain:p.witnessDomain,root_parameter_count:p.recipes.integers.parameterCount,root_variable_count:p.recipes.integers.variableCount,root_witness_count:p.recipes.integers.witnessCount},null,2));
