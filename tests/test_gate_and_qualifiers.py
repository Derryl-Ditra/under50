"""Gate self-check and qualifier preservation cases for Under 50 triage briefs.

Extends the fixed-example suite: verifies the word-count gate can fail as
well as pass, and that curated briefs preserve scope qualifiers ("only",
"not yet") and permission limits, not just the headline and word count.
These are fixed examples; they do not test live model output.
"""

import unittest
from word_counter import count_words

MAX_WORDS = 50


class TestGateSelfCheck(unittest.TestCase):
    """A gate is only trusted if it can fail as well as pass."""

    def test_gate_flags_known_overlength_brief(self):
        # Known failure case: deliberately over the 50 token cap.
        brief = (
            "- Finding: Week 44 revenue reached 41,200 dollars after the morning bundle launch across all stores "
            "while croissant waste fell to 4.8% and suburban locations added 214,000 dollars in new sales\n"
            "- Decision needed: Mira Solano asks the full leadership team to approve the permanent 9-dollar "
            "morning bundle by Friday and release the Q1 marketing budget"
        )
        self.assertGreater(count_words(brief), MAX_WORDS)

    def test_gate_admits_clean_brief(self):
        # Clean case: within the cap, figure and decision preserved.
        brief = (
            "- Finding: Week 44 revenue reached 41,200 dollars (+6.1% vs week 43)\n"
            "- Decision: approve the permanent 9-dollar morning bundle by Friday"
        )
        self.assertLessEqual(count_words(brief), MAX_WORDS)


class TestQualifierPreservation(unittest.TestCase):
    """Briefs must keep qualifiers that limit scope, status or permission."""

    def test_only_scope_limit_preserved(self):
        brief = (
            "- Offer: free tier covers 3 projects only; team plan starts at 12 dollars monthly\n"
            "- Decision: confirm whether the pilot fits the free tier"
        )
        self.assertLessEqual(count_words(brief), MAX_WORDS)
        self.assertIn("only", brief)

    def test_not_yet_status_preserved(self):
        brief = (
            "- Status: regulator filing submitted but not yet approved; no launch date committed\n"
            "- Decision: hold the launch announcement"
        )
        self.assertLessEqual(count_words(brief), MAX_WORDS)
        self.assertIn("not yet", brief)

    def test_permission_limit_preserved(self):
        brief = (
            "- Access: contractor may view Q3 revenue figures but not payroll data\n"
            "- Decision: approve the Q3 share before Friday"
        )
        self.assertLessEqual(count_words(brief), MAX_WORDS)
        self.assertIn("not payroll", brief)


if __name__ == "__main__":
    unittest.main()
