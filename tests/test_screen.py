"""This is tests of module termgame.screen"""
import termgame as tg

import unittest


class ScreenTestCase(unittest.TestCase):
    def setUp(self):
        self.screen = tg.Screen()

    def test_empty(self):
        tg.draw.rectangle(0, 0, 5, 5, self.screen, fill_letter='A')

        self.screen.empty()

        for y in range(self.screen.rows):
            for x in range(self.screen.columns):
                self.assertIn(self.screen.board[x, y], [' ', '\n'])
