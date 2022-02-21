from .draw import symbol


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
        in_image = False

        for y, line in enumerate(self.text.splitlines(), self.y):
            for x, letter in enumerate(line, self.x):
                if letter == ' ' and in_image:
                    in_image = False
                elif letter != ' ':
                    in_image = True

                if not in_image:
                    symbol(x, y, self.screen, self.screen.symbol)
                else:
                    symbol(x, y, self.screen, self.screen.bg + self.screen.text_color + letter)


def load(file_name: str, screen) -> Image:
    """
    Create and return exemplar of class
    termgame.image.Image with attribute text from file
    with name file_name.
    """
    with open(file_name) as f:
        return Image(0, 0, f.read(), screen)
