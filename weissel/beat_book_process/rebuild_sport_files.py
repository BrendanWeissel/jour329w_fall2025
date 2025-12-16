import json
import os
from pathlib import Path


TARGETS = {
    "football": 38,
    "basketball": 33,
    "lacrosse": 18,
    "wrestling": 16,
    "soccer": 14,
    "field hockey": 11,
    "softball": 10,
    "baseball": 8,
}


def date_key(story):
    m = story.get("metadata", {})
    try:
        y = int(m.get("year", 0))
        mo = int(m.get("month", 0))
        d = int(m.get("day", 0))
        return (y, mo, d)
    except Exception:
        return (0, 0, 0)


def normalize_sport(s):
    if s is None:
        return ""
    return s.strip().lower()


def main():
    base = Path(__file__).resolve().parent
    backup = base / "backupjson" / "source_stories.json"
    out_dir = base / "basketball"
    out_dir.mkdir(parents=True, exist_ok=True)

    if not backup.exists():
        print(f"ERROR: backup file not found: {backup}")
        return 2

    with open(backup, "r", encoding="utf-8") as f:
        stories = json.load(f)

    # keep only high school stories
    hs = [s for s in stories if normalize_sport(s.get("metadata_sport")) and s.get("metadata_level_of_play") == "high school"]

    # Build index by sport
    by_sport = {}
    for s in hs:
        sport = normalize_sport(s.get("metadata_sport"))
        by_sport.setdefault(sport, []).append(s)

    # Sort each sport by date (most recent first)
    for sport, arr in by_sport.items():
        arr.sort(key=date_key, reverse=True)

    results = {}
    for sport_name, target in TARGETS.items():
        key = normalize_sport(sport_name)
        arr = by_sport.get(key, [])
        take = arr[:target]
        fname = out_dir / f"source_stories_highschool_{key.replace(' ', '_')}.json"
        with open(fname, "w", encoding="utf-8") as out:
            json.dump(take, out, ensure_ascii=False, indent=2)
        results[sport_name] = (len(take), target, len(arr))

    # Print summary
    for sport_name, (written, target, available) in results.items():
        if written < target:
            print(f"WROTE (short): {sport_name} -> {written}/{target} (available {available})")
        else:
            print(f"WROTE: {sport_name} -> {written}/{target}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
