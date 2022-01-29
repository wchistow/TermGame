def symbol(x: int, y: int, screen, letter='▇'):
    screen.board[y][x] = letter


def line(x1: int, y1: int, x2: int, y2: int, screen, letter='▇'):
    dx = abs(max(x1, x2) - min(x1, x2))
    dy = abs(max(y1, y2) - min(y1, y2))
    if dx == 0:
        for y in range(y1, dy + 1):
            symbol(x1, y, screen, letter=letter)
        return
    if dy == 0:
        for x in range(x1, dx + 1):
            symbol(x, y1, screen, letter=letter)
        return
    x, y = x1, y1
    step = round(dy / dx)
    while x != x2 + 1 and y != y2 + 1:
        for _ in range(step):
            if x > x2 and y > y2:
                break
            symbol(x, y, screen, letter=letter)
            y += 1
        x += 1


def rectangle(x, y, width, height, screen, outline_letter='▇', fill_letter=' '):
    line(x, y, x + width + 1, y, screen, letter=outline_letter)
    current_x, current_y = x, y + 1
    for _ in range(height - 2):
        symbol(current_x, current_y, screen, letter=outline_letter)
        current_x += 1
        for _ in range(width - 2):
            symbol(current_x, current_y, screen, letter=fill_letter)
            current_x += 1
        symbol(current_x, current_y, screen, letter=outline_letter)
        current_x = x
        current_y += 1
    line(x, y + height - 1, x + width + 1, y + height - 1, screen, letter=outline_letter)
