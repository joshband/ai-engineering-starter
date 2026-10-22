#!/usr/bin/env python3
"""M1 structural checker and M2 control validation entry point."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = '''README.md CHANGELOG.md core/standards/ENGINEERING_STANDARD.md core/standards/AUTONOMY_AND_RISK.md core/contracts/TASK_CONTRACT.md core/contracts/HANDOFF_CONTRACT.md core/contracts/COMPLETION_CONTRACT.md core/contracts/EXCEPTION_CONTRACT.md core/workflows/LIFECYCLE.md core/workflows/PROFILES.md core/templates/AGENTS.md core/templates/PROJECT_PROFILE.md core/templates/TASK.md core/templates/HANDOFF.md core/templates/REVIEW.md core/templates/ADR.md docs/ADOPTION.md docs/SECURITY_BOUNDARIES.md validation/acceptance-matrix.md'''.split()
errors=[]
def check(ok, message):
    if not ok: errors.append(message)
for name in REQUIRED:
    check((ROOT/name).is_file(), 'Missing: '+name)
docs={p:p.read_text(encoding='utf-8') for p in ROOT.rglob('*.md')}
expected=[f'STD-{i:02}' for i in range(1,17)]
definitions=[]
links=0
for path,body in docs.items():
    found=re.findall(r'^## (STD-\d{2}) — ', body, re.M)
    definitions.extend(found)
    check(path==ROOT/'core/standards/ENGINEERING_STANDARD.md' or not found, 'Definition outside standard: '+str(path))
    for policy in re.findall(r'\bSTD-\d+\b',body):
        check(policy in expected,'Unknown policy: '+policy)
    for dest in re.findall(r'\[[^\]\n]+\]\(([^)\s]+)\)',body):
        if re.match(r'[A-Za-z][A-Za-z0-9+.-]*:',dest): continue
        links+=1
        file,_,fragment=unquote(dest).partition('#')
        target=(path.parent/file).resolve() if file else path
        check(target.is_relative_to(ROOT),'Escaping link: '+dest)
        check(target.is_file(),f'Broken link: {path.relative_to(ROOT)} -> {dest}')
        if fragment and target.is_file():
            anchors={re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in re.findall(r'^#{1,6} (.+)$',target.read_text(),re.M)}
            check(fragment in anchors,'Unknown fragment: '+dest)
    check(not re.search(r'(?i)\bSSMX\b|sk-proj-[A-Za-z0-9]+|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',body),'Project or credential marker: '+str(path))
check(sorted(definitions)==expected,'Expected one canonical heading per STD')
fields={
'core/contracts/TASK_CONTRACT.md':['Objective','Scope','Constraints','Acceptance criteria','Authority boundaries','risk and autonomy','project revision','dependencies','budget','approval and escalation'],
'core/templates/TASK.md':['Objective:','Scope:','Constraints:','Acceptance criteria:','Authority boundaries:','Risk / autonomy','Project revision:','Dependencies:','Budget:','Approval and escalation:'],
'core/templates/HANDOFF.md':['Current objective:','Authorized scope:','Work completed:','Repository and revision:','Checks run:','Decisions:','Unresolved issues:','Next safe action:'],
'core/contracts/EXCEPTION_CONTRACT.md':['requirement ID','reason','scope','risk','compensating safeguard','responsible authorizer','expiration or review trigger']}
for name,terms in fields.items():
    body=docs.get(ROOT/name,'').lower()
    for term in terms: check(term.lower() in body,'Missing field '+term+' in '+name)
completion=docs.get(ROOT/'core/contracts/COMPLETION_CONTRACT.md','')
for heading,values in {
'Execution state':['Completed','Partial','Blocked','Rejected','Canceled'],
'Acceptance state':['Pending review','Accepted','Changes requested','Rejected','Not applicable'],
'Verification status':['Passed','Failed','Not run','Not applicable','Unverified']}.items():
    section=re.search(rf'^## {heading}\n(.*?)(?=^## |\Z)',completion,re.M|re.S)
    check(section is not None,'Missing status section: '+heading)
    if section:
        rows=re.findall(r'^\| ([^|]+?) \|',section[1],re.M)
        check(rows[2:]==values,'Incorrect vocabulary: '+heading)
taxonomy=docs.get(ROOT/'core/standards/AUTONOMY_AND_RISK.md','')
for heading in ['Risk profiles','Autonomy levels','Task complexity','Workflow profiles']:
    check('## '+heading in taxonomy,'Missing classification: '+heading)
if errors:
    print('Failed: M1 structural validation')
    for error in errors: print('- '+error)
    sys.exit(1)
print(f'Passed: {len(REQUIRED)} required files; {len(docs)} Markdown files; {links} relative links; 16 canonical definitions; expected fields, classification sections, status vocabulary, narrow hygiene scan.')
print('Unverified by M1 checks: semantic policy correctness, enforcement, agent compatibility, comprehensive confidentiality. M1–M3 and M5 accepted; M4 provisionally accepted with live discovery deferred; M5 acceptance: Accepted and merged.')
from validate_controls import main as validate_m2
sys.exit(validate_m2([]))
