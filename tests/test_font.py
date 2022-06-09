"""This is tests of module termgame.font"""
import termgame as tg

import random
import string
import unittest


class FontTestCase(unittest.TestCase):
    def test_join_func(self):
        for s1 in random.sample(string.printable, 10):
            for s2 in random.sample(string.printable, 10):
                self.assertEqual(tg.font.join(s1, s2), s2 + s1 + tg.font.RESET_FONT)
