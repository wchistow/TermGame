from os import get_terminal_size
from sys import stdout


class Screen:
    def __init__(self, symbol=' ', color='\033[0;30m', bg=''):
        self.bg = bg
        self.text_color = color
        self.symbol = bg + color + symbol

        self.board = []
        self.empty()

    def empty(self):
        self.board = []
        size = get_terminal_size()
        self.rows, self.columns = size.lines + 1, size.columns
        for _ in range(self.rows):
            self.board.append([self.symbol] * self.columns)

    def draw(self):
        stdout.write(f'\033[{len(self.board)}A')  # move cursor to (0,0)
        stdout.write('\n'.join(''.join(row) for row in self.board))
