from os import get_terminal_size
from sys import stdout


class Screen:
    def __init__(self, symbol=' ', bg_color='\033[0;40m'):
        self.symbol = symbol
        self.bg_color = bg_color

        self.board = []

        size = get_terminal_size()
        self.rows, self.columns = size.lines - 1, size.columns - 1
        for _ in range(self.rows):
            self.board.append([self.symbol] * self.columns)

    def draw(self):
        stdout.write(f'\033[{len(self.board)}A')  # move cursor to (0,0)
        stdout.write('\n'.join(''.join(row) for row in self.board))
