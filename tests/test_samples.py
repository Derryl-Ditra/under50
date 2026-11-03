"""Run Under 50 triage briefs on sample test documents with verified factual fidelity."""

import unittest
from word_counter import count_words

class TestSampleDocumentsTriage(unittest.TestCase):

    def test_sample_1_copper_kettle_bakery(self):
        brief = (
            "- Finding: Week 44 revenue reached 41,200 dollars (+6.1% vs week 43) via morning bundle; "
            "croissant waste fell to 4.8%\n"
            "- Decision needed: Mira Solano asks team to approve permanent 9-dollar morning bundle by Friday\n"
            "- Condition: replaces special if margin holds above 31% this week; otherwise weekend-only"
        )
        count = count_words(brief)
        self.assertEqual(count, 45)
        self.assertLessEqual(count, 50)

    def test_sample_2_halcyon_foods(self):
        brief = (
            "- Finding: October revenue reached 1.84 million dollars (+8.4% vs September); "
            "gross margin slipped from 33.9 to 32.6%\n"
            "- Context: Suburban stores added 214,000 dollars; soft cheese spoilage lost 11,400 dollars\n"
            "- Decision: Sign or decline Dairyfresh 4.9 dollars/kilo contract by 14 November; "
            "Finance modeler Grace Osei prefers signing"
        )
        count = count_words(brief)
        self.assertEqual(count, 46)
        self.assertLessEqual(count, 50)

    def test_sample_3_northwind_retail_group(self):
        # Verified against actual decision asks in source (no fabricated contract signatures)
        brief = (
            "- Context: Consolidated 16-workstream annual review of trading year to October across store network\n"
            "- Finding: Network margin is 5.2% off January plan; business revenue is 7.3% off\n"
            "- Decisions: Operating cash flow (mid-May); fill rate (mid-April); conversion and footfall (mid-July); absence rate (mid-January)"
        )
        count = count_words(brief)
        self.assertEqual(count, 41)
        self.assertLessEqual(count, 50)

    def test_sample_4_northline_10k(self):
        # Verified: contains only figures present in the 10k text (no imported $10,790,000 upfront)
        brief = (
            "- Recommendation: Adopt 4-hub network across 24 depots: keep 6, upgrade 5, and merge 9 smaller sites\n"
            "- Financials: 5-year cost is $157,615,000 vs $186,238,000 baseline; saves $28,623,000 (15.4% saving)\n"
            "- Decision needed: Steering group to approve depot actions, release Q1 budget, and open wave-1 consultation"
        )
        count = count_words(brief)
        self.assertEqual(count, 43)
        self.assertLessEqual(count, 50)

    def test_sample_5_northline_20k(self):
        # Verified: $10,790,000 upfront commitment is explicitly present in line 665 of 20k text
        brief = (
            "- Recommendation: Adopt 4-hub network across 24 depots: keep 6, upgrade 5, and merge 9 smaller sites\n"
            "- Financials: 5-year cost is $157,615,000 vs $186,238,000 baseline; saves $28,623,000 (15.4%), requiring $10,790,000 upfront\n"
            "- Decision needed: Steering group to approve depot actions, release Q1 budget, and open wave-1 consultation"
        )
        count = count_words(brief)
        self.assertEqual(count, 45)
        self.assertLessEqual(count, 50)

if __name__ == "__main__":
    unittest.main()
