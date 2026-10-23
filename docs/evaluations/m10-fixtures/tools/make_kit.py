#!/usr/bin/env python3
"""Recreate the pinned, link-repaired starter-kit copies used for Arm B in the M10 pilot.

Usage: make_kit.py <repo> <sha> <out-dir> [--with-safe-handoff]

Copies core/standards/ENGINEERING_STANDARD.md and AUTONOMY_AND_RISK.md (to core/) and the
task-intake and change-verification skills (to skills/<name>/SKILL.md) from <repo> at <sha>.
Markdown links to files that are absent from the fixture are replaced by their link text;
links between the two standards are kept. F4 also used --with-safe-handoff.
The pilot used sha 3386843808902b993142f25731c54e7d7786661a.
"""
import pathlib, re, subprocess, sys

args = [a for a in sys.argv[1:] if not a.startswith("--")]
repo, sha, out = args
skills = ["task-intake", "change-verification"] + (["safe-handoff"] if "--with-safe-handoff" in sys.argv else [])
KEEP = {"ENGINEERING_STANDARD.md", "AUTONOMY_AND_RISK.md"}

def show(path):
    return subprocess.run(["git", "-C", repo, "show", f"{sha}:{path}"], capture_output=True, text=True, check=True).stdout

def repair(text):
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: m.group(0) if m.group(2) in KEEP else m.group(1), text)

files = {
    "core/ENGINEERING_STANDARD.md": "core/standards/ENGINEERING_STANDARD.md",
    "core/AUTONOMY_AND_RISK.md": "core/standards/AUTONOMY_AND_RISK.md",
}
for s in skills:
    files[f"skills/{s}/SKILL.md"] = f"skills/{s}/SKILL.md"
for dst, src in files.items():
    p = pathlib.Path(out) / dst
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(repair(show(src)))
