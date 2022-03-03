# Documentation of TermGame library version 0.1.0

## Module index:
 + ### [clock](https://gitflic.ru/project/wchistow/term-game/blob?file=DOCUMENTATION.md###clock)
 + ### [color](https://gitflic.ru/project/wchistow/term-game/blob?file=DOCUMENTATION.md###color)
 + ### [draw](https://gitflic.ru/project/wchistow/term-game/blob?file=DOCUMENTATION.md###draw)
 + ### [events](https://gitflic.ru/project/wchistow/term-game/blob?file=DOCUMENTATION.md###events)
 + ### [image](https://gitflic.ru/project/wchistow/term-game/blob?file=DOCUMENTATION.md###image)
 + ### [pictures](https://gitflic.ru/project/wchistow/term-game/blob?file=DOCUMENTATION.md###pictures)
 + ### [screen](https://gitflic.ru/project/wchistow/term-game/blob?file=DOCUMENTATION.md###screen)

## Modules:

---
 + ### Clock
### class Clock:

---

#### methods:
 + #### tick (fps: int):
parameters:
 
 + fps -- number of frames per second

---

 + #### get_fps ():
returns:
 
 type: float -- number of frames per second

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

 + #### join (
   symbol: str,\
   arg1: str,\
   arg2=''
#### )
parameters:

 + symbol, arg1, arg2 -- strings

returns:

type: str -- arg1 + arg2 + symbol

---
---

 + ### Draw

---

### functions:

 + #### symbol (
   x: int, y: int, screen, letter='▇'
#### )

description:

Draws a letter in coordinates (x, y).

parameters:

x, y -- coordinates of symbol\
screen -- exemplar of class termgame.Screen\
letter -- symbol that draws on screen

---

 + #### line (
   x1: int, y1: int, x2: int, y2: int,\
   screen, letter='▇'
   #### )

description:

Draws a line from (x1, y1) to (x2, y2) with symbol letter

parameters:

x1, y1 -- coordinates from which draws line\
x2, y2 -- coordinates to which draws line\
screen -- exemplar of class termgame.Screen\
letter -- symbol that draws on screen

---

 + rectangle (
   x, y, width, height, screen,
   outline_letter='▇', fill_letter=' '
   )

description:

Draws a rectangle in coordinates (x, y) with width,
height and outline_letter and fill it with fill_letter.

parameters:

x, y -- coordinates from which draws rectangle\
width, height -- width and height of rectangle\
screen -- exemplar of class termgame.Screen\
outline_letter, fill_letter -- outline_letter and
fill_letter of rectangle

---

 + #### draw_matrix (
   matrix, start_x, start_y,
   x1, y1, x2, y2, screen, board
   #### )

description:

Draws matrix in (start_x, start_y) from (x1, y1) to
(x2, y2) and replace elements with board.

parameters:

matrix -- matrix, which one draws\
start_x, start_y -- coordinates from which draws matrix\
x1, y1 -- coordinates in matrix from which it draws\
x2, y2 -- coordinates in matrix to which it draws\
screen -- exemplar of class termgame.Screen\
board -- dictionary with which replace elements of matrix

---
---

 + ## Events

Warning! In start of programme must use:
```
termgame.events.init()
```

---

### functions:

 + #### get_events ()

description:

Return an iterable object of events.

returns:

type: iter -- an iterable object of events

---


### constants:

K_a\
K_b\
K_c\
K_d\
K_e\
K_f\
K_g\
K_h\
K_i\
K_j\
K_k\
K_l\
K_m\
K_n\
K_o\
K_p\
K_q\
K_r\
K_s\
K_t\
K_u\
K_v\
K_w\
K_x\
K_y\
K_z

K_0\
K_1\
K_2\
K_3\
K_4\
K_5\
K_6\
K_7\
K_8\
K_9

K_TAB\
K_ENTER\
K_ESC

SPACE

K_UP\
K_DOWN\
K_RIGHT\
K_LEFT

---
---

 + ### Image

### class Image

#### methods:
 + #### \_\_init__ (
   x, y, text, screen
   #### )
parameters:

x, y -- coordinates from which draws image\
text -- string, which provides an image\
screen -- exemplar of class termgame.Screen

---

 + #### draw ():
description:
 
Draws attribute text in (self.x, self.y) in screen and
fill spaces with screen's symbol.

---

### functions:

 + #### load(file_name, screen)
description:

Create and return exemplar of class
termgame.image.Image with attribute text from file
with name file_name.

returns:

type: Image -- exemplar of class
termgame.image.Image with attribute text from file
with name file_name.

---
---

 + ## Pictures

This module has some useful pictures:

 + rocket1, rocket2 -- pictures of rockets
 + alien1 -- picture of alien
 + ball -- picture of ball
 + tetraminos -- list of pictures for Tetris game

---
---

 + ## Screen

### class Screen

#### methods:
 + #### \_\_init__ (
   size=None, symbol=' ', color='', bg=''
   #### )
parameters:

size -- size of screen, default = os.get_terminal_size()\
symbol -- symbol, which fill a screen, default -- space\
color -- color of screen, default -- empty\
bg -- background of screen, default -- empty

---

 + #### empty ():
description:
 
Empty attribute board.

---

 + #### draw ():
description:
 
Draws attribute board in screen.

---
---
