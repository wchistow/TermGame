import termgame as tg

import time


class Ball:
    def __init__(self, screen):
        self.screen = screen

        self.vx = 1
        self.vy = 1

        self.image = tg.image.Image(screen.width // 2, screen.height // 2, 'O', self.screen)

    def update(self):
        if self.image.y == 1:
            self.vy = 1
        elif self.image.y == self.screen.height - 1:
            self.vy = -1
        if self.image.x == 1:
            self.vx = 1
        elif self.image.x == self.screen.width - 2:
            self.vx = -1

        self.image.x += self.vx
        self.image.y += self.vy

    def draw(self):
        self.image.draw()


screen = tg.Screen()
ball = Ball(screen)

while True:
    screen.empty()

    ball.update()
    ball.draw()

    screen.draw()

    time.sleep(0.05)
