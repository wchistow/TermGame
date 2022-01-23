class Screen:
    def __init__(self, width=80, height=24, color='\033[1;37m', symbol=' ', bg_color='\033[0;40m'):
        self.width = width
        self.height = height
        self.color = color
        self.symbol = symbol
        self.bg_color = bg_color

        self.start_line = 1

        # Draw empty board
        for y in range(self.height):
            print(f'{self.color}{self.symbol}' * self.width)
