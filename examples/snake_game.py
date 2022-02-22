import termgame as tg

import random

screen = tg.Screen()


class Snake:
    def __init__(self):
        self.image = tg.image.Image(screen.columns // 2, screen.rows // 2,
                           tg.color.join(' ', tg.color.GREEN_BG), screen)
        self.heading = 0

    def move(self):
        if self.heading == 0:
            self.image.x += 1
        elif self.heading == 90:
            self.image.y -= 1
        elif self.heading == 180:
            self.image.x -= 1
        elif self.heading == 270:
            self.image.y += 1

    def draw(self):
        self.image.draw()


class Apple:
    def __init__(self):
        self.image = tg.image.Image(0, 0,
                                    tg.color.join(' ', tg.color.RED_BG),
                                    screen)

    def draw(self):
        self.image.draw()


snake = Snake()
apple = Apple()

sts = []
sts_pos = []


def new_stamp():
    sts.append(tg.image.Image(snake.image.x, snake.image.y, '@', screen))
    sts_pos.append((snake.image.x, snake.image.y))


def check_hit_edge():
    if snake.image.x == screen.columns - 1:
        snake.image.x = 1
    elif snake.image.x == 1:
        snake.image.x = screen.columns - 1
    elif snake.image.y == screen.rows - 1:
        snake.image.y = 1
    elif snake.image.y == 1:
        snake.image.y = screen.rows - 1


def check_events():
    for evt in tg.events.get_events():
        if evt == tg.events.K_ESC:
            exit()
        elif evt == tg.events.K_RIGHT:
            snake.heading = 0
        elif evt == tg.events.K_LEFT:
            snake.heading = 180
        elif evt == tg.events.K_UP:
            snake.heading = 90
        elif evt == tg.events.K_DOWN:
            snake.heading = 270


def new_apple():
    apple.x = random.randint(1, screen.columns - 1)
    apple.y =  random.randint(1, screen.rows - 1)
