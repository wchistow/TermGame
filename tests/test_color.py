import termgame as tg

import random
import string
import unittest


class ColorTestCase(unittest.TestCase):
    def test_color_func_join_with_2_args(self):
        for s1 in random.sample(string.printable, 10):
            for s2 in random.sample(string.printable, 10):
                self.assertEqual(tg.color.join(s1, s2), s2 + s1 + tg.color.RESET_COLOR)

    def test_color_func_join_with_3_args(self):
        s1, s2 = [random.choice(string.printable) for _ in range(2)]
        for s3 in random.sample(string.printable, 10):
            self.assertEqual(tg.color.join(s1, s2, s3), s2 + s3 + s1 + tg.color.RESET_COLOR)
