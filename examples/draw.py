"""Simple graphic example."""
import termgame as tg
import random

screen = tg.Screen()

tg.draw.symbol(3, 3, screen)
tg.draw.line(15, 20, 10, 0, screen)
tg.draw.line(30, 13, 45, 28, screen)
tg.draw.line(20, 1, 30, 1, screen)
tg.draw.rectangle(20, 20, 10, 10, screen)

matrix = [[random.randint(0, 1) for _ in range(16)] for _ in range(11)]

tg.draw_matrix(matrix, 35, 3, 0, 0, 15, 10, screen, {0: 'A', 1: 'B'})

screen.draw()
