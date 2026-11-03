# Under50

An agent skill that forces a hard triage rule: compress any long document into a brief of **50 words or fewer** - the core point, the decisive figures, and the action it needs - so you can decide in about 15 seconds whether the full document deserves your time.

Built for reading relief in a world where AI generates far more text than anyone can read.

## What is in this repo

- `SKILL.md` - the skill instructions (the actual product)
- `word_counter.py` - the word-count standard (markdown markers stripped)
- `tests/` - 14 fixture-based unit tests
- `references/` - research notes, worked before/after example, quality grading notes

## How to use it

**Claude** (or any agent that loads skills): copy the `under50` folder into your skills directory.

**Gemini**: create a Gem and paste the contents of `SKILL.md` as its instructions, then invoke it with `@yourgemname`. Or paste `SKILL.md` into a fresh chat and send: "Follow this skill exactly from now on."

Then, with any document:

```
Using the loaded skill, triage the following document in 50 words or fewer. Reply with only the brief.
```

## Honest status

This is an experimental personal project, shared so people can try it and push on it - not because it is proven.

- The automated suite passes 14/14, but those tests only check word counts on fixed example strings. They do not run an agent.
- In the first blind A/B pair (one real public regulatory document, with skill vs without, same model), the with-skill output had cleaner bullet formatting but was slightly *worse* on factual fidelity than the plain baseline. A wider paired test set (two more real documents, with and without the skill) is prepared but currently paused.
- Under50 is a triage read, not a summary. Non-essential detail is deliberately dropped; never rely on it where the full document matters.

## Why 50 words

50 words is a product rule, not a scientific law. Brysbaert (2019, meta-analysis of 190 studies) puts average adult English nonfiction reading speed at 238 words per minute, so 50 words is roughly a 13-15 second read. Morkes & Nielsen (1997) found the combined concise + scannable + objective rewrite of promotional web prose improved measured usability by 124% (concise wording alone: 58%). Whether those 1997 web-writing results transfer to markdown triage is an assumption, not a tested result. See `references/research.md`.

## Running the tests

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT - see `LICENSE`.
