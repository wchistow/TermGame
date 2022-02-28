import termgame as tg

import time


class Ball:
    def __init__(self, screen):
        self.screen = screen

        self.image = tg.image.Image(screen.columns // 2, screen.rows // 2, 'O', self.screen)

    def draw(self):
        self.image.draw()


screen = tg.Screen()
ball = Ball(screen)

while True:
    ball.draw()

    time.sleep(0.05)
