import atexit
import sys
import termios
import signal

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

SPACE = 32

K_UP = 128
K_DOWN = 129
K_RIGHT = 130
K_LEFT = 131


def _non_blocking_input():
    class StopInput(Exception):
        pass

    def handler(*args):
        raise StopInput()

    buffer = []
    old_handler = signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 0.01)

    while True:
        try:
            buffer.append(sys.stdin.read(1))
        except StopInput:
            break

    signal.signal(signal.SIGALRM, old_handler)
    return buffer


def _clear_escape(buffer):
    codes = {
        'A': K_UP,
        'B': K_DOWN,
        'C': K_RIGHT,
        'D': K_LEFT,
    }
    i = 0
    while i < len(buffer):
        if buffer[i] == '\033' and i < len(buffer) - 2 and buffer[i + 1] == '[':
            yield codes[buffer[i + 2]]
            i += 3
        else:
            yield ord(buffer[i])
            i += 1


def get_events() -> iter:
    """Return an iterable object of events."""
    buffer = _non_blocking_input()
    yield from _clear_escape(buffer)


def init():
    def set_normal_term():
        """Set terminal mode to normal."""
        termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

    fd = sys.stdin.fileno()
    new_term = termios.tcgetattr(fd)
    old_term = termios.tcgetattr(fd)

    # New terminal setting unbuffered
    new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

    # Support normal-terminal reset at exit
    atexit.register(set_normal_term)
