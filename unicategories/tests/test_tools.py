
import sys
import unittest

import unicategories as module
import unicategories.tools as tools


class Test(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(
            tools.merge(((0, 5), (0, 5), (1, 1), (1, 4), (8, 8))),
            ((0, 5), (8, 8))
            )

    def test_merge_categories(self):
        self.assertEqual(
            tools.merge(*tools.generate().values()),
            ((0, sys.maxunicode + 1),)
            )

    def test_public_api(self):
        self.assertIs(
            module.merge,
            tools.merge
            )
        self.assertIs(
            module.RangeGroup,
            tools.RangeGroup
            )

    def test_iterators(self):
        r = tools.RangeGroup(((1, 2), (3, 10)))
        i = [1, 3, 4, 5, 6, 7, 8, 9]
        self.assertListEqual(list(r.codes()), i)
        self.assertListEqual(list(r.characters()), list(map(chr, i)))

    def test_has(self):
        r = tools.RangeGroup(((1, 2), (3, 10)))
        self.assertFalse(r.has(0))
        self.assertTrue(r.has(1))
        self.assertFalse(r.has(2))
        self.assertTrue(r.has(3))
        self.assertFalse(r.has(10))

    def test_mul(self):
        r = tools.RangeGroup(((1, 2), (3, 10)))
        self.assertEqual(r*2, r)

    def test_add(self):
        r = tools.RangeGroup(((1, 2), (3, 10)))
        b = tools.RangeGroup(((1, 2),)) \
            + tools.RangeGroup(((3, 5),)) \
            + tools.RangeGroup(((4, 10),))
        self.assertEqual(r, b)

    def test_repr(self):
        self.assertTrue(repr(tools.RangeGroup()).startswith('RangeGroup('))
