from os import get_terminal_size
from sys import stdout


class Screen:
    """Provides screen of game."""
    def __init__(self, size=None, symbol=' ', color='', bg=''):
        self.bg = bg
        self.text_color = color
        self.symbol = bg + color + symbol

        if size is None:
            s = get_terminal_size()
            size = s.lines - 1, s.columns
        self.rows, self.columns = size

        self.board = Matrix(self.rows, self.columns, self.symbol)

    def empty(self):
        """Empty attribute board."""
        for y in range(self.rows):
            for x in range(self.columns - 1):
                self.board[y, x] = self.symbol
            self.board[y, self.columns - 1] = '\n'

    def draw(self):
        """Draws attribute board in screen."""
        stdout.write(f'\033[{self.board.height}A')  # move cursor to (0,0)
        stdout.write(''.join(self.board.board))


class Matrix:
    """Provides matrix with using simple list."""
    def __init__(self, height, width, symbol):
        self.height = height
        self.width = width

        self.board = [symbol] * width * height

    def __getitem__(self, item: tuple[int, int]):
        col, row = item
        s = row * self.width + col
        return self.board[s]

    def __setitem__(self, key: tuple[int, int], value):
        row, col = key
        s = row * self.width + col
        self.board[s] = value
