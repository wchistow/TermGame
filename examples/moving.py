import termgame as tg

text = '''
 ^
|O|
/|\
'''

screen = tg.Screen()
image = tg.image.Image(5, 5, text, screen)
clock = tg.Clock()

while True:
    screen.empty()
    image.draw()
    screen.draw()
    clock.tick(30)
