"""Test Depth Mode expansion blocks on Northline 20k document."""

import unittest
from word_counter import count_words

class TestDepthMode(unittest.TestCase):

    def setUp(self):
        self.block_mergers = (
            "### Mergers (9 depots into 4 hubs)\n"
            "- Action: Merge 9 depots into 4 hubs (15,770 pallets/week added to Eastmoor, Halden Cross, Pellam Bay, Ravenport)\n"
            "- Scope: Marrow Lane, Vesper Row, Juniper Quay, Fenwick Row, Calder Mill, Ashgrove, Larkspur, Oakhaven, Underhill\n"
            "- Wave 1 (leases to 2029): 7 depots, 12,450 pallets/week, $4,224,000 one-off cost"
        )
        self.block_upgrades = (
            "### Upgrades (5 depots in place)\n"
            "- Action: Upgrade Ironbridge, Kestrel Hill, Quillon, Stonecross, Wrenford in place ($3,474,000 capital)\n"
            "- Economics: Recovers capital via 12% lower operating costs and error rates below 1.8% to 3.6%\n"
            "- Constraints: Stonecross and Kestrel Hill exceed 100km hub distance limit, preventing merger"
        )
        self.block_keep = (
            "### Keep (6 depots unchanged)\n"
            "- Action: Retain Brackwater, Dunmere, Garrow Point, Nettlefold, Rookery Bend, Thornley as is\n"
            "- Reason: Upgrades miss 3.5% hurdle; Garrow Point exceeds 100km cold-chain transfer limit\n"
            "- Watch item: Review when leases approach 2030-2034; track error rates quarterly"
        )

    def test_each_depth_block_under_50_tokens(self):
        self.assertEqual(count_words(self.block_mergers), 50)
        self.assertLessEqual(count_words(self.block_mergers), 50)
        self.assertEqual(count_words(self.block_upgrades), 44)
        self.assertLessEqual(count_words(self.block_upgrades), 50)
        self.assertEqual(count_words(self.block_keep), 39)
        self.assertLessEqual(count_words(self.block_keep), 50)

    def test_total_depth_mode_exceeds_50_tokens_as_expected(self):
        total = count_words(self.block_mergers) + count_words(self.block_upgrades) + count_words(self.block_keep)
        self.assertGreater(total, 50)

if __name__ == "__main__":
    unittest.main()
