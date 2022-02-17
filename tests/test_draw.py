import termgame as tg

import unittest


class DrawTestCase(unittest.TestCase):
    def setUp(self):
        self.screen = tg.Screen()

    def test_symbol(self):
        tg.draw.symbol(0, 0, self.screen, 'A')
        self.assertEqual(self.screen.board[0, 0], 'A')

    def test_line(self):
        tg.draw.line(0, 0, 0, 10, self.screen, 'A')
        for y in range(0, 11):
            self.assertEqual(self.screen.board[0, y], 'A')
