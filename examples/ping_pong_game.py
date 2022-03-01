import termgame as tg

import time


class Ball:
    def __init__(self, screen):
        self.screen = screen

        self.vx = 1
        self.vy = 1

        self.image = tg.image.Image(screen.width // 2, screen.height // 2,
                                    '●', self.screen, text_color=tg.color.RED)

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


class Paddle:
    def __init__(self, screen):
        self.width = 20

        self.screen = screen

        self.x = screen.width // 2 - self.width // 2
        self.y = screen.height - 10

        self.image = tg.image.Image(self.x, self.y, ' ' * self.width, self.screen,
                                    bg_color=tg.color.BLUE_BG)

    def draw(self):
        self.image.draw()


screen = tg.Screen()
ball = Ball(screen)
paddle = Paddle(screen)

while True:
    screen.empty()

    ball.update()

    paddle.draw()
    ball.draw()

    screen.draw()

    time.sleep(0.05)
