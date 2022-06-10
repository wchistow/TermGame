"""This is tests of module termgame.draw"""
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

    def test_rectangle(self):
        tg.draw.rectangle(0, 0, 5, 5, self.screen, outline_letter='A')

        for y in range(0, 6):
            self.assertEqual(self.screen.board[0, y], 'A')
        for x in range(1, 5):
            self.assertEqual(self.screen.board[x, 0], 'A')
            for y in range(1, 5):
                self.assertEqual(self.screen.board[x, y], ' ')
            self.assertEqual(self.screen.board[x, 5], 'A')
        for y in range(0, 6):
            self.assertEqual(self.screen.board[5, y], 'A')

    def test_matrix(self):
        matrix = [['A' for _ in range(5)] for _ in range(5)]
        tg.draw.matrix(matrix, 0, 0, 0, 0, 5, 5, self.screen)
        for x in range(0, 5):
            for y in range(0, 5):
                self.assertEqual(self.screen.board[x, y], 'A')

    def test_text(self):
        text = 'Hello\nWorld'
        tg.draw.text(text, 0, 0, self.screen)
        for x, letter in zip(range(0, 6), 'Hello'):
            self.assertEqual(self.screen.board[x, 0], letter)
        for x, letter in zip(range(0, 6), 'World'):
            self.assertEqual(self.screen.board[x, 1], letter)
