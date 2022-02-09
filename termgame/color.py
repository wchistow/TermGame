# colors for symbols
BLACK = '\033[0;30m'
RED = '\033[0;31m'
GREEN = '\033[0;32m'
BRAUN = '\033[0;33m'
BLUE = '\033[0;34m'
PURPLE = '\033[0;35m'
CYAN = '\033[0;36m'
LIGHT_GREY = '\033[0;37m'
DARK_GREY = '\033[1;30m'
LIGHT_RED = '\033[1;31m'
LIGHT_GREEN = '\033[132m'
YELLOW = '\033[1;33m'
LIGHT_BLUE = '\033[1;34m'
LIGHT_PURPLE = '\033[1;35m'
LIGHT_CYAN = '\033[1;36m'
WHITE = '\033[1;37m'

# colors for background
BLACK_BG = '\033[0;40m'
RED_BG = '\033[0;41m'
GREEN_BG = '\033[0;42m'
BRAUN_BG = '\033[0;43m'
BLUE_BG = '\033[0;44m'
PURPLE_BG = '\033[0;45m'
CYAN_BG = '\033[0;46m'
LIGHT_GREY_BG = '\033[0;47m'

RESET_COLOR = '\033[0m'


def join(symbol: str, arg1: str, arg2='') -> str:
    return arg1 + arg2 + symbol + RESET_COLOR
