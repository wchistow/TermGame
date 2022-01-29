"""Simple graphic example."""

import termgame as tg

screen = tg.Screen()

tg.draw.symbol(3, 3, screen)
tg.draw.line(15, 20, 10, 0, screen)
tg.draw.line(30, 10, 45, 25, screen)
tg.draw.line(20, 5, 30, 5, screen)
tg.draw.rectangle(20, 20, 10, 10, screen)

screen.draw()
