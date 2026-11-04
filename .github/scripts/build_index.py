#!/usr/bin/env python3
"""Writes cases/index.json: every flowsheet under cases/ and the preview picture next to it.

DWSIM reads this file from raw.githubusercontent.com to fill the Case Library tab of its welcome
screen. The GitHub API it read before allows 60 requests an hour per network and is blocked by some
proxies; a plain file has neither problem. The index workflow runs this on every push to main, so
the file never needs editing by hand.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CASES = os.path.join(ROOT, 'cases')

cases = []
for dirpath, dirs, files in os.walk(CASES):
    dirs.sort()
    for name in sorted(files):
        if not name.lower().endswith(('.dwxmz', '.dwxml')):
            continue
        path = os.path.relpath(os.path.join(dirpath, name), ROOT).replace(os.sep, '/')
        preview = os.path.splitext(path)[0] + '.png'
        cases.append({'path': path, 'preview': preview if os.path.exists(os.path.join(ROOT, preview)) else None})

cases.sort(key=lambda c: c['path'].lower())
with open(os.path.join(CASES, 'index.json'), 'w', encoding='utf-8', newline='\n') as fh:
    json.dump({'version': 1, 'cases': cases}, fh, indent=1)
    fh.write('\n')
print(len(cases), 'cases in cases/index.json')
