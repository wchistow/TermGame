# Documentation of TermGame library version alpha 0.1.0

## Module index:
 + ### [clock](https://github.com/wchistow/TermGame/DOCUMENTATION.md###Clock)
 + ### [color](https://github.com/wchistow/TermGame/DOCUMENTATION.md###Color)
 + ### [draw](https://github.com/wchistow/TermGame/DOCUMENTATION.md###Draw)
 + ### [events](https://github.com/wchistow/TermGame/DOCUMENTATION.md###Events)
 + ### [image](https://github.com/wchistow/TermGame/DOCUMENTATION.md###Image)
 + ### [screen](https://github.com/wchistow/TermGame/DOCUMENTATION.md###Screen)

## Modules:

---
 + ### Clock
### class Clock:

---

#### methods:
 + #### tick(fps: int):
parameters:
 
 + fps - number of frames per second

---

 + #### get_fps():
returns:
 
 type: float - number of frames per second

---
---

 + ### Color

### constants:

#### Colors for text:
BLACK = '\033[0;30m'\
RED = '\033[0;31m'\
GREEN = '\033[0;32m'\
BRAUN = '\033[0;33m'\
BLUE = '\033[0;34m'\
PURPLE = '\033[0;35m'\
CYAN = '\033[0;36m'\
LIGHT_GREY = '\033[0;37m'\
DARK_GREY = '\033[1;30m'\
LIGHT_RED = '\033[1;31m'\
LIGHT_GREEN = '\033[132m'\
YELLOW = '\033[1;33m'\
LIGHT_BLUE = '\033[1;34m'\
LIGHT_PURPLE = '\033[1;35m'\
LIGHT_CYAN = '\033[1;36m'\
WHITE = '\033[1;37m'

#### Colors for background:
BLACK_BG = '\033[0;40m'\
RED_BG = '\033[0;41m'\
GREEN_BG = '\033[0;42m'\
BRAUN_BG = '\033[0;43m'\
BLUE_BG = '\033[0;44m'\
PURPLE_BG = '\033[0;45m'\
CYAN_BG = '\033[0;46m'\
LIGHT_GREY_BG = '\033[0;47m'

#### Reset color and background:
RESET_COLOR = '\033[0m'

---
### functions:

 + #### join(
   symbol: str,\
   arg1: str,\
   arg2=''
#### )
parameters:

 + symbol, arg1, arg2 - strings

returns:

type str - symbol + arg1 + arg2

---
---
