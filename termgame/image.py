from .draw import symbol
from .color import join


class Image:
    def __init__(self, x: int, y: int, text: str, screen, text_color='', bg_color=''):
        self.x = x
        self.y = y
        self.width = max([len(line) for line in text.splitlines()])
        self.height = len(text.splitlines())

        self.text = text
        self.screen = screen
        self.text_color = text_color
        self.bg_color = bg_color

    def collide_point(self, x: int, y: int) -> bool:
        """Return True if point (x, y) collide with image, else False."""
        if x in range(self.x, self.x + self.width + 1) and y in range(self.y, self.y + self.height + 1):
            return True
        return False

    def collide_image(self, image) -> bool:
        """Return True if image collide with an image, to that this function, else False."""
        if set(range(self.x, self.x + self.width + 1)) | set(range(image.x, image.x + image.width + 1)) != set():
            if set(range(self.y, self.y + self.height + 1)) | set(range(image.y, image.y + image.height + 1)) != set():
                return True
        return False

    def draw(self):
        """
        Draws attribute text in (self.x, self.y) in screen and
        fill spaces with screen's symbol.
        """
        for y, line in enumerate(self.text.splitlines(), self.y):
            for x, letter in enumerate(line, self.x):
                symbol(x, y, self.screen, join(letter, self.text_color, self.bg_color))


def load(file_name: str, screen) -> Image:
    """
    Create and return exemplar of class
    termgame.image.Image with attribute text from file
    with name file_name.
    """
    with open(file_name) as f:
        return Image(0, 0, f.read(), screen)
