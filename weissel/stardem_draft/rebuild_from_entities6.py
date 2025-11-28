import json
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
    # repository root is two levels up from this script
    repo_root = Path(__file__).resolve().parents[2]
    src = repo_root / "weissel" / "stardem_choice" / "stories_with_entities6.json"
    out_dir = base / "basketball"
    out_dir.mkdir(parents=True, exist_ok=True)

    if not src.exists():
        print(f"ERROR: source file not found: {src}")
        return 2

    with open(src, "r", encoding="utf-8") as f:
        stories = json.load(f)

    hs = [s for s in stories if s.get("metadata_level_of_play") == "high school"]

    by_sport = {}
    for s in hs:
        sport = normalize_sport(s.get("metadata_sport"))
        by_sport.setdefault(sport, []).append(s)

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

    for sport_name, (written, target, available) in results.items():
        if written < target:
            print(f"WROTE (short): {sport_name} -> {written}/{target} (available {available})")
        else:
            print(f"WROTE: {sport_name} -> {written}/{target}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
