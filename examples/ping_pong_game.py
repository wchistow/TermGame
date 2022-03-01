import termgame as tg

import time


class Ball:
    def __init__(self, screen, paddle):
        self.screen = screen
        self.paddle = paddle

        self.vx = 1
        self.vy = 1

        self.image = tg.image.Image(screen.width // 2, screen.height // 2,
                                    '●', self.screen, text_color=tg.color.RED)

    def update(self):
        if self.image.y == 1:
            self.vy = 1
        elif self.image.y == self.screen.height - 1:
            game_over()
        if self.image.x == 1:
            self.vx = 1
        elif self.image.x == self.screen.width - 2:
            self.vx = -1

        if self.image.y == self.paddle.image.y - 1 and \
                self.image.x in range(self.paddle.image.x, self.paddle.image.x + self.paddle.width):
            self.vy = -1

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


def game_over():
    screen.empty()

    text = '''
       _____                         ____
      / ____|                       / __ \\
     | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ ____
     | | |_ |/ _` | '_ ` _ \\ / _ \\ | | |  | \\ \\ / / _ \\ '__|
     | |__| | (_| | | | | | |  __/ | |__| |\\ V /  __/ |
      \\_____|\\__,_|_| |_| |_|\\___|  \\____/  \\_/ \\___|_|
    '''

    tg.draw.symbol(screen.width // 2, screen.height // 2, screen, text)

    screen.draw()

    exit()


def check_events():
    for evt in tg.events.get_events():
        if evt == tg.events.K_ESC:
            game_over()
        elif evt == tg.events.K_RIGHT:
            if paddle.image.x < (screen.width - 2) - paddle.width:
                paddle.image.x += 3
        elif evt == tg.events.K_LEFT:
            if paddle.image.x > 3:
                paddle.image.x -= 3


tg.events.init()

screen = tg.Screen()
paddle = Paddle(screen)
ball = Ball(screen, paddle)

while True:
    check_events()

    screen.empty()

    ball.update()

    paddle.draw()
    ball.draw()

    screen.draw()

    time.sleep(0.05)
