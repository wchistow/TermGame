"""This is tests of module termgame.events"""
import termgame as tg

import random
import unittest


class EventsTestCase(unittest.TestCase):
    def test_get_unicode_of_event(self):
        for _ in range(100):
            n = random.randint(0, 10**5)
            self.assertEqual(tg.events.get_unicode(n), chr(n))
