import copy, json, pathlib, tempfile, unittest
import wire_sources as w
class Wiring(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=pathlib.Path(self.tmp.name);self.addCleanup(self.tmp.cleanup)
        def save(path,value):
            raw=json.dumps(value).encode();(self.root/path).write_bytes(raw);return dict(side='head',path=path,sha256=w.sha(raw))
        self.save=save;self.op=save('original.json',dict(sources=[dict(side='head',path='original.md',sha256='1'*64)],uses=[dict(id='O')]))
        self.entries=[];all_sources=[dict(side='head',path='original.md',sha256='1'*64)]
        for i in range(2):
            source=dict(side='head',path='added'+str(i)+'.md',sha256=str(i+2)*64)
            ip=save('initial'+str(i)+'.json',dict(sources=[source],uses=[dict(id='S'+str(i))]));pp=save('passages'+str(i)+'.json',[])
            f=dict(frozen_at='2026-11-09T01:00:00Z',method='Synthetic read',prior_exposure='Explicit synthetic exposure',limitations='Unit fixture only')
            fp=save('freeze'+str(i)+'.json',f);spec=dict(original_initial=self.op,supplemental_initial=ip,supplemental_passages=pp,freeze=fp,sources=[source])
            comp=dict(initial_sha256=ip['sha256'],initial_passages_sha256=pp['sha256'],reconstruction=dict(f,run_id='synthetic-reviewer',compared_at='2026-11-09T01:01:00Z'))
            self.entries.append((spec,comp));all_sources.append(source)
        self.d=dict(initial=self.op,sources=all_sources,reconstruction=dict(frozen_at='2026-11-08T01:00:00Z'))
    def runwire(self):return w.wire(self.d,self.entries,self.root)
    def test_two_extensions_preserve_original(self):
        old=copy.deepcopy(self.d);out=self.runwire();self.assertEqual(old,self.d);self.assertEqual(len(out['source_extensions']),2);self.assertEqual(out['reconstruction'],old['reconstruction'])
    def test_missing_comparison_time(self):
        del self.entries[0][1]['reconstruction']['compared_at']
        with self.assertRaises(KeyError):self.runwire()
    def test_bad_chronology(self):
        self.entries[0][1]['reconstruction']['compared_at']='2026-11-09T01:00:00Z'
        with self.assertRaisesRegex(ValueError,'not after'):self.runwire()
    def test_wrong_initial(self):
        self.entries[0][1]['initial_sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'wrong supplement'):self.runwire()
    def test_exposure_rewrite(self):
        self.entries[0][1]['reconstruction']['prior_exposure']='Blind'
        with self.assertRaisesRegex(ValueError,'attestation changed'):self.runwire()
    def test_missing_second_extension(self):
        self.entries.pop()
        with self.assertRaisesRegex(ValueError,'source union'):self.runwire()
    def test_overlap(self):
        self.entries.append(self.entries[0])
        with self.assertRaisesRegex(ValueError,'overlapping'):self.runwire()
    def test_no_existing_replacement(self):
        self.d['source_extensions']=[]
        with self.assertRaisesRegex(ValueError,'refuse replacement'):self.runwire()
    def test_changed_frozen_file(self):
        (self.root/'initial0.json').write_text('{}')
        with self.assertRaisesRegex(ValueError,'changed frozen'):self.runwire()
if __name__=='__main__':unittest.main()
