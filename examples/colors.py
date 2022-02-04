import termgame as tg

screen = tg.Screen()

for x, name in enumerate(dir(tg.color), 2):
    if not name.startswith('__') and not name == 'join':
        symbol = tg.color.join('A ', eval('tg.color.' + name))
        tg.draw.symbol(x, 2, screen, symbol)

screen.draw()
