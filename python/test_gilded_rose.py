# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_aged_brie_increases_in_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]

        GildedRose(items).update_quality()

        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(80, items[0].quality)
if __name__ == '__main__':
    unittest.main()
