#!/usr/bin/env python3
import json
import re
from pathlib import Path

SRC = Path("/workspaces/jour329w_fall2025/weissel/stardem_topic_entities/Sports.json")
OUT = Path("/workspaces/jour329w_fall2025/weissel/stardem_topic_entities/sports2024highschool.json")

HIGH_SCHOOL_RE = re.compile(r"\b(high school|high-school|prep\b|varsity|junior varsity|jr\.? varsity|\bJV\b|class of\b|freshman|sophomore|junior|senior|county high|HS\b|highschool)\b", re.I)
ROUNDUP_TITLE_RE = re.compile(r"\b(roundup|scores|prep scores|local scores|prep roundup|box scores|finals?)\b", re.I)
SCORE_PATTERN = re.compile(r"\b\d+[-–]\d+\b")


def looks_high_school(item):
    # Check explicit year/metadata fields first
    # If there's a target/audience field, prefer that
    for key in ("target_audience", "audience", "who_is_this_targeted_to"):
        v = item.get(key)
        if v and isinstance(v, str) and "high" in v.lower():
            return True

    # Tags or section
    tags = item.get("tags") or item.get("topics") or item.get("llm_tags")
    if isinstance(tags, list):
        for t in tags:
            if isinstance(t, str) and HIGH_SCHOOL_RE.search(t):
                return True

    section = item.get("Section") or item.get("section") or item.get("section_name")
    if isinstance(section, str) and HIGH_SCHOOL_RE.search(section):
        return True

    # Title and content
    title = (item.get("title") or "")
    content = (item.get("content") or "")
    if HIGH_SCHOOL_RE.search(title) or HIGH_SCHOOL_RE.search(content):
        return True

    # LLM classification may hint
    llm = item.get("llm_classification") or {}
    # sometimes llm_classification has explanation mentioning 'high school'
    explanation = llm.get("explanation") if isinstance(llm, dict) else None
    if isinstance(explanation, str) and HIGH_SCHOOL_RE.search(explanation):
        return True

    # fallback: if content mentions common HS words like 'senior', 'freshman' near team/school
    if re.search(r"\b(senior|freshman|sophomore|junior)\b", content, re.I):
        return True

    return False


def is_roundup(item):
    title = (item.get("title") or "")
    content = (item.get("content") or "")
    # Title indicates scores/roundup
    if ROUNDUP_TITLE_RE.search(title):
        return True
    # If content is short and contains many score patterns, consider it a roundup/scores list
    score_matches = SCORE_PATTERN.findall(content)
    words = len(re.findall(r"\w+", content))
    if words < 200 and len(score_matches) >= 2:
        return True
    # If content consists mostly of short lines like score lines (many newlines and short lines)
    lines = [l.strip() for l in content.splitlines() if l.strip()]
    short_lines = sum(1 for l in lines if len(l.split()) <= 6 and SCORE_PATTERN.search(l))
    if short_lines >= 3:
        return True
    return False


def year_is_2024(item):
    # Check 'year' field
    y = item.get("year")
    if isinstance(y, int):
        return y == 2024
    if isinstance(y, str) and y.isdigit():
        return int(y) == 2024
    # fallback: look in date string
    date = item.get("date") or item.get("pub_date") or item.get("publication_date") or ""
    if isinstance(date, str) and "2024" in date:
        return True
    # also check content for a 2024 date
    content = item.get("content") or ""
    if "2024" in content:
        return True
    return False


def main():
    data = json.loads(SRC.read_text())
    # Expecting a list
    if isinstance(data, dict):
        # try common keys
        for k in ("stories", "items", "articles"):
            if k in data and isinstance(data[k], list):
                data = data[k]
                break
        else:
            # if no list found, try to find the first list value
            for v in data.values():
                if isinstance(v, list):
                    data = v
                    break

    out = []
    for item in data:
        try:
            if not year_is_2024(item):
                continue
            if not looks_high_school(item):
                continue
            if is_roundup(item):
                continue
            out.append(item)
        except Exception:
            continue

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(len(out))


if __name__ == "__main__":
    main()
