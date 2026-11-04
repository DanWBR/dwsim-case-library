#!/usr/bin/env python3
"""Writes cases/index.json: every flowsheet under cases/, the preview picture next to it, and the
DWSIM Patreon Edition components it uses.

DWSIM reads this file from raw.githubusercontent.com to fill the Case Library tab of its welcome
screen. The GitHub API it read before allows 60 requests an hour per network and is blocked by some
proxies; a plain file has neither problem. The index workflow runs this on every push to main, so
the file never needs editing by hand.

A case that uses a component of the Patreon Edition (a unit operation, property package or
extension the open-source DWSIM does not have) is listed with those components under "requires":
the open-source DWSIM marks it, so its users know it will not open there. The components are found
by the types the flowsheet records, against patreon_components.json (the public types of each
Patreon Edition assembly, regenerated from the DWSIM builds when components are added).
"""
import json
import os
import re
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CASES = os.path.join(ROOT, 'cases')

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'patreon_components.json'), encoding='utf-8') as fh:
    COMPONENTS = json.load(fh)['components']
OWNER = {t: c for c in COMPONENTS for t in c['types']}


def flowsheet_xml(path):
    """The flowsheet's XML: the file itself (.dwxml), or the XML inside the zip (.dwxmz)."""
    if path.lower().endswith('.dwxml'):
        with open(path, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    with zipfile.ZipFile(path) as z:
        name = next(n for n in z.namelist() if n.lower().endswith('.xml'))
        return z.read(name).decode('utf-8', 'replace')


def requires(path):
    """The Patreon Edition components the flowsheet uses, by name, in the catalog's order."""
    types = {t.split(',')[0].strip() for t in re.findall(r'<Type>([^<]+)</Type>', flowsheet_xml(path))}
    used = {OWNER[t]['assembly'] for t in types if t in OWNER}
    return [{'name': c['name'], 'assembly': c['assembly']} for c in COMPONENTS if c['assembly'] in used]


cases = []
for dirpath, dirs, files in os.walk(CASES):
    dirs.sort()
    for name in sorted(files):
        if not name.lower().endswith(('.dwxmz', '.dwxml')):
            continue
        full = os.path.join(dirpath, name)
        path = os.path.relpath(full, ROOT).replace(os.sep, '/')
        preview = os.path.splitext(path)[0] + '.png'
        case = {'path': path, 'preview': preview if os.path.exists(os.path.join(ROOT, preview)) else None}
        needs = requires(full)
        if needs:
            case['edition'] = 'patreon'
            case['requires'] = needs
        cases.append(case)

cases.sort(key=lambda c: c['path'].lower())
with open(os.path.join(CASES, 'index.json'), 'w', encoding='utf-8', newline='\n') as fh:
    json.dump({'version': 1, 'cases': cases}, fh, indent=1)
    fh.write('\n')
patreon = [c for c in cases if c.get('edition') == 'patreon']
print(len(cases), 'cases in cases/index.json,', len(patreon), 'need the Patreon Edition')
for c in patreon:
    print('  ', c['path'], '->', ', '.join(r['name'] for r in c['requires']))
