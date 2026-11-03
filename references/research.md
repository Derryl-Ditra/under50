# Under 50 - Research: word limit, grouping, and format

Date: 2026-11-03. Status: research before build. Purpose: decide whether the Under 50 concept (compress any markdown document to a 50-word core) has a defensible basis, how to group output, and what format best supports understanding.

Scope note: six sources reviewed on 2026-11-03. When this document says a source does or does not show something, it means within these reviewed sources; that is not proof about the whole literature. Research findings and design judgment are labeled separately throughout.

---

## The questions

1. Is a 50-word limit scientifically correct?
2. One 50-word summary of the whole document, or split per batch/topic?
3. What output format best supports human understanding?

---

## What the reviewed sources say

### A. Reading speed

Brysbaert (2019), meta-analysis of 190 studies with 18,573 participants: adults read English nonfiction at an average of 238 words per minute, most within 175-300 wpm.
https://doi.org/10.1016/j.jml.2019.104047

Computed reading times at 238 wpm:
- 50 words: about 13 seconds
- 100 words: about 25 seconds
- 300 words: about 76 seconds
- 2,000 words: about 8.4 minutes
- 2,437 words (our test report): about 10.2 minutes

Supports: a 50-word brief is roughly a 13-second read, so "done in about 20 seconds" is a defensible estimate.
The reviewed sources do not establish any attention or comprehension threshold in words. 238 wpm is a speed measure, nothing more.

### B. Scanning behavior and concise writing

Nielsen Norman Group analysis of 59,573 natural page views: an estimate from visit durations that users had time to read at most 28% of the words on an average page. Caveat: this is derived from page-view times, not observed comprehension, and describes web browsing, not universal reading behavior.
https://www.nngroup.com/articles/how-little-do-users-read/

Morkes and Nielsen (1997), 51 users tested 5 versions of the same content in different writing styles: concise text scored 58% higher in measured usability, scannable text 47% higher, and the combined concise + scannable + objective version 124% higher than control. Context: web content, 1997, one small study; transferring it to markdown triage is an assumption, not a tested result.
https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/

Supports: in that experiment, concise and scannable writing measurably outperformed the promotional prose control. This is the most direct support found for the Under 50 premise.

### C. Working memory (listed for completeness, not a basis for block rules)

Cowan (2001), Behavioral and Brain Sciences: working memory holds about 4 chunks at once.
https://www.cambridge.org/core/journals/behavioral-brain-sciences/article/magical-number-4-in-shortterm-memory-a-reconsideration-of-mental-storage-capacity/44023F1147D4A1D44BDC0AD226838496

This concerns holding items in mind from memory, not reading reference material on screen. It provides no rule for how many output blocks a summary should have, and this document does not use it as one.

### D. Signaling in learning materials

Schneider et al. (2018), meta-analysis of 103 studies with 12,201 participants: signaling - cues that highlight the organization of relevant information, such as headings and summaries - improved retention (g+ = 0.53) and transfer (g+ = 0.33) and reduced cognitive load. Context: learning with media (study materials), not markdown decision triage.
https://www.sciencedirect.com/science/article/abs/pii/S1747938X17300581

Supports, with that context caveat: organizational cues helped learners in the reviewed evidence. It does not prove headings improve arbitrary documents.

### E. Information overload framing

Eppler and Mengis (2004), cross-disciplinary review: overload occurs when information processing requirements exceed capacity; filtering and condensing are standard countermeasures.
https://doi.org/10.1080/01972240490507974

Supports: the problem framing (daily reading volume exceeds capacity). It offers no word limits.

---

## Answers

### 1. Is 50 words scientifically correct?

The reviewed sources do not establish an optimal summary length, and nothing reviewed gives 50 a special status. It is a design constraint: about 13 seconds at the average reading speed in A, and consistent in spirit with the concise-writing result in B.

Honest claim for the product: "50 words is a product rule chosen for a roughly 15-second read." Not: "science says 50 words."

### 2. One core brief, or per-topic blocks?

The tradeoff is coverage against speed. Note that a percentage of words retained measures length, not semantic coverage: a 50-word core can triage a long document without covering it, and you have explicitly accepted that omission tradeoff. Length alone does not prove the cap breaks down.

Two modes compared (design judgment, not an empirically optimal answer):

- Default mode: one core brief of 50 words or fewer TOTAL per document - the point, the decisive numbers, the action needed. Fastest; coverage deliberately sacrificed; matches the Under 50 name and your stated goal.
- Depth mode (on request only): per-topic expansion blocks of 50 words or fewer each. Total then exceeds 50 words: a core plus 5 blocks is 300 words, about 76 seconds at 238 wpm - no longer a 20-second read.

Recommendation: default to the core of 50 words or fewer in total, with depth only when asked. Baking expansion into the default would silently break the promise.

### 3. Format for understanding

- Conclusion first, details after (design standard, consistent with the scanning behavior in B).
- Numbers and names carried verbatim, never rephrased into different figures (design judgment: compression must not alter facts).
- Bullets: one idea per line, no sub-bullets (design judgment informed by the scannability result in B).
- Prose cores as one or two short declarative sentences (reasoned design judgment: fragments can drop the relation between facts; this is not an empirical absolute).
- Organizational cues (a heading per block) plausibly help, per D, but that evidence is from learning media and is not proven for arbitrary markdown.
- Mapping each compressed element back to its source location is my proposal, not a user requirement. It gives a one-step "did I miss something" check.
- Comparing bullets vs prose below: bullets suit decision triage (scan, pick the action); short prose suits cases where the relationship between facts matters (learning). Default for Under 50, given your stated triage goal: bullets.

### 4. What the reviewed sources do not test

- No reviewed source tests 50 vs 100 vs 150-word summaries for decision triage.
- The studies above are English-language, in web or multimedia-learning contexts. Bahasa Indonesia reading behavior may differ.

---

## Example output (illustrative; content invented for this document, not from a real report)

Word count method: whitespace-separated tokens (a hyphenated compound like 14-month counts as one token); markdown bullet markers excluded. Counts below were computed by script on the exact text shown.

Core, bullets (37 words):

- Revenue: +8.4% in Q3; logistics margin down to 11%
- Recommendation: fund Route C now, 14-month payback
- Fallbacks: Route B contingency, Route A deferred to 2028
- Decision: approve Route C budget this quarter, or accept further margin decline

Core, prose (41 words):

Q3 revenue grew 8.4% but logistics margin fell to 11%. Recommendation: fund Route C now (14-month payback), keep Route B as contingency, defer Route A to 2028. Decision needed: approve the Route C budget this quarter, or accept further margin decline.

Both variants state the same four facts (per-line bullet counts: 9 + 7 + 9 + 12 = 37). The difference is shape, not coverage: bullets separate the facts for scanning, prose keeps the relations between them.

---

## Proposed pilot (a pilot, not general proof)

Take 10 of your real agent-generated markdown files, produce the core output for each, and measure:
1. Time to state the document's point and its decision, compared to reading the original.
2. Missed items: after answering from the compressed version, check the original and count anything that would have changed your action.

Limitations to state up front: one reader, practice and order effects across 10 documents, and results describe your use only. "Near zero missed items" is a weak criterion unless you decide beforehand which items count as important. A good pilot for your own decision would not be evidence the format works for knowledge workers generally.

---

## Sources

- Brysbaert (2019), reading-rate meta-analysis: https://doi.org/10.1016/j.jml.2019.104047
- NN/g, How Little Do Users Read: https://www.nngroup.com/articles/how-little-do-users-read/
- Morkes and Nielsen (1997), concise/scannable usability study: https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/
- Cowan (2001), working memory capacity: https://www.cambridge.org/core/journals/behavioral-brain-sciences/article/magical-number-4-in-shortterm-memory-a-reconsideration-of-mental-storage-capacity/44023F1147D4A1D44BDC0AD226838496
- Schneider et al. (2018), signaling meta-analysis: https://www.sciencedirect.com/science/article/abs/pii/S1747938X17300581
- Eppler and Mengis (2004), information overload review: https://doi.org/10.1080/01972240490507974
