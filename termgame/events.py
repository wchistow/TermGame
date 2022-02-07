import atexit
from queue import Queue
import sys
import termios
from threading import Thread

K_a = 97
K_b = 98
K_c = 99
K_d = 100
K_e = 101
K_f = 102
K_g = 103
K_h = 104
K_i = 105
K_j = 106
K_k = 107
K_l = 108
K_m = 109
K_n = 110
K_o = 111
K_p = 112
K_q = 113
K_r = 114
K_s = 115
K_t = 116
K_u = 117
K_v = 118
K_w = 119
K_x = 120
K_y = 121
K_z = 122

K_0 = 48
K_1 = 49
K_2 = 50
K_3 = 51
K_4 = 52
K_5 = 53
K_6 = 54
K_7 = 55
K_8 = 56
K_9 = 57

K_TAB = 9
K_ENTER = 10
K_ESC = 27

K_UP = 'up'
K_DOWN = 'down'
K_RIGHT = 'right'
K_LEFT = 'left'


events = Queue(maxsize=150)


def read():
    try:
        codes = {
            'A': 'up',
            'B': 'down',
            'C': 'right',
            'D': 'left',
        }

        while True:
            try:
                key = sys.stdin.read(1)
                events.put(key)
                if events.qsize() == 3 and events.get() == '\x1b':
                    events.get()
                    events.put(codes[events.get()])
            except KeyError:
                pass
    finally:
        set_normal_term()


def set_normal_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)


def get_events() -> iter:
    for _ in range(events.qsize()):
        yield ord(events.get())


fd = sys.stdin.fileno()
new_term = termios.tcgetattr(fd)
old_term = termios.tcgetattr(fd)

# New terminal setting unbuffered
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)
termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

# Support normal-terminal reset at exit
atexit.register(set_normal_term)

t = Thread(target=read, daemon=True)
t.start()
