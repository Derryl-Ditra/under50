# Under 50 - Quality Grading, Evaluation, and Scaling Limits (Audited)

Date: 2026-11-03  
Evaluation baseline: Audited against source texts using `word_counter.py` (markers stripped) and raw whitespace tokens (`wc -w`).

---

## 1. Scorecard (Audited)

| Document | Source (Package Counter) | Source (Raw wc -w) | Output Words | Compression | Factual Fidelity | Triage Decision Quality | Grade |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Copper Kettle Bakery** (`dummy-test-200.md`) | 200 words | 204 words | 45 words | 77.5% | Matches source on checked figures | Complete decision-readiness with conditions | **A** |
| **Halcyon Foods** (`dummy-test-1000.md`) | 1,000 words | 1,009 words | 46 words | 95.4% | Matches source on checked figures | Clear primary trade-off and recommendation | **A-** |
| **Northwind Retail** (`dummy-test-10000.md`) | 10,000 words | 10,018 words | 41 words | 99.59% | Matches source on checked figures (after audit fix) | High omission across 16 workstreams; surfaces 4 real decisions | **B** |
| **Northline 10k** (`sample-10000-words.md`) | 10,000 words | 10,058 words | 43 words | 99.57% | Matches source on checked figures | Core macro-decision and baseline savings | **A** |
| **Northline 20k** (`sample-20000-words.md`) | 20,000 words | 20,108 words | 45 words | 99.78% | Matches source on checked figures ($10.79M upfront is in this 20k source) | Full macro-decision and upfront capital commitment | **A** |

---

## 2. Audit Findings & Corrections

An independent factual audit revealed two critical failure modes in the initial drafts:
1. **Source Bleed Across Variants (Northline 10k)**:
   - *Issue*: The initial 10k brief included "$10,790,000 upfront". While this figure is genuine in the 20k report (line 665), it does not appear in the 10k text.
   - *Fix*: The 10k brief was decoupled from the 20k text, reporting only figures present in the 10k source ($157.6M cost, $28.6M savings, 15.4%).
2. **Decision Invention (Northwind Retail)**:
   - *Issue*: The initial brief stated "contract signatures (mid-April/middle of July)". In the source, "contract signature" was a monitored metric, not a requested decision.
   - *Fix*: Replaced with actual named decision requests from the text: operating cash flow (Tomas Beer, mid-May), fill rate (Ana Ruiz, mid-April), conversion/footfall (Ana Ruiz, mid-July), and absence rate (Grace Osei, mid-January).
3. **Source Word Count Discrepancies**:
   - Initial documentation misreported source sizes (e.g. reporting Northwind as 2,608 words instead of 10,000). Both package-counter tokens and raw whitespace counts are now explicitly documented.

---

## 3. What Was Checked vs. What Was Not

- **Checked by the automated suite (14 tests, fixed fixtures only)**:
  - Word counting: whitespace tokens, hyphenated words kept as one, markdown markers excluded.
  - The saved example briefs and depth-mode blocks are within the word limits.
  - The saved prompt-injection fixture strings stay under the limit and contain no embedded command text. These tests do not run an agent.
  - Depth-mode blocks (`test_depth_mode.py`): mergers 50 words, upgrades 44, keep 39. Place names are written in full as in the source (Halden Cross, Pellam Bay, Fenwick Row, Calder Mill).
- **Checked by hand against the source files (static comparison)**: figures, names, owners and dates in the five briefs and the depth-mode blocks.
- **Not tested**:
  - Behavior of an installed agent. No test runs the skill inside an agent, so injection resistance and fidelity of fresh outputs are unproven.
  - Triage quality on documents other than these five samples.
  - Languages other than English and genres other than business/operational text.
- **Limitation**: Default Mode is a triage tool, not an exhaustive summary. Multi-stream documents lose most detail.
