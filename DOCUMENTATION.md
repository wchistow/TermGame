# Documentation of TermGame library version beta 0.1.0

## Module index:
 + ### [clock](https://github.com/wchistow/TermGame/blob/master/DOCUMENTATION.md###clock)
 + ### [color](https://github.com/wchistow/TermGame/blob/master/DOCUMENTATION.md###color)
 + ### [draw](https://github.com/wchistow/TermGame/blob/master/DOCUMENTATION.md###draw)
 + ### [events](https://github.com/wchistow/TermGame/blob/master/DOCUMENTATION.md###events)
 + ### [image](https://github.com/wchistow/TermGame/blob/master/DOCUMENTATION.md###image)
 + ### [pictures](https://github.com/wchistow/TermGame/blob/master/DOCUMENTATION.md###pictures)
 + ### [screen](https://github.com/wchistow/TermGame/blob/master/DOCUMENTATION.md###screen)

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
