# Documentation of TermGame library version beta 0.1.0

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
BLACK\
RED\
GREEN\
BRAUN\
BLUE\
PURPLE\
CYAN\
LIGHT_GREY\
DARK_GREY\
LIGHT_RED\
LIGHT_GREEN\
YELLOW\
LIGHT_BLUE\
LIGHT_PURPLE\
LIGHT_CYAN\
WHITE

#### Colors for background:
BLACK_BG\
RED_BG\
GREEN_BG\
BRAUN_BG\
BLUE_BG\
PURPLE_BG\
CYAN_BG\
LIGHT_GREY_BG

#### Reset color and background:
RESET_COLOR

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
