# Under50

An agent skill that forces a hard triage rule: compress any long document into a brief of **50 words or fewer** - the core point, the decisive figures, and the action it needs - so you can decide in about 15 seconds whether the full document deserves your time.

Built for reading relief in a world where AI generates far more text than anyone can read.

## What is in this repo

- `SKILL.md` - the skill instructions (the actual product)
- `word_counter.py` - the word-count standard (markdown markers stripped)
- `tests/` - 14 fixture-based unit tests
- `tests/triggering/` - skill-firing test pack: prompts, runner and scoring for measuring whether the skill gets loaded at all
- `references/` - research notes, worked before/after example, quality grading notes

## How to use it

**Claude** (or any agent that loads skills): copy the `under50` folder into your skills directory.

**Gemini**: create a Gem and paste the contents of `SKILL.md` as its instructions, then invoke it with `@yourgemname`. Or paste `SKILL.md` into a fresh chat and send: "Follow this skill exactly from now on."

Then, with any document:

```
Using the loaded skill, triage the following document in 50 words or fewer. Reply with only the brief.
```

## Getting the skill to fire

Skills do not fire reliably on their own. In a measured test of 26 public skills (1,872 Claude Code runs, [Towards Data Science, 10 Nov 2026](https://towardsdatascience.com/a-session-start-hook-raised-claude-code-skill-firing-from-15-to-62/)), an indirect request - one that needs the skill but uses none of its words - loaded the right skill only 15% of the time. Direct requests in the skill's own words fired 49%. The experiment measured two fixes:

- **Pushy description** (already applied to `SKILL.md`): one sentence in the form Anthropic's skill-creator recommends ("Make sure to use this skill whenever ...") added about 5 points on indirect requests and 8 on direct ones. Small, free, already in.
- **Session-start hook**: a hook that tells the agent at session start to check its skills before anything else raised indirect firing from 15% to 62% in that test. Caveats: one plugin's hook, one harness, one day - treat the number as directional, and near-miss requests loaded neighboring skills more often with the hook on (75 of 324 runs vs 43 without). Claude Code has no native "invoke skill X at session start" setting ([anthropics/claude-code#65371](https://github.com/anthropics/claude-code/issues/65371), closed unimplemented as stale). The user-side equivalent is a line in your `CLAUDE.md`, for example:

  ```
  Before answering anything, check whether an installed skill applies. For any long document, invoke the under50 skill first.
  ```

- **Guaranteed**: invoke the skill directly with `/under50` instead of relying on automatic firing.

To measure firing on your own setup, use the trigger test pack in `tests/triggering/` - same equivalence-class method as the experiment above.

## Honest status

This is an experimental personal project, shared so people can try it and push on it - not because it is proven.

- The automated suite passes 14/14, but those tests only check word counts on fixed example strings. They do not run an agent.
- In the first blind A/B pair (one real public regulatory document, with skill vs without, same model), the with-skill output had cleaner bullet formatting but was slightly *worse* on factual fidelity than the plain baseline. A wider paired test set (two more real documents, with and without the skill) is prepared but currently paused.
- Triggering: the description now carries the pushy sentence described above and `tests/triggering/` ships the firing test pack, but firing has NOT been measured on under50 itself yet. The 15% / 62% figures come from someone else's 26 skills, not this one.
- Under50 is a triage read, not a summary. Non-essential detail is deliberately dropped; never rely on it where the full document matters.

## Why 50 words

50 words is a product rule, not a scientific law. Brysbaert (2019, meta-analysis of 190 studies) puts average adult English nonfiction reading speed at 238 words per minute, so 50 words is roughly a 13-15 second read. Morkes & Nielsen (1997) found the combined concise + scannable + objective rewrite of promotional web prose improved measured usability by 124% (concise wording alone: 58%). Whether those 1997 web-writing results transfer to markdown triage is an assumption, not a tested result. See `references/research.md`.

## Running the tests

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT - see `LICENSE`.

