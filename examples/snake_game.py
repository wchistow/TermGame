import termgame as tg

import random

screen = tg.Screen()


class Snake:
    def __init__(self, x=screen.columns // 2, y=screen.rows // 2):
        self.image = tg.image.Image(x, y, 'S', screen)
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
        self.image = tg.image.Image(0, 0, 'A', screen)

    def draw(self):
        self.image.draw()

tg.events.init()

snake = Snake()
apple = Apple()

sts = []
sts_pos = []


def new_stamp():
    sts.append(Snake(snake.image.x, snake.image.y))
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
    apple.y = random.randint(1, screen.rows - 1)


score = 0
new_apple()

while True:
    check_events()
    check_hit_edge()

    if len(sts) > score * 2:
        sts.pop(0)
        sts_pos.pop(0)
    new_stamp()
    if snake.image.x == apple.image.x and snake.image.y == apple.image.y:
        new_apple()
        score += 1
    snake.move()
    if (snake.image.x, snake.image.y) in sts_pos:
        break

    screen.empty()

    snake.draw()
    apple.draw()
    for s in sts:
        s.draw()

    screen.draw()
