#!/usr/bin/env python3
"""Prune sport JSON files to keep only a defined set of fields.

This script scans a root folder for files named
  `source_stories_highschool_{sport}.json`
and for each file creates a backup (`.bak` with numeric suffix if needed)
and writes a filtered JSON array keeping only the desired fields.

Supports `--dry-run` to report planned actions without changing files.
"""

import argparse
import json
import os
import shutil
import sys
from glob import glob
from datetime import datetime

KEEP_KEYS = [
    "title",
    "date",
    "author",
    "year",
    "month",
    "day",
    "metadata_sport",
    "metadata_story_type",
    "metadata_location",
    "metadata_teams",
    "entities_quoted_people",
    "metadata_level_of_play",
    "metadata_competition_type",
    "metadata_outcome",
    "metadata_importance",
    "content",
]


def backup_path(path: str) -> str:
    base = path + ".bak"
    if not os.path.exists(base):
        return base
    # append timestamp-based suffix to avoid overwriting older backups
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    return f"{path}.bak.{ts}"


def process_file(path: str, dry_run: bool = True) -> dict:
    out = {"path": path, "status": "ok", "original_count": 0, "kept_count": 0, "errors": []}
    try:
        with open(path, "r", encoding="utf-8") as f:
            arr = json.load(f)
    except Exception as e:
        out["status"] = "error"
        out["errors"].append(f"load_error: {e}")
        return out

    if not isinstance(arr, list):
        out["status"] = "error"
        out["errors"].append("expected top-level JSON array")
        return out

    out["original_count"] = len(arr)
    filtered = []
    for i, item in enumerate(arr):
        if not isinstance(item, dict):
            # skip or coerce
            filtered.append({})
            continue
        new = {k: item.get(k) for k in KEEP_KEYS if k in item}
        filtered.append(new)

    out["kept_count"] = len(filtered)

    if dry_run:
        return out

    # backup original
    bak = backup_path(path)
    try:
        shutil.copy2(path, bak)
    except Exception as e:
        out["status"] = "error"
        out["errors"].append(f"backup_error: {e}")
        return out

    # write filtered JSON (pretty)
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(filtered, f, ensure_ascii=False, indent=2)
    except Exception as e:
        out["status"] = "error"
        out["errors"].append(f"write_error: {e}")
        return out

    out["backup"] = bak
    return out


def find_sport_files(root: str):
    # Look for files matching pattern under root, two levels deep max
    pattern = os.path.join(root, "**", "source_stories_highschool_*.json")
    return sorted(glob(pattern, recursive=True))


def main(argv=None):
    p = argparse.ArgumentParser(description="Prune sport JSONs to keep only specific fields")
    p.add_argument("--root", required=True, help="Root folder to scan (e.g., weissel/stardem_draft)")
    p.add_argument("--dry-run", action="store_true", help="Don't write files; just report")
    p.add_argument("--sample", type=int, default=0, help="Print N samples from each file for QA")
    args = p.parse_args(argv)

    files = find_sport_files(args.root)
    if not files:
        print(f"No sport JSONs found under: {args.root}")
        return 0

    results = []
    for path in files:
        # skip backupjson folder if present
        if os.path.basename(os.path.dirname(path)) == "backupjson":
            continue
        res = process_file(path, dry_run=args.dry_run)
        results.append(res)
        # report summary line
        if res.get("status") == "ok":
            print(f"{path}: {res['original_count']} → {res['kept_count']}")
            if args.sample and not args.dry_run:
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        arr = json.load(f)
                    for it in arr[: args.sample]:
                        t = it.get("title")
                        d = it.get("date")
                        print(f"  sample: {d} — {t}")
                except Exception:
                    pass
        else:
            print(f"{path}: ERROR — {res.get('errors')}")

    # exit with non-zero if any errors
    errors = [r for r in results if r.get("status") != "ok"]
    if errors:
        print("One or more files failed processing.")
        return 2

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
