import termgame as tg

tg.events.init()

running = True

while running:
    for evt in tg.events.get_events():
        if evt == tg.events.K_ESC:
            running = False
            break
        elif evt == tg.events.K_h:
            print('Help')
        else:
            print(tg.events.get_unicode(evt))
