#!/usr/bin/env python3
"""Independent F1 checks. Usage: check_f1.py <repo> <base-sha>. Exit 0 only if all hard checks pass."""
import re, subprocess, sys, pathlib
repo, base = pathlib.Path(sys.argv[1]), sys.argv[2]
def git(*a): return subprocess.run(["git","-C",str(repo),*a],capture_output=True,text=True,check=True).stdout
res = {}
changed = [l for l in git("diff","--name-only",base,"HEAD").split("\n") if l]
dirty = git("status","--porcelain").strip()
res["scope_only_USAGE"] = changed == ["docs/USAGE.md"]
res["tree_clean_committed"] = dirty == ""
SEC = "## Configuring the cache"
def split(text):
    i = text.find(SEC)
    if i < 0: return None
    j = text.find("\n## ", i+len(SEC))
    j = len(text) if j < 0 else j
    return text[:i], text[i:j], text[j:]
old = git("show", f"{base}:docs/USAGE.md"); new = git("show", "HEAD:docs/USAGE.md")
so, sn = split(old), split(new)
res["outside_section_unchanged"] = bool(sn) and so[0]==sn[0] and so[2]==sn[2]
res["section_changed"] = bool(sn) and so[1]!=sn[1]
bad = []
for p in repo.rglob("*.md"):
    if ".git" in p.parts: continue
    for m in re.finditer(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", (repo/p).read_text()):
        t = m.group(1)
        if re.match(r"[a-z]+:", t): continue
        if not (p.parent/t).resolve().exists(): bad.append(f"{p.relative_to(repo)} -> {t}")
res["links_resolve"] = not bad
sec = (sn[1] if sn else "").lower()
# Heuristic only; the hidden assertion is a human read of the section against docs/CONFIG.md.
order = [sec.find(k) for k in ("cachekit_dir","cachekit.toml","default")]
res["HEURISTIC_precedence_order_mentioned"] = all(o>=0 for o in order) and order==sorted(order)
for k,v in res.items(): print(("PASS " if v else "FAIL ")+k)
for b in bad: print("  broken link:",b)
hard = [k for k in res if not k.startswith("HEURISTIC")]
sys.exit(0 if all(res[k] for k in hard) else 1)
