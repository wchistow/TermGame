"""This is tests of module termgame.image"""
import termgame as tg

from os import remove
import unittest


class ImageTestCase(unittest.TestCase):
    def setUp(self):
        self.screen = tg.Screen()
        self.img = tg.image.Image(0, 0, ' A ', self.screen)

    def test_class_image(self):
        self.img.draw()

        self.assertEqual(self.screen.board[0, 0], ' ')
        self.assertEqual(self.screen.board[1, 0], 'A')
        self.assertEqual(self.screen.board[2, 0], ' ')

    def test_collide_point(self):
        self.assertTrue(self.img.collide_point(1, 0))

    def test_collide_image(self):
        test_img = tg.image.Image(1, 0, 'A', self.screen)

        self.assertTrue(self.img.collide_image(test_img))

    def test_func_load(self):
        with open('some_test.txt', 'w') as f:
            f.write('A')

        img = tg.image.load('some_test.txt', self.screen)

        self.assertEqual(img.text, 'A')

        remove('some_test.txt')
