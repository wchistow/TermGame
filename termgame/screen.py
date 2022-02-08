from os import get_terminal_size
from sys import stdout


class Screen:
    def __init__(self, symbol=' ', color='', bg=''):
        self.bg = bg
        self.text_color = color
        self.symbol = bg + color + symbol

        size = get_terminal_size()
        self.rows, self.columns = size.lines + 1, size.columns

        self.board = UTF32Matrix(self.rows, self.columns)
        self.empty()

    def empty(self):
        for y in range(self.rows):
            for x in range(self.columns):
                self.board[x, y] = self.symbol
            self.board[self.columns, y] = '\n'

    def draw(self):
        stdout.write(f'\033[{self.board.height}')  # move cursor to (0,0)
        stdout.write(self.board.board.decode('utf-32'))


class UTF32Matrix:
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.board = bytearray([0] * width * height * 4)

    def __getitem__(self, item: tuple[int, int]):
        col, row = item
        s = row * self.width + col
        return self.board[s * 4 : s * 4 + 4].decode('utf-32')

    def __setitem__(self, key, value):
        row, col = key
        s = row * self.width + col
        self.board[s * 4: s * 4 + 4] = value.encode('utf-32')[4:]
