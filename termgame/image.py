from .draw import symbol
from .color import WHITE


class Image:
    def __init__(self, x: int, y: int, text: str, screen):
        self.x = x
        self.y = y
        self.text = text
        self.screen = screen

    def draw(self):
        in_image = False

        for y, line in enumerate(self.text.splitlines(), self.y - 1):
            for x, letter in enumerate(line, self.x):
                if letter == ' ' and in_image:
                    in_image = False
                elif letter != ' ':
                    in_image = True

                if not in_image:
                    symbol(x, y, self.screen, self.screen.symbol)
                else:
                    symbol(x, y, self.screen, self.screen.bg + WHITE + letter)
