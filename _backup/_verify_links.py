# -*- coding: utf-8 -*-
import re, os, urllib.parse

html = open(r'E:\vscode\index.html', encoding='utf-8').read()
links = [urllib.parse.unquote(m) for m in re.findall(r'href="\./([^"]+)"', html)]
files = {f for f in os.listdir(r'E:\vscode') if f.lower().endswith('.html')}
missing = [l for l in links if l not in files]

print('LINKS(%d):' % len(links))
for l in links:
    print('  ', l)
print('MISSING:', missing if missing else 'none')

# also check: every lesson html on disk (excluding index itself) is linked
all_pages = sorted(f for f in files if f.lower() != 'index.html')
unlinked = [f for f in all_pages if f not in links]
print('UNLINKED_ON_DISK:', unlinked if unlinked else 'none')
