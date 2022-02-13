import termgame as tg

import time
import unittest


class ClockTestCase(unittest.TestCase):
    def setUp(self):
        self.testing_clock = tg.Clock()

    def test_tick(self):
        start = time.time()
        for _ in range(30):
            self.testing_clock.tick(30)
        finish = time.time()
        self.assertEqual(round(finish - start), 1)

    def test_get_fps(self):
        self.testing_clock.tick(30)
        self.assertEqual(self.testing_clock.get_fps(), 30.0)
