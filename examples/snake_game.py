import termgame as tg

import time
import random

screen = tg.Screen()


class Snake:
    def __init__(self, x=screen.width // 2, y=screen.height // 2):
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


class ScoreBoard:
    def draw(self):
        tg.draw.symbol(0, 0, screen, str(score))


tg.events.init()

snake = Snake()
apple = Apple()

sts = []
sts_pos = []


def new_stamp():
    sts.append(Snake(snake.image.x, snake.image.y))
    sts_pos.append((snake.image.x, snake.image.y))


def check_hit_edge():
    if snake.image.x == screen.width - 1:
        game_over()
    elif snake.image.x == 1:
        game_over()
    elif snake.image.y == screen.height - 1:
        game_over()
    elif snake.image.y == 1:
        game_over()


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
            snake.heading = 0
        elif evt == tg.events.K_LEFT:
            snake.heading = 180
        elif evt == tg.events.K_UP:
            snake.heading = 90
        elif evt == tg.events.K_DOWN:
            snake.heading = 270
        elif evt == tg.events.SPACE:
            new_apple()


def new_apple():
    apple.image.x = random.randint(1, screen.width - 1)
    apple.image.y = random.randint(1, screen.height - 1)


score = 0
score_board = ScoreBoard()

new_apple()

while True:
    check_events()
    check_hit_edge()

    if len(sts) > score:
        sts.pop(0)
        sts_pos.pop(0)
    new_stamp()
    if snake.image.collide_point(apple.image.x, apple.image.y):
        score += 1
        new_apple()
    snake.move()
    if (snake.image.x, snake.image.y) in sts_pos:
        break

    screen.empty()

    snake.draw()
    apple.draw()
    score_board.draw()

    for s in sts:
        s.draw()

    screen.draw()

    time.sleep(0.05)
