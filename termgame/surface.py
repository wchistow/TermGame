import curses


class Screen:
    def __init__(self, width=80, height=24, color='\033[0;31m', symbol=' ', bg_color='\033[0;40m'):
        self.width = width
        self.height = height
        self.color = color
        self.symbol = symbol
        self.bg_color = bg_color

        self.board = ''

        for y in range(self.height):
            for x in range(self.width):
                self.board += self.symbol
            self.board += '\n'

        curses.wrapper(self.draw, self.board)

    def draw(self, canvas, text):
        rows_number, columns_number = canvas.getmaxyx()

        while True:
            pressed_key_code = canvas.getch()
            if pressed_key_code == 27:
                return

            for row, line in enumerate(text.splitlines()):
                if row >= rows_number:
                    break

                for column, symbol in enumerate(line):
                    if column >= columns_number:
                        break

                    if symbol == ' ':
                        continue

                    if row == rows_number - 1 and column == columns_number - 1:
                        continue

                    canvas.addch(row, column, symbol)
