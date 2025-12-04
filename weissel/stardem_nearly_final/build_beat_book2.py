#!/usr/bin/env python3
"""
Build a sports beat book from a JSON collection of high-school sports stories.

This script is a sports-focused variant that defaults to using
`sports2024highschool.json` and `combined/prompt_sport_combine.txt` (if present).

It supports a `--dry-run` mode that validates the JSON and prompt formatting
without calling any LLMs. For full runs it uses the `uv` CLI to call a Groq
model and the Anthropic client for Claude refinement (both optional and
lazy-imported so dry-run works without them).
"""
import json
import subprocess
import argparse
import time
import random
import os
import re
from pathlib import Path
from datetime import datetime

try:
    from dotenv import load_dotenv
except Exception:
    def load_dotenv():
        print("Warning: 'python-dotenv' not installed; skipping .env loading. Set environment variables directly if needed.")

# Load environment variables (noop if python-dotenv missing)
load_dotenv()


SPORTS_BEAT_PROMPT = """You are creating a comprehensive "beat book" for a new reporter covering high-school sports in Caroline County, Maryland for the Easton Star-Democrat.

<context>
Today is {current_date}.

You are being shown stories in batches of {batch_size} at a time from a total collection of {total_stories} sports stories. This is batch {batch_num} of {total_batches}. Your job is to INTEGRATE and EXPAND the sports beat book based on what you learn from these new stories.

CRITICAL FOCUS: This beat book is ONLY about high-school sports in Caroline County, MD. EXCLUDE and IGNORE any information about other counties.

The current beat book below already contains information from {processed_count} previously analyzed stories. Your task is to ADD to and ENRICH this existing content, NOT replace it.
</context>

<current_beat_book>
{current_beat_book}
</current_beat_book>

<new_stories>
{stories}
</new_stories>

<instructions>
- Add new teams, coaches, athletic directors, and institutions IN CAROLINE COUNTY
- Expand recurring themes (funding, facilities, participation trends) with local examples
- Suggest meaningful story angles for sports coverage specific to Caroline County
- Preserve and build on existing beat book content
- If stories are primarily about other counties, SKIP them
</instructions>

<output_format>
If no update needed: "NO UPDATE NEEDED"
If updating: Return the COMPLETE updated beat book as Markdown (no preamble)
</output_format>"""


TEMPLATE_SCAFFOLD = """
--BEAT BOOK TEMPLATE SCAFFOLD (REQUIRED STRUCTURE)--

# Opening Narrative
- Short overview of the beat, key themes, and what matters locally.

# Core Beat Responsibilities
- Weekly Workflow Foundation (provide a short table with columns: Task | Frequency | Who | Notes)

# Travel & Logistics
- How reporters cover multiple games, transportation notes, and contact lists.

# Building & Maintaining Sources
- Lists of coaches, athletic directors, AD contacts, and local boosters.

# Story Structure: 5-W-1-H + Quote + Stat
- Show a brief template/example for match/game stories.

# Essential Story Types
- Game Recaps
- Feature Profiles
- Season Previews
- Postseason Coverage

# Data & Stats
- Key stats to collect for each sport and where to find them.

# Ethical & Permission Notes
- Note on athlete privacy, minors, and photo/video permissions.

# Sport-Specific Sections
For each sport include subsections:
- Rules & How the Game Works
- Key Stats
- What Decides Games
- Positions & Terminology
- What to Watch For
- Interview Tips
- Story Angles

# Appendix / Templates
- Contact spreadsheet columns, sample outreach email, and game checklist.

Return the full beat book in Markdown, using all sections above and filling with local examples when available.
"""


def load_prompt_template_from_file():
    """Load `combined/prompt_sport_combine.txt` next to this script if present."""
    try:
        p = Path(__file__).parent / 'combined' / 'prompt_sport_combine.txt'
        if p.exists():
            # Append the required scaffold so the model outputs the expected structure
            base = p.read_text(encoding='utf-8')
            return base + "\n\n" + TEMPLATE_SCAFFOLD
    except Exception:
        pass
    # If no external prompt, combine the built-in prompt and the scaffold
    return SPORTS_BEAT_PROMPT + "\n\n" + TEMPLATE_SCAFFOLD


def reformat_with_claude_to_template(text, template_scaffold):
    """If Claude is available, ask it to reformat `text` to exactly follow `template_scaffold`.
    Returns the reformatted text or the original text on failure.
    """
    client = try_load_anthropic_client()
    if client is None:
        return None
    prompt = (
        "Please reformat the following beat book text so it exactly follows this Markdown template:\n\n"
        + template_scaffold
        + "\n\nSOURCE DOCUMENT:\n" + text
        + "\n\nReturn only the complete reformatted Markdown document."
    )
    try:
        response = client.messages.create(model='claude-sonnet-4-5-20250929', messages=[{'role':'user','content':prompt}])
        out = ''
        for block in response.content:
            if block.type == 'text':
                out += block.text
        return out.strip() or None
    except Exception:
        return None


def ensure_minimum_structure(beat_text, template_scaffold):
    """Lightweight fallback: ensure key headings exist in beat_text. Returns modified text.
    This is used when Claude is not available.
    """
    required_heads = [
        '# Opening Narrative',
        '# Core Beat Responsibilities',
        '# Travel & Logistics',
        '# Building & Maintaining Sources',
        '# Story Structure: 5-W-1-H + Quote + Stat',
        '# Essential Story Types',
        '# Data & Stats',
        '# Ethical & Permission Notes',
        '# Sport-Specific Sections',
        '# Appendix / Templates'
    ]
    out = beat_text or ''
    for h in required_heads:
        if h not in out:
            out += '\n\n' + h + '\n\n' + '_(Add content here — model did not produce this section.)_'
    return out


def validate_input_json(path, required_keys=None, sample_count=1):
    if required_keys is None:
        required_keys = ['title', 'date', 'content']
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input JSON not found: {path}")
    with open(p, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Input JSON must be an array of story objects")
    if len(data) == 0:
        raise ValueError("Input JSON contains no stories")
    for i, item in enumerate(data[:100]):
        if not isinstance(item, dict):
            raise ValueError(f"Story at index {i} is not an object")
        for key in required_keys:
            if key not in item:
                raise ValueError(f"Story at index {i} missing required key: {key}")
    return data, data[:sample_count]


def format_stories_for_prompt(stories_batch):
    return "\n\n---\n\n".join([
        f"STORY {i+1}:\nTitle: {story.get('title')}\nDate: {story.get('date')}\nContent: {story.get('content')}"
        for i, story in enumerate(stories_batch)
    ])


def update_beat_book_with_groq(prompt_text):
    """Call the Groq model via `uv run llm ...` (assumes `uv` is configured).
    Returns the model response text or raises on failure.
    """
    try:
        result = subprocess.run(
            ['uv', 'run', 'llm', '-m', 'groq/openai/gpt-oss-120b', '-o', 'max_tokens', '2048', prompt_text],
            capture_output=True,
            text=True,
            check=True,
            timeout=180
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Groq model call failed: {e.stderr}")


def try_load_anthropic_client():
    try:
        from anthropic import Anthropic
    except Exception:
        return None
    return Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))


def refine_with_claude(previous_refined, latest_groq, batch_num, total_batches, processed_count, total_stories):
    client = try_load_anthropic_client()
    if client is None:
        print("Claude client not available (install 'anthropic') — skipping refinement")
        return previous_refined
    # Build refine prompt using a simple wrapper; here we reuse the latest_groq as input
    current_date = datetime.now().strftime('%B %d, %Y')
    prompt = f"Refine the following sports beat book (date: {current_date}).\n\nPREVIOUS_REFINED:\n{previous_refined}\n\nLATEST_DRAFT:\n{latest_groq}\n\nReturn the full refined beat book."
    response = client.messages.create(model='claude-sonnet-4-5-20250929', messages=[{'role':'user','content':prompt}])
    # Extract text blocks
    out = ''
    for block in response.content:
        if block.type == 'text':
            out += block.text
    return out.strip() or previous_refined


def main():
    parser = argparse.ArgumentParser(description='Build a sports beat book (high-school sports)')
    default_input = str(Path(__file__).parent / 'sports2024highschool.json')
    parser.add_argument('--input', default=default_input, help=f'Input JSON (default: {default_input})')
    parser.add_argument('--state', default='sports_beat_book1_state.json', help='State file')
    parser.add_argument('--output', default='sports_beat_book1.md', help='Groq beat book output')
    parser.add_argument('--refined-output', default='sports_beat_book1_refined.md', help='Claude refined output')
    parser.add_argument('--batch-size', type=int, default=20)
    parser.add_argument('--delay', type=int, default=2)
    parser.add_argument('--dry-run', action='store_true', help='Validate JSON + prompt and exit')
    args = parser.parse_args()

    if args.dry_run:
        try:
            stories, samples = validate_input_json(args.input)
            print(f"Input JSON OK — {len(stories)} stories. Showing 1 sample:\n")
            s = samples[0]
            print('---')
            print(f"Title: {s.get('title')}")
            print(f"Date: {s.get('date')}")
            print(f"Content (first 500 chars):\n{s.get('content','')[:500]}\n")
            prompt_template = load_prompt_template_from_file()
            print(f"\nLoaded prompt template length: {len(prompt_template)} chars")
            # Test formatting
            test_values = {
                'current_date': datetime.now().strftime('%B %d, %Y'),
                'batch_num': 1,
                'total_batches': 1,
                'total_stories': len(stories),
                'batch_size': min(20, len(stories)),
                'processed_count': 0,
                'current_beat_book': '# Sports Beat Book - Test',
                'stories': 'STORY 1: Title: Test'
            }
            try:
                preview = prompt_template.format(**test_values)
                print('\nPrompt formatted successfully. Preview (first 1000 chars):\n')
                print(preview[:1000])
            except KeyError as ke:
                print(f"Prompt missing placeholder: {ke}")
                raise
            print('\nDry-run succeeded — no LLMs were contacted.')
            return
        except Exception as e:
            print(f"Dry-run failed: {e}")
            return

    # Non-dry run: minimal pipeline
    stories, _ = validate_input_json(args.input)
    total_stories = len(stories)
    # Shuffle and process in batches
    indices = list(range(total_stories))
    random.shuffle(indices)
    total_batches = (total_stories + args.batch_size - 1) // args.batch_size
    beat_book = '# Sports Beat Book\n\n(This document will be built iteratively.)'
    refined_book = beat_book
    prompt_template = load_prompt_template_from_file()

    for batch_num, i in enumerate(range(0, total_stories, args.batch_size), start=1):
        batch_indices = indices[i:i+args.batch_size]
        stories_batch = [stories[idx] for idx in batch_indices]
        stories_text = format_stories_for_prompt(stories_batch)
        prompt_text = prompt_template.format(
            current_date=datetime.now().strftime('%B %d, %Y'),
            batch_num=batch_num,
            total_batches=total_batches,
            total_stories=total_stories,
            batch_size=len(stories_batch),
            processed_count=(batch_num-1)*args.batch_size,
            current_beat_book=beat_book,
            stories=stories_text
        )
        print(f"Sending batch {batch_num}/{total_batches} to Groq...")
        try:
            updated = update_beat_book_with_groq(prompt_text)
            if updated and updated != 'NO UPDATE NEEDED':
                # Try to reformat to the exact scaffold using Claude (best-effort)
                reformatted = reformat_with_claude_to_template(updated, TEMPLATE_SCAFFOLD)
                if reformatted:
                    beat_book = reformatted
                    print('Reformatted Groq output using Claude to match scaffold.')
                else:
                    # Fallback: ensure minimum headings are present
                    beat_book = ensure_minimum_structure(updated, TEMPLATE_SCAFFOLD)
                    print('Applied lightweight scaffold fallback to Groq output.')

                Path(args.output).write_text(beat_book, encoding='utf-8')
                print(f"Saved Groq draft to {args.output}")
            else:
                print('Groq returned NO UPDATE NEEDED for this batch')
        except Exception as e:
            print(f"Groq step failed: {e}. Skipping refinement for this batch.")
            continue

        # Try Claude refinement (best-effort)
        refined = refine_with_claude(refined_book, beat_book, batch_num, total_batches, batch_num*args.batch_size, total_stories)
        if refined:
            refined_book = refined
            Path(args.refined_output).write_text(refined_book, encoding='utf-8')
            print(f"Saved refined beat book to {args.refined_output}")

        time.sleep(args.delay)

    print('All batches processed (or attempted).')


if __name__ == '__main__':
    main()
