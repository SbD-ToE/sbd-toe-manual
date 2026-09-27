import json,sys,glob,pathlib
root=pathlib.Path(sys.argv[1]); n=0
for job in glob.glob(str(root/'**'/'*.job.json'),recursive=True):
    out=pathlib.Path(job[:-9]+'.out.json')
    if not out.exists(): continue
    units=set(json.load(open(job))['units']); O=json.load(open(out,encoding='utf-8'))
    keep=[s for s in O['segments'] if s['id'] in units]
    if len(keep)!=len(O['segments']):
        n+=len(O['segments'])-len(keep); O['segments']=keep; json.dump(O,open(out,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print("dropped non-unit ids:",n)
