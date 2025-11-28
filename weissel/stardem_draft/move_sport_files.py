#!/usr/bin/env python3
"""Safe mover for per-sport JSONs.

Usage examples:
  Dry-run (shows planned moves and counts):
    python3 weissel/stardem_draft/move_sport_files.py \
      --source-dir weissel/stardem_draft/basketball \
      --dest-root weissel/stardem_draft \
      --dry-run

  Execute move and print counts + 3-sample titles/dates:
    python3 weissel/stardem_draft/move_sport_files.py \
      --source-dir weissel/stardem_draft/basketball \
      --dest-root weissel/stardem_draft \
      --sample 3

The script detects files named like:
  source_stories_highschool_{sport}.json
and moves them to: {dest_root}/{sport}/

It is idempotent and will not overwrite existing files unless --overwrite is passed.
"""

import argparse
import json
import os
import re
import shutil
import sys
from typing import List


FNAME_RE = re.compile(r"source_stories_highschool_(?P<sport>[a-z0-9_]+)\.json$")

TARGETS = {
    "football": 38,
    "basketball": 33,
    "lacrosse": 18,
    "wrestling": 16,
    "soccer": 14,
    "field_hockey": 11,
    "softball": 10,
    "baseball": 8,
}


def find_matching_files(source_dir: str) -> List[str]:
    files = []
    for name in os.listdir(source_dir):
        if FNAME_RE.match(name):
            files.append(os.path.join(source_dir, name))
    return sorted(files)


def load_count_and_sample(path: str, sample_n: int = 0):
    try:
        with open(path, "r", encoding="utf-8") as f:
            arr = json.load(f)
    except Exception as e:
        return None, f"ERROR loading JSON: {e}", []
    count = len(arr) if isinstance(arr, list) else 0
    sample = []
    if sample_n and isinstance(arr, list):
        for i, it in enumerate(arr[:sample_n]):
            title = it.get("title") if isinstance(it, dict) else None
            date = it.get("date") if isinstance(it, dict) else None
            sample.append((title, date))
    return count, None, sample


def main(argv=None):
    p = argparse.ArgumentParser(description="Move per-sport JSON files into sport subfolders safely")
    p.add_argument("--source-dir", required=True, help="Directory containing the staged JSONs")
    p.add_argument("--dest-root", required=True, help="Destination root for sport folders")
    p.add_argument("--dry-run", action="store_true", help="Show planned moves but don't perform them")
    p.add_argument("--overwrite", action="store_true", help="Overwrite destination file if it exists")
    p.add_argument("--sample", type=int, default=0, help="Print N sample title/date from each file after move")
    p.add_argument("--quiet", action="store_true", help="Minimal output")
    args = p.parse_args(argv)

    source_dir = args.source_dir
    dest_root = args.dest_root

    if not os.path.isdir(source_dir):
        print(f"Source dir not found: {source_dir}")
        sys.exit(2)
    if not os.path.isdir(dest_root):
        print(f"Dest root not found, creating: {dest_root}")
        if not args.dry_run:
            os.makedirs(dest_root, exist_ok=True)

    files = find_matching_files(source_dir)
    if not files:
        print(f"No matching sport JSONs found in {source_dir}")
        return

    planned = []
    for src in files:
        name = os.path.basename(src)
        m = FNAME_RE.match(name)
        sport = m.group("sport")
        dest_dir = os.path.join(dest_root, sport)
        dest_path = os.path.join(dest_dir, name)
        planned.append((src, dest_dir, dest_path, sport))

    if not args.quiet:
        print("Planned moves:")
        for src, dest_dir, dest_path, sport in planned:
            print(f"  {os.path.basename(src)} -> {dest_dir}/")

    if args.dry_run:
        print("Dry-run only; no files were changed.")
    else:
        for src, dest_dir, dest_path, sport in planned:
            os.makedirs(dest_dir, exist_ok=True)
            if os.path.exists(dest_path) and not args.overwrite:
                print(f"Skipping (exists): {dest_path}")
                continue
            try:
                shutil.move(src, dest_path)
                print(f"Moved: {os.path.basename(src)} -> {dest_dir}/")
            except Exception as e:
                print(f"ERROR moving {src} -> {dest_path}: {e}")

    # Verification + sampling
    print("\nVerification:")
    any_errors = False
    for src, dest_dir, dest_path, sport in planned:
        check_path = dest_path if not args.dry_run else src
        if not os.path.exists(check_path):
            print(f"  Missing after move: {check_path}")
            any_errors = True
            continue
        count, err, sample = load_count_and_sample(check_path, sample_n=args.sample)
        if err:
            print(f"  {os.path.basename(check_path)}: {err}")
            any_errors = True
            continue
        target = TARGETS.get(sport)
        match_note = ""
        if target is not None:
            match_note = " (matches target)" if count == target else f" (target {target})"
        print(f"  {os.path.basename(check_path)}: {count} stories{match_note}")
        if args.sample and sample:
            for t, d in sample:
                print(f"    - {d} — {t}")

    if any_errors:
        print("\nOne or more errors were reported. Please review the messages above.")
        sys.exit(1)
    else:
        print("\nAll done.")


if __name__ == "__main__":
    main()
