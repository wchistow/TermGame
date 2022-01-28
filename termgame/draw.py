def symbol(x: int, y: int, screen, letter='▇'):
    screen.board[y][x] = letter


def line(x1: int, y1: int, x2: int, y2: int, screen, letter='▇'):
    dx = abs(max(x1, x2) - min(x1, x2))
    dy = abs(max(y1, y2) - min(y1, y2))
    if dx == 0:
        for y in range(dy):
            symbol(x1, y, screen, letter=letter)
        return
    if dy == 0:
        for x in range(dx):
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
