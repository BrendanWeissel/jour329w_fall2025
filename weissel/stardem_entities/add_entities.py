import json
import re
import subprocess
import time
import argparse
import sys
from pathlib import Path

def extract_metadata(story_title, story_content, schema_prompt, model):
    """Use LLM to extract structured metadata from story title and summary."""
    prompt = f"""
Extract metadata from this news story in JSON format using only the title and summary provided.

Schema to follow:
{schema_prompt}

Story Title: {story_title}
Story Summary: {story_content}

Return only valid JSON with the metadata. If information is not available, use an empty array:
"""
    
    try:
        result = subprocess.run([
            'llm', '-m', model, prompt
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            # Parse and validate the JSON response
            response_text = result.stdout.strip()
            # Remove any markdown code blocks if present
            if response_text.startswith('```'):
                response_text = response_text.split('\n', 1)[1]
                response_text = response_text.rsplit('\n', 1)[0]
            
            metadata = json.loads(response_text)
            return metadata
        else:
            return {"error": "LLM failed", "stderr": result.stderr}
    except Exception as e:
        return {"error": str(e)}

def main():
    parser = argparse.ArgumentParser(description='Add metadata to CNS beat stories using LLM')
    parser.add_argument('--model', required=True, help='LLM model to use (e.g., gpt-4o-mini, claude-3.5-haiku)')
    parser.add_argument('--input', default='story_summaries_elections.json', help='Input JSON file with stories')

    # Show help if no arguments provided
    if len(sys.argv) == 1:
        parser.print_help()
        return

    args = parser.parse_args()

    # Define your schema prompt based on your beat - CUSTOMIZE THIS!
    # Make keys lowercase, use underscores and provide example values so the LLM
    # returns consistent field names (this helps avoid duplicate/variant columns).
    # We want the LLM to extract three arrays: people, places, organizations.
    # Provide an explicit example in the schema so the model returns consistent keys
    # and short name tokens. The LLM should return JSON like the example.
    schema_prompt = """
        {
            "people": ["First Last", "Another Person"],
            "places": ["Town, State", "Organization Location"],
            "organizations": ["Organization Name", "Agency"]
        }

        IMPORTANT: For `people` return ONLY very important people — the primary
        named sources, elected officials, victims/defendants, key witnesses, or the
        main subjects of the story. Do NOT include the author/byline, long rosters,
        or passing mentions. Keep the people list focused and short.

        For `places` return the most relevant place names (town, county, or
        location) and LIMIT the array to at most 3 items (most relevant first).

        For `organizations` include organizations directly relevant to the story.

        Example (desired output for a short story):
        {
            "people": ["Mayor Jane Doe", "John Smith"],
            "places": ["Easton, MD", "Queen Anne's County"],
            "organizations": ["Star Democrat", "Queen Anne's County Commissioners"]
        }
        """

    # Load your beat stories
    try:
        with open(args.input) as f:
            stories = json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find input file '{args.input}'")
        print("Make sure to update the --input parameter to match your topic file!")
        return

    # Process each story
    enhanced_stories = []
    for i, story in enumerate(stories):
        print(f"Processing {i+1}/{len(stories)}: {story.get('title', '<no title>')}")

        # prefer full article content when available
        story_content = story.get('content') or story.get('summary') or ''
        metadata = extract_metadata(story.get('title', ''), story_content, schema_prompt, args.model)

        # Add metadata fields as separate columns instead of nested object
        enhanced_story = story.copy()

        # If metadata extraction was successful, add people/places/organizations as JSON arrays
        if isinstance(metadata, dict) and 'error' not in metadata:
            # expected entity keys
            for key in ('people', 'places', 'organizations'):
                val = metadata.get(key, [])
                # ensure it's a list
                if not isinstance(val, list):
                    # if the model returned a single string, wrap it
                    if isinstance(val, str) and val.strip():
                        val = [v.strip() for v in re.split(r'[;,]\s*', val) if v.strip()]
                    else:
                        val = []

                # Post-process to enforce policy: prioritize important people,
                # limit places to 3, and keep organizations as returned.
                if key == 'people':
                    # Remove the author/byline if present
                    author = story.get('author') or story.get('byline') or ''
                    def normalize_name(n):
                        return n.strip()

                    # dedupe while preserving order
                    seen = set(); deduped = []
                    for x in val:
                        k = normalize_name(x)
                        if not k: continue
                        if author and k.lower() == author.strip().lower():
                            continue
                        if k not in seen:
                            seen.add(k); deduped.append(k)

                    # simple prioritization: prefer entries containing role/title
                    role_words = ('Mayor', 'Senator', 'Representative', 'Judge', 'Dr', 'Mr', 'Mrs', 'Ms', 'Chief', 'Sheriff', 'Officer', 'Coach', 'President', 'Principal')
                    story_text = (story.get('title') or '') + '\n' + (story_content or '')

                    def person_score(name, idx):
                        score = 0
                        lname = name.lower()
                        st = story_text.lower()
                        # role/title presence is a strong signal
                        for rw in role_words:
                            if rw.lower() in name.lower():
                                score += 4
                        # frequency of mentions is important
                        freq = st.count(lname)
                        score += min(freq, 5) * 1.5
                        # earlier appearance is better
                        pos = st.find(lname)
                        if pos != -1:
                            # earlier -> higher score
                            score += max(0, 3 - (pos / 200.0))
                        # shorter names slightly preferred
                        score += max(0, 1 - (len(name.split()) - 2) * 0.1)
                        return (-score, idx)

                    scored = sorted([(person_score(p, i), p) for i, p in enumerate(deduped)], key=lambda x: x[0])
                    prioritized = [p for _, p in scored]
                    # Keep only likely human first+last names (two tokens, capitalized)
                    def is_human_name(n):
                        # Allow letters, hyphens and apostrophes in names
                        m = re.match(r"^[A-Z][A-Za-z'\-]+\s+[A-Z][A-Za-z'\-]+$", n)
                        if not m:
                            return False
                        # exclude organization-like tokens
                        org_tokens = ('County','School','District','Commission','Commissioners','Board','Department','Inc','Company','Association','Committee','Publishing','Press','Times','Record','Observer','News','Document')
                        for t in org_tokens:
                            if t in n:
                                return False
                        # filter out likely team/place fragments that look like two words
                        block_words = ('High','School','Conference','Athletic','Saints','Royals','Bucs','Sabres','Kings','Lady','Saint','Team','Delmarva','Star','Democrat','Christian','Eastern','Shore','Independent','Publishing','Press','Times','Record','Observer','News','Document')
                        for part in n.split():
                            if part in block_words:
                                return False
                        return True

                    human_only = [p for p in prioritized if is_human_name(p)]
                    # Keep ONLY human-looking first+last names; if none found, leave empty
                    val = human_only[:4]

                if key == 'places':
                    # dedupe and keep only the top 3 places (most relevant)
                    seen = set(); places_ordered = []
                    for p in val:
                        k = p.strip()
                        if not k: continue
                        if k not in seen:
                            seen.add(k); places_ordered.append(k)
                    val = places_ordered[:3]

                # write out as JSON string in the story record
                enhanced_story[f'entities_{key}'] = json.dumps(val)
            # keep any additional fields (optional) as metadata_ prefixed columns
            for key, value in metadata.items():
                if key not in ('people', 'places', 'organizations'):
                    norm_key = key.strip().lower().replace(' ', '_').replace('-', '_')
                    col_name = f'metadata_{norm_key}'
                    enhanced_story[col_name] = json.dumps(value) if isinstance(value, list) else value
        else:
            # If there was an error, add error information
            enhanced_story['metadata_error'] = (metadata.get('error') if isinstance(metadata, dict) else str(metadata)) or 'Unknown error'

        enhanced_stories.append(enhanced_story)

        # Be respectful to the API
        time.sleep(1)

    # Save the enhanced collection (stories_with_entities.json per assignment)
    with open('stories_with_entities3.json', 'w') as f:
        json.dump(enhanced_stories, f, indent=2)

    print(f"Processed {len(enhanced_stories)} stories with metadata")

if __name__ == "__main__":
    main()
