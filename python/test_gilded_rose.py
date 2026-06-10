# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_aged_brie_increases_in_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]

        GildedRose(items).update_quality()

        self.assertEqual(21, items[0].quality)
if __name__ == '__main__':
    unittest.main()
