---
name: release-check
description: Check docs cover the latest released Trails SDK version.
---

# Release Check (Docs)

## Run

```
python3 .claude/skills/release-check/scripts/check.py
```

- The live changelog (`https://docs.trails.build/sdk/changelog`) lists the latest released `0xtrails` version (npm dist-tag `latest`).
- On `origin/main` but not live = deploy lag (WARN). On neither = the docs update never happened (FAIL).
- Prints PASS/FAIL/WARN lines with details; exits 1 on any FAIL.