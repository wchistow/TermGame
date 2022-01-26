import curses


class Game:
    def __init__(self, width=80, height=24, color='\033[0;31m', symbol=' ', bg_color='\033[0;40m'):
        self.width = width
        self.height = height
        self.color = color
        self.symbol = symbol

        self.bg_color = bg_color

        self.board = ''

        self.tasks = []

    def add_task(self, task: callable):
        self.tasks.append(task)

    def remove_task(self, task: callable):
        if task in self.tasks:
            self.tasks.remove(task)

    def create_screen(self):
        for y in range(self.height):
            self.board += self.symbol * self.width + '\n'

    def run(self):
        curses.wrapper(self._run)

    def _run(self, canvas: curses.window):
        canvas.nodelay(True)
        curses.curs_set(0)

        while True:
            rows_number, columns_number = canvas.getmaxyx()
            pressed_key_code = canvas.getch()

            if pressed_key_code == 27:  # Escape
                return

            for row, line in enumerate(self.board.splitlines()):
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

            for task in self.tasks:
                task(canvas)
