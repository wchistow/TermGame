"""This is tests of module termgame.events"""
import termgame as tg

import unittest


class EventsTestCase(unittest.TestCase):
    def test_getting_events(self):
        tg.events.events.put('a')
        self.assertEqual([tg.events.K_a], list(tg.events.get_events()))
