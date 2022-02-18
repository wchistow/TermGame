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
 + #### tick (fps: int):
parameters:
 
 + fps - number of frames per second

---

 + #### get_fps ():
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

 + #### join (
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

 + ### Draw

---

### functions:

 + #### symbol (
   x: int, y: int, screen, letter='▇'
#### )

description:

Draws a letter in coordinates (x, y).

parameters:

x, y - coordinates of symbol\
screen - exemplar of class termgame.Screen\
letter - symbol that draws on screen

---

 + #### line (
   x1: int, y1: int, x2: int, y2: int,\
   screen, letter='▇'
   #### )

description:

Draws a line from (x1, y1) to (x2, y2) with symbol letter

parameters:

x1, y1 - coordinates from which draws line\
x2, y2 - coordinates to which draws line\
screen - exemplar of class termgame.Screen\
letter - symbol that draws on screen

---

 + rectangle (
   x, y, width, height, screen,
   outline_letter='▇', fill_letter=' '
   )

description:

Draws a rectangle in coordinates (x, y) with width,
height and outline_letter and fill it with fill_letter.

parameters:

x, y - coordinates from which draws rectangle\
width, height - width and height of rectangle\
screen - exemplar of class termgame.Screen\
outline_letter, fill_letter - outline_letter and
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

matrix - matrix, which one draws\
start_x, start_y - coordinates from which draws matrix\
x1, y1 - coordinates in matrix from which it draws\
x2, y2 - coordinates in matrix to which it draws\
screen - exemplar of class termgame.Screen\
board - dictionary with which replace elements of matrix

---
---
