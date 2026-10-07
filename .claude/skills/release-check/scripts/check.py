#!/usr/bin/env python3
"""Release check for trails-docs.

Usage: check.py

The live changelog (docs.trails.build/sdk/changelog) lists the latest released
0xtrails version (npm dist-tag latest). On origin/main but not live = deploy
lag (WARN); on neither = the docs update never happened (FAIL).
Exits 1 on any FAIL.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

import urllib.request

BRANCH = "main"
CHANGELOG_PATH = "sdk/changelog.mdx"
DOCS_CHANGELOG_URL = "https://docs.trails.build/sdk/changelog"
REGISTRY = "https://registry.npmjs.org"
REPO_ROOT = Path(__file__).resolve().parents[4]

OPENER = urllib.request.build_opener()
OPENER.addheaders = [("User-Agent", "curl/8")]
urllib.request.install_opener(OPENER)

FAILURES = []


def report(status, name, detail):
    print(f"{status:4}  {name}: {detail}")
    if status == "FAIL":
        FAILURES.append(name)


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO_ROOT)
    if p.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)} failed: {p.stderr.strip()[:300]}")
    return p.stdout


def npm_latest(pkg):
    with urllib.request.urlopen(f"{REGISTRY}/{pkg}", timeout=15) as r:
        d = json.load(r)
    return d["dist-tags"]["latest"]


def main():
    latest = npm_latest("0xtrails")
    marker = f"0xtrails@{latest}"
    run(["git", "fetch", "-q", "origin", BRANCH])
    try:
        main_has = marker in run(["git", "show", f"origin/{BRANCH}:{CHANGELOG_PATH}"])
    except RuntimeError:
        main_has = False
    try:
        live = urllib.request.urlopen(DOCS_CHANGELOG_URL, timeout=15).read().decode(errors="replace")
        live_has = marker in live
        newest_live = re.search(r"0xtrails@(\d+\.\d+\.\d+)", live)
        live_detail = f"live changelog tops out at {newest_live.group(1)}" if newest_live else "live changelog unreadable"
    except Exception as e:
        live_has = False
        live_detail = f"live changelog unreachable: {e}"
    if live_has:
        report("PASS", "docs", f"live changelog includes released {marker}")
    elif main_has:
        report("WARN", "docs", f"{marker} on origin/{BRANCH} but not live (deploy lag); {live_detail}")
    else:
        report("FAIL", "docs", f"docs never updated for {marker}; {live_detail}")
    print()
    sys.exit(1 if FAILURES else 0)


if __name__ == "__main__":
    main()