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
        self.height, self.width = size

        self.empty()

    def empty(self):
        """Empty attribute board."""
        self.board = Matrix(self.height, self.width, self.symbol)

        for y in range(self.height):
            for x in range(self.width - 1):
                self.board[y, x] = self.symbol
            self.board[y, self.width - 1] = '\n'

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
        """Item must be y, x."""
        col, row = item
        s = row * self.width + col
        return self.board[s]

    def __setitem__(self, key: tuple[int, int], value):
        """Key must be y, x."""
        row, col = key
        s = row * self.width + col
        self.board[s] = value
