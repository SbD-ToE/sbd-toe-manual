"""After a re-prepare that added do-not-translate names, restore their markers in existing out.json files:
for each translatable unit, replace the protected text (or its en-GB-respelled variant) by the marker."""
import json, sys, re, glob, pathlib
root=pathlib.Path(sys.argv[1]); changed=0
def variants(t):
    v={t}
    v.add(t.replace('Modeling','Modelling').replace('modeling','modelling'))
    v.add(t.replace('Defense','Defence'))
    return v
for job in glob.glob(str(root/'**'/'*.job.json'),recursive=True):
    out=pathlib.Path(job[:-len('.job.json')]+'.out.json')
    if not out.exists(): continue
    J=json.load(open(job)); O=json.load(open(out,encoding='utf-8')); segs={s['id']:s for s in O['segments']}
    prot={}
    def walk(x):
        if isinstance(x,dict):
            if x.get('translate') and 'id' in x and x.get('protected'): prot[x['id']]=x['protected']
            for v in x.values(): walk(v)
        elif isinstance(x,list):
            for v in x: walk(v)
    walk(J['segments'])
    n=0
    for uid,plist in prot.items():
        s=segs.get(uid)
        if not s: continue
        for p in plist:
            if p['marker'] in s['text']: continue
            for v in sorted(variants(p['text']),key=len,reverse=True):
                if v in s['text']:
                    s['text']=s['text'].replace(v,p['marker'],1); n+=1; break
    if n:
        json.dump(O,open(out,'w',encoding='utf-8'),ensure_ascii=False,indent=1); changed+=n; print(f"{out.name}: {n} marker(s) restored")
print("total restored:",changed)
