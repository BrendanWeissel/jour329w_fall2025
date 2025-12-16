
# Copilot Conversation Narrative

This Copilot conversation started as a very practical “make something usable” problem and gradually turned into a bigger workflow: collecting stories, cleaning/filtering them, enriching them with metadata, browsing them in Datasette, and then writing a beat book process guide that could help someone else do the same thing.

## Phase 1: Turning a beat book into a usable website

The first goal was to take a long sports beat book written in Markdown and turn it into a single-page website that a reporter could use quickly. The key UX requirement was simple: the website needed dropdown/collapsible sections (one per sport) so it wasn’t just a wall of text.

To do that, Copilot helped create a Python script that:

- reads a Markdown file (the beat book source)
- breaks it into sport-specific sections
- converts those sections to HTML
- writes out a self-contained HTML page with basic navigation and collapsible UI

Along the way, a real-world templating bug showed up: Python string formatting collided with CSS braces in the HTML template. That caused a runtime KeyError. The fix was to escape braces in the template so formatting only happened where it was intended.

The other big problem in this phase was a content problem, not a code problem: the site looked “empty” because the parser wasn’t grabbing full sections reliably. We adjusted the parsing to match the actual headings in the Markdown (for example, sections like “## Baseball Beat Guide”), and to capture everything up to the next sport heading.

Finally, because this work happened in a dev container / Codespace-style environment, opening a local file directly in a browser wasn’t reliable. The solution was to serve the generated HTML over a local port using a tiny HTTP server script, so the page could be viewed via a normal http://localhost URL.

## Phase 2: Using LLM prompts for record-book analysis (and designing for failure)

After the website work, the focus shifted to using an LLM prompt workflow to extract information from large text inputs (for example, record-book text files generated from PDFs). The original “all at once” approach was brittle: large prompts could time out, error, or return partial/empty output.

To make the workflow more reliable, Copilot helped reorganize the process into smaller runs (splitting by season, for example Fall/Spring/Winter), then combining the outputs into one final document. The major lesson here was that prompt workflows need the same engineering mindset as code:

- chunk large inputs
- write outputs to files every step
- capture stderr so failures are visible
- combine outputs only after confirming each part succeeded

## Phase 3: Datasette, counts, and “trust but verify”

Another recurring theme in the conversation was verification. It’s easy to assume “the script ran” means “the result is correct.” So we kept coming back to simple validation checks:

- count how many stories are in a JSON file
- confirm that what’s in a database matches what’s in the source file

This became especially relevant with Datasette. The goal was to browse stories through a real interface (search, filter, inspect records) instead of reading raw files. When there was confusion about how to open URLs (typing a URL into the terminal instead of a browser), Copilot clarified the difference and created helper scripts to make launching Datasette repeatable.

## Phase 4: Writing the beat book process guide (and making it readable)

The last major stage of the conversation was driven by the assignment prompt in [assignments/beat_book_process.md](assignments/beat_book_process.md): write a non-technical “How To” guide, and then end the conversation by creating a narrative summary in a file called copilot.md.

Copilot helped build and iteratively revise the guide in [weissel/beat_book_process/guide_notes.md](weissel/beat_book_process/guide_notes.md). The guide went through multiple improvements based on feedback:

- First draft: a straightforward step-by-step workflow.
- Revision: lean much more heavily on what actually happened (successes and failures).
- Revision: add direct quotes from the process notes, but keep it short.
- Revision: rewrite it to a general audience (not written as “you should…” to the author).
- Revision: step back and explain why a beat book is useful, especially for onboarding: “To help new reporters in a news room”.
- Revision: simplify jargon (“corpus” became “the pile of stories”), remove overly detailed sub-sections, and generalize beyond sports.
- Revision: expand metadata explanations, including what “good metadata” means and why a stable schema matters.
- Revision: add an example of a specific beat definition (a local government beat) so readers can see what “enough detail” looks like.

One of the most important structural decisions was changing “What didn’t / struggle” into “Trial notes.” That made the document feel more like an honest lab notebook: what was tried, what worked, what broke, and what would be changed next time.

## Where the required files are

This assignment requires the guide to live in the beat_book_process directory. The guide is included here:

- [weissel/beat_book_process/guide_notes.md](weissel/beat_book_process/guide_notes.md)

And this narrative summary is included here:

- [weissel/beat_book_process/copilot.md](weissel/beat_book_process/copilot.md)

## The through-line: building a workflow, not just a document

The biggest theme across the whole conversation was that a beat book isn’t just a writing assignment. It’s an output of a workflow:

- define the beat clearly
- build the dataset
- filter it in layers
- add consistent metadata (schema-driven)
- validate counts early
- browse the result to spot issues
- write a beat book that helps someone new succeed on day one

That mindset—designing for reruns, partial failures, and verification—was the most valuable “Copilot lesson” that carried through every phase of the work.
