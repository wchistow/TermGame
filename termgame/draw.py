from typing import Any


def symbol(x: int, y: int, screen, letter='▇'):
    """Draws a letter in coordinates (x, y)."""
    screen.board[y, x] = letter


def line(x1: int, y1: int, x2: int, y2: int, screen, letter='▇'):
    """Draws a line from (x1, y1) to (x2, y2) with symbol letter"""
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if dx == 0:
        if y2 < y1:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            symbol(x1, y, screen, letter=letter)
        return
    if dy == 0:
        if x2 < x1:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            symbol(x, y1, screen, letter=letter)
        return
    x, y = x1, y1
    step = round(dy / dx)
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1
    while x != x2 + step_x and y != y2 + step_y:
        for _ in range(step):
            if x * step_x > x2 * step_x or y * step_y > y2 * step_y:
                return
            symbol(x, y, screen, letter=letter)
            y += step_y
        x += step_x


def rectangle(x, y, width, height, screen, outline_letter='▇', fill_letter=' '):
    """
    Draws a rectangle in coordinates (x, y) with width, height
    and outline_letter and fill it with fill_letter.
    """
    line(x, y, x + width, y, screen, letter=outline_letter)
    for current_y in range(y + 1, y + height):
        symbol(x, current_y, screen, letter=outline_letter)
        for current_x in range(x + 1, x + width):
            symbol(current_x, current_y, screen, letter=fill_letter)
        symbol(x + width, current_y, screen, letter=outline_letter)
    line(x, y + height, x + width, y + height, screen, letter=outline_letter)


def matrix(drawing_matrix: list[list[Any]],
           start_x: int, start_y: int,
           x1: int, y1: int,
           x2: int, y2: int,
           screen,
           board=None
           ):
    """
    Draws drawing_matrix in (start_x, start_y) from (x1, y1) to
    (x2, y2) and replace elements with board.
    """
    if board is None:
        for line in drawing_matrix:
            board = {s: str(s) for s in set([s for s in line])}

    for y, line in enumerate(drawing_matrix[y1:y2], start_y):
        for x, letter in enumerate(line[x1:x2], start_x):
            if letter in board:
                symbol(x, y, screen, board[letter])
            else:
                symbol(x, y, screen, letter)
