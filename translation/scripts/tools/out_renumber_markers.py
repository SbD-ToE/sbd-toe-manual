"""Renumber markers in an out.json unit after new protected tokens were inserted by a re-prepare.
Old markers in the out text are, in order, the job's protected items whose literal text is NOT present in the out text."""
import json, re, sys
rel, uid = sys.argv[1], sys.argv[2]
job=json.load(open(f'{rel}.job.json')); P=f'{rel}.out.json'; O=json.load(open(P,encoding='utf-8'))
u=None
def walk(x):
    global u
    if isinstance(x,dict):
        if x.get('id')==uid and x.get('translate'): u=x
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(job['segments'])
seg=next(s for s in O['segments'] if s['id']==uid); text=seg['text']
prot=u['protected']
literal=[p for p in prot if p['text'] in text]
remaining=[p for p in prot if p['text'] not in text]
old=re.findall(r'⟦P\d+⟧', text)
old_unique=list(dict.fromkeys(old))
assert len(old_unique)==len(remaining), (uid, old_unique, [p['marker'] for p in remaining])
tmp=text
for i,om in enumerate(old_unique): tmp=tmp.replace(om, f'@@{i}@@')
for i,p in enumerate(remaining): tmp=tmp.replace(f'@@{i}@@', p['marker'])
for p in sorted(literal,key=lambda p:-len(p['text'])): tmp=tmp.replace(p['text'], p['marker'],1)
seg['text']=tmp; json.dump(O,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1); print(uid,'→',tmp[:160])
