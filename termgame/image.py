from . import draw


class Image:
    def __init__(self, x: int, y: int, text: str, screen):
        self.x = x
        self.y = y
        self.text = text
        self.screen = screen

    def draw(self):
        pass
