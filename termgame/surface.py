class Screen:
    def __init__(self, width=80, height=24):
        self.width = width
        self.height = height

        self.start_line = 1

        # Draw empty board
        for y in range(self.height):
            print(' ' * self.width)
