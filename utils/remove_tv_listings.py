#!/usr/bin/env python3
"""Remove items whose title starts with 'TV LISTING' from the filtered sports JSON.

Writes output to: weissel/stardem_topic_entities/sports2024highschool2.json
Prints removed and remaining counts.
"""
import json
from pathlib import Path

SRC = Path("weissel/stardem_topic_entities/sports2024highschool.json")
OUT = Path("weissel/stardem_topic_entities/sports2024highschool2.json")

def is_tv_listing(item):
    title = item.get("title") if isinstance(item, dict) else None
    if not title or not isinstance(title, str):
        return False
    t = title.strip().upper()
    return t.startswith("TV LISTING")

def main():
    if not SRC.exists():
        print(f"Source not found: {SRC}")
        return
    data = json.loads(SRC.read_text(encoding="utf-8"))
    # handle top-level dict with list inside
    if isinstance(data, dict):
        # try common keys
        for k in ("items","articles","stories","data"):
            if k in data and isinstance(data[k], list):
                arr = data[k]
                break
        else:
            # not in known shape; try any list-valued value
            lists = [v for v in data.values() if isinstance(v, list)]
            arr = lists[0] if lists else []
        top_level_is_dict = True
    elif isinstance(data, list):
        arr = data
        top_level_is_dict = False
    else:
        print("Unrecognized JSON structure")
        return

    original_count = len(arr)
    filtered = [it for it in arr if not is_tv_listing(it)]
    removed_count = original_count - len(filtered)

    # write back preserving top-level shape
    if top_level_is_dict:
        # find the key we extracted earlier
        out_data = data.copy()
        for k in ("items","articles","stories","data"):
            if k in out_data and isinstance(out_data[k], list):
                out_data[k] = filtered
                break
        else:
            # fallback: replace first list value
            for k,v in out_data.items():
                if isinstance(v, list):
                    out_data[k] = filtered
                    break
    else:
        out_data = filtered

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out_data, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Wrote {OUT} — removed {removed_count}, remaining {len(filtered)}")

if __name__ == "__main__":
    main()
