# How to Make a Beat Book (General Guide + Trial Notes)

This writeup is based on the scripts in `weissel/beat_book_process/` and the process notes in `notes.md`, but it’s written to be useful for any beat (schools, local government, courts, business, environment, sports, etc.).

Direct quotes below are copied verbatim from the process notes.

## Why a beat book is useful

A beat book is a practical “how this beat works” reference. It reduces ramp-up time, prevents repeated mistakes, and helps reporters make better decisions under deadline pressure.

In a newsroom, the core purpose is simple: “To help new reporters in a news room”.

## 1) Define the beat (what the beat *is*)

A good beat definition is specific enough that two different reporters would make similar choices about what to cover.

**Beat definition checklist (keep it short, but complete):**

- **Topic scope:** what counts as “in” vs “out” (include 2–3 examples of each)
- **Geography:** the map (city/county/region, plus any edge cases)
- **Time window:** ongoing vs a specific period (e.g., “2024 only”)
- **Primary audience:** who this is for (new reporter, general reader, policymakers, parents, etc.)
- **Key stakeholders:** the institutions/people that show up repeatedly
- **Recurring calendar:** meetings, seasons, deadlines, annual events
- **Story formats:** what this newsroom typically publishes on this beat (recaps, previews, explainers, investigations, profiles)
- **Success criteria:** what “done” means (dataset + beat book + a way to browse/search)

**Example beat definition (local government):**

- **Topic scope (in):** county council + budget + zoning/land use + major contracts
- **Topic scope (out):** state/federal politics unless it directly impacts the county; opinion columns
- **Geography:** Talbot County; include towns within Talbot; exclude neighboring counties unless a shared issue (regional transit, watershed)
- **Time window:** ongoing, but keep a “this year” view for budget season
- **Primary audience:** new reporter on deadline + residents trying to understand decisions
- **Key stakeholders:** council members, county manager, planning/zoning staff, major developers, school board when budgets overlap
- **Recurring calendar:** council meetings, work sessions, budget hearings, election filing deadlines
- **Story formats:** meeting recaps, explainers (what a vote means), accountability checks (promises vs outcomes), quick-turn breaking news
- **Success criteria:** searchable dataset + a beat book that explains the process + a browsing tool (Datasette) to spot patterns

**Trial notes (what happened in practice):**

- When scope wasn’t enforced early, filtering drifted and cleanup work grew.

## 2) Build the dataset (stories in a consistent format)

Think of this as “the pile of stories that will feed the beat book.”

**Action:** Put stories into one JSON array file where each story is one object.

Minimum useful fields:

- `title`
- `date` (or `year/month/day`)
- `content` (or a summary)
- a stable ID (`article_id` is ideal)

**Trial notes:**

- Process notes: “I modified the data so that I have 240 stories (20 from each month)… I suspect this will give me a better sense of the yearround coverage from the Stardemocrat.”
- Even sampling is only helpful if the selection step is accurate; otherwise it becomes an even sample of the wrong material.

## 3) Filter in layers (save time and improve accuracy)

Filtering is the most important “engineering” step because it prevents wasting time (and LLM calls) on stories that don’t belong in the beat.

**Action (general pattern):**

1) **Deterministic filters:** rules that should never change (time window, source publication, required fields)
2) **Heuristic filters:** fast keyword/scoring rules for obvious out-of-scope material and junk formats (listings, transactions, roundups with no reporting)
3) **Optional LLM filter:** only after the dataset is already mostly correct


**Trial notes:**

- Removing “TV listings” and other junk took multiple tries because (LLM) filters can remove too much or too little.

## 4) Add metadata (what it is, why it matters, and how to do it)

Metadata is the structured information added to each story so the dataset can be searched, faceted, and summarized (without rereading every story).

**What good metadata looks like:**

- **Consistent:** the same keys exist on every record
- **Predictable:** values come from small, repeatable categories (good for charts and filters)
- **Actionable:** it answers real beat questions (who/what/where/so-what)

Examples (works for almost any beat):

- `metadata_topic` (or beat category)
- `metadata_story_type` (recap/explainer/profile/investigation/etc.)
- `metadata_locations`
- `entities_people`, `entities_orgs`
- `entities_quoted_people`
- `metadata_audience_blurb` (who would care, stated plainly)

**How the process works (script + schema):**

- Define a **schema** (the exact keys and the allowed value formats).
- Run a script (example: `add_entities.py`) that reads JSON stories, prompts a model to fill the schema, and writes an enriched JSON output.
- Validate that every record has the required keys, then rerun only failures.

**What a metadata script needs:**

- an input JSON file + an output path
- a schema definition (required keys + allowed formats)
- a prompt/template that instructs the model to fill the schema
- retry/error handling (LLMs fail sometimes)
- basic validation (missing keys, empty values, malformed JSON)

**Why schema matters:**

- If the schema changes midstream, fields can disappear or change shape and downstream steps (counts, Datasette import) break.

**Trial notes:**

- “Other than the fact that this took about 2 hours to run I was very pleased with the results.”

## 5) Validate early (counts catch mistakes)

After filtering + metadata, run quick checks:

- total record count
- count by month
- count by `metadata_story_type`
- count by topic/category
- missing-field counts (how often key fields are blank)

## 6) Browse it (Datasette is a fast reality check)

Loading the dataset into Datasette makes it easy to search, facet, and spot weird records quickly.

- Script: `import_to_datasette.py`
- Output: a `.db` with full-text search

**Trial notes:**

- Process notes: “it said all 247 stories ran but only 41 appeared in the datasette.”
- Always check that the JSON length matches the DB row count.

## 7) Write the beat book (two formats)

Two formats work well for almost any beat:

1) **Narrative onboarding guide:** the “how this beat works” memo (what matters, who matters, what happens when, what good coverage looks like)
2) **Reference-first guide:** templates + checklists + “where to look” lists for deadline use

This repo also includes a batch-writing pattern (`Build_beat_book.py`) that prompts a model to preserve and expand a running document instead of rewriting it from scratch.

### What makes a good beat-book prompt (accurate, not just “nice sounding”)

When an LLM writes a beat book, the biggest risk is not grammar—it’s **making up details**. A strong prompt is built to reduce hallucination by forcing the model to stay grounded in the story set.

**Prompt checklist:**

- **Define the beat again (briefly):** one paragraph summarizing scope, geography, and time window.
- **Specify the input:** tell the model what it is receiving (full text stories, summaries, metadata tables, or a mix).
- **Forbid guessing:** if something is not present in the input, the model must say “Not found in provided stories.”
- **Require evidence:** ask for 2–5 short bullet “evidence notes” per section (titles/dates/IDs if available).
- **Make it additive:** if writing in batches, require “preserve and expand; do not delete prior content unless directly contradicted.”
- **Separate “facts” from “advice”:** facts must be grounded in the dataset; advice can be generalized but should be labeled as guidance.
- **Choose a consistent structure:** headings + short bullets beat long prose for newsroom use.

### Prompt templates (copy/paste)

These are intentionally generic so they work for non-sports beats.

**Template A: Narrative onboarding beat book (grounded + readable)**

Paste this above a batch of story text (or a set of story summaries + metadata):

"""
You are writing a BEAT BOOK for a newsroom.

Beat definition:
- Topic scope: <IN/OUT in one sentence each>
- Geography: <place>
- Time window: <range>
- Primary audience: new reporter starting this beat

Input:
You will receive a list of stories with some combination of: title, date, ID, summary, and/or full text.

Rules for accuracy:
- Use ONLY information that appears in the provided stories.
- Do NOT guess names, numbers, outcomes, or processes not explicitly stated.
- If information is missing, write: "Not found in provided stories."

Task:
Write a beat book that helps a new reporter succeed in week 1.

Required sections:
1) What this beat covers (and what it does NOT cover)
2) Key stakeholders and institutions (only if they appear in stories; otherwise say Not found)
3) The beat calendar (recurring events and when news tends to happen, based on story dates)
4) Common story types and what they look like here
5) Fast background: key terms or recurring issues (define in plain language)
6) Reporting workflow: what to check first, who to call first (only if supported by stories)

Evidence requirements:
- After each section, include an "Evidence" sub-bullet list with 2–5 story references (title/date/ID if available) that support the claims in that section.

Style:
- Plain language, short paragraphs, bullet points.
"""

**Template B: Reference-first beat book (deadline-friendly)**

"""
You are writing a REFERENCE-FIRST beat book for a newsroom.

Beat definition:
<same as above>

Rules for accuracy:
- Use ONLY information from the provided stories.
- Do NOT guess; use "Not found in provided stories." when needed.

Output format (use these headings exactly):
1) Quick definitions (key terms that appear in coverage)
2) Who’s who (people/orgs mentioned often)
3) Where to look (documents, meetings, recurring events mentioned)
4) Story templates (fill-in-the-blank outlines for the common story types in this dataset)
5) Red flags (common points of confusion or mistakes new reporters make, based on what the stories suggest)
6) Verification checklist (what to confirm before publishing)

Evidence requirements:
- Under each heading, add a short "Evidence" list of story references.

Keep it scannable:
- bullets over paragraphs
- avoid opinionated language
"""

**Template C: Batch update prompt (preserve + expand)**

Use this when feeding stories in chunks:

"""
You are updating an existing beat book.

Inputs:
1) CURRENT_BEAT_BOOK (markdown)
2) NEW_STORIES (a batch of story summaries/text)

Rules:
- Preserve the existing structure and content.
- Add new details only when supported by NEW_STORIES.
- If NEW_STORIES contradicts CURRENT_BEAT_BOOK, flag it in a "Potential conflicts" section.
- Do NOT remove large sections; only edit for factual corrections.

Output:
- Return the UPDATED_BEAT_BOOK in markdown.
- Add an "Evidence" list of story references for any new claims.
"""

**Trial notes:**

- Process notes: “Cleaning up the data is not that important becasue I can just facet by High School.” (The general lesson: when faceting is strong, perfect cleaning is less critical.)
- “For people quoted not every person quoted was given a title which I would like to clean up in the future.”

## 8) Iterate (the workflow loop)

1) Build the dataset
2) Filter in layers
3) Add metadata (schema-driven)
4) Validate counts
5) Browse in Datasette
6) Write/revise beat book

Each step should produce an output file that can be kept even if the next step fails.

## 9) What “done” looks like

Done looks like:

- a filtered dataset that matches the beat definition
- metadata that supports search and faceting
- a browsing tool (Datasette) where record counts match
- a beat book that a new reporter could use on day one


