# Contributing to Under50

Under50 is an experimental personal project. Contributions are welcome - especially real-world failure cases.

## The most useful contribution: failure reports

If Under50 produced a bad brief, open an issue with:
- the document you triaged (or a link, if it is public - please do not post private or licensed documents),
- the output you got,
- what was wrong: wrong fact, lost core message, invented action, wrong date association, over-50 words,
- the tool and model you used (e.g. Gemini Flash, Claude Sonnet).

Keep private documents private: describe the failure pattern instead of pasting the text.

## Code and prompt changes

1. Fork the repo and create a branch.
2. Run the tests before and after your change:
   `python3 -m unittest discover -s tests -v`
   All 14 must pass. The suite checks word counts on fixed fixtures; if your change alters an example brief, keep the word count at or under 50.
3. Open a pull request describing what changed and why.

## Ground rules

- Honest claims only. Do not describe the skill as accurate, proven, or production-ready in docs or comments. If you ran a real with/without-skill comparison, say exactly what you ran.
- Changes to `SKILL.md` wording are product changes: expect discussion before merge.
- No tracking, analytics, network calls, or external dependencies in `word_counter.py`.
- By contributing, you agree your contribution is published under the repo's license.
