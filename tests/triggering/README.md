# Trigger test pack: does under50 fire at all?

Measures whether an agent loads the under50 skill when it should, using the
equivalence-class method from "A Session-Start Hook Raised Claude Code Skill
Firing From 15% to 62%" (Towards Data Science, 2026-11-10:
https://towardsdatascience.com/a-session-start-hook-raised-claude-code-skill-firing-from-15-to-62/).

In that experiment (1,872 runs, 26 public skills, Haiku/Sonnet/Opus 5.5):

- Direct requests in the skill's own words fired the target 49% of the time.
- Indirect requests (same need, none of the skill's words) fired 15%.
- A "pushy" description sentence added ~5 points on indirect requests.
- A session-start hook telling the agent to check skills first raised indirect
  firing to 62%.
- Near-miss requests (share a word, need a different job) never fired the target.

## Prompt classes (`prompts.json`)

- `direct` (4): use the skill's own words. Should fire.
- `indirect` (6): same need, no shared content words. Should fire.
- `near_miss` (6): share a word (markdown, document, 50 words, decision) but
  ask for a different job. Should stay quiet.
- `control` (2): unrelated. No skill should load.

## Run it

Requires the Claude Code CLI with usage billing (the experiment's runs cost
about 2 cents each; the full matrix below is 144 runs, roughly $3 and a few
minutes). On free/limited Claude, run one model and fewer reps instead.

```bash
cd tests/triggering
python3 run_trigger_test.py --model haiku --model sonnet --model opus --runs 3
```

Each run is one `claude -p` call in a throwaway git repo holding only this
skill, scored on the agent's FIRST tool call: a run fires when that call loads
under50. Raw results append to `trigger_results.jsonl`; a per-class fire-rate
table prints at the end.

To compare descriptions (old vs pushy), run once against the previous SKILL.md:

```bash
git show HEAD~1:SKILL.md > /tmp/SKILL.old.md
python3 run_trigger_test.py --model sonnet --runs 3 --skill-path /tmp/SKILL.old.md --out results_old.jsonl
python3 run_trigger_test.py --model sonnet --runs 3 --out results_new.jsonl
```

## Honest limits (from the same source)

- Three runs per cell detect only big differences; the experiment itself missed
  its own 10-point bar for the pushy sentence with 6 skills.
- Numbers move with model and CLI versions. Rerun after any model, description
  or harness change.
- This measures firing, not output quality. The word-count A/B fidelity test
  in the main README is a separate, still-open question.
