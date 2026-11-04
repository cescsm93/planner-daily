import json, glob, os
files = sorted(glob.glob('data/*.json'))
latest = files[-1]
dates = [os.path.basename(f)[:-5] for f in files]
def js(o): return json.dumps(o, ensure_ascii=False).replace('</', '<\\/')
d = json.load(open(latest))
assert [s['id'] for s in d['sections']] == ['papers','policies','cases','tools'], 'sections must be papers/policies/cases/tools'
for s in d['sections']:
    for it in s['items']:
        for k in ('title','source','date','brief','url'): assert it.get(k), (s['id'], it.get('title'), k)
html = open('template.html').read().replace('__DATA__', js(d)).replace('__DATES__', js(dates))
open('index.html', 'w').write(html)
print('built from', latest, '| issues:', dates, '| items:', sum(len(s['items']) for s in d['sections']))
