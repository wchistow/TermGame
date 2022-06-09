import termgame as tg

screen = tg.Screen()

for x, name in enumerate(dir(tg.font), 2):
    if not name.startswith('__') and name != 'join':
        symbol = tg.font.join('A', eval('tg.font.' + name)) + ' '  # Draw symbol "A" with all kinds of fonts
        tg.draw.symbol(x, 2, screen, symbol)                       # from module termgame.font.

screen.draw()
