# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_expired_items_degrade_twice_as_fast(self):
        items = [Item("foo", 0, 10)]

        GildedRose(items).update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

if __name__ == '__main__':
    unittest.main()
