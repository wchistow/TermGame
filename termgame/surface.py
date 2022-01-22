class Screen:
    def __init__(self, width=80, height=24, color='\033[1;37m', symbol=' '):
        self.width = width
        self.height = height

        self.start_line = 1

        # Draw empty board
        for y in range(self.height):
            print(f'{color}{symbol}' * self.width)
