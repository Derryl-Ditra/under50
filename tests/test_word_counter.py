"""Tests for Under 50 word counter and fixtures from research.md."""

import unittest
from word_counter import count_words, extract_tokens


class TestWordCounter(unittest.TestCase):

    def setUp(self):
        # Fixtures directly from research.md
        self.bullet_variant = (
            "- Revenue: +8.4% in Q3; logistics margin down to 11%\n"
            "- Recommendation: fund Route C now, 14-month payback\n"
            "- Fallbacks: Route B contingency, Route A deferred to 2028\n"
            "- Decision: approve Route C budget this quarter, or accept further margin decline\n"
        )
        self.prose_variant = (
            "Q3 revenue grew 8.4% but logistics margin fell to 11%. "
            "Recommendation: fund Route C now (14-month payback), keep Route B as contingency, "
            "defer Route A to 2028. Decision needed: approve the Route C budget this quarter, "
            "or accept further margin decline."
        )

    def test_research_bullet_variant_fixture(self):
        """research.md states: bullet variant counts 9 + 7 + 9 + 12 = 37 words."""
        lines = [l for l in self.bullet_variant.strip().split("\n") if l]
        line_counts = [count_words(line) for line in lines]
        self.assertEqual(line_counts, [9, 7, 9, 12])
        self.assertEqual(count_words(self.bullet_variant), 37)

    def test_research_prose_variant_fixture(self):
        """research.md states: prose variant counts 41 words."""
        self.assertEqual(count_words(self.prose_variant), 41)

    def test_hyphenated_compound_is_single_token(self):
        """Hyphenated compounds like '14-month' or 'cost-effective' count as 1 token."""
        self.assertEqual(count_words("14-month payback"), 2)
        self.assertEqual(count_words("cost-effective real-time monitoring"), 3)

    def test_markdown_markers_excluded(self):
        """Bullet dashes, asterisks, pluses, heading markers, and list numbers are excluded."""
        self.assertEqual(count_words("# Heading"), 1)
        self.assertEqual(count_words("### Sub Heading"), 2)
        self.assertEqual(count_words("- First bullet"), 2)
        self.assertEqual(count_words("* Second bullet"), 2)
        self.assertEqual(count_words("+ Third bullet"), 2)
        self.assertEqual(count_words("1. Ordered item"), 2)
        self.assertEqual(count_words("> Quoted text"), 2)

    def test_under_50_limit_assertion(self):
        """Output emitted under default mode must not exceed 50 tokens."""
        self.assertLessEqual(count_words(self.bullet_variant), 50)
        self.assertLessEqual(count_words(self.prose_variant), 50)

    def test_example_triage_under_50(self):
        """Verify the real example triage briefs stay strictly under 50 words."""
        example_bullet = (
            "- Finding: 50-word cap is a product rule for ~15-second triage, not scientific optimum\n"
            "- Evidence: Brysbaert (2019) adult reading average is 238 wpm; Morkes-Nielsen (1997) shows concise text boosts usability 58%\n"
            "- Default format: single core brief <= 50 words, verbatim numbers/names, bullets\n"
            "- Decision: approve v1 build defaults and packaging\n"
        )
        example_prose = (
            "Research establishes 50 words as a product design choice for a 15-second triage read "
            "(Brysbaert 2019 adult average: 238 wpm). Combined concise, scannable, objective style "
            "improves usability by 124% (Morkes & Nielsen 1997). Build defaults: one core brief under 50 "
            "words with verbatim figures. Decision: approve v1 build package."
        )
        self.assertEqual(count_words(example_bullet), 48)
        self.assertLessEqual(count_words(example_bullet), 50)
        self.assertEqual(count_words(example_prose), 49)
        self.assertLessEqual(count_words(example_prose), 50)


if __name__ == "__main__":
    unittest.main()
