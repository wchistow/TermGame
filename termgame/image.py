from .draw import symbol
from .color import join


class Image:
    def __init__(self, x: int, y: int, text: str, screen):
        self.x = x
        self.y = y
        self.text = text
        self.screen = screen

    def draw(self):
        """
        Draws attribute text in (self.x, self.y) in screen and
        fill spaces with screen's symbol.
        """
        for y, line in enumerate(self.text.splitlines(), self.y):
            for x, letter in enumerate(line, self.x):
                if letter == ' ':
                    symbol(x, y, self.screen, self.screen.symbol)
                else:
                    symbol(x, y, self.screen, join(letter, self.screen.text_color, self.screen.bg))


def load(file_name: str, screen) -> Image:
    """
    Create and return exemplar of class
    termgame.image.Image with attribute text from file
    with name file_name.
    """
    with open(file_name) as f:
        return Image(0, 0, f.read(), screen)
